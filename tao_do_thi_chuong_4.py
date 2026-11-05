# -*- coding: utf-8 -*-
import sys
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import math
import numpy as np
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Segoe UI'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 12

BASE_DIR = Path(r"C:\Users\Admin\Downloads\RCWL1601")
GRAPH_DIRS = [
    BASE_DIR / "graph",
    Path(r"C:\Users\Admin\Downloads") / "graph"
]
for g in GRAPH_DIRS:
    g.mkdir(parents=True, exist_ok=True)

# ==========================================================
# 1. HÌNH 4.1: Sơ đồ nguyên lý hình học Bồn chứa mini để bàn
# R = 4cm (D = 8cm), H_tank = 12cm, H_cổ = 5cm, V = 603 mL
# ==========================================================
print("Tạo Hình 4.1: Sơ đồ nguyên lý bồn chứa để bàn (R=4cm, H=12cm)...")
fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)

tank_x = 2.2
tank_y = 1.0
tank_w = 3.6  # đại diện D = 8.0 cm
tank_h = 5.4  # đại diện H = 12.0 cm

# Bồn chứa (Cốc đong chia vạch trong suốt)
tank_rect = patches.Rectangle((tank_x, tank_y), tank_w, tank_h, linewidth=2.5, edgecolor='#2c3e50', facecolor='#f8f9fa', alpha=0.4)
ax.add_patch(tank_rect)

# Các vạch chia ml trên thành bồn mô phỏng cốc đong thí nghiệm
for v_lvl, v_ml in [(0.2, "100"), (0.4, "200"), (0.6, "300"), (0.8, "400"), (1.0, "500"), (1.15, "600 ml")]:
    y_pos = tank_y + v_lvl * (tank_h / 1.2)
    ax.plot([tank_x, tank_x + 0.3], [y_pos, y_pos], color='#7f8c8d', linewidth=1.2)
    ax.text(tank_x + 0.35, y_pos, v_ml, fontsize=6.5, va='center', color='#555')

# Cổ nối gá lắp cảm biến vượt vùng chết (H_cổ = 5 cm)
neck_w = 2.0
neck_h = 2.25 # đại diện H_cổ = 5.0 cm
neck_x = tank_x + (tank_w - neck_w) / 2.0
neck_y = tank_y + tank_h
neck_rect = patches.Rectangle((neck_x, neck_y), neck_w, neck_h, linewidth=1.8, linestyle='--', edgecolor='#7f8c8d', facecolor='#e9ecef')
ax.add_patch(neck_rect)

# Cảm biến RCWL-1601 lắp trên đỉnh cổ nối
sensor_w = 1.6
sensor_h = 0.5
sensor_x = tank_x + (tank_w - sensor_w) / 2.0
sensor_y = neck_y + neck_h - sensor_h
sensor_rect = patches.Rectangle((sensor_x, sensor_y), sensor_w, sensor_h, linewidth=1.5, edgecolor='#c0392b', facecolor='#e74c3c')
ax.add_patch(sensor_rect)
ax.text(sensor_x + sensor_w/2.0, sensor_y + sensor_h/2.0, "RCWL-1601", color='white', ha='center', va='center', weight='bold', fontsize=8)

# Mức nước hiện tại trong bồn
water_h = 3.375
water_rect = patches.Rectangle((tank_x, tank_y), tank_w, water_h, linewidth=1.0, edgecolor='#2980b9', facecolor='#3498db', alpha=0.5)
ax.add_patch(water_rect)

# Sóng gợn trên mặt nước
wave_x = np.linspace(tank_x, tank_x + tank_w, 100)
wave_y = tank_y + water_h + 0.04 * np.sin(2 * np.pi * 3 * (wave_x - tank_x) / tank_w)
ax.plot(wave_x, wave_y, color='#1f618d', linewidth=1.8)

# Vùng chết (Blind Zone: 0 - 3 cm) nằm an toàn trong lòng cổ gá
blind_h = 1.35 # đại diện 3.0 cm
blind_rect = patches.Rectangle((neck_x + 0.1, sensor_y - blind_h), neck_w - 0.2, blind_h, linewidth=1.0, linestyle=':', edgecolor='#e74c3c', facecolor='#fadbd8', alpha=0.75)
ax.add_patch(blind_rect)
ax.text(neck_x + neck_w/2.0, sensor_y - blind_h/2.0, "Vùng chết (0 - 3 cm)\n(Cách ly an toàn trong cổ)", color='#922b21', ha='center', va='center', fontsize=7, weight='bold')

