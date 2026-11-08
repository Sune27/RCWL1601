# -*- coding: utf-8 -*-
"""
Kịch bản nối tiếp Chương 2 vào tệp Word hiện có (Bao_Cao_Thuc_Nghiem_RCWL1601.docx)
Tuân thủ nghiêm ngặt quy chuẩn GEMINI.md:
- Heading 1: 16pt, Bold, C_NAVY
- Heading 2: 14pt, Bold, C_NAVY
- Heading 3: 13pt, Bold, C_MAROON
- Body text: 13pt, Line spacing 1.35, Space after 6pt, Justified, First-line indent 1.0cm
- Chèn Hình 2.1 (Biểu đồ Student 95% N=50) căn giữa, có Caption chuẩn bên dưới
- Bảng 2.1, 2.2, 2.3 định dạng chuẩn IEEE/APA với header xanh pastel D9E1F2
"""

import os
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
IMAGE_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\bieu_do_chot_N50_student_t95.png"

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
# BẮT ĐẦU NỐI CHƯƠNG 2
# -------------------------------------------------------------
doc.add_page_break()

add_heading_1("CHƯƠNG 2: THIẾT KẾ VÀ BỐ TRÍ THỰC NGHIỆM")

# 2.1
add_heading_2("2.1. MỤC TIÊU THỰC NGHIỆM")

add_heading_3("2.1.1. Mục tiêu thực nghiệm")
add_body_p(
    "Nghiên cứu thực nghiệm được thiết kế nhằm mục đích kiểm chứng các đặc tính đo lường của module cảm biến siêu âm RCWL-1601: "
    "Khảo sát dải đo thực tế, định lượng độ chụm và độ chính xác, đánh giá độ tuyến tính, đánh giá ảnh hưởng của nhiệt độ môi trường, "
    "đánh giá ảnh hưởng của bề mặt phản xạ, đánh giá độ trễ"
)

# 2.2
add_heading_2("2.2. THIẾT KẾ PHẦN CỨNG VÀ KHÔNG GIAN THỰC NGHIỆM")

add_heading_3("2.2.1. Thiết kế phần cứng và sơ đồ kết nối điện")
add_body_p(
    "Module cảm biến siêu âm RCWL-1601 được kết nối trực tiếp với vi điều khiển ESP32. "
    "Các đường tín hiệu TRIG và ECHO giao tiếp trực tiếp với các chân GPIO của ESP32 ở mức logic 3.3 V."
)

p_tbl1 = doc.add_paragraph()
p_tbl1.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_tbl1.paragraph_format.space_after = Pt(4)
r_t1 = p_tbl1.add_run("Bảng 2.1: Sơ đồ kết nối phần cứng giữa cảm biến RCWL-1601 và vi điều khiển ESP32")
r_t1.font.name = 'Times New Roman'
r_t1.font.size = Pt(12)
r_t1.font.bold = True

pin_data = [
    ("VCC", "3V3", "Cấp nguồn nuôi cảm biến"),
    ("GND", "GND", "Nối đất chung hệ thống"),
    ("TRIG", "GPIO 5", "Ngõ vào kích phát xung siêu âm"),
    ("ECHO", "GPIO 18", "Ngõ ra phản hồi thời gian bay ToF")
]

table_pin = doc.add_table(rows=len(pin_data)+1, cols=3)
table_pin.alignment = WD_TABLE_ALIGNMENT.CENTER
table_pin.autofit = False

pin_widths = [Cm(4.0), Cm(4.0), Cm(8.0)]
pin_headers = ["Chân RCWL-1601", "Chân ESP32", "Chức năng kỹ thuật"]

for idx, text in enumerate(pin_headers):
    c = table_pin.rows[0].cells[idx]
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

for row_idx, data in enumerate(pin_data, start=1):
    for col_idx, text in enumerate(data):
        c = table_pin.rows[row_idx].cells[col_idx]
        c.text = text
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in (0, 1) else WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            if col_idx in (0, 1):
                r.font.bold = True

