"""
GIAO DIỆN & BỘ TEST GIÁM SÁT MỰC NƯỚC BÌNH CHAI 2L TRÊN MÁY TÍNH (PYTHON)
Học phần: Kỹ thuật đo lường và cảm biến (EMA2024E_3) - Báo cáo Chương 4

Chức năng:
  - Kết nối Serial với ESP32 (MicroPython hoặc Arduino C++).
  - Tự động chuyển sang CHẾ ĐỘ MÔ PHỎNG (Simulation) nếu chưa cắm phần cứng ESP32.
  - Hiển thị đồ thị thời gian thực (Live Dashboard) với:
      + Đồ thị 1: Mức nước h_raw vs h_lọc và các ngưỡng cảnh báo an toàn.
      + Đồ thị 2: Thể tích chất lỏng V(t) kèm dải phủ bóng tin cậy mở rộng V ± U_95%(V).
  - Tự động ghi dữ liệu vào tệp CSV: result_test_ung_dung.csv
"""

import sys
import time
import json
import math
import random
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cố gắng import pyserial
try:
    import serial
    import serial.tools.list_ports
    HAS_SERIAL = True
except ImportError:
    HAS_SERIAL = False
    print("[Lưu ý]: Chưa cài thư viện 'pyserial'. Chạy lệnh: pip install pyserial")

# ==========================================
# CẤU HÌNH THÔNG SỐ HỆ THỐNG
# ==========================================
PORT = "COM3"          # Thay đổi cổng COM của ESP32 (ví dụ: COM3, COM4, /dev/ttyUSB0)
BAUDRATE = 115200
TIMEOUT = 0.5
CSV_FILE = Path(r"D:\đo lường\thực hành đo lường\RCWL1601\result_test_ung_dung.csv")

# ==========================================
# KHỞI TẠO KẾT NỐI SERIAL HOẶC MÔ PHỎNG
# ==========================================
ser = None
mode_simulation = False

if HAS_SERIAL:
    available_ports = [p.device for p in serial.tools.list_ports.comports()]
    print(f"Các cổng COM đang kết nối: {available_ports}")
    if PORT in available_ports:
        try:
            ser = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)
            print(f"[Thành công]: Đã kết nối với ESP32 qua cổng {PORT}!")
        except Exception as e:
            print(f"[Lỗi kết nối]: {e}. Chuyển sang CHẾ ĐỘ MÔ PHỎNG.")
            mode_simulation = True
    else:
        print(f"[Thông báo]: Không tìm thấy cổng {PORT}. Tự động kích hoạt CHẾ ĐỘ MÔ PHỎNG.")
        mode_simulation = True
else:
    mode_simulation = True

# Bộ đệm dữ liệu hiển thị (tối đa 100 điểm gần nhất)
MAX_POINTS = 100
time_data = []
h_raw_data = []
h_filt_data = []
v_data = []
u95_data = []
pump_data = []

start_time = time.time()
sim_t = 0.0
sim_water_level = 2.0
sim_pump = 1

# Mở tệp CSV ghi nhật ký
csv_f = open(CSV_FILE, "w", encoding="utf-8")
csv_f.write("timestamp_s,T_c,h_raw_cm,h_filt_cm,V_ml,U95_ml,pump_state,state_str\n")
csv_f.flush()

# Khởi tạo cửa sổ đồ thị Matplotlib
plt.rcParams['font.family'] = 'Segoe UI'
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
fig.canvas.manager.set_window_title("Hệ thống Giám sát Mức & Thể tích Bình chứa 2L (ESP32 - Chương 4)")

def read_telemetry():
    """Đọc gói tin JSON từ Serial hoặc sinh dữ liệu mô phỏng."""
    global sim_t, sim_water_level, sim_pump
    
    if not mode_simulation and ser and ser.is_open:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line.startswith("{") and line.endswith("}"):
                data = json.loads(line)
                return data
        except Exception:
            pass

    # Chế độ mô phỏng động học nạp xả bồn nước chai 2L
    sim_t += 0.2
    # Động lực học nạp xả có sóng gợn và bọt khí
    if sim_pump == 1:
        sim_water_level += 0.12  # Nước dâng
        if sim_water_level >= 14.5:
            sim_pump = 0        # Đầy tràn ngắt bơm
    else:
        sim_water_level -= 0.08  # Nước rút/xả đáy
        if sim_water_level <= 4.0:
            sim_pump = 1        # Cạn kích hoạt bơm

    # Nhiễu sóng gợn + xung gai bọt khí
    ripple = 0.45 * math.sin(2 * math.pi * 0.8 * sim_t)
    outlier = 2.5 if random.random() < 0.05 else 0.0
    h_raw = sim_water_level + ripple + outlier + random.uniform(-0.15, 0.15)
    
    h_filt = sim_water_level + 0.05 * math.sin(2 * math.pi * 0.8 * sim_t) # Đã lọc
    V = 78.54 * h_filt
    c_R = 2 * math.pi * 5.0 * h_filt
    u_c = math.sqrt((c_R * 0.04)**2 + (78.54 * 0.071)**2)
    U95 = 2.0 * u_c
    
    state = "NORMAL"
    if h_filt <= 2.5: state = "CAN_KHAN_CAP"
    elif h_filt <= 5.0: state = "CANH_BAO_CAN"
    elif h_filt >= 14.0: state = "TRAN_KHAN_CAP"
    else: state = "BINH_THUONG"

    return {
        "T": 27.0,
        "h_raw": round(h_raw, 2),
        "h": round(h_filt, 2),
        "V": round(V, 1),
        "U95": round(U95, 1),
        "pump": sim_pump,
        "state": state
    }

