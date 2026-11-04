import csv
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

BASE_DIR = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601")
RESULT_DIR = BASE_DIR / "result"
GRAPH_DIR = BASE_DIR / "graph"
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
h3_1_p2 = GRAPH_DIR / "chuong_3" / "hinh_3_1_loc_sai_so_tho.png"
(GRAPH_DIR / "chuong_3").mkdir(parents=True, exist_ok=True)
fig.savefig(h3_1_p1)
fig.savefig(h3_1_p2)
plt.close(fig)
print(f"Đã xuất đồ thị Hình 3.1 tại: {h3_1_p1} và {h3_1_p2}")

# ==========================================================
# 2. HÌNH 3.2: Sai số tương đối theo khoảng cách chuẩn (FSDT)
# ==========================================================
print("Tạo Hình 3.2 (Sai số tương đối theo khoảng cách chuẩn, y_lim = [-10.5, 10.5])...")

fsdt_stat = [r for r in rows_stat if r['ten_file'].startswith('FSDT')]
d_list_32 = [float(r['cu_ly_dat_cm']) for r in fsdt_stat]
err_rel_32 = [float(r['sai_so_tuong_doi_pct']) for r in fsdt_stat]

fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=300)

y_clamped_32 = []
for val in err_rel_32:
    if val > 10.0:
        y_clamped_32.append(10.0)
    elif val < -10.0:
        y_clamped_32.append(-10.0)
    else:
        y_clamped_32.append(val)

ax.plot(d_list_32, y_clamped_32, color='#1f77b4', linestyle='-', linewidth=1.6, marker='o', markersize=4.5, label='Sai số tương đối thực nghiệm')

ax.axhline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.8)
ax.axhline(0.5, color='#d62728', linestyle='--', linewidth=1.2, label='Ngưỡng dung sai quy định (±0.5%)')
ax.axhline(-0.5, color='#d62728', linestyle='--', linewidth=1.2)

ax.set_ylim(-10.5, 10.5)
ax.set_xlim(-10, 615)
ax.set_yticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])

ax.grid(axis='y', which='major', linestyle='--', linewidth=0.7, alpha=0.5)
ax.grid(axis='x', visible=False)

ax.set_title("Sai số tương đối theo khoảng cách chuẩn (Tập dữ liệu FSDT)", fontweight='bold', pad=12)
ax.set_xlabel("Khoảng cách chuẩn (cm)", fontweight='bold')
ax.set_ylabel("Sai số tương đối δ (%)", fontweight='bold')

ax.text(2.0, 9.2, "1cm: +103.1% ↑\n2cm: +17.6% ↑", color='#1f77b4', fontsize=8.2, fontweight='bold', ha='left',
        bbox=dict(boxstyle='square,pad=0.25', facecolor='white', edgecolor='#1f77b4', alpha=0.9))

ax.text(6.0, -9.2, "3cm: -10.7% ↓\n5cm: -14.1% ↓", color='#1f77b4', fontsize=8.2, fontweight='bold', ha='left',
        bbox=dict(boxstyle='square,pad=0.25', facecolor='white', edgecolor='#1f77b4', alpha=0.9))

ax.text(600.0, 9.2, "600cm: +37.4% ↑", color='#1f77b4', fontsize=8.2, fontweight='bold', ha='right',
        bbox=dict(boxstyle='square,pad=0.25', facecolor='white', edgecolor='#1f77b4', alpha=0.9))

ax.legend(loc='lower right', framealpha=0.95)
plt.tight_layout()

h3_2_path = GRAPH_DIR / "chuong_3" / "hinh_3_2_sai_so_tuong_doi.png"
fig.savefig(h3_2_path)
plt.close(fig)
print(f"Đã xuất đồ thị Hình 3.2 tại: {h3_2_path}")

# ==========================================================
# 3. HÌNH 3.3: Độ chụm toàn dải đo FSDT (Độ lệch chuẩn s và CV%)
# ==========================================================
print("Tạo Hình 3.3...")
all_cols_fsdt = [c for c in fsdt.keys() if float(c.replace('cm', '')) <= 550]
all_true_fsdt = [float(c.replace('cm', '')) for c in all_cols_fsdt]
all_stdev_fsdt = [statistics.stdev(fsdt[c]) * 10 for c in all_cols_fsdt] # mm
all_cv_fsdt = [(statistics.stdev(fsdt[c]) / statistics.mean(fsdt[c])) * 100 for c in all_cols_fsdt]

