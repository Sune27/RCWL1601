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
IMG_CH2_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\graph\bieu_do_chot_N50_student_t95.png"

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
    return doc.add_heading(text, level=1)

def add_heading_2(text):
    return doc.add_heading(text, level=2)

def add_heading_3(text):
    return doc.add_heading(text, level=3)

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
doc.add_heading("LỜI NÓI ĐẦU", level=1)

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
    "khảo sát chi tiết vùng chết (1 cm – 3 cm), dải đo xa mở rộng vượt định mức (lên đến 550 cm), độ chụm (độ lệch chuẩn, hệ số biến thiên), "
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
doc.add_heading("MỤC LỤC", level=1)

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
doc.add_heading("BẢNG QUY ƯỚC KÝ HIỆU VÀ CẤU TRÚC DỮ LIỆU THỰC NGHIỆM", level=1)

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
    "vận tốc sóng âm sẽ biến thiên khoảng 7.27 m/s (2.12%). Nếu hệ thống sử dụng vận tốc cố định, sai số đo khoảng cách sẽ trôi lũy tiến "
    "theo cự ly đo, đạt tới hàng chục milimét ở cự ly trên 2 m. Do đó, việc đo nhiệt độ môi trường thời gian thực để bù trừ vận tốc v(T) "
    "là yêu cầu kỹ thuật bắt buộc."
)

add_heading_3("1.1.3. Sự suy hao năng lượng sóng âm theo cự ly đo")
add_body_p("Năng lượng và biên độ áp suất âm p(d) của sóng âm suy giảm mạnh theo khoảng cách truyền dẫn do hai cơ chế vật lý song song:")
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
add_body_p("Module RCWL-1601 giao tiếp với vi điều khiển ESP32 thông qua giao thức xung kỹ thuật số hai chân (Trigger và Echo):")
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
    ("Điện áp hoạt động (V_CC)", "2.8 V – 5.5 V (Một chiều - DC)", "Tương thích hoàn toàn mức logic 3.3V của ESP32"),
    ("Dòng điện tiêu thụ tĩnh", "< 2 mA", "Thích hợp cho các trạm quan trắc năng lượng thấp"),
    ("Dòng điện cực đại khi phát", "≈ 15 mA – 20 mA", "Tiêu thụ xung tức thời trong 200 μs khi phát sóng"),
    ("Tần số sóng siêu âm", "40 kHz ± 1.0 kHz", "Tối ưu hóa giữa độ định hướng và suy hao không khí"),
    ("Dải đo danh định công bố", "2 cm – 400 cm (hoặc 450 cm)", "Độ chính xác cao nhất trên bề mặt phẳng nhẵn"),
    ("Độ phân giải lý thuyết", "1 mm", "Phụ thuộc độ phân giải bộ đếm thời gian vi điều khiển"),
    ("Góc mở chùm sóng âm", "≈ 15°", "Góc mở hình nón của mặt sóng phát xạ"),
    ("Tín hiệu kích hoạt (TRIG)", "Xung mức CAO (HIGH) ≥ 10 μs", "Tương thích logic TTL / CMOS 3.3V"),
    ("Tín hiệu phản hồi (ECHO)", "Độ rộng xung mức CAO (PWM)", "Độ rộng xung tỷ lệ thuận với khoảng cách đo")
]

table_ds = doc.add_table(rows=len(ds_data)+1, cols=3)
table_ds.alignment = WD_TABLE_ALIGNMENT.CENTER
table_ds.autofit = False

ds_widths = [Cm(5.0), Cm(5.0), Cm(6.0)]
ds_headers = ["Thông số kỹ thuật", "Giá trị công bố (Datasheet)", "Đánh giá & Ý nghĩa kỹ thuật"]

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
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx == 0 else (WD_ALIGN_PARAGRAPH.CENTER if col_idx == 1 else WD_ALIGN_PARAGRAPH.JUSTIFY)
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

add_bullet_p("Đại diện cho mức độ phân tán ngẫu nhiên của các giá trị đo quanh giá trị trung bình:", "• Độ lệch chuẩn mẫu thực nghiệm (Sample Standard Deviation): ")

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