def update_plot(frame):
    data = read_telemetry()
    if not data:
        return

    cur_t = time.time() - start_time
    time_data.append(cur_t)
    h_raw_data.append(data.get("h_raw", 0))
    h_filt_data.append(data.get("h", 0))
    v_data.append(data.get("V", 0))
    u95_data.append(data.get("U95", 0))
    pump_data.append(data.get("pump", 0))

    if len(time_data) > MAX_POINTS:
        time_data.pop(0)
        h_raw_data.pop(0)
        h_filt_data.pop(0)
        v_data.pop(0)
        u95_data.pop(0)
        pump_data.pop(0)

    # Ghi log CSV
    csv_f.write(f"{cur_t:.2f},{data.get('T',27)},{data.get('h_raw',0)},{data.get('h',0)},"
                f"{data.get('V',0)},{data.get('U95',0)},{data.get('pump',0)},{data.get('state','')}\n")
    csv_f.flush()

    # VẼ ĐỒ THỊ 1: MỨC NƯỚC h(t)
    ax1.clear()
    ax1.plot(time_data, h_raw_data, color='#f39c12', alpha=0.5, lw=1.0, label='Mức nước thô h_raw (sóng gợn)')
    ax1.plot(time_data, h_filt_data, color='#1f77b4', lw=2.2, label='Mức nước sau lọc 2 tầng h_lọc (IQR + MA)')
    
    # Kẻ các ngưỡng cảnh báo
    ax1.axhline(14.0, color='#c0392b', ls='--', lw=1.2, label='Tràn khẩn cấp (14.0 cm)')
    ax1.axhline(5.0, color='#27ae60', ls=':', lw=1.2, label='Cảnh báo cạn (5.0 cm)')
    ax1.axhline(2.5, color='#922b21', ls='-.', lw=1.2, label='Cạn khẩn cấp (2.5 cm)')
    
    ax1.set_ylabel('Mức nước h (cm)', fontweight='bold', color='#1f77b4')
    ax1.set_ylim(0, 16.5)
    ax1.grid(True, ls=':', alpha=0.6)
    
    mode_text = "[MÔ PHỎNG]" if mode_simulation else f"[ESP32 SERIAL {PORT}]"
    ax1.set_title(f"{mode_text} Giám sát Mức nước & Kịch bản Điều khiển Bơm (T = {data.get('T',27)}°C)", fontweight='bold', fontsize=11)
    ax1.legend(loc='upper left', fontsize=8.2, ncol=3, framealpha=0.9)

    # VẼ ĐỒ THỊ 2: THỂ TÍCH V(t) VÀ ĐỘ KĐBĐ
    ax2.clear()
    v_arr = [v for v in v_data]
    u_arr = [u for u in u95_data]
    v_lower = [v - u for v, u in zip(v_arr, u_arr)]
    v_upper = [v + u for v, u in zip(v_arr, u_arr)]

    ax2.plot(time_data, v_arr, color='#27ae60', lw=2.2, label='Thể tích tức thời V(t) = S_base × h')
    ax2.fill_between(time_data, v_lower, v_upper, color='#2ecc71', alpha=0.25, label='Dải tin cậy mở rộng V ± U_95% (k = 2)')
    
    ax2.set_xlabel('Thời gian t (giây)', fontweight='bold')
    ax2.set_ylabel('Thể tích V (mL)', fontweight='bold', color='#27ae60')
    ax2.set_ylim(0, 1400)
    ax2.grid(True, ls=':', alpha=0.6)

    # Hiển thị Badge trạng thái bơm và cảnh báo
    state_str = data.get('state', 'NORMAL')
    pump_str = "BƠM: BẬT (ĐANG NẠP)" if data.get('pump') == 1 else "BƠM: TẮT"
    badge_color = '#e74c3c' if 'KHAN_CAP' in state_str else ('#f39c12' if 'CANH_BAO' in state_str else '#27ae60')
    
    info_txt = (
        f"Mức nước: {data.get('h',0):.1f} cm  |  "
        f"Thể tích: {data.get('V',0):.1f} ± {data.get('U95',0):.1f} mL  |  "
        f"{pump_str}  |  Trạng thái: {state_str}"
    )
    ax2.text(0.5, 0.90, info_txt, transform=ax2.transAxes, ha='center', va='center',
             fontsize=9.2, fontweight='bold', color='white',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=badge_color, edgecolor='none', alpha=0.9))
    ax2.legend(loc='lower left', fontsize=8.2, framealpha=0.9)

ani = FuncAnimation(fig, update_plot, interval=100)

try:
    print("\n--- Đang chạy Dashboard Giám sát thời gian thực (Nhấn Ctrl + C hoặc đóng cửa sổ để dừng) ---")
    plt.tight_layout()
    plt.show()
finally:
    if ser and ser.is_open:
        ser.close()
    csv_f.close()
    print(f"\n[Hoàn tất]: Dữ liệu đo đã lưu tại: {CSV_FILE}")
