# -*- coding: utf-8 -*-
"""
Kịch bản xuất bản Báo Cáo Chuyên Đề Chương 4 (Word .docx) riêng biệt
Phiên bản cập nhật: Mô hình thực nghiệm bồn để bàn R = 4.0 cm, H = 12.0 cm, V = 603.2 mL
Tuân thủ tuyệt đối quy chuẩn GEMINI.md:
1. Hệ thống Headings tương tác cho Navigation Pane (Ctrl+F / View -> Navigation Pane):
   - Heading 1: Tên Chương (16pt, Bold, C_NAVY)
   - Heading 2: Mục lớn 4.X (14pt, Bold, C_NAVY)
   - Heading 3: Tiểu mục 4.X.Y (13pt, Bold, C_MAROON)
2. Công thức toán học chuẩn Microsoft Word Equation (OMML, Alt + =).
3. Bảng biểu chuẩn IEEE/APA (header xanh pastel #D9E1F2, viền nét đơn chuẩn, căn giữa).
4. Hình ảnh độ phân giải cao (300 DPI), căn giữa, caption in nghiêng bên dưới.
5. Định dạng văn bản: Times New Roman 13pt, line spacing 1.35, thụt lề 1.0cm, căn đều (Justified).
"""

import os
import sys
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE_1 = os.path.join(BASE_DIR, "Bao_Cao_Chuong_4_Ung_Dung_Thuc_Te.docx")
OUTPUT_FILE_2 = os.path.join(r"C:\Users\Admin\Downloads", "Bao_Cao_Chuong_4_Ung_Dung_Thuc_Te.docx")

IMG_H4_1 = os.path.join(BASE_DIR, "graph", "hinh_4_1_nguyen_ly_bon_chua.png")
IMG_H4_2 = os.path.join(BASE_DIR, "graph", "hinh_4_2_mo_phong_loc_song_gon.png")
IMG_H4_3 = os.path.join(BASE_DIR, "graph", "hinh_4_3_danh_gia_sai_so_the_tich.png")

doc = Document()

# Bảng màu chuẩn học thuật kỹ thuật
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

# Header và Footer
header = section.header
p_head = header.paragraphs[0]
p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r_head = p_head.add_run("HỌC PHẦN: KỸ THUẬT ĐO LƯỜNG VÀ CẢM BIẾN (EMA2024E_3) — CHƯƠNG 4")
r_head.font.name = 'Times New Roman'
r_head.font.size = Pt(9.5)
r_head.font.color.rgb = C_GRAY

footer = section.footer
p_foot = footer.paragraphs[0]
p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_foot = p_foot.add_run()
fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
r_foot._r.append(fldChar1)
r_foot._r.append(instrText)
r_foot._r.append(fldChar2)
r_foot._r.append(fldChar3)
r_foot.font.name = 'Times New Roman'
r_foot.font.size = Pt(10)
r_foot.font.color.rgb = C_GRAY

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
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(10)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    return p

def add_heading_2(text):
    p = doc.add_heading(level=2)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    return p

def add_heading_3(text):
    p = doc.add_heading(level=3)
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
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
        r_b.font.color.rgb = C_BLACK
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    return p

def add_native_equation(omml_xml_content, eq_num=""):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.2
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    wrapper_xml = (
        f'<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
        f'<m:oMath>{omml_xml_content}</m:oMath>'
        f'</m:oMathPara>'
    )
    p._p.append(parse_xml(wrapper_xml))
    
    if eq_num:
        p_num = doc.add_paragraph()
        p_num.paragraph_format.space_before = Pt(0)
        p_num.paragraph_format.space_after = Pt(4)
        p_num.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p_num.add_run(f"({eq_num})")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.color.rgb = C_GRAY
    return p

def add_image_box(img_path, caption_text, width_cm=14.5):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.line_spacing = 1.0
        p_img.paragraph_format.keep_with_next = True
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=Cm(width_cm))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        p_cap.paragraph_format.line_spacing = 1.15
        
        parts = caption_text.split(":", 1)
        if len(parts) == 2:
            r_bold = p_cap.add_run(parts[0] + ":")
            r_bold.font.name = 'Times New Roman'
            r_bold.font.size = Pt(11.5)
            r_bold.font.bold = True
            r_bold.font.color.rgb = C_NAVY
            
            r_desc = p_cap.add_run(parts[1])
            r_desc.font.name = 'Times New Roman'
            r_desc.font.size = Pt(11.5)
            r_desc.font.italic = True
        else:
            r_all = p_cap.add_run(caption_text)
            r_all.font.name = 'Times New Roman'
            r_all.font.size = Pt(11.5)
            r_all.font.italic = True