add_bullet_p("Giá trị chia đôi tập dữ liệu đã sắp xếp thứ tự: Med = x_((N+1)/2) với N lẻ. Giá trị trung vị có tính chất thống kê bền vững (Robust Statistics), hoàn toàn không bị ảnh hưởng bởi các xung nhiễu đột biến cực đoan.", "• Giá trị trung vị mẫu (Median): ")

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

add_body_p("Hàng rào dưới (Lower Fence) và Hàng rào trên (Upper Fence) được xác định theo:")

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
add_bullet_p("Phản ánh độ ổn định tương đối của phép đo, chuẩn hóa độ lệch chuẩn theo giá trị trung bình: CV% = (s / x̄) · 100%.", "1. Hệ số biến thiên (Coefficient of Variation): ")
add_bullet_p("Đánh giá mức độ sai lệch giữa giá trị đo trung bình và giá trị chuẩn: Sai số tuyệt đối Δd = d̄ - d_true; Sai số tương đối δ% = (Δd / d_true) · 100%.", "2. Sai số đo lường:", )
add_bullet_p("Tỷ số giữa độ biến thiên tín hiệu đầu ra và độ biến thiên đại lượng đo đầu vào: S_t = Δt / Δd_true (μs/cm).", "3. Độ nhạy (Sensitivity): ")
add_bullet_p(
    "Đánh giá mức độ bám sát của đặc tính tĩnh thực nghiệm với đường thẳng lý thuyết ŷ = a · x + b. "
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
    "Hệ số xác định tương quan R² = 1 - [∑(y_k - ŷ_k)² / ∑(y_k - ȳ)²]. "
    "Sai số phi tuyến cực đại: δ_NL% = (max_k |d̄_k - d̂_k| / d_FS) · 100%."
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
    "Theo hướng dẫn quốc tế ISO/IEC Guide 98-3 (GUM), độ tin cậy của kết quả đo được lượng hóa qua ngân sách độ không đảm bảo đo toàn diện:"
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

add_heading_1("CHƯƠNG 2: THIẾT KẾ VÀ BỐ TRÍ HỆ THỐNG THỰC NGHIỆM")

# 2.1
add_heading_2("2.1. MỤC TIÊU VÀ PHƯƠNG PHÁP LUẬN THỰC NGHIỆM")

add_heading_3("2.1.1. Mục tiêu thực nghiệm")
add_body_p(
    "Nghiên cứu thực nghiệm được thiết kế nhằm mục đích kiểm chứng khoa học và định lượng hóa các đặc tính đo lường "
    "của module cảm biến siêu âm RCWL-1601 trên nền tảng vi điều khiển ESP32 với các mục tiêu trọng tâm:"
)
add_bullet_p("Xác định dải đo tuyến tính ổn định, khảo sát chi tiết vùng chết (1 cm – 3 cm), kiểm tra giới hạn đo xa cực đại vượt định mức (lên đến 550 cm), và ngưỡng bão hòa timeout (580 cm – 600 cm).", "1. Khảo sát dải đo thực tế: ")
add_bullet_p("Đánh giá độ lặp lại (độ lệch chuẩn thực nghiệm s, hệ số biến thiên CV%), sai số tuyệt đối và sai số tương đối trên toàn dải đo.", "2. Định lượng độ chụm và độ chính xác: ")
add_bullet_p("Xác định hàm truyền thời gian bay ToF theo khoảng cách, tìm hệ số góc độ nhạy thực tế St (μs/cm) và đối chiếu với mô hình lý thuyết Laplace.", "3. Đánh giá độ nhạy và độ tuyến tính: ")
add_bullet_p("Định lượng sai số trôi cự ly do vận tốc sóng âm khi nhiệt độ phòng thay đổi từ 27.0 °C xuống 20.0 °C, chứng minh hiệu quả triệt tiêu sai số của thuật toán bù nhiệt độ Laplace.", "4. Đánh giá ảnh hưởng của nhiệt độ môi trường: ")
add_bullet_p("So sánh đặc tính phản xạ gương (mặt phẳng nhẵn) và tán xạ khuếch tán (mặt gồ ghề nhấp nhô) ảnh hưởng đến độ chụm và cự ly cực đại.", "5. Đánh giá ảnh hưởng của bề mặt phản xạ: ")
add_bullet_p("Đánh giá sự bất đối xứng của hàm truyền khi di chuyển bia phản xạ theo chiều tiến và chiều lùi.", "6. Đánh giá độ trễ (Hysteresis): ")

add_heading_3("2.1.2. Phương pháp luận thực nghiệm")
add_body_p(
    "Để đảm bảo tính khách quan và khả năng tái lập của kết quả đo, nghiên cứu áp dụng phương pháp luận đo lường chuẩn hóa:"
)
add_bullet_p("Sử dụng giàn ray trượt quang cơ khí dài 7 m có vạch chia milimét tiêu chuẩn (độ không đảm bảo đo u_B1 = 0.289 mm) làm chuẩn chiều dài đối chứng.", "• Phương pháp đo so sánh trực tiếp: ")
add_bullet_p("Tại mỗi mốc cự ly chuẩn, thực hiện lặp lại N lần đo độc lập trong điều kiện môi trường ổn định để đánh giá độ phân tán ngẫu nhiên và tính toán độ không đảm bảo đo Loại A (u_A).", "• Phương pháp đo lặp thống kê: ")
add_bullet_p("Nhiệt độ môi trường phòng thực nghiệm được giám sát liên tục bằng nhiệt kế điện tử chuẩn (độ chính xác ±0.5 °C). Dữ liệu nhiệt độ được ghi nhận đồng bộ vào từng mẫu đo để áp dụng thuật toán bù vận tốc sóng âm Laplace.", "• Phương pháp kiểm soát và bù trừ điều kiện môi trường: ")
add_bullet_p("Toàn bộ dữ liệu thô (thời gian bay t, cự ly đo d, nhiệt độ T) được ESP32 truyền về máy tính qua giao tiếp nối tiếp UART với tốc độ 115200 bps, tự động ghi lưu thành các tệp định dạng CSV để triệt tiêu hoàn toàn sai số chủ quan của con người.", "• Phương pháp thu thập dữ liệu tự động hóa: ")

# 2.2
add_heading_2("2.2. THIẾT KẾ PHẦN CỨNG, MÔ HÌNH GÁ ĐẶT VÀ KHÔNG GIAN THỰC NGHIỆM")

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
    ("VCC", "3V3 (ESP32)", "Cấp nguồn nuôi cảm biến", "3.3 V DC (Dòng tĩnh < 3 mA)"),
    ("GND", "GND (ESP32)", "Nối đất chung hệ thống", "0 V (Mass tham chiếu)"),
    ("TRIG", "GPIO 5 (ESP32)", "Ngõ vào kích phát xung siêu âm", "Mức logic 3.3 V (Xung kích ≥ 10 μs)"),
    ("ECHO", "GPIO 18 (ESP32)", "Ngõ ra phản hồi thời gian bay ToF", "Mức logic 3.3 V (Độ rộng xung tỷ lệ thuận ToF)")
]

