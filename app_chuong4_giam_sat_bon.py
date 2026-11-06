"""
HỆ THỐNG GIÁM SÁT MỨC VÀ THỂ TÍCH CHẤT LỎNG THÔNG MINH BÌNH CHAI 2L
Chạy trên ESP32 bằng MicroPython (Module điều khiển thực thi Chương 4)

Kết nối phần cứng:
  1. Cảm biến siêu âm RCWL-1601:
     - VCC -> 3.3V hoặc 5V (khuyên dùng 3.3V trên ESP32 để an toàn chân logic)
     - GND -> GND
     - TRIG -> GPIO 5
     - ECHO -> GPIO 18
  2. Cảm biến nhiệt độ DHT11 (bù vận tốc âm Laplace):
     - VCC -> 3.3V, GND -> GND, DATA -> GPIO 4
  3. Module Relay điều khiển bơm mini 6V:
     - IN -> GPIO 23 (Kích mức LOW hoặc HIGH tùy module relay)
  4. Còi báo Buzzer 5V:
     - Chân (+) -> GPIO 22, Chân (-) -> GND
  5. Đèn chỉ thị LED:
     - LED Đỏ (Cảnh báo nguy cấp): Anode -> Điện trở 220Ω -> GPIO 21, Cathode -> GND
     - LED Xanh (Bình thường an toàn): Anode -> Điện trở 220Ω -> GPIO 19, Cathode -> GND
"""

import time
import math
from machine import Pin, time_pulse_us
import dht


# ==========================================================
# 1. CÁC THÔNG SỐ HÌNH HỌC VÀ ĐO LƯỜNG CỦA MÔ HÌNH CHAI 2L
# ==========================================================
H_TONG = 22.0          # Tổng chiều cao từ cảm biến tới đáy bình (cm)
H_BINH = 17.0          # Chiều cao hữu dụng của thân chai 2L (cm)
H_GA = 5.0             # Chiều cao giá gá cảm biến cách ly miệng chai (cm)
BAN_KINH_R = 5.0       # Bán kính bình trụ tròn (cm) (Đường kính D = 10.0 cm)
S_BASE = math.pi * (BAN_KINH_R ** 2)  # Diện tích đáy bình ≈ 78.54 cm²

# Độ không đảm bảo đo chuẩn thành phần (ISO/GUM)
U_R = 0.04             # Sai số đo bán kính bằng thước kẹp cơ khí (cm)
U_H = 0.071            # Sai số đo mức nước cảm biến siêu âm từ Chương 3 (cm)

# Các ngưỡng cảnh báo và điều khiển (cm)
NGUONG_TRAN_KHAN_CAP = 14.0   # High-High (cm) -> Ngắt bơm chống tràn
NGUONG_CANH_BAO_CAN  = 5.0    # Low (cm)       -> Bật bơm bù nước
NGUONG_CAN_KHAN_CAP  = 2.5    # Low-Low (cm)   -> Khóa bơm chống cháy


# ==========================================================
# 2. KHỞI TẠO PHẦN CỨNG NGOẠI VI
# ==========================================================
pin_trig = Pin(5, Pin.OUT, value=0)
pin_echo = Pin(18, Pin.IN)
pin_dht = Pin(4, Pin.IN, Pin.PULL_UP)
sensor_dht = dht.DHT11(pin_dht)

pin_relay = Pin(23, Pin.OUT, value=1)  # Relay thường ngắt ở mức HIGH (Active LOW)
pin_buzzer = Pin(22, Pin.OUT, value=0) # Buzzer kêu ở mức HIGH
pin_led_red = Pin(21, Pin.OUT, value=0)
pin_led_green = Pin(19, Pin.OUT, value=0)

# Trạng thái điều khiển bơm (0: Tắt, 1: Bật)
trang_thai_bom = 0
last_dht_read_ms = 0
current_temp_c = 27.0  # Nhiệt độ phòng mặc định 27°C


# ==========================================================
# 3. CÁC HÀM XỬ LÝ ĐO LƯỜNG VÀ BÙ NHIỆT ĐỘ LAPLACE
# ==========================================================
def cap_nhat_nhiet_do():
    """Đọc nhiệt độ từ DHT11 mỗi 1 giây để cập nhật v(T)."""
    global current_temp_c, last_dht_read_ms
    now = time.ticks_ms()
    if last_dht_read_ms == 0 or time.ticks_diff(now, last_dht_read_ms) >= 1000:
        try:
            sensor_dht.measure()
            current_temp_c = float(sensor_dht.temperature())
            last_dht_read_ms = now
        except Exception:
            pass  # Nếu lỗi giữ nguyên nhiệt độ gần nhất
    return current_temp_c

