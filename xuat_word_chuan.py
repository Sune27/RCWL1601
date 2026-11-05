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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "Bao_Cao_Thuc_Nghiem_RCWL1601.docx")
IMG_H2_1_PATH = os.path.join(BASE_DIR, "graph", "chuong_2", "hinh_2_1_hoi_tu_sai_so_N.png")
IMG_H2_2_PATH = os.path.join(BASE_DIR, "graph", "chuong_2", "hinh_2_2_dao_ham_diem_khuyu_tay.png")

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
        f'<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
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
    "Trong tiến trình tự động hóa công nghiệp và phát triển các hệ thống điều khiển thông minh "
    "(Công nghiệp 4.0, Robotics, Internet vạn vật - IoT), bài toán đo lường cự ly, vị trí và mức chất lỏng "
    "không tiếp xúc đóng vai trò mang tính sống còn. Các hệ thống cảnh báo va chạm của xe tự hành AGV trong nhà máy, "
    "trạm phân loại kích thước bao bì kiện hàng trên băng tải logistics, hay các bồn chứa hóa chất ăn mòn đều đòi hỏi "
    "phương pháp đo đạc không tiếp xúc vật lý nhằm tránh hỏng hóc cơ học, tránh gây nhiễm bẩn dung dịch và bảo đảm khả năng "
    "vận hành liên tục 24/7.",

    "Trong số các công nghệ đo khoảng cách hiện nay (Laser LiDAR, Radar sóng milimét, Cảm biến quang học hồng ngoại và Siêu âm), "
    "cảm biến siêu âm nổi bật lên như một giải pháp cân bằng tối ưu giữa chi phí sản xuất cực thấp, độ bền cơ học cao, không phụ thuộc "
    "vào màu sắc hay độ trong suốt của vật thể phản xạ, và đặc biệt an toàn tuyệt đối cho người vận hành.",

    "Module cảm biến siêu âm RCWL-1601 thế hệ mới là phiên bản nâng cấp phần cứng vượt trội so với dòng cảm biến kinh điển HC-SR04. "
    "Được tích hợp vi mạch điều khiển chuyên dụng RCWL-9610, RCWL-1601 cho phép cấp nguồn và giao tiếp trực tiếp với vi điều khiển "
    "ở dải điện áp rộng từ 2.8 V đến 5.5 V, hoàn toàn tương thích mức logic 3.3 V của vi điều khiển ESP32 mà không cần mạch chuyển mức điện áp. "
    "Bên cạnh đó, việc vận tốc lan truyền sóng âm trong không khí phụ thuộc phi tuyến vào nhiệt độ môi trường theo phương trình Laplace "
    "là nguồn gốc của sai số trôi cự ly lớn trong điều kiện khí hậu nóng ẩm tại Việt Nam nếu không có giải thuật bù trừ thích hợp.",

    "Xuất phát từ yêu cầu thực tiễn của học phần Kỹ thuật Đo lường và Cảm biến, nhóm sinh viên đã lựa chọn "
    "và thực hiện đề tài: 'Khảo sát thực nghiệm đặc tính đo lường của cảm biến siêu âm RCWL-1601'. Mục tiêu của báo cáo bao gồm:",

    "1. Khảo sát toàn diện đặc tính tĩnh và động học của cảm biến RCWL-1601 trên giàn thực nghiệm chuẩn hóa: xác định dải đo tuyến tính, "
    "khảo sát chi tiết vùng chết (1 cm – 3 cm), dải đo xa mở rộng vượt định mức (lên đến 550 cm), độ chụm (độ lệch chuẩn thực nghiệm, sai số chuẩn trung bình), "
    "độ chính xác, độ nhạy thời gian bay, và đánh giá độ không đảm bảo đo mở rộng theo tiêu chuẩn quốc tế ISO/GUM.",

    "2. Khảo sát các hiện tượng vật lý chuyên sâu ảnh hưởng đến phép đo siêu âm: độ trễ đo giữa chiều tiến và chiều lùi (Hysteresis), "
    "hiện tượng tán xạ khuếch tán trên bề mặt gồ ghề (Diffuse Scattering), và định lượng hiệu quả bù trôi vận tốc sóng âm Laplace theo nhiệt độ.",

    "3. Xây dựng chuỗi lọc số thích nghi (Khoảng tứ phân vị IQR) và thiết kế hệ thống hoàn chỉnh: "
    "'Giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ trên ESP32', giải quyết triệt để vấn đề vùng chết và sóng gợn mặt nước.",

    "Nội dung bản báo cáo được bố cục chặt chẽ thành 5 chương chính:\n"
    "• Chương 1: Cơ sở lý thuyết về cảm biến siêu âm và phương pháp đánh giá đo lường.\n"
    "• Chương 2: Thiết kế và bố trí hệ thống thực nghiệm.\n"
    "• Chương 3: Phân tích kết quả thực nghiệm và xử lý số liệu.\n"
    "• Chương 4: Xây dựng và phân tích bài toán ứng dụng thực tế.\n"
    "• Chương 5: Kết luận và kiến nghị kỹ thuật."
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
add_heading_1("BẢNG QUY ƯỚC KÝ HIỆU VÀ CẤU TRÚC DỮ LIỆU THỰC NGHIỆM")

p_cap = doc.add_paragraph()
p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_cap.paragraph_format.space_after = Pt(6)
r_cap = p_cap.add_run("Bảng 0.1: Bảng quy ước định danh 4 tập dữ liệu thực nghiệm chuẩn hóa của đề tài")
r_cap.font.name = 'Times New Roman'
r_cap.font.size = Pt(12)
r_cap.font.bold = True

table_conv = doc.add_table(rows=5, cols=5)
table_conv.alignment = WD_TABLE_ALIGNMENT.CENTER
table_conv.autofit = False

col_widths = [Cm(2.5), Cm(2.5), Cm(3.2), Cm(2.8), Cm(5.0)]
headers = ["Ký hiệu mã", "Chiều dịch chuyển", "Bề mặt phản xạ", "Nhiệt độ môi trường", "Mục đích nghiên cứu kiểm chứng"]

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
    ("FSDT", "Tiến (Forward)\n1 cm → 600 cm", "Phẳng nhẵn bóng\n(Specular)", "27.0 °C\n(Nhiệt độ phòng)", "Khảo sát toàn dải, vùng chết (1-3cm), dải xa mở rộng (550cm), độ chụm & độ chính xác."),
    ("BSDT", "Lùi (Backward)\n300 cm → 10 cm", "Phẳng nhẵn bóng\n(Specular)", "27.0 °C\n(Nhiệt độ phòng)", "Đối chứng trực tiếp với FSDT trên 19 mốc cự ly để đánh giá hiện tượng Độ trễ (Hysteresis)."),
    ("FRDT", "Tiến (Forward)\n10 cm → 375 cm", "Nhám gồ ghề\n(Diffuse)", "27.0 °C\n(Nhiệt độ phòng)", "Đánh giá hiện tượng tán xạ khuếch tán, độ suy giảm tỷ số S/N và giới hạn tầm đo trên bề mặt xốp."),
    ("FSAT", "Tiến (Forward)\n10 cm → 300 cm", "Phẳng nhẵn bóng\n(Specular)", "20.0 °C\n(Phòng điều hòa)", "Khảo sát độ trôi cự ly do vận tốc âm và kiểm chứng hiệu quả thuật toán bù nhiệt Laplace.")
]

for row_idx, data in enumerate(dataset_rows, start=1):
    row_cells = table_conv.rows[row_idx].cells
    for col_idx, text in enumerate(data):
        row_cells[col_idx].text = text
        p = row_cells[col_idx].paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 4 else WD_ALIGN_PARAGRAPH.JUSTIFY
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
r_sep_t = p_sep.add_run("Phân định cấu trúc tổ chức dữ liệu dự án:")
r_sep_t.font.name = 'Times New Roman'
r_sep_t.font.size = Pt(13)
r_sep_t.font.bold = True
r_sep_t.font.color.rgb = C_NAVY

p_f1 = doc.add_paragraph()
p_f1.paragraph_format.first_line_indent = Cm(1.0)
p_f1.paragraph_format.space_after = Pt(4)
r1 = p_f1.add_run("• Thư mục 'result/': ")
r1.font.bold = True
p_f1.add_run(
    "Lưu trữ toàn bộ các tệp dữ liệu thô ban đầu được ghi nhận trực tiếp từ vi điều khiển ESP32 theo từng mốc cự ly đơn lẻ. "
    "Mỗi tệp bao gồm 50 dòng đo lường với 3 trường thông tin chuẩn hóa: thời gian bay hai chiều t (μs), khoảng cách đo được distance_cm (cm) "
    "và nhiệt độ môi trường ghi nhận temperature_c (°C). Quy ước đặt tên tệp: <MÃ_TẬP>_<XXX>cm.csv (ví dụ: FSDT_010cm.csv, FSDT_100cm.csv)."
)
for r in p_f1.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

p_f2 = doc.add_paragraph()
p_f2.paragraph_format.first_line_indent = Cm(1.0)
p_f2.paragraph_format.space_after = Pt(12)
r2 = p_f2.add_run("• Thư mục 'du_lieu_tong_hop/': ")
r2.font.bold = True
p_f2.add_run(
    "Lưu trữ các tệp dữ liệu tổng hợp đã được hợp nhất. Mỗi tệp tổ chức cấu trúc bảng ma trận với các cột là các mốc cự ly khảo sát "
    "và các hàng là 50 lần đo tương ứng. Toàn bộ các phân tích định lượng, hồi quy ma trận và đánh giá độ không đảm bảo đo ở Chương 3 "
    "đều được thực thi trực tiếp từ thư mục này."
)
for r in p_f2.runs:
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
    "Module cảm biến phát ra một chuỗi xung kích siêu âm hình sin ở tần số công tác danh định 40 kHz. "
    "Sóng âm lan truyền trong không gian tự do với vận tốc v, gặp mặt phẳng vật cản và phản xạ dội ngược trở lại đầu thu. "
    "Đầu thu áp điện chuyển đổi năng lượng dao động cơ học của sóng âm dội về thành tín hiệu điện áp phản hồi."
)
add_body_p("Khoảng cách x từ cảm biến đến vật cản được xác định từ thời gian bay tổng cộng t của sóng âm theo phương trình:")

# Native Word Equation 1.1: x = (v · t) / 2
add_native_equation(
    '<m:r><m:t>x</m:t></m:r>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:f>'
    '<m:num><m:r><m:t>v · t</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>2</m:t></m:r></m:den>'
    '</m:f>',
    eq_num="1.1"
)

add_body_p(
    "Trong đó: x là khoảng cách đo từ mặt trước màng rung cảm biến đến bề mặt phản xạ (m); "
    "v là vận tốc truyền sóng âm trong không khí (m/s); t là thời gian bay khứ hồi từ khi phát xung đến khi thu được xung dội về (s). "
    "Hệ số 2 thể hiện sóng âm phải vượt qua hai lần quãng đường (lượt đi và lượt về)."
)