table_pin = doc.add_table(rows=len(pin_data)+1, cols=4)
table_pin.alignment = WD_TABLE_ALIGNMENT.CENTER
table_pin.autofit = False

pin_widths = [Cm(3.0), Cm(3.5), Cm(5.5), Cm(4.0)]
pin_headers = ["Chân RCWL-1601", "Chân ESP32", "Chức năng kỹ thuật", "Ghi chú mức điện áp"]

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
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in (0, 1) else (WD_ALIGN_PARAGRAPH.LEFT if col_idx == 2 else WD_ALIGN_PARAGRAPH.CENTER)
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

add_heading_3("2.2.2. Thiết kế mô hình gá đặt cơ khí")
add_body_p(
    "Để đảm bảo độ chính xác cơ học và khả năng định vị chuẩn dọc theo hành trình 6 m, hệ thống gá đặt thực nghiệm được thiết kế bao gồm:"
)
add_bullet_p("Được ghép từ các thanh ray nhôm định hình chuẩn có độ võng nhỏ hơn 0.5 mm trên chiều dài 2 m, đặt thẳng hàng tuyệt đối. Dọc theo ray có dán thước thép đo khoảng cách chuẩn chiều dài 7 m, độ chia nhỏ nhất 1 mm.", "1. Ray trượt dẫn hướng chiều dài 7 m: ")
add_bullet_p("Cảm biến RCWL-1601 được gá cố định tại mốc tọa độ x = 0 cm. Mặt phẳng hai mắt phát - thu gốm áp điện được căn chỉnh vuông góc 90° so với trục dọc của ray trượt bằng bọt thủy nivo quang học và thước đo góc vuông laser.", "2. Giá đỡ cảm biến chuẩn tọa độ gốc: ")
add_bullet_p("Tấm bia phản xạ kích thước 30 cm × 40 cm (đảm bảo bao trùm hoàn toàn diện tích đáy của búp sóng siêu âm 15° ở cự ly xa) được gắn vuông góc trên con trượt cơ khí. Con trượt trang bị con trỏ chỉ vạch cơ khí có độ dày mũi trỏ < 0.2 mm, kết hợp chốt hãm vít ren giúp khóa chặt vị trí tại từng mốc cự ly đặt.", "3. Cụm bia phản xạ trượt di động: ")