# =============================================================
# TRANG BÌA CHUYÊN ĐỀ PHẦN 4
# =============================================================
p_top = doc.add_paragraph()
p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_top.paragraph_format.space_before = Pt(12)
p_top.paragraph_format.space_after = Pt(2)
r_top = p_top.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nTRƯỜNG ĐẠI HỌC BÁCH KHOA HÀ NỘI\nVIỆN CƠ KHÍ / TRƯỜNG CƠ KHÍ")
r_top.font.name = 'Times New Roman'
r_top.font.size = Pt(12.5)
r_top.font.bold = True
r_top.font.color.rgb = C_NAVY

p_div = doc.add_paragraph()
p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_div.paragraph_format.space_after = Pt(20)
r_div = p_div.add_run("━━━━━━━━━━━━━━━━━━━━━")
r_div.font.name = 'Times New Roman'
r_div.font.color.rgb = C_MAROON

p_rep = doc.add_paragraph()
p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_rep.paragraph_format.space_after = Pt(6)
r_rep = p_rep.add_run("BÁO CÁO THỰC NGHIỆM CHUYÊN ĐỀ")
r_rep.font.name = 'Times New Roman'
r_rep.font.size = Pt(17)
r_rep.font.bold = True
r_rep.font.color.rgb = C_MAROON

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(16)
r_sub = p_sub.add_run("HỌC PHẦN: KỸ THUẬT ĐO LƯỜNG VÀ CẢM BIẾN (EMA2024E_3)")
r_sub.font.name = 'Times New Roman'
r_sub.font.size = Pt(13)
r_sub.font.bold = True
r_sub.font.color.rgb = C_NAVY

p_title_box = doc.add_paragraph()
p_title_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title_box.paragraph_format.space_after = Pt(20)
r_title1 = p_title_box.add_run("ĐỀ TÀI CHUNG: KHẢO SÁT THỰC NGHIỆM ĐẶC TÍNH ĐO LƯỜNG CỦA CẢM BIẾN SIÊU ÂM RCWL-1601\n")
r_title1.font.name = 'Times New Roman'
r_title1.font.size = Pt(13)
r_title1.font.bold = True
r_title1.font.color.rgb = C_BLACK

r_title2 = p_title_box.add_run("PHẦN 4: XÂY DỰNG VÀ TRIỂN KHAI BÀI TOÁN ỨNG DỤNG THỰC TẾ\n(HỆ THỐNG GIÁM SÁT MỨC VÀ THỂ TÍCH BỒN CHỨA THỰC NGHIỆM ĐỂ BÀN CÓ BÙ NHIỆT ĐỘ TRÊN ESP32)")
r_title2.font.name = 'Times New Roman'
r_title2.font.size = Pt(14.5)
r_title2.font.bold = True
r_title2.font.color.rgb = C_NAVY

p_meta = doc.add_paragraph()
p_meta.paragraph_format.left_indent = Cm(2.0)
p_meta.paragraph_format.space_after = Pt(24)
r_meta = p_meta.add_run(
    "Sinh viên thực hiện phần 4: Thành viên Nhóm Nghiên cứu\n"
    "Giảng viên hướng dẫn: Bộ môn Kỹ thuật Đo lường và Cảm biến\n"
    "Mô hình thực nghiệm: Bồn hình trụ tròn để bàn (R = 4.0 cm, H = 12.0 cm, V ≈ 603 mL)\n"
    "Địa điểm thực hiện: Phòng Thực nghiệm Đo lường & Cảm biến — ĐHBK Hà Nội\n"
    "Thời gian hoàn thành: Tháng 11/2026"
)
r_meta.font.name = 'Times New Roman'
r_meta.font.size = Pt(12)
r_meta.font.italic = True

doc.add_page_break()

# =============================================================
# CHƯƠNG 4: TOÀN VĂN HỌC THUẬT ĐỊNH LƯỢNG
# =============================================================
add_heading_1("CHƯƠNG 4: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ")

add_heading_2("4.1. TỔNG QUAN TIỀM NĂNG ỨNG DỤNG TỪ KẾT QUẢ KHẢO SÁT THỰC NGHIỆM CỦA CẢM BIẾN RCWL-1601")

add_heading_3("4.1.1. Các đặc tính đo lường định hình không gian ứng dụng")
add_body_p(
    "Từ các kết quả nghiên cứu và kiểm chứng thực nghiệm chuyên sâu được thực hiện ở Chương 3, các thông số "
    "đặc tính tĩnh và động của module cảm biến siêu âm RCWL-1601 trên nền tảng vi điều khiển ESP32 được xác lập "
    "qua các ràng buộc kỹ thuật cốt lõi sau:"
)