def tinh_van_toc_am(temp_c):
    """v(T) = 331.3 + 0.606 * T (cm/us)."""
    speed_m_s = 331.3 + 0.606 * temp_c
    return speed_m_s / 10000.0  # cm/us

def doc_khoang_trong_cm():
    """Đo khoảng cách trống d(t) từ RCWL-1601 đến mặt nước (cm)."""
    temp_c = cap_nhat_nhiet_do()
    v_cm_us = tinh_van_toc_am(temp_c)
    
    # Phát xung Trigger 10us
    pin_trig.value(0)
    time.sleep_us(2)
    pin_trig.value(1)
    time.sleep_us(10)
    pin_trig.value(0)
    
    # Đọc độ rộng xung Echo (chờ tối đa 30,000 us ~ 5 mét)
    duration_us = time_pulse_us(pin_echo, 1, 30000)
    if duration_us <= 0:
        return None  # Timeout hoặc lỗi
    
    d_cm = (duration_us * v_cm_us) / 2.0
    return d_cm


# ==========================================================
# 4. CHUỖI LỌC SỐ THÍCH NGHI 2 TẦNG (IQR + MOVING AVERAGE)
# ==========================================================
buffer_iqr = []    # Cửa sổ trượt tầng 1 (N = 5 mẫu)
buffer_ma = []     # Cửa sổ trượt tầng 2 (W = 7 mẫu)

def loc_thich_nghi_2_tang(val_raw):
    """
    Tầng 1: Lọc phi tuyến IQR (N = 5) loại xung gai bọt khí.
    Tầng 2: Lọc tuyến tính Moving Average (W = 7) làm phẳng sóng gợn.
    """
    global buffer_iqr, buffer_ma
    if val_raw is None:
        if len(buffer_ma) > 0:
            return buffer_ma[-1]
        return 0.0

    # --- TẦNG 1: LỌC KHOẢNG TỨ PHÂN VỊ (IQR) ---
    buffer_iqr.append(val_raw)
    if len(buffer_iqr) > 5:
        buffer_iqr.pop(0)

    if len(buffer_iqr) < 5:
        val_stage1 = val_raw
    else:
        sorted_win = sorted(buffer_iqr)
        q25 = sorted_win[1]
        q75 = sorted_win[3]
        iqr = q75 - q25
        median = sorted_win[2]
        
        # Nếu là ngoại lai (vượt ngoài [Q1 - 1.5*IQR, Q3 + 1.5*IQR]) thay bằng Median
        if val_raw < (q25 - 1.5 * iqr) or val_raw > (q75 + 1.5 * iqr):
            val_stage1 = median
        else:
            val_stage1 = val_raw

    # --- TẦNG 2: LỌC TRUNG BÌNH TRƯỢT (MOVING AVERAGE) ---
    buffer_ma.append(val_stage1)
    if len(buffer_ma) > 7:
        buffer_ma.pop(0)

    val_filtered = sum(buffer_ma) / len(buffer_ma)
    return val_filtered


# ==========================================================
# 5. TÍNH ĐỘ KHÔNG ĐẢM BẢO ĐO THEO ISO/GUM
# ==========================================================
def tinh_do_khong_dam_bao_do(h_cm):
    """Tính độ không đảm bảo đo mở rộng U_95%(V) (mL) với k = 2."""
    c_R = 2.0 * math.pi * BAN_KINH_R * h_cm
    c_h = S_BASE
    u_c_V = math.sqrt(((c_R * U_R) ** 2) + ((c_h * U_H) ** 2))
    U_95_V = 2.0 * u_c_V  # Hệ số phủ k = 2 (Độ tin cậy 95%)
    return U_95_V