add_heading_3("2.2.3. Thiết kế không gian và kiểm soát điều kiện môi trường thực nghiệm")
add_body_p(
    "Đặc tính sóng siêu âm có góc mở búp sóng hình nón 15° đòi hỏi không gian đo phải được tính toán cẩn trọng để loại trừ các phản xạ phụ:"
)
add_bullet_p("Bán kính vùng nón sóng âm phát triển theo khoảng cách: R_cone(d) = d · tan(7.5°). Tại cự ly đo lớn nhất d = 6.0 m, bán kính búp sóng đạt R_cone ≈ 0.79 m (đường kính vệt sóng ≈ 1.58 m).", "• Vùng bao sóng âm: ")
add_bullet_p("Toàn bộ giàn ray trượt và cảm biến được đặt trên hệ giá đỡ nâng cao H_shelf = 75.0 cm so với mặt sàn phòng thí nghiệm. Thiết kế độ cao 75 cm đảm bảo ở cự ly đo đến 5.5 m, mép dưới của búp sóng 15° vẫn chưa chạm tới mặt sàn, triệt tiêu hoàn toàn phản xạ phụ từ sàn nhà vào đầu thu.", "• Thiết kế chiều cao nâng kệ H_shelf = 75 cm: ")
add_bullet_p("Thực nghiệm được bố trí dọc theo hành lang kín gió dài 10 m, chiều rộng 2.8 m. Cảm biến đặt cách tường bên ít nhất 1.4 m để tránh sóng dội thành vách. Trong suốt quá trình đo, hệ thống cửa được đóng kín để duy trì vi khí hậu ổn định, tránh gió lùa và biến thiên nhiệt độ đột ngột.", "• Kiểm soát vi khí hậu phòng đo: ")

# 2.3
add_heading_2("2.3. THIẾT KẾ MA TRẬN KỊCH BẢN THỰC NGHIỆM")
add_body_p(
    "Để đánh giá đầy đủ, độc lập và toàn diện các đặc tính kỹ thuật, nghiên cứu thiết lập ma trận thực nghiệm gồm 4 kịch bản đo lường chuyên biệt:"
)

p_tbl2 = doc.add_paragraph()
p_tbl2.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_tbl2.paragraph_format.space_after = Pt(4)
r_t2 = p_tbl2.add_run("Bảng 2.2: Ma trận 4 kịch bản khảo sát thực nghiệm tổng thể của đề tài")
r_t2.font.name = 'Times New Roman'
r_t2.font.size = Pt(12)
r_t2.font.bold = True