add_bullet_p(
    "Hệ số xác định hồi quy đạt R² = 0.999988, sai số tương đối luôn nằm dưới ngưỡng ±0.35%, độ lệch chuẩn lặp lại "
    "thực nghiệm cực nhỏ (s < 0.4 mm ở cự ly dưới 1 m và s < 2.5 mm ở cự ly đến 3.5 m). Kết quả này khẳng định cảm biến "
    "đạt độ tin cậy tương đương các thiết bị đo công nghiệp trong dải cự ly làm việc tiêu chuẩn.",
    bold_prefix="1. Dải làm việc tuyến tính tối ưu (5 cm → 350 cm): "
)

add_bullet_p(
    "Sai số tuyệt đối tăng vọt trên 100% do thời gian dao động suy giảm của màng gốm áp điện (150 µs) và ngưỡng ngắt "
    "câm nội của IC RCWL-9610. Mọi hệ thống ứng dụng bắt buộc phải thiết kế khoảng cách lắp đặt cơ khí cách ly vật thể "
    "tối thiểu 5 cm để không bao giờ rơi vào vùng mù này.",
    bold_prefix="2. Vùng chết vật lý (1 cm → 3 cm): "
)

add_bullet_p(
    "Bề mặt phản xạ không bằng phẳng hoặc xốp làm độ lệch chuẩn tăng vọt gấp 15 - 26 lần và làm suy giảm cự ly đo "
    "tin cậy. Ngược lại, mặt thoáng chất lỏng tĩnh đóng vai trò như gương phản xạ phẳng hoàn hảo, hỗ trợ chùm sóng dội về trọn vẹn.",
    bold_prefix="3. Hiện tượng phản xạ và hướng tính sóng âm: "
)

add_bullet_p(
    "Sự biến thiên nhiệt độ chỉ 7.0°C (giữa nhiệt độ phòng mặc định 27.0°C và phòng lạnh 20.0°C) làm thay đổi vận tốc "
    "sóng âm 1.24% (từ 347.662 m/s xuống 343.420 m/s), gây trôi sai số cự ly. Do đó, việc tích hợp thuật toán bù vận tốc "
    "sóng âm Laplace theo nhiệt độ môi trường thời gian thực là bắt buộc.",
    bold_prefix="4. Độ nhạy nhiệt độ của môi trường không khí: "
)

add_heading_3("4.1.2. Định hướng các bài toán kỹ thuật tiêu biểu và Lựa chọn mô hình thực nghiệm")
add_body_p(
    "Dựa trên các đặc tính định lượng nêu trên, module cảm biến RCWL-1601 kết hợp ESP32 hoàn toàn đáp ứng xuất sắc "
    "ba bài toán đo lường và tự động hóa: (1) Giám sát mức và thể tích bồn chứa chất lỏng không tiếp xúc; (2) Cảm biến cảnh báo "
    "cự ly an toàn cho xe tự hành AGV; (3) Trạm tự động đo kích thước 3 chiều và thể tích bao bì trên băng tải logistics."
)

add_body_p(
    "Nhằm hiện thực hóa bài toán ứng dụng thành một mô hình vật lý trực quan phục vụ chế tạo, đo kiểm và trình diễn thực tế "
    "(Desktop Laboratory Prototype), nhóm nghiên cứu lựa chọn thiết kế Mô hình Hệ thống Giám sát Mức và Thể tích Bồn chứa "
    "Thực nghiệm Để bàn (dung tích khoảng 600 mL, chiều cao thân bồn 12 cm, bán kính đáy 4 cm). Mô hình này vừa vặn với các cốc đong "
    "chia vạch tiêu chuẩn trong phòng thí nghiệm, cho phép quan sát trực tiếp mặt thoáng và kiểm chứng sai số đo lường với độ trực quan cao nhất."
)

add_heading_2("4.2. THIẾT KẾ CHI TIẾT BÀI TOÁN: HỆ THỐNG GIÁM SÁT MỨC VÀ THỂ TÍCH BỒN CHỨA THỰC NGHIỆM ĐỂ BÀN TRÊN ESP32")

add_heading_3("4.2.1. Đặt bài toán và Mô hình toán học hình học bồn chứa để bàn")
add_body_p(
    "Mô hình bồn chứa thực nghiệm để bàn được thiết kế dạng hình trụ đứng bằng vật liệu mica trong suốt hoặc thủy tinh có vạch chia milimet, "
    "tương thích hoàn hảo với kích thước module cảm biến RCWL-1601 (kích thước PCB 4.5 cm × 2.0 cm) và các cơ cấu bơm nạp mini trong phòng lab:"
)

add_bullet_p("Bán kính trong đáy bồn: R = 4.0 cm = 0.04 m (Đường kính trong D = 8.0 cm = 0.08 m).")
add_bullet_p("Chiều cao thân bồn chứa chất lỏng: H_tank = 12.0 cm = 0.12 m.")
add_bullet_p("Chiều cao ống cổ nối gá lắp cảm biến: H_cổ = 5.0 cm = 0.05 m.")
add_bullet_p("Tổng chiều cao chuẩn từ mặt đầu đo cảm biến đến đáy bồn: H_tổng = H_tank + H_cổ = 12.0 + 5.0 = 17.0 cm = 0.17 m.")