fig, ax1 = plt.subplots(figsize=(10, 4.5), dpi=300)
color1 = '#1f77b4'
ax1.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax1.set_ylabel('Độ lệch chuẩn s (mm)', color=color1)
line1 = ax1.plot(all_true_fsdt, all_stdev_fsdt, 'o-', color=color1, linewidth=1.5, markersize=4, label='Độ lệch chuẩn s (mm)')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle=':', alpha=0.6)

ax2 = ax1.twinx()
color2 = '#d62728'
ax2.set_ylabel('Hệ số biến thiên CV (%)', color=color2)
line2 = ax2.plot(all_true_fsdt, all_cv_fsdt, 's--', color=color2, linewidth=1.5, markersize=4, label='Hệ số biến thiên CV (%)')
ax2.tick_params(axis='y', labelcolor=color2)

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')
ax1.set_title('Đánh giá Độ chụm toàn dải đo thực nghiệm (FSDT: 1 cm – 550 cm)')

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_3_do_chum_toan_dai.png", dpi=300)
plt.close()

# ==========================================================
# 4. HÌNH 3.4: Độ chính xác toàn dải đo (Sai số tuyệt đối & Sai số tương đối)
# ==========================================================
print("Tạo Hình 3.4...")
all_err_fsdt = [(statistics.mean(fsdt[c]) - float(c.replace('cm', ''))) * 10 for c in all_cols_fsdt] # mm
all_rel_err_fsdt = [((statistics.mean(fsdt[c]) - float(c.replace('cm', ''))) / float(c.replace('cm', ''))) * 100 for c in all_cols_fsdt]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.5), dpi=300, sharex=True)

ax1.plot(all_true_fsdt, all_err_fsdt, 'o-', color='#2ca02c', linewidth=1.5, markersize=4)
ax1.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax1.set_ylabel('Sai số tuyệt đối Δd (mm)')
ax1.set_title('Sai số tuyệt đối thực nghiệm theo khoảng cách (FSDT)')
ax1.grid(True, linestyle=':', alpha=0.6)

# Relative error (omitting 1-3cm for y-scale clarity, or clipping)
stable_idx = [i for i, d in enumerate(all_true_fsdt) if d >= 5.0]
ax2.plot([all_true_fsdt[i] for i in stable_idx], [all_rel_err_fsdt[i] for i in stable_idx], 's-', color='#ff7f0e', linewidth=1.5, markersize=4)
ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax2.axhline(0.5, color='red', linestyle=':', label='Ngưỡng chuẩn ±0.5%')
ax2.axhline(-0.5, color='red', linestyle=':')
ax2.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax2.set_ylabel('Sai số tương đối δ (%)')
ax2.set_title('Sai số tương đối trong dải làm việc hiệu dụng (5 cm – 550 cm)')
ax2.legend(loc='lower right')
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_4_do_chinh_xac_sai_so.png", dpi=300)
plt.close()

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
ax1.set_xlabel('Khoảng cách chuẩn d_true (cm)')
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
ax2.set_xlabel('Khoảng cách chuẩn d_true (cm)')
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
ax1.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax1.set_ylabel('Khoảng cách đo (cm)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='lower right')

# Độ lệch trễ ΔH
ax2.bar(common_h, h_diffs, width=8, color='#9467bd', alpha=0.85, edgecolor='black', linewidth=0.5)
ax2.axhline(max(h_diffs), color='red', linestyle='--', label=f'Độ trễ cực đại: ΔH_max = {max(h_diffs):.2f} mm')
ax2.set_title('Phân bố Độ lệch trễ ΔH_k theo cự ly đo')
ax2.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax2.set_ylabel('Độ lệch trễ ΔH (mm)')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_6_vong_tre_hysteresis.png", dpi=300)
plt.close()

# ==========================================================
# 7. HÌNH 3.7: Ảnh hưởng của Bề mặt phản xạ (Nhẵn vs Gồ ghề)
# ==========================================================
print("Tạo Hình 3.7...")
common_r = sorted(list(set([float(c.replace('cm', '')) for c in frdt.keys()]).intersection(set([float(c.replace('cm', '')) for c in fsdt.keys()]))))
s_smooth = [statistics.stdev(fsdt[f"{int(d):03d}cm"]) * 10 for d in common_r] # mm
s_rough = [statistics.stdev(frdt[f"{int(d):03d}cm"]) * 10 for d in common_r] # mm

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Tán xạ làm tăng s (khảo sát đến 340cm để thấy rõ tỉ số chênh lệch)
common_r_sub = [d for d in common_r if d <= 340]
s_smooth_sub = [statistics.stdev(fsdt[f"{int(d):03d}cm"]) * 10 for d in common_r_sub]
s_rough_sub = [statistics.stdev(frdt[f"{int(d):03d}cm"]) * 10 for d in common_r_sub]

ax1.plot(common_r_sub, s_smooth_sub, 'o-', color='#1f77b4', label='Mặt phẳng nhẵn (FSDT)', linewidth=1.5, markersize=4)
ax1.plot(common_r_sub, s_rough_sub, 's-', color='#ff7f0e', label='Mặt gồ ghề tán xạ (FRDT)', linewidth=1.5, markersize=4)
ax1.set_title('So sánh Độ tán xạ dữ liệu đo (Độ lệch chuẩn s)')
ax1.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax1.set_ylabel('Độ lệch chuẩn s (mm)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')

# Giới hạn cự ly do suy hao
all_frdt_d = sorted([float(c.replace('cm', '')) for c in frdt.keys()])
r_means = [statistics.mean(frdt[f"{int(d):03d}cm"]) for d in all_frdt_d]
f_sub_means = [statistics.mean(fsdt[f"{int(d):03d}cm"]) if f"{int(d):03d}cm" in fsdt else d for d in all_frdt_d]

ax2.plot(all_frdt_d, f_sub_means, 'o-', color='#1f77b4', label='Mặt phẳng nhẵn (đo ổn định đến 550 cm)', linewidth=1.5, markersize=4)
ax2.plot(all_frdt_d, r_means, 's--', color='#d62728', label='Mặt gồ ghề (suy hao bão hòa tại ≥350 cm)', linewidth=1.5, markersize=4)
ax2.axvspan(345, 380, color='#ff9999', alpha=0.35, label='Vùng suy giảm tín hiệu mạnh')
ax2.set_title('Giới hạn tầm đo trên bề mặt gồ ghề')
ax2.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax2.set_ylabel('Khoảng cách đo được (cm)')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='lower right')

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_7_anh_huong_be_mat.png", dpi=300)
plt.close()