sc_data = [
    ("Bề mặt phản xạ", "Phẳng nhẵn (Tấm composite)", "Phẳng nhẵn (Tấm composite)", "Nhám gồ ghề (Tấm bìa bọc xốp)", "Phẳng nhẵn (Tấm composite)"),
    ("Chiều di chuyển", "Tiến (1 cm → 600 cm)", "Lùi (300 cm → 10 cm)", "Tiến (10 cm → 375 cm)", "Tiến (10 cm → 300 cm)"),
    ("Số lượng mốc đo", "35 mốc cự ly", "19 mốc cự ly đối ứng", "23 mốc cự ly", "19 mốc cự ly đối ứng"),
    ("Nhiệt độ môi trường", "27.0 °C (Nhiệt độ phòng)", "27.0 °C (Nhiệt độ phòng)", "27.0 °C (Nhiệt độ phòng)", "20.0 °C (Bật điều hòa lạnh)"),
    ("Số lần đo lặp N", "50 mẫu / mốc", "50 mẫu / mốc", "50 mẫu / mốc", "50 mẫu / mốc"),
    ("Tổng số mẫu đo", "1.750 mẫu dữ liệu", "950 mẫu dữ liệu", "1.150 mẫu dữ liệu", "950 mẫu dữ liệu"),
    ("Mục đích nghiên cứu", "Khảo sát toàn dải, vùng chết, độ chụm, độ chính xác, độ nhạy ToF", "Đối chứng với FSDT để xác định Độ trễ đo (Hysteresis)", "Đánh giá ảnh hưởng tán xạ khuếch tán bề mặt nhám", "Định lượng độ trôi nhiệt độ và kiểm chứng bù Laplace")
]

table_sc = doc.add_table(rows=len(sc_data)+1, cols=5)
table_sc.alignment = WD_TABLE_ALIGNMENT.CENTER
table_sc.autofit = False

sc_widths = [Cm(3.2), Cm(3.2), Cm(3.2), Cm(3.2), Cm(3.2)]
sc_headers = ["Tham số khảo sát", "Kịch bản 1: FSDT (Chuẩn)", "Kịch bản 2: BSDT (Trễ)", "Kịch bản 3: FRDT (Nhám)", "Kịch bản 4: FSAT (Nhiệt)"]

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
add_heading_2("2.4. CƠ SỞ THỐNG KÊ VÀ THỰC NGHIỆM XÁC ĐỊNH CỠ MẪU TỐI ƯU N = 50")

add_heading_3("2.4.1. Cơ sở lý thuyết đường cong hội tụ Student 95%")
add_body_p(
    "Trong đo lường thực nghiệm, việc lựa chọn số lần đo lặp N là bài toán tối ưu hóa đa mục tiêu giữa độ chính xác thống kê "
    "và thời gian đáp ứng thời gian thực. Theo lý thuyết xác suất thống kê và tiêu chuẩn ISO/GUM, khi số lần đo k tăng dần (k = 2, 3, ..., N), "
    "bán kính khoảng tin cậy mở rộng tại mức tin cậy 95% được xác định theo phân bố Student:"
)

# Native Word Equation 2.1: epsilon_95 = t_0.975 * (s / sqrt(k))
add_native_equation(
    '<m:sSub><m:e><m:r><m:t>ε</m:t></m:r></m:e><m:sub><m:r><m:t>95%</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(k) = </m:t></m:r>'
    '<m:sSub><m:e><m:r><m:t>t</m:t></m:r></m:e><m:sub><m:r><m:t>0.975</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(k - 1) · </m:t></m:r>'
    '<m:f>'
    '<m:num><m:r><m:t>s(k)</m:t></m:r></m:num>'
    '<m:den>'
    '<m:rad><m:deg/><m:e><m:r><m:t>k</m:t></m:r></m:e></m:rad>'
    '</m:den>'
    '</m:f>',
    eq_num="2.1"
)

add_body_p(
    "Trong đó: t_{0.975}(k - 1) là phân vị Student hai phía ở mức tin cậy 95% với bậc tự do f = k - 1; "
    "s(k) là độ lệch chuẩn mẫu tính trên k quan sát đầu tiên; √k là thừa số thu hẹp phương sai theo định lý giới hạn trung tâm. "
    "Khi k còn nhỏ (k < 10), hệ số Student t_{0.975} rất lớn (t ≈ 2.78 tại k = 5) và mẫu số √k nhỏ, khiến bán kính sai số ε_95% phồng to. "
    "Khi k tăng dần, giá trị t_{0.975} tiệm cận nhanh về giá trị phân vị chuẩn Gauss z_0.975 = 1.960 và tốc độ thu hẹp bán kính chậm dần lại."
)

