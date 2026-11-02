import math
import numpy as np
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Cấu hình thẩm mỹ học thuật và font tiếng Việt
plt.rcParams['font.family'] = 'Segoe UI'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 12

BASE_DIR = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601")
GRAPH_DIR = BASE_DIR / "graph"
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# 1. HÌNH 4.1: Sơ đồ nguyên lý hình học Bồn chứa thông minh
# ==========================================================
print("Tạo Hình 4.1: Sơ đồ nguyên lý bồn chứa...")
fig, ax = plt.subplots(figsize=(8, 7), dpi=300)

# Vẽ thân bồn chứa hình trụ (2D profile)
tank_x = 2.0
tank_y = 1.0
tank_w = 4.0
tank_h = 6.0

# Bồn chứa
tank_rect = patches.Rectangle((tank_x, tank_y), tank_w, tank_h, linewidth=2.5, edgecolor='#2c3e50', facecolor='#ecf0f1', alpha=0.3)
ax.add_patch(tank_rect)

# Cổ nối lắp cảm biến (đảm bảo vượt vùng chết 15cm)
neck_w = 1.2
neck_h = 0.8
neck_x = tank_x + (tank_w - neck_w) / 2.0
neck_y = tank_y + tank_h
neck_rect = patches.Rectangle((neck_x, neck_y), neck_w, neck_h, linewidth=2.0, edgecolor='#2c3e50', facecolor='#bdc3c7')
ax.add_patch(neck_rect)

# Cảm biến RCWL-1601 lắp trên đỉnh cổ nối
sensor_w = 0.8
sensor_h = 0.3
sensor_x = tank_x + (tank_w - sensor_w) / 2.0
sensor_y = neck_y + neck_h - sensor_h
sensor_rect = patches.Rectangle((sensor_x, sensor_y), sensor_w, sensor_h, linewidth=1.5, edgecolor='#c0392b', facecolor='#e74c3c')
ax.add_patch(sensor_rect)
ax.text(sensor_x + sensor_w/2.0, sensor_y + sensor_h/2.0, "RCWL-1601", color='white', ha='center', va='center', weight='bold', fontsize=8)

# Mức nước hiện tại
water_h = 3.8
water_rect = patches.Rectangle((tank_x, tank_y), tank_w, water_h, linewidth=1.0, edgecolor='#2980b9', facecolor='#3498db', alpha=0.55)
ax.add_patch(water_rect)

# Sóng gợn trên mặt nước
wave_x = np.linspace(tank_x, tank_x + tank_w, 100)
wave_y = tank_y + water_h + 0.05 * np.sin(2 * np.pi * 3 * (wave_x - tank_x) / tank_w)
ax.plot(wave_x, wave_y, color='#1f618d', linewidth=2.0)

# Vùng chết (Blind Zone: 3cm) ngay dưới cảm biến
blind_h = 0.4
blind_rect = patches.Rectangle((neck_x + 0.1, sensor_y - blind_h), neck_w - 0.2, blind_h, linewidth=1.0, linestyle=':', edgecolor='#e74c3c', facecolor='#fadbd8', alpha=0.8)
ax.add_patch(blind_rect)
ax.text(neck_x + neck_w/2.0, sensor_y - blind_h/2.0, "Vùng chết (0-3 cm)", color='#922b21', ha='center', va='center', fontsize=7.5, weight='bold')

# Chùm sóng âm phản xạ
cone_top_x = tank_x + tank_w / 2.0
cone_top_y = sensor_y
ax.plot([cone_top_x, tank_x + 0.8], [cone_top_y, tank_y + water_h], '--', color='#e67e22', linewidth=1.5)
ax.plot([cone_top_x, tank_x + tank_w - 0.8], [cone_top_y, tank_y + water_h], '--', color='#e67e22', linewidth=1.5)
ax.text(cone_top_x, (cone_top_y + tank_y + water_h)/2.0, "Chùm sóng âm (15°)", color='#d35400', ha='center', va='center', fontsize=8.5, weight='bold', bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#e67e22', alpha=0.9))

# Các đường kích thước (Dimension lines)
# Tổng chiều cao H_tank
ax.annotate('', xy=(tank_x - 0.4, tank_y), xytext=(tank_x - 0.4, neck_y + neck_h),
            arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=1.2))