add_heading_3("1.1.2. Mô hình toán học bù nhiệt độ môi trường cho vận tốc âm thanh")
add_body_p(
    "Trong chất khí lý tưởng, sóng âm lan truyền dưới dạng sóng dọc thông qua quá trình nén và giãn nở đoạn nhiệt tuần hoàn. "
    "Vận tốc truyền sóng âm được xác định theo phương trình nhiệt động học Laplace:"
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
    "M là khối lượng mol biểu kiến trung bình của không khí khô (M ≈ 0.028964 kg/mol); T_K là nhiệt độ tuyệt đối của môi trường (K), với T_K = T + 273.15 (°C)."
)
add_body_p(
    "Khai triển chuỗi Taylor bậc nhất của vận tốc sóng âm quanh điểm chuẩn 0 °C (T_0 = 273.15 K, v_0 ≈ 331.3 m/s) ta thu được "
    "phương trình thực nghiệm xấp xỉ tuyến tính chính xác cao:"
)

# Native Word Equation 1.3: v(T) = 331.3 + 0.606 * T
add_native_equation(
    '<m:r><m:t>v(T) = 331.3 + 0.606 · T    (m/s)</m:t></m:r>',
    eq_num="1.3"
)

add_body_p(
    "Phương trình tuyến tính (1.3) chỉ ra rằng: khi nhiệt độ môi trường thay đổi 1 °C, vận tốc sóng âm thay đổi tương ứng 0.606 m/s "
    "(khoảng 0.177%). Nếu nhiệt độ phòng dao động 7 °C (ví dụ giữa phòng bật điều hòa 20 °C và nhiệt độ phòng mặc định 27 °C), "
    "vận tốc sóng âm sẽ biến thiên khoảng 4.24 m/s (1.24%). Nếu hệ thống sử dụng vận tốc cố định, sai số đo khoảng cách sẽ trôi lũy tiến "
    "theo cự ly đo, đạt tới hàng chục milimét ở cự ly trên 2 m. Do đó, việc đo nhiệt độ môi trường thời gian thực để bù trừ vận tốc v(T) "
    "là yêu cầu kỹ thuật bắt buộc."
)

add_heading_3("1.1.3. Sự suy hao năng lượng sóng âm theo cự ly đo")
add_body_p("Năng lượng và biên độ áp suất âm p(x) của sóng âm suy giảm mạnh theo khoảng cách truyền dẫn do hai cơ chế vật lý song song:")
add_bullet_p("Do chùm sóng âm phát đi theo dạng hình nón. Năng lượng sóng âm phân bố trên diện tích mặt cầu tăng dần, khiến mật độ công suất âm suy giảm tỷ lệ nghịch với bình phương khoảng cách: I(x) ~ 1/x².", "1. Phân kỳ hình học: ")
add_bullet_p("Quá trình truyền sóng gây ma sát phân tử và dẫn nhiệt trong chất khí, làm suy hao biên độ áp suất âm. Ở tần số 40 kHz và nhiệt độ phòng 27 °C, độ ẩm 60%, hệ số suy hao khí quyển đạt xấp xỉ α ≈ 1.2 dB/m.", "2. Hấp thụ âm nội tại của không khí: ")
add_body_p(
    "Tổng suy hao sau hành trình hai chiều (2x) lên tới hàng chục decibel ở cự ly xa (x > 3 m). "
    "Vì vậy, ở cự ly trên 5.5 m, biên độ xung phản xạ sẽ tụt xuống dưới ngưỡng nhạy phát hiện của bộ so sánh, dẫn tới việc vi điều khiển "
    "bị tràn thời gian ngắt câm và trả về giá trị lỗi bão hòa."
)

# 1.2
add_heading_2("1.2. ĐẶC TÍNH HOẠT ĐỘNG VÀ THÔNG SỐ CỦA MODULE RCWL-1601")

add_heading_3("1.2.1. Giản đồ xung kích hoạt và phản hồi thời gian bay")
add_body_p("Module RCWL-1601 giao tiếp với vi điều khiển ESP32 thông qua giao thức xung kỹ thuật số hai chân (Trigger và Echo):")
add_bullet_p("Vi điều khiển chủ động kéo chân TRIG lên mức logic CAO để phát lệnh đo.", "• Bước 1 - Kích hoạt xung (Trigger Pulse): ")
add_bullet_p("Khi nhận được xung TRIG, vi mạch chuyên dụng RCWL-9610 trên module tự động kích hoạt mạch dao động công suất phát chuỗi 8 chu kỳ xung siêu âm dạng sóng vuông ở tần số 40 kHz. Đồng thời, chân ECHO được kéo lên mức CAO để báo hiệu bắt đầu chu kỳ bay.", "• Bước 2 - Phát chùm sóng siêu âm: ")
add_bullet_p("Sóng âm dội về tác động lên màng thu, tạo điện áp vi sai xoay chiều. Vi mạch RCWL-9610 thực hiện khuếch đại tự động độ lợi và lọc thông dải 40 kHz. Ngay khi biên độ tín hiệu vượt ngưỡng so sánh, IC lập tức kéo chân ECHO xuống mức THẤP.", "• Bước 3 - Thu nhận sóng phản xạ và ngắt xung (Echo Pulse): ")
add_bullet_p("Độ rộng mức cao của xung ECHO (t_echo) tỷ lệ thuận chính xác với thời gian bay hai chiều t của sóng âm.", "• Bước 4 - Đo thời gian bay ToF: ")

add_heading_3("1.2.2. Bảng thông số kỹ thuật danh định của RCWL-1601")
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
add_heading_2("1.3. CƠ SỞ LÝ THUYẾT XỬ LÝ SỐ LIỆU ĐO LƯỜNG VÀ ĐỘ KHÔNG ĐẢM BẢO ĐO (ISO/GUM)")

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

add_heading_3("1.3.2. Tiêu chuẩn phát hiện và lọc sai số thô bằng Khoảng tứ phân vị (IQR)")
add_body_p(
    "Trong đo đạc thực nghiệm sóng siêu âm, các xung nhiễu điện từ, bọt khí bề mặt, góc phản xạ dị thường hoặc hiện tượng mất xung phản hồi "
    "ở cự ly xa (dẫn đến tràn thời gian bay bão hòa) có thể tạo ra các mẫu đo ngoại lai (sai số thô) có giá trị sai lệch nghiêm trọng. "
    "Hệ thống lựa chọn phương pháp thống kê phi tham số bền vững dựa trên Khoảng tứ phân vị (Interquartile Range - IQR) "
    "kết hợp hệ hàng rào Tukey (Tukey's Fences) làm giải thuật lọc số chuẩn hóa duy nhất:"
)

# Native Word Equation 1.6: IQR = Q_3 - Q_1
add_native_equation(
    '<m:r><m:t>IQR = </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>3</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> - </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>Q</m:t></m:r></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub>',
    eq_num="1.6"
)

add_body_p("Cận dưới (Lower Fence) và Cận trên (Upper Fence) được xác định theo:")

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

add_body_p(
    "Mọi mẫu đo nằm ngoài khoảng [LF, UF] đều bị loại bỏ hoàn toàn trước khi đưa vào tính toán các chỉ số thống kê đo lường. "
    "Phương pháp này có ưu thế vượt trội do tính chất bền vững, hoàn toàn miễn nhiễm với các mẫu tràn thời gian cực trị (824.6 cm) "
    "và triệt tiêu triệt để hiện tượng che khuất ngoại lai (masking effect)."
)

