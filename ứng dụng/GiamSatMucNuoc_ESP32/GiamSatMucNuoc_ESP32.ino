/*
 * BÀI TOÁN ỨNG DỤNG MỤC 4: GIÁM SÁT MỨC VÀ THỂ TÍCH BÌNH CHAI 2L
 * Chạy trên ESP32 DevKit bằng Arduino IDE (C/C++)
 *
 * Sơ đồ đấu nối chân ESP32 (Chuẩn Bảng mở rộng Shield G-V-S):
 *  - RCWL-1601 : VCC -> 3.3V/5V (Hàng V), GND -> GND (Hàng G)
 *                TRIG -> GPIO 5 (Hàng S), ECHO -> GPIO 18 (Hàng S)
 *  - DHT11     : VCC -> 3.3V (Hàng V), GND -> GND (Hàng G)
 *                DATA -> GPIO 4 (Hàng S)
 *  - LED Đỏ    : Anode (+) -> Trở 220Ω -> GPIO 21 (Hàng S), Cathode (-) -> GND (Hàng G)
 *  - LED Xanh  : Anode (+) -> Trở 220Ω -> GPIO 19 (Hàng S), Cathode (-) -> GND (Hàng G)
 */

#include <DHT.h>

#define PIN_TRIG        5
#define PIN_ECHO        18
#define PIN_DHT         4
#define PIN_LED_RED     21
#define PIN_LED_GREEN   19

#define DHTTYPE DHT11
DHT dht(PIN_DHT, DHTTYPE);

// Thông số bình chai 2L
const float H_TONG = 22.0;       // Tổng chiều cao cảm biến tới đáy bình (cm)
const float H_BINH = 17.0;       // Chiều cao thân chai (cm)
const float BAN_KINH_R = 5.0;    // Bán kính đáy bình (cm) (D = 10.0 cm)
const float S_BASE = 78.5398;    // Diện tích đáy bình ≈ 78.54 cm²

// Sai số thành phần theo ISO/GUM
const float U_R = 0.04;          // Sai số thước kẹp cơ khí (cm)
const float U_H = 0.071;         // Sai số đo mức nước RCWL-1601 từ Chương 3 (cm)

// Ngưỡng cảnh báo an toàn (cm)
const float TH_CAN_KHAN_CAP   = 2.5;   // Low-Low
const float TH_CANH_BAO_CAN    = 5.0;   // Low
const float TH_TRAN_KHAN_CAP  = 14.0;  // High-High

// Bộ đệm cho chuỗi lọc thích nghi 2 tầng
float buf_iqr[5];
int count_iqr = 0;
float buf_ma[7];
int count_ma = 0;

float current_temp_c = 27.0;
unsigned long last_dht_time = 0;
int pump_state = 0; // 0: Tắt, 1: Bật (chế độ giám sát)

void setup() {
  Serial.begin(115200);
  delay(1000);

  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  digitalWrite(PIN_TRIG, LOW);

  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  digitalWrite(PIN_LED_RED, LOW);
  digitalWrite(PIN_LED_GREEN, LOW);

  dht.begin();
  Serial.println(F("{\"status\":\"ESP32 Level & Volume Monitor Initialized\"}"));
}

// Bù nhiệt độ Laplace: v(T) = 331.3 + 0.606 * T (cm/us)
float get_sound_speed_cm_us(float temp_c) {
  float speed_m_s = 331.3 + 0.606 * temp_c;
  return speed_m_s / 10000.0;
}

// Đo khoảng trống d(t) từ cảm biến đến mặt nước
float read_distance_cm() {
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);

  long duration = pulseIn(PIN_ECHO, HIGH, 30000); // Timeout 30ms (~5m)
  if (duration <= 0) return -1.0;

  float v_cm_us = get_sound_speed_cm_us(current_temp_c);
  float dist_cm = (duration * v_cm_us) / 2.0;

  if (dist_cm < 2.0 || dist_cm > 400.0) return -1.0;
  return dist_cm;
}