ax.text(tank_x - 0.55, (tank_y + neck_y + neck_h)/2.0, "H_tổng = H_tank + H_cổ", color='#2c3e50', ha='right', va='center', rotation=90, weight='bold')

# Khoảng cách đo d(t)
ax.annotate('', xy=(cone_top_x + 0.5, tank_y + water_h), xytext=(cone_top_x + 0.5, cone_top_y),
            arrowprops=dict(arrowstyle='<->', color='#c0392b', lw=1.5))
ax.text(cone_top_x + 0.65, (cone_top_y + tank_y + water_h)/2.0, "Khoảng trống d(t)\n(Cảm biến đo)", color='#c0392b', ha='left', va='center', weight='bold')

# Mức chất lỏng h(t)
ax.annotate('', xy=(tank_x + tank_w + 0.4, tank_y), xytext=(tank_x + tank_w + 0.4, tank_y + water_h),
            arrowprops=dict(arrowstyle='<->', color='#2980b9', lw=1.5))
ax.text(tank_x + tank_w + 0.55, tank_y + water_h/2.0, "Mức chất lỏng h(t)\nh(t) = H_tổng - d(t)", color='#2980b9', ha='left', va='center', weight='bold')

# Các ngưỡng cảnh báo
ax.axhline(tank_y + 5.2, xmin=0.25, xmax=0.75, color='#c0392b', linestyle='--', linewidth=1.0)
ax.text(tank_x + 0.1, tank_y + 5.35, "Ngưỡng tràn High-High (90%)", color='#c0392b', fontsize=8, weight='bold')

ax.axhline(tank_y + 4.5, xmin=0.25, xmax=0.75, color='#e67e22', linestyle=':', linewidth=1.0)
ax.text(tank_x + 0.1, tank_y + 4.65, "Ngưỡng cảnh báo cao High (75%)", color='#d35400', fontsize=8)

ax.axhline(tank_y + 1.2, xmin=0.25, xmax=0.75, color='#27ae60', linestyle=':', linewidth=1.0)
ax.text(tank_x + 0.1, tank_y + 1.35, "Ngưỡng cạn Low (20%)", color='#27ae60', fontsize=8)

# Thiết bị ngoại vi ESP32 + Nhiệt kế
box_esp_x = 6.8
box_esp_y = 6.2
rect_esp = patches.FancyBboxPatch((box_esp_x, box_esp_y), 2.2, 1.2, boxstyle="round,pad=0.1", fc="#2ecc71", ec="#27ae60", lw=1.5)
ax.add_patch(rect_esp)
ax.text(box_esp_x + 1.1, box_esp_y + 0.6, "ESP32 Controller\n+ Thuật toán bù Laplace\n+ Lọc số IQR & MA", color='white', ha='center', va='center', weight='bold', fontsize=7.5)

# Cáp nối cảm biến về ESP32
ax.plot([sensor_x + sensor_w, box_esp_x], [sensor_y + sensor_h/2.0, box_esp_y + 0.8], '-', color='#7f8c8d', lw=1.5)
ax.text((sensor_x + sensor_w + box_esp_x)/2.0, (sensor_y + sensor_h/2.0 + box_esp_y + 0.8)/2.0 + 0.15, "GPIO 5/18 (3.3V)", color='#34495e', fontsize=7.5)

# Cảm biến nhiệt độ môi trường
ax.plot([box_esp_x, neck_x + neck_w], [box_esp_y + 0.3, neck_y + 0.2], ':', color='#e74c3c', lw=1.5)
ax.plot(neck_x + neck_w - 0.05, neck_y + 0.2, 'o', color='#e74c3c', markersize=6)
ax.text(neck_x + neck_w + 0.1, neck_y + 0.2, "Đo nhiệt độ T (°C)\nbù vận tốc v(T)", color='#c0392b', fontsize=7.5, weight='bold')

ax.set_xlim(0.5, 9.5)
ax.set_ylim(0.0, 8.5)
ax.axis('off')
ax.set_title("Sơ đồ nguyên lý Hệ thống Giám sát Mức và Thể tích Bồn chứa Thông minh (RCWL-1601 & ESP32)", pad=15)

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_4_1_nguyen_ly_bon_chua.png", dpi=300)
plt.close()

