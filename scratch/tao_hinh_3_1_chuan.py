import csv
import math
import statistics
from pathlib import Path
import matplotlib.pyplot as plt

# Cấu hình chuẩn thẩm mỹ theo GEMINI.md
plt.rcParams['font.family'] = 'Segoe UI'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 8.5
plt.rcParams['figure.titlesize'] = 12

BASE_DIR = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601")
GRAPH_DIR = BASE_DIR / "graph"
GRAPH_C3_DIR = GRAPH_DIR / "chuong_3"
GRAPH_C3_DIR.mkdir(parents=True, exist_ok=True)
AGG_DIR = BASE_DIR / "du_lieu_tong_hop"

def load_col(fname, col_name):
    with open(AGG_DIR / fname, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [float(row[col_name]) for row in reader]

v_580 = load_col("FSDT.csv", "580cm")
v_350 = load_col("FRDT.csv", "350cm")

def get_iqr_stats(vals):
    q1, med, q3 = statistics.quantiles(vals, n=4, method='inclusive')
    iqr = max(q3 - q1, 0.0175)
    lf = q1 - 1.5 * iqr
    uf = q3 + 1.5 * iqr
    m_raw = statistics.mean(vals)
    valid_pts = [(i+1, x) for i, x in enumerate(vals) if lf <= x <= uf]
    outlier_pts = [(i+1, x) for i, x in enumerate(vals) if x < lf or x > uf]
    m_clean = statistics.mean([x for _, x in valid_pts])
    s_clean = statistics.stdev([x for _, x in valid_pts])
    return q1, med, q3, iqr, lf, uf, m_raw, m_clean, s_clean, valid_pts, outlier_pts

q1_1, med_1, q3_1, iqr_1, lf_1, uf_1, m_raw_1, m_clean_1, s_clean_1, val_1, out_1 = get_iqr_stats(v_580)
q1_2, med_2, q3_2, iqr_2, lf_2, uf_2, m_raw_2, m_clean_2, s_clean_2, val_2, out_2 = get_iqr_stats(v_350)

print("Vẽ Hình 3.1 chuẩn quy tắc không mũi tên, không vùng bóng...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Subplot 1: FSDT 580cm
ax1.plot([x[0] for x in val_1], [x[1] for x in val_1], linestyle='None', marker='o', markersize=4.5, color='#1f77b4', label=f'Mẫu hợp lệ ({len(val_1)} mẫu)')
ax1.plot([x[0] for x in out_1], [x[1] for x in out_1], linestyle='None', marker='x', markersize=7.0, markeredgewidth=2.0, color='#d62728', label=f'Ngoại lai bị loại ({len(out_1)} mẫu)')

ax1.axhline(m_raw_1, color='#d62728', linestyle='--', linewidth=1.3, label=f'Mean thô: {m_raw_1:.2f} cm')
ax1.axhline(m_clean_1, color='#2ca02c', linestyle='-', linewidth=1.5, label=f'Mean sạch: {m_clean_1:.2f} cm')
ax1.axhline(med_1, color='#333333', linestyle=':', linewidth=1.2, label=f'Median: {med_1:.2f} cm')
ax1.axhline(lf_1, color='#7f7f7f', linestyle='-.', linewidth=1.1, label=f'Hàng rào LF ({lf_1:.2f} cm)')
ax1.axhline(uf_1, color='#7f7f7f', linestyle='-.', linewidth=1.1, label=f'Hàng rào UF ({uf_1:.2f} cm)')

ax1.set_title("LỌC NGOẠI LAI TIMEOUT CỰ LY XA (FSDT - 580 cm)", fontweight='bold', pad=10)
ax1.set_xlabel("Thứ tự lần đo k", fontweight='bold')
ax1.set_ylabel("Khoảng cách đo (cm)", fontweight='bold')
ax1.set_xlim(0, 51)
ax1.set_ylim(575, 835)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper right', framealpha=0.92)

# Subplot 2: FRDT 350cm
ax2.plot([x[0] for x in val_2], [x[1] for x in val_2], linestyle='None', marker='s', markersize=4.5, color='#ff7f0e', label=f'Mẫu hợp lệ ({len(val_2)} mẫu)')
ax2.plot([x[0] for x in out_2], [x[1] for x in out_2], linestyle='None', marker='x', markersize=7.0, markeredgewidth=2.0, color='#d62728', label=f'Ngoại lai bị loại ({len(out_2)} mẫu)')

ax2.axhline(m_raw_2, color='#d62728', linestyle='--', linewidth=1.3, label=f'Mean thô: {m_raw_2:.2f} cm')
ax2.axhline(m_clean_2, color='#2ca02c', linestyle='-', linewidth=1.5, label=f'Mean sạch: {m_clean_2:.2f} cm')
ax2.axhline(med_2, color='#333333', linestyle=':', linewidth=1.2, label=f'Median: {med_2:.2f} cm')
ax2.axhline(lf_2, color='#7f7f7f', linestyle='-.', linewidth=1.1, label=f'Hàng rào LF ({lf_2:.2f} cm)')
ax2.axhline(uf_2, color='#7f7f7f', linestyle='-.', linewidth=1.1, label=f'Hàng rào UF ({uf_2:.2f} cm)')

ax2.set_title("LỌC NGOẠI LAI TÁN XẠ KHUẾCH TÁN (FRDT - 350 cm)", fontweight='bold', pad=10)
ax2.set_xlabel("Thứ tự lần đo k", fontweight='bold')
ax2.set_ylabel("Khoảng cách đo (cm)", fontweight='bold')
ax2.set_xlim(0, 51)
ax2.set_ylim(345, 835)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', framealpha=0.92)

plt.tight_layout()

# Lưu cả 2 vị trí để tương thích
p1 = GRAPH_DIR / "hinh_3_1_loc_sai_so_tho.png"
p2 = GRAPH_C3_DIR / "hinh_3_1_loc_sai_so_tho.png"
fig.savefig(p1)
fig.savefig(p2)
plt.close(fig)

print(f"Đã xuất đồ thị Hình 3.1 tại: {p1} và {p2}")