add_body_p("Diện tích mặt đáy hình tròn của bồn chứa thực nghiệm được xác định theo công thức:")
add_native_equation(
    '<m:r><m:t>S</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>base</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> = π · </m:t></m:r>'
    '<m:sSup><m:e><m:r><m:t>R</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup>'
    '<m:r><m:t> = π · </m:t></m:r>'
    '<m:sSup><m:e><m:r><m:t>(4.0)</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup>'
    '<m:r><m:t> ≈ 50.2655 </m:t></m:r>'
    '<m:sSup><m:e><m:r><m:t>cm</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup>'
    '<m:r><m:t> = 0.005027 </m:t></m:r>'
    '<m:sSup><m:e><m:r><m:t>m</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup>',
    eq_num="4.1"
)

add_body_p("Thể tích dung tích toàn phần của thân bồn chứa là:")
add_native_equation(
    '<m:r><m:t>V</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>toàn phần</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> = S</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>base</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> · H</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>tank</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> = 50.2655 × 12.0 ≈ 603.19 </m:t></m:r>'
    '<m:sSup><m:e><m:r><m:t>cm</m:t></m:r></m:e><m:sup><m:r><m:t>3</m:t></m:r></m:sup></m:sSup>'
    '<m:r><m:t> ≈ 603.2 mL  (≈ 0.603 Lít)</m:t></m:r>',
    eq_num="4.2"
)

add_body_p(
    "Khi cảm biến siêu âm phát sóng thẳng đứng từ đỉnh ống gá xuống mặt thoáng, mức chất lỏng h(t) và thể tích tức thời V(t) "
    "được tính toán tức thời theo khoảng trống không khí d_comp(t) đo được:"
)

add_native_equation(
    '<m:r><m:t>h(t) = H</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>tổng</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> - d</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>comp</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(t) = 17.0 - d</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>comp</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(t)    (cm)</m:t></m:r>',
    eq_num="4.3"
)

add_native_equation(
    '<m:r><m:t>V(t) = S</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>base</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> · h(t) = 50.2655 · h(t)    (mL)</m:t></m:r>',
    eq_num="4.4"
)

add_body_p(
    "Độ nhạy chuyển đổi thể tích của mô hình đạt xấp xỉ 5.03 mL / 1 mm chiều cao nước. Đây là độ nhạy rất phù hợp để đánh giá "
    "độ phân giải của cảm biến siêu âm trên một mô hình thực tế."
)

add_image_box(
    IMG_H4_1,
    "Hình 4.1: Sơ đồ nguyên lý hình học và kiến trúc kết nối của Mô hình Bồn chứa Để bàn Thông minh (R = 4 cm, H = 12 cm, V ≈ 603 mL) trên nền tảng RCWL-1601 và ESP32.",
    width_cm=14.0
)

add_heading_3("4.2.2. Vận dụng trực tiếp các phát hiện thực nghiệm ở Chương 3 vào thiết kế hệ thống")
add_body_p(
    "Để mô hình thực nghiệm để bàn hoạt động chính xác và ổn định, các phát hiện thực nghiệm định lượng ở Chương 3 "
    "được chuyển hóa thành các giải pháp kỹ thuật đo lường chuyên biệt:"
)

add_body_p(
    "1. Thiết kế ống cổ nối cách ly vùng chết vật lý (H_cổ = 5.0 cm):\n"
    "• Phát hiện ở Mục 3.2: Trong khoảng cự ly 1 cm → 3 cm, cảm biến bị mù phản xạ hoàn toàn và kẹp kết quả ở mức 2.0 - 2.6 cm "
    "do thời gian dao động suy giảm của màng áp điện và ngưỡng ngắt câm nội của IC RCWL-9610.\n"
    "• Giải pháp thiết kế: Cảm biến được lắp trên ống cổ nối hình trụ có chiều cao H_cổ = 5.0 cm, đường kính 8.0 cm đồng trục với bồn chứa.\n"
    "• Hiệu quả: Khi bồn chứa được nạp đầy 100% dung tích (mức nước h = 12.0 cm), khoảng cách từ mặt cảm biến tới mặt nước vẫn đạt đúng "
    "d = 5.0 cm. Cự ly này nằm trọn vẹn ở biên ngoài của vùng chết (vùng tuyến tính lý tưởng, độ lệch chuẩn lặp lại s < 0.1 mm), "
    "triệt tiêu hoàn toàn nguy cơ mất kiểm soát khi bồn đầy."
)

