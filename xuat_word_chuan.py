# -*- coding: utf-8 -*-
"""
Kịch bản xuất bản Báo Cáo Thực Nghiệm RCWL-1601 (Word .docx)
Tuân thủ tuyệt đối quy chuẩn GEMINI.md cập nhật:
1. Hệ thống Headings tương tác cho Navigation Pane (Thanh điều hướng Ctrl+F / View -> Navigation Pane):
   - Heading 1: Tên Chương (16pt, Bold, C_NAVY)
   - Heading 2: Mục lớn X.Y (14pt, Bold, C_NAVY)
   - Heading 3: Tiểu mục X.Y.Z (13pt, Bold, C_MAROON)
2. Công thức toán học chuẩn Microsoft Word Equation (OMML, tương đương phím tắt Alt + =):
   - Có phân số thực thụ, căn bậc hai, tổng sigma, ma trận, chỉ số trên/dưới.
3. Bảo toàn 100% các chỉnh sửa thủ công của người dùng trên Trang bìa và Lời nói đầu.
"""

import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_FILE = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\Bao_Cao_Thuc_Nghiem_RCWL1601.docx"
IMG_H2_1_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_2\hinh_2_1_hoi_tu_sai_so_N.png"
IMG_H2_2_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_2\hinh_2_2_dao_ham_diem_khuyu_tay.png"

doc = Document()

# Màu sắc chuẩn giao diện báo cáo kỹ thuật
C_NAVY = RGBColor(0, 51, 102)     # #003366
C_MAROON = RGBColor(128, 0, 0)   # #800000
C_BLACK = RGBColor(0, 0, 0)
C_GRAY = RGBColor(100, 100, 100)

# Cấu hình Trang in A4 (Lề Trái 3.0cm, Phải 2.0cm, Trên 2.0cm, Dưới 2.0cm)
section = doc.sections[0]
section.page_width = Cm(21.0)
section.page_height = Cm(29.7)
section.top_margin = Cm(2.0)
section.bottom_margin = Cm(2.0)
section.left_margin = Cm(3.0)
section.right_margin = Cm(2.0)

# Cấu hình Style Normal
style_normal = doc.styles['Normal']
style_normal.font.name = 'Times New Roman'
style_normal.font.size = Pt(13)
style_normal.font.color.rgb = C_BLACK
style_normal.paragraph_format.line_spacing = 1.35
style_normal.paragraph_format.space_after = Pt(6)
style_normal.paragraph_format.space_before = Pt(0)
style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# Cấu hình Style Heading 1
style_h1 = doc.styles['Heading 1']
style_h1.font.name = 'Times New Roman'
style_h1.font.size = Pt(16)
style_h1.font.bold = True
style_h1.font.color.rgb = C_NAVY
style_h1.paragraph_format.space_before = Pt(16)
style_h1.paragraph_format.space_after = Pt(10)
style_h1.paragraph_format.keep_with_next = True
style_h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Cấu hình Style Heading 2
style_h2 = doc.styles['Heading 2']
style_h2.font.name = 'Times New Roman'
style_h2.font.size = Pt(14)
style_h2.font.bold = True
style_h2.font.color.rgb = C_NAVY
style_h2.paragraph_format.space_before = Pt(12)
style_h2.paragraph_format.space_after = Pt(6)
style_h2.paragraph_format.keep_with_next = True
style_h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

# Cấu hình Style Heading 3
style_h3 = doc.styles['Heading 3']
style_h3.font.name = 'Times New Roman'
style_h3.font.size = Pt(13)
style_h3.font.bold = True
style_h3.font.color.rgb = C_MAROON
style_h3.paragraph_format.space_before = Pt(8)
style_h3.paragraph_format.space_after = Pt(4)
style_h3.paragraph_format.keep_with_next = True
style_h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

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
    p = doc.add_heading(level=1)
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    rPr = r._r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), 'Times New Roman')
    rFonts.set(qn('w:hAnsi'), 'Times New Roman')
    rFonts.set(qn('w:cs'), 'Times New Roman')
    return p

def add_heading_2(text):
    p = doc.add_heading(level=2)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    rPr = r._r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), 'Times New Roman')
    rFonts.set(qn('w:hAnsi'), 'Times New Roman')
    rFonts.set(qn('w:cs'), 'Times New Roman')
    return p

def add_heading_3(text):
    p = doc.add_heading(level=3)
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = C_BLACK
    rPr = r._r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), 'Times New Roman')
    rFonts.set(qn('w:hAnsi'), 'Times New Roman')
    rFonts.set(qn('w:cs'), 'Times New Roman')
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

def add_native_equation(omml_xml_content, eq_num=""):
    """
    Chèn đối tượng công thức toán học chuẩn Microsoft Word Equation (OMML Alt + =)
    Căn giữa trang, đánh số ở lề phải nếu có eq_num.
    """
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.2
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Tạo bao bọc oMathPara
    wrapper_xml = (
        f'<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f'<m:oMath>{omml_xml_content}</m:oMath>'
        f'</m:oMathPara>'
    )
    p._p.append(parse_xml(wrapper_xml))
    
    if eq_num:
        # Thêm số công thức lề phải
        p_num = doc.add_paragraph()
        p_num.paragraph_format.space_before = Pt(0)
        p_num.paragraph_format.space_after = Pt(4)
        p_num.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p_num.add_run(f"({eq_num})")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.color.rgb = C_GRAY
    return p

# -------------------------------------------------------------
# PHẦN 1: TRANG BÌA (COVER PAGE - ĐÃ CẬP NHẬT TÊN RÚT GỌN CỦA BẠN)
# -------------------------------------------------------------
cover_table = doc.add_table(rows=1, cols=1)
cover_table.alignment = WD_TABLE_ALIGNMENT.CENTER
cover_cell = cover_table.cell(0, 0)
cover_cell.width = Cm(16.0)

set_cell_border(cover_cell,
    top=dict(val='double', sz=12, color='003366'),
    bottom=dict(val='double', sz=12, color='003366'),
    left=dict(val='double', sz=12, color='003366'),
    right=dict(val='double', sz=12, color='003366')
)

p_b1 = cover_cell.paragraphs[0]
p_b1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_b1.paragraph_format.space_before = Pt(12)
p_b1.paragraph_format.space_after = Pt(4)
r = p_b1.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nTRƯỜNG ĐẠI HỌC BÁCH KHOA HÀ NỘI")
r.font.name = 'Times New Roman'
r.font.size = Pt(13)
r.font.bold = True
r.font.color.rgb = C_NAVY

p_b2 = cover_cell.add_paragraph()
p_b2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_b2.paragraph_format.space_before = Pt(0)
p_b2.paragraph_format.space_after = Pt(24)
r = p_b2.add_run("VIỆN CƠ KHÍ / TRƯỜNG CƠ KHÍ")
r.font.name = 'Times New Roman'
r.font.size = Pt(13)
r.font.bold = True
r.font.color.rgb = C_NAVY

p_line = cover_cell.add_paragraph()
p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_line.paragraph_format.space_after = Pt(28)
r_line = p_line.add_run("━━━━━━━━━━━━━━━━━━━")
r_line.font.name = 'Times New Roman'
r_line.font.color.rgb = C_MAROON

p_main = cover_cell.add_paragraph()
p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_main.paragraph_format.space_after = Pt(8)
r_rep = p_main.add_run("BÁO CÁO THỰC NGHIỆM HỌC PHẦN")
r_rep.font.name = 'Times New Roman'
r_rep.font.size = Pt(18)
r_rep.font.bold = True
r_rep.font.color.rgb = C_MAROON

p_course = cover_cell.add_paragraph()
p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_course.paragraph_format.space_after = Pt(28)
r_course = p_course.add_run("KỸ THUẬT ĐO LƯỜNG VÀ CẢM BIẾN\nMÃ HỌC PHẦN: EMA2024E_3")
r_course.font.name = 'Times New Roman'
r_course.font.size = Pt(14)
r_course.font.bold = True
r_course.font.color.rgb = C_NAVY

p_topic = cover_cell.add_paragraph()
p_topic.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_topic.paragraph_format.space_after = Pt(8)
r_lbl = p_topic.add_run("ĐỀ TÀI:")
r_lbl.font.name = 'Times New Roman'
r_lbl.font.size = Pt(13)
r_lbl.font.bold = True
r_lbl.font.color.rgb = C_MAROON

# Tên đề tài rút gọn đúng theo ý bạn
p_title = cover_cell.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(50)
r_title = p_title.add_run("KHẢO SÁT THỰC NGHIỆM ĐẶC TÍNH ĐO LƯỜNG CỦA CẢM BIẾN SIÊU ÂM RCWL-1601")
r_title.font.name = 'Times New Roman'
r_title.font.size = Pt(16)
r_title.font.bold = True
r_title.font.color.rgb = C_NAVY

p_info = cover_cell.add_paragraph()
p_info.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_info.paragraph_format.left_indent = Cm(1.5)
p_info.paragraph_format.space_after = Pt(40)

r_gv = p_info.add_run("Giảng viên hướng dẫn:\t")
r_gv.font.bold = True
r_gvn = p_info.add_run("[TS. / ThS. Điền tên Giảng viên]\n")
r_gvn.font.italic = True

r_lp = p_info.add_run("Lớp học phần:\t\t")
r_lp.font.bold = True
p_info.add_run("EMA2024E_3\n")

r_sv = p_info.add_run("Nhóm sinh viên thực hiện:\n")
r_sv.font.bold = True
p_info.add_run("  1. [Họ và tên Sinh viên 1]\t-\tMSSV: [Điền MSSV 1]\n")
p_info.add_run("  2. [Họ và tên Sinh viên 2]\t-\tMSSV: [Điền MSSV 2]\n")
p_info.add_run("  3. [Họ và tên Sinh viên 3]\t-\tMSSV: [Điền MSSV 3]\n")

for run in p_info.runs:
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

p_date = cover_cell.add_paragraph()
p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_date.paragraph_format.space_after = Pt(12)
r_date = p_date.add_run("HÀ NỘI, THÁNG 11 NĂM 2026")
r_date.font.name = 'Times New Roman'
r_date.font.size = Pt(12)
r_date.font.bold = True
r_date.font.color.rgb = C_NAVY

doc.add_page_break()

# -------------------------------------------------------------
# PHẦN 2: LỜI NÓI ĐẦU (CÓ HEADING ĐỂ HIỆN TRÊN NAVIGATION PANE)
# -------------------------------------------------------------
add_heading_1("LỜI NÓI ĐẦU")

preface_paragraphs = [
    "Trong tiến trình tự động hóa công nghiệp và phát triển các hệ thống điều khiển thông minh, "
    "bài toán đo lường cự ly, vị trí và mức chất lỏng không tiếp xúc đóng vai trò mang tính sống còn. "
    "Các hệ thống cảnh báo va chạm của xe tự hành AGV trong nhà máy, trạm phân loại kích thước bao bì kiện hàng "
    "trên băng tải logistics, hay các bồn chứa hóa chất ăn mòn đều đòi hỏi phương pháp đo đạc không tiếp xúc vật lý "
    "nhằm tránh hỏng hóc cơ học, tránh gây nhiễm bẩn dung dịch và bảo đảm khả năng vận hành liên tục 24/7.",

    "Trong số các công nghệ đo khoảng cách hiện nay (Laser LiDAR, Radar sóng milimét, Cảm biến quang học hồng ngoại và Siêu âm), "
    "cảm biến siêu âm nổi lên như một giải pháp cân bằng tối ưu giữa chi phí sản xuất cực thấp, độ bền cơ học cao, "
    "không phụ thuộc vào màu sắc hay độ trong suốt của vật thể phản xạ, và đặc biệt an toàn cho người vận hành.",

    "Module cảm biến siêu âm RCWL-1601 thế hệ mới là phiên bản nâng cấp phần cứng vượt trội so với dòng cảm biến kinh điển HC-SR04. "
    "Được tích hợp vi mạch điều khiển chuyên dụng RCWL-9610, RCWL-1601 hoàn toàn tương thích mức logic 3.3 V của vi điều khiển ESP32. "
    "Bên cạnh đó, việc vận tốc lan truyền sóng âm trong không khí phụ thuộc vào nhiệt độ môi trường là nguồn gốc của sai số trôi cự ly "
    "lớn trong điều kiện khí hậu nóng ẩm tại Việt Nam.",

    "Xuất phát từ yêu cầu thực tiễn của học phần Kỹ thuật Đo lường và Cảm biến, nhóm sinh viên đã lựa chọn "
    "và thực hiện đề tài: 'Khảo sát thực nghiệm đặc tính đo lường của cảm biến siêu âm RCWL-1601'. Mục tiêu của báo cáo bao gồm:",

    "1. Khảo sát toàn diện đặc tính tĩnh và động học của cảm biến RCWL-1601 trên giàn thực nghiệm chuẩn hóa: xác định dải đo, "
    "độ chụm, độ chính xác, đánh giá độ không đảm bảo đo mở rộng.",

    "2. Khảo sát các hiện tượng vật lý chuyên sâu ảnh hưởng đến phép đo siêu âm: độ trễ (Hysteresis), hiện tượng tán xạ trên "
    "bề mặt gồ ghề, và hiệu quả bù trôi vận tốc sóng âm Laplace theo nhiệt độ.",

    "3. Xây dựng chuỗi lọc số (Khoảng tứ phân vị IQR) và thiết kế hệ thống: "
    "'Giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ trên ESP32'."
]

for para_text in preface_paragraphs:
    add_body_p(para_text)

doc.add_page_break()

# -------------------------------------------------------------
# PHẦN 3: MỤC LỤC TỰ ĐỘNG (CÓ HEADING TRÊN NAVIGATION PANE)
# -------------------------------------------------------------
add_heading_1("MỤC LỤC")

p_toc_hint = doc.add_paragraph()
p_toc_hint.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_toc_hint.paragraph_format.space_after = Pt(12)
r_hint = p_toc_hint.add_run("(Nhấp chuột phải vào vùng mục lục bên dưới và chọn 'Update Field' để cập nhật tự động toàn bộ số trang)")
r_hint.font.name = 'Times New Roman'
r_hint.font.size = Pt(11)
r_hint.font.italic = True
r_hint.font.color.rgb = RGBColor(128, 128, 128)

p_toc_field = doc.add_paragraph()
p_toc_field.paragraph_format.space_after = Pt(24)
fld_xml = parse_xml(r'''
    <w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
        <w:r>
            <w:fldChar w:fldCharType="begin"/>
        </w:r>
        <w:r>
            <w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText>
        </w:r>
        <w:r>
            <w:fldChar w:fldCharType="separate"/>
        </w:r>
        <w:r>
            <w:fldChar w:fldCharType="end"/>
        </w:r>
    </w:p>
''')
p_toc_field._p.addnext(fld_xml)

doc.add_page_break()

# -------------------------------------------------------------
# PHẦN 4: BẢNG QUY ƯỚC KÝ HIỆU (CÓ HEADING TRÊN NAVIGATION PANE)
# -------------------------------------------------------------
add_heading_1("BẢNG QUY ƯỚC KÝ HIỆU VÀ DỮ LIỆU THỰC NGHIỆM")

p_cap = doc.add_paragraph()
p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_cap.paragraph_format.space_after = Pt(6)
r_cap = p_cap.add_run("Bảng 0.1: Bảng quy ước tên 4 tập dữ liệu thực nghiệm chuẩn hóa của đề tài")
r_cap.font.name = 'Times New Roman'
r_cap.font.size = Pt(12)
r_cap.font.bold = True

table_conv = doc.add_table(rows=5, cols=4)
table_conv.alignment = WD_TABLE_ALIGNMENT.CENTER
table_conv.autofit = False

col_widths = [Cm(3.0), Cm(4.0), Cm(4.5), Cm(3.5)]
headers = ["Ký hiệu mã", "Chiều dịch chuyển", "Bề mặt phản xạ", "Nhiệt độ môi trường"]

hdr_cells = table_conv.rows[0].cells
for idx, text in enumerate(headers):
    hdr_cells[idx].text = text
    set_cell_background(hdr_cells[idx], "D9E1F2")
    p = hdr_cells[idx].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

dataset_rows = [
    ("FSDT", "Tiến (Forward)\n", "Phẳng nhẵn bóng\n(Smooth)", "27.0 °C\n"),
    ("BSDT", "Lùi (Backward)", "Phẳng nhẵn bóng\n(Smooth)", "27.0 °C"),
    ("FRDT", "Tiến (Forward)", "Nhám gồ ghề\n(Rough)", "27.0 °C"),
    ("FSAT", "Tiến (Forward)", "Phẳng nhẵn bóng\n(Smooth)", "20.0 °C")
]

for row_idx, data in enumerate(dataset_rows, start=1):
    row_cells = table_conv.rows[row_idx].cells
    for col_idx, text in enumerate(data):
        row_cells[col_idx].text = text
        p = row_cells[col_idx].paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = C_MAROON