# ==========================================================
# 2. HÌNH 4.2: Mô phỏng Chuỗi Lọc số (IQR + Moving Average)
# ==========================================================
print("Tạo Hình 4.2: Mô phỏng chuỗi lọc sóng gợn bồn chứa...")
np.random.seed(42)

# Thời gian mô phỏng quá trình bơm nạp chất lỏng (200 bước lấy mẫu, Ts = 0.5s -> 100s)
t = np.linspace(0, 100, 200)

# Mức nước thực tế tăng dần từ 0.5m đến 1.8m (Ground Truth)
h_true = 0.5 + 1.3 * (1 - np.exp(-t / 35.0)) # cm: 50cm -> 180cm
h_true_cm = h_true * 100.0 # cm

# Sóng gợn do dòng xả của máy bơm (biên độ +- 2.5 cm, tần số 0.3 Hz)
wave_noise = 2.5 * np.sin(2 * np.pi * 0.3 * t)

# Nhiễu âm học Gaussian tự nhiên (std = 0.4 cm)
gauss_noise = np.random.normal(0, 0.4, len(t))

# Dữ liệu đo thô với sóng gợn và nhiễu
h_raw = h_true_cm + wave_noise + gauss_noise

# Bổ sung 3 xung dị biệt bão hòa do bọt khí/tia nước bắn làm mất echo (timeout -> 824.6 cm khoảng trống -> h_raw nhảy về cự ly âm/cực đoan)
h_raw[45] = 12.0 # Giảm đột biến do phản xạ tia nước trên không
h_raw[110] = -50.0 # Lỗi bão hòa timeout
h_raw[165] = 230.0 # Gai nhiễu phản xạ thành bồn

# 1. Áp dụng lọc cửa sổ trượt Khoảng tứ phân vị (IQR Filter, Window W = 11)
W_iqr = 11
h_iqr = np.copy(h_raw)
for i in range(len(t)):
    start_idx = max(0, i - W_iqr // 2)
    end_idx = min(len(t), i + W_iqr // 2 + 1)
    sub_win = h_raw[start_idx:end_idx]
    q1 = np.percentile(sub_win, 25)
    q3 = np.percentile(sub_win, 75)
    iqr = q3 - q1
    lf = q1 - 1.5 * iqr
    uf = q3 + 1.5 * iqr
    if h_raw[i] < lf or h_raw[i] > uf:
        h_iqr[i] = np.median(sub_win) # Thay thế ngoại lai bằng trung vị cửa sổ

# 2. Áp dụng Lọc trung bình trượt (Moving Average, M = 9) khử hoàn toàn sóng gợn
M_ma = 9
h_filtered = np.convolve(h_iqr, np.ones(M_ma)/M_ma, mode='same')

# Vẽ đồ thị 2 tầng: Tầng 1 là tín hiệu, Tầng 2 là sai số so với Ground Truth
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.5), dpi=300, sharex=True)

# Tầng 1: Tín hiệu
ax1.plot(t, h_raw, '.', color='#bdc3c7', markersize=3.5, label='Dữ liệu đo thô (Chứa sóng gợn & xung dị biệt)', alpha=0.8)
ax1.plot(t, h_iqr, '--', color='#e67e22', linewidth=1.2, label='Sau lọc IQR (Đã loại trừ xung đột biến & bọt khí)')
ax1.plot(t, h_filtered, '-', color='#27ae60', linewidth=1.8, label='Sau lọc Trung bình trượt MA (Làm mịn mức mặt nước)')
ax1.plot(t, h_true_cm, '-', color='#2c3e50', linewidth=1.5, linestyle=':', label='Mức chất lỏng thực tế (Ground Truth)')

# Đánh dấu các xung ngoại lai đã bị khử
ax1.plot([t[45], t[110], t[165]], [h_raw[45], h_raw[110], h_raw[165]], 'rx', markersize=8, markeredgewidth=2, label='Xung ngoại lai bị triệt tiêu')
ax1.set_ylabel('Mức chất lỏng h (cm)')
ax1.set_title('Hiệu quả Khử sóng gợn và Lọc ngoại lai trong chuỗi xử lý tín hiệu Bồn chứa')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='lower right', fontsize=8.5)
ax1.set_ylim(-10, 220)

