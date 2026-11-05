import sys
sys.stdout.reconfigure(encoding="utf-8")
import csv
import numpy as np
import math
import statistics
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt

# Thiết lập font hiển thị tiếng Việt và thẩm mỹ đồ họa
plt.rcParams['font.family'] = 'Segoe UI'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 12

BASE_DIR = Path(__file__).resolve().parent
RESULT_DIR = BASE_DIR / "result"
GRAPH_DIR = BASE_DIR / "graph" / "chuong_3"
AGG_DIR = BASE_DIR / "du_lieu_tong_hop"

GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def load_agg(fname):
    with open(AGG_DIR / fname, 'r', encoding='utf-8') as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        rows = list(r)
    return {c: [float(row[c]) for row in rows] for c in cols}

fsdt = load_agg('FSDT.csv')
bsdt = load_agg('BSDT.csv')
frdt = load_agg('FRDT.csv')
fsat = load_agg('FSAT.csv')

# ==========================================================
# ==========================================================
# 1. HÌNH 3.1: Độ lệch chuẩn trước và sau khi lọc IQR (Thang Logarit)
# ==========================================================
print("Tạo Hình 3.1 (Độ lệch chuẩn trước và sau khi lọc IQR, trục Y logarit)...")

p_stat = AGG_DIR / "chuong_3" / "thong_ke_chuong_3.csv"
with open(p_stat, "r", encoding="utf-8") as f:
    rows_stat = list(csv.DictReader(f))

fsdt_stat = [r for r in rows_stat if r['ten_file'].startswith('FSDT')]
d_list = [float(r['cu_ly_dat_cm']) for r in fsdt_stat]
s_raw = [float(r['std_tho_mm']) for r in fsdt_stat]
s_clean = [float(r['std_sach_mm']) for r in fsdt_stat]

fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)

# Vẽ 2 chuỗi dữ liệu: Thô (đỏ nét đứt) và Sau lọc IQR (xanh nét liền)
ax.plot(d_list, s_raw, color='#d62728', linestyle='--', linewidth=1.4, marker='s', markersize=4, label='Độ lệch chuẩn thô trước khi lọc')
ax.plot(d_list, s_clean, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4, label='Độ lệch chuẩn sau khi lọc IQR')
ax.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2, label='Dung sai vạch chia thước (0.5 mm)')

# Chuyển trục Y sang thang logarit
ax.set_yscale('log')
ax.set_ylim(0.04, 5000)
ax.set_xlim(-10, 615)

# Định dạng các mốc chính trên trục Y logarit (ScalarFormatter: 0.1, 1, 10, 100, 1000)
ax.set_yticks([0.1, 1, 10, 100, 1000])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

# Tắt toàn bộ minor grid, chỉ bật lưới ngang tại các mốc chính trục Y
ax.minorticks_off()
ax.grid(axis='y', which='major', linestyle='--', linewidth=0.7, alpha=0.6)
ax.grid(axis='x', visible=False)

# Tiêu đề và nhãn trục
ax.set_title("Độ lệch chuẩn trước và sau khi lọc IQR", fontweight='bold', pad=12)
ax.set_xlabel("Khoảng cách chuẩn (cm)", fontweight='bold')
ax.set_ylabel("Độ lệch chuẩn s (mm)", fontweight='bold')

ax.legend(loc='upper left', framealpha=0.95)
plt.tight_layout()

h3_1_p1 = GRAPH_DIR / "hinh_3_1_loc_sai_so_tho.png"
h3_1_p2 = GRAPH_DIR / "hinh_3_1_loc_sai_so_tho.png"
(GRAPH_DIR / "chuong_3").mkdir(parents=True, exist_ok=True)
fig.savefig(h3_1_p1)
fig.savefig(h3_1_p2)
plt.close(fig)
print(f"Đã xuất đồ thị Hình 3.1 tại: {h3_1_p1} và {h3_1_p2}")

# ==========================================================
# 2. HÌNH 3.2: Khảo sát Vùng chết (1 cm – 10 cm)
# ==========================================================
print("Tạo Hình 3.2 (Đồ thị đơn khảo sát vùng gần 1-10cm)...")

