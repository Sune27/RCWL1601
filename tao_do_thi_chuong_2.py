import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Cấu hình thẩm mỹ khoa học theo quy chuẩn GEMINI.md
plt.rcParams['font.family'] = 'Segoe UI'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 12

BASE_DIR = Path(r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601")
C2_DATA_DIR = BASE_DIR / "du_lieu_tong_hop" / "chuong_2"
GRAPH_C2_DIR = BASE_DIR / "graph" / "chuong_2"
GRAPH_ROOT = BASE_DIR / "graph"

GRAPH_C2_DIR.mkdir(parents=True, exist_ok=True)

def load_data(dist_name):
    path = C2_DATA_DIR / f"hoi_tu_{dist_name}.csv"
    ks = []
    eps_mm = []
    d_eps_mm = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            k = int(r["k"])
            if k >= 2:
                ks.append(k)
                eps_mm.append(float(r["epsilon95_mm"]))
                d_val = r["d_epsilon95_mm"]
                d_eps_mm.append(abs(float(d_val)) if d_val and d_val != "nan" else 0.0)
    return ks, eps_mm, d_eps_mm

k50, eps50, d_eps50 = load_data("50cm")
k100, eps100, d_eps100 = load_data("100cm")
k150, eps150, d_eps150 = load_data("150cm")

# ==========================================================
# 1. HÌNH 2.1: Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu
# ==========================================================
print("Tạo Hình 2.1: Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu...")
fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

ax.plot(k50, eps50, color='#1f77b4', linewidth=1.8, marker='o', markersize=3, label='Mốc 50 cm (Cự ly gần)')
ax.plot(k100, eps100, color='#ff7f0e', linewidth=1.8, marker='s', markersize=3, label='Mốc 100 cm (Cự ly trung bình)')
ax.plot(k150, eps150, color='#2ca02c', linewidth=1.8, marker='^', markersize=3, label='Mốc 150 cm (Cự ly xa)')

# Đường ngưỡng dung sai vạch chia thước (±0.5 mm)
ax.axhline(y=0.5, color='#d62728', linestyle='--', linewidth=1.5, label='Dung sai vạch chia thước')

# Đường vạch chốt N = 50
ax.axvline(x=50, color='#9467bd', linestyle='-.', linewidth=1.8, label='N = 50')

ax.set_title("BÁN KÍNH SAI SỐ NGẪU NHIÊN THEO TÍCH LŨY CỠ MẪU", fontweight='bold', pad=12)
ax.set_xlabel("Cỡ mẫu tích lũy k", fontweight='bold')
ax.set_ylabel("Bán kính sai số ngẫu nhiên $\\varepsilon_{95\\%}$ (mm)", fontweight='bold')
ax.set_xlim(2, 100)
ax.set_ylim(0, 1.4)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.95)

plt.tight_layout()
h2_1_path = GRAPH_C2_DIR / "hinh_2_1_hoi_tu_sai_so_N.png"
fig.savefig(h2_1_path)
fig.savefig(GRAPH_ROOT / "bieu_do_chot_N50_student_t95.png") # backward compatibility
plt.close(fig)
print(f"Đã lưu: {h2_1_path}")

# ==========================================================
# 2. HÌNH 2.2: Đồ thị tốc độ biến thiên sai số theo cỡ mẫu k
# ==========================================================
print("Tạo Hình 2.2: Đồ thị tốc độ biến thiên sai số...")
fig2, ax2 = plt.subplots(figsize=(9, 5), dpi=300)

# Cắt từ k=3 vì k=2 d_eps là 0
k3_50, d3_50 = k50[1:], d_eps50[1:]
k3_100, d3_100 = k100[1:], d_eps100[1:]
k3_150, d3_150 = k150[1:], d_eps150[1:]

ax2.plot(k3_50, d3_50, color='#1f77b4', linewidth=1.8, marker='o', markersize=3, label='Đạo hàm mốc 50 cm')
ax2.plot(k3_100, d3_100, color='#ff7f0e', linewidth=1.8, marker='s', markersize=3, label='Đạo hàm mốc 100 cm')
ax2.plot(k3_150, d3_150, color='#2ca02c', linewidth=1.8, marker='^', markersize=3, label='Đạo hàm mốc 150 cm')

# Vạch phân ranh giới bão hòa đạo hàm triệt tiêu (0.005 mm)
ax2.axhline(y=0.005, color='#d62728', linestyle=':', linewidth=1.5, label='Ngưỡng bão hòa tốc độ giảm (0.005 mm/bước)')
ax2.axvline(x=50, color='#9467bd', linestyle='-.', linewidth=1.8, label='N = 50')

ax2.set_title("TỐC ĐỘ BIẾN THIÊN SAI SỐ |d$\\varepsilon_{95\\%}$/dk| THEO CỠ MẪU k", fontweight='bold', pad=12)
ax2.set_xlabel("Cỡ mẫu tích lũy k", fontweight='bold')
ax2.set_ylabel("Tốc độ biến thiên sai số |d$\\varepsilon$/dk| (mm/bước đo)", fontweight='bold')
ax2.set_xlim(3, 100)
ax2.set_ylim(-0.005, 0.12)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', framealpha=0.95)

plt.tight_layout()
h2_2_path = GRAPH_C2_DIR / "hinh_2_2_dao_ham_diem_khuyu_tay.png"
fig2.savefig(h2_2_path)
plt.close(fig2)
print(f"Đã lưu: {h2_2_path}")