# Tầng 2: Sai số
err_raw = h_raw - h_true_cm
err_filtered = h_filtered - h_true_cm
ax2.plot(t, err_raw, color='#e74c3c', alpha=0.4, label='Sai số tín hiệu thô (Bị sóng gợn ±3 cm & ngoại lai)')
ax2.plot(t, err_filtered, color='#2980b9', linewidth=1.5, label=f'Sai số sau lọc (Độ lệch chuẩn: {np.std(err_filtered[10:-10]):.2f} cm)')
ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax2.axhline(1.0, color='gray', linestyle=':', label='Dải dung sai kỹ thuật ±1 cm')
ax2.axhline(-1.0, color='gray', linestyle=':')
ax2.set_xlabel('Thời gian quan trắc (giây)')
ax2.set_ylabel('Sai số đo Δh (cm)')
ax2.set_ylim(-6, 6)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', fontsize=8.5)

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_4_2_mo_phong_loc_song_gon.png", dpi=300)
plt.close()

# ==========================================================
# 3. HÌNH 4.3: Đánh giá Lan truyền Sai số và Độ không đảm bảo Thể tích
# ==========================================================
print("Tạo Hình 4.3: Lan truyền độ không đảm bảo thể tích...")

# Thiết lập bồn chứa công nghiệp tiêu chuẩn: Bồn đứng R = 0.5 m (Đường kính D = 1.0 m, Diện tích đáy S = pi * R^2 = 0.7854 m2)
# Chiều cao bồn H = 2.5 m -> Thể tích toàn phần V_total = S * H = 1.9635 m3 = 1963.5 Lít
R_tank = 0.5 # mét
S_base = math.pi * (R_tank ** 2) # m2

# Dải mức nước từ 0.1m đến 2.3m (10cm đến 230cm)
h_levels = np.linspace(0.1, 2.3, 23) # mét
V_liters = S_base * h_levels * 1000.0 # Lít

# Độ không đảm bảo đo chiều cao U_95%(h) = U_95%(d) từ Chương 3 (Mục 3.8)
# Ở khoảng trống d = H_total - h (khoảng 0.2m đến 2.4m): U_95%(d) dao động từ 1.0 mm đến 2.5 mm
# Xấp xỉ thực nghiệm: U_95%(d) = 0.6 mm + 0.8 mm * (d/1.0m)
d_empty = 2.5 - h_levels # khoảng cách cảm biến đo
U_h_mm = 0.6 + 0.8 * d_empty # mm
U_h_m = U_h_mm / 1000.0 # mét

# Độ không đảm bảo thể tích: U_V = S_base * U_h (bỏ qua sai số chế tạo bồn cơ khí để tập trung vào cảm biến)
U_V_liters = S_base * U_h_m * 1000.0 # Lít
rel_U_V_pct = (U_V_liters / V_liters) * 100.0 # %

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Cột 1: Thể tích và Độ KĐBĐ mở rộng U_95%(V)
U_95_V = U_V_liters
ax1.plot(h_levels * 100, V_liters, 'o-', color='#2980b9', linewidth=1.5, markersize=4, label='Thể tích bồn V(h)')
ax1.fill_between(h_levels * 100, V_liters - U_95_V, V_liters + U_95_V, color='#3498db', alpha=0.25, label='Dải mở rộng tin cậy 95% (±U_V)')
ax1.set_title('Thể tích chất lỏng tức thời và Dải tin cậy 95%')
ax1.set_xlabel('Mức chất lỏng h (cm)')
ax1.set_ylabel('Thể tích chất lỏng V (Lít)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')

# Cột 2: Sai số thể tích tương đối
ax2.plot(h_levels * 100, rel_U_V_pct, 's-', color='#e67e22', linewidth=1.5, markersize=4, label='Độ KĐBĐ tương đối U_V/V (%)')
ax2.axhline(0.5, color='red', linestyle='--', label='Ngưỡng chuẩn công nghiệp 0.5%')
ax2.set_title('Độ không đảm bảo Thể tích tương đối theo Mức nước')
ax2.set_xlabel('Mức chất lỏng h (cm)')
ax2.set_ylabel('Độ không đảm bảo tương đối (%)')
ax2.set_ylim(0, 1.6)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_4_3_danh_gia_sai_so_the_tich.png", dpi=300)
plt.close()

print("Hoàn tất tạo thành công 3 đồ thị kỹ thuật cho Chương 4!")
