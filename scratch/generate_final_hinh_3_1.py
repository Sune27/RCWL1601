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

BASE_DIR = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601")
p_stat = BASE_DIR / "du_lieu_tong_hop" / "chuong_3" / "thong_ke_chuong_3.csv"
GRAPH_C3_DIR = BASE_DIR / "graph" / "chuong_3"
GRAPH_DIR = BASE_DIR / "graph"
GRAPH_C3_DIR.mkdir(parents=True, exist_ok=True)

with open(p_stat, "r", encoding="utf-8") as f:
    rows_stat = list(csv.DictReader(f))

# Lấy đầy đủ toàn bộ 35 mốc cự ly từ 1cm đến 600cm
fsdt_stat = [r for r in rows_stat if r['ten_file'].startswith('FSDT')]
d_list = [float(r['cu_ly_dat_cm']) for r in fsdt_stat]
s_raw = [float(r['std_tho_mm']) for r in fsdt_stat]
s_clean = [float(r['std_sach_mm']) for r in fsdt_stat]

fig, ax = plt.subplots(figsize=(10.5, 5), dpi=300)

ax.plot(d_list, s_clean, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Dữ liệu sau khi làm sạch bằng IQR (s ≤ 4.0 mm)')
ax.plot(d_list, s_raw, color='#d62728', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='Dữ liệu thô ban đầu (Trước lọc)')
ax.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')

# y max là 8, x max vẽ đến 600
ax.set_ylim(-0.2, 8.0)
ax.set_xlim(-10, 615)

# Chỉ bật lưới ngang tại các mốc chính trục Y (0, 2, 4, 6, 8)
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.5)

ax.set_title("HIỆU QUẢ TRIỆT TIÊU ĐỘ LỆCH CHUẨN THỰC NGHIỆM TRƯỚC VÀ SAU LỌC IQR", fontweight='bold', pad=12)
ax.set_xlabel("Khoảng cách đặt chuẩn đối chứng (cm)", fontweight='bold')
ax.set_ylabel("Độ lệch chuẩn thực nghiệm s (mm)", fontweight='bold')

# Hộp nhãn hướng lên cao tại các điểm vượt ngưỡng (> 8mm)
# 1. Mốc 360cm (s = 90.3 mm)
ax.text(360, 7.35, "360cm: s = 90.3 mm ↑", color='#d62728', fontsize=8.2, fontweight='bold', ha='center',
        bbox=dict(boxstyle='square,pad=0.25', facecolor='white', edgecolor='#d62728', alpha=0.9))

# 2. Mốc 580cm (s = 346.1 mm) và 600cm (s = 2621.0 mm) so le hoặc tách biệt để không đè nhau
ax.text(545, 7.35, "580cm: s = 346.1 mm ↑", color='#d62728', fontsize=8.2, fontweight='bold', ha='right',
        bbox=dict(boxstyle='square,pad=0.25', facecolor='white', edgecolor='#d62728', alpha=0.9))

ax.text(610, 6.4, "600cm: s = 2621.0 mm ↑", color='#d62728', fontsize=8.2, fontweight='bold', ha='right',
        bbox=dict(boxstyle='square,pad=0.25', facecolor='white', edgecolor='#d62728', alpha=0.9))

ax.legend(loc='upper left', framealpha=0.95)
plt.tight_layout()

p_c3 = GRAPH_C3_DIR / "hinh_3_1_loc_sai_so_tho.png"
p_root = GRAPH_DIR / "hinh_3_1_loc_sai_so_tho.png"
fig.savefig(p_c3)
fig.savefig(p_root)
plt.close(fig)
print(f"Đã lưu thành công Hình 3.1 tại: {p_c3}")