# ==========================================================
# 6. GIẢI THUẬT ĐIỀU KHIỂN BƠM 6V & PHÂN 4 CẤP CẢNH BÁO
# ==========================================================
def cap_nhat_dieu_khien(h_cm, V_ml):
    """
    Phân cấp 4 ngưỡng an toàn và kịch bản vận hành bơm có trễ logic:
    - h <= 2.5 cm : Cạn khẩn cấp (Ngắt bơm, LED Đỏ nhấp nháy, Còi BEEP)
    - 2.5 < h <= 5: Cảnh báo cạn (Bật bơm nạp, LED Vàng/Đỏ nhẹ)
    - 5 < h < 14  : Bình thường  (LED Xanh sáng, Còi tắt)
    - h >= 14.0 cm: Tràn khẩn cấp (Cắt relay ngắt bơm, Còi hú, LED Đỏ sáng)
    """
    global trang_thai_bom
    cap_do = "NORMAL"

    if h_cm <= NGUONG_CAN_KHAN_CAP:
        cap_do = "CAN_KHAN_CAP"
        trang_thai_bom = 0
        pin_relay.value(1)       # Ngắt bơm chống cháy
        pin_led_red.value(1)
        pin_led_green.value(0)
        pin_buzzer.value(1)      # Kêu còi báo động
        time.sleep_ms(50)
        pin_buzzer.value(0)

    elif h_cm <= NGUONG_CANH_BAO_CAN:
        cap_do = "CANH_BAO_CAN"
        # Cơ chế trễ: khi tụt dưới 5cm thì kích hoạt bơm nạp
        trang_thai_bom = 1
        pin_relay.value(0)       # Bật relay bơm 6V (Active LOW)
        pin_led_red.value(1)
        pin_led_green.value(0)
        pin_buzzer.value(0)

    elif h_cm >= NGUONG_TRAN_KHAN_CAP:
        cap_do = "TRAN_KHAN_CAP"
        trang_thai_bom = 0
        pin_relay.value(1)       # Ngắt relay bơm lập tức
        pin_led_red.value(1)
        pin_led_green.value(0)
        pin_buzzer.value(1)      # Hú còi cảnh báo tràn

    else:
        # Vùng bình thường (5.0 < h < 14.0 cm)
        cap_do = "BINH_THUONG"
        # Giữ nguyên trạng thái bơm đang nạp cho tới khi đầy 14cm
        pin_led_red.value(0)
        pin_led_green.value(1)
        pin_buzzer.value(0)

    return cap_do


# ==========================================================
# 7. VÒNG LẶP CHÍNH THỜI GIAN THỰC (MAIN LOOP)
# ==========================================================
def main():
    print("=" * 60)
    print("HE THONG GIAM SAT MUC VA THE TICH CHAI 2L - RCWL-1601")
    print(f"Chieu cao tong: {H_TONG} cm | Duong kinh: {BAN_KINH_R*2} cm")
    print("=" * 60)
    
    sample_count = 0
    while True:
        try:
            d_raw = doc_khoang_trong_cm()
            if d_raw is not None:
                # Tính mức nước thô: h_raw = H_tong - d_raw
                h_raw = H_TONG - d_raw
                if h_raw < 0:
                    h_raw = 0.0
                if h_raw > H_BINH:
                    h_raw = H_BINH
            else:
                h_raw = None

            # Qua chuỗi lọc 2 tầng (IQR + Moving Average)
            h_filtered = loc_thich_nghi_2_tang(h_raw)

            # Tính thể tích V và độ không đảm bảo đo U_95%
            V_tuc_thoi = S_BASE * h_filtered
            U_95 = tinh_do_khong_dam_bao_do(h_filtered)

            # Điều khiển bơm và cảnh báo
            trang_thai = cap_nhat_dieu_khien(h_filtered, V_tuc_thoi)

            sample_count += 1
            # Xuất gói tin Telemetry chuẩn JSON qua Serial (để PC hoặc Dashboard đọc)
            print(
                f'{{"sample": {sample_count}, "T": {current_temp_c:.1f}, '
                f'"h_raw": {h_raw if h_raw is not None else -1:.2f}, '
                f'"h": {h_filtered:.2f}, "V": {V_tuc_thoi:.1f}, '
                f'"U95": {U_95:.1f}, "pump": {trang_thai_bom}, "state": "{trang_thai}"}}'
            )

        except Exception as e:
            print(f"[Loi he thong]: {e}")

        # Chu kỳ lấy mẫu 50 ms (tần số quét 20 Hz)
        time.sleep_ms(50)


if __name__ == "__main__":
    main()