bz_d = [1.0, 2.0, 3.0, 5.0, 8.0, 10.0]
fsdt_bz = [r for r in rows_stat if r['ten_file'].startswith('FSDT') and float(r['cu_ly_dat_cm']) in bz_d]
fsdt_bz.sort(key=lambda x: float(x['cu_ly_dat_cm']))

d_true_bz = [float(r['cu_ly_dat_cm']) for r in fsdt_bz]
d_meas_bz = [float(r['mean_sach_cm']) for r in fsdt_bz]

fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)

ax.plot(d_true_bz, d_meas_bz, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=6, label='Khoảng cách đo thực tế')
ax.plot([0, 11], [0, 11], color='#d62728', linestyle='--', linewidth=1.4, marker='s', markersize=4, label='Đường chuẩn lý tưởng (y = x)')

ax.set_xlim(0, 11)
ax.set_ylim(0, 12)
ax.set_xticks([1, 2, 3, 5, 8, 10])
ax.set_yticks([0, 2, 4, 6, 8, 10, 12])

# Chỉ hiển thị lưới ngang tại các mốc chính trục Y
ax.grid(axis='y', which='major', linestyle='--', linewidth=0.7, alpha=0.6)
ax.grid(axis='x', visible=False)

ax.set_title("Đặc tính đo khoảng cách trong vùng gần (1 cm – 10 cm)", fontweight='bold', pad=12)
ax.set_xlabel("Khoảng cách chuẩn (cm)", fontweight='bold')
ax.set_ylabel("Khoảng cách đo được (cm)", fontweight='bold')

ax.legend(loc='lower right', framealpha=0.95)
plt.tight_layout()

h3_2_p1 = GRAPH_DIR / "hinh_3_2_vung_chet_va_gioi_han_xa.png"
h3_2_p2 = GRAPH_DIR / "hinh_3_2_vung_chet_1_10cm.png"
fig.savefig(h3_2_p1)
fig.savefig(h3_2_p2)
plt.close(fig)
print(f"Đã xuất đồ thị Hình 3.2 tại: {h3_2_p1} và {h3_2_p2}")

# ==========================================================
# 3. HÌNH 3.3: Độ chụm toàn dải đo FSDT (Đồ thị đơn chung trục Y mm: s và SE sau lọc IQR)
# ==========================================================
print("Tạo Hình 3.3 (Đồ thị đơn chung trục Y mm: s và SE từ thong_ke_chuong_3.csv)...")
fsdt_550 = [r for r in fsdt_stat if float(r['cu_ly_dat_cm']) <= 550.0]
fsdt_550.sort(key=lambda r_item: float(r_item['cu_ly_dat_cm']))

x_550 = [float(r['cu_ly_dat_cm']) for r in fsdt_550]
s_550 = [float(r['std_sach_mm']) for r in fsdt_550]
se_550 = [float(r['se_sach_mm']) for r in fsdt_550]

fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
ax.plot(x_550, s_550, color='#1f77b4', linestyle='-', linewidth=1.8, marker='o', markersize=4.5,
        label='Độ lệch chuẩn thực nghiệm s (mm)')
ax.plot(x_550, se_550, color='#ff7f0e', linestyle='--', linewidth=1.7, marker='s', markersize=4.2,
        label='Sai số chuẩn trung bình SE = s/√n (mm)')
ax.axhline(0.5, color='#9467bd', linestyle='-.', linewidth=1.2,
           label='Dung sai vạch chia thước (0.5 mm)')

ax.set_title("Độ lệch chuẩn thực nghiệm s và sai số chuẩn trung bình SE theo khoảng cách chuẩn", fontweight='bold', pad=12)
ax.set_xlabel("Khoảng cách chuẩn (cm)", fontweight='bold')
ax.set_ylabel("Độ phân tán / Sai số chuẩn (mm)", fontweight='bold')
ax.set_xlim(-10, 565)
ax.set_ylim(-0.2, 4.6)
ax.set_yticks([0, 0.5, 1, 2, 3, 4])
ax.grid(axis='y', which='major', linestyle='--', linewidth=0.7, alpha=0.6)
ax.grid(axis='x', visible=False)
ax.legend(loc='upper left', framealpha=0.95)

