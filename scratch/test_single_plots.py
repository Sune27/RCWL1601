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
err_raw = [abs(float(r['mean_tho_cm']) - d) * 10 for d, r in zip(d_list, fsdt)]
err_clean = [abs(float(r['mean_sach_cm']) - d) * 10 for d, r in zip(d_list, fsdt)]

# Phương án 1: Đồ thị Độ lệch chuẩn s trước và sau lọc (Thang Logarit)
fig1, ax1 = plt.subplots(figsize=(9.5, 5), dpi=300)
ax1.plot(d_list, s_raw, color='#d62728', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='Dữ liệu thô ban đầu (Trước lọc)')
ax1.plot(d_list, s_clean, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Dữ liệu sau khi làm sạch bằng IQR')
ax1.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')
ax1.set_yscale('log')
ax1.set_title("HIỆU QUẢ TRIỆT TIÊU ĐỘ LỆCH CHUẨN THỰC NGHIỆM TRƯỚC VÀ SAU LỌC IQR", fontweight='bold', pad=12)
ax1.set_xlabel("Khoảng cách đặt chuẩn đối chứng (cm)", fontweight='bold')
ax1.set_ylabel("Độ lệch chuẩn thực nghiệm s (mm) - Thang logarit", fontweight='bold')
ax1.set_xlim(-10, 620)
ax1.grid(True, which="both", linestyle=':', alpha=0.6)
ax1.legend(loc='upper left', framealpha=0.95)
plt.tight_layout()
fig1.savefig(Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\test_pa1_std.png"))
plt.close(fig1)

# Phương án 2: Đồ thị Sai số đo trung bình |mean - true| trước và sau lọc (Thang Logarit)
fig2, ax2 = plt.subplots(figsize=(9.5, 5), dpi=300)
ax2.plot(d_list, err_raw, color='#d62728', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='Sai số tuyệt đối dữ liệu thô (Trước lọc)')
ax2.plot(d_list, err_clean, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Sai số tuyệt đối sau lọc IQR')
ax2.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')
ax2.set_yscale('log')
ax2.set_title("ĐỘ LỆCH CỦA GIÁ TRỊ TRUNG BÌNH SO VỚI CHUẨN ĐỐI CHỨNG TRƯỚC VÀ SAU LỌC IQR", fontweight='bold', pad=12)
ax2.set_xlabel("Khoảng cách đặt chuẩn đối chứng (cm)", fontweight='bold')
ax2.set_ylabel("Độ lệch tuyệt đối |d_tb - d_chuan| (mm) - Thang logarit", fontweight='bold')
ax2.set_xlim(-10, 620)
ax2.grid(True, which="both", linestyle=':', alpha=0.6)
ax2.legend(loc='lower right', framealpha=0.95)
plt.tight_layout()
fig2.savefig(Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\test_pa2_mean_err.png"))
plt.close(fig2)

print("Đã tạo xong 2 phương án test đồ thị đơn!")