add_body_p(
    "2. Ứng dụng thành bồn trơn nhẵn làm Ống dẫn sóng âm học (Acoustic Waveguide):\n"
    "• Vấn đề âm học: Với góc mở chùm tia ±15°, tại đáy bồn (d_max = 17.0 cm), đường kính chùm sóng tự do là W = 2 · 17 · tan(15°) ≈ 9.1 cm, "
    "tiệm cận đường kính trong của bồn D = 8.0 cm. Ở nửa trên của bồn (d ≤ 11 cm), đường kính chùm sóng chỉ là 5.9 cm < 8.0 cm.\n"
    "• Giải pháp kỹ thuật: Bồn sử dụng ống mica tròn trơn nhẵn đóng vai trò như một Ống dẫn sóng tĩnh (Stilling Well) — giải pháp chuẩn "
    "trong đo mức bồn chứa công nghiệp. Ống dẫn sóng giúp định hướng chùm sóng đi thẳng góc xuống mặt nước, triệt tiêu tiếng vang phụ từ thành bồn "
    "và bảo vệ tín hiệu khỏi luồng gió ngoại cảnh."
)

add_body_p(
    "3. Tích hợp thuật toán bù vận tốc sóng âm Laplace theo nhiệt độ bồn chứa:\n"
    "Bố trí đầu dò nhiệt độ số DS18B20 gắn tại cổ bồn chứa. ESP32 cập nhật nhiệt độ môi trường T (°C) trước mỗi chu kỳ phát xung "
    "và hiệu chỉnh vận tốc truyền sóng theo phương trình Laplace thực nghiệm:"
)

add_native_equation(
    '<m:r><m:t>v(T) = 331.3 + 0.606 · T    (m/s)</m:t></m:r>',
    eq_num="4.5"
)

add_native_equation(
    '<m:r><m:t>d</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>comp</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:f>'
    '<m:num><m:r><m:t>v(T) · t</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>2</m:t></m:r></m:den>'
    '</m:f>'
    '<m:r><m:t>    (m)</m:t></m:r>',
    eq_num="4.6"
)

add_body_p(
    "4. Chuỗi lọc số thích nghi: Lọc Khoảng tứ phân vị (IQR) kết hợp Trung bình trượt (Moving Average):\n"
    "Nhằm khắc phục sóng gợn bề mặt khi máy bơm mini cấp nước và các bọt khí vỡ làm mất xung echo tức thời, tín hiệu thời gian bay "
    "được số hóa qua hai tầng lọc nối tiếp:\n"
    "   - Tầng 1 - Lọc Khoảng tứ phân vị (IQR Filter) theo cửa sổ trượt (W = 9 mẫu): Cắt tỉa triệt để các xung ngoại lai nằm ngoài "
    "hàng rào Tukey [Q₁ - 1.5·IQR, Q₃ + 1.5·IQR] và thay thế bằng giá trị trung vị Med của cửa sổ.\n"
    "   - Tầng 2 - Lọc trung bình trượt (Moving Average Filter, M = 7 mẫu): Làm mịn hoàn toàn các dao động sóng gợn chu kỳ nhỏ theo công thức:"
)

add_native_equation(
    '<m:acc><m:accPr><m:chr m:val="¯"/></m:accPr><m:e><m:r><m:t>h</m:t></m:r></m:e></m:acc>'
    '<m:r><m:t>[k] = </m:t></m:r>'
    '<m:f>'
    '<m:num><m:r><m:t>1</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>M</m:t></m:r></m:den>'
    '</m:f>'
    '<m:nary>'
    '<m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/></m:naryPr>'
    '<m:sub><m:r><m:t>j=0</m:t></m:r></m:sub>'
    '<m:sup><m:r><m:t>M-1</m:t></m:r></m:sup>'
    '<m:e>'
    '<m:r><m:t>h</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>IQR</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>[k - j]</m:t></m:r>'
    '</m:e>'
    '</m:nary>',
    eq_num="4.7"
)

add_body_p(
    "5. Lan truyền Độ không đảm bảo đo Thể tích theo tiêu chuẩn ISO/GUM:\n"
    "Áp dụng kết quả đánh giá ở Mục 3.8: Tại dải khoảng cách gần d = 5 cm → 17 cm, độ không đảm bảo đo mở rộng của cự ly là "
    "U_95%(d) ≈ 0.8 mm → 1.15 mm. Theo định luật lan truyền độ không đảm bảo đo:"
)

add_native_equation(
    '<m:r><m:t>h = H</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>tổng</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> - d  ⟹  u</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>c</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(h) ≈ u</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>c</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(d)</m:t></m:r>',
    eq_num="4.8"
)

add_native_equation(
    '<m:r><m:t>U</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>95%</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(V) = S</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>base</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> · U</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>95%</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t>(h)</m:t></m:r>',
    eq_num="4.9"
)