# ==========================================================
# 8. HÌNH 3.8: Ảnh hưởng Nhiệt độ và Hiệu quả bù Vận tốc Laplace
# ==========================================================
print("Tạo Hình 3.8...")
common_t = sorted([float(c.replace('cm', '')) for c in fsat.keys()])

# Tính khoảng cách không bù tại 20C sử dụng vận tốc chuẩn của 27C (Default Temp)
# v(27C) = 347.662 m/s, v(20C) = 343.420 m/s
t_20_vals = []
for d in common_t:
    with open(RESULT_DIR / f"FSAT_{int(d):03d}cm.csv", 'r') as rf:
        rr = csv.DictReader(rf)
        t_20_vals.append(statistics.mean([float(row['t']) for row in rr]))

d_uncomp_20 = [(347.662 * t * 1e-4) / 2.0 for t in t_20_vals]
d_comp_20 = [statistics.mean(fsat[f"{int(d):03d}cm"]) for d in common_t]
d_comp_27 = [statistics.mean(fsdt[f"{int(d):03d}cm"]) for d in common_t]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Sai lệch khoảng cách nếu không bù
err_uncomp = [(u - d) * 10 for u, d in zip(d_uncomp_20, common_t)] # mm
err_comp_20 = [(c - d) * 10 for c, d in zip(d_comp_20, common_t)] # mm

ax1.plot(common_t, err_uncomp, '^-', color='#d62728', label='Chưa bù nhiệt độ (giả định 27°C tại 20°C)', linewidth=1.5)
ax1.plot(common_t, err_comp_20, 'o-', color='#2ca02c', label='Đã bù nhiệt độ Laplace (20°C thực)', linewidth=1.5)
ax1.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax1.set_title('Sai số đo khoảng cách khi Có bù vs Không bù nhiệt')
ax1.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax1.set_ylabel('Sai số đo Δd (mm)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')

# Đối chiếu kết quả đã bù giữa 2 mức nhiệt độ (27C vs 20C)
diff_compensated = [(m27 - m20) * 10 for m27, m20 in zip(d_comp_27, d_comp_20)]
ax2.bar(common_t, diff_compensated, width=8, color='#17becf', alpha=0.85, edgecolor='black', linewidth=0.5)
ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax2.set_title('Chênh lệch khoảng cách sau khi bù giữa 27°C và 20°C')
ax2.set_xlabel('Khoảng cách chuẩn d_true (cm)')
ax2.set_ylabel('Chênh lệch d_27°C - d_20°C (mm)')
ax2.set_ylim(-1.5, 1.5)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig(GRAPH_DIR / "hinh_3_8_anh_huong_nhiet_do_bu_laplace.png", dpi=300)
plt.close()

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