# Chùm sóng âm phản xạ (Góc mở 15°)
cone_top_x = tank_x + tank_w / 2.0
cone_top_y = sensor_y
ax.plot([cone_top_x, tank_x + 0.3], [cone_top_y, tank_y + water_h], '--', color='#e67e22', linewidth=1.3)
ax.plot([cone_top_x, tank_x + tank_w - 0.3], [cone_top_y, tank_y + water_h], '--', color='#e67e22', linewidth=1.3)
ax.text(cone_top_x, (cone_top_y + tank_y + water_h)/2.0, "Chùm sóng âm (±15°)\n(Định hướng dọc ống)", color='#d35400', ha='center', va='center', fontsize=7.5, weight='bold', bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#e67e22', alpha=0.9))

# Đường nạp nước dưới đáy
pipe_x = [tank_x - 0.8, tank_x + 0.4, tank_x + 0.4]
pipe_y = [tank_y + 0.3, tank_y + 0.3, tank_y + 0.05]
ax.plot(pipe_x, pipe_y, color='#2980b9', linewidth=2.5)
ax.text(tank_x - 0.85, tank_y + 0.3, "Từ bơm mini 5V\n(Nạp êm từ đáy)", color='#1f618d', ha='right', va='center', fontsize=7.5, weight='bold')

# Kích thước tổng thể
ax.annotate('', xy=(tank_x - 0.3, tank_y), xytext=(tank_x - 0.3, neck_y + neck_h),
            arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=1.2))
ax.text(tank_x - 0.45, (tank_y + neck_y + neck_h)/2.0, "H_tổng = 17 cm\n(H_tank 12cm + H_cổ 5cm)", color='#2c3e50', ha='right', va='center', rotation=90, fontsize=7.5, weight='bold')

# Khoảng cách đo d(t)
ax.annotate('', xy=(cone_top_x + 0.7, tank_y + water_h), xytext=(cone_top_x + 0.7, cone_top_y),
            arrowprops=dict(arrowstyle='<->', color='#c0392b', lw=1.3))
ax.text(cone_top_x + 0.85, (cone_top_y + tank_y + water_h)/2.0, "Khoảng trống d(t)\n(Cảm biến đo)", color='#c0392b', ha='left', va='center', fontsize=7.5, weight='bold')

# Mức nước h(t)
ax.annotate('', xy=(tank_x + tank_w + 0.3, tank_y), xytext=(tank_x + tank_w + 0.3, tank_y + water_h),
            arrowprops=dict(arrowstyle='<->', color='#2980b9', lw=1.3))
ax.text(tank_x + tank_w + 0.45, tank_y + water_h/2.0, "Mức nước h(t)\nh(t) = H_tổng - d(t)", color='#2980b9', ha='left', va='center', fontsize=7.5, weight='bold')

# Khối ESP32
box_esp_x = 6.8
box_esp_y = 5.0
rect_esp = patches.FancyBboxPatch((box_esp_x, box_esp_y), 2.4, 1.4, boxstyle="round,pad=0.1", fc="#2ecc71", ec="#27ae60", lw=1.5)
ax.add_patch(rect_esp)
ax.text(box_esp_x + 1.2, box_esp_y + 0.7, "ESP32 Controller\n• Bù nhiệt Laplace v(T)\n• Lọc số IQR + MA\n• Rơ-le điều khiển Bơm", color='white', ha='center', va='center', weight='bold', fontsize=7.5)

ax.plot([sensor_x + sensor_w, box_esp_x], [sensor_y + sensor_h/2.0, box_esp_y + 0.9], '-', color='#7f8c8d', lw=1.5)
ax.text((sensor_x + sensor_w + box_esp_x)/2.0, (sensor_y + sensor_h/2.0 + box_esp_y + 0.9)/2.0 + 0.15, "GPIO 5/18", color='#34495e', fontsize=7.5)

ax.plot([box_esp_x, neck_x + neck_w], [box_esp_y + 0.4, neck_y + 0.4], ':', color='#e74c3c', lw=1.5)
ax.plot(neck_x + neck_w - 0.05, neck_y + 0.4, 'o', color='#e74c3c', markersize=5)
ax.text(neck_x + neck_w + 0.1, neck_y + 0.4, "Đầu dò DS18B20\n(Bù vận tốc âm v(T))", color='#c0392b', fontsize=7, weight='bold')

ax.set_xlim(0.5, 9.8)
ax.set_ylim(0.0, 9.0)
ax.axis('off')
ax.set_title("Sơ đồ nguyên lý Mô hình Bồn chứa Để bàn Thông minh (R = 4 cm, H = 12 cm, V ≈ 603 mL)", pad=12)

plt.tight_layout()
for g in GRAPH_DIRS:
    plt.savefig(g / "hinh_4_1_nguyen_ly_bon_chua.png", dpi=300)
plt.close()

# ==========================================================
# 2. HÌNH 4.2: Mô phỏng Chuỗi Lọc số (IQR + Moving Average)
# ==========================================================
print("Tạo Hình 4.2: Mô phỏng chuỗi lọc sóng gợn bồn chứa mini...")
np.random.seed(42)

t = np.linspace(0, 30, 150)
h_true_cm = 1.5 + 9.0 * (1 - np.exp(-t / 12.0))
wave_noise = 0.6 * np.sin(2 * np.pi * 0.5 * t)
gauss_noise = np.random.normal(0, 0.08, len(t))
h_raw = h_true_cm + wave_noise + gauss_noise
h_raw[25] = 0.5
h_raw[75] = -4.0
h_raw[120] = 13.5