add_heading_3("2.4.2. Biểu đồ hội tụ thực nghiệm và Bảng số liệu đối chiếu")
add_body_p(
    "Để chứng minh thực nghiệm, nhóm nghiên cứu đã tiến hành chuỗi thực nghiệm lấy mẫu liên tục N_max = 100 lần đo tại 3 mốc cự ly tiêu biểu: "
    "50 cm (cự ly gần), 100 cm (cự ly trung bình), và 150 cm (cự ly xa). Đường cong biến thiên của bán kính khoảng tin cậy ε_95%(k) theo cỡ mẫu k "
    "được minh họa trực quan trên Hình 2.1:"
)

# Chèn ảnh Hình 2.1
if os.path.exists(IMG_CH2_PATH):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(IMG_CH2_PATH, width=Cm(15.0))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(10)
    r_c = p_cap.add_run("Hình 2.1: Đường cong hội tụ thực nghiệm của Bán kính khoảng tin cậy Student 95% (ε_95%) theo cỡ mẫu k tại các mốc cự ly 50 cm, 100 cm, 150 cm, minh chứng tính tối ưu kỹ thuật của cỡ mẫu N = 50.")
    r_c.font.name = 'Times New Roman'
    r_c.font.size = Pt(11)
    r_c.font.italic = True

add_body_p("Bảng 2.3 chi tiết hóa các mốc biến thiên của bán kính khoảng tin cậy theo cỡ mẫu k:")

p_tbl3 = doc.add_paragraph()
p_tbl3.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_tbl3.paragraph_format.space_after = Pt(4)
r_t3 = p_tbl3.add_run("Bảng 2.3: Bảng số liệu hội tụ của bán kính khoảng tin cậy Student 95% (ε_95%) theo cỡ mẫu k")
r_t3.font.name = 'Times New Roman'
r_t3.font.size = Pt(12)
r_t3.font.bold = True

cv_data = [
    ("k = 5", "2.776", "± 0.11 mm", "± 0.62 mm", "± 1.25 mm", "Sai số lớn vượt ngưỡng dung sai cho phép (> 0.5 mm)"),
    ("k = 10", "2.262", "± 0.07 mm", "± 0.34 mm", "± 0.89 mm", "Độ tin cậy chưa cao, độ lệch chuẩn chưa ổn định"),
    ("k = 20", "2.093", "± 0.04 mm", "± 0.18 mm", "± 0.42 mm", "Bắt đầu bước vào vùng chuyển tiếp hội tụ"),
    ("k = 30", "2.045", "± 0.03 mm", "± 0.14 mm", "± 0.28 mm", "Đạt yêu cầu đo lường cơ bản, phân vị tiệm cận Gauss"),
    ("k = 50 (Tối ưu)", "2.010", "± 0.02 mm", "± 0.09 mm", "± 0.15 mm", "Điểm uốn tối ưu: ε_95% < 0.15 mm, tốc độ quét hoàn hảo"),
    ("k = 75", "1.993", "± 0.02 mm", "± 0.08 mm", "± 0.13 mm", "Hiệu quả cải thiện không đáng kể (< 0.02 mm)"),
    ("k = 100", "1.984", "± 0.02 mm", "± 0.07 mm", "± 0.12 mm", "Tăng gấp đôi thời gian đo nhưng sai số chỉ giảm 0.03 mm")
]

table_cv = doc.add_table(rows=len(cv_data)+1, cols=6)
table_cv.alignment = WD_TABLE_ALIGNMENT.CENTER
table_cv.autofit = False

cv_widths = [Cm(2.6), Cm(2.2), Cm(2.4), Cm(2.4), Cm(2.4), Cm(4.0)]
cv_headers = ["Cỡ mẫu k", "Hệ số Student", "Mốc 50cm (ε_95%)", "Mốc 100cm (ε_95%)", "Mốc 150cm (ε_95%)", "Nhận xét trạng thái kỹ thuật"]

for idx, text in enumerate(cv_headers):
    c = table_cv.rows[0].cells[idx]
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