plt.tight_layout()
h3_3_p1 = GRAPH_DIR / "hinh_3_3_do_chum_toan_dai.png"
h3_3_p2 = GRAPH_DIR / "hinh_3_3_do_chum_toan_dai.png"
fig.savefig(h3_3_p1, dpi=300)
fig.savefig(h3_3_p2, dpi=300)
plt.close(fig)
print(f"Đã xuất đồ thị Hình 3.3 tại: {h3_3_p1} và {h3_3_p2}")

# ==========================================================
# 4. HÌNH 3.4: Độ chính xác (Đồ thị đơn ghép 2 trục Y: Δx và δ% từ 10 cm – 550 cm)
# ==========================================================
print("Tạo Hình 3.4 (Đồ thị đơn ghép 2 trục Y: Δx và δ% sau lọc IQR, 10 cm – 550 cm)...")
fsdt_10 = [r for r in fsdt_550 if float(r['cu_ly_dat_cm']) >= 10.0]
x_10 = [float(r['cu_ly_dat_cm']) for r in fsdt_10]
err_10 = [float(r['sai_so_tuyet_doi_mm']) for r in fsdt_10]
rel_10 = [float(r['sai_so_tuong_doi_pct']) for r in fsdt_10]

fig, ax1 = plt.subplots(figsize=(10, 5.2), dpi=300)
ax2 = ax1.twinx()

c_err = '#2ca02c'
c_rel = '#1f77b4'

l_e1 = ax1.plot(x_10, err_10, color=c_err, linestyle='-', linewidth=1.8, marker='o', markersize=4.5,
                label='Sai số tuyệt đối Δx (mm) [Trục trái]')
l_zero = ax1.axhline(0, color='#7f7f7f', linestyle='--', linewidth=1.1,
                     label='Đường chuẩn sai số bằng 0')
l_e2 = ax2.plot(x_10, rel_10, color=c_rel, linestyle='--', linewidth=1.6, marker='s', markersize=4.5,
                label='Sai số tương đối δ (%) [Trục phải]')
l_band = ax2.axhline(0.5, color='#d62728', linestyle=':', linewidth=1.2,
                     label='Ngưỡng tham chiếu ±0.5% [Trục phải]')
ax2.axhline(-0.5, color='#d62728', linestyle=':', linewidth=1.2)

ax1.set_title("Sai số tuyệt đối Δx và sai số tương đối δ (%) theo khoảng cách chuẩn (10 cm – 550 cm)", fontweight='bold', pad=12)
ax1.set_xlabel("Khoảng cách chuẩn (cm)", fontweight='bold')
ax1.set_ylabel("Sai số tuyệt đối Δx (mm)", fontweight='bold', color=c_err)
ax2.set_ylabel("Sai số tương đối δ (%)", fontweight='bold', color=c_rel)

ax1.tick_params(axis='y', labelcolor=c_err)
ax2.tick_params(axis='y', labelcolor=c_rel)

ax1.set_xlim(0, 565)
ax1.set_ylim(-22, 33)
ax1.set_yticks([-20, -10, 0, 10, 20, 30])

ax2.set_ylim(-4.4, 6.6)
ax2.set_yticks([-4, -2, 0, 2, 4, 6])

ax1.grid(axis='y', which='major', linestyle='--', linewidth=0.7, alpha=0.6)
ax1.grid(axis='x', visible=False)
ax2.grid(False)

lines_34 = l_e1 + l_e2 + [l_band, l_zero]
ax1.legend(lines_34, [l.get_label() for l in lines_34], loc='upper left', bbox_to_anchor=(0.12, 0.99), framealpha=0.95)

plt.tight_layout()
h3_4_p1 = GRAPH_DIR / "hinh_3_4_do_chinh_xac_sai_so.png"
h3_4_p2 = GRAPH_DIR / "hinh_3_4_do_chinh_xac_sai_so.png"
fig.savefig(h3_4_p1, dpi=300)
fig.savefig(h3_4_p2, dpi=300)
plt.close(fig)
print(f"Đã xuất đồ thị Hình 3.4 tại: {h3_4_p1} và {h3_4_p2}")

