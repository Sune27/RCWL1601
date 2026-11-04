# -*- coding: utf-8 -*-
"""
Kịch bản nối tiếp Chương 1 vào tệp Word hiện có (Bao_Cao_Thuc_Nghiem_RCWL1601.docx)
Bảo tồn 100% nội dung và các chỉnh sửa của người dùng ở Phần Mở Đầu.
Áp dụng chuẩn định dạng GEMINI.md:
- Heading 1: 16pt, Bold, C_NAVY
- Heading 2: 14pt, Bold, C_NAVY
- Heading 3: 13pt, Bold, C_MAROON
- Body text: 13pt, Line spacing 1.35, Space after 6pt, Justified, First-line indent 1.0cm
- Equation: Căn giữa, đánh số ở lề phải
- Table: Header xanh pastel, viền thanh nhã IEEE/APA
"""

import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\Bao_Cao_Thuc_Nghiem_RCWL1601.docx"

doc = Document(FILE_PATH)

C_NAVY = RGBColor(0, 51, 102)     # #003366
C_MAROON = RGBColor(128, 0, 0)   # #800000
C_BLACK = RGBColor(0, 0, 0)
C_GRAY = RGBColor(100, 100, 100)

def set_cell_border(cell, **kwargs):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = f'w:{edge}'
            element = parse_xml(f'<{tag} {nsdecls("w")} w:val="{edge_data.get("val", "single")}" w:sz="{edge_data.get("sz", 4)}" w:space="0" w:color="{edge_data.get("color", "auto")}"/>')
            tcBorders.append(element)
    tcPr.append(tcBorders)

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(10)
    p.paragraph_format.keep_with_next = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    return p

def add_heading_3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = C_MAROON
    return p

def add_body_p(text, indent=True):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.0)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.35
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.color.rgb = C_BLACK
    return p

def add_bullet_p(text, bold_prefix=""):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.25
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(13)
        r_b.font.bold = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    return p