W_iqr = 9
h_iqr = np.copy(h_raw)
for i in range(len(t)):
    s_idx = max(0, i - W_iqr // 2)
    e_idx = min(len(t), i + W_iqr // 2 + 1)
    sub = h_raw[s_idx:e_idx]
    q1 = np.percentile(sub, 25)
    q3 = np.percentile(sub, 75)
    iqr = q3 - q1
    lf = q1 - 1.5 * iqr
    uf = q3 + 1.5 * iqr
    if h_raw[i] < lf or h_raw[i] > uf:
        h_iqr[i] = np.median(sub)

M_ma = 7
h_filtered = np.convolve(h_iqr, np.ones(M_ma)/M_ma, mode='same')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.2), dpi=300, sharex=True)

ax1.plot(t, h_raw, '.', color='#bdc3c7', markersize=4, label='Dữ liệu đo thô (Chứa sóng gợn & gai nhiễu)', alpha=0.8)
ax1.plot(t, h_iqr, '--', color='#e67e22', linewidth=1.2, label='Sau lọc IQR (Đã loại trừ xung đột biến & bọt khí)')
ax1.plot(t, h_filtered, '-', color='#27ae60', linewidth=1.8, label='Sau lọc Trung bình trượt MA (Làm phẳng mức mặt nước)')
ax1.plot(t, h_true_cm, color='#2c3e50', linewidth=1.5, linestyle=':', label='Mức nước thực tế (Ground Truth)')

ax1.plot([t[25], t[75], t[120]], [h_raw[25], h_raw[75], h_raw[120]], 'rx', markersize=8, markeredgewidth=2, label='Xung ngoại lai bị triệt tiêu')
ax1.set_ylabel('Mức nước h (cm)')
ax1.set_title('Hiệu quả Khử sóng gợn và Lọc ngoại lai trong chuỗi xử lý tín hiệu Bồn chứa để bàn')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='lower right', fontsize=8.5)
ax1.set_ylim(-6, 16)

err_raw = h_raw - h_true_cm
err_filtered = h_filtered - h_true_cm
ax2.plot(t, err_raw, color='#e74c3c', alpha=0.35, label='Sai số tín hiệu thô (Bị sóng gợn ±0.6 cm & ngoại lai)')
ax2.plot(t, err_filtered, color='#2980b9', linewidth=1.5, label=f'Sai số sau lọc (Độ lệch chuẩn s = {np.std(err_filtered[8:-8])*10:.2f} mm)')
ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax2.axhline(0.2, color='gray', linestyle=':', label='Dải dung sai kỹ thuật ±2.0 mm')
ax2.axhline(-0.2, color='gray', linestyle=':')
ax2.set_xlabel('Thời gian quan trắc (giây)')
ax2.set_ylabel('Sai số đo Δh (cm)')
ax2.set_ylim(-2.0, 2.0)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', fontsize=8.5)

plt.tight_layout()
for g in GRAPH_DIRS:
    plt.savefig(g / "hinh_4_2_mo_phong_loc_song_gon.png", dpi=300)
plt.close()

# ==========================================================
# 3. HÌNH 4.3: Lan truyền Độ không đảm bảo đo Thể tích Bồn mini
# ==========================================================
print("Tạo Hình 4.3: Lan truyền độ không đảm bảo thể tích bồn mini...")

R_tank = 4.0 # cm
S_base = math.pi * (R_tank ** 2)

h_levels_cm = np.linspace(1.0, 11.5, 22)
V_ml = S_base * h_levels_cm

d_empty = 17.0 - h_levels_cm
U_h_mm = 0.75 + 0.3 * (d_empty / 17.0)
U_h_cm = U_h_mm / 10.0

U_V_ml = S_base * U_h_cm
rel_U_V_pct = (U_V_ml / V_ml) * 100.0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

ax1.plot(h_levels_cm, V_ml, 'o-', color='#2980b9', linewidth=1.5, markersize=4, label='Thể tích bồn V(h)')
ax1.fill_between(h_levels_cm, V_ml - U_V_ml, V_ml + U_V_ml, color='#3498db', alpha=0.25, label='Dải tin cậy 95% (±U_V)')
ax1.set_title('Thể tích chất lỏng tức thời và Dải tin cậy 95%')
ax1.set_xlabel('Mức nước h (cm)')
ax1.set_ylabel('Thể tích chất lỏng V (mL)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')

ax2.plot(h_levels_cm, rel_U_V_pct, 's-', color='#e67e22', linewidth=1.5, markersize=4, label='Độ KĐBĐ tương đối U_V/V (%)')
ax2.axhline(1.0, color='red', linestyle='--', label='Ngưỡng kiểm soát 1.0%')
ax2.set_title('Độ không đảm bảo Thể tích tương đối theo Mức nước')
ax2.set_xlabel('Mức nước h (cm)')
ax2.set_ylabel('Độ không đảm bảo tương đối (%)')
ax2.set_ylim(0, 8.0)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right')

plt.tight_layout()
for g in GRAPH_DIRS:
    plt.savefig(g / "hinh_4_3_danh_gia_sai_so_the_tich.png", dpi=300)
plt.close()

print("Hoàn tất tạo thành công 3 đồ thị kỹ thuật Chương 4!")