add_body_p(
    "Tại mức nước đầy (h = 12.0 cm, khoảng trống d = 5.0 cm, U_95%(h) = 0.80 mm = 0.08 cm):\n"
    "U_95%(V) = 50.2655 cm² × 0.08 cm ≈ 4.02 mL.\n"
    "Sai số tương đối của thể tích khi đầy bồn đạt mức cực kỳ ấn tượng:"
)

add_native_equation(
    '<m:f>'
    '<m:num><m:r><m:t>U</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>95%</m:t></m:r></m:sub></m:sSub><m:r><m:t>(V)</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>V</m:t></m:r></m:den>'
    '</m:f>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:f>'
    '<m:num><m:r><m:t>4.02 mL</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>603.2 mL</m:t></m:r></m:den>'
    '</m:f>'
    '<m:r><m:t> × 100% = 0.67%</m:t></m:r>',
    eq_num="4.10"
)

add_heading_2("4.3. KẾT QUẢ THỬ NGHIỆM MÔ PHỎNG VÀ ĐÁNH GIÁ HIỆU NĂNG ỨNG DỤNG")

add_heading_3("4.3.1. Mô phỏng động học quá trình bơm nạp và hiệu quả chuỗi lọc số")
add_body_p(
    "Quá trình bơm nạp chất lỏng vào bồn để bàn được mô phỏng trong thời gian 30 giây thực tế (tần số lấy mẫu f_s = 5 Hz, N = 150 mẫu). "
    "Mức chất lỏng thực tế tăng dần từ mức đáy 1.5 cm đến mức 10.5 cm theo lưu lượng bơm mini 5V. Phương thức cấp nước từ đáy bình "
    "giúp khống chế biên độ sóng gợn ở mức nhỏ (±0.6 cm, tần số 0.5 Hz). Hệ thống giả lập 3 xung nhiễu ngoại lai tại giây thứ 5.0 (0.5 cm do bọt khí), "
    "giây thứ 15.0 (-4.0 cm do timeout mất echo), và giây thứ 24.0 (13.5 cm do phản xạ thành bồn)."
)

add_image_box(
    IMG_H4_2,
    "Hình 4.2: Hiệu quả khử sóng gợn và lọc ngoại lai trong chuỗi xử lý tín hiệu Bồn chứa để bàn: Tín hiệu đo thô bị ảnh hưởng bởi sóng gợn và gai nhiễu, tín hiệu sau tầng lọc IQR và tín hiệu hoàn chỉnh sau tầng lọc Moving Average bám sát mức nước thực tế.",
    width_cm=14.5
)

add_body_p(
    "Đánh giá định lượng hiệu quả chuỗi lọc số:\n"
    "• Tín hiệu đo thô dao động với sai số lớn do sóng gợn và gai nhiễu ngoại lai.\n"
    "• Tầng lọc IQR loại bỏ chính xác 100% cả 3 xung dị biệt bão hòa, đưa tín hiệu về thuần túy biên độ dao động sóng gợn.\n"
    "• Tầng lọc trung bình trượt MA làm phẳng hoàn toàn sóng gợn, giảm độ lệch chuẩn sai số xuống còn s_error = 0.08 cm = 0.8 mm. "
    "Đường đặc tính đo bám sát đường mức nước thực tế trong dải dung sai cho phép ±2.0 mm."
)

add_heading_3("4.3.2. Bảng tổng hợp độ không đảm bảo đo thể tích toàn bồn chứa để bàn")
add_body_p(
    "Kế thừa giá trị độ không đảm bảo đo mở rộng U_95%(d) từ Mục 3.8, bảng dưới đây chi tiết hóa giá trị thể tích, khoảng cách đo "
    "và độ không đảm bảo đo thể tích tương ứng trên toàn bộ dải mức nước làm việc của bồn chứa để bàn:"
)

# Bảng 4.1: Bảng tổng hợp độ không đảm bảo đo
p_cap_t41 = doc.add_paragraph()
p_cap_t41.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_t41.paragraph_format.space_before = Pt(8)
p_cap_t41.paragraph_format.space_after = Pt(4)
r_t41_num = p_cap_t41.add_run("Bảng 4.1: ")
r_t41_num.font.name = 'Times New Roman'
r_t41_num.font.size = Pt(12)
r_t41_num.font.bold = True
r_t41_num.font.color.rgb = C_NAVY

r_t41_title = p_cap_t41.add_run("Bảng tổng hợp độ không đảm bảo đo mức nước và thể tích bồn chứa thực nghiệm để bàn")
r_t41_title.font.name = 'Times New Roman'
r_t41_title.font.size = Pt(12)
r_t41_title.font.bold = True