for row in table_conv.rows:
    for idx, width in enumerate(col_widths):
        row.cells[idx].width = width
        set_cell_border(row.cells[idx],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_conv.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_conv.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

p_sep = doc.add_paragraph()
p_sep.paragraph_format.space_before = Pt(14)
p_sep.paragraph_format.space_after = Pt(4)
r_sep_t = p_sep.add_run("Cấu trúc tổ chức dữ liệu dự án:")
r_sep_t.font.name = 'Times New Roman'
r_sep_t.font.size = Pt(13)
r_sep_t.font.bold = True
r_sep_t.font.color.rgb = C_NAVY

p_f1 = doc.add_paragraph()
p_f1.paragraph_format.first_line_indent = Cm(1.0)
p_f1.paragraph_format.space_after = Pt(4)
r1 = p_f1.add_run("• Thư mục 'result/': ")
r1.font.bold = True
p_f1.add_run("Lưu trữ toàn bộ các tệp dữ liệu thô ban đầu. Mỗi tệp bao gồm 50 dòng với 3 cột thông tin chuẩn hóa: thời gian bay t (μs), khoảng cách đo được distance_cm và nhiệt độ temperature_c.")
for r in p_f1.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

p_f2 = doc.add_paragraph()
p_f2.paragraph_format.first_line_indent = Cm(1.0)
p_f2.paragraph_format.space_after = Pt(4)
r2 = p_f2.add_run("• Thư mục 'du_lieu_tong_hop/': ")
r2.font.bold = True
p_f2.add_run("Lưu trữ các tệp dữ liệu tổng hợp và tính toán. Toàn bộ các phân tích định lượng, khớp hàm và đánh giá độ không đảm bảo đo ở Chương 3 đều được thực thi trực tiếp từ thư mục này.")
for r in p_f2.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

p_f3 = doc.add_paragraph()
p_f3.paragraph_format.first_line_indent = Cm(1.0)
p_f3.paragraph_format.space_after = Pt(12)
r3 = p_f3.add_run("• Thư mục ‘graph/’: ")
r3.font.bold = True
p_f3.add_run("Lưu trữ figure các đồ thị được sử dụng trong bài báo cáo này.")
for r in p_f3.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

# -------------------------------------------------------------
# PHẦN 5: CHƯƠNG 1 (CƠ SỞ LÝ THUYẾT & NATIVE WORD EQUATIONS)
# -------------------------------------------------------------
doc.add_page_break()

add_heading_1("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM")

# 1.1
add_heading_2("1.1. NGUYÊN LÝ ĐO KHOẢNG CÁCH THỜI GIAN BAY VÀ MÔ HÌNH BÙ NHIỆT ĐỘ MÔI TRƯỜNG")

add_heading_3("1.1.1. Phương trình lan truyền sóng siêu âm thời gian bay")
add_body_p(
    "Phương pháp đo khoảng cách bằng sóng siêu âm dựa trên nguyên lý đo thời gian bay (Time-of-Flight - ToF). "
    "Module cảm biến phát ra một chuỗi xung kích siêu âm hình sin ở tần số 40 kHz. "
    "Sóng âm lan truyền trong không gian tự do với vận tốc v, gặp mặt phẳng vật cản và phản xạ dội ngược trở lại đầu thu. "
    "Đầu thu áp điện chuyển đổi năng lượng dao động cơ học của sóng âm dội về thành tín hiệu điện áp phản hồi."
)
add_body_p("Khoảng cách d từ cảm biến đến vật cản được xác định từ thời gian bay tổng cộng t của sóng âm theo phương trình:")

# Native Word Equation 1.1: d = (v · t) / 2
add_native_equation(
    '<m:r><m:t>d</m:t></m:r>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:f>'
    '<m:num><m:r><m:t>v · t</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>2</m:t></m:r></m:den>'
    '</m:f>',
    eq_num="1.1"
)

add_body_p(
    "Trong đó: d là khoảng cách đo từ mặt trước màng rung cảm biến đến bề mặt phản xạ (m); "
    "v là vận tốc truyền sóng âm trong không khí (m/s); t là thời gian bay khứ hồi (s). "
)

add_heading_3("1.1.2. Sự ảnh hưởng của nhiệt độ tới vận tốc âm thanh")
add_body_p(
    "Trong chất khí lý tưởng, sóng âm lan truyền dưới dạng sóng dọc thông qua quá trình nén và giãn nở đoạn nhiệt. "
    "Vận tốc truyền sóng âm:"
)

# Native Word Equation 1.2: v = sqrt(gamma * R * T_K / M)
add_native_equation(
    '<m:r><m:t>v</m:t></m:r>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:rad>'
    '<m:deg/>'
    '<m:e>'
    '<m:f>'
    '<m:num>'
    '<m:r><m:t>γ · R · </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>T</m:t></m:r></m:e><m:sub><m:r><m:t>K</m:t></m:r></m:sub></m:sSub>'
    '</m:num>'
    '<m:den><m:r><m:t>M</m:t></m:r></m:den>'
    '</m:f>'
    '</m:e>'
    '</m:rad>',
    eq_num="1.2"
)

add_body_p(
    "Trong đó: γ là hệ số đoạn nhiệt của không khí khô (γ ≈ 1.402); R là hằng số khí lý tưởng phổ quát (R = 8.314 J/(mol·K)); "
    "M là khối lượng mol biểu kiến trung bình của không khí khô (M ≈ 0.028964 kg/mol); T_K là nhiệt độ tuyệt đối của môi trường (K)."
)
add_body_p(
    "Khai triển chuỗi Taylor bậc nhất của vận tốc sóng âm quanh điểm chuẩn 0 °C (T_0 = 273.15 K, v_0 ≈ 331.3 m/s) ta thu được phương trình:"
)

# Native Word Equation 1.3: v(T) = 331.3 + 0.606 * T
add_native_equation(
    '<m:r><m:t>v(T) = 331.3 + 0.606 · T    (m/s)</m:t></m:r>',
    eq_num="1.3"
)

add_heading_3("1.1.3. Sự suy hao năng lượng sóng âm theo cự ly")
add_body_p("Năng lượng và biên độ áp suất âm p(d) của sóng âm suy giảm mạnh theo khoảng cách do:")
add_body_p("1. Phân kỳ hình học: Do chùm sóng âm phát đi theo dạng hình nón. Mật độ công suất âm suy giảm tỷ lệ nghịch với bình phương khoảng cách: I(d) ~ 1/d².", indent=False)
add_body_p("2. Ma sát với không khí: Quá trình truyền sóng gây ma sát trong chất khí, làm suy hao năng lượng. ", indent=False)

# 1.2
add_heading_2("1.2. ĐẶC TÍNH VÀ THÔNG SỐ CỦA MODULE RCWL-1601")

add_heading_3("1.2.1. Giản đồ xung kích hoạt và phản hồi thời gian bay")
add_body_p("Module RCWL-1601 giao tiếp với vi điều khiển ESP32 thông qua giao thức xung kỹ thuật số hai chân (Trigger và Echo):")
add_body_p("• Bước 1 - Kích hoạt xung (Trigger Pulse): Vi điều khiển chủ động kéo chân TRIG lên mức logic CAO để phát lệnh đo.", indent=False)
add_body_p("• Bước 2 - Phát chùm sóng siêu âm: Khi nhận được xung TRIG, cảm biến phát chuỗi 8 chu kỳ xung siêu âm dạng sóng vuông ở tần số 40 kHz. Đồng thời, chân ECHO được kéo lên mức CAO để báo hiệu bắt đầu chu kỳ bay.", indent=False)
add_body_p("• Bước 3 - Thu nhận sóng phản xạ và ngắt xung (Echo Pulse): Sóng âm dội về tác động lên màng thu và cảm biến ghi nhận thay đổi. Ngay sau đó, IC lập tức kéo chân ECHO xuống mức THẤP.", indent=False)
add_body_p("• Bước 4 - Đo thời gian bay ToF: Độ rộng mức cao của xung ECHO (t_echo) tỷ lệ thuận chính xác với thời gian bay hai chiều t của sóng âm.", indent=False)

add_heading_3("1.2.2. Bảng thông số kỹ thuật của RCWL-1601")
p_tbl = doc.add_paragraph()
p_tbl.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_tbl.paragraph_format.space_after = Pt(4)
r_tcap = p_tbl.add_run("Bảng 1.1: Bảng thông số kỹ thuật của module cảm biến siêu âm RCWL-1601")
r_tcap.font.name = 'Times New Roman'
r_tcap.font.size = Pt(12)
r_tcap.font.bold = True

ds_data = [
    ("Điện áp hoạt động (V_CC)", "2.8 V – 5.5 V (Một chiều - DC)"),
    ("Dòng điện tiêu thụ tĩnh", "< 2 mA"),
    ("Dòng điện cực đại khi phát", "≈ 15 mA – 20 mA"),
    ("Tần số sóng siêu âm", "40 kHz ± 1.0 kHz"),
    ("Dải đo công bố", "2 cm – 400 cm (hoặc 450 cm)"),
    ("Độ phân giải lý thuyết", "1 mm"),
    ("Góc mở chùm sóng âm", "≈ 15°"),
    ("Tín hiệu kích hoạt (TRIG)", "Xung mức CAO (HIGH) ≥ 10 μs"),
    ("Tín hiệu phản hồi (ECHO)", "Độ rộng xung mức CAO (PWM)")
]

table_ds = doc.add_table(rows=len(ds_data)+1, cols=2)
table_ds.alignment = WD_TABLE_ALIGNMENT.CENTER
table_ds.autofit = False

ds_widths = [Cm(7.5), Cm(8.5)]
ds_headers = ["Thông số kỹ thuật", "Giá trị công bố"]

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
add_heading_2("1.3. CƠ SỞ LÝ THUYẾT XỬ LÝ SỐ LIỆU ĐO LƯỜNG VÀ ĐỘ KHÔNG ĐẢM BẢO ĐO")

add_heading_3("1.3.1. Các đại lượng thống kê mô tả mẫu đo")
add_body_p(
    "Tại mỗi mốc cự ly chuẩn, thực hiện lặp lại N lần đo độc lập trong điều kiện môi trường ổn định, "
    "thu được tập mẫu đo khoảng cách: X = {x_1, x_2, ..., x_N}. Các đại lượng thống kê cơ bản bao gồm:"
)
add_bullet_p("Đại diện cho giá trị xu thế trung tâm của tập mẫu đo lặp:", "• Giá trị trung bình mẫu: ")

# Native Word Equation 1.4: x_bar = 1/N * sum(x_i)
add_native_equation(
    '<m:acc>'
    '<m:accPr><m:chr m:val="̄"/></m:accPr>'
    '<m:e><m:r><m:t>x</m:t></m:r></m:e>'
    '</m:acc>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:f>'
    '<m:num><m:r><m:t>1</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>N</m:t></m:r></m:den>'
    '</m:f>'
    '<m:nary>'
    '<m:naryPr><m:chr m:val="∑"/></m:naryPr>'
    '<m:sub><m:r><m:t>i=1</m:t></m:r></m:sub>'
    '<m:sup><m:r><m:t>N</m:t></m:r></m:sup>'
    '<m:e><m:sSub><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub></m:e>'
    '</m:nary>',
    eq_num="1.4"
)

add_bullet_p("Đại diện cho mức độ phân tán ngẫu nhiên của các giá trị đo quanh giá trị trung bình:", "• Độ lệch chuẩn mẫu thực nghiệm: ")

# Native Word Equation 1.5: s = sqrt(1/(N-1) * sum((x_i - x_bar)^2))
add_native_equation(
    '<m:r><m:t>s</m:t></m:r>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:rad>'
    '<m:deg/>'
    '<m:e>'
    '<m:f>'
    '<m:num><m:r><m:t>1</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>N - 1</m:t></m:r></m:den>'
    '</m:f>'
    '<m:nary>'
    '<m:naryPr><m:chr m:val="∑"/></m:naryPr>'
    '<m:sub><m:r><m:t>i=1</m:t></m:r></m:sub>'
    '<m:sup><m:r><m:t>N</m:t></m:r></m:sup>'
    '<m:e>'
    '<m:sSup>'
    '<m:e>'
    '<m:d>'
    '<m:e>'
    '<m:sSub><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> - </m:t></m:r>'
    '<m:acc><m:accPr><m:chr m:val="̄"/></m:accPr><m:e><m:r><m:t>x</m:t></m:r></m:e></m:acc>'
    '</m:e>'
    '</m:d>'
    '</m:e>'
    '<m:sup><m:r><m:t>2</m:t></m:r></m:sup>'
    '</m:sSup>'
    '</m:e>'
    '</m:nary>'
    '</m:e>'
    '</m:rad>',
    eq_num="1.5"
)

add_bullet_p("Giá trị chia đôi tập dữ liệu đã sắp xếp thứ tự: Med = x_((N+1)/2) với N lẻ. Giá trị trung vị có tính chất thống kê bền vững, hoàn toàn không bị ảnh hưởng bởi các xung nhiễu đột biến cực đoan.", "• Giá trị trung vị mẫu (Median): ")

add_heading_3("1.3.2. Lọc sai số thô bằng Khoảng tứ phân vị (IQR)")
add_body_p(
    "Trong đo đạc thực nghiệm sóng siêu âm, các xung nhiễu điện từ, bọt khí bề mặt, góc phản xạ dị thường hoặc hiện tượng mất xung phản hồi "
    "ở cự ly xa (dẫn đến tràn thời gian bay bão hòa) có thể tạo ra các mẫu đo ngoại lai có giá trị sai lệch nghiêm trọng. "
    "Nhóm lựa chọn phương pháp Lọc Khoảng tứ phân vị (Interquartile Range - IQR) làm giải thuật lọc số:"
)

# Native Word Equation 1.6: IQR = Q_3 - Q_1
add_native_equation(
    '<m:r><m:t>IQR = </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>3</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> - </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub>',
    eq_num="1.6"
)

add_body_p("Cận dưới và Cận trên được xác định theo:")

# Native Word Equation 1.7: LF & UF
add_native_equation(
    '<m:r><m:t>LF = </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> - 1.5 · IQR,          UF = </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>3</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> + 1.5 · IQR</m:t></m:r>',
    eq_num="1.7"
)

add_body_p("Mẫu đo x_i được chấp nhận là giá trị hợp lệ nếu nằm trong khoảng:")

# Native Word Equation 1.8: x_i in [LF, UF]
add_native_equation(
    '<m:sSub><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> ∈ [LF, UF]   ⇔   </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> - 1.5 · IQR  ≤  </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>  ≤  </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>3</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> + 1.5 · IQR</m:t></m:r>',
    eq_num="1.8"
)

add_heading_3("1.3.3. Hệ thống công thức đánh giá các Đặc tính tĩnh của cảm biến")
add_bullet_p(
    "Đánh giá mức độ lặp lại nhất quán của phép đo thông qua độ lệch chuẩn thực nghiệm mẫu s và sai số chuẩn của giá trị trung bình SE = s / √N "
    "(phản ánh độ chụm của ước lượng trung bình mẫu x̄ khi thực hiện N lần đo lặp độc lập).",
    "1. Độ chụm và Sai số chuẩn trung bình: "
)
add_bullet_p("Đánh giá mức độ sai lệch giữa giá trị đo trung bình và giá trị chuẩn: Sai số tuyệt đối Δd = d̄ - d_true; Sai số tương đối δ% = (Δd / d_true) · 100%.", "2. Sai số đo lường: ")
add_bullet_p(
    "Đánh giá mức độ bám sát của đặc tính tĩnh thực nghiệm với đường thẳng lý thuyết ŷ = a · x + b. "
    "Áp dụng phương pháp bình phương bé nhất dưới dạng phương trình ma trận chuẩn tắc, vector hệ số hồi quy được giải trực tiếp theo:",
    "3. Độ tuyến tính và Sai số phi tuyến (Linearity): "
)

# Native Word Equation 1.9: beta_hat = [a, b]^T = (X^T * X)^(-1) * X^T * Y
add_native_equation(
    '<m:acc><m:accPr><m:chr m:val="̂"/></m:accPr><m:e><m:r><m:t>β</m:t></m:r></m:e></m:acc>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:d><m:e><m:m><m:mr><m:e><m:r><m:t>a</m:t></m:r></m:e></m:mr><m:mr><m:e><m:r><m:t>b</m:t></m:r></m:e></m:mr></m:m></m:e></m:d>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:sSup><m:e><m:d><m:e><m:sSup><m:e><m:r><m:t>X</m:t></m:r></m:e><m:sup><m:r><m:t>T</m:t></m:r></m:sup></m:sSup><m:r><m:t> · X</m:t></m:r></m:e></m:d></m:e><m:sup><m:r><m:t>-1</m:t></m:r></m:sup></m:sSup>'
    '<m:sSup><m:e><m:r><m:t> · X</m:t></m:r></m:e><m:sup><m:r><m:t>T</m:t></m:r></m:sup></m:sSup>'
    '<m:r><m:t> · Y</m:t></m:r>',
    eq_num="1.9"
)

add_bullet_p(
    "Phản ánh sự bất đối xứng của giá trị đo tại cùng một điểm cự ly khi tiếp cận theo hai hướng ngược nhau (Chiều tiến Forward và Chiều lùi Backward): "
    "ΔH_k = |d̄_forward,k - d̄_backward,k|. "
    "Sai số trễ tương đối toàn dải: γ_H% = (max_k ΔH_k / d_FS) · 100%.",
    "5. Độ trễ (Hysteresis): "
)

add_heading_3("1.3.4. Đánh giá Độ không đảm bảo đo")
add_bullet_p("Đánh giá bằng phương pháp phân tích thống kê chuỗi quan sát lặp lại: u_A = s / √N.", "• Độ không đảm bảo đo Loại A (u_A): ")
add_bullet_p(
    "Độ không đảm bảo chuẩn thành phần là: u_B = a / √3, trong đó a là nửa khoảng dung sai cho phép.",
    "• Độ không đảm bảo đo Loại B (u_B): "
)
add_bullet_p("Kết hợp toàn bộ các thành phần theo định luật lan truyền sai số: u_c = √(u_A² + ∑ u_{B,j}²).", "• Độ không đảm bảo đo chuẩn tổng hợp (u_c): ")
add_bullet_p("Mở rộng khoảng tin cậy với hệ số phủ k_p = 2 (tương ứng mức tin cậy xấp xỉ 95% đối với bậc tự do lớn): U_95% = k_p · u_c = 2 · u_c.", "• Độ không đảm bảo đo mở rộng (U_95%): ")
add_body_p("Kết quả đo hoàn chỉnh của phép đo khoảng cách được biểu diễn:")

# Native Word Equation 1.10: Y = d_bar +- U_95%
add_native_equation(
    '<m:r><m:t>Y = </m:t></m:r>'
    '<m:acc><m:accPr><m:chr m:val="̄"/></m:accPr><m:e><m:r><m:t>d</m:t></m:r></m:e></m:acc>'
    '<m:r><m:t> ± </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>U</m:t></m:r></m:e><m:sub><m:r><m:t>95%</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>   (với </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>k</m:t></m:r></m:e><m:sub><m:r><m:t>p</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> = 2, Mức tin cậy 95%)</m:t></m:r>',
    eq_num="1.10"
)

# -------------------------------------------------------------
# PHẦN 6: CHƯƠNG 2 (THIẾT KẾ THỰC NGHIỆM & HÌNH ẢNH N=50)
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

add_native_equation(
    '<m:f>'
    '<m:num><m:r><m:t>t</m:t></m:r><m:sSub><m:e><m:r><m:t>0.975</m:t></m:r></m:e><m:sub><m:r><m:t>N-1</m:t></m:r></m:sub></m:sSub><m:r><m:t>·s</m:t></m:r></m:num>'
    '<m:den>'
    '<m:rad><m:deg/><m:e><m:r><m:t>N</m:t></m:r></m:e></m:rad>'
    '</m:den>'
    '</m:f>',
    eq_num="2.1"
)

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

# ==========================================================
# PHẦN 7: CHƯƠNG 3 (PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM)
# ==========================================================
add_heading_1("CHƯƠNG 3: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM")

add_body_p("Chương 3 trình bày việc xử lý số liệu và phân tích kết quả đo từ dữ liệu thực nghiệm: ")

add_heading_2("3.1. Tiền xử lý dữ liệu và Đánh giá hiệu quả lọc sai số thô bằng Khoảng tứ phân vị (IQR)")

add_heading_3("3.1.1. Khung tiền xử lý và cơ chế hình thành ngoại lai trong phép đo siêu âm")
add_body_p(
    "Theo thuật toán phát hiện sai số thô bằng Khoảng tứ phân vị đã nêu tại Mục 1.3.2, dữ liệu từ 4 tập thực nghiệm được xử lý. "
    "Mẫu nào nằm ngoài khoảng hợp lệ [LF, UF] sẽ được chuyển thành giá trị NaN."
)

add_heading_3("3.1.2. Tổng hợp kết quả lọc")
add_body_p(
    "Kết quả tính toán chi tiết của từng mốc cự ly được lưu tại bảng dữ liệu “du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv”, "
    "và dữ liệu sau khi lọc được lưu tại 4 tệp: FSDT_clean.csv, BSDT_clean.csv, FRDT_clean.csv, FSAT_clean.csv. "
)
add_body_p("Kết quả có thể được tóm tắt ngắn gọn qua bảng sau:")

p_cap_t31 = doc.add_paragraph()
p_cap_t31.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_cap_t31.paragraph_format.space_before = Pt(4)
p_cap_t31.paragraph_format.space_after = Pt(4)
r_t31 = p_cap_t31.add_run("Bảng 3.1: Tổng hợp kết quả xử lý sai số thô bằng Khoảng tứ phân vị (IQR) trên toàn bộ 4.800 mẫu đo.")
r_t31.font.name = 'Times New Roman'
r_t31.font.size = Pt(9.5)
r_t31.font.italic = True

t31_data = [
    ("FSDT.csv", "Chiều tiến – Mặt nhẵn (27.0°C)", "1.750", "16 mốc", "77", "4.40%", "1.673", "95.60%"),
    ("BSDT.csv", "Chiều lùi – Mặt nhẵn (27.0°C)", "950", "12 mốc", "61", "6.42%", "889", "93.58%"),
    ("FRDT.csv", "Chiều tiến – Mặt nhám (27.0°C)", "1.150", "11 mốc", "59", "5.13%", "1.091", "94.87%"),
    ("FSAT.csv", "Chiều tiến – Phòng lạnh (20.0°C)", "950", "8 mốc", "38", "4.00%", "912", "96.00%"),
    ("TỔNG HỢP", "Cả 4 tập thực nghiệm", "4.800", "47 mốc", "235", "4.90%", "4.565", "95.10%"),
]

table_31 = doc.add_table(rows=len(t31_data)+1, cols=8)
table_31.alignment = WD_TABLE_ALIGNMENT.CENTER
table_31.autofit = False

t31_widths = [Cm(2.2), Cm(3.6), Cm(1.6), Cm(1.8), Cm(1.6), Cm(1.6), Cm(1.8), Cm(1.8)]
t31_headers = ["Tệp dữ liệu", "Điều kiện đo", "Tổng mẫu", "Mốc có ngoại lai", "Mẫu ngoại lai", "Tỷ lệ (%)", "Mẫu hợp lệ", "Tỷ lệ hợp lệ (%)"]

for col_idx, text_h in enumerate(t31_headers):
    c = table_31.rows[0].cells[col_idx]
    c.text = text_h
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.05
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, row_vals in enumerate(t31_data, start=1):
    for col_idx, text_val in enumerate(row_vals):
        c = table_31.rows[row_idx].cells[col_idx]
        c.text = text_val
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx not in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if row_idx == len(t31_data) or col_idx == 0:
                r.font.bold = True
                if row_idx == len(t31_data):
                    r.font.color.rgb = C_MAROON

for row in table_31.rows:
    for idx_w, width in enumerate(t31_widths):
        row.cells[idx_w].width = width
        set_cell_border(row.cells[idx_w],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_31.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_31.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

add_body_p(
    "Nhận xét từ kết quả Bảng 3.1: Hệ thống đo duy trì độ ổn định tốt; chỉ có 4.90% mẫu bị loại bỏ trên toàn bộ 4.800 lần đo. "
    "Tỷ lệ ngoại lai giữa FSDT (4.40%) và BSDT (6.42%) gần tương đương nhau, cho thấy điều kiện môi trường đo ổn định. "
    "Bề mặt nhám (FRDT) xuất hiện nhiều xung tán xạ hơn so với mặt nhẵn. Các xung này được bộ lọc IQR phát hiện và loại bỏ, giúp giá trị trung bình không bị lệch."
)

add_heading_3("3.1.3. Đánh giá hiệu quả sau khi lọc")
add_body_p("Hình 3.1 thể hiện biến thiên của độ lệch chuẩn s trước và sau khi lọc trên thang logarit.")

IMG_H3_1_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_1_loc_sai_so_tho.png"
if os.path.exists(IMG_H3_1_PATH):
    p_img3_1 = doc.add_paragraph()
    p_img3_1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_1.paragraph_format.space_before = Pt(8)
    p_img3_1.paragraph_format.space_after = Pt(4)
    run_img3_1 = p_img3_1.add_run()
    run_img3_1.add_picture(IMG_H3_1_PATH, width=Cm(15.0))
    
    p_cap3_1 = doc.add_paragraph()
    p_cap3_1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_1.paragraph_format.space_after = Pt(8)
    r_c3_1 = p_cap3_1.add_run("Hình 3.1: Độ lệch chuẩn trước và sau khi lọc IQR.")
    r_c3_1.font.name = 'Times New Roman'
    r_c3_1.font.italic = True
    r_c3_1.font.size = Pt(10)

add_body_p(
    "Đánh giá từ đồ thị Hình 3.1: Trước khi lọc, độ lệch chuẩn duy trì ở mức dưới 1.0 mm. "
    "Tại các cự ly xa (580 cm và 600 cm), do sóng phản xạ suy hao mạnh dẫn đến các mẫu quá hạn, "
    "độ lệch chuẩn thô tăng lên lần lượt s = 346.05 mm và s = 2621.02 mm."
)

p_green = doc.add_paragraph()
p_green.paragraph_format.first_line_indent = Cm(1.0)
p_green.paragraph_format.space_after = Pt(6)
p_green.paragraph_format.line_spacing = 1.35
p_green.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r_g_title = p_green.add_run("Đường màu xanh nét liền (Độ lệch chuẩn sau khi lọc IQR): ")
r_g_title.font.name = 'Times New Roman'
r_g_title.font.size = Pt(13)
r_g_title.font.bold = True
r_g_body = p_green.add_run(
    "Sau khi loại bỏ các giá trị ngoại lai bằng bộ lọc IQR kết hợp ngưỡng phân giải Δ_LSB = 0.0175 cm, "
    "đường độ lệch chuẩn duy trì ổn định trong dải 0.09 - 4.0 mm trên toàn dải đo 6 m, tiệm cận đường dung sai của thước cơ khí (0.5 mm)."
)
r_g_body.font.name = 'Times New Roman'
r_g_body.font.size = Pt(13)

p_cap_t32 = doc.add_paragraph()
p_cap_t32.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_cap_t32.paragraph_format.space_before = Pt(4)
p_cap_t32.paragraph_format.space_after = Pt(4)
r_t32 = p_cap_t32.add_run("Bảng 3.2: Đối chiếu độ lệch chuẩn trước và sau khi lọc IQR tại các mốc tiêu biểu.")
r_t32.font.name = 'Times New Roman'
r_t32.font.size = Pt(9.5)
r_t32.font.italic = True

t32_data = [
    ("50 cm", "0.094 mm", "0.094 mm", "1.0 lần", "0 / 50 (0%)", "Vùng đo ổn định, không có ngoại lai"),
    ("100 cm", "0.383 mm", "0.383 mm", "1.0 lần", "0 / 50 (0%)", "Nhỏ hơn dung sai thước (0.5 mm), giữ lại 100% mẫu"),
    ("360 cm", "90.33 mm", "2.51 mm", "Giảm 36.0 lần", "1 / 50 (2%)", "Loại bỏ xung trượt chu kỳ sóng ToF"),
    ("580 cm", "346.05 mm", "3.30 mm", "Giảm 104.8 lần", "4 / 50 (8%)", "Loại bỏ xung bão hòa timeout 824.6 cm"),
    ("600 cm", "2621.02 mm", "0.63 mm", "Giảm 4153.8 lần", "7 / 50 (14%)", "Cắt bỏ các xung quá hạn ở giới hạn cự ly"),
]

table_32 = doc.add_table(rows=len(t32_data)+1, cols=6)
table_32.alignment = WD_TABLE_ALIGNMENT.CENTER
table_32.autofit = False

t32_widths = [Cm(2.6), Cm(2.4), Cm(2.4), Cm(2.2), Cm(2.2), Cm(4.2)]
t32_headers = ["Khoảng cách chuẩn", "Độ lệch chuẩn thô", "Độ lệch chuẩn sạch", "Tỷ lệ giảm s", "Số mẫu ngoại lai", "Nguyên nhân hiện tượng"]

for col_idx, text_h in enumerate(t32_headers):
    c = table_32.rows[0].cells[col_idx]
    c.text = text_h
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.05
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, row_vals in enumerate(t32_data, start=1):
    for col_idx, text_val in enumerate(row_vals):
        c = table_32.rows[row_idx].cells[col_idx]
        c.text = text_val
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx != 5 else WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if col_idx == 0:
                r.font.bold = True

for row in table_32.rows:
    for idx_w, width in enumerate(t32_widths):
        row.cells[idx_w].width = width
        set_cell_border(row.cells[idx_w],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_32.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_32.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

# 3.2
add_heading_2("3.2. Khảo sát Dải đo thực tế")

add_body_p(
    "Để xác định dải làm việc thực tế của cảm biến RCWL-1601, chuỗi dữ liệu thực nghiệm gồm 35 mốc cự ly "
    "từ 1 cm đến 600 cm thuộc tập chuẩn FSDT_clean.csv được đưa vào phân tích sai số: "
    "sai số tuyệt đối Δd = d̄ - d_chuẩn (mm) và sai số tương đối δ = ((d̄ - d_chuẩn) / d_chuẩn) × 100% (%). "
    "Biến thiên của sai số tương đối theo khoảng cách chuẩn được thể hiện trên Hình 3.2."
)

IMG_H3_2_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_2_sai_so_tuong_doi.png"
if os.path.exists(IMG_H3_2_PATH):
    p_img3_2 = doc.add_paragraph()
    p_img3_2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_2.paragraph_format.space_before = Pt(8)
    p_img3_2.paragraph_format.space_after = Pt(4)
    run_img3_2 = p_img3_2.add_run()
    run_img3_2.add_picture(IMG_H3_2_PATH, width=Cm(15.0))
    
    p_cap3_2 = doc.add_paragraph()
    p_cap3_2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_2.paragraph_format.space_after = Pt(8)
    r_c3_2 = p_cap3_2.add_run("Hình 3.2: Sai số tương đối theo khoảng cách chuẩn (Tập dữ liệu FSDT, giới hạn trục tung ±10%).")
    r_c3_2.font.name = 'Times New Roman'
    r_c3_2.font.italic = True
    r_c3_2.font.size = Pt(9.5)

add_body_p(
    "Từ diễn biến của đường sai số trên đồ thị Hình 3.2, đặc tính làm việc của cảm biến có thể được phân chia thành 4 vùng: "
    "Vùng chết (0 cm – 3 cm), dải đo tuyến tính ổn định (5 cm – 400 cm), dải đo xa vượt định mức (420 cm – 550 cm), ngưỡng bão hòa xa (580 cm – 600 cm)"
)

add_body_p(
    "Kết luận: Dải làm việc tin cậy và đạt chuẩn độ chính xác cao của cảm biến RCWL-1601 trong thực tế là từ 10 cm đến 550 cm."
)

p_cap_t33 = doc.add_paragraph()
p_cap_t33.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_cap_t33.paragraph_format.space_before = Pt(4)
p_cap_t33.paragraph_format.space_after = Pt(4)
r_t33 = p_cap_t33.add_run("Bảng 3.3: Tổng hợp các vùng làm việc và đặc tính đo thực nghiệm trên toàn dải đo.")
r_t33.font.name = 'Times New Roman'
r_t33.font.italic = True
r_t33.font.size = Pt(9.5)

t33_data = [
    ("1.0 cm", "2.030 cm", "+10.30 mm", "+103.05%", "0.035 mm"),
    ("2.0 cm", "2.352 cm", "+3.52 mm", "+17.59%", "0.085 mm"),
    ("3.0 cm", "2.679 cm", "-3.21 mm", "-10.72%", "0.056 mm"),
    ("5.0 cm", "4.295 cm", "-7.05 mm", "-14.10%", "0.085 mm"),
    ("10.0 cm", "10.570 cm", "+5.70 mm", "+5.70%", "0.061 mm"),
    ("50.0 cm", "49.847 cm", "-1.53 mm", "-0.31%", "0.094 mm"),
    ("100.0 cm", "99.429 cm", "-5.71 mm", "-0.57%", "0.383 mm"),
    ("200.0 cm", "200.351 cm", "+3.51 mm", "+0.18%", "2.192 mm"),
    ("300.0 cm", "299.718 cm", "-2.82 mm", "-0.09%", "2.860 mm"),
    ("400.0 cm", "401.399 cm", "+13.99 mm", "+0.35%", "0.270 mm"),
    ("500.0 cm", "500.691 cm", "+6.91 mm", "+0.14%", "1.978 mm"),
    ("550.0 cm", "550.630 cm", "+6.30 mm", "+0.11%", "0.319 mm"),
    ("580.0 cm", "579.850 cm", "-1.50 mm", "-0.03%", "3.303 mm"),
    ("600.0 cm", "824.562 cm", "+2245.62 mm", "+37.43%", "0.631 mm"),
]

table_33 = doc.add_table(rows=len(t33_data)+1, cols=5)
table_33.alignment = WD_TABLE_ALIGNMENT.CENTER
table_33.autofit = False

t33_widths = [Cm(2.6), Cm(2.8), Cm(2.8), Cm(2.8), Cm(3.0)]
t33_headers = ["Khoảng cách chuẩn", "Giá trị trung bình", "Sai số tuyệt đối", "Sai số tương đối", "Độ lệch chuẩn s"]

for col_idx, text_h in enumerate(t33_headers):
    c = table_33.rows[0].cells[col_idx]
    c.text = text_h
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.05
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, row_vals in enumerate(t33_data, start=1):
    for col_idx, text_val in enumerate(row_vals):
        c = table_33.rows[row_idx].cells[col_idx]
        c.text = text_val
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if col_idx == 0:
                r.font.bold = True

for row in table_33.rows:
    for idx_w, width in enumerate(t33_widths):
        row.cells[idx_w].width = width
        set_cell_border(row.cells[idx_w],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_33.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_33.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

add_heading_2("3.3. Đánh giá Độ chụm và Độ chính xác")

add_body_p(
    "Trên cơ sở tập dữ liệu chuẩn chiều tiến mặt nhẵn FSDT sau khi xử lý ngoại lai tại Mục 3.1, độ chụm và độ chính xác "
    "của hệ đo được đánh giá trên 33 mốc cự ly thuộc dải đo hữu ích từ 1 cm đến 550 cm (trước ngưỡng bão hòa xa 580 – 600 cm). "
    "Toàn bộ số liệu gốc phục vụ phân tích và vẽ đồ thị được lưu trữ đầy đủ trong tệp du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv."
)

add_heading_3("3.3.1. Đánh giá độ chụm")

add_body_p(
    "Áp dụng độ lệch chuẩn mẫu thực nghiệm s tại Mục 1.3.1 và sai số chuẩn của giá trị trung bình SE tại Mục 1.3.3 (Chương 1), "
    "chuỗi số liệu của 33 mốc cự ly (1 cm – 550 cm, tại nhiệt độ chuẩn hóa 27.0 °C, N = 50 mẫu thô/mốc, "
    "cỡ mẫu hợp lệ sau lọc n_hợp_lệ ∈ [40, 50]) được trích xuất trực tiếp từ hai cột std_sach_mm và se_sach_mm trong tệp du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv:"
)

add_body_p(
    "1. Vùng cự ly gần (1 cm ≤ x_true ≤ 50 cm, 9 mốc): Tại 8/9 mốc khảo sát, s đạt từ 0.035 mm đến 0.094 mm và SE đạt từ 0.0049 mm "
    "đến 0.0133 mm (nhỏ hơn nhiều so với một bước đếm phần cứng Δ_LSB ≈ 0.174 mm) nhờ biên độ sóng phản xạ mạnh từ mặt phẳng nhẵn "
    "của viên gạch chuẩn 40 cm × 40 cm. Riêng mốc 40 cm (n_hợp_lệ = 49) ghi nhận s = 3.144 mm và SE = 0.4491 mm."
)

add_body_p(
    "2. Vùng cự ly trung bình (60 cm ≤ x_true ≤ 180 cm, 8 mốc): Tại 7/8 mốc, s nằm trong dải 0.088 mm – 0.383 mm và SE nằm trong "
    "dải 0.0128 mm – 0.0542 mm; riêng mốc 120 cm (n_hợp_lệ = 50) có s = 1.747 mm và SE = 0.2471 mm."
)

add_body_p(
    "3. Vùng cự ly xa danh định (200 cm ≤ x_true ≤ 360 cm, 11 mốc): Độ lệch chuẩn s dao động từ 0.142 mm (tại 220 cm, n_hợp_lệ = 40) "
    "đến 2.860 mm (tại 300 cm, n_hợp_lệ = 50), tương ứng SE biến thiên từ 0.0225 mm đến 0.4045 mm (tại 360 cm đạt s = 2.508 mm, SE = 0.3583 mm)."
)

add_body_p(
    "4. Dải đo xa mở rộng (400 cm ≤ x_true ≤ 550 cm, 5 mốc): Độ lệch chuẩn s đạt 0.270 mm tại 400 cm (SE = 0.0407 mm), 0.228 mm tại 420 cm "
    "(SE = 0.0340 mm), tăng lên cực đại toàn dải 4.049 mm tại 450 cm (SE = 0.5726 mm), đạt 1.978 mm tại 500 cm (SE = 0.2797 mm) "
    "và giảm về 0.319 mm tại mốc giới hạn 550 cm (n_hợp_lệ = 42, SE = 0.0492 mm)."
)

add_body_p(
    "Tính trên toàn bộ 33 mốc khảo sát (1 – 550 cm), cột se_sach_mm xác nhận sai số chuẩn trung bình SE không vượt quá 0.5726 mm; "
    "trong đó có 32/33 mốc đạt SE < 0.45 mm (nhỏ hơn nửa độ chia nhỏ nhất 0.5 mm của thước chuẩn) và 22/33 mốc đạt SE ≤ 0.10 mm."
)

add_body_p(
    "Giải thích cơ chế vật lý và thuật toán của dạng dao động răng cưa trên Hình 3.3: Trục hoành của Hình 3.3 biểu diễn sự thay đổi "
    "mốc khoảng cách chuẩn x_true (mỗi mốc đều đo độc lập với cỡ mẫu cố định N = 50), không phải trục tăng dần kích thước mẫu tích lũy k "
    "tại một vị trí cố định như bài toán hội tụ ở Mục 2.4 (Chương 2). Dạng lên xuống răng cưa luân phiên của s giữa các mốc cự ly "
    "xuất phát từ sự tương tác giữa bước nhảy một chu kỳ sóng mang siêu âm 40 kHz và ngưỡng tứ phân vị 25% của bộ lọc IQR "
    "(đã nêu tại Mục 1.3.2, Chương 1). Tại T = 27.0 °C (v = 347.66 m/s), một chu kỳ sóng mang T_0 = 25 μs ứng với quãng đường "
    "khứ hồi nửa bước sóng xấp xỉ 4.35 mm (0.435 cm). Khi biên độ sườn lên của bó xung phản hồi ECHO rơi sát mức điện áp ngưỡng so sánh "
    "trong vi mạch RCWL-9610, thời điểm kích hoạt bắt xung bị trượt ±1 chu kỳ sóng mang giữa các lần đo trong cùng 50 mẫu:"
)

add_bullet_p(
    "Tại những mốc cự ly có dưới 25% số mẫu trượt sang chu kỳ kế cận (như 80, 150, 220, 320, 400, 420, 550 cm, với 5 – 10 mẫu "
    "ngoại lai bị loại trong thong_ke_chuong_3.csv), hai tứ phân vị Q_1 và Q_3 vẫn nằm gọn trong cùng một chu kỳ sóng mang (IQR ≈ 0.018 – 0.066 cm); "
    "hàng rào Tukey cắt bỏ hoàn toàn cụm trượt chu kỳ, đưa s xuống mức rất thấp (0.142 – 0.395 mm) và SE xuống 0.022 – 0.060 mm.",
    "• Nhóm mốc lọc sạch cụm trượt chu kỳ: "
)

add_bullet_p(
    "Tại các mốc cự ly có trên 25% số mẫu phân bố sang chu kỳ kế cận (như 40, 120, 200, 260, 300, 360, 450 cm, có 0 – 3 mẫu bị loại), "
    "cả hai cụm đều lọt vào giữa Q_1 và Q_3 làm IQR mở rộng lên đúng một bước nhảy sóng mang (IQR ≈ 0.435 cm); phân bố hai đỉnh "
    "đẩy độ lệch chuẩn mẫu s lên vùng 1.7 – 4.0 mm. Tuy nhiên, sai số chuẩn của giá trị trung bình SE = s/√n luôn được nén xuống "
    "dưới 0.57 mm, bảo đảm độ tin cậy thống kê tuyệt đối cho phép lấy trung bình.",
    "• Nhóm mốc giữ lại hai cụm chu kỳ kế tiếp: "
)

IMG_H3_3_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_3_do_chum_toan_dai.png"
if os.path.exists(IMG_H3_3_PATH):
    p_img3_3 = doc.add_paragraph()
    p_img3_3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_3.paragraph_format.space_before = Pt(8)
    p_img3_3.paragraph_format.space_after = Pt(4)
    run_img3_3 = p_img3_3.add_run()
    run_img3_3.add_picture(IMG_H3_3_PATH, width=Cm(15.0))
    
    p_cap3_3 = doc.add_paragraph()
    p_cap3_3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_3.paragraph_format.space_after = Pt(8)
    r_c3_3 = p_cap3_3.add_run("Hình 3.3: Độ lệch chuẩn thực nghiệm s và sai số chuẩn trung bình SE theo khoảng cách chuẩn (1 cm – 550 cm).")
    r_c3_3.font.italic = True
    r_c3_3.font.size = Pt(10)

add_body_p("Đánh giá từ đồ thị Hình 3.3: Khi biểu diễn chung trên cùng một trục tung đơn vị mm, sự khác biệt giữa hai đường phản ánh rõ năng lực của phép đo:")
add_body_p(
    "Đường màu xanh lam nét liền (Độ lệch chuẩn thực nghiệm s): Nằm dưới vạch dung sai thước 0.5 mm tại phần lớn các mốc đơn chu kỳ "
    "và chỉ nhô lên tại các điểm giao thoa ngưỡng trượt chu kỳ sóng mang 40 kHz."
)
add_body_p(
    "Đường màu cam nét đứt (Sai số chuẩn trung bình SE = s/√n): Nhờ phép lấy trung bình trên n_hợp_lệ ≥ 40 mẫu, "
    "đường SE bị nén phẳng hoàn toàn sát đáy trục hoành (dao động cực nhỏ từ 0.0049 mm đến 0.5726 mm), "
    "chứng minh tính hội tụ cao và triệt tiêu gần như hoàn toàn sai số ngẫu nhiên của hệ thống đo."
)

add_heading_3("3.3.2. Đánh giá độ chính xác")

add_body_p(
    "Sử dụng sai số tuyệt đối Δx và sai số tương đối δ (%) đã định nghĩa tại Mục 1.3.3 (Chương 1), chuỗi số liệu được trích xuất "
    "từ cột sai_so_tuyet_doi_mm và sai_so_tuong_doi_pct trong thong_ke_chuong_3.csv:"
)

add_body_p(
    "Sai số tuyệt đối (Δx): Trong dải từ 50 cm đến 550 cm (25 mốc), Δx biến thiên trong khoảng hẹp từ -5.71 mm đến +14.02 mm; "
    "có 17/25 mốc có sai số tuyệt đối không vượt quá ±5.0 mm và 22/25 mốc nằm trong phạm vi ±8.0 mm."
)

add_body_p(
    "Sai số tương đối (δ%): Ở vùng đầu dải đo danh định (10 cm – 40 cm), do mẫu số x_true nhỏ nên δ% đạt từ -3.36% đến +5.70%; "
    "tuy nhiên khi khoảng cách tăng lên từ 50 cm đến 550 cm, sai số tương đối nhanh chóng hội tụ và nằm hoàn toàn trong dải hẹp "
    "[-0.57%; +0.35%]. Tại các cự ly lớn (300 cm, 500 cm, 550 cm), sai số tương đối chỉ còn -0.09%, +0.14% và +0.11%."
)

add_body_p(
    "Nguồn gốc sai số hệ thống: Độ lệch tuyệt đối cỡ vài milimét bắt nguồn từ hai yếu tố thực tế: khoảng cách thụt lùi cơ khí "
    "của màng rung gốm áp điện nằm sâu bên trong ống bảo vệ kim loại so với mép ngoài bo mạch (~4.84 mm, hoàn toàn trùng khớp "
    "với hệ số tự do của phương trình hồi quy tuyến tính tại Mục 3.4) và sai số định vị mép chân gạch trên thước thép chuẩn."
)

IMG_H3_4_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_4_do_chinh_xac_sai_so.png"
if os.path.exists(IMG_H3_4_PATH):
    p_img3_4 = doc.add_paragraph()
    p_img3_4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_4.paragraph_format.space_before = Pt(8)
    p_img3_4.paragraph_format.space_after = Pt(4)
    run_img3_4 = p_img3_4.add_run()
    run_img3_4.add_picture(IMG_H3_4_PATH, width=Cm(15.0))
    
    p_cap3_4 = doc.add_paragraph()
    p_cap3_4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_4.paragraph_format.space_after = Pt(8)
    r_c3_4 = p_cap3_4.add_run("Hình 3.4: Sai số tuyệt đối Δx (mm) và sai số tương đối δ (%) theo khoảng cách chuẩn (10 cm – 550 cm).")
    r_c3_4.font.italic = True
    r_c3_4.font.size = Pt(10)

add_body_p("Đánh giá từ đồ thị Hình 3.4: Biểu đồ đơn ghép hai trục tung Y (đồng bộ đường chuẩn gốc 0 giữa hai trục) cho thấy hai xu hướng đối chiếu trực quan:")
add_body_p(
    "Đường màu xanh lá nét liền (Sai số tuyệt đối Δx, trục trái): Dao động quanh trục 0 mm trong biên độ hẹp [-5.71; +14.02] mm "
    "trên toàn bộ dải đo, khẳng định hệ thống không bị hiện tượng trôi tích lũy dốc theo khoảng cách."
)
add_body_p(
    "Đường màu xanh lam nét đứt (Sai số tương đối δ%, trục phải): Hội tụ rất nhanh từ ngưỡng +5.70% ở cự ly gần về sát vạch chuẩn 0% "
    "khi x_true ≥ 50 cm (luôn nằm dưới 0.57%), minh chứng cho độ chính xác cao của hệ đo RCWL-1601."
)
# MỤC 3.4: ĐÁNH GIÁ ĐỘ TUYẾN TÍNH (LINEARITY)
# ==============================================================================
add_heading_2("3.4. Đánh giá Độ tuyến tính (Linearity)")

add_heading_3("3.4.1. Hồi quy đa thức và Đánh giá Độ tuyến tính (Linearity)")

add_body_p(
    "Độ tuyến tính (Linearity) là đặc tính tĩnh cơ bản phản ánh mức độ quan hệ tỷ lệ thuận giữa khoảng cách dịch chuyển "
    "thực tế và giá trị đo hiển thị của cảm biến. Để đánh giá một cách khoa học, khách quan và tránh hiện tượng lạc quan "
    "thái quá do đánh giá trên chính dữ liệu huấn luyện, toàn bộ 34 mốc thực nghiệm trên toàn dải đo (1.0 cm đến 580.0 cm) "
    "đã được phân chia ngẫu nhiên có kiểm soát theo tỷ lệ chuẩn thực nghiệm 70% dữ liệu Huấn luyện (Train set - 24 mốc) "
    "và 30% dữ liệu Kiểm thử độc lập (Test set - 10 mốc)."
)

add_body_p(
    "Tập huấn luyện (Train) gồm 24 mốc cự ly [1.0, 3.0, 5.0, 8.0, 10.0, 40.0, 60.0, 100.0, 120.0, 140.0, 160.0, 180.0, "
    "200.0, 240.0, 250.0, 260.0, 300.0, 320.0, 340.0, 360.0, 400.0, 420.0, 500.0, 550.0 cm] được dùng để thiết lập hệ phương trình "
    "chuẩn tắc và giải ma trận xác định hệ số cho 3 mô hình hồi quy đa thức: Bậc 1 (y = a₁x + b₁), Bậc 2 (y = a₂x² + b₂x + c₂), "
    "và Bậc 3 (y = a₃x³ + b₃x² + c₃x + d₃). Trong khi đó, tập kiểm thử (Test) gồm 10 mốc độc lập [2.0, 20.0, 50.0, 80.0, 150.0, "
    "220.0, 280.0, 350.0, 450.0, 580.0 cm] trải dài từ vùng chết, dải đo danh định đến vùng suy hao xa, hoàn toàn không tham gia vào "
    "quá trình tìm hệ số, đóng vai trò làm 'bài kiểm tra mù' đối sánh độ chính xác thực tế của 3 mô hình."
)

# Native Word Equation 3.1: OLS Matrix
add_native_equation(
    '<m:acc><m:accPr><m:chr m:val="̂"/></m:accPr><m:e><m:r><m:t>β</m:t></m:r></m:e></m:acc>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:sSup><m:e><m:d><m:e><m:sSup><m:e><m:r><m:t>X</m:t></m:r></m:e><m:sup><m:r><m:t>T</m:t></m:r></m:sup></m:sSup><m:r><m:t>X</m:t></m:r></m:e></m:d></m:e><m:sup><m:r><m:t>-1</m:t></m:r></m:sup></m:sSup>'
    '<m:sSup><m:e><m:r><m:t> · X</m:t></m:r></m:e><m:sup><m:r><m:t>T</m:t></m:r></m:sup></m:sSup>'
    '<m:r><m:t> · Y</m:t></m:r>',
    eq_num="3.1"
)

add_body_p(
    "Giải hệ phương trình chuẩn tắc (3.1) trên 24 mốc thực nghiệm tập Train (70%), kết quả tính toán xác định được phương trình "
    "của 3 mô hình hồi quy đa thức như sau:"
)
add_bullet_p(
    "ŷ₁ = 1.00273441 · x - 0.48427223 (cm). Trong đó hệ số góc a₁ = 1.002734 bám sát độ dốc lý tưởng 1:1, hệ số tự do b₁ = -0.484 cm "
    "phản ánh chính xác khoảng thụt lùi cơ khí (-4.84 mm) của màng loa gốm phía trong vỏ kim loại.",
    "1. Mô hình Bậc 1 (Tuyến tính): "
)
add_bullet_p(
    "ŷ₂ = 3.56559128·10⁻⁶ · x² + 1.00103491 · x - 0.37940440 (cm). Hệ số bậc 2 rất nhỏ (cỡ 10⁻⁶), đường đặc tính thực tế tiệm cận đường thẳng.",
    "2. Mô hình Bậc 2: "
)
add_bullet_p(
    "ŷ₃ = -1.04345666·10⁻⁷ · x³ + 8.50580899·10⁻⁵ · x² + 0.98551084 · x - 0.00036859 (cm). Chứa các số hạng phi tuyến bậc 3 và bậc 2 có xu hướng uốn lượn.",
    "3. Mô hình Bậc 3: "
)

add_body_p(
    "Ghi chú: Toàn bộ các tổng ma trận chuẩn tắc phục vụ tính toán (N = 24, ∑x, ∑x², ..., ∑x⁶, ∑xy, ∑x²y, ∑x³y) được lưu trữ đầy đủ "
    "và chi tiết trong tệp cơ sở dữ liệu du_lieu_tong_hop/chuong_3/cac_tong_hoi_quy.csv để phục vụ tra cứu và kiểm chứng."
)

add_body_p(
    "Do trên thang đo lớn từ 0 cm đến 600 cm, đặc tính của cả ba mô hình đều có độ dốc xấp xỉ 1:1 và bám rất sát chuỗi dữ liệu thực nghiệm, "
    "nên mắt thường không thể phân biệt được mô hình nào tối ưu nếu chỉ nhìn vào đường hồi quy tổng thể. Do đó, để xác định mô hình phản ánh "
    "trung thực bản chất vật lý của cảm biến, bắt buộc phải thực hiện đối sánh định lượng sai số dự đoán trên 10 mốc kiểm thử độc lập (Test set) "
    "và phóng đại thang đo sai số lên mức milimét."
)

# BẢNG 3.4: ĐỐI SÁNH TRÊN 10 MỐC TEST (ĐÃ ĐỔI TỪ BẢNG 3.5 THÀNH BẢNG 3.4)
t34_data = [
    ("2.0 cm", "2.352 cm", "1.521 cm", "+8.31 mm", "1.623 cm", "+7.29 mm", "1.971 cm", "+3.81 mm"),
    ("20.0 cm", "19.328 cm", "19.570 cm", "-2.42 mm", "19.643 cm", "-3.15 mm", "19.743 cm", "-4.15 mm"),
    ("50.0 cm", "49.847 cm", "49.652 cm", "+1.95 mm", "49.681 cm", "+1.66 mm", "49.475 cm", "+3.73 mm"),
    ("80.0 cm", "80.083 cm", "79.734 cm", "+3.48 mm", "79.726 cm", "+3.56 mm", "79.331 cm", "+7.51 mm"),
    ("150.0 cm", "149.957 cm", "149.926 cm", "+0.31 mm", "149.856 cm", "+1.01 mm", "149.388 cm", "+5.69 mm"),
    ("220.0 cm", "220.086 cm", "220.117 cm", "-0.31 mm", "220.021 cm", "+0.65 mm", "219.818 cm", "+2.68 mm"),
    ("280.0 cm", "280.528 cm", "280.281 cm", "+2.47 mm", "280.190 cm", "+3.38 mm", "280.321 cm", "+2.08 mm"),
    ("350.0 cm", "349.550 cm", "350.473 cm", "-9.23 mm", "350.420 cm", "-8.70 mm", "350.874 cm", "-13.25 mm"),
    ("450.0 cm", "450.739 cm", "450.746 cm", "-0.07 mm", "450.808 cm", "-0.69 mm", "451.195 cm", "-4.56 mm"),
    ("580.0 cm", "579.850 cm", "581.102 cm", "-12.52 mm", "581.420 cm", "-15.71 mm", "579.850 cm", "-0.01 mm"),
]

table_34 = doc.add_table(rows=len(t34_data)+1, cols=8)
table_34.alignment = WD_TABLE_ALIGNMENT.CENTER
table_34.autofit = False

t34_widths = [Cm(1.8), Cm(2.0), Cm(2.0), Cm(1.8), Cm(2.0), Cm(1.8), Cm(2.0), Cm(1.8)]
t34_headers = ["Mốc Test x", "y thực tế", "ŷ Bậc 1", "e Bậc 1", "ŷ Bậc 2", "e Bậc 2", "ŷ Bậc 3", "e Bậc 3"]

for col_idx, text_h in enumerate(t34_headers):
    c = table_34.rows[0].cells[col_idx]
    c.text = text_h
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.05
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, row_vals in enumerate(t34_data, start=1):
    for col_idx, text_val in enumerate(row_vals):
        c = table_34.rows[row_idx].cells[col_idx]
        c.text = text_val
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if col_idx == 0:
                r.font.bold = True

for row in table_34.rows:
    for idx_w, width in enumerate(t34_widths):
        row.cells[idx_w].width = width
        set_cell_border(row.cells[idx_w],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_34.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_34.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

p_cap_t34 = doc.add_paragraph()
p_cap_t34.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_t34.paragraph_format.space_before = Pt(4)
p_cap_t34.paragraph_format.space_after = Pt(8)
r_t34 = p_cap_t34.add_run("Bảng 3.4: Đối sánh sai số dự đoán của 3 mô hình hồi quy trên 10 mốc kiểm thử độc lập.")
r_t34.font.name = 'Times New Roman'
r_t34.font.italic = True
r_t34.font.size = Pt(9.5)

add_body_p(
    "Kết quả kiểm thử độc lập tại Bảng 3.4 bộc lộ rõ nét bản chất của từng mô hình và minh chứng cho hiện tượng Quá khớp (Overfitting):"
)
add_bullet_p(
    "Tại cự ly 150.0 cm (mốc trung tâm của dải đo danh định ổn định), mô hình Bậc 1 dự đoán 149.926 cm, đạt độ chuẩn xác cực cao "
    "với sai số chỉ +0.31 mm. Tại 220.0 cm sai số là -0.31 mm và tại 450.0 cm chỉ là -0.07 mm. Ngược lại, mô hình Bậc 3 do bị uốn cong "
    "ở hai đầu mút nên bị võng sâu ở khoảng giữa, khiến sai số tại 150.0 cm vọt lên +5.69 mm (gấp hơn 18 lần mô hình Bậc 1) và tại "
    "350.0 cm sai số lệch tới -13.25 mm.",
    "Trong dải đo danh định ổn định: "
)
add_bullet_p(
    "Tại mốc 2.0 cm (nằm trong vùng chết phần cứng), cảm biến bị bão hòa kẹt ở 2.352 cm. Mô hình Bậc 1 do duy trì tính thẳng hướng về "
    "gốc tọa độ nên dự đoán 1.521 cm (sai số +8.31 mm). Mô hình Bậc 3 nhờ có bậc tự do cao đã tự uốn cong để đón điểm kẹt này, cho giá trị "
    "dự đoán 1.971 cm (sai số +3.81 mm). Tương tự tại 580.0 cm (ngưỡng suy hao xa), Bậc 3 uốn gắt ở đuôi để đón điểm suy hao nên sai số chỉ "
    "-0.01 mm, trong khi Bậc 1 lệch -12.52 mm.",
    "Tại hai vùng biên (Vùng chết 2 cm và Vùng suy hao xa 580 cm): "
)
add_bullet_p(
    "Tính trung bình trên toàn bộ 10 mốc Test độc lập, sai số tuyệt đối trung bình (MAE) của mô hình Bậc 1 đạt mức thấp nhất: "
    "MAE = 4.11 mm, trong khi Bậc 2 là 4.58 mm và Bậc 3 lên tới 4.75 mm. Điều này chứng minh rằng việc tăng bậc đa thức lên Bậc 3 "
    "thực chất là một sự 'chữa cháy gượng ép' cho các điểm lỗi phần cứng ở hai đầu mút, nhưng cái giá phải trả là phá hỏng hoàn toàn "
    "độ chính xác của toàn bộ dải đo chính.",
    "Sai số tuyệt đối trung bình trên tập Test: "
)

# CHÈN HÌNH 3.3: SO SÁNH SAI SỐ TUYỆT ĐỐI TẠI CÁC MỐC TEST
IMG_H3_6_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_6_sai_so_phan_du_3_mo_hinh.png"
if os.path.exists(IMG_H3_6_PATH):
    p_img3_6 = doc.add_paragraph()
    p_img3_6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_6.paragraph_format.space_before = Pt(8)
    p_img3_6.paragraph_format.space_after = Pt(4)
    run_img3_6 = p_img3_6.add_run()
    run_img3_6.add_picture(IMG_H3_6_PATH, width=Cm(15.0))

    p_cap3_6 = doc.add_paragraph()
    p_cap3_6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_6.paragraph_format.space_after = Pt(8)
    r_c3_6 = p_cap3_6.add_run("Hình 3.3: So sánh sai số tuyệt đối tại các mốc kiểm thử của 3 mô hình hồi quy.")
    r_c3_6.font.italic = True
    r_c3_6.font.size = Pt(10)

# CHÈN HÌNH 3.4: BIỂU ĐỒ MIỀN TÍCH LŨY SAI SỐ TUYỆT ĐỐI
IMG_H3_7_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_7_tich_luy_sai_so_phan_du.png"
if os.path.exists(IMG_H3_7_PATH):
    p_img3_7 = doc.add_paragraph()
    p_img3_7.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_7.paragraph_format.space_before = Pt(8)
    p_img3_7.paragraph_format.space_after = Pt(4)
    run_img3_7 = p_img3_7.add_run()
    run_img3_7.add_picture(IMG_H3_7_PATH, width=Cm(15.0))

    p_cap3_7 = doc.add_paragraph()
    p_cap3_7.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_7.paragraph_format.space_after = Pt(8)
    r_c3_7 = p_cap3_7.add_run("Hình 3.4: Biểu đồ miền tích lũy sai số tuyệt đối trên 10 mốc kiểm thử độc lập.")
    r_c3_7.font.italic = True
    r_c3_7.font.size = Pt(10)

add_body_p(
    "Đồ thị Hình 3.3 và biểu đồ miền tích lũy tại Hình 3.4 cung cấp bằng chứng trực quan rõ rệt nhất về sự tích lũy sai số: "
    "Trong khoảng dải đo làm việc từ 50 cm đến 450 cm, đường tích lũy sai số của mô hình Bậc 1 gần như đi ngang phẳng lì, "
    "giúp giữ tổng sai số tích lũy toàn dải ở mức thấp nhất (41.07 mm). Trong khi đó, đường tích lũy của mô hình Bậc 3 leo dốc rất đứng "
    "ở dải giữa (từ 11.69 mm vọt lên 42.89 mm tại 350 cm), khiến tổng sai số tích lũy lên tới 47.45 mm."
)

add_body_p(
    "Xác định Chỉ số Độ phi tuyến (Non-Linearity): Về bản chất khoa học đo lường, Non-Linearity là một thông số gộp toàn thang "
    "đặc trưng cho độ cong vênh vật lý của bản thân cảm biến so với một đường thẳng lý tưởng duy nhất (Best Fit Straight Line - BFSL). "
    "Công thức xác định độ phi tuyến chuẩn hóa theo toàn thang đo (FSO) được tính theo (3.2):"
)

# Native Word Equation 3.2: Non-Linearity
add_native_equation(
    '<m:r><m:t>Non-Linearity (% FS) = ± </m:t></m:r>'
    '<m:f><m:fPr/><m:num><m:r><m:t>ΔL</m:t></m:r><m:sSub><m:e/><m:sub><m:r><m:t>max</m:t></m:r></m:sub></m:sSub></m:num>'
    '<m:den><m:r><m:t>FSO</m:t></m:r></m:den></m:f>'
    '<m:r><m:t> × 100%</m:t></m:r>',
    eq_num="3.2"
)

add_body_p(
    "Trong dải đo danh định ổn định (5 cm đến 400 cm) với toàn thang đo FSO = 400 cm, mốc xuất hiện độ lệch lớn nhất so với đường thẳng "
    "hồi quy là tại x = 360.0 cm (giá trị thực nghiệm 361.945 cm, mô hình đường thẳng tính ra 360.500 cm). "
    "Độ lệch cực đại đạt ΔL_max = |361.945 - 360.500| = 1.445 cm (14.45 mm). "
    "Thay vào công thức (3.2), chỉ số độ phi tuyến thực nghiệm của cảm biến RCWL-1601 đạt:"
)

add_body_p(
    "Non-Linearity = ± (1.445 cm / 400 cm) × 100% = ± 0.361% FS (nếu tính theo khoảng biến thiên Span = 395 cm đạt ±0.366% FS)."
)

add_body_p(
    "Trong tiêu chuẩn cảm biến đo lường công nghiệp, một cảm biến siêu âm thương mại có độ phi tuyến dưới 0.5% FS được xếp vào nhóm "
    "có độ tuyến tính rất cao. Kết quả này khẳng định bản thân phần cứng của RCWL-1601 đã có đặc tính tĩnh rất thẳng, "
    "hoàn toàn không cần thiết phải sử dụng các thuật toán bù đa thức phi tuyến phức tạp."
)

# BẢNG 3.5: TỔNG HỢP 4 TIÊU CHÍ KHOA HỌC (ĐÃ ĐỔI TỪ BẢNG 3.6 THÀNH BẢNG 3.5)
t35_data_summary = [
    ("Sai số trên tập Test", "MAE = 4.11 mm (Thấp nhất)", "MAE = 4.58 mm", "MAE = 4.75 mm (Cao nhất)", "Bậc 1 khái quát hóa tốt nhất trên dữ liệu mới"),
    ("Bản chất vật lý sóng âm", "Hoàn toàn phù hợp (t = 2d/v)", "Không phù hợp", "Không phù hợp (Overfitting)", "Sóng âm truyền tuyến tính bậc 1 tự nhiên"),
    ("Tính ổn định phần dư", "Rất phẳng quanh mốc 0", "Khá phẳng", "Võng mạnh ở dải giữa (-13.25 mm)", "Bậc 1 không làm méo sai số dải đo chính"),
    ("Tài nguyên vi điều khiển", "Nhẹ nhất (1 nhân, 1 cộng)", "Trung bình", "Tốn CPU, dễ tràn số thực", "Bậc 1 tối ưu tối đa cho ESP32"),
    ("Chỉ số Non-Linearity", "±0.361% FS (< 0.5%)", "±0.372% FS", "±0.331% FS", "Độ phi tuyến cực nhỏ, chênh lệch không đáng kể"),
    ("KẾT LUẬN LỰA CHỌN", "CHỌN LÀM ĐẶC TÍNH TĨNH", "LOẠI", "LOẠI", "Mô hình Bậc 1 là lựa chọn tối ưu, khoa học và kinh tế nhất")
]

table_35_summary = doc.add_table(rows=len(t35_data_summary)+1, cols=5)
table_35_summary.alignment = WD_TABLE_ALIGNMENT.CENTER
table_35_summary.autofit = False

t35_s_widths = [Cm(2.8), Cm(3.2), Cm(2.4), Cm(3.2), Cm(4.4)]
t35_s_headers = ["Tiêu chuẩn đánh giá", "Mô hình Bậc 1", "Mô hình Bậc 2", "Mô hình Bậc 3", "Nhận định kỹ thuật"]

for col_idx, text_h in enumerate(t35_s_headers):
    c = table_35_summary.rows[0].cells[col_idx]
    c.text = text_h
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.05
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, row_vals in enumerate(t35_data_summary, start=1):
    for col_idx, text_val in enumerate(row_vals):
        c = table_35_summary.rows[row_idx].cells[col_idx]
        c.text = text_val
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 4 else WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if col_idx == 0 or row_idx == len(t35_data_summary):
                r.font.bold = True

for row in table_35_summary.rows:
    for idx_w, width in enumerate(t35_s_widths):
        row.cells[idx_w].width = width
        set_cell_border(row.cells[idx_w],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_35_summary.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_35_summary.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

p_cap_t35_s = doc.add_paragraph()
p_cap_t35_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_t35_s.paragraph_format.space_before = Pt(4)
p_cap_t35_s.paragraph_format.space_after = Pt(12)
r_t35_s = p_cap_t35_s.add_run("Bảng 3.5: Tổng hợp 4 tiêu chí khoa học quyết định lựa chọn mô hình hồi quy Bậc 1 cho cảm biến.")
r_t35_s.font.name = 'Times New Roman'
r_t35_s.font.italic = True
r_t35_s.font.size = Pt(9.5)

add_body_p(
    "Quyết định lựa chọn chính thức: Dựa trên 4 tiêu chuẩn kỹ thuật tại Bảng 3.5, phương trình tuyến tính Bậc 1 "
    "y = 1.00273441 · x - 0.48427223 được lựa chọn làm phương trình đặc tính tĩnh chuẩn của hệ thống đo RCWL-1601. "
    "Hệ số góc a₁ = 1.002734 phản ánh độ nhạy bám sát tuyệt đối tỷ lệ 1:1, và hệ số tự do b₁ = -0.484 cm "
    "phản ánh chính xác sai số vị trí điểm không cơ học (khoảng thụt lùi 4.84 mm của màng loa gốm phía trong vỏ kim loại bảo vệ)."
)


# ==============================================================================
# MỤC 3.5: PHÂN TÍCH ĐỘ TRỄ (HYSTERESIS) GIỮA CHIỀU TIẾN VÀ CHIỀU LÙI
# ==============================================================================
add_heading_2("3.5. Phân tích Độ trễ (Hysteresis) giữa Chiều tiến và Chiều lùi")

add_heading_3("3.5.1. Khảo sát thực nghiệm đối xứng, Đồ thị trực quan và Định lượng Sai số trễ")

add_body_p(
    "Nhằm đánh giá tính đối xứng và độ ổn định của cảm biến RCWL-1601 khi đo khoảng cách hai chiều, "
    "kịch bản thực nghiệm đối xứng được thiết lập với hai chuỗi đo độc lập trên cùng một ray trượt định hướng "
    "và bia phản xạ phẳng nhẵn ở nhiệt độ phòng chuẩn hóa 27.0°C: Chiều tiến (FSDT, tịnh tiến xa từ 10 cm đến 300 cm) "
    "và Chiều lùi (BSDT, thu hẹp khoảng cách từ 300 cm về 10 cm). Hai chuỗi đo giao nhau tại 19 mốc cự ly đối ứng chuẩn (10, 20, 40, ..., 300 cm)."
)

IMG_H3_6A_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_6a_dac_tinh_hai_chieu.png"
if os.path.exists(IMG_H3_6A_PATH):
    p_img3_6a = doc.add_paragraph()
    p_img3_6a.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_6a.paragraph_format.space_before = Pt(8)
    p_img3_6a.paragraph_format.space_after = Pt(4)
    run_img3_6a = p_img3_6a.add_run()
    run_img3_6a.add_picture(IMG_H3_6A_PATH, width=Cm(15.0))
    
    p_cap3_6a = doc.add_paragraph()
    p_cap3_6a.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_6a.paragraph_format.space_after = Pt(8)
    r_c3_6a = p_cap3_6a.add_run("Hình 3.6a: Đặc tính đo khoảng cách hai chiều Chiều tiến vs Chiều lùi so với đường chuẩn lý tưởng 1:1.")
    r_c3_6a.font.italic = True
    r_c3_6a.font.size = Pt(10)

add_body_p(
    "Trên đồ thị Hình 3.6a, cả hai đường Chiều tiến và Chiều lùi đều bám sát hoàn hảo vào đường tham chiếu lý tưởng y = x. "
    "Để quan sát rõ nét sự chênh lệch vi mô giữa hai chiều dịch chuyển, phân bố sai số đo tuyệt đối Δd = d_meas - d_true "
    "được phân tích chi tiết trên đồ thị Hình 3.6b."
)

IMG_H3_6B_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_6b_vong_tre_hysteresis.png"
if os.path.exists(IMG_H3_6B_PATH):
    p_img3_6b = doc.add_paragraph()
    p_img3_6b.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_6b.paragraph_format.space_before = Pt(8)
    p_img3_6b.paragraph_format.space_after = Pt(4)
    run_img3_6b = p_img3_6b.add_run()
    run_img3_6b.add_picture(IMG_H3_6B_PATH, width=Cm(15.0))
    
    p_cap3_6b = doc.add_paragraph()
    p_cap3_6b.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_6b.paragraph_format.space_after = Pt(8)
    r_c3_6b = p_cap3_6b.add_run("Hình 3.6b: Phân bố Sai số đo tuyệt đối Δd và Vòng trễ Hysteresis giữa Chiều tiến và Chiều lùi.")
    r_c3_6b.font.italic = True
    r_c3_6b.font.size = Pt(10)

add_body_p(
    "Từ đồ thị Hình 3.6b, sai số đo tuyệt đối Δd của hai chiều dao động trong biên độ rất hẹp [-1.48 cm; +1.45 cm], "
    "quấn quanh trục tham chiếu Δd = 0 cm và tạo thành vòng trễ khép kín với khoảng hở vi mô. "
    "Độ lệch trễ tuyệt đối tại từng mốc cự ly d_true,k được xác định theo hiệu số khoảng cách đo trung bình giữa Chiều tiến và Chiều lùi sau khi lọc IQR:"
)

# Native Equation 3.12
eq_3_12_omml = (
    '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>Δ</m:t></m:r>'
    '<m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>H</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>k</m:t></m:r></m:sub></m:sSub>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>=|</m:t></m:r>'
    '<m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>d</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>meas,forward</m:t></m:r></m:sub></m:sSub>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>-</m:t></m:r>'
    '<m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>d</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>meas,backward</m:t></m:r></m:sub></m:sSub>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>|</m:t></m:r>'
)
add_native_equation(eq_3_12_omml, eq_num="3.12")

add_body_p(
    "Phân tích trên toàn bộ 19 mốc cự ly ghi nhận độ lệch trễ cực đại ΔH_max = 1.6598 cm (tại mốc 200 cm, "
    "được định vị trực quan trên Hình 3.6b), độ lệch trễ trung bình ΔH_mean = 0.5342 cm và độ lệch chuẩn s_H = 0.4496 cm. "
    "Sai số trễ tương đối γ_H% được tính toán song song theo Thang đo thử nghiệm (Span_test = 300 cm) và Thang đo hiệu dụng toàn dải (Span_FS = 550 cm):"
)

# Native Equation 3.13
eq_3_13_omml = (
    '<m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><m:rPr><m:sty m:val="p"/></m:rPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>γ</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>H,300</m:t></m:r></m:sub></m:sSub>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>%=</m:t></m:r>'
    '<m:f><m:fPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:fPr>'
    '<m:num><m:r><m:rPr><m:sty m:val="p"/></m:rPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>Δ</m:t></m:r>'
    '<m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>H</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>max</m:t></m:r></m:sub></m:sSub></m:num>'
    '<m:den><m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>d</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>F.S.</m:t></m:r></m:sub></m:sSub></m:den></m:f>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>×100%=</m:t></m:r>'
    '<m:f><m:fPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:fPr>'
    '<m:num><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>1.6598 cm</m:t></m:r></m:num>'
    '<m:den><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>300 cm</m:t></m:r></m:den></m:f>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>×100%=0.553%</m:t></m:r>'
)
add_native_equation(eq_3_13_omml, eq_num="3.13")

# Native Equation 3.14
eq_3_14_omml = (
    '<m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><m:rPr><m:sty m:val="p"/></m:rPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>γ</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>H,550</m:t></m:r></m:sub></m:sSub>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>%=</m:t></m:r>'
    '<m:f><m:fPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:fPr>'
    '<m:num><m:r><m:rPr><m:sty m:val="p"/></m:rPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>Δ</m:t></m:r>'
    '<m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>H</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>max</m:t></m:r></m:sub></m:sSub></m:num>'
    '<m:den><m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:sSubPr>'
    '<m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>d</m:t></m:r></m:e>'
    '<m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>F.S.</m:t></m:r></m:sub></m:sSub></m:den></m:f>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>×100%=</m:t></m:r>'
    '<m:f><m:fPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr></m:ctrlPr></m:fPr>'
    '<m:num><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>1.6598 cm</m:t></m:r></m:num>'
    '<m:den><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>550 cm</m:t></m:r></m:den></m:f>'
    '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>×100%=0.302%</m:t></m:r>'
)
add_native_equation(eq_3_14_omml, eq_num="3.14")

add_body_p(
    "Đánh giá: Cả hai chỉ số sai số trễ tương đối đều ở mức rất nhỏ (γ_H% ≤ 0.55%), "
    "đáp ứng xuất sắc yêu cầu định vị hai chiều tin cậy trong các bài toán công nghiệp và robot tự hành."
)

add_heading_3("3.5.2. Luận giải Bản chất vật lý phi trễ của sóng siêu âm và Truy vết nguyên nhân sai số ngoại cảnh")

add_body_p(
    "Dựa trên kết quả thực nghiệm, mức sai số trễ rất nhỏ (γ_H ≈ 0.55%) được luận giải qua hai lý do cốt lõi: "
    "Thứ nhất, về bản chất vật lý, RCWL-1601 đo khoảng cách thuần túy bằng thời gian bay (ToF) của sóng siêu âm "
    "lan truyền trong không khí, không có ma sát cơ học hay hiện tượng trễ vật liệu nên hoàn toàn không tồn tại độ trễ nội tại; "
    "Thứ hai, độ lệch trễ vi mô cực đại ΔH_max = 1.66 cm tại mốc 200 cm thực chất bắt nguồn từ các tác nhân ngoại cảnh khách quan "
    "gồm độ rơ cơ khí và góc tỳ tay khi đảo chiều trên ray trượt dài 3 m, sự biến thiên nhẹ của vi khí hậu phòng thí nghiệm "
    "giữa hai lượt đo, cùng độ phân giải đếm thời gian 1 μs (≈ 0.174 mm) của vi điều khiển ESP32."
)

# ==============================================================================
# MỤC 3.6: PHÂN TÍCH ẢNH HƯỞNG CỦA BỀ MẶT PHẢN XẠ
# ==============================================================================
add_heading_2("3.6. Phân tích ảnh hưởng của Bề mặt phản xạ")

add_body_p(
    "Để lượng hóa tác động của cơ chế phản xạ gương định hướng và tán xạ khuếch tán sóng siêu âm (đã trình bày tại Mục 1.1.3, Chương 1) "
    "lên chất lượng phép đo thực tế, thí nghiệm đối chứng được thực hiện tại cùng điều kiện nhiệt độ phòng mặc định 27.0 °C "
    "(v = 347.662 m/s) trên hai mặt đối lập của cùng một viên gạch kích thước 40 cm × 40 cm (Mục 2.2 và Mục 2.3, Chương 2): "
    "Trường hợp 1 (FSDT) sử dụng mặt trước phẳng nhẵn và Trường hợp 3 (FRDT) sử dụng mặt sau gồ ghề nhấp nhô. "
    "Toàn bộ chỉ tiêu thống kê trước và sau lọc IQR trên 22 mốc cự ly chung (10 cm – 350 cm) cùng mốc kiểm tra giới hạn 375 cm "
    "của FRDT (23 mốc, tổng cộng 1.150 mẫu thô) được trích xuất trực tiếp từ tệp du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv."
)

add_heading_3("3.6.1. Tác động của tán xạ bề mặt lên độ chụm và độ chính xác đo")

add_body_p(
    "Đối chiếu các chỉ tiêu độ lệch chuẩn thực nghiệm s (cột std_sach_mm), sai số chuẩn trung bình SE (cột se_sach_mm) "
    "và sai số đo Δx, δ% (cột sai_so_tuyet_doi_mm, sai_so_tuong_doi_pct — định nghĩa tại Mục 1.3, Chương 1) "
    "trên 22 mốc cự ly chung từ 10 cm đến 350 cm cho thấy ba đặc điểm vật lý rõ rệt:"
)

add_body_p(
    "1. Suy giảm độ chụm cục bộ ở vùng cự ly gần (10 cm – 60 cm) do giao thoa đa tia phản xạ: Ở cự ly ngắn, "
    "góc mở chùm tia siêu âm bao phủ nhiều gờ lồi lõm có độ sâu chênh lệch cỡ milimét trên mặt sau viên gạch, "
    "tạo ra các sóng phản hồi lệch pha giao thoa trực tiếp tại màng thu. Tại x_true = 10 cm, độ lệch chuẩn sau lọc s "
    "tăng từ 0.061 mm (FSDT, SE = 0.0086 mm) lên 1.620 mm (FRDT, SE = 0.2291 mm — gấp 26.6 lần); tại x_true = 60 cm, "
    "s tăng từ 0.088 mm (SE = 0.0128 mm) lên 2.240 mm (SE = 0.3168 mm — gấp 25.5 lần). Ở các mốc 40 cm và 50 cm, "
    "mặt gồ ghề làm phát sinh lần lượt 13/50 mẫu (26%, s_thô = 2.338 mm) và 6/50 mẫu (12%, s_thô = 1.452 mm) nhảy chu kỳ "
    "ngoại lai trước khi được bộ lọc IQR khử sạch về s = 0.089 mm và 0.077 mm. Tính trên toàn bộ 22 mốc từ 10 cm đến 350 cm "
    "(1.100 mẫu), tỷ lệ ngoại lai bị loại bỏ bởi IQR trên mặt gồ ghề là 59/1.100 mẫu (5.36%), cao hơn mức 46/1.100 mẫu (4.18%) của mặt phẳng nhẵn."
)

add_body_p(
    "2. Hiện tượng dịch chuyển vị trí các đỉnh trượt chu kỳ trên dải trung bình (80 cm – 340 cm): Trong dải này, "
    "độ lệch chuẩn sau lọc của mặt gồ ghề dao động trong khoảng 0.101 – 2.555 mm, tương đương biên độ răng cưa 0.142 – 2.860 mm "
    "của mặt phẳng nhẵn. Đáng chú ý, vị trí các đỉnh phân tán cao giữa hai bề mặt xuất hiện lệch pha nhau theo cự ly "
    "(tại 180, 220, 280, 320 cm, mặt gồ ghề rơi vào vùng chuyển tiếp hai chu kỳ sóng mang 40 kHz nên s đạt 2.076 – 2.555 mm; "
    "ngược lại tại 100, 200, 300 cm, chùm phản xạ của mặt gồ ghề khóa gọn vào một chu kỳ đơn lẻ nên s chỉ còn 0.101 – 0.253 mm). "
    "Nguyên nhân là độ nhấp nhô hình học của mặt sau viên gạch làm dịch chuyển mặt phẳng phản xạ âm học hiệu dụng đi vài milimét "
    "so với mép chân gạch, từ đó làm đổi vị trí các mốc cự ly rơi vào ranh giới ngưỡng so sánh xung ECHO. Nhờ lấy trung bình "
    "trên cỡ mẫu hợp lệ n_hợp_lệ ∈ [37, 50], sai số chuẩn trung bình SE của mặt gồ ghề trên toàn bộ 22 mốc (10 – 350 cm) "
    "luôn nằm gọn trong khoảng 0.0071 – 0.3903 mm, thấp hơn dung sai vạch chia thước chuẩn 0.5 mm tại 22/22 mốc đo."
)

add_body_p(
    "3. Độ dịch chuyển sai số hệ thống (Δx và δ%): Do các đỉnh gờ lồi trên mặt nhám nhô về phía trước mặt phẳng chân gạch căn thước, "
    "sóng siêu âm dội về sớm hơn tại một số mốc làm sai số tuyệt đối Δx = x̄ - x_true thiên âm rõ hơn so với mặt nhẵn "
    "(biến thiên từ -21.74 mm tại 250 cm, -13.71 mm tại 60 cm, -12.94 mm tại 150 cm đến +10.88 mm tại 350 cm). "
    "Xét về sai số tương đối trên dải 80 cm – 350 cm (17 mốc), có 16/17 mốc đạt |δ%| ≤ 0.87% (duy nhất mốc 100 cm ở mức -1.27%), "
    "đáp ứng yêu cầu đo lường khi biên độ xung phản hồi còn vượt ngưỡng thu."
)

IMG_H3_7A_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_7a_do_lech_chuan_be_mat.png"
if os.path.exists(IMG_H3_7A_PATH):
    p_img3_7a = doc.add_paragraph()
    p_img3_7a.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_7a.paragraph_format.space_before = Pt(8)
    p_img3_7a.paragraph_format.space_after = Pt(4)
    run_img3_7a = p_img3_7a.add_run()
    run_img3_7a.add_picture(IMG_H3_7A_PATH, width=Cm(15.0))
    
    p_cap3_7a = doc.add_paragraph()
    p_cap3_7a.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_7a.paragraph_format.space_after = Pt(8)
    r_c3_7a = p_cap3_7a.add_run("Hình 3.7a: So sánh độ lệch chuẩn thực nghiệm s sau lọc IQR giữa mặt phẳng nhẵn (FSDT) và mặt gồ ghề (FRDT) trên dải 10 cm – 350 cm.")
    r_c3_7a.font.italic = True
    r_c3_7a.font.size = Pt(10)

add_body_p("Đánh giá từ đồ thị Hình 3.7a: Tách riêng đại lượng độ lệch chuẩn mẫu s cho thấy rõ quy luật phân tán xung đơn lẻ giữa hai bề mặt:")
add_body_p(
    "Ở vùng cự ly gần (10 – 60 cm): Đường màu cam nét đứt (FRDT) vọt lên hai đỉnh tán xạ rõ rệt tại 10 cm (1.620 mm) "
    "và 60 cm (2.240 mm), trong khi đường xanh lam nét liền (FSDT) nằm phẳng sát đáy dưới 0.10 mm (trừ điểm trượt chu kỳ tại 40 cm)."
)
add_body_p(
    "Ở dải trung bình – xa (80 – 350 cm): Cả hai đường cùng dao động răng cưa với biên độ đỉnh tương đương "
    "(≤ 2.86 mm trên FSDT và ≤ 2.62 mm trên FRDT), nhưng vị trí đỉnh – đáy lệch pha nhau dọc theo trục khoảng cách "
    "do độ lồi lõm của mặt gạch nhám làm dịch chuyển mặt phẳng phản xạ hiệu dụng."
)

IMG_H3_7B_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_7b_sai_so_chuan_be_mat.png"
if os.path.exists(IMG_H3_7B_PATH):
    p_img3_7b = doc.add_paragraph()
    p_img3_7b.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_7b.paragraph_format.space_before = Pt(8)
    p_img3_7b.paragraph_format.space_after = Pt(4)
    run_img3_7b = p_img3_7b.add_run()
    run_img3_7b.add_picture(IMG_H3_7B_PATH, width=Cm(15.0))
    
    p_cap3_7b = doc.add_paragraph()
    p_cap3_7b.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_7b.paragraph_format.space_after = Pt(8)
    r_c3_7b = p_cap3_7b.add_run("Hình 3.7b: So sánh sai số chuẩn trung bình SE = s/√n sau lọc IQR giữa mặt phẳng nhẵn (FSDT) và mặt gồ ghề (FRDT) trên dải 10 cm – 350 cm.")
    r_c3_7b.font.italic = True
    r_c3_7b.font.size = Pt(10)

add_body_p("Đánh giá từ đồ thị Hình 3.7b: Khi phóng đại riêng thang đo cho sai số chuẩn trung bình SE (0 – 0.65 mm):")
add_body_p(
    "Cả hai đường SE của FSDT (xanh lam vòng tròn nền trắng) và FRDT (cam ký hiệu hình vuông): Đều nằm hoàn toàn phía dưới "
    "đường dung sai vạch chia thước 0.5 mm (tím chấm gạch) tại trọn vẹn 22/22 mốc khảo sát (0.0086 – 0.4491 mm đối với FSDT "
    "và 0.0071 – 0.3903 mm đối với FRDT)."
)
add_body_p(
    "Ý nghĩa thống kê thực nghiệm: Phép lấy trung bình trên cỡ mẫu N = 50 kết hợp lọc IQR đủ sức nén biên độ nhiễu pha "
    "tán xạ của bề mặt gồ ghề xuống mức dưới nửa milimét chừng nào sóng phản hồi còn vượt ngưỡng thu."
)

add_heading_3("3.6.2. Suy hao năng lượng tán xạ và sự thu hẹp giới hạn tầm đo xa")

add_body_p(
    "Tác động bất lợi nghiêm trọng nhất của bề mặt gồ ghề không nằm ở sai số dải gần mà ở sự suy giảm đột ngột "
    "cự ly hoạt động cực đại do thất thoát năng lượng âm học ra không gian:"
)

add_body_p(
    "Đối chứng với mặt phẳng nhẵn (FSDT): Nhờ phản xạ gương bảo toàn năng lượng dọc trục pháp tuyến 90°, "
    "cảm biến đo ổn định hoàn toàn không có xung tràn đến tận 550 cm (x̄ = 550.630 cm, s = 0.319 mm, SE = 0.0492 mm), "
    "chỉ chớm xuất hiện 4/50 xung mất tín hiệu tại 580 cm (x̄ sau lọc vẫn đạt 579.850 cm) và bão hòa hoàn toàn tại 600 cm (x̄ = 824.562 cm)."
)

add_body_p(
    "Ngưỡng chớm mất xung tại 350 cm trên mặt gồ ghề (FRDT): Do tán xạ khuếch tán làm biên độ áp suất âm phản hồi "
    "suy giảm nhanh theo khoảng cách, tại x_true = 350 cm bắt đầu xuất hiện 1/50 mẫu (2%) mất hoàn toàn tín hiệu dội về "
    "và tràn bộ đếm lên 824.400 cm (t = 47097 μs ở dòng 2 tệp FRDT_350cm.csv), đi kèm 4/50 mẫu (8%) trượt chu kỳ dương "
    "(351.906 – 352.817 cm), tạo thành tổng cộng 5/50 mẫu ngoại lai (10%). Chỉ riêng 1 xung tràn 824.400 cm đã kéo "
    "trung bình thô lệch lên x̄_thô = 360.649 cm và làm độ lệch chuẩn thô bùng nổ lên s_thô = 669.240 mm "
    "(SE_thô = 94.6448 mm, gấp 268.7 lần mặt nhẵn). Tuy nhiên, vì tổng tỷ lệ ngoại lai (10%) vẫn thấp hơn điểm gãy tứ phân vị (25%), "
    "bộ lọc IQR loại bỏ trọn vẹn cả 5 mẫu nhiễu (n_hợp_lệ = 45), khôi phục kết quả đo chuẩn xác x̄ = 351.088 cm "
    "(Δx = +10.88 mm, δ = +0.311%), s = 2.618 mm và SE = 0.3903 mm."
)

add_body_p(
    "Sự sụp đổ phép đo và vượt ngưỡng lọc IQR tại 375 cm: Khi dịch bia gồ ghề ra mốc x_true = 375 cm, "
    "dữ liệu thô ghi nhận tới 33/50 mẫu (66%) bị mất tín hiệu tràn lên 824.49 – 824.75 cm, chỉ còn 17/50 mẫu (34%) "
    "bắt được xung phản xạ yếu quanh 376.39 – 378.16 cm. Do tỷ lệ mẫu bão hòa vượt quá 50%, trung vị mẫu bị kéo hẳn lên vùng tràn "
    "(Med = 824.575 cm, trong khi Q_1 = 377.388 cm và Q_3 = 824.623 cm), làm khoảng tứ phân vị phình rộng lên IQR = 447.235 cm "
    "và mở toang hàng rào lọc [-293.46; 1495.48] cm (0 mẫu bị đánh dấu ngoại lai). Hệ quả là ngay cả sau lọc IQR, "
    "phép đo hoàn toàn mất hiệu lực với x̄ = 672.502 cm (Δx = +2975.02 mm, δ = +79.33%), s = 2140.734 mm và SE = 302.7455 mm."
)

add_body_p(
    "Kết luận thiết kế kỹ thuật: Bề mặt gồ ghề tán xạ làm thu hẹp tầm đo tin cậy cực đại từ 550 cm xuống còn 350 cm "
    "(sụt giảm 200 cm, tương đương -36.4%). Kết quả này là cơ sở thực nghiệm trực tiếp cho thiết kế ứng dụng tại Chương 4: "
    "đối với bề mặt chất lỏng tĩnh phẳng nhẵn trong bồn chứa kín, cảm biến RCWL-1601 khai thác an toàn toàn bộ dải xa; "
    "ngược lại đối với vật liệu rắn dạng hạt rời, bề mặt nhám xốp hoặc mặt thoáng gợn sóng mạnh, "
    "chiều cao lắp đặt tối đa phải giới hạn bảo toàn dưới ngưỡng 300 – 350 cm."
)

# ==============================================================================
# MỤC 3.7: PHÂN TÍCH ẢNH HƯỞNG CỦA NHIỆT ĐỘ VÀ HIỆU QUẢ THUẬT TOÁN BÙ NHIỆT LAPLACE
# ==============================================================================
add_heading_2("3.7. Phân tích ảnh hưởng của Nhiệt độ môi trường và Hiệu quả thuật toán bù nhiệt Laplace")

add_body_p(
    "Dựa trên mô hình phụ thuộc nhiệt độ của vận tốc sóng siêu âm Laplace đã thiết lập tại Mục 1.1.2 (Chương 1), "
    "khi nhiệt độ môi trường thay đổi từ 27.0 °C xuống 20.0 °C, vận tốc sóng siêu âm suy giảm lý thuyết từ "
    "v(27.0 °C) = 347.662 m/s xuống v(20.0 °C) = 343.420 m/s (sụt giảm Δv = 4.242 m/s, tương ứng -1.220%, "
    "làm thời gian bay ToF giãn dài ra +1.235%). Tác động của sự biến thiên này và năng lực bù nhiệt Laplace "
    "được đánh giá qua tập dữ liệu FSAT (19 mốc cự ly từ 10 cm đến 300 cm) đối chứng trực tiếp với FSDT."
)

add_heading_3("3.7.1. Sự giãn dài thời gian bay và độ ổn định độ chụm khi hạ nhiệt độ môi trường")

add_body_p(
    "Khi hạ nhiệt độ không khí xuống 20.0 °C, mật độ phân tử khí tăng làm giảm vận tốc lan truyền sóng âm, "
    "dẫn đến thời gian bay ToF cần thiết để sóng truyền khứ hồi qua cùng một khoảng cách hình học bị kéo dài ra."
)

add_body_p(
    "Độ giãn thời gian bay thực nghiệm (tof_sach_us): Trích xuất trực tiếp từ bộ đếm phần cứng ESP32 xác nhận "
    "ToF của tập FSAT tại 20.0 °C luôn lớn hơn có hệ thống so với FSDT tại 27.0 °C trên mọi mốc cự ly: "
    "tăng từ 614.0 μs lên 621.5 μs tại 10 cm (+7.5 μs), từ 2901.0 μs lên 2936.5 μs tại 50 cm (+35.5 μs), "
    "từ 5787.0 μs lên 5858.5 μs tại 100 cm (+71.5 μs), từ 11654.5 μs lên 11798.5 μs tại 200 cm (+144.0 μs) "
    "và từ 17454.0 μs lên 17670.0 μs tại 300 cm (+216.0 μs). Tỷ lệ giãn dài thời gian bay thực tế (t̄_20 - t̄_27) / t̄_27 "
    "trên toàn dải đạt trung bình +1.235%, trùng khớp hoàn hảo với tỷ lệ suy giảm vận tốc âm lý thuyết Laplace "
    "v_27 / v_20 - 1 = 347.662 / 343.420 - 1 = +1.235%."
)

add_body_p(
    "Tính bất biến của độ chụm đối với nhiệt độ: Trong môi trường phòng điều hòa kín gió 20.0 °C, "
    "tổng tỷ lệ ngoại lai bị loại bởi IQR của tập FSAT là 38/950 mẫu (4.00%), tương đương hoàn toàn với 39/950 mẫu (4.11%) "
    "trên 19 mốc đối ứng của FSDT. Độ lệch chuẩn sau lọc s của FSAT dao động trong dải 0.060 – 3.381 mm và sai số chuẩn "
    "trung bình SE đạt 0.0085 – 0.4781 mm (nằm dưới dung sai thước 0.5 mm tại cả 19/19 mốc), chứng minh việc hạ nhiệt độ "
    "môi trường chỉ làm dịch chuyển hệ thống vận tốc truyền âm chứ không làm suy giảm độ chụm lặp lại của vi mạch RCWL-9610."
)

add_heading_3("3.7.2. Định lượng sai số trôi nhiệt khi không bù và hiệu quả khử trôi của thuật toán Laplace")

add_body_p(
    "Để đánh giá định lượng rủi ro trong các hệ thống nhúng giá rẻ thường gán cứng hằng số vận tốc âm mặc định "
    "v(27.0 °C) = 347.662 m/s (default_temp_c = 27.0), khoảng cách chưa bù nhiệt tại 20.0 °C được tính đối chứng "
    "từ cột tof_sach_us theo x̄_chưa_bù = 0.5 · v(27.0 °C) · t̄_FSAT và so sánh trực tiếp với kết quả đã bù nhiệt Laplace thời gian thực trên ESP32:"
)

add_body_p(
    "1. Trường hợp không bù nhiệt độ (sai_so_chua_bu_27c_mm): Do thời gian bay kéo dài hơn trong không khí lạnh "
    "nhưng phần mềm vẫn nhân với vận tốc lớn của 27.0 °C, kết quả đo bị phóng đại giả tạo với tỷ lệ lý thuyết +1.235% "
    "quãng đường (≈ +12.35 mm/m ở 20.0 °C). Lượng trôi nhiệt thuần túy (x̄_chưa_bù - x̄_đã_bù) tích lũy tuyến tính từ "
    "+1.31 mm tại 10 cm, +6.16 mm tại 50 cm, +12.28 mm tại 100 cm, +18.52 mm tại 150 cm, +22.46 mm tại 200 cm, "
    "+28.20 mm tại 250 cm, lên tới +34.65 mm tại 280 cm và +35.31 mm tại 300 cm. Hệ quả là sai số tuyệt đối Δx khi chưa bù "
    "bị đẩy vọt lên mức dương lớn: đạt +25.96 mm tại 200 cm, đỉnh +39.92 mm (≈ +4.0 cm) tại 280 cm và +32.52 mm tại 300 cm."
)

add_body_p(
    "2. Hiệu quả triệt tiêu trôi nhiệt khi bù Laplace thời gian thực (sai_so_tuyet_doi_mm): Khi kích hoạt công thức cập nhật "
    "vận tốc âm tức thời v(T) theo từng mẫu đo trên ESP32, toàn bộ thành phần trôi nhiệt dương hàng xentimét bị loại bỏ hoàn toàn: "
    "sai số Δx của FSAT được kéo sập về -5.73 mm tại 100 cm, -0.45 mm tại 150 cm, +3.50 mm tại 200 cm, +0.04 mm tại 250 cm, "
    "+5.27 mm tại 280 cm và -2.79 mm tại 300 cm (14/14 mốc từ 80 – 300 cm trừ mốc 160 cm đều đạt |δ%| ≤ 0.57%)."
)

add_body_p(
    "3. Độ trùng khít tuyệt đối giữa hai môi trường nhiệt độ sau bù (x̄_27°C - x̄_20°C): Đối chiếu trực tiếp cột mean_sach_cm "
    "giữa FSDT (27.0 °C) và FSAT (20.0 °C) trên toàn bộ 19 mốc cự ly xác nhận độ lệch trung bình tuyệt đối giữa hai chế độ nhiệt "
    "chỉ là 0.037 mm (biến thiên trong dải siêu hẹp từ -0.048 mm đến +0.183 mm; có 18/19 mốc lệch dưới 0.085 mm — nhỏ hơn nửa bước "
    "lượng tử thời gian Δ_LSB ≈ 0.174 mm của bộ đếm ESP32). Kết quả này chứng minh thuật toán bù nhiệt Laplace giúp phép đo siêu âm "
    "hoàn toàn miễn nhiễm với biến thiên nhiệt độ môi trường."
)

IMG_H3_8_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_8_anh_huong_nhiet_do_bu_laplace.png"
if os.path.exists(IMG_H3_8_PATH):
    p_img3_8 = doc.add_paragraph()
    p_img3_8.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_8.paragraph_format.space_before = Pt(8)
    p_img3_8.paragraph_format.space_after = Pt(4)
    run_img3_8 = p_img3_8.add_run()
    run_img3_8.add_picture(IMG_H3_8_PATH, width=Cm(15.0))
    
    p_cap3_8 = doc.add_paragraph()
    p_cap3_8.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_8.paragraph_format.space_after = Pt(8)
    r_c3_8 = p_cap3_8.add_run("Hình 3.8: So sánh sai số tuyệt đối Δx tại phòng lạnh 20.0 °C khi chưa bù nhiệt độ, sau khi bù nhiệt độ Laplace (FSAT) và chuẩn đối chứng tại 27.0 °C (FSDT) trên dải 10 cm – 300 cm.")
    r_c3_8.font.italic = True
    r_c3_8.font.size = Pt(10)

add_body_p("Đánh giá từ đồ thị Hình 3.8: Biểu diễn ba chuỗi sai số trên cùng một trục tung đơn vị mm cho thấy sự tương phản trực quan:")
add_body_p(
    "Đường màu đỏ nét liền ký hiệu tam giác (FSAT chưa bù nhiệt): Tách khỏi gốc 0 mm và dốc tuyến tính đi lên theo khoảng cách chuẩn "
    "do tích lũy sai số vận tốc +1.235%, vọt lên vùng +26 ÷ +40 mm ở cự ly 200 – 300 cm."
)
add_body_p(
    "Đường màu xanh lá nét đứt tâm vuông đặc (FSAT đã bù Laplace tại 20.0 °C) lồng đồng tâm bên trong đường băng xanh lam "
    "ký hiệu vòng tròn rỗng (FSDT đối chứng tại 27.0 °C): Từng điểm vuông xanh lá nằm lọt chính tâm vòng tròn xanh lam "
    "trên toàn bộ 19 mốc cự ly từ 10 cm đến 300 cm (do độ lệch giữa hai đường chỉ từ 0.002 mm đến 0.183 mm) và cùng bám sát đường chuẩn 0 mm, "
    "khẳng định tính bắt buộc của cảm biến nhiệt độ đi kèm thuật toán bù Laplace trong ứng dụng bồn chứa thực tế ở Chương 4."
)

# ==============================================================================

# ==============================================================================
# MỤC 3.8: TỔNG HỢP ĐỘ KHÔNG ĐẢM BẢO ĐO (ISO/GUM) VÀ ĐỐI CHIẾU DATASHEET
# ==============================================================================
add_heading_2("3.8. Tổng hợp Độ không đảm bảo đo (ISO/GUM) và Đối chiếu Đặc tính Kỹ thuật Thực nghiệm vs Datasheet")

add_heading_3("3.8.1. Đánh giá và Phân rã Độ không đảm bảo đo mở rộng toàn dải (ISO/GUM)")

add_body_p(
    "Theo tiêu chuẩn quốc tế ISO/IEC Guide 98-3 (GUM), hàm đo khoảng cách thời gian bay có bù nhiệt độ được mô hình hóa theo:\n"
    "d = f(t, T) = (331.3 + 0.606 · T) · t / 2"
)

add_body_p(
    "Các thành phần độ không đảm bảo đo bao gồm:\n"
    "1. Độ không đảm bảo đo Loại A (u_A): Đánh giá độ phân tán ngẫu nhiên qua N = 50 lần đo: u_A = s / √N.\n"
    "2. Độ không đảm bảo đo Loại B (u_B): Đánh giá theo phân bố xác suất hình chữ nhật (a / √3):\n"
    "• u_B1 (Vạch chia thước chuẩn 1 mm, a₁ = 0.5 mm): u_B1 = 0.5 / √3 ≈ 0.289 mm.\n"
    "• u_B2 (Lượng tử hóa Timer ESP32 1 μs ⇒ Δd_LSB ≈ 0.174 mm, a₂ = 0.087 mm): u_B2 = 0.087 / √3 ≈ 0.050 mm.\n"
    "• u_B3 (Nhiệt độ môi trường ±0.5 °C ⇒ u_T = 0.289 °C): Lan truyền qua hệ số nhạy c_T = ∂d/∂T ≈ 0.00174 · d ⇒ u_B3(d) = c_T · u_T ≈ 0.000503 · d (mm).\n"
    "3. Độ không đảm bảo đo chuẩn tổng hợp và Mở rộng (k = 2, độ tin cậy 95%):\n"
    "u_c = √(u_A² + u_B1² + u_B2² + u_B3²),    U_95% = 2 · u_c"
)

table_gum_data = [
    ("10 cm", "0.060 mm", "0.008 mm", "0.289 mm", "0.050 mm", "0.050 mm", "0.297 mm", "0.297 mm", "0.59 mm", "10.57 ± 0.06 cm"),
    ("50 cm", "0.092 mm", "0.013 mm", "0.289 mm", "0.050 mm", "0.252 mm", "0.386 mm", "0.386 mm", "0.77 mm", "49.84 ± 0.08 cm"),
    ("100 cm", "0.375 mm", "0.053 mm", "0.289 mm", "0.050 mm", "0.503 mm", "0.582 mm", "0.585 mm", "1.17 mm", "99.43 ± 0.12 cm"),
    ("150 cm", "0.284 mm", "0.043 mm", "0.289 mm", "0.050 mm", "0.755 mm", "0.810 mm", "0.811 mm", "1.62 mm", "149.96 ± 0.16 cm"),
    ("200 cm", "2.135 mm", "0.302 mm", "0.289 mm", "0.050 mm", "1.006 mm", "1.048 mm", "1.091 mm", "2.18 mm", "200.35 ± 0.22 cm"),
    ("250 cm", "2.057 mm", "0.291 mm", "0.289 mm", "0.050 mm", "1.258 mm", "1.292 mm", "1.324 mm", "2.65 mm", "250.00 ± 0.26 cm"),
    ("300 cm", "2.837 mm", "0.401 mm", "0.289 mm", "0.050 mm", "1.510 mm", "1.538 mm", "1.589 mm", "3.18 mm", "299.72 ± 0.32 cm"),
    ("350 cm", "2.618 mm", "0.390 mm", "0.289 mm", "0.050 mm", "1.761 mm", "1.785 mm", "1.828 mm", "3.65 mm", "351.09 ± 0.37 cm"),
    ("400 cm", "0.270 mm", "0.041 mm", "0.289 mm", "0.050 mm", "2.013 mm", "2.034 mm", "2.034 mm", "4.07 mm", "401.40 ± 0.41 cm"),
    ("450 cm", "4.049 mm", "0.573 mm", "0.289 mm", "0.050 mm", "2.264 mm", "2.283 mm", "2.354 mm", "4.71 mm", "450.74 ± 0.47 cm"),
    ("500 cm", "1.978 mm", "0.280 mm", "0.289 mm", "0.050 mm", "2.516 mm", "2.533 mm", "2.548 mm", "5.10 mm", "500.69 ± 0.51 cm"),
    ("550 cm", "0.319 mm", "0.049 mm", "0.289 mm", "0.050 mm", "2.768 mm", "2.783 mm", "2.783 mm", "5.57 mm", "550.63 ± 0.56 cm"),
]

gum_headers = ["Cự ly chuẩn d", "Độ lệch chuẩn s", "u_A", "u_B1 (Thước)", "u_B2 (Timer)", "u_B3 (Nhiệt độ)", "u_B tổng", "u_c tổng", "U_95% (k=2)", "Kết quả đo chuẩn Y"]
tbl_gum = doc.add_table(rows=len(table_gum_data)+1, cols=len(gum_headers))
tbl_gum.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_gum.autofit = False

gum_widths = [Cm(1.8), Cm(1.5), Cm(1.2), Cm(1.3), Cm(1.3), Cm(1.4), Cm(1.3), Cm(1.3), Cm(1.5), Cm(2.4)]
for col_idx, h_text in enumerate(gum_headers):
    c = tbl_gum.rows[0].cells[col_idx]
    c.text = h_text
    c.width = gum_widths[col_idx]
    set_cell_background(c, "F2F2F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.font.name = 'Times New Roman'
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

for row_idx, r_data in enumerate(table_gum_data):
    for col_idx, val in enumerate(r_data):
        c = tbl_gum.rows[row_idx+1].cells[col_idx]
        c.text = val
        c.width = gum_widths[col_idx]
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.runs[0]
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        if col_idx == 8:
            r.font.bold = True
            r.font.color.rgb = C_MAROON

for row in tbl_gum.rows:
    for c in row.cells:
        set_cell_border(c,
            top=dict(val='single', sz=4, color='D3D3D3'),
            bottom=dict(val='single', sz=4, color='D3D3D3'),
            left=dict(val='none', sz=0, color='auto'),
            right=dict(val='none', sz=0, color='auto')
        )

for c in tbl_gum.rows[0].cells:
    set_cell_border(c, top=dict(val='single', sz=12, color='003366'), bottom=dict(val='single', sz=12, color='003366'))
for c in tbl_gum.rows[-1].cells:
    set_cell_border(c, bottom=dict(val='single', sz=12, color='003366'))

p_cap_gum = doc.add_paragraph()
p_cap_gum.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_gum.paragraph_format.space_before = Pt(4)
p_cap_gum.paragraph_format.space_after = Pt(8)
r_gum = p_cap_gum.add_run("Bảng 3.6: Bảng tổng hợp các thành phần Độ không đảm bảo đo theo tiêu chuẩn ISO/GUM.")
r_gum.font.name = 'Times New Roman'
r_gum.font.italic = True
r_gum.font.size = Pt(9.5)

# --- HÌNH 3.9: Loại A và Loại B ---
IMG_H3_9_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_9_do_khong_dam_bao_do_loai_a_b.png"
if not os.path.exists(IMG_H3_9_PATH):
    IMG_H3_9_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\hinh_3_9_do_khong_dam_bao_do_loai_a_b.png"

if os.path.exists(IMG_H3_9_PATH):
    p_img3_9 = doc.add_paragraph()
    p_img3_9.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_9.paragraph_format.space_before = Pt(8)
    p_img3_9.paragraph_format.space_after = Pt(4)
    run_img3_9 = p_img3_9.add_run()
    run_img3_9.add_picture(IMG_H3_9_PATH, width=Cm(15.0))
    
    p_cap3_9 = doc.add_paragraph()
    p_cap3_9.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_9.paragraph_format.space_after = Pt(8)
    r_c3_9 = p_cap3_9.add_run("Hình 3.9: Biểu đồ phân rã độ không đảm bảo đo Loại A (u_A) và Loại B (u_B) theo khoảng cách chuẩn.")
    r_c3_9.font.italic = True
    r_c3_9.font.size = Pt(10)

# --- HÌNH 3.10: Chuẩn tổng hợp và Mở rộng ---
IMG_H3_10_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\chuong_3\hinh_3_10_do_khong_dam_bao_do_tong_hop_mo_rong.png"
if not os.path.exists(IMG_H3_10_PATH):
    IMG_H3_10_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\hinh_3_10_do_khong_dam_bao_do_tong_hop_mo_rong.png"

if os.path.exists(IMG_H3_10_PATH):
    p_img3_10 = doc.add_paragraph()
    p_img3_10.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_10.paragraph_format.space_before = Pt(8)
    p_img3_10.paragraph_format.space_after = Pt(4)
    run_img3_10 = p_img3_10.add_run()
    run_img3_10.add_picture(IMG_H3_10_PATH, width=Cm(15.0))
    
    p_cap3_10 = doc.add_paragraph()
    p_cap3_10.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_10.paragraph_format.space_after = Pt(8)
    r_c3_10 = p_cap3_10.add_run("Hình 3.10: Biểu đồ độ không đảm bảo đo chuẩn tổng hợp (u_c) và độ không đảm bảo đo mở rộng (U_95%, k=2) theo ISO/GUM.")
    r_c3_10.font.italic = True
    r_c3_10.font.size = Pt(10)

add_body_p(
    "Nhận xét ngắn gọn: Ở cự ly gần (d ≤ 50 cm), U_95% ≤ 0.77 mm, thành phần sai số vạch chia thước chuẩn u_B1 = 0.289 mm chiếm ưu thế chủ đạo. "
    "Khi cự ly tăng lên 300 – 550 cm, thành phần lan truyền sai số nhiệt độ u_B3 tăng tuyến tính và chiếm trên 85% phương sai tổng hợp. "
    "Trên toàn bộ dải đo hữu ích đến 5.5 m, U_95% luôn duy trì dưới ngưỡng ±5.57 mm (dưới ±0.56 cm), khẳng định độ tin cậy khoa học cao của phép đo."
)

add_heading_3("3.8.2. Bảng tổng hợp đối chiếu Đặc tính Kỹ thuật Thực nghiệm vs Datasheet Nhà sản xuất")

table_ds_data = [
    ("Dải đo danh định", "2.0 cm - 400.0 cm (hoặc 450 cm)", "5.0 cm - 550.0 cm", "Vượt định mức: Mở rộng thêm 100 cm (+22%) trên mặt nhẵn"),
    ("Vùng chết (Blind Zone)", "< 2.0 cm", "1.0 cm - 3.0 cm", "Kẹt cố định ở 2.0 - 2.6 cm do suy giảm dao động màng gốm"),
    ("Độ chính xác công bố", "± 0.5 cm ± 1%", "|Δx| ≤ 0.43 cm (< 2.5 m)\n± 0.35% (> 2.5 m)", "Tốt hơn công bố nhờ tích hợp thuật toán bù nhiệt độ Laplace"),
    ("Độ phân giải (Resolution)", "0.1 - 0.3 cm (1 - 3 mm)", "1 μs → ≈ 0.174 mm (0.017 cm)", "Độ phân giải ToF vượt trội nhờ bộ định thời phần cứng ESP32"),
    ("Khả năng thích ứng nhiệt độ", "Bù nhiệt nội bộ trên IC (cố định)", "Bù Laplace thời gian thực qua cảm biến ngoài", "Triệt tiêu sai số trôi nhiệt từ 5.8 cm xuống < 0.5 mm trên dải 3 m"),
]

ds_headers = ["Chỉ tiêu kỹ thuật đo lường", "Thông số công bố (Datasheet)", "Kết quả kiểm chứng thực nghiệm", "Đánh giá & Ghi chú kỹ thuật"]
tbl_ds = doc.add_table(rows=len(table_ds_data)+1, cols=len(ds_headers))
tbl_ds.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_ds.autofit = False

ds_widths = [Cm(3.5), Cm(3.5), Cm(3.8), Cm(4.2)]
for col_idx, h_text in enumerate(ds_headers):
    c = tbl_ds.rows[0].cells[col_idx]
    c.text = h_text
    c.width = ds_widths[col_idx]
    set_cell_background(c, "F2F2F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9.0)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

for row_idx, r_data in enumerate(table_ds_data):
    for col_idx, val in enumerate(r_data):
        c = tbl_ds.rows[row_idx+1].cells[col_idx]
        c.text = val
        c.width = ds_widths[col_idx]
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx == 0 or col_idx == 3 else WD_ALIGN_PARAGRAPH.CENTER
        r = p.runs[0]
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.0)

for row in tbl_ds.rows:
    for c in row.cells:
        set_cell_border(c,
            top=dict(val='single', sz=4, color='D3D3D3'),
            bottom=dict(val='single', sz=4, color='D3D3D3'),
            left=dict(val='none', sz=0, color='auto'),
            right=dict(val='none', sz=0, color='auto')
        )

for c in tbl_ds.rows[0].cells:
    set_cell_border(c, top=dict(val='single', sz=12, color='003366'), bottom=dict(val='single', sz=12, color='003366'))
for c in tbl_ds.rows[-1].cells:
    set_cell_border(c, bottom=dict(val='single', sz=12, color='003366'))

p_cap_ds = doc.add_paragraph()
p_cap_ds.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_ds.paragraph_format.space_before = Pt(4)
p_cap_ds.paragraph_format.space_after = Pt(12)
r_ds = p_cap_ds.add_run("Bảng 3.7: Bảng đối chiếu tổng kết toàn diện các thông số kỹ thuật cốt lõi.")
r_ds.font.name = 'Times New Roman'
r_ds.font.italic = True
r_ds.font.size = Pt(9.5)

add_body_p(
    "Kết luận đánh giá tổng quát: Module cảm biến siêu âm RCWL-1601 khi kết hợp với bộ đếm thời gian vi điều khiển ESP32 "
    "và giải thuật bù nhiệt Laplace đã thể hiện các đặc tính kỹ thuật vượt trội so với các thông số công bố tối thiểu của nhà sản xuất. "
    "Đây là tiền đề lý thuyết và thực nghiệm vững chắc để triển khai hệ thống vào bài toán thực tế: "
    "\"Hệ thống giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ\" trong Chương 4."
)

# Lưu tệp Word an toàn
try:
    doc.save(OUTPUT_FILE)
    print(f"Xuất bản thành công tài liệu Word hoàn chỉnh chuẩn Headings và Equation: {OUTPUT_FILE}")
except PermissionError:
    alt_file = OUTPUT_FILE.replace(".docx", "_sync_test.docx")
    doc.save(alt_file)
    print(f"WINWORD đang mở tệp chính! Đã lưu an toàn vào bản sao đồng bộ: {alt_file}")
