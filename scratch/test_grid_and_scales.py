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

fsdt = [r for r in rows if r['ten_file'].startswith('FSDT')]
d_list = [float(r['cu_ly_dat_cm']) for r in fsdt]
s_raw = [float(r['std_tho_mm']) for r in fsdt]
s_clean = [float(r['std_sach_mm']) for r in fsdt]

# Bản 1: Thang tuyến tính hoàn toàn (Linear Scale 0 - 2700 mm) - Chỉ lưới ngang mốc chính
fig1, ax1 = plt.subplots(figsize=(9.5, 5), dpi=300)
ax1.plot(d_list, s_raw, color='#d62728', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='Dữ liệu thô ban đầu (Trước lọc)')
ax1.plot(d_list, s_clean, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Dữ liệu sau khi làm sạch bằng IQR')
ax1.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')
ax1.set_title("ĐỘ LỆCH CHUẨN THỰC NGHIỆM TRƯỚC VÀ SAU LỌC IQR (THANG TUYẾN TÍNH TOÀN DẢI)", fontweight='bold', pad=12)
ax1.set_xlabel("Khoảng cách đặt chuẩn đối chứng (cm)", fontweight='bold')
ax1.set_ylabel("Độ lệch chuẩn thực nghiệm s (mm)", fontweight='bold')
ax1.set_xlim(-10, 620)
ax1.set_ylim(-50, 2750)
ax1.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.5)
ax1.legend(loc='upper left', framealpha=0.95)
plt.tight_layout()
p1 = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\test_linear_full.png")
fig1.savefig(p1)
plt.close(fig1)

# Bản 2: Thang Logarit - Chỉ giữ đường ngang tại các mốc chính (Major ticks: 0.1, 1, 10, 100, 1000), BỎ TOÀN BỘ LƯỚI PHỤ
fig2, ax2 = plt.subplots(figsize=(9.5, 5), dpi=300)
ax2.plot(d_list, s_raw, color='#d62728', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='Dữ liệu thô ban đầu (Trước lọc)')
ax2.plot(d_list, s_clean, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Dữ liệu sau khi làm sạch bằng IQR')
ax2.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')
ax2.set_yscale('log')
ax2.set_title("ĐỘ LỆCH CHUẨN THỰC NGHIỆM TRƯỚC VÀ SAU LỌC IQR (THANG LOGARIT - CHỈ LƯỚI CHÍNH)", fontweight='bold', pad=12)
ax2.set_xlabel("Khoảng cách đặt chuẩn đối chứng (cm)", fontweight='bold')
ax2.set_ylabel("Độ lệch chuẩn thực nghiệm s (mm)", fontweight='bold')
ax2.set_xlim(-10, 620)
ax2.set_ylim(0.02, 4000)
# Chỉ bật lưới ngang tại major ticks
ax2.grid(axis='y', which='major', linestyle='--', linewidth=0.7, alpha=0.5)
ax2.legend(loc='upper left', framealpha=0.95)
plt.tight_layout()
p2 = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\test_log_clean_grid.png")
fig2.savefig(p2)
plt.close(fig2)

# Bản 3: Thang tuyến tính dải làm việc tiêu chuẩn (0 - 550 cm, s từ 0 đến 100 mm)
fig3, ax3 = plt.subplots(figsize=(9.5, 5), dpi=300)
d_550 = d_list[:-2] # đến 550cm
s_raw_550 = s_raw[:-2]
s_clean_550 = s_clean[:-2]
ax3.plot(d_550, s_raw_550, color='#d62728', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='Dữ liệu thô ban đầu (Trước lọc)')
ax3.plot(d_550, s_clean_550, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Dữ liệu sau khi làm sạch bằng IQR')
ax3.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')
ax3.set_title("ĐỘ LỆCH CHUẨN TRONG DẢI ĐO LÀM VIỆC 1 - 550 CM (THANG TUYẾN TÍNH)", fontweight='bold', pad=12)
ax3.set_xlabel("Khoảng cách đặt chuẩn đối chứng (cm)", fontweight='bold')
ax3.set_ylabel("Độ lệch chuẩn thực nghiệm s (mm)", fontweight='bold')
ax3.set_xlim(-10, 560)
ax3.set_ylim(-2, 100)
ax3.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.5)
ax3.legend(loc='upper left', framealpha=0.95)
plt.tight_layout()
p3 = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\test_linear_550cm.png")
fig3.savefig(p3)
plt.close(fig3)

print("Đã tạo xong 3 bản so sánh!")