t41_data = [
    ("Tỷ lệ nạp (%)", "Mức nước h (cm)", "Khoảng trống d (cm)", "Thể tích V (mL)", "Độ KĐBĐ mức nước U_95%(h) (mm)", "Độ KĐBĐ thể tích U_95%(V) (mL)", "Độ KĐBĐ thể tích tương đối (%)"),
    ("10%", "1.2", "15.8", "60.3", "1.15", "5.78", "9.58%"),
    ("20%", "2.4", "14.6", "120.6", "1.10", "5.53", "4.58%"),
    ("30%", "3.6", "13.4", "181.0", "1.05", "5.28", "2.92%"),
    ("40%", "4.8", "12.2", "241.3", "1.00", "5.03", "2.08%"),
    ("50%", "6.0", "11.0", "301.6", "0.95", "4.78", "1.58%"),
    ("60%", "7.2", "9.8", "361.9", "0.90", "4.52", "1.25%"),
    ("70%", "8.4", "8.6", "422.2", "0.85", "4.27", "1.01%"),
    ("80%", "9.6", "7.4", "482.6", "0.82", "4.12", "0.85%"),
    ("90%", "10.8", "6.2", "542.9", "0.80", "4.02", "0.74%"),
    ("100%", "12.0", "5.0", "603.2", "0.80", "4.02", "0.67%")
]

table_41 = doc.add_table(rows=len(t41_data), cols=7)
table_41.alignment = WD_TABLE_ALIGNMENT.CENTER
t41_widths = [Cm(2.0), Cm(2.2), Cm(2.4), Cm(2.3), Cm(2.5), Cm(2.4), Cm(2.2)]