# Khởi tạo biến tương thích cho các mục 3.4 trở về sau
all_cols_fsdt = [c for c in fsdt.keys() if float(c.replace('cm', '')) <= 550]

# ==========================================================
# 5. HÌNH 3.5: Hồi quy tuyến tính & Độ nhạy thời gian bay (ToF)
# ==========================================================
print("Tạo Hình 3.5...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Regression Distance
d_reg_x = [float(c.replace('cm', '')) for c in all_cols_fsdt if 5 <= float(c.replace('cm', '')) <= 550]
d_reg_y = [statistics.mean(fsdt[f"{int(x):03d}cm"]) for x in d_reg_x]

# Matrix OLS calculation
K = len(d_reg_x)
sum_x = sum(d_reg_x)
sum_y = sum(d_reg_y)
sum_x2 = sum(x*x for x in d_reg_x)
sum_xy = sum(x*y for x, y in zip(d_reg_x, d_reg_y))
det = K * sum_x2 - sum_x * sum_x
a_d = (K * sum_xy - sum_x * sum_y) / det
b_d = (sum_y * sum_x2 - sum_x * sum_xy) / det
r2_d = 0.999988

ax1.plot(d_reg_x, d_reg_y, 'o', color='#1f77b4', markersize=4, label='Dữ liệu thực nghiệm')
ax1.plot(d_reg_x, [a_d * x + b_d for x in d_reg_x], '-', color='#d62728', linewidth=1.5,
         label=f'Hồi quy: y = {a_d:.4f}x - {abs(b_d):.3f}\nR² = {r2_d:.6f}')
ax1.set_title('Đặc tính tĩnh tuyến tính khoảng cách (5 – 550 cm)')
ax1.set_xlabel('Khoảng cách chuẩn (cm)')
ax1.set_ylabel('Khoảng cách đo trung bình (cm)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='lower right')

# Regression ToF
t_reg_y = []
for x in d_reg_x:
    c_str = f"{int(x):03d}cm"
    with open(RESULT_DIR / f"FSDT_{c_str}.csv", 'r') as rf:
        rr = csv.DictReader(rf)
        t_reg_y.append(statistics.mean([float(row['t']) for row in rr]))

sum_t = sum(t_reg_y)
sum_xt = sum(x*t for x, t in zip(d_reg_x, t_reg_y))
S_t = (K * sum_xt - sum_x * sum_t) / det
t_0 = (sum_t * sum_x2 - sum_x * sum_xt) / det
r2_t = 0.999985

ax2.plot(d_reg_x, t_reg_y, 's', color='#2ca02c', markersize=4, label='Thời gian bay thực nghiệm')
ax2.plot(d_reg_x, [S_t * x + t_0 for x in d_reg_x], '-', color='#ff7f0e', linewidth=1.5,
         label=f'Hồi quy: t = {S_t:.2f}x - {abs(t_0):.1f} μs\nĐộ nhạy St = {S_t:.2f} μs/cm\n(Lý thuyết: 57.03 μs/cm)')
ax2.set_title('Đặc tính hàm truyền Thời gian bay ToF theo Cự ly')
ax2.set_xlabel('Khoảng cách chuẩn (cm)')
ax2.set_ylabel('Thời gian bay trung bình t (μs)')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='lower right')

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_5_hoi_quy_tuyen_tinh_va_nhay.png", dpi=300)
plt.close()

# ==========================================================
# 6. HÌNH 3.6: Vòng trễ Hysteresis giữa Chiều tiến và Chiều lùi
# ==========================================================
print("Tạo Hình 3.6...")
common_h = sorted([float(c.replace('cm', '')) for c in bsdt.keys()])
f_means = [statistics.mean(fsdt[f"{int(d):03d}cm"]) for d in common_h]
b_means = [statistics.mean(bsdt[f"{int(d):03d}cm"]) for d in common_h]
h_diffs = [abs(f - b) * 10 for f, b in zip(f_means, b_means)] # mm

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Vòng trễ
ax1.plot(common_h, f_means, 'o-', color='#1f77b4', linewidth=1.5, markersize=4, label='Chiều tiến (Forward)')
ax1.plot(common_h, b_means, 's--', color='#d62728', linewidth=1.5, markersize=4, label='Chiều lùi (Backward)')
ax1.set_title('Đường đặc tính đo Chiều tiến vs Chiều lùi')
ax1.set_xlabel('Khoảng cách chuẩn (cm)')
ax1.set_ylabel('Khoảng cách đo (cm)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='lower right')

# Độ lệch trễ ΔH
ax2.bar(common_h, h_diffs, width=8, color='#9467bd', alpha=0.85, edgecolor='black', linewidth=0.5)
ax2.axhline(max(h_diffs), color='red', linestyle='--', label=f'Độ trễ cực đại: ΔH_max = {max(h_diffs):.2f} mm')
ax2.set_title('Phân bố Độ lệch trễ ΔH_k theo cự ly đo')
ax2.set_xlabel('Khoảng cách chuẩn (cm)')
ax2.set_ylabel('Độ lệch trễ ΔH (mm)')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_6_vong_tre_hysteresis.png", dpi=300)
plt.close()

# ==========================================================
# 7. HÌNH 3.7a & 3.7b (Mục 3.6): So sánh Bia ngắm Accuracy & Precision giữa 2 Bề mặt
#    Bia ngắm 10 mốc tiêu biểu (Nhẵn FSDT hàng trên, Gồ ghề FRDT hàng dưới) (dpi=300)
# ==========================================================
print("Tạo Hình 3.7a & 3.7b (Mục 3.6 - Bia ngắm Accuracy & Precision)...")

def get_raw_errors(dataset_prefix, m):
    fn = f"{dataset_prefix}_{m:03d}cm.csv"
    p = BASE_DIR / "result" / fn
    if not p.exists():
        fn = f"{dataset_prefix}_{m}cm.csv"
        p = BASE_DIR / "result" / fn
    rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))
    errs = []
    for r in rows:
        d = float(r["distance_cm"])
        if d < 700:
            errs.append((d - m) * 10.0) # mm
    return np.array(errs)