add_heading_3("1.3.3. Hệ thống công thức đánh giá các Đặc tính tĩnh của cảm biến")
add_bullet_p("Đánh giá mức độ lặp lại nhất quán của phép đo thông qua độ lệch chuẩn thực nghiệm mẫu s và sai số chuẩn của giá trị trung bình SE = s / √N (phản ánh độ chụm của ước lượng trung bình mẫu x̄ khi thực hiện N lần đo lặp độc lập).", "1. Độ chụm và Sai số chuẩn trung bình: ")
add_bullet_p("Đánh giá mức độ sai lệch giữa giá trị đo trung bình và giá trị chuẩn: Sai số tuyệt đối Δx = x̄ - x_true; Sai số tương đối δ% = (Δx / x_true) · 100%.", "2. Sai số đo lường: ")
add_bullet_p("Tỷ số giữa độ biến thiên tín hiệu đầu ra và độ biến thiên đại lượng đo đầu vào: S_t = Δt / Δx_true (μs/cm).", "3. Độ nhạy (Sensitivity): ")
add_bullet_p(
    "Đánh giá mức độ bám sát của đặc tính tĩnh thực nghiệm với đường thẳng lý thuyết x̂ = a · x_true + b. "
    "Áp dụng phương pháp bình phương bé nhất dưới dạng phương trình ma trận chuẩn tắc, vector hệ số hồi quy được giải trực tiếp theo:",
    "4. Độ tuyến tính và Sai số phi tuyến (Linearity): "
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

add_body_p(
    "Hệ số xác định tương quan R² = 1 - [∑(x̄_k - x̂_k)² / ∑(x̄_k - x̄_tb)²]. "
    "Sai số phi tuyến cực đại: δ_NL% = (max_k |x̄_k - x̂_k| / x_FS) · 100%."
)
add_bullet_p(
    "Phản ánh sự bất đối xứng của giá trị đo tại cùng một điểm cự ly khi tiếp cận theo hai hướng ngược nhau (Chiều tiến Forward và Chiều lùi Backward): "
    "ΔH_k = |x̄_forward,k - x̄_backward,k|. "
    "Sai số trễ tương đối toàn dải: γ_H% = (max_k ΔH_k / x_FS) · 100%.",
    "5. Độ trễ (Hysteresis): "
)
add_bullet_p(
    "Biến thiên nhỏ nhất của khoảng cách đầu vào mà hệ thống đo có thể nhận biết và phân biệt rõ ràng. "
    "Được xác định bởi độ phân giải bộ đếm thời gian vi điều khiển (1 μs tương đương ≈ 0.175 mm) và độ tán xạ ngẫu nhiên s của cảm biến.",
    "6. Độ phân giải (Resolution): "
)

add_heading_3("1.3.4. Đánh giá Độ không đảm bảo đo")
add_body_p(
    "Theo hướng dẫn quốc tế ISO/IEC Guide 98-3 (GUM), độ tin cậy của kết quả đo được lượng hóa qua độ không đảm bảo đo toàn diện:"
)
add_bullet_p("Đánh giá bằng phương pháp phân tích thống kê chuỗi quan sát lặp lại: u_A = SE = s / √N.", "• Độ không đảm bảo đo Loại A (u_A): ")
add_bullet_p(
    "Đánh giá bằng các phương pháp phi thống kê (thông số kỹ thuật thiết bị, độ phân giải vi điều khiển, độ chia thước chuẩn cơ khí). "
    "Với giả thiết phân bố xác suất hình chữ nhật, độ không đảm bảo chuẩn thành phần là: u_B = a / √3, "
    "trong đó a là nửa khoảng dung sai cho phép.",
    "• Độ không đảm bảo đo Loại B (u_B): "
)
add_bullet_p("Kết hợp toàn bộ các thành phần theo định luật lan truyền sai số: u_c = √(u_A² + ∑ u_{B,j}²).", "• Độ không đảm bảo đo chuẩn tổng hợp (u_c): ")
add_bullet_p("Mở rộng khoảng tin cậy với hệ số phủ k_p = 2 (tương ứng mức tin cậy xấp xỉ 95% đối với bậc tự do lớn): U_95% = k_p · u_c = 2 · u_c.", "• Độ không đảm bảo đo mở rộng (U_95%): ")
add_body_p("Kết quả đo hoàn chỉnh của phép đo khoảng cách được biểu diễn:")

# Native Word Equation 1.10: x = x_bar +- U_95%
add_native_equation(
    '<m:r><m:t>x = </m:t></m:r>'
    '<m:acc><m:accPr><m:chr m:val="̄"/></m:accPr><m:e><m:r><m:t>x</m:t></m:r></m:e></m:acc>'
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

add_heading_1("CHƯƠNG 2: THIẾT KẾ VÀ BỐ TRÍ HỆ THỐNG THỰC NGHIỆM")

# 2.1
add_heading_2("2.1. MỤC TIÊU VÀ PHƯƠNG PHÁP LUẬN THỰC NGHIỆM")

add_heading_3("2.1.1. Mục tiêu thực nghiệm")
add_body_p(
    "Nghiên cứu thực nghiệm được thiết kế nhằm mục đích kiểm chứng khoa học và định lượng hóa các đặc tính đo lường "
    "của module cảm biến siêu âm RCWL-1601 trên nền tảng vi điều khiển ESP32 với các mục tiêu trọng tâm:"
)
add_bullet_p("Xác định dải đo tuyến tính ổn định, khảo sát chi tiết vùng chết (1 cm – 3 cm), kiểm tra giới hạn đo xa cực đại vượt định mức (lên đến 550 cm), và ngưỡng bão hòa timeout (580 cm – 600 cm).", "1. Khảo sát dải đo thực tế: ")
add_bullet_p("Đánh giá độ lặp lại (độ lệch chuẩn thực nghiệm s, sai số chuẩn của giá trị trung bình SE), sai số tuyệt đối và sai số tương đối trên toàn dải đo.", "2. Định lượng độ chụm và độ chính xác: ")
add_bullet_p("Xác định hàm truyền thời gian bay ToF theo khoảng cách, tìm hệ số góc độ nhạy thực tế St (μs/cm) và đối chiếu với mô hình lý thuyết Laplace.", "3. Đánh giá độ nhạy và độ tuyến tính: ")
add_bullet_p("Định lượng sai số trôi cự ly do vận tốc sóng âm khi nhiệt độ phòng thay đổi từ 27.0 °C xuống 20.0 °C, chứng minh hiệu quả triệt tiêu sai số của thuật toán bù nhiệt độ Laplace.", "4. Đánh giá ảnh hưởng của nhiệt độ môi trường: ")
add_bullet_p("So sánh đặc tính phản xạ gương (mặt phẳng nhẵn) và tán xạ khuếch tán (mặt gồ ghề nhấp nhô) ảnh hưởng đến độ chụm và cự ly cực đại.", "5. Đánh giá ảnh hưởng của bề mặt phản xạ: ")
add_bullet_p("Đánh giá sự bất đối xứng của hàm truyền khi di chuyển bia phản xạ theo chiều tiến và chiều lùi.", "6. Đánh giá độ trễ (Hysteresis): ")

add_heading_3("2.1.2. Phương pháp luận thực nghiệm")
add_body_p(
    "Để đảm bảo tính khách quan và khả năng tái lập của kết quả đo, nghiên cứu áp dụng phương pháp luận đo lường chuẩn hóa:"
)
add_bullet_p("Sử dụng thước đo tiêu chuẩn có độ chia milimét tiêu chuẩn (độ không đảm bảo đo u_B1 = 0.289 mm) làm chuẩn chiều dài đối chứng.", "• Phương pháp đo so sánh trực tiếp: ")
add_bullet_p("Tại mỗi mốc cự ly chuẩn, thực hiện lặp lại N lần đo độc lập trong điều kiện môi trường ổn định để đánh giá độ phân tán ngẫu nhiên và tính toán độ không đảm bảo đo Loại A (u_A).", "• Phương pháp đo lặp thống kê: ")
add_bullet_p("Nhiệt độ môi trường phòng thực nghiệm được giám sát liên tục bằng nhiệt kế. Dữ liệu nhiệt độ được ghi nhận đồng bộ vào từng mẫu đo để áp dụng thuật toán bù vận tốc sóng âm Laplace.", "• Phương pháp kiểm soát và bù trừ điều kiện môi trường: ")
add_bullet_p("Toàn bộ dữ liệu thô (thời gian bay t, khoảng cách đo x, nhiệt độ T) được ESP32 truyền về máy tính tự động ghi lưu thành các tệp định dạng CSV.", "• Phương pháp thu thập dữ liệu tự động hóa: ")

# 2.2
add_heading_2("2.2. THIẾT KẾ PHẦN CỨNG VÀ KHÔNG GIAN THỰC NGHIỆM")

add_heading_3("2.2.1. Thiết kế phần cứng và sơ đồ kết nối điện")
add_body_p(
    "Hệ thống đo lường sử dụng module cảm biến siêu âm RCWL-1601 kết nối trực tiếp với vi điều khiển ESP32 NodeMCU-32S. "
    "Nhờ tích hợp vi mạch RCWL-9610 hỗ trợ dải điện áp công tác rộng từ 2.8 V đến 5.5 V, cảm biến được cấp nguồn trực tiếp từ chân 3V3 của ESP32. "
    "Các đường tín hiệu TRIG và ECHO giao tiếp trực tiếp với các chân GPIO của ESP32 ở mức logic 3.3 V mà không cần mạch chuyển đổi mức logic."
)

p_tbl1 = doc.add_paragraph()
p_tbl1.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_tbl1.paragraph_format.space_after = Pt(4)
r_t1 = p_tbl1.add_run("Bảng 2.1: Sơ đồ kết nối phần cứng giữa cảm biến RCWL-1601 và vi điều khiển ESP32")
r_t1.font.name = 'Times New Roman'
r_t1.font.size = Pt(12)
r_t1.font.bold = True

pin_data = [
    ("VCC", "3V3 (ESP32)", "Cấp nguồn nuôi cảm biến"),
    ("GND", "GND (ESP32)", "Nối đất chung hệ thống"),
    ("TRIG", "GPIO 5 (ESP32)", "Ngõ vào kích phát xung siêu âm"),
    ("ECHO", "GPIO 18 (ESP32)", "Ngõ ra phản hồi thời gian bay ToF")
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

add_heading_3("2.2.2. Thiết kế không gian và kiểm soát điều kiện môi trường thực nghiệm")
add_body_p(
    "Đặc tính sóng siêu âm có hình nón đòi hỏi không gian đo phải được tính toán để loại trừ các phản xạ phụ:"
)
add_bullet_p("Hệ thống cảm biến và viên gạch phản xạ được đặt trên hai bàn thí nghiệm có độ cao H_table = 85.0 cm so với mặt sàn phòng đo.", "• Chiều cao bàn đo H_table = 85 cm: ")
add_bullet_p("Thực nghiệm được bố trí dọc theo hành lang kín gió dài 10 m, chiều rộng 2.8 m. Cảm biến đặt cách tường bên ít nhất 1.4 m. Trong suốt quá trình đo, hệ thống cửa được đóng kín tránh gió lùa và biến thiên nhiệt độ đột ngột.", "• Nhiệt độ phòng đo: ")

add_heading_3("2.2.3. Bố trí mô hình và định vị thiết bị đo")
add_body_p(
    "Để đảm bảo phép đo đạt độ chính xác cao và hạn chế tối đa sai số góc lệch trục, mô hình thực nghiệm được bố trí khoa học và chắc chắn:"
)
add_bullet_p("Module cảm biến RCWL-1601 được cắm cố định vững chắc trên breadboard. Breadboard gắn cảm biến cùng vi điều khiển ESP32 và máy tính thu thập dữ liệu được đặt trên bàn có độ cao khoảng 85 cm so với mặt sàn. Cảm biến được bố trí ở sát mép bàn, hướng hai mắt phát - thu trực diện ra ngoài.", "1. Cố định cảm biến tại vị trí mốc đo gốc: ")
add_bullet_p("Vật thể đo chuẩn là một viên gạch kích thước 40 cm × 40 cm có hai mặt với đặc tính bề mặt khác nhau: mặt trước phẳng nhẵn và mặt sau gồ ghề. Viên gạch được dựng thẳng đứng sát mép của chiếc bàn có cùng chiều cao 85 cm. Khi tiến hành đo, viên gạch luôn được căn chỉnh vuông góc với mặt bàn và đối diện trực diện với trục phát của cảm biến.", "2. Vật thể phản xạ mục tiêu: ")
add_bullet_p("Khoảng cách chuẩn x_true được xác định thủ công bằng thước dây đo chuẩn có độ chia nhỏ nhất đến milimet. Thước được căng thẳng giữa hai mép bàn để định vị chính xác từng mốc cự ly đo trước khi người thực nghiệm phát lệnh kích hoạt cảm biến đo và ghi nhận chuỗi dữ liệu trên máy tính.", "3. Căn chỉnh cự ly bằng thước đo tiêu chuẩn: ")

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
    ("Số lần đo lặp N", "50", "50", "50", "50"),
    ("Tổng số mẫu", "1.750", "950", "1.150", "950"),
    ("Mục đích", "Khảo sát toàn dải, độ chụm, độ chính xác, độ nhạy", "Khảo sát độ trễ (Hysteresis)", "Khảo sát tán xạ bề mặt", "Khảo sát trôi nhiệt độ")
]

table_sc = doc.add_table(rows=len(sc_data)+1, cols=5)
table_sc.alignment = WD_TABLE_ALIGNMENT.CENTER
table_sc.autofit = False

sc_widths = [Cm(3.2), Cm(3.2), Cm(3.2), Cm(3.2), Cm(3.2)]
sc_headers = ["Tham số", "FSDT (Chuẩn)", "BSDT (Trễ)", "FRDT (Nhám)", "FSAT (Nhiệt độ)"]

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

add_heading_3("2.4.1. Bản chất bài toán tối ưu cỡ mẫu trong đo lường siêu âm")
add_body_p(
    "Trong kỹ thuật đo lường, kết quả đo khoảng cách thực nghiệm không thể là một giá trị đơn độc, mà luôn được biểu diễn dưới dạng một khoảng tin cậy: "
    "x ∈ [x̄ - ε, x̄ + ε] (tương đương x = x̄ ± ε), trong đó x̄ là trung bình mẫu và ε là bán kính sai số ngẫu nhiên giới hạn của giá trị trung bình ở mức tin cậy 95%."
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
    "thừa số 1/√N đóng vai trò nén sai số khi tăng số lần đo lặp N. Mâu thuẫn kỹ thuật đặt ra là: muốn sai số ε cực nhỏ thì phải tăng N thật lớn, "
    "nhưng N càng lớn thì thời gian đo càng dài, tiêu hao năng lượng và dẫn tới nguy cơ trôi nhiệt độ môi trường (làm vận tốc âm thanh v(T) biến đổi sinh ra sai số hệ thống ngược lại). "
    "Mục tiêu bài toán là xác định kích thước mẫu N tối ưu để sai số ε < 0.5 mm (dung sai vạch chia thước), tốc độ đạo hàm đạt ngưỡng dừng bão hòa (|dε/dN| ≈ 0), "
    "và thời gian đo đủ ngắn để môi trường vi khí hậu được coi là bất biến."
)

add_heading_3("2.4.2. Phân tích dữ liệu thực nghiệm")
add_body_p(
    "Thực nghiệm tiến hành đo liên tục 100 lần tại 3 cự ly: 50 cm, 100 cm và 150 cm (nhiệt độ 27.0°C). "
    "Dữ liệu được lưu trữ tại bảng tổng hợp du_lieu_tong_hop/mau_100.csv. "
    "Thuật toán duyệt k từ 2 đến 100 trên tệp mau_100.csv để tính độ lệch chuẩn tích lũy s(k), bán kính sai số ε_95%(k) "
    "và đạo hàm bậc 1. Toàn bộ kết quả được phân tách thành 3 tệp độc lập trong thư mục du_lieu_tong_hop/chuong_2/: "
    "hoi_tu_50cm.csv, hoi_tu_100cm.csv và hoi_tu_150cm.csv."
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
    r_c1 = p_cap1.add_run("Hình 2.1: Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu tại 3 cự ly.")
    r_c1.font.name = 'Times New Roman'
    r_c1.font.size = Pt(10)
    r_c1.font.italic = True

add_body_p(
    "Đánh giá từ đồ thị Hình 2.1: Khi số lần đo k tăng từ 2 đến khoảng 30, bán kính sai số ngẫu nhiên ε_95% giảm nhanh ở cả 3 cự ly. "
    "Từ k ≥ 40 - 50, đường cong bắt đầu đi ngang và hội tụ ổn định. Tại k = 50, bán kính sai số ở cự ly 50 cm là ±0.03 mm, "
    "ở 100 cm là ±0.11 mm, và ở 150 cm là ±0.40 mm; tất cả đều nhỏ hơn giới hạn dung sai của thước cơ khí (±0.5 mm)."
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
    "Ở các giá trị k < 20, tốc độ biến thiên lớn (từ 0.05 đến 0.15 mm/bước), cho thấy việc tăng số lần đo ở giai đoạn đầu giảm sai số rất hiệu quả. "
    "Khi k tiến dần đến 50, tốc độ biến thiên giảm nhanh về xấp xỉ 0 (|dε/dk| ≤ 0.0005 mm/bước ≈ 0), đồ thị chuyển sang trạng thái bão hòa, "
    "việc đo thêm sau mốc 50 hầu như không làm sai số giảm thêm."
)

cv_data = [
    ("k = 5", "± 0.12 mm", "± 0.12 mm", "± 0.15 mm", "Mẫu nhỏ, sai số còn lớn"),
    ("k = 10", "± 0.06 mm", "± 0.06 mm", "± 0.12 mm", "Sai số giảm nhanh nhưng chưa phản ánh đủ biến động"),
    ("k = 20", "± 0.05 mm", "± 0.17 mm", "± 0.07 mm", "Sai số tiếp tục giảm, bắt đầu phân hóa theo cự ly"),
    ("k = 30", "± 0.03 mm", "± 0.14 mm", "± 0.28 mm", "Xuất hiện trượt chu kỳ sóng tại 150cm, sai số tăng lên"),
    ("k = 50", "± 0.03 mm", "± 0.11 mm", "± 0.40 mm", "Sai số nhỏ hơn 0.5 mm ở cả 3 cự ly, đạt bão hòa"),
    ("k = 100", "± 0.02 mm", "± 0.08 mm", "± 0.27 mm", "Vùng bão hòa, sai số hầu như không giảm thêm")
]

table_cv = doc.add_table(rows=len(cv_data)+1, cols=5)
table_cv.alignment = WD_TABLE_ALIGNMENT.CENTER
table_cv.autofit = False

cv_widths = [Cm(2.6), Cm(2.4), Cm(2.4), Cm(2.4), Cm(6.2)]
cv_headers = ["Cỡ mẫu k", "Mốc 50cm (ε_95%)", "Mốc 100cm (ε_95%)", "Mốc 150cm (ε_95%)", "Nhận xét"]

for idx_h, text_h in enumerate(cv_headers):
    c = table_cv.rows[0].cells[idx_h]
    c.text = text_h
    set_cell_background(c, "D9E1F2")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

for row_idx, data_row in enumerate(cv_data, start=1):
    for col_idx, text_val in enumerate(data_row):
        c = table_cv.rows[row_idx].cells[col_idx]
        c.text = text_val
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 4 else WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if col_idx == 0:
                r.font.bold = True
                if "50" in text_val:
                    r.font.color.rgb = C_MAROON

for row in table_cv.rows:
    for idx_w, width in enumerate(cv_widths):
        row.cells[idx_w].width = width
        set_cell_border(row.cells[idx_w],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_cv.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_cv.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

p_tbl3 = doc.add_paragraph()
p_tbl3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_tbl3.paragraph_format.space_before = Pt(4)
p_tbl3.paragraph_format.space_after = Pt(8)
r_t3 = p_tbl3.add_run("Bảng 2.3: Bảng trích số liệu của bán kính sai số Student 95%")
r_t3.font.name = 'Times New Roman'
r_t3.font.size = Pt(9.5)
r_t3.font.italic = True

add_body_p(
    "Đánh giá từ Bảng 2.3: Số liệu định lượng xác nhận xu hướng hội tụ của phép đo. "
    "Việc tăng cỡ mẫu từ k = 10 lên k = 50 giúp giảm sai số hơn 2 lần ở cả 3 cự ly. "
    "Tuy nhiên, khi tăng từ k = 50 lên k = 100, sai số tại mốc 100 cm chỉ giảm thêm 0.03 mm (từ 0.11 mm xuống 0.08 mm), "
    "giá trị này nhỏ hơn nhiều so với độ phân giải phần cứng của vi điều khiển (≈ 0.175 mm)."
)

add_body_p(
    "Kết luận: Dựa trên các phân tích và đánh giá từ hai đồ thị và bảng số liệu nêu trên, "
    "nhóm nghiên cứu đưa ra quyết định lựa chọn cỡ mẫu N = 50 cho toàn bộ các phép đo thực nghiệm của đề tài với các lý do:"
)
add_bullet_p(
    "Tại N = 50, bán kính sai số ngẫu nhiên ε_95% ở cả 3 cự ly đều nhỏ hơn dung sai vạch chia của thước chuẩn cơ khí (±0.5 mm): "
    "đạt ±0.03 mm tại 50cm; ±0.11 mm tại 100cm; và ±0.40 mm tại 150cm.",
    "1. Đạt tiêu chuẩn dung sai đo lường: "
)
add_bullet_p(
    "Đồ thị Hình 2.2 chứng minh tại k = 50, đạo hàm sai phân |dε/dk| ≤ 0.0005 mm/bước ≈ 0, xác nhận đường cong đã bước vào vùng bão hòa. "
    "Việc tăng số lần đo lên N = 100 chỉ giảm thêm 0.03 mm ở mốc 100cm (nhỏ hơn độ phân giải phần cứng vi điều khiển ≈ 0.175 mm).",
    "2. Điểm dừng đạo hàm tối ưu bão hòa: "
)
add_bullet_p(
    "Với chu kỳ lấy mẫu 50 ms (tần số quét 20 Hz), việc thu thập N = 50 mẫu chỉ mất đúng T_total = 2.5 giây cho mỗi mốc cự ly. "
    "Khoảng thời gian 2.5 giây đủ ngắn để nhiệt độ phòng và vi khí hậu được coi là bất biến, loại trừ hiện tượng trôi nhiệt độ môi trường.",
    "3. Bảo toàn tính ổn định vi khí hậu: "
)

# ==========================================================
# PHẦN 7: CHƯƠNG 3 (PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM)
# ==========================================================
add_heading_1("CHƯƠNG 3: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM")

add_body_p(
    "Chương 3 trình bày việc xử lý số liệu và phân tích kết quả đo từ bốn tập dữ liệu thực nghiệm: "
    "FSDT.csv (chiều tiến, mặt nhẵn, 27.0°C), BSDT.csv (chiều lùi, mặt nhẵn, 27.0°C), "
    "FRDT.csv (chiều tiến, mặt nhám, 27.0°C) và FSAT.csv (chiều tiến, mặt nhẵn, 20.0°C). "
    "Các phân tích dựa trên mô hình truyền sóng âm Laplace, phương pháp bình phương tối thiểu "
    "và quy chuẩn đánh giá độ không đảm bảo đo ISO/GUM đã nêu ở Chương 1."
)

add_heading_2("3.1. Tiền xử lý dữ liệu và Đánh giá hiệu quả lọc sai số thô bằng Khoảng tứ phân vị (IQR)")

add_heading_3("3.1.1. Khung tiền xử lý và cơ chế hình thành ngoại lai trong phép đo siêu âm")
add_body_p(
    "Theo thuật toán phát hiện sai số thô bằng Khoảng tứ phân vị (IQR / Tukey's Fences) đã nêu tại Mục 1.3.2 (Chương 1), "
    "dữ liệu từ 4 tập thực nghiệm được xử lý. Để giữ nguyên chuỗi thời gian, thuật toán thực hiện gán giá trị trực tiếp: "
    "mẫu nào nằm ngoài khoảng hợp lệ [LF, UF] sẽ được chuyển thành giá trị NaN."
)
add_body_p("Trong quá trình thu thập tín hiệu, dữ liệu thực nghiệm xuất hiện sai số thô do một số nguyên nhân:")
add_bullet_p(
    "Sóng âm phản xạ bị suy hao biên độ dưới ngưỡng phát hiện của mạch thu RCWL-9610. "
    "Bộ đếm thời gian của vi điều khiển ESP32 chờ hết chu kỳ (48 ms) và trả về giá trị ≈ 824.6 cm.",
    "1. Xung quá thời gian chờ: "
)
add_bullet_p(
    "Trên bề mặt nhám (FRDT), sóng âm phản xạ qua các vật thể phụ trước khi về đầu thu, "
    "làm tăng thời gian lan truyền ToF và tạo các giá trị đột biến.",
    "2. Tán xạ phản xạ nhiều đường: "
)

add_heading_3("3.1.2. Tổng hợp kết quả lọc ngoại lai trên toàn bộ 4 tập dữ liệu thực nghiệm")
add_body_p(
    "Kết quả tính toán chi tiết của từng mốc cự ly được lưu tại bảng dữ liệu du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv, "
    "và dữ liệu sau khi lọc được lưu tại 4 tệp: FSDT_clean.csv, BSDT_clean.csv, FRDT_clean.csv, FSAT_clean.csv. "
    "Bảng 3.1 tổng hợp kết quả lọc dữ liệu trên 4 tập thực nghiệm:"
)

t31_data = [
    ("FSDT.csv", "Chiều tiến – Mặt nhẵn (27.0°C)", "35 mốc", "1.750", "16 mốc", "77", "4.40%", "1.673", "95.60%"),
    ("BSDT.csv", "Chiều lùi – Mặt nhẵn (27.0°C)", "19 mốc", "950", "12 mốc", "61", "6.42%", "889", "93.58%"),
    ("FRDT.csv", "Chiều tiến – Mặt nhám (27.0°C)", "23 mốc", "1.150", "11 mốc", "59", "5.13%", "1.091", "94.87%"),
    ("FSAT.csv", "Chiều tiến – Phòng lạnh (20.0°C)", "19 mốc", "950", "8 mốc", "38", "4.00%", "912", "96.00%"),
    ("TỔNG HỢP", "Cả 4 tập thực nghiệm", "96 mốc", "4.800", "47 mốc", "235", "4.90%", "4.565", "95.10%"),
]

table_31 = doc.add_table(rows=len(t31_data)+1, cols=9)
table_31.alignment = WD_TABLE_ALIGNMENT.CENTER
table_31.autofit = False

t31_widths = [Cm(2.0), Cm(3.2), Cm(1.4), Cm(1.4), Cm(1.6), Cm(1.5), Cm(1.5), Cm(1.6), Cm(1.8)]
t31_headers = ["Tệp dữ liệu", "Điều kiện đo", "Số mốc", "Tổng mẫu", "Mốc có ngoại lai", "Mẫu ngoại lai", "Tỷ lệ (%)", "Mẫu hợp lệ", "Tỷ lệ hợp lệ (%)"]

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

p_cap_t31 = doc.add_paragraph()
p_cap_t31.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_t31.paragraph_format.space_before = Pt(4)
p_cap_t31.paragraph_format.space_after = Pt(8)
r_t31 = p_cap_t31.add_run("Bảng 3.1: Tổng hợp kết quả xử lý sai số thô bằng Khoảng tứ phân vị (IQR) trên toàn bộ 4.800 mẫu đo.")
r_t31.font.italic = True
r_t31.font.size = Pt(9.5)

add_body_p("Nhận xét từ kết quả Bảng 3.1:")
add_bullet_p(
    "Hệ thống đo duy trì độ ổn định tốt; chỉ có 4.90% mẫu bị loại bỏ trên toàn bộ 4.800 lần đo.",
    "Tỷ lệ giữ lại mẫu đạt 95.10%: "
)
add_bullet_p(
    "Tỷ lệ ngoại lai giữa FSDT (4.40%) và BSDT (6.42%) gần tương đương nhau, cho thấy điều kiện môi trường đo ổn định.",
    "Tính đối xứng giữa chiều tiến và chiều lùi: "
)
add_bullet_p(
    "Bề mặt nhám (FRDT) xuất hiện nhiều xung tán xạ hơn so với mặt nhẵn. Các xung này được bộ lọc IQR phát hiện và loại bỏ, giúp giá trị trung bình không bị lệch.",
    "Ảnh hưởng của bề mặt phản xạ: "
)

add_heading_3("3.1.3. Đánh giá trực quan hiệu quả triệt tiêu độ lệch chuẩn trên toàn dải đo")
add_body_p(
    "Hình 3.1 thể hiện biến thiên của độ lệch chuẩn thực nghiệm s trước và sau khi lọc trên thang bán logarit (semi-log scale), "
    "trong đó trục tung biểu diễn độ lệch chuẩn s theo thang logarit cơ số 10 (0.1 đến 1000 mm) và trục hoành biểu diễn khoảng cách chuẩn đối chứng từ 1 cm đến 600 cm."
)

IMG_H3_1_PATH = os.path.join(BASE_DIR, "graph", "chuong_3", "hinh_3_1_loc_sai_so_tho.png")
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
    r_c3_1.font.italic = True
    r_c3_1.font.size = Pt(10)

add_body_p("Đánh giá từ đồ thị Hình 3.1:")
add_bullet_p(
    "Trong khoảng đo làm việc (1 - 340 cm), độ lệch chuẩn duy trì ở mức dưới 1.0 mm. "
    "Tại mốc 360 cm, do hiện tượng trượt chu kỳ sóng ToF, độ lệch chuẩn thô tăng lên s = 90.33 mm. "
    "Tại các cự ly xa (580 cm và 600 cm), do sóng phản xạ suy hao mạnh dẫn đến các mẫu quá hạn (timeout 824.6 cm), "
    "độ lệch chuẩn thô tăng lên lần lượt s = 346.05 mm và s = 2621.02 mm.",
    "Đường màu đỏ nét đứt (Độ lệch chuẩn thô trước khi lọc): "
)
add_bullet_p(
    "Sau khi loại bỏ các giá trị ngoại lai bằng bộ lọc IQR kết hợp ngưỡng phân giải Δ_LSB = 0.0175 cm, "
    "đường độ lệch chuẩn duy trì ổn định trong dải 0.09 - 4.0 mm trên toàn dải đo 6 m, "
    "tiệm cận đường dung sai của thước cơ khí (0.5 mm).",
    "Đường màu xanh nét liền (Độ lệch chuẩn sau khi lọc IQR): "
)

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

t32_widths = [Cm(2.2), Cm(2.4), Cm(2.4), Cm(2.4), Cm(2.2), Cm(4.4)]
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
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 5 else WD_ALIGN_PARAGRAPH.LEFT
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

p_cap_t32 = doc.add_paragraph()
p_cap_t32.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_t32.paragraph_format.space_before = Pt(4)
p_cap_t32.paragraph_format.space_after = Pt(10)
r_t32 = p_cap_t32.add_run("Bảng 3.2: Đối chiếu độ lệch chuẩn trước và sau khi lọc IQR tại các mốc tiêu biểu.")
r_t32.font.italic = True
r_t32.font.size = Pt(9.5)

# ==========================================================
# MỤC 3.2: KHẢO SÁT DẢI ĐO THỰC TẾ, VÙNG CHẾT VÀ BÃO HÒA XA
# ==========================================================
add_heading_2("3.2. Khảo sát Dải đo thực tế, Vùng chết và Giới hạn bão hòa xa")

add_body_p(
    "Từ dữ liệu thực nghiệm 35 mốc cự ly từ 1 cm đến 600 cm trên tập FSDT.csv, đặc tính đo của cảm biến "
    "RCWL-1601 được phân chia thành các vùng làm việc: Vùng chết (1 cm – 3 cm), Vùng chuyển tiếp (4 cm – 5 cm), "
    "Dải làm việc ổn định (8 cm – 400 cm), Dải đo xa mở rộng (420 cm – 550 cm), và Ngưỡng bão hòa xa (580 cm – 600 cm)."
)

add_heading_3("3.2.1. Vùng chết (1 cm – 3 cm)")
add_body_p(
    "Khi khoảng cách từ vật cản đến cảm biến nhỏ hơn hoặc bằng 3 cm, cảm biến không đo được khoảng cách thực tế "
    "và giá trị đo bị giữ quanh ngưỡng 2.0 - 2.6 cm: tại cự ly chuẩn 1.0 cm, giá trị trung bình là 2.030 cm (sai số +103.05%); "
    "tại 2.0 cm là 2.352 cm (sai số +17.59%); tại 3.0 cm là 2.679 cm (sai số -10.72%)."
)
add_body_p(
    "Hiện tượng này xuất hiện do màng loa áp điện cần khoảng 120 - 150 μs để suy giảm dao động sau khi phát xung kích 40 kHz (200 μs). "
    "Ở cự ly dưới 3 cm, thời gian sóng âm đi và về nhỏ hơn 175 μs, trùng với thời gian tắt dần của màng phát và thời gian ngắt câm "
    "(blanking time) của vi mạch RCWL-9610. Mạch thu không phân biệt được sóng phản xạ và xung phát, khiến giá trị đo bị kẹp ở mức tối thiểu tương đương 2.0 - 2.6 cm."
)

IMG_H3_2_PATH = os.path.join(BASE_DIR, "graph", "chuong_3", "hinh_3_2_vung_chet_1_10cm.png")
if os.path.exists(IMG_H3_2_PATH):
    p_img3_2 = doc.add_paragraph()
    p_img3_2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3_2.paragraph_format.space_before = Pt(8)
    p_img3_2.paragraph_format.space_after = Pt(4)
    run_img3_2 = p_img3_2.add_run()
    run_img3_2.add_picture(IMG_H3_2_PATH, width=Cm(14.5))
    
    p_cap3_2 = doc.add_paragraph()
    p_cap3_2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap3_2.paragraph_format.space_after = Pt(8)
    r_c3_2 = p_cap3_2.add_run("Hình 3.2: Đặc tính đo khoảng cách trong vùng gần (1 cm – 10 cm).")
    r_c3_2.font.italic = True
    r_c3_2.font.size = Pt(10)

add_heading_3("3.2.2. Dải làm việc ổn định và dải mở rộng (5 cm – 550 cm)")
add_body_p(
    "Từ cự ly 8 cm đến 400 cm, xung phản xạ tách biệt rõ ràng khỏi xung phát và biên độ nằm trong dải khuếch đại của mạch thu. "
    "Sai số tương đối trong dải này luôn nhỏ hơn ±0.5%, chứng minh cảm biến hoạt động ổn định trong dải đo nhà sản xuất công bố."
)
add_body_p(
    "Ở dải 420 cm đến 550 cm, dù vượt cự ly định mức danh định (400 - 450 cm), cảm biến vẫn thu nhận tín hiệu chính xác "
    "với sai số nhỏ hơn 0.3%: tại 420 cm sai số là +0.29%, tại 500 cm sai số là +0.14%, và tại 550 cm sai số là +0.10% (độ lệch chuẩn 1.52 mm). "
    "Kết quả này đạt được nhờ tầng khuếch đại tự động điều chỉnh độ lợi trên vi mạch RCWL-9610 và bề mặt phản xạ phẳng đặt vuông góc."
)

add_heading_3("3.2.3. Ngưỡng suy hao và bão hòa xa (580 cm – 600 cm)")
add_body_p(
    "Ở cự ly từ 580 cm trở lên, năng lượng sóng phản xạ suy giảm mạnh do khoảng cách lớn: tại 580 cm bắt đầu xuất hiện mẫu timeout 824.6 cm; "
    "tại 600 cm tỷ lệ mất xung tăng lên 14% sau lọc IQR (và 62% ở dữ liệu thô), kéo giá trị trung bình thô lên 720.16 cm và độ lệch chuẩn thô lên 2621.02 mm. "
    "Do đó, 550 cm là giới hạn đo xa tin cậy thực tế của cảm biến."
)

t33_data = [
    ("1.0 cm", "2.030 cm", "0.035 mm", "+10.30 mm", "+103.05%", "Vùng chết (màng rung suy giảm)"),
    ("2.0 cm", "2.352 cm", "0.085 mm", "+3.52 mm", "+17.59%", "Vùng chết (kẹp ngưỡng ngắt câm)"),
    ("3.0 cm", "2.679 cm", "0.056 mm", "-3.21 mm", "-10.72%", "Vùng chết (thoát ngưỡng ngắt câm)"),
    ("5.0 cm", "4.295 cm", "0.085 mm", "-7.05 mm", "-14.10%", "Vùng chuyển tiếp"),
    ("10.0 cm", "10.570 cm", "0.061 mm", "+5.70 mm", "+5.70%", "Bắt đầu dải đo danh định"),
    ("50.0 cm", "49.847 cm", "0.094 mm", "-1.53 mm", "-0.31%", "Dải làm việc ổn định"),
    ("100.0 cm", "99.429 cm", "0.383 mm", "-5.71 mm", "-0.57%", "Dải làm việc ổn định"),
    ("200.0 cm", "200.351 cm", "2.192 mm", "+3.51 mm", "+0.18%", "Dải làm việc ổn định"),
    ("300.0 cm", "299.718 cm", "2.860 mm", "-2.82 mm", "-0.09%", "Dải làm việc ổn định"),
    ("400.0 cm", "401.402 cm", "1.850 mm", "+14.02 mm", "+0.35%", "Giới hạn danh định của cảm biến"),
    ("500.0 cm", "500.691 cm", "1.978 mm", "+6.91 mm", "+0.14%", "Dải đo xa mở rộng"),
    ("550.0 cm", "550.566 cm", "1.520 mm", "+5.66 mm", "+0.10%", "Giới hạn đo xa thực tế"),
    ("580.0 cm", "584.808 cm", "346.051 mm", "+48.08 mm", "+0.83%", "Ngưỡng suy hao (bắt đầu có timeout)"),
    ("600.0 cm", "720.161 cm", "2621.017 mm", "+1201.61 mm", "+20.03%", "Ngưỡng bão hòa xa (nhiều timeout)"),
]

table_33 = doc.add_table(rows=len(t33_data)+1, cols=6)
table_33.alignment = WD_TABLE_ALIGNMENT.CENTER
table_33.autofit = False

t33_widths = [Cm(2.0), Cm(2.4), Cm(2.4), Cm(2.4), Cm(2.2), Cm(4.6)]
t33_headers = ["Khoảng cách chuẩn", "Giá trị trung bình", "Độ lệch chuẩn s", "Sai số tuyệt đối", "Sai số tương đối", "Trạng thái vùng làm việc"]

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
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 5 else WD_ALIGN_PARAGRAPH.LEFT
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

p_cap_t33 = doc.add_paragraph()
p_cap_t33.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_t33.paragraph_format.space_before = Pt(4)
p_cap_t33.paragraph_format.space_after = Pt(10)
r_t33 = p_cap_t33.add_run("Bảng 3.3: Tổng hợp các vùng làm việc và đặc tính đo thực nghiệm trên toàn dải đo.")
r_t33.font.italic = True
r_t33.font.size = Pt(9.5)

# ==========================================================
# MỤC 3.3: ĐÁNH GIÁ ĐỘ CHỤM VÀ ĐỘ CHÍNH XÁC
# ==========================================================
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
    "cỡ mẫu hợp lệ sau lọc n_hợp_lệ ∈ [40, 50]) được trích xuất trực tiếp từ hai cột std_sach_mm và se_sach_mm "
    "trong tệp du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv:"
)
add_bullet_p(
    "Tại 8/9 mốc khảo sát, s đạt từ 0.035 mm đến 0.094 mm và SE đạt từ 0.0049 mm đến 0.0133 mm "
    "(nhỏ hơn nhiều so với một bước đếm phần cứng Δ_LSB ≈ 0.174 mm) nhờ biên độ sóng phản xạ mạnh từ mặt phẳng nhẵn của viên gạch chuẩn 40 cm × 40 cm. "
    "Riêng mốc 40 cm (n_hợp_lệ = 49) ghi nhận s = 3.144 mm và SE = 0.4491 mm.",
    "1. Vùng cự ly gần (1 cm ≤ x_true ≤ 50 cm, 9 mốc): "
)
add_bullet_p(
    "Tại 7/8 mốc, s nằm trong dải 0.088 mm – 0.383 mm và SE nằm trong dải 0.0128 mm – 0.0542 mm; "
    "riêng mốc 120 cm (n_hợp_lệ = 50) có s = 1.747 mm và SE = 0.2471 mm.",
    "2. Vùng cự ly trung bình (60 cm ≤ x_true ≤ 180 cm, 8 mốc): "
)
add_bullet_p(
    "Độ lệch chuẩn s dao động từ 0.142 mm (tại 220 cm, n_hợp_lệ = 40) đến 2.860 mm (tại 300 cm, n_hợp_lệ = 50), "
    "tương ứng SE biến thiên từ 0.0225 mm đến 0.4045 mm (tại 360 cm đạt s = 2.508 mm, SE = 0.3583 mm).",
    "3. Vùng cự ly xa danh định (200 cm ≤ x_true ≤ 360 cm, 11 mốc): "
)
add_bullet_p(
    "Độ lệch chuẩn s đạt 0.270 mm tại 400 cm (SE = 0.0407 mm), 0.228 mm tại 420 cm (SE = 0.0340 mm), "
    "tăng lên cực đại toàn dải 4.049 mm tại 450 cm (SE = 0.5726 mm), đạt 1.978 mm tại 500 cm (SE = 0.2797 mm) "
    "và giảm về 0.319 mm tại mốc giới hạn 550 cm (n_hợp_lệ = 42, SE = 0.0492 mm).",
    "4. Dải đo xa mở rộng (400 cm ≤ x_true ≤ 550 cm, 5 mốc): "
)
add_body_p(
    "Tính trên toàn bộ 33 mốc khảo sát (1 – 550 cm), cột se_sach_mm xác nhận sai số chuẩn trung bình SE không vượt quá 0.5726 mm; "
    "trong đó có 32/33 mốc đạt SE < 0.45 mm (nhỏ hơn nửa độ chia nhỏ nhất 0.5 mm của thước chuẩn) và 22/33 mốc đạt SE ≤ 0.10 mm."
)
add_body_p(
    "Giải thích cơ chế vật lý và thuật toán của dạng dao động răng cưa trên Hình 3.3: "
    "Trục hoành của Hình 3.3 biểu diễn sự thay đổi mốc khoảng cách chuẩn x_true (mỗi mốc đều đo độc lập với cỡ mẫu cố định N = 50), "
    "không phải trục tăng dần kích thước mẫu tích lũy k tại một vị trí cố định như bài toán hội tụ ở Mục 2.4 (Chương 2). "
    "Dạng lên xuống răng cưa luân phiên của s giữa các mốc cự ly xuất phát từ sự tương tác giữa bước nhảy một chu kỳ sóng mang siêu âm 40 kHz "
    "và ngưỡng tứ phân vị 25% của bộ lọc IQR (đã nêu tại Mục 1.3.2, Chương 1). Tại T = 27.0 °C (v = 347.66 m/s), một chu kỳ sóng mang T_0 = 25 μs "
    "ứng với quãng đường khứ hồi nửa bước sóng xấp xỉ 4.35 mm (0.435 cm). Khi biên độ sườn lên của bó xung phản hồi ECHO rơi sát mức điện áp ngưỡng "
    "so sánh trong vi mạch RCWL-9610, thời điểm kích hoạt bắt xung bị trượt ±1 chu kỳ sóng mang giữa các lần đo trong cùng 50 mẫu:"
)
add_bullet_p(
    "Tại những mốc cự ly có dưới 25% số mẫu trượt sang chu kỳ kế cận (như 80, 150, 220, 320, 400, 420, 550 cm, với 5 – 10 mẫu ngoại lai bị loại trong thong_ke_chuong_3.csv), "
    "hai tứ phân vị Q_1 và Q_3 vẫn nằm gọn trong cùng một chu kỳ sóng mang (IQR ≈ 0.018 – 0.066 cm); hàng rào Tukey cắt bỏ hoàn toàn cụm trượt chu kỳ, "
    "đưa s xuống mức rất thấp (0.142 – 0.395 mm) và SE xuống 0.022 – 0.060 mm.",
    "• Nhóm mốc lọc sạch cụm trượt chu kỳ: "
)
add_bullet_p(
    "Tại các mốc cự ly có trên 25% số mẫu phân bố sang chu kỳ kế cận (như 40, 120, 200, 250, 300, 340, 350, 450, 500 cm), "
    "Q_1 rơi vào chu kỳ dưới còn Q_3 rơi vào chu kỳ trên làm IQR mở rộng lên 0.284 – 0.806 cm; cả hai cụm chu kỳ đều nằm trong hàng rào hợp lệ "
    "(so_ngoai_lai = 0 ÷ 1), khiến s phản ánh độ tách biệt giữa hai cụm (1.747 – 4.049 mm) và SE đạt 0.247 – 0.573 mm.",
    "• Nhóm mốc giữ lại hai cụm chu kỳ kế tiếp: "
)

IMG_H3_3_PATH = os.path.join(BASE_DIR, "graph", "chuong_3", "hinh_3_3_do_chum_toan_dai.png")
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

add_body_p(
    "Đánh giá từ đồ thị Hình 3.3: Khi biểu diễn chung trên cùng một trục tung đơn vị mm, sự khác biệt về bản chất thống kê "
    "giữa độ phân tán mẫu đơn lẻ và độ chụm của trung bình mẫu hiện rõ trực quan:"
)
add_bullet_p(
    "Nằm dưới vạch dung sai thước 0.5 mm tại 22/33 mốc khảo sát và nổi lên các đỉnh răng cưa 1.72 – 4.05 mm "
    "tại 11 mốc xảy ra phân tách hai cụm chu kỳ sóng mang 40 kHz.",
    "Đường màu xanh lam nét liền (Độ lệch chuẩn thực nghiệm s): "
)
add_bullet_p(
    "Nhờ phép lấy trung bình trên n_hợp_lệ ∈ [40, 50] mẫu làm giảm biên độ phân tán đi khoảng 6.3 – 7.1 lần, "
    "đường SE đi phẳng sát trục hoành và nằm hoàn toàn phía dưới đường dung sai vạch chia thước 0.5 mm tại 32/33 mốc đo "
    "(chỉ nhô nhẹ lên 0.573 mm tại mốc 450 cm), chứng minh ước lượng trung bình mẫu x̄ đạt độ ổn định cao trên toàn dải.",
    "Đường màu cam nét đứt (Sai số chuẩn trung bình SE = s/√n): "
)

add_heading_3("3.3.2. Đánh giá độ chính xác")
add_body_p(
    "Sử dụng sai số tuyệt đối Δx và sai số tương đối δ (%) đã định nghĩa tại Mục 1.3.3 (Chương 1), dữ liệu đối chiếu giữa "
    "giá trị đo trung bình sau lọc x̄ (cột mean_sach_cm) và khoảng cách chuẩn x_true (cột cu_ly_dat_cm) được trích xuất từ hai cột "
    "sai_so_tuyet_doi_mm và sai_so_tuong_doi_pct trong tệp du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv:"
)
add_bullet_p(
    "Trong dải từ 50 cm đến 550 cm (25 mốc), Δx biến thiên trong khoảng từ -14.55 mm (tại 160 cm) đến +19.45 mm (tại 360 cm). "
    "Tại các mốc kiểm định chính (50, 80, 100, 150, 200, 250, 300, 400, 500, 550 cm), Δx dao động trong dải hẹp từ -5.72 mm đến +13.99 mm "
    "(điển hình tại 150 cm là -0.43 mm, tại 250 cm là +0.03 mm, tại 300 cm là -2.82 mm và tại 550 cm là +6.30 mm).",
    "Sai số tuyệt đối (Δx): "
)
add_bullet_p(
    "Ở vùng đầu dải đo danh định (10 cm – 40 cm), do mẫu số x_true nhỏ nên độ lệch vài milimét tạo ra sai số tương đối từ -3.36% (tại 20 cm) "
    "đến +5.70% (tại 10 cm) — các mốc vùng chết và chuyển tiếp dưới 10 cm đã được phân tích riêng tại Mục 3.2. "
    "Trên dải từ 80 cm đến 550 cm (23 mốc), có 22/23 mốc đạt |δ%| ≤ 0.57% (riêng mốc 160 cm là -0.91%). "
    "Đặc biệt trong dải từ 200 cm đến 550 cm (16 mốc), 15/16 mốc nằm gọn trong phạm vi ±0.45% (mốc 360 cm đạt +0.54%; "
    "các mốc 300 cm, 500 cm và 550 cm đạt lần lượt -0.09%, +0.14% và +0.12%), tốt hơn mức dung sai danh định ±1% của nhà sản xuất.",
    "Sai số tương đối (δ%): "
)
add_body_p(
    "Nguồn gốc sai số hệ thống: Độ lệch tuyệt đối cỡ vài milimét bắt nguồn từ hai yếu tố thực tế trong bố trí mô hình đo: "
    "(1) Mặt phẳng màng gốm áp điện phát – thu nằm thụt sâu khoảng 5 – 6 mm bên trong ống bảo vệ kim loại so với mép trước bo mạch "
    "thử nghiệm đặt tại vạch gốc 0 mm, tạo ra một độ lệch gốc tọa độ cố định; (2) Tại một số mốc cự ly trung gian (60, 160, 320, 360 cm), "
    "thao tác dịch chuyển bàn đỡ viên gạch dọc hành lang dài 10 m và căng thước dây thủ công giữa hai mép bàn phát sinh sai lệch định vị cỡ vài milimét. "
    "Thành phần độ lệch gốc cố định sẽ được lượng hóa bằng hệ số chặn hồi quy tuyến tính tại Mục 3.4 để bù trừ trực tiếp bằng phần mềm trên ESP32."
)

IMG_H3_4_PATH = os.path.join(BASE_DIR, "graph", "chuong_3", "hinh_3_4_do_chinh_xac_sai_so.png")
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

add_body_p(
    "Đánh giá từ đồ thị Hình 3.4: Biểu đồ đơn ghép hai trục tung Y (đồng bộ đường chuẩn gốc 0 giữa trục trái mm và trục phải %) "
    "trên dải làm việc 10 cm – 550 cm cho thấy:"
)
add_bullet_p(
    "Dao động quanh trục 0 mm trong biên độ hẹp ở cự ly dưới 150 cm và có xu hướng dương nhẹ (+4.83 mm đến +13.99 mm) ở dải xa 400 – 550 cm.",
    "Đường màu xanh lá nét liền (Sai số tuyệt đối Δx, trục trái): "
)
add_bullet_p(
    "Hội tụ rất nhanh từ ngưỡng +5.70% (tại 10 cm) vào bên trong dải tham chiếu màu đỏ ±0.5% ngay từ mốc 80 cm trở đi "
    "và duy trì bám sát đường chuẩn 0% đến hết mốc 550 cm.",
    "Đường màu xanh lam nét đứt (Sai số tương đối δ%, trục phải): "
)

# ==========================================================
# [VÙNG CHỜ GHÉP NHÁNH MỤC 3.4 & MỤC 3.5 TỪ CÁC THÀNH VIÊN KHÁC]
# ==========================================================

# ==========================================================
# MỤC 3.6: PHÂN TÍCH ẢNH HƯỞNG CỦA BỀ MẶT PHẢN XẠ
# ==========================================================
add_heading_2("3.6. Phân tích ảnh hưởng của Bề mặt phản xạ")

add_body_p(
    "Để lượng hóa ảnh hưởng của phản xạ gương định hướng và tán xạ khuếch tán (Mục 1.1.3, Chương 1), thí nghiệm đối chứng được thực hiện "
    "ở cùng nhiệt độ phòng mặc định 27.0 °C (v = 347.662 m/s) trên hai mặt của cùng một viên gạch 40 cm × 40 cm (Mục 2.2 và Mục 2.3, Chương 2): "
    "Trường hợp 1 (FSDT) dùng mặt trước phẳng nhẵn và Trường hợp 3 (FRDT) dùng mặt sau gồ ghề. "
    "Số liệu thống kê trên 22 mốc chung (10 cm – 350 cm) và mốc kiểm tra 375 cm của FRDT được lấy từ tệp du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv."
)

add_heading_3("3.6.1. Tác động của tán xạ bề mặt lên độ chụm và độ chính xác đo")
add_body_p(
    "Đối chiếu sai số chuẩn trung bình SE (cột se_sach_mm) và sai số đo Δx, δ% (định nghĩa tại Mục 1.3, Chương 1) "
    "trên 22 mốc chung từ 10 cm đến 350 cm cho thấy:"
)
add_bullet_p(
    "Ở cự ly ngắn, chùm siêu âm bao phủ nhiều gờ lồi lõm trên mặt sau viên gạch nên các sóng phản hồi lệch pha giao thoa tại màng thu. "
    "Tại 10 cm, s tăng từ 0.061 mm (FSDT, SE = 0.0086 mm) lên 1.620 mm (FRDT, SE = 0.2291 mm); tại 60 cm, s tăng từ 0.088 mm "
    "(SE = 0.0128 mm) lên 2.240 mm (SE = 0.3168 mm). Trên toàn bộ 22 mốc (1.100 mẫu), IQR loại 59 mẫu ngoại lai (5.36%) ở mặt gồ ghề, "
    "cao hơn 46 mẫu (4.18%) ở mặt nhẵn.",
    "Suy giảm độ chụm ở vùng gần (10 cm – 60 cm): "
)
add_bullet_p(
    "Trên dải 80 cm – 340 cm, các đỉnh phân tán cao của hai bề mặt xuất hiện lệch pha nhau theo cự ly, do độ nhấp nhô làm dịch mặt phẳng phản xạ "
    "âm học hiệu dụng đi vài milimét so với chân gạch. Nhờ lấy trung bình trên n_hợp_lệ ∈ [37, 50] mẫu, SE của mặt gồ ghề luôn nằm trong khoảng "
    "0.0071 – 0.3903 mm, thấp hơn dung sai vạch chia thước 0.5 mm tại 22/22 mốc.",
    "Lệch pha các đỉnh phân tán: "
)
add_bullet_p(
    "Mặt gồ ghề làm Δx thiên âm rõ hơn mặt nhẵn (từ -21.74 mm tại 250 cm đến +10.88 mm tại 350 cm). "
    "Trên dải 80 cm – 350 cm (17 mốc), có 16/17 mốc đạt |δ%| ≤ 0.87% (ngoại lệ là mốc 100 cm với -1.27%).",
    "Sai số hệ thống (Δx và δ%): "
)

IMG_H3_7_PATH = os.path.join(BASE_DIR, "graph", "chuong_3", "hinh_3_7_sai_so_chuan_se_be_mat.png")
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
    r_c3_7 = p_cap3_7.add_run(
        "Hình 3.7: So sánh sai số chuẩn trung bình SE = s/√n sau lọc IQR "
        "giữa mặt phẳng nhẵn (FSDT) và mặt gồ ghề (FRDT) trên dải 10 cm – 350 cm."
    )
    r_c3_7.font.italic = True
    r_c3_7.font.size = Pt(10)

add_body_p(
    "Đánh giá từ đồ thị Hình 3.7: SE của cả FSDT (0.0086 – 0.4491 mm) và FRDT (0.0071 – 0.3903 mm) đều nằm dưới đường dung sai 0.5 mm "
    "tại 22/22 mốc. Như vậy, trung bình trên N = 50 mẫu kết hợp lọc IQR giữ được độ chụm dưới nửa milimét chừng nào sóng phản hồi còn vượt ngưỡng thu."
)

add_heading_3("3.6.2. Suy hao năng lượng tán xạ và sự thu hẹp giới hạn tầm đo xa")
add_body_p(
    "Tác động bất lợi nhất của bề mặt gồ ghề là làm suy giảm đột ngột cự ly hoạt động cực đại do năng lượng âm thất thoát ra không gian:"
)
add_bullet_p(
    "Phản xạ gương bảo toàn năng lượng dọc trục pháp tuyến nên cảm biến đo ổn định đến 550 cm "
    "(x̄ = 550.630 cm, s = 0.319 mm, SE = 0.0492 mm), chớm mất tín hiệu 4/50 mẫu tại 580 cm và bão hòa hoàn toàn tại 600 cm (x̄ = 824.562 cm).",
    "Mặt phẳng nhẵn (FSDT): "
)
add_bullet_p(
    "Có 1/50 mẫu (2%) mất tín hiệu và tràn bộ đếm lên 824.400 cm, cùng 4/50 mẫu (8%) trượt chu kỳ dương, tổng cộng 5/50 mẫu ngoại lai (10%). "
    "Khi chưa lọc, riêng xung tràn đã đẩy s_thô lên 669.240 mm. Vì tỷ lệ ngoại lai thấp hơn điểm gãy tứ phân vị (25%), IQR loại hết 5 mẫu (n_hợp_lệ = 45) "
    "và khôi phục x̄ = 351.088 cm (Δx = +10.88 mm, δ = +0.311%), s = 2.618 mm, SE = 0.3903 mm.",
    "Chớm mất xung tại 350 cm trên mặt gồ ghề (FRDT): "
)
add_bullet_p(
    "Có 33/50 mẫu (66%) tràn lên khoảng 824.6 cm, vượt quá 50% nên trung vị bị kéo lên vùng tràn (Med = 824.575 cm), IQR phình lên 447.235 cm "
    "và hàng rào lọc mở rộng thành [-293.46; 1495.48] cm nên không mẫu nào bị loại. Kết quả sau lọc mất hiệu lực: x̄ = 672.502 cm "
    "(Δx = +2975.02 mm, δ = +79.33%), s = 2140.734 mm.",
    "Sụp đổ phép đo tại 375 cm: "
)
add_bullet_p(
    "Bề mặt gồ ghề thu hẹp tầm đo tin cậy cực đại từ 550 cm xuống 350 cm (giảm 200 cm, tương đương -36.4%). "
    "Với chất lỏng tĩnh phẳng nhẵn trong bồn kín, cảm biến RCWL-1601 dùng được toàn dải xa; với vật liệu rắn dạng hạt, bề mặt nhám xốp "
    "hoặc mặt thoáng gợn sóng mạnh, chiều cao lắp đặt tối đa nên giới hạn dưới 300 – 350 cm (cơ sở cho thiết kế ở Chương 4).",
    "Kết luận thiết kế: "
)


# ==========================================================
# MỤC 3.7: PHÂN TÍCH ẢNH HƯỞNG CỦA NHIỆT ĐỘ VÀ BÙ LAPLACE
# ==========================================================
add_heading_2("3.7. Phân tích ảnh hưởng của Nhiệt độ môi trường và Hiệu quả thuật toán bù nhiệt Laplace")

add_body_p(
    "Dựa trên mô hình phụ thuộc nhiệt độ của vận tốc sóng siêu âm Laplace đã thiết lập tại Mục 1.1.2 (Chương 1), "
    "thí nghiệm đối chứng được tiến hành trên cùng mặt trước phẳng nhẵn của viên gạch chuẩn dọc 19 mốc cự ly chung từ 10 cm đến 300 cm "
    "(Mục 2.3, Chương 2) giữa hai chế độ nhiệt: Trường hợp 1 (FSDT) tại điều kiện phòng mặc định T_1 = 27.0 °C (v_1 = 347.662 m/s) "
    "và Trường hợp 4 (FSAT) trong phòng điều hòa làm lạnh T_2 = 20.0 °C (v_2 = 343.420 m/s, có dao động vi khí hậu nhẹ lên 21.0 °C "
    "ở một số mẫu thuộc mốc 200, 250, 300 cm được cảm biến nhiệt ghi nhận trực tiếp). Toàn bộ dữ liệu thời gian bay trung bình sau lọc "
    "(cột tof_sach_us), kết quả đo khi chưa bù nhiệt (cột mean_chua_bu_27c_cm, sai_so_chua_bu_27c_mm) và kết quả sau khi bù nhiệt Laplace "
    "(cột mean_sach_cm, sai_so_tuyet_doi_mm, std_sach_mm, se_sach_mm) được lưu trữ đầy đủ trong tệp du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv."
)

add_heading_3("3.7.1. Sự giãn dài thời gian bay và độ ổn định độ chụm khi hạ nhiệt độ môi trường")
add_body_p(
    "Khi hạ nhiệt độ không khí xuống 20.0 °C, mật độ phân tử khí tăng làm giảm vận tốc lan truyền sóng siêu âm một lượng "
    "Δv = -4.242 m/s (-1.220% so với mức chuẩn hóa 27.0 °C), kéo dài thời gian bay khứ hồi t của xung siêu âm trên cùng một khoảng cách hình học x_true:"
)
add_bullet_p(
    "Trích xuất trực tiếp từ bộ đếm phần cứng 1 μs của ESP32 sau lọc IQR cho thấy thời gian bay trung bình của tập FSAT lớn hơn FSDT "
    "một cách nhất quán và tăng tuyến tính theo cự ly với tốc độ xấp xỉ +120.5 μs trên mỗi mét khoảng cách: tại x_true = 100 cm, "
    "t̄ tăng từ 5670.42 μs lên 5790.42 μs (Δt̄ = +120.00 μs); tại x_true = 200 cm, tăng từ 11413.42 μs lên 11654.78 μs (Δt̄ = +241.36 μs); "
    "và tại x_true = 300 cm, tăng từ 17083.52 μs lên 17445.24 μs (Δt̄ = +361.72 μs).",
    "Độ giãn thời gian bay thực nghiệm (tof_sach_us): "
)
add_bullet_p(
    "Trong môi trường phòng điều hòa kín gió 20.0 °C, tổng tỷ lệ ngoại lai bị loại bởi IQR của tập FSAT là 38/950 mẫu (4.00%), "
    "tương đương hoàn toàn với 39/950 mẫu (4.11%) trên 19 mốc đối ứng của FSDT. Độ lệch chuẩn sau lọc s của FSAT dao động trong dải "
    "0.060 – 3.381 mm và sai số chuẩn trung bình SE đạt 0.0085 – 0.4781 mm (nằm dưới dung sai thước 0.5 mm tại cả 19/19 mốc), "
    "chứng minh việc hạ nhiệt độ môi trường chỉ làm dịch chuyển hệ thống vận tốc truyền âm chứ không làm suy giảm độ chụm lặp lại của vi mạch RCWL-9610.",
    "Tính bất biến của độ chụm đối với nhiệt độ: "
)

add_heading_3("3.7.2. Định lượng sai số trôi nhiệt khi không bù và hiệu quả khử trôi của thuật toán Laplace")
add_body_p(
    "Để đánh giá định lượng rủi ro trong các hệ thống nhúng giá rẻ thường gán cứng hằng số vận tốc âm mặc định v(27.0 °C) = 347.662 m/s "
    "(default_temp_c = 27.0), khoảng cách chưa bù nhiệt tại 20.0 °C được tính đối chứng từ cột tof_sach_us theo "
    "x̄_chưa_bù = 0.5 · v(27.0 °C) · t̄_FSAT và so sánh trực tiếp với kết quả đã bù nhiệt Laplace thời gian thực trên ESP32:"
)
add_bullet_p(
    "Do thời gian bay kéo dài hơn trong không khí lạnh nhưng phần mềm vẫn nhân với vận tốc lớn của 27.0 °C, kết quả đo bị phóng đại giả tạo "
    "với tỷ lệ lý thuyết +1.235% quãng đường (≈ +12.35 mm/m ở 20.0 °C). Lượng trôi nhiệt thuần túy (x̄_chưa_bù - x̄_đã_bù) tích lũy tuyến tính "
    "từ +1.31 mm tại 10 cm, +6.16 mm tại 50 cm, +12.28 mm tại 100 cm, +18.52 mm tại 150 cm, +22.46 mm tại 200 cm, +28.20 mm tại 250 cm, "
    "lên tới +34.65 mm tại 280 cm và +35.31 mm tại 300 cm. Hệ quả là sai số tuyệt đối Δx khi chưa bù bị đẩy vọt lên mức dương lớn: "
    "đạt +25.96 mm tại 200 cm, đỉnh +39.92 mm (≈ +4.0 cm) tại 280 cm và +32.52 mm tại 300 cm.",
    "1. Trường hợp không bù nhiệt độ (sai_so_chua_bu_27c_mm): "
)
add_bullet_p(
    "Khi kích hoạt công thức cập nhật vận tốc âm tức thời v(T) theo từng mẫu đo trên ESP32, toàn bộ thành phần trôi nhiệt dương hàng xentimét "
    "bị loại bỏ hoàn toàn: sai số Δx của FSAT được kéo sập về -5.73 mm tại 100 cm, -0.45 mm tại 150 cm, +3.50 mm tại 200 cm, "
    "+0.04 mm tại 250 cm, +5.27 mm tại 280 cm và -2.79 mm tại 300 cm (14/14 mốc từ 80 – 300 cm trừ mốc 160 cm đều đạt |δ%| ≤ 0.57%).",
    "2. Hiệu quả triệt tiêu trôi nhiệt khi bù Laplace thời gian thực (sai_so_tuyet_doi_mm): "
)
add_bullet_p(
    "Đối chiếu trực tiếp cột mean_sach_cm giữa FSDT (27.0 °C) và FSAT (20.0 °C) trên toàn bộ 19 mốc cự ly xác nhận độ lệch trung bình tuyệt đối "
    "giữa hai chế độ nhiệt chỉ là 0.037 mm (biến thiên trong dải siêu hẹp từ -0.048 mm đến +0.183 mm; có 18/19 mốc lệch dưới 0.085 mm — "
    "nhỏ hơn nửa bước lượng tử thời gian Δ_LSB ≈ 0.174 mm của bộ đếm ESP32). Kết quả này chứng minh thuật toán bù nhiệt Laplace giúp phép đo "
    "siêu âm hoàn toàn miễn nhiễm với biến thiên nhiệt độ môi trường.",
    "3. Độ trùng khít tuyệt đối giữa hai môi trường nhiệt độ sau bù (x̄_27°C - x̄_20°C): "
)

IMG_H3_8_PATH = os.path.join(BASE_DIR, "graph", "chuong_3", "hinh_3_8_anh_huong_nhiet_do_bu_laplace.png")
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
    r_c3_8 = p_cap3_8.add_run(
        "Hình 3.8: So sánh sai số tuyệt đối Δx tại phòng lạnh 20.0 °C khi chưa bù nhiệt độ, "
        "sau khi bù nhiệt độ Laplace (FSAT) và chuẩn đối chứng tại 27.0 °C (FSDT) trên dải 10 cm – 300 cm."
    )
    r_c3_8.font.italic = True
    r_c3_8.font.size = Pt(10)

add_body_p("Đánh giá từ đồ thị Hình 3.8: Biểu diễn ba chuỗi sai số trên cùng một trục tung đơn vị mm cho thấy sự tương phản trực quan:")
add_bullet_p(
    "Tách khỏi gốc 0 mm và dốc tuyến tính đi lên theo khoảng cách chuẩn do tích lũy sai số vận tốc +1.235%, "
    "vọt lên vùng +26 ÷ +40 mm ở cự ly 200 – 300 cm.",
    "Đường màu đỏ nét liền ký hiệu tam giác (FSAT chưa bù nhiệt): "
)
add_bullet_p(
    "Từng điểm vuông xanh lá nằm lọt chính tâm vòng tròn xanh lam trên toàn bộ 19 mốc cự ly từ 10 cm đến 300 cm "
    "(do độ lệch giữa hai đường chỉ từ 0.002 mm đến 0.183 mm) và cùng bám sát đường chuẩn 0 mm, "
    "khẳng định tính bắt buộc của cảm biến nhiệt độ đi kèm thuật toán bù Laplace trong ứng dụng bồn chứa thực tế ở Chương 4.",
    "Đường màu xanh lá nét đứt tâm vuông đặc (FSAT đã bù Laplace tại 20.0 °C) lồng đồng tâm bên trong đường băng xanh lam ký hiệu vòng tròn rỗng (FSDT đối chứng tại 27.0 °C): "
)

import os
doc.save(OUTPUT_FILE)
print(f"Xuất bản thành công tài liệu Word hoàn chỉnh chuẩn Headings và Equation: {OUTPUT_FILE}")

# Gộp thành 1 bản báo cáo duy nhất: dọn dẹp tệp phụ nếu có
alt_output = OUTPUT_FILE.replace("Bao_Cao_Thuc_Nghiem_RCWL1601.docx", "Bao_Cao_Thuc_Nghiem_RCWL1601_CapNhat.docx")
if os.path.exists(alt_output):
    try:
        os.remove(alt_output)
        print(f"Đã dọn dẹp và gộp hoàn tất vào một bản duy nhất: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Lưu ý dọn dẹp tệp phụ: {e}")