def add_equation_box(eq_text, eq_num=""):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.2
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(eq_text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.italic = True
    if eq_num:
        r_tab = p.add_run(f"\t\t\t\t\t({eq_num})")
        r_tab.font.name = 'Times New Roman'
        r_tab.font.size = Pt(12)
        r_tab.font.italic = False
        r_tab.font.bold = False
        r_tab.font.color.rgb = C_GRAY
    return p

# -------------------------------------------------------------
# BẮT ĐẦU NỐI CHƯƠNG 1
# -------------------------------------------------------------
doc.add_page_break()

add_heading_1("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM")

# 1.1
add_heading_2("1.1. NGUYÊN LÝ ĐO KHOẢNG CÁCH THỜI GIAN BAY VÀ MÔ HÌNH BÙ NHIỆT ĐỘ MÔI TRƯỜNG")

add_heading_3("1.1.1. Phương trình lan truyền sóng siêu âm thời gian bay")
add_body_p(
    "Phương pháp đo khoảng cách bằng sóng siêu âm dựa trên nguyên lý đo thời gian bay (Time-of-Flight - ToF). "
    "Module cảm biến phát ra một chuỗi xung kích siêu âm hình sin ở tần số công tác danh định 40 kHz. "
    "Sóng âm lan truyền trong không gian tự do với vận tốc v, gặp mặt phẳng vật cản và phản xạ dội ngược trở lại đầu thu. "
    "Đầu thu áp điện chuyển đổi năng lượng dao động cơ học của sóng âm dội về thành tín hiệu điện áp phản hồi."
)
add_body_p(
    "Khoảng cách d từ cảm biến đến vật cản được xác định từ thời gian bay tổng cộng t của sóng âm theo phương trình:"
)
add_equation_box("d = (v · t) / 2", "1.1")
add_body_p(
    "Trong đó: d là khoảng cách đo từ mặt trước màng rung cảm biến đến bề mặt phản xạ (m); "
    "v là vận tốc truyền sóng âm trong không khí (m/s); t là thời gian bay khứ hồi từ khi phát xung đến khi thu được xung dội về (s). "
    "Hệ số 2 thể hiện sóng âm phải vượt qua hai lần quãng đường (lượt đi và lượt về)."
)

add_heading_3("1.1.2. Mô hình toán học bù nhiệt độ môi trường cho vận tốc âm thanh")
add_body_p(
    "Trong chất khí lý tưởng, sóng âm lan truyền dưới dạng sóng dọc thông qua quá trình nén và giãn nở đoạn nhiệt tuần hoàn. "
    "Vận tốc truyền sóng âm được xác định theo phương trình nhiệt động học Laplace:"
)
add_equation_box("v = √(γ · R · T_K / M)", "1.2")
add_body_p(
    "Trong đó: γ là hệ số đoạn nhiệt của không khí khô (γ ≈ 1.402); R là hằng số khí lý tưởng phổ quát (R = 8.314 J/(mol·K)); "
    "M là khối lượng mol biểu kiến trung bình của không khí khô (M ≈ 0.028964 kg/mol); T_K là nhiệt độ tuyệt đối của môi trường (K), với T_K = T + 273.15 (°C)."
)
add_body_p(
    "Khai triển chuỗi Taylor bậc nhất của vận tốc sóng âm quanh điểm chuẩn 0 °C (T_0 = 273.15 K, v_0 ≈ 331.3 m/s) ta thu được "
    "phương trình thực nghiệm xấp xỉ tuyến tính chính xác cao:"
)
add_equation_box("v(T) = 331.3 + 0.606 · T  (m/s)", "1.3")
add_body_p(
    "Phương trình tuyến tính (1.3) chỉ ra rằng: khi nhiệt độ môi trường thay đổi 1 °C, vận tốc sóng âm thay đổi tương ứng 0.606 m/s "
    "(khoảng 0.177%). Nếu nhiệt độ phòng dao động 7 °C (ví dụ giữa phòng bật điều hòa 20 °C và nhiệt độ mặc định 27 °C), "
    "vận tốc sóng âm sẽ biến thiên khoảng 7.27 m/s (2.12%). Nếu hệ thống sử dụng vận tốc cố định, sai số đo khoảng cách sẽ trôi lũy tiến "
    "theo cự ly đo, đạt tới hàng chục milimét ở cự ly trên 2 m. Do đó, việc đo nhiệt độ môi trường thời gian thực để bù trừ vận tốc v(T) "
    "là yêu cầu kỹ thuật bắt buộc."
)

add_heading_3("1.1.3. Sự suy hao năng lượng sóng âm theo cự ly đo")
add_body_p(
    "Năng lượng và biên độ áp suất âm p(d) của sóng âm suy giảm mạnh theo khoảng cách truyền dẫn do hai cơ chế vật lý song song:"
)
add_bullet_p("Do chùm sóng âm phát đi theo dạng hình nón có góc mở định hướng θ ≈ 15°. Năng lượng sóng âm phân bố trên diện tích mặt cầu tăng dần, khiến mật độ công suất âm suy giảm tỷ lệ nghịch với bình phương khoảng cách: I(d) ~ 1/d².", "1. Phân kỳ hình học (Geometric Divergence): ")
add_bullet_p("Quá trình truyền sóng gây ma sát phân tử và dẫn nhiệt trong chất khí, làm suy hao biên độ áp suất âm theo quy luật hàm mũ: p(d) = p_0 · e^(-α·d). Ở tần số 40 kHz và nhiệt độ phòng 25 °C, độ ẩm 60%, hệ số suy hao khí quyển đạt xấp xỉ α ≈ 1.2 dB/m.", "2. Hấp thụ âm nội tại của không khí (Atmospheric Absorption): ")
add_body_p(
    "Tổng suy hao sau hành trình hai chiều (2d) lên tới hàng chục decibel ở cự ly xa (d > 3 m). "
    "Vì vậy, ở cự ly trên 5.5 m, biên độ xung phản xạ sẽ tụt xuống dưới ngưỡng nhạy phát hiện của bộ so sánh, dẫn tới việc vi điều khiển "
    "bị tràn thời gian ngắt câm và trả về giá trị lỗi bão hòa."
)

# 1.2
add_heading_2("1.2. ĐẶC TÍNH HOẠT ĐỘNG VÀ THÔNG SỐ DANH ĐỊNH CỦA MODULE RCWL-1601")

add_heading_3("1.2.1. Giản đồ xung kích hoạt và phản hồi thời gian bay")
add_body_p(
    "Module RCWL-1601 giao tiếp với vi điều khiển ESP32 thông qua giao thức xung kỹ thuật số hai chân (Trigger và Echo):"
)
add_bullet_p("Vi điều khiển chủ động kéo chân TRIG lên mức logic CAO (HIGH, 3.3V) trong khoảng thời gian tối thiểu 10 μs để phát lệnh đo.", "• Bước 1 - Kích hoạt xung (Trigger Pulse): ")
add_bullet_p("Khi nhận được xung TRIG, vi mạch chuyên dụng RCWL-9610 trên module tự động kích hoạt mạch dao động công suất đẩy màng loa phát chuỗi 8 chu kỳ xung siêu âm dạng sóng vuông ở tần số 40 kHz (kéo dài đúng 200 μs). Đồng thời, chân ECHO được kéo lên mức CAO để báo hiệu bắt đầu chu kỳ bay.", "• Bước 2 - Phát chùm sóng siêu âm (Burst Generation): ")
add_bullet_p("Sóng âm dội về tác động lên màng thu, tạo điện áp vi sai xoay chiều. Vi mạch RCWL-9610 thực hiện khuếch đại tự động độ lợi (AGC) và lọc thông dải 40 kHz. Ngay khi biên độ tín hiệu vượt ngưỡng so sánh, IC lập tức kéo chân ECHO xuống mức THẤP (LOW).", "• Bước 3 - Thu nhận sóng phản xạ và ngắt xung (Echo Pulse): ")
add_bullet_p("Độ rộng mức cao của xung ECHO (t_echo) tỷ lệ thuận chính xác với thời gian bay hai chiều t của sóng âm.", "• Bước 4 - Đo thời gian bay ToF: ")

add_heading_3("1.2.2. Bảng thông số kỹ thuật danh định của RCWL-1601 (Theo Datasheet)")
add_body_p("Bảng 1.1 tổng hợp các thông số kỹ thuật cốt lõi do nhà sản xuất công bố cho module RCWL-1601:")

p_tbl = doc.add_paragraph()
p_tbl.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_tbl.paragraph_format.space_after = Pt(4)
r_tcap = p_tbl.add_run("Bảng 1.1: Bảng thông số kỹ thuật danh định của module cảm biến siêu âm RCWL-1601")
r_tcap.font.name = 'Times New Roman'
r_tcap.font.size = Pt(12)
r_tcap.font.bold = True

ds_data = [
    ("Điện áp hoạt động (V_CC)", "2.8 V – 5.5 V (Một chiều - DC)"),
    ("Dòng điện tiêu thụ tĩnh", "< 2 mA"),
    ("Dòng điện cực đại khi phát", "≈ 15 mA – 20 mA"),
    ("Tần số sóng siêu âm", "40 kHz ± 1.0 kHz"),
    ("Dải đo danh định công bố", "2 cm – 400 cm (hoặc 450 cm)"),
    ("Độ phân giải lý thuyết", "1 mm"),
    ("Góc mở chùm sóng âm", "≈ 15°"),
    ("Tín hiệu kích hoạt (TRIG)", "Xung mức CAO (HIGH) ≥ 10 μs"),
    ("Tín hiệu phản hồi (ECHO)", "Độ rộng xung mức CAO (PWM)")
]

table_ds = doc.add_table(rows=len(ds_data)+1, cols=2)
table_ds.alignment = WD_TABLE_ALIGNMENT.CENTER
table_ds.autofit = False

ds_widths = [Cm(7.5), Cm(8.5)]
ds_headers = ["Thông số kỹ thuật", "Giá trị công bố (Datasheet)"]

for idx, text in enumerate(ds_headers):
    c = table_ds.rows[0].cells[idx]
    c.text = text
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, data in enumerate(ds_data, start=1):
    for col_idx, text in enumerate(data):
        c = table_ds.rows[row_idx].cells[col_idx]
        c.text = text
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            if col_idx == 0:
                r.font.bold = True

for row in table_ds.rows:
    for idx, width in enumerate(ds_widths):
        row.cells[idx].width = width
        set_cell_border(row.cells[idx],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_ds.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_ds.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

# 1.3
add_heading_2("1.3. CƠ SỞ LÝ THUYẾT XỬ LÝ SỐ LIỆU ĐO LƯỜNG VÀ ĐỘ KHÔNG ĐẢM BẢO ĐO (ISO/GUM)")

add_heading_3("1.3.1. Các đại lượng thống kê mô tả mẫu đo")
add_body_p(
    "Tại mỗi mốc cự ly chuẩn, thực hiện lặp lại N lần đo độc lập trong điều kiện môi trường ổn định, "
    "thu được tập mẫu đo khoảng cách: X = {x_1, x_2, ..., x_N}. Các đại lượng thống kê cơ bản bao gồm:"
)
add_bullet_p("Đại diện cho giá trị xu thế trung tâm của tập mẫu đo lặp:", "• Giá trị trung bình mẫu (Sample Mean): ")
add_equation_box("x̄ = (1 / N) · ∑_{i=1}^N x_i", "1.4")
add_bullet_p("Đại diện cho mức độ phân tán ngẫu nhiên của các giá trị đo quanh giá trị trung bình:", "• Độ lệch chuẩn mẫu thực nghiệm (Sample Standard Deviation): ")
add_equation_box("s = √[ (1 / (N - 1)) · ∑_{i=1}^N (x_i - x̄)² ]", "1.5")
add_bullet_p("Giá trị chia đôi tập dữ liệu đã sắp xếp thứ tự: Med = x_((N+1)/2) với N lẻ. Giá trị trung vị có tính chất thống kê bền vững (Robust Statistics), hoàn toàn không bị ảnh hưởng bởi các xung nhiễu đột biến cực đoan.", "• Giá trị trung vị mẫu (Median): ")

add_heading_3("1.3.2. Tiêu chuẩn phát hiện và lọc sai số thô bằng Khoảng tứ phân vị (IQR)")
add_body_p(
    "Trong đo đạc thực nghiệm sóng siêu âm, các xung nhiễu điện từ, bọt khí bề mặt, góc phản xạ dị thường hoặc hiện tượng mất xung phản hồi "
    "ở cự ly xa (dẫn đến tràn thời gian bay bão hòa) có thể tạo ra các mẫu đo ngoại lai (sai số thô) có giá trị sai lệch nghiêm trọng. "
    "Hệ thống lựa chọn phương pháp thống kê phi tham số bền vững dựa trên Khoảng tứ phân vị (Interquartile Range - IQR) "
    "kết hợp hệ hàng rào Tukey (Tukey's Fences) làm giải thuật lọc số chuẩn hóa duy nhất:"
)
add_equation_box("IQR = Q_3 - Q_1", "1.6")
add_body_p("Hàng rào dưới (Lower Fence) và Hàng rào trên (Upper Fence) được xác định theo:")
add_equation_box("LF = Q_1 - 1.5 · IQR,    UF = Q_3 + 1.5 · IQR", "1.7")
add_body_p("Mẫu đo x_i được chấp nhận là giá trị hợp lệ nếu nằm trong khoảng:")
add_equation_box("x_i ∈ [LF, UF]  <=>  Q_1 - 1.5 · IQR ≤ x_i ≤ Q_3 + 1.5 · IQR", "1.8")
add_body_p(
    "Mọi mẫu đo nằm ngoài khoảng [LF, UF] đều bị loại bỏ hoàn toàn trước khi đưa vào tính toán các chỉ số thống kê đo lường. "
    "Phương pháp này có ưu thế vượt trội do tính chất bền vững, hoàn toàn miễn nhiễm với các mẫu tràn thời gian cực trị (824.6 cm) "
    "và triệt tiêu triệt để hiện tượng che khuất ngoại lai (masking effect)."
)

add_heading_3("1.3.3. Hệ thống công thức đánh giá các Đặc tính tĩnh của cảm biến")
add_bullet_p("Phản ánh độ ổn định tương đối của phép đo, chuẩn hóa độ lệch chuẩn theo giá trị trung bình: CV% = (s / x̄) · 100%.", "1. Hệ số biến thiên (Coefficient of Variation): ")
add_bullet_p("Đánh giá mức độ sai lệch giữa giá trị đo trung bình và giá trị chuẩn: Sai số tuyệt đối Δd = d̄ - d_true; Sai số tương đối δ% = (Δd / d_true) · 100%.", "2. Sai số đo lường:", )
add_bullet_p("Tỷ số giữa độ biến thiên tín hiệu đầu ra và độ biến thiên đại lượng đo đầu vào: S_t = Δt / Δd_true (μs/cm).", "3. Độ nhạy (Sensitivity): ")
add_bullet_p(
    "Đánh giá mức độ bám sát của đặc tính tĩnh thực nghiệm với đường thẳng lý thuyết ŷ = a · x + b. "
    "Áp dụng phương pháp bình phương bé nhất dưới dạng phương trình ma trận chuẩn tắc, vector hệ số hồi quy được giải trực tiếp theo: "
    "β̂ = [a, b]^T = (X^T · X)^(-1) · X^T · Y. "
    "Hệ số xác định tương quan R² = 1 - [∑(y_k - ŷ_k)² / ∑(y_k - ȳ)²]. "
    "Sai số phi tuyến cực đại: δ_NL% = (max_k |d̄_k - d̂_k| / d_FS) · 100%.",
    "4. Độ tuyến tính và Sai số phi tuyến (Linearity): "
)
add_bullet_p(
    "Phản ánh sự bất đối xứng của giá trị đo tại cùng một điểm cự ly khi tiếp cận theo hai hướng ngược nhau (Chiều tiến Forward và Chiều lùi Backward): "
    "ΔH_k = |d̄_forward,k - d̄_backward,k|. "
    "Sai số trễ tương đối toàn dải: γ_H% = (max_k ΔH_k / d_FS) · 100%.",
    "5. Độ trễ (Hysteresis): "
)
add_bullet_p(
    "Biến thiên nhỏ nhất của khoảng cách đầu vào mà hệ thống đo có thể nhận biết và phân biệt rõ ràng. "
    "Được xác định bởi độ phân giải bộ đếm thời gian vi điều khiển (1 μs tương đương ≈ 0.175 mm) và độ tán xạ ngẫu nhiên s của cảm biến.",
    "6. Độ phân giải (Resolution): "
)

add_heading_3("1.3.4. Đánh giá Độ không đảm bảo đo theo tiêu chuẩn ISO/GUM")
add_body_p(
    "Theo hướng dẫn quốc tế ISO/IEC Guide 98-3 (GUM), độ tin cậy của kết quả đo được lượng hóa qua độ không đảm bảo đo toàn diện:"
)
add_bullet_p("Đánh giá bằng phương pháp phân tích thống kê chuỗi quan sát lặp lại: u_A = s / √N.", "• Độ không đảm bảo đo Loại A (u_A): ")
add_bullet_p(
    "Đánh giá bằng các phương pháp phi thống kê (thông số kỹ thuật thiết bị, độ phân giải vi điều khiển, độ chia thước chuẩn cơ khí). "
    "Với giả thiết phân bố xác suất hình chữ nhật (Uniform Distribution), độ không đảm bảo chuẩn thành phần là: u_B = a / √3, "
    "trong đó a là nửa khoảng dung sai cho phép.",
    "• Độ không đảm bảo đo Loại B (u_B): "
)
add_bullet_p("Kết hợp toàn bộ các thành phần theo định luật lan truyền sai số: u_c = √(u_A² + ∑ u_{B,j}²).", "• Độ không đảm bảo đo chuẩn tổng hợp (u_c): ")
add_bullet_p("Mở rộng khoảng tin cậy với hệ số phủ k_p = 2 (tương ứng mức tin cậy xấp xỉ 95% đối với bậc tự do lớn): U_95% = k_p · u_c = 2 · u_c.", "• Độ không đảm bảo đo mở rộng (U_95%): ")
add_body_p("Kết quả đo hoàn chỉnh của phép đo khoảng cách được biểu diễn theo chuẩn quốc tế:")
add_equation_box("Y = d̄ ± U_95%  (với k_p = 2, Mức tin cậy 95%)", "1.9")

doc.save(FILE_PATH)
print(f"Nối thành công Chương 1 vào tệp Word: {FILE_PATH}")