// Chuỗi lọc thích nghi 2 tầng (IQR + Moving Average)
float filter_2_stages(float raw_val) {
  if (raw_val < 0) return (count_ma > 0) ? buf_ma[count_ma - 1] : 0.0;

  // TẦNG 1: Lọc IQR (W=5)
  if (count_iqr < 5) {
    buf_iqr[count_iqr++] = raw_val;
  } else {
    for (int i = 0; i < 4; i++) buf_iqr[i] = buf_iqr[i + 1];
    buf_iqr[4] = raw_val;
  }

  float stage1_val = raw_val;
  if (count_iqr == 5) {
    float temp_sort[5];
    for (int i = 0; i < 5; i++) temp_sort[i] = buf_iqr[i];
    // Sắp xếp đơn giản 5 phần tử
    for (int i = 0; i < 4; i++) {
      for (int j = i + 1; j < 5; j++) {
        if (temp_sort[i] > temp_sort[j]) {
          float t = temp_sort[i]; temp_sort[i] = temp_sort[j]; temp_sort[j] = t;
        }
      }
    }
    float q25 = temp_sort[1];
    float q75 = temp_sort[3];
    float iqr = q75 - q25;
    float med = temp_sort[2];
    if (raw_val < q25 - 1.5 * iqr || raw_val > q75 + 1.5 * iqr) {
      stage1_val = med; // Khử xung ngoại lai bọt khí
    }
  }

  // TẦNG 2: Moving Average (W=7)
  if (count_ma < 7) {
    buf_ma[count_ma++] = stage1_val;
  } else {
    for (int i = 0; i < 6; i++) buf_ma[i] = buf_ma[i + 1];
    buf_ma[6] = stage1_val;
  }

  float sum = 0;
  for (int i = 0; i < count_ma; i++) sum += buf_ma[i];
  return sum / count_ma;
}

// Tính độ không đảm bảo đo mở rộng U_95%(V) (mL) theo ISO/GUM
float calc_uncertainty_U95(float h) {
  float c_R = 2.0 * PI * BAN_KINH_R * h;
  float c_h = S_BASE;
  float u_c = sqrt(sq(c_R * U_R) + sq(c_h * U_H));
  return 2.0 * u_c; // k = 2
}

void loop() {
  // Cập nhật nhiệt độ phòng mỗi 1 giây
  if (millis() - last_dht_time >= 1000) {
    last_dht_time = millis();
    float t = dht.readTemperature();
    if (!isnan(t) && t > 0 && t < 60) {
      current_temp_c = t;
    }
  }

  // Đo cự ly ToF và tính mức nước h
  float d_raw = read_distance_cm();
  float h_raw = -1.0;
  if (d_raw > 0) {
    h_raw = H_TONG - d_raw;
    if (h_raw < 0) h_raw = 0;
    if (h_raw > H_BINH) h_raw = H_BINH;
  }

  // Lọc số 2 tầng thích nghi
  float h_filtered = filter_2_stages(h_raw);
  float V_ml = S_BASE * h_filtered;
  float U95_ml = calc_uncertainty_U95(h_filtered);

  // Kịch bản phân 4 cấp cảnh báo trực quan bằng LED Đỏ và LED Xanh
  String state_str = "NORMAL";
  if (h_filtered <= TH_CAN_KHAN_CAP) {
    state_str = "CAN_KHAN_CAP";
    pump_state = 0;
    digitalWrite(PIN_LED_RED, HIGH);
    digitalWrite(PIN_LED_GREEN, LOW);
  } else if (h_filtered <= TH_CANH_BAO_CAN) {
    state_str = "CANH_BAO_CAN";
    pump_state = 1;
    digitalWrite(PIN_LED_RED, HIGH);
    digitalWrite(PIN_LED_GREEN, LOW);
  } else if (h_filtered >= TH_TRAN_KHAN_CAP) {
    state_str = "TRAN_KHAN_CAP";
    pump_state = 0;
    // Nhấp nháy LED Đỏ liên tục khi nguy cơ tràn bồn
    digitalWrite(PIN_LED_RED, (millis() / 250) % 2 == 0 ? HIGH : LOW);
    digitalWrite(PIN_LED_GREEN, LOW);
  } else {
    state_str = "BINH_THUONG";
    pump_state = 0;
    digitalWrite(PIN_LED_RED, LOW);
    digitalWrite(PIN_LED_GREEN, HIGH);
  }

  // Xuất gói JSON Telemetry qua Serial
  Serial.print(F("{\"T\":")); Serial.print(current_temp_c, 1);
  Serial.print(F(",\"h_raw\":")); Serial.print(h_raw, 2);
  Serial.print(F(",\"h\":")); Serial.print(h_filtered, 2);
  Serial.print(F(",\"V\":")); Serial.print(V_ml, 1);
  Serial.print(F(",\"U95\":")); Serial.print(U95_ml, 1);
  Serial.print(F(",\"pump\":")); Serial.print(pump_state);
  Serial.print(F(",\"state\":\"")); Serial.print(state_str);
  Serial.println(F("\"}"));

  delay(50); // Tần số lấy mẫu 20 Hz (50 ms)
}