for row in table_pin.rows:
    for idx, width in enumerate(pin_widths):
        row.cells[idx].width = width
        set_cell_border(row.cells[idx],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_pin.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_pin.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

add_heading_3("2.2.2. Thiết kế không gian thực nghiệm")
add_bullet_p("Hệ thống cảm biến và vật đo được đặt trên hai bàn thí nghiệm có độ cao 85.0 cm so với mặt sàn phòng đo.", "• Chiều cao bàn đo 85 cm: ")
add_bullet_p("Thực nghiệm được bố trí dọc theo hành lang kín gió dài 10 m, chiều rộng 2.8 m. Cảm biến đặt cách tường bên ít nhất 1.4 m. Trong suốt quá trình đo, hệ thống cửa được đóng kín tránh gió lùa và biến thiên nhiệt độ đột ngột.", "• Phòng đo: ")

add_heading_3("2.2.3. Bố trí mô hình và định vị thiết bị đo")
add_body_p("Để đảm bảo phép đo đạt độ chính xác cao, mô hình thực nghiệm được bố trí:")
add_bullet_p("RCWL-1601 được cắm cố định vững chắc trên breadboard, sát mép bàn, hướng hai mắt phát - thu trực diện ra ngoài.", "1. Cố định cảm biến: ")
add_bullet_p("Vật thể đo chuẩn là một viên gạch kích thước 40 cm × 40 cm có mặt trước phẳng nhẵn và mặt sau gồ ghề. Viên gạch được dựng thẳng đứng sát mép của chiếc bàn có cùng chiều cao 85 cm. Khi tiến hành đo, viên gạch luôn được căn chỉnh vuông góc với mặt bàn và đối diện với trục phát của cảm biến.", "2. Vật thể phản xạ mục tiêu: ")
add_bullet_p("Khoảng cách chuẩn d_true được xác định thủ công bằng thước dây. ", "3. Căn chỉnh cự ly bằng thước đo tiêu chuẩn: ")

# 2.3
add_heading_2("2.3. CÁC TRƯỜNG HỢP ĐO VÀ ĐIỀU KIỆN THỰC NGHIỆM")
add_body_p(
    "Để đánh giá đầy đủ, độc lập và toàn diện các đặc tính kỹ thuật, nghiên cứu thiết lập 4 trường hợp đo chuyên biệt với các điều kiện môi trường tương ứng:"
)

p_tbl2 = doc.add_paragraph()
p_tbl2.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_tbl2.paragraph_format.space_after = Pt(4)
r_t2 = p_tbl2.add_run("Bảng 2.2: Bảng tổng hợp các trường hợp đo và thông số thực nghiệm")
r_t2.font.name = 'Times New Roman'
r_t2.font.size = Pt(12)
r_t2.font.bold = True

sc_data = [
    ("Bề mặt phản xạ", "Mặt nhẵn", "Mặt nhẵn", "Mặt gồ ghề", "Mặt nhẵn"),
    ("Chiều di chuyển", "Tiến (1 – 600 cm)", "Lùi (300 – 10 cm)", "Tiến (10 – 375 cm)", "Tiến (10 – 300 cm)"),
    ("Số mốc cự ly", "35", "19", "23", "19"),
    ("Nhiệt độ môi trường", "27.0 °C", "27.0 °C", "27.0 °C", "20.0 °C"),
    ("Tổng số mẫu", "1.750", "950", "1.150", "950"),
    ("Mục đích", "Khảo sát toàn dải, độ chụm, độ chính xác, độ nhạy", "Khảo sát độ trễ", "Khảo sát tán xạ bề mặt", "Khảo sát trôi nhiệt độ")
]

table_sc = doc.add_table(rows=len(sc_data)+1, cols=5)
table_sc.alignment = WD_TABLE_ALIGNMENT.CENTER
table_sc.autofit = False

sc_widths = [Cm(3.2), Cm(3.2), Cm(3.2), Cm(3.2), Cm(3.2)]
sc_headers = ["Tham số", "FSDT", "BSDT", "FRDT", "FSAT"]

for idx, text in enumerate(sc_headers):
    c = table_sc.rows[0].cells[idx]
    c.text = text
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, data in enumerate(sc_data, start=1):
    for col_idx, text in enumerate(data):
        c = table_sc.rows[row_idx].cells[col_idx]
        c.text = text
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            if col_idx == 0:
                r.font.bold = True

for row in table_sc.rows:
    for idx, width in enumerate(sc_widths):
        row.cells[idx].width = width
        set_cell_border(row.cells[idx],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_sc.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_sc.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

# 2.4
add_heading_2("2.4. XÁC ĐỊNH CỠ MẪU TỐI ƯU")

add_heading_3("2.4.1. Tối ưu cỡ mẫu")
add_body_p(
    "Trong kỹ thuật đo lường, kết quả đo khoảng cách thực nghiệm không thể là một giá trị đơn độc, mà luôn được biểu diễn dưới dạng một khoảng tin cậy: "
    "d ∈ [d̄ - ε, d̄ + ε] (tương đương d = d̄ ± ε), trong đó d̄ là trung bình mẫu và ε là bán kính sai số ngẫu nhiên giới hạn của giá trị trung bình ở mức tin cậy 95%."
)
add_body_p(
    "Theo lý thuyết xác suất thống kê và phân phối Student, bán kính sai số ε được xác định bởi mô hình:"
)

add_equation_box("ε(N) = [ t_{0.975, N-1} · s ] / √N", "2.1")

add_body_p(
    "Trong đó: s là độ lệch chuẩn thực nghiệm đại diện cho độ tán xạ và nhiễu phần cứng thực tế trong môi trường truyền sóng; "
    "thừa số 1/√N đóng vai trò nén sai số khi tăng số lần đo lặp N. "
)

add_body_p(
    "Mâu thuẫn đặt ra là: muốn sai số ε cực nhỏ thì phải tăng N thật lớn, nhưng N càng lớn thì thời gian đo càng dài. "
    "Mục tiêu bài toán là xác định kích thước mẫu N tối ưu để sai số ε < 0.5 mm (dung sai vạch chia thước), "
    "tốc độ đạo hàm đạt ngưỡng dừng bão hòa (|dε/dN| ≈ 0), và thời gian đo đủ ngắn."
)

add_heading_3("2.4.2. Phân tích dữ liệu thực nghiệm")
add_body_p(
    "Thực nghiệm tiến hành đo liên tục 100 lần tại 3 cự ly: 50 cm, 100 cm và 150 cm (nhiệt độ 27.0°C). "
    "Dữ liệu được lưu trữ tại “du_lieu_tong_hop/mau_100.csv”. "
    "Tính độ lệch chuẩn tích lũy s(k), bán kính sai số ε_95%(k) và đạo hàm bậc 1. "
    "Kết quả tính toán được ghi lại trong “du_lieu_tong_hop/chuong_2”"
)

IMG_H2_1_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_2\hinh_2_1_hoi_tu_sai_so_N.png"
IMG_H2_2_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_2\hinh_2_2_dao_ham_diem_khuyu_tay.png"

# Chèn ảnh Hình 2.1
if os.path.exists(IMG_H2_1_PATH):
    p_img1 = doc.add_paragraph()
    p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img1.paragraph_format.space_before = Pt(8)
    p_img1.paragraph_format.space_after = Pt(4)
    run_img1 = p_img1.add_run()
    run_img1.add_picture(IMG_H2_1_PATH, width=Cm(15.0))

    p_cap1 = doc.add_paragraph()
    p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap1.paragraph_format.space_after = Pt(6)
    r_c1 = p_cap1.add_run("Hình 2.1: Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu.")
    r_c1.font.name = 'Times New Roman'
    r_c1.font.size = Pt(10)
    r_c1.font.italic = True

add_body_p(
    "Đánh giá từ đồ thị Hình 2.1: Khi số lần đo k tăng từ 2 đến khoảng 30, bán kính sai số ngẫu nhiên ε_95% giảm nhanh ở cả 3 cự ly. "
    "Từ k ≥ 40 - 50, đường cong bắt đầu đi ngang và hội tụ ổn định. "
)

# Chèn ảnh Hình 2.2
if os.path.exists(IMG_H2_2_PATH):
    p_img2 = doc.add_paragraph()
    p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img2.paragraph_format.space_before = Pt(8)
    p_img2.paragraph_format.space_after = Pt(4)
    run_img2 = p_img2.add_run()
    run_img2.add_picture(IMG_H2_2_PATH, width=Cm(15.0))

    p_cap2 = doc.add_paragraph()
    p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap2.paragraph_format.space_after = Pt(6)
    r_c2 = p_cap2.add_run("Hình 2.2: Tốc độ biến thiên sai số |dε_95%/dk| theo cỡ mẫu k.")
    r_c2.font.name = 'Times New Roman'
    r_c2.font.size = Pt(10)
    r_c2.font.italic = True

add_body_p(
    "Đánh giá từ đồ thị Hình 2.2: Đồ thị thể hiện tốc độ suy giảm sai số |dε_95%/dk| sau mỗi lần đo bổ sung. "
    "Ở các giá trị k < 20, tốc độ biến thiên cực lớn, cho thấy việc tăng số lần đo ở giai đoạn đầu giảm sai số rất hiệu quả. "
    "Khi k tiến dần đến 50, tốc độ biến thiên giảm nhanh, đường đồ thị chuyển sang đi ngang, "
    "việc đo thêm sau mốc 50 hầu như không làm sai số giảm hiệu quả như ban đầu."
)

add_body_p(
    "Kết luận: Dựa trên các phân tích và đánh giá từ hai đồ thị và bảng số liệu nêu trên, "
    "nhóm nghiên cứu đưa ra quyết định lựa chọn cỡ mẫu N = 50 cho toàn bộ các phép đo thực nghiệm."
)

doc.save(FILE_PATH)
print(f"Nối thành công Chương 2 vào tệp Word: {FILE_PATH}")
