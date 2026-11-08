import csv
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Segoe UI'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 12

p = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\du_lieu_tong_hop\chuong_3\thong_ke_chuong_3.csv")
with open(p, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Bỏ mốc 600cm, chỉ lấy đến 580cm
fsdt = [r for r in rows if r['ten_file'].startswith('FSDT') and float(r['cu_ly_dat_cm']) <= 580.0]
d_list = [float(r['cu_ly_dat_cm']) for r in fsdt]
s_raw = [float(r['std_tho_mm']) for r in fsdt]
s_clean = [float(r['std_sach_mm']) for r in fsdt]

# Thang tuyến tính với y_limit = [0, 10 mm], chỉ gióng ngang tại mốc chính trục Y
fig, ax = plt.subplots(figsize=(10, 5), dpi=300)

# Vẽ đường sạch
ax.plot(d_list, s_clean, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Dữ liệu sau khi làm sạch bằng IQR (s ≤ 4.0 mm)')

# Vẽ đường thô (cắt ngưỡng để đường hướng lên cao)
# Với điểm vọt lên > 10, ta để nó nối thẳng lên trên đỉnh
ax.plot(d_list, s_raw, color='#d62728', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='Dữ liệu thô ban đầu (Trước lọc)')

# Đường dung sai thước
ax.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')

# Giới hạn trục Y tuyến tính 0 - 10 mm
ax.set_ylim(-0.2, 10.0)
ax.set_xlim(-10, 595)

# Chỉ bật lưới ngang tại các mốc chính trục Y
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.5)

ax.set_title("ĐỘ LỆCH CHUẨN THỰC NGHIỆM TRƯỚC VÀ SAU LỌC IQR (THANG TUYẾN TÍNH 0 - 10 MM)", fontweight='bold', pad=12)
ax.set_xlabel("Khoảng cách đặt chuẩn đối chứng (cm)", fontweight='bold')
ax.set_ylabel("Độ lệch chuẩn thực nghiệm s (mm)", fontweight='bold')

# Chú thích hướng lên cao tại 360cm và 580cm mà không dùng mũi tên rườm rà (dùng text box nhỏ thanh lịch hoặc legend)
ax.text(360, 9.2, "360cm: s = 90.3 mm ↑", color='#d62728', fontsize=8.5, fontweight='bold', ha='center',
        bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#d62728', alpha=0.85))
ax.text(575, 9.2, "580cm: s = 346.1 mm ↑", color='#d62728', fontsize=8.5, fontweight='bold', ha='right',
        bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#d62728', alpha=0.85))

ax.legend(loc='upper left', framealpha=0.95)
plt.tight_layout()

test_p = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\test_linear_shoot_up.png")
fig.savefig(test_p)
plt.close(fig)
print("Đã tạo test_linear_shoot_up.png")