for row_idx, row_content in enumerate(t41_data):
    row = table_41.rows[row_idx]
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    if row_idx == 0:
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        
    for col_idx, text_val in enumerate(row_content):
        c = row.cells[col_idx]
        c.width = t41_widths[col_idx]
        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.05
        
        r = p.add_run(text_val)
        r.font.name = 'Times New Roman'
        if row_idx == 0:
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = C_NAVY
            set_cell_background(c, "D9E1F2")
        else:
            r.font.size = Pt(9.5)
            if col_idx == 0 or col_idx == 6:
                r.font.bold = True
            if row_idx % 2 == 1:
                set_cell_background(c, "F9FAFB")
        
        if row_idx == 0:
            set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
        elif row_idx == len(t41_data) - 1:
            set_cell_border(c, top=dict(sz=4, val='single', color='B0C4DE'), bottom=dict(sz=12, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
        else:
            set_cell_border(c, top=dict(sz=4, val='single', color='E5E7EB'), bottom=dict(sz=4, val='single', color='E5E7EB'), left=dict(val='none'), right=dict(val='none'))

add_image_box(
    IMG_H4_3,
    "Hình 4.3: Biểu đồ Thể tích chất lỏng kèm dải tin cậy mở rộng 95% và Phân bố Độ không đảm bảo đo thể tích tương đối theo tỷ lệ mức nước trong bồn chứa để bàn.",
    width_cm=14.5
)

add_body_p(
    "Nhận xét phân tích dung sai thể tích bồn để bàn:\n"
    "• Khi bồn ở mức cạn dưới 30% (mức nước dưới 3.6 cm, V < 180 mL), độ không đảm bảo tương đối tăng cao (từ 2.9% đến 9.6%) do thể tích "
    "chất lỏng nền rất nhỏ trong khi sai số đo khoảng cách là đại lượng tuyệt đối (khoảng ±1 mm).\n"
    "• Khi bồn nạp từ 50% dung tích trở lên (V ≥ 300 mL), sai số tương đối nhanh chóng hạ xuống dưới 1.5%, và khi đầy bồn đạt tới 0.67%. "
    "Đây là kết quả đo lường rất tốt cho một mô hình thí nghiệm để bàn sử dụng cảm biến chi phí thấp."
)

add_heading_3("4.3.3. Phân ngưỡng cảnh báo tự động và Kiến trúc truyền thông mạng không dây IoT")
add_body_p(
    "Hệ thống điều khiển trên ESP32 tự động phân loại trạng thái bồn chứa để bàn thành 5 cấp độ an toàn và điều khiển đóng cắt máy bơm mini 5V qua module rơ-le:"
)

# Bảng 4.2: Phân ngưỡng cảnh báo
p_cap_t42 = doc.add_paragraph()
p_cap_t42.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_t42.paragraph_format.space_before = Pt(8)
p_cap_t42.paragraph_format.space_after = Pt(4)
r_t42_num = p_cap_t42.add_run("Bảng 4.2: ")
r_t42_num.font.name = 'Times New Roman'
r_t42_num.font.size = Pt(12)
r_t42_num.font.bold = True
r_t42_num.font.color.rgb = C_NAVY

r_t42_title = p_cap_t42.add_run("Phân ngưỡng cảnh báo và kịch bản tác động cơ cấu chấp hành trên mô hình để bàn")
r_t42_title.font.name = 'Times New Roman'
r_t42_title.font.size = Pt(12)
r_t42_title.font.bold = True

t42_data = [
    ("Cấp độ trạng thái", "Ngưỡng mức h", "Ngưỡng thể tích V", "Hành động chấp hành tự động", "Tín hiệu cảnh báo"),
    ("Cạn khẩn cấp (Low-Low)", "h ≤ 1.5 cm (< 12%)", "V ≤ 75 mL", "Khóa cưỡng bức rơ-le bơm xả, chống cháy bơm do chạy khan", "Còi báo động liên tục, LED Đỏ chớp nhanh"),
    ("Cảnh báo cạn (Low)", "1.5 cm < h ≤ 3.5 cm", "75 mL < V ≤ 175 mL", "Tự động kích hoạt rơ-le bật máy bơm nạp", "LED Vàng sáng, gửi thông báo nạp bồn"),
    ("Bình thường (Normal)", "3.5 cm < h < 10.5 cm", "175 mL < V < 525 mL", "Duy trì chế độ làm việc ổn định, tự động ngắt bơm nạp khi chạm ngưỡng", "LED Xanh sáng cố định"),
    ("Cảnh báo đầy (High)", "10.5 cm ≤ h < 11.5 cm", "525 mL ≤ V < 580 mL", "Ngắt bơm nạp chính, cảnh báo mức cao", "LED Vàng chớp chậm"),
    ("Tràn khẩn cấp (High-High)", "h ≥ 11.5 cm (> 95%)", "V ≥ 580 mL", "Cắt điện toàn bộ bơm nạp, kích hoạt van xả tràn", "Còi hú liên tục, ngắt nguồn khẩn cấp")
]

table_42 = doc.add_table(rows=len(t42_data), cols=5)
table_42.alignment = WD_TABLE_ALIGNMENT.CENTER
t42_widths = [Cm(3.2), Cm(2.8), Cm(2.6), Cm(4.4), Cm(3.0)]

for row_idx, row_content in enumerate(t42_data):
    row = table_42.rows[row_idx]
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    if row_idx == 0:
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        
    for col_idx, text_val in enumerate(row_content):
        c = row.cells[col_idx]
        c.width = t42_widths[col_idx]
        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 3 else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.1
        
        r = p.add_run(text_val)
        r.font.name = 'Times New Roman'
        if row_idx == 0:
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = C_NAVY
            set_cell_background(c, "D9E1F2")
        else:
            r.font.size = Pt(10)
            if col_idx == 0:
                r.font.bold = True
            if row_idx % 2 == 1:
                set_cell_background(c, "F9FAFB")
                
        if row_idx == 0:
            set_cell_border(c, top=dict(sz=12, val='single', color='003366'), bottom=dict(sz=8, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
        elif row_idx == len(t42_data) - 1:
            set_cell_border(c, top=dict(sz=4, val='single', color='B0C4DE'), bottom=dict(sz=12, val='single', color='003366'), left=dict(val='none'), right=dict(val='none'))
        else:
            set_cell_border(c, top=dict(sz=4, val='single', color='E5E7EB'), bottom=dict(sz=4, val='single', color='E5E7EB'), left=dict(val='none'), right=dict(val='none'))

add_body_p(
    "Kiến trúc truyền thông mạng không dây IoT:\n"
    "Nhờ tích hợp sẵn vi điều khiển lõi kép ESP32 có hỗ trợ Wi-Fi 802.11 b/g/n và Bluetooth BLE:\n"
    "• Dữ liệu mức nước h(t), thể tích V(t), nhiệt độ môi trường T(t) và trạng thái cảnh báo được đóng gói theo định dạng chuẩn JSON.\n"
    "• Thiết bị phát bản tin định kỳ qua giao thức MQTT (Message Queuing Telemetry Transport) với cơ chế bảo mật TLS/SSL tới Broker máy chủ trung tâm (Node-RED, ThingsBoard hoặc Home Assistant).\n"
    "• Người vận hành có thể theo dõi biểu đồ xu hướng thể tích theo thời gian thực trên giao diện Web Dashboard hoặc nhận tin nhắn cảnh báo sự cố tràn/cạn tức thời qua ứng dụng Telegram / SMS."
)

# Lưu tệp Word vào cả 2 vị trí (RCWL1601 và Downloads)
doc.save(OUTPUT_FILE_1)
shutil.copyfile(OUTPUT_FILE_1, OUTPUT_FILE_2)
print(f"XUẤT BẢN THÀNH CÔNG TỆP WORD CHƯƠNG 4:\n1. {OUTPUT_FILE_1}\n2. {OUTPUT_FILE_2}")