for row_idx, data in enumerate(cv_data, start=1):
    for col_idx, text in enumerate(data):
        c = table_cv.rows[row_idx].cells[col_idx]
        c.text = text
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 5 else WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            if col_idx == 0:
                r.font.bold = True
                if "50" in text:
                    r.font.color.rgb = C_MAROON

for row in table_cv.rows:
    for idx, width in enumerate(cv_widths):
        row.cells[idx].width = width
        set_cell_border(row.cells[idx],
            top=dict(sz=4, val='single', color='B0C4DE'),
            bottom=dict(sz=4, val='single', color='B0C4DE'),
            left=dict(val='none'), right=dict(val='none'))

for c in table_cv.rows[0].cells:
    set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
for c in table_cv.rows[-1].cells:
    set_cell_border(c, bottom=dict(sz=12, val='single', color='003366'), top=dict(sz=4, val='single', color='B0C4DE'), left=dict(val='none'), right=dict(val='none'))

add_heading_3("2.4.3. Luận giải khoa học quyết định lựa chọn cỡ mẫu N = 50")
add_body_p(
    "Dựa trên phân tích giải tích và kết quả thực nghiệm, quyết định chốt cỡ mẫu N = 50 cho toàn bộ đề tài được khẳng định bởi 3 luận cứ khoa học vững chắc:"
)
add_bullet_p(
    "Từ k = 5 đến k = 30, đường cong ε_95%(k) dốc đứng, sai số giảm cực kỳ nhanh chóng. "
    "Tuy nhiên, bắt đầu từ k = 50 trở đi, tốc độ biến thiên đạo hàm d(ε_95%)/dk tiệm cận về 0 (đường cong nằm ngang phẳng tuyệt đối). "
    "Việc tăng số lần đo từ N = 50 lên N = 100 đòi hỏi thời gian thu thập tăng gấp đôi (từ 2.5 giây lên 5.0 giây tại tần số quét 20 Hz), "
    "nhưng bán kính khoảng tin cậy ε_95% chỉ giảm được từ 0.15 mm xuống 0.12 mm (chênh lệch 0.03 mm - hoàn toàn nhỏ hơn độ phân giải phần cứng vi điều khiển 0.175 mm).",
    "1. Quy luật hiệu suất biên giảm dần (Law of Diminishing Marginal Returns): "
)
add_bullet_p(
    "Tại N = 50, bán kính khoảng tin cậy ε_95% đạt mức < 0.15 mm trên toàn dải đo khảo sát. "
    "Giá trị này nhỏ hơn đáng kể so với sai số vạch chia của thước chuẩn cơ khí (±0.5 mm), đảm bảo tính đại diện và độ chính xác thống kê "
    "tuyệt đối cho giá trị trung bình mẫu.",
    "2. Đảm bảo độ chính xác đo lường kỹ thuật: "
)
add_bullet_p(
    "Với chu kỳ đo lặp 50 ms (tần số lấy mẫu 20 Hz, tránh hiện tượng chồng lấn âm phản xạ nhiều lần), "
    "việc thu thập N = 50 mẫu chỉ mất đúng T_total = 50 × 50 ms = 2.5 giây cho mỗi mốc cự ly. "
    "Khoảng thời gian 2.5 giây đủ ngắn để môi trường vi khí hậu (nhiệt độ, áp suất không khí) được coi là bất biến, "
    "loại trừ hoàn toàn hiện tượng trôi nhiệt độ môi trường trong từng phiên đo.",
    "3. Cân bằng tối ưu giữa độ chính xác và thời gian quét: "
)

# Lưu tệp Word hoàn chỉnh
try:
    doc.save(OUTPUT_FILE)
    print(f"Xuất bản thành công tài liệu Word hoàn chỉnh chuẩn Headings và Equation: {OUTPUT_FILE}")
except PermissionError:
    alt_output = OUTPUT_FILE.replace("Bao_Cao_Thuc_Nghiem_RCWL1601.docx", "Bao_Cao_Thuc_Nghiem_RCWL1601_CapNhat.docx")
    doc.save(alt_output)
    print(f"Tệp chính đang được mở trong Word! Đã lưu bản cập nhật sang: {alt_output}")