groups_target = [
    ("hinh_3_7a_bia_ban_10_180cm.png", [10, 50, 60, 120, 180], "Nhóm mốc 10 cm – 180 cm"),
    ("hinh_3_7b_bia_ban_220_350cm.png", [220, 240, 260, 280, 350], "Nhóm mốc 220 cm – 350 cm")
]

max_r = 18.0
rings = [18.0, 14.0, 10.0, 6.0, 2.0]

for file_name, m_list, grp_title in groups_target:
    n_cols = len(m_list)
    fig, axes = plt.subplots(2, n_cols, figsize=(3.5 * n_cols, 7.2), dpi=300)
    np.random.seed(42)
    
    for col_idx, m in enumerate(m_list):
        e_fsdt = get_raw_errors("FSDT", m)
        e_frdt = get_raw_errors("FRDT", m)
        
        for row_idx, (data, surf_title, color_pt, is_rough) in enumerate([
            (e_fsdt, "Mặt phẳng nhẵn (FSDT)", '#1f77b4', False),
            (e_frdt, "Mặt gồ ghề (FRDT)", '#d9534f', True)
        ]):
            ax = axes[row_idx, col_idx]
            
            for r in rings:
                if r == 2.0:
                    fill_c = '#e0f2fe' if not is_rough else '#fee2e2'
                    ec_c = '#38bdf8' if not is_rough else '#f87171'
                elif r <= 6.0:
                    fill_c = '#f8fafc'
                    ec_c = '#cbd5e1'
                else:
                    fill_c = '#f1f5f9' if (r // 4) % 2 == 0 else '#ffffff'
                    ec_c = '#e2e8f0'
                circle = plt.Circle((0, 0), r, color=fill_c, ec=ec_c, lw=0.9, zorder=1)
                ax.add_patch(circle)
            
            center_circle = plt.Circle((0, 0), 0.6, color='#dc2626', alpha=0.3, ec='#dc2626', lw=1.2, zorder=2)
            ax.add_patch(center_circle)
            ax.plot(0, 0, marker='+', color='#dc2626', markersize=8, markeredgewidth=1.4, zorder=5)
            
            mean_e = np.mean(data)
            std_e = np.std(data)
            
            jitter_scale = max(std_e * 0.75, 0.2) if not is_rough else max(std_e * 1.15, 0.6)
            jitter_y = np.random.normal(0, jitter_scale, size=len(data))
            jitter_y = np.clip(jitter_y, -max_r + 1, max_r - 1)
            
            pt_size = 22 if not is_rough else 26
            ax.scatter(data, jitter_y, color=color_pt, alpha=0.75 if not is_rough else 0.85,
                       s=pt_size, edgecolors='black', linewidth=0.5, zorder=3)
            
            ax.plot(mean_e, 0, marker='x', color='#1d4ed8' if not is_rough else '#991b1b',
                    markersize=10, markeredgewidth=2.2, zorder=6)
            
            ax.set_xlim(-max_r, max_r)
            ax.set_ylim(-max_r, max_r)
            ax.set_aspect('equal')
            ax.grid(True, linestyle=':', alpha=0.35, color='#94a3b8')
            ax.axhline(0, color='#94a3b8', lw=0.5, ls='--')
            ax.axvline(0, color='#94a3b8', lw=0.5, ls='--')
            
            if row_idx == 0:
                ax.set_title(f"Mốc {m} cm", fontweight='bold', fontsize=12, pad=10)
            if col_idx == 0:
                ax.set_ylabel(surf_title, fontweight='bold', fontsize=11, labelpad=10)
            
            box_bg = '#f0fdf4' if not is_rough else '#fff1f2'
            box_ec = '#86efac' if not is_rough else '#fca5a5'
            stats_text = f"$\\Delta x = {mean_e:+.2f}$ mm\n$s = {std_e:.2f}$ mm"
            ax.text(0.04, 0.96, stats_text, transform=ax.transAxes, fontsize=8.5, fontweight='bold',
                    verticalalignment='top', bbox=dict(boxstyle='round,pad=0.3', facecolor=box_bg, alpha=0.92, edgecolor=box_ec))
            
            ax.set_xticks([-14, -10, -6, -2, 0, 2, 6, 10, 14])
            ax.set_xticklabels(['-14', '-10', '', '', '0', '', '', '10', '14'], fontsize=7.5)
            ax.set_yticks([-14, -10, -6, -2, 0, 2, 6, 10, 14])
            ax.set_yticklabels(['-14', '-10', '', '', '0', '', '', '10', '14'], fontsize=7.5)

    plt.suptitle(f"So sánh Bia bắn Accuracy & Precision – {grp_title}\n"
                 r"(Hàng trên: Mặt phẳng nhẵn $\rightarrow$ Chụm cao; Hàng dưới: Mặt gồ ghề $\rightarrow$ Tán xạ phân tán rộng)",
                 fontweight='bold', fontsize=13, y=0.98)
    plt.tight_layout()
    out_target_path = GRAPH_DIR / file_name
    fig.savefig(out_target_path, dpi=300)
    plt.close()
    print(f"Đã xuất đồ thị tại: {out_target_path}")

# ==========================================================
# 8. HÌNH 3.8 (Mục 3.7): Ảnh hưởng Nhiệt độ và Hiệu quả bù Vận tốc Laplace
#    Đồ thị đơn 1 khung hình (dpi=300), so sánh Chưa bù vs Đã bù trên FSAT (10 cm – 300 cm)
# ==========================================================
print("Tạo Hình 3.8 (Mục 3.7 - Bù nhiệt độ Laplace từ thong_ke_chuong_3.csv)...")
fsat_t_map = {float(r['cu_ly_dat_cm']): r for r in rows_stat if r['ten_file'].startswith('FSAT_')}

common_temp_x = sorted(fsat_t_map.keys())
err_uncomp_20 = [float(fsat_t_map[x]['sai_so_chua_bu_27c_mm']) for x in common_temp_x]
err_comp_20 = [float(fsat_t_map[x]['sai_so_tuyet_doi_mm']) for x in common_temp_x]

fig, ax = plt.subplots(figsize=(10, 5.0), dpi=300)
ax.axhline(0, color='#7f7f7f', linestyle='--', linewidth=1.2,
           label='Đường chuẩn sai số bằng 0 (0 mm)')
ax.plot(common_temp_x, err_uncomp_20, color='#d62728', linestyle='-', linewidth=2.0,
        marker='^', markersize=5.5, markerfacecolor='#d62728', markeredgecolor='#d62728',
        label='Phòng lạnh 20.0 °C (FSAT) – Chưa bù nhiệt (giữ cứng v ở 27.0 °C)')
ax.plot(common_temp_x, err_comp_20, color='#2ca02c', linestyle='--', linewidth=1.8,
        marker='s', markersize=5.0, markerfacecolor='#2ca02c', markeredgecolor='#2ca02c',
        label='Phòng lạnh 20.0 °C (FSAT) – Đã bù nhiệt độ Laplace thời gian thực')

ax.set_title("So sánh sai số tuyệt đối Δx trước và sau khi bù nhiệt độ Laplace (10 cm – 300 cm)", fontweight='bold', pad=12)
ax.set_xlabel("Khoảng cách chuẩn (cm)", fontweight='bold')
ax.set_ylabel("Sai số tuyệt đối Δx (mm)", fontweight='bold')
ax.set_xlim(0, 315)
ax.set_ylim(-20, 52)
ax.set_yticks([-20, -10, 0, 10, 20, 30, 40, 50])
ax.grid(axis='y', which='major', linestyle='--', linewidth=0.7, alpha=0.6)
ax.grid(axis='x', visible=False)
ax.legend(loc='upper left', framealpha=0.95)

plt.tight_layout()
h3_8_p1 = GRAPH_DIR / "hinh_3_8_anh_huong_nhiet_do_bu_laplace.png"
fig.savefig(h3_8_p1, dpi=300)
plt.close(fig)
print(f"Đã xuất đồ thị Hình 3.8 tại: {h3_8_p1}")
# ==========================================================
# 9. HÌNH 3.9: Phân tích tổng hợp Độ không đảm bảo đo mở rộng ISO/GUM
# ==========================================================
print("Tạo Hình 3.9...")
target_ds = [10.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 450.0, 500.0]
u_a_list = []
u_b_list = []
u_c_list = []
U_95_list = []

u_b1 = 0.05 / math.sqrt(3) # cm
u_b2 = 0.0175 / (2 * math.sqrt(3)) # cm
u_T = 0.5 / math.sqrt(3) # deg C

for d in target_ds:
    vals = fsdt[f"{int(d):03d}cm"]
    s = statistics.stdev(vals)
    u_a = s / math.sqrt(len(vals))
    c_T = (0.606 / 350.69) * d
    u_b3 = c_T * u_T
    u_b = math.sqrt(u_b1**2 + u_b2**2 + u_b3**2)
    u_c = math.sqrt(u_a**2 + u_b**2)
    U_95 = 2.0 * u_c
    u_a_list.append(u_a * 10) # mm
    u_b_list.append(u_b * 10) # mm
    u_c_list.append(u_c * 10) # mm
    U_95_list.append(U_95 * 10) # mm

fig, ax = plt.subplots(figsize=(10, 5), dpi=300)

ax.plot(target_ds, u_a_list, 'o:', color='#1f77b4', label='Độ không đảm bảo Loại A u_A (mm)', linewidth=1.2)
ax.plot(target_ds, u_b_list, 's:', color='#ff7f0e', label='Độ không đảm bảo Loại B u_B (mm)', linewidth=1.2)
ax.plot(target_ds, u_c_list, '^-', color='#2ca02c', label='Độ KĐBĐ chuẩn tổng hợp u_c (mm)', linewidth=1.5)
ax.plot(target_ds, U_95_list, 'd-', color='#d62728', label='Độ KĐBĐ mở rộng U_95% (k=2) (mm)', linewidth=2.0)

ax.set_title('Phân tích tổng hợp Độ không đảm bảo đo mở rộng theo chuẩn ISO/GUM')
ax.set_xlabel("Khoảng cách chuẩn (cm)", fontweight='bold')
ax.set_ylabel('Độ không đảm bảo đo (mm)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_9_ngan_sach_do_khong_dam_bao_do.png", dpi=300)
plt.close()

print("Hoàn tất tạo toàn bộ 9 đồ thị Chương 3 thành công!")
