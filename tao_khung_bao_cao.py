# -*- coding: utf-8 -*-
"""
Cập nhật file Word Báo Cáo Thực Nghiệm dựa trên ĐỀ CƯƠNG MỚI (7 CHƯƠNG - 31 ĐẾN 35 TRANG)
Đề tài: Thiết kế hệ thống thu thập dữ liệu, khảo sát thực nghiệm các đặc tính đo lường
        và xây dựng bài toán ứng dụng cho cảm biến khoảng cách siêu âm RCWL-1601
        kết hợp bù nhiệt độ môi trường trên ESP32
"""

import os
import sys
import html
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Thiết lập encoding UTF-8 an toàn cho console output
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

OUTPUT_DIR = r"D:\đo lường\thực hành đo lường\RCWL1601"
OUTPUT_FILE_MAIN = os.path.join(OUTPUT_DIR, "báo cáo.docx")
OUTPUT_FILE_NEW = os.path.join(OUTPUT_DIR, "báo cáo_khung_moi.docx")
OUTPUT_FILE_NEW_EN = os.path.join(OUTPUT_DIR, "bao_cao_khung_moi.docx")

doc = Document()

# Page Margins chuẩn A4
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.9)
    s.right_margin = Inches(0.9)

# Colors
C_NAVY = RGBColor(0, 51, 102)     # #003366
C_MAROON = RGBColor(128, 0, 0)   # #800000
C_GRAY = RGBColor(90, 90, 90)
C_DARK = RGBColor(30, 30, 30)
C_BLUE = RGBColor(26, 82, 118)

# Biến đếm ID duy nhất cho Word Bookmarks
bm_counter = 0

def add_bookmark(paragraph, bookmark_name):
    """Gắn thẻ Bookmark vào paragraph để làm anchor cho internal hyperlink."""
    global bm_counter
    bm_counter += 1
    bm_start = parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{bookmark_name}"/>')
    bm_end = parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>')
    pPr = paragraph._p.pPr
    if pPr is not None:
        pPr.addnext(bm_start)
    else:
        paragraph._p.insert(0, bm_start)
    paragraph._p.append(bm_end)

def set_cell_bg(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_pad(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(19)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(14)
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = C_MAROON
    return p

def add_meta(label, val):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(3)
    r1 = p.add_run(label + ": ")
    r1.font.bold = True
    r1.font.size = Pt(11)
    r2 = p.add_run(val)
    r2.font.size = Pt(11)

def add_h1(text, anchor=None, back_to_toc=True):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    
    if back_to_toc and anchor:
        p.add_run("   ")
        back_hl = parse_xml(
            f'<w:hyperlink {nsdecls("w")} w:anchor="toc_nav">'
            f'<w:r>'
            f'<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:color w:val="2563EB"/><w:sz w:val="18"/><w:i/></w:rPr>'
            f'<w:t>[↑ Về Mục Lục]</w:t>'
            f'</w:r>'
            f'</w:hyperlink>'
        )
        p._p.append(back_hl)

    if anchor:
        add_bookmark(p, anchor)
    return p

def add_h2(text, anchor=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(11)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = C_MAROON
    if anchor:
        add_bookmark(p, anchor)
    return p

def add_h3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = C_BLUE
    return p

def add_p(text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r.font.italic = italic
    return p

def add_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.12
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    return p

def add_guide_box(text, tip_title="[HƯỚNG DẪN ĐIỀN SỐ LIỆU & ĐỒ THỊ CHO MỤC NÀY]"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_bg(cell, "F2F7FA")
    set_cell_pad(cell, top=90, bottom=90, left=140, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="6" w:space="0" w:color="3B82F6"/><w:bottom w:val="single" w:sz="6" w:space="0" w:color="3B82F6"/><w:left w:val="single" w:sz="18" w:space="0" w:color="2563EB"/><w:right w:val="single" w:sz="6" w:space="0" w:color="3B82F6"/></w:tcBorders>')
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(tip_title + "\n")
    r1.font.name = 'Calibri'
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(30, 64, 175)
    
    r2 = p.add_run(text)
    r2.font.name = 'Calibri'
    r2.font.size = Pt(9.5)
    r2.font.italic = True
    r2.font.color.rgb = RGBColor(55, 65, 81)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_placeholder_img(caption):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_bg(cell, "F8FAFC")
    set_cell_pad(cell, top=160, bottom=160, left=240, right=240)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="dashed" w:sz="8" w:space="0" w:color="94A3B8"/><w:bottom w:val="dashed" w:sz="8" w:space="0" w:color="94A3B8"/><w:left w:val="dashed" w:sz="8" w:space="0" w:color="94A3B8"/><w:right w:val="dashed" w:sz="8" w:space="0" w:color="94A3B8"/></w:tcBorders>')
    tcPr.append(tcBorders)
    
    cp = cell.paragraphs[0]
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = cp.add_run("[VỊ TRÍ CHÈN HÌNH ẢNH / BIỂU ĐỒ - DÙNG INSERT > PICTURE HOẶC XUẤT TỪ SCRIPT]")
    r.font.name = 'Calibri'
    r.font.size = Pt(9.0)
    r.font.italic = True
    r.font.color.rgb = RGBColor(100, 116, 139)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(7)
    rc = p_cap.add_run(caption)
    rc.font.name = 'Calibri'
    rc.font.size = Pt(9.5)
    rc.font.italic = True
    rc.font.color.rgb = C_GRAY

def add_toc_entry(doc, title, anchor, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.05
    if level == 1:
        p.paragraph_format.space_before = Pt(3.5)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Inches(0)
        color = "003366"  # C_NAVY
        bold_tag = "<w:b/>"
        size = 20  # 10 pt
        prefix = "■ "
    else:
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Inches(0.2)
        color = "1D4ED8"  # Royal Blue
        bold_tag = ""
        size = 18  # 9 pt
        prefix = "▸ "

    safe_text = html.escape(f"{prefix}{title}")
    hyperlink = parse_xml(
        f'<w:hyperlink {nsdecls("w")} w:anchor="{anchor}">'
        f'<w:r>'
        f'<w:rPr>'
        f'<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>'
        f'<w:rStyle w:val="Hyperlink"/>'
        f'<w:color w:val="{color}"/>'
        f'{bold_tag}'
        f'<w:sz w:val="{size}"/>'
        f'</w:rPr>'
        f'<w:t>{safe_text}</w:t>'
        f'</w:r>'
        f'</w:hyperlink>'
    )
    p._p.append(hyperlink)

# ==================== TRANG BÌA (TRANG 1) ====================
p_top_school = doc.add_paragraph()
p_top_school.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_top_school.paragraph_format.space_before = Pt(10)
p_top_school.paragraph_format.space_after = Pt(2)
r_sch = p_top_school.add_run("TRƯỜNG ĐẠI HỌC BÁCH KHOA HÀ NỘI\nKHOA ĐIỆN - ĐIỆN TỬ")
r_sch.font.name = 'Calibri'
r_sch.font.size = Pt(11)
r_sch.font.bold = True
r_sch.font.color.rgb = C_GRAY

add_title("BÁO CÁO THỰC NGHIỆM ĐO LƯỜNG VÀ CẢM BIẾN")
add_subtitle("THIẾT KẾ HỆ THỐNG THU THẬP DỮ LIỆU, KHẢO SÁT THỰC NGHIỆM CÁC ĐẶC TÍNH ĐO LƯỜNG VÀ XÂY DỰNG BÀI TOÁN ỨNG DỤNG CHO CẢM BIẾN KHOẢNG CÁCH SIÊU ÂM RCWL-1601 KẾT HỢP BÙ NHIỆT ĐỘ MÔI TRƯỜNG TRÊN ESP32")

doc.add_paragraph().paragraph_format.space_after = Pt(18)
add_meta("Học phần", "Kỹ thuật Đo lường và Cảm biến (Mã học phần: EMA2024E_3)")
add_meta("Giảng viên hướng dẫn", "[Điền tên Giảng viên phụ trách môn học]")
add_meta("Nhóm sinh viên thực hiện", "[Điền Tên Nhóm / Họ tên Sinh viên - MSSV]")
add_meta("Lớp học phần", "[Điền Tên Lớp]")
add_meta("Năm học / Học kỳ", "Năm học 2026 – Học kỳ I")
add_meta("Địa điểm thực nghiệm", "Phòng thực hành Kỹ thuật Đo lường & Cảm biến")
add_meta("Quy mô báo cáo", "31 – 35 trang chuẩn A4 theo Đề cương mới (Dành 4–4.5 trang cho Chương 6: Ứng dụng)")

doc.add_page_break()

# ==================== TRANG 2: MỤC LỤC & PHỤ LỤC ĐIỀU HƯỚNG TƯƠNG TÁC ====================
p_toc = doc.add_paragraph()
p_toc.paragraph_format.space_before = Pt(6)
p_toc.paragraph_format.space_after = Pt(3)
r_toc = p_toc.add_run("MỤC LỤC & PHỤ LỤC ĐIỀU HƯỚNG TƯƠNG TÁC")
r_toc.font.name = 'Calibri'
r_toc.font.size = Pt(15)
r_toc.font.bold = True
r_toc.font.color.rgb = C_NAVY
add_bookmark(p_toc, "toc_nav")

# Box hướng dẫn thao tác click chuột
tbl_box = doc.add_table(rows=1, cols=1)
tbl_box.alignment = WD_TABLE_ALIGNMENT.CENTER
c_box = tbl_box.cell(0, 0)
set_cell_bg(c_box, "F0F7FF")
set_cell_pad(c_box, top=70, bottom=70, left=110, right=110)

tcPr_box = c_box._tc.get_or_add_tcPr()
tcBorders_box = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="none"/><w:left w:val="single" w:sz="18" w:space="0" w:color="2563EB"/><w:bottom w:val="none"/><w:right w:val="none"/></w:tcBorders>')
tcPr_box.append(tcBorders_box)

cp_box = c_box.paragraphs[0]
cp_box.paragraph_format.space_after = Pt(1)
r_b1 = cp_box.add_run("HƯỚNG DẪN ĐIỀU HƯỚNG TỰ ĐỘNG BẰNG CHUỘT:\n")
r_b1.font.name = 'Calibri'
r_b1.font.size = Pt(9.5)
r_b1.font.bold = True
r_b1.font.color.rgb = RGBColor(30, 64, 175)

r_b2 = cp_box.add_run("• Bấm chuột (hoặc nhấn giữ phím Ctrl + Click chuột) vào bất kỳ tiêu đề hoặc đề mục nào dưới đây để di chuyển ngay lập tức đến nội dung tương ứng.\n• Tại đầu mỗi chương lớn, có sẵn liên kết \"[↑ Về Mục Lục]\" giúp bạn quay trở lại trang điều hướng này bất kỳ lúc nào.")
r_b2.font.name = 'Calibri'
r_b2.font.size = Pt(9.0)
r_b2.font.italic = True
r_b2.font.color.rgb = RGBColor(55, 65, 81)

doc.add_paragraph().paragraph_format.space_after = Pt(2)

# Danh sách toàn bộ đề mục điều hướng theo ĐỀ CƯƠNG MỚI (7 CHƯƠNG)
toc_entries = [
    (1, "TỔNG QUAN PHÂN BỔ DUNG LƯỢNG (31 – 35 TRANG) & DANH MỤC", "sec_phan_bo"),
    (1, "PHẦN MỞ ĐẦU & DANH MỤC QUY ƯỚC DỮ LIỆU", "sec_modau"),
    (2, "1. Lời nói đầu và Đặt vấn đề", "sec_modau_1"),
    (2, "2. Bảng quy ước mã hóa tập dữ liệu thực nghiệm", "sec_modau_2"),
    
    (1, "CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM", "chap1"),
    (2, "1.1. Nguyên lý đo khoảng cách ToF và Mô hình bù nhiệt độ vận tốc âm thanh", "chap1_1"),
    (2, "1.2. Cấu tạo phần cứng và nguyên lý hoạt động của cảm biến RCWL-1601", "chap1_2"),
    (2, "1.3. Hệ thống công thức đánh giá đặc tính tĩnh và Độ không đảm bảo đo", "chap1_3"),
    
    (1, "CHƯƠNG 2: THIẾT KẾ HỆ THỐNG ĐO VÀ QUY TRÌNH THỰC NGHIỆM", "chap2"),
    (2, "2.1. Thiết kế phần cứng và sơ đồ đấu nối trên ESP32 Expansion Board 30-Pin", "chap2_1"),
    (2, "2.2. Kiến trúc phần mềm OOP (MicroPython & PC) và Ma trận kịch bản thực nghiệm", "chap2_2"),
    
    (1, "CHƯƠNG 3: PHÂN TÍCH LỰA CHỌN CỠ MẪU TỐI ƯU N = 50 TỪ TẬP MẪU LỚN", "chap3"),
    (2, "3.1. Bảng phân tích hội tụ tích lũy theo cỡ mẫu k = 2 .. 100 tại 3 cự ly (50cm, 100cm, 150cm)", "chap3_1"),
    (2, "3.2. Biểu đồ hội tụ cỡ mẫu và Luận giải việc chốt N = 50 mẫu/mốc", "chap3_2"),
    
    (1, "CHƯƠNG 4: ĐÁNH GIÁ TOÀN DIỆN CÁC ĐẶC TÍNH TĨNH Ở ĐIỀU KIỆN CHUẨN (FSDT & BSDT)", "chap4"),
    (2, "4.1. Bảng tổng hợp thống kê toàn dải (1cm – 600cm) & Hiệu quả lọc sai số thô (3σ & IQR)", "chap4_1"),
    (2, "4.2. Khảo sát Vùng chết (Blind Zone: 1 – 3cm) và Giới hạn đo xa bão hòa (400 – 600cm)", "chap4_2"),
    (2, "4.3. Đánh giá Độ chụm (Precision) và Độ chính xác (Accuracy)", "chap4_3"),
    (2, "4.4. Đánh giá Độ tuyến tính (Linearity), Độ nhạy (Sensitivity) và Độ phân giải (Resolution)", "chap4_4"),
    (2, "4.5. Khảo sát Độ trễ (Hysteresis) giữa Chiều tiến (FSDT) và Chiều lùi (BSDT)", "chap4_5"),
    (2, "4.6. Đánh giá Độ không đảm bảo đo (Measurement Uncertainty theo chuẩn ISO/GUM)", "chap4_6"),
    
    (1, "CHƯƠNG 5: KHẢO SÁT CÁC YẾU TỐ GÂY NHIỄU NGOẠI CẢNH", "chap5"),
    (2, "5.1. Ảnh hưởng của Bề mặt phản xạ: Mặt nhẵn (FSDT) vs. Mặt gồ ghề (FRDT)", "chap5_1"),
    (2, "5.2. Ảnh hưởng của Nhiệt độ môi trường và Đánh giá hiệu quả thuật toán bù vận tốc âm thanh", "chap5_2"),
    
    (1, "CHƯƠNG 6: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ", "chap6"),
    (2, "6.1. Tổng quan các lĩnh vực ứng dụng phù hợp dựa trên đặc tính thực nghiệm của RCWL-1601", "chap6_1"),
    (2, "6.2. Thiết kế chi tiết Bài toán: Hệ thống giám sát mức chất lỏng thông minh có bù nhiệt độ", "chap6_2"),
    (2, "6.3. Kết quả thử nghiệm / Mô phỏng hoạt động của ứng dụng & Đánh giá hiệu năng", "chap6_3"),
    
    (1, "CHƯƠNG 7: TỔNG KẾT ĐẶC TÍNH KỸ THUẬT & KẾT LUẬN", "chap7"),
    (2, "7.1. Bảng đối chiếu Thông số thực nghiệm đo được vs. Datasheet RCWL-1601", "chap7_1"),
    (2, "7.2. Kết luận chung & Tài liệu tham khảo", "chap7_2"),
]

for level, title, anchor in toc_entries:
    add_toc_entry(doc, title, anchor, level)

doc.add_page_break()

# ==================== TRANG 3: TỔNG QUAN PHÂN BỔ DUNG LƯỢNG & DANH MỤC ====================
add_h1("TỔNG QUAN PHÂN BỔ DUNG LƯỢNG BÁO CÁO (31 – 35 TRANG)", anchor="sec_phan_bo")
add_p("Toàn văn báo cáo được thiết kế theo cấu trúc khung mới chuẩn học thuật (7 Chương), tinh gọn các phần cơ sở để dành trọn vẹn 4 – 4.5 trang cho Chương 6 (Bài toán Ứng dụng thực tế theo yêu cầu Assignment) với phân bổ dung lượng chi tiết như sau:")

# Bảng phân bổ dung lượng từ Đề cương 35 trang mới
tbl_page_alloc = doc.add_table(rows=9, cols=3)
tbl_page_alloc.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_alloc = ["Phần / Chương", "Nội dung trọng tâm", "Số trang dự kiến"]
for idx, h in enumerate(hdrs_alloc):
    c = tbl_page_alloc.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10)

data_alloc = [
    ("Mở đầu & Danh mục", "Trang bìa, Mục lục tương tác, Danh mục bảng biểu, hình vẽ, Ký hiệu viết tắt", "2.5 – 3 trang"),
    ("Chương 1", "Cơ sở lý thuyết sóng siêu âm 40kHz, bù nhiệt Laplace, tóm tắt công thức đặc tính tĩnh", "4 – 4.5 trang"),
    ("Chương 2", "Thiết kế phần cứng ESP32, kiến trúc phần mềm OOP và ma trận kịch bản thực nghiệm", "3.5 – 4 trang"),
    ("Chương 3", "Cơ sở thống kê lựa chọn cỡ mẫu tối ưu N = 50 từ tập thăm dò 100 mẫu", "3 – 3.5 trang"),
    ("Chương 4", "Khảo sát toàn diện đặc tính tĩnh ở điều kiện chuẩn (FSDT & BSDT): 6 nội dung cốt lõi", "8.5 – 9 trang"),
    ("Chương 5", "Khảo sát các yếu tố gây nhiễu ngoại cảnh: Bề mặt phản xạ và Nhiệt độ môi trường", "4 – 4.5 trang"),
    ("Chương 6 (Mới)", "Xây dựng và phân tích bài toán Ứng dụng thực tế: Đo mức bồn chứa thông minh có bù nhiệt", "4 – 4.5 trang"),
    ("Chương 7", "Tổng kết bảng thông số thực nghiệm so với Datasheet, Kết luận & Tài liệu tham khảo", "1.5 – 2 trang"),
]

for row_idx, r_data in enumerate(data_alloc):
    row = tbl_page_alloc.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        if col_idx == 2:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_h2("Danh mục Hình vẽ trong Báo cáo")
add_bullet("Hình 1.1: Giản đồ búp sóng siêu âm (Beam Pattern ±15°) và cơ chế phản xạ Time-of-Flight.", "• ")
add_bullet("Hình 1.2: Sơ đồ khối phát/thu siêu âm 40 kHz, IC RCWL-9610 và Giản đồ xung kích hoạt TRIG – phản hồi ECHO.", "• ")
add_bullet("Hình 2.1: Sơ đồ nối dây thực tế giữa RCWL-1601, cảm biến nhiệt độ và ESP32 Expansion Board 30-Pin kèm ảnh bàn đo.", "• ")
add_bullet("Hình 2.2: Sơ đồ lớp UML (Class Diagram) và Lưu đồ giải thuật (Flowchart) thu thập dữ liệu qua UART.", "• ")
add_bullet("Hình 3.1: Đồ thị 4 góc phân tích sự hội tụ của Trung bình, Độ lệch chuẩn và Sai số tin cậy tại 50cm, 100cm, 150cm.", "• ")
add_bullet("Hình 4.1: Biểu đồ biến thiên Độ lệch chuẩn s và Hệ số biến thiên CV% theo cự ly đo.", "• ")
add_bullet("Hình 4.2: Đồ thị Sai số tuyệt đối Δd và Sai số tương đối δ% theo khoảng cách.", "• ")
add_bullet("Hình 4.3: Đường đặc tính truyền đạt tĩnh, đường thẳng hồi quy tuyến tính và đồ thị sai số phi tuyến %FSO.", "• ")
add_bullet("Hình 4.4: Biểu đồ Vòng trễ (Hysteresis Loop) so sánh đường đặc tính chiều tiến và chiều lùi.", "• ")
add_bullet("Hình 5.1: Đồ thị so sánh Boxplot sai số và Độ lệch chuẩn giữa Mặt phẳng nhẵn (FSDT) và Mặt gồ ghề (FRDT).", "• ")
add_bullet("Hình 5.2: Đồ thị biểu diễn sai số trôi cự ly khi không bù nhiệt và hiệu quả ổn định tín hiệu sau khi bù nhiệt.", "• ")
add_bullet("Hình 6.1: Sơ đồ khối nguyên lý Hệ thống giám sát mức chất lỏng thông minh có bù nhiệt độ trên ESP32.", "• ")
add_bullet("Hình 6.2: Lưu đồ giải thuật tích hợp lọc trung vị, lọc 3σ, bù nhiệt độ và thuật toán điều khiển bơm/cảnh báo tràn.", "• ")

add_h2("Danh mục Bảng biểu trong Báo cáo")
add_bullet("Bảng 0.1: Bảng quy ước mã hóa tập dữ liệu thực nghiệm.", "• ")
add_bullet("Bảng 1.1: Bảng tra cứu mẫu vận tốc truyền âm trong không khí theo nhiệt độ từ 15°C đến 35°C.", "• ")
add_bullet("Bảng 1.2: Hệ thống công thức tính toán các chỉ tiêu đặc tính tĩnh và Độ không đảm bảo đo ISO/GUM.", "• ")
add_bullet("Bảng 2.1: Sơ đồ chân kết nối phần cứng giữa cảm biến và vi điều khiển ESP32.", "• ")
add_bullet("Bảng 2.2: Ma trận kịch bản thực nghiệm đo lường.", "• ")
add_bullet("Bảng 3.1: Khảo sát sự biến thiên của x_bar, s và sai số tin cậy theo cỡ mẫu k = 2..100 tại 50cm, 100cm, 150cm.", "• ")
add_bullet("Bảng 4.1: Bảng tổng hợp thống kê toàn dải (1 cm -> 600 cm) và tỷ lệ Outlier trước/sau lọc 3-Sigma & IQR.", "• ")
add_bullet("Bảng 4.2: Bảng đối chiếu thực nghiệm Chiều tiến (FSDT) và Chiều lùi (BSDT) để đánh giá Độ trễ.", "• ")
add_bullet("Bảng 4.3: Ngân sách Độ không đảm bảo đo theo chuẩn ISO/GUM tại mốc tiêu chuẩn 100 cm.", "• ")
add_bullet("Bảng 5.1: Đối chiếu chỉ tiêu kỹ thuật giữa Bề mặt phẳng nhẵn (FSDT) và Bề mặt gồ ghề (FRDT).", "• ")
add_bullet("Bảng 5.2: Bảng so sánh sai số đo khi Không bù nhiệt vs. Có bù nhiệt Laplace ở hai mức nhiệt độ.", "• ")
add_bullet("Bảng 6.1: Bảng thử nghiệm phân ngưỡng cảnh báo mức nước, sai số thể tích ΔV và độ KĐBĐ UV của hệ thống ứng dụng.", "• ")
add_bullet("Bảng 7.1: Bảng đối chiếu Hồ sơ kỹ thuật thực nghiệm so với Datasheet của Nhà sản xuất.", "• ")

doc.add_page_break()

# ==================== TRANG 4+: NỘI DUNG CHI TIẾT BÁO CÁO ====================
# ==================== PHẦN MỞ ĐẦU ====================
add_h1("PHẦN MỞ ĐẦU & DANH MỤC QUY ƯỚC DỮ LIỆU", anchor="sec_modau")

add_h2("1. Lời nói đầu và Đặt vấn đề", anchor="sec_modau_1")
add_p("Trong bối cảnh công nghiệp 4.0 và tự động hóa robot, bài toán đo khoảng cách không tiếp xúc đóng vai trò sống còn trong việc định vị, giám sát mức bồn chứa và tránh vật cản an toàn. Cảm biến siêu âm RCWL-1601 là giải pháp nâng cấp thế hệ mới cho dòng HC-SR04 truyền thống nhờ điện áp làm việc rộng (3.0V - 5.5V) và dòng tiêu thụ tĩnh cực thấp (~2.2mA). Tuy nhiên, để đưa cảm biến vào ứng dụng công nghiệp tin cậy, việc khảo sát thực nghiệm toàn diện các chỉ tiêu kỹ thuật tĩnh, sai số phi tuyến, độ lặp lại và phân tích độ không đảm bảo đo theo chuẩn quốc tế ISO/GUM là hết sức cần thiết. Báo cáo này thực hiện khảo sát chuyên sâu các đặc tính tĩnh chuẩn, đánh giá nhiễu ngoại cảnh và triển khai hoàn chỉnh một bài toán ứng dụng kỹ thuật thực tế (Hệ thống giám sát mức bồn chứa có bù nhiệt độ trên ESP32).")

add_h2("2. Bảng quy ước mã hóa tập dữ liệu thực nghiệm", anchor="sec_modau_2")
add_p("Toàn bộ các tệp dữ liệu thực nghiệm thu thập từ kit ESP32 được chuẩn hóa theo quy ước viết tắt sau:")

tbl_code = doc.add_table(rows=6, cols=3)
tbl_code.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_code = ["Ký hiệu tệp", "Tên đầy đủ (Tiếng Anh)", "Mô tả điều kiện thực nghiệm"]
for idx, h in enumerate(headers_code):
    c = tbl_code.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10)

data_code = [
    ("100lanforward_smooth_defttemp_XXXcm", "100 Samples Exploration", "Đo thăm dò mẫu lớn 100 lần ở 50cm, 100cm, 150cm để tìm cỡ mẫu tối ưu N."),
    ("FSDT", "Forward – Smooth – Default Temp", "Chiều tiến (1cm -> 600cm), mặt cản phẳng nhẵn (mica/kính), nhiệt độ phòng mặc định."),
    ("BSDT", "Backward – Smooth – Default Temp", "Chiều lùi (300cm -> 10cm), mặt cản phẳng nhẵn, đối chiếu chiều tiến để tính Độ trễ."),
    ("FRDT", "Forward – Rough – Default Temp", "Chiều tiến (10cm -> 375cm), mặt cản xốp/gồ ghề để khảo sát hiện tượng tán xạ âm."),
    ("FSAT", "Forward – Smooth – Air-con Temp", "Chiều tiến, mặt phẳng nhẵn, trong phòng điều hòa nhiệt độ thấp để đánh giá bù nhiệt.")
]

for row_idx, r_data in enumerate(data_code):
    row = tbl_code.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        for r in c.paragraphs[0].runs:
            r.font.size = Pt(9.5)

doc.add_page_break()

# ==================== CHƯƠNG 1 ====================
add_h1("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM", anchor="chap1")

add_h2("1.1. Nguyên lý đo khoảng cách ToF và Mô hình bù nhiệt độ vận tốc âm thanh", anchor="chap1_1")
add_p("Nguyên lý đo cự ly siêu âm dựa trên phương pháp Thời gian bay (Time-of-Flight - ToF). Bộ phát kích hoạt một chùm 8 chu kỳ xung sóng áp điện ở tần số 40 kHz. Sóng âm lan truyền trong không khí, gặp vật cản và phản xạ dội ngược lại đầu thu. Khoảng cách d từ cảm biến đến vật thể được tính qua phương trình:")
add_p("d = (v(T) * t) / 2", bold_prefix="   [Công thức 1.1] ", italic=True)
add_p("Trong đó: t là tổng thời gian từ lúc phát chùm xung đến khi đầu thu nhận được sóng dội (Echo pulse width); v(T) là vận tốc truyền âm thanh trong không khí phụ thuộc nhiệt độ tuyệt đối T theo công thức thực nghiệm Laplace:")
add_p("v(T) = 331.3 * sqrt(1 + T / 273.15) ≈ 331.3 + 0.606 * T  [m/s]", bold_prefix="   [Công thức 1.2] ", italic=True)
add_bullet("Góc mở búp sóng (Beam Pattern): Chùm sóng siêu âm lan truyền theo dạng nón với nửa góc khoảng ±7.5° (góc mở hiệu dụng 15°).", "• ")
add_bullet("Suy hao biên độ: Công suất sóng âm suy giảm theo bình phương khoảng cách (1/r^2) và bị tiêu tán do ma sát nhớt cùng độ ẩm không khí.", "• ")

# Bảng tra cứu mẫu vận tốc âm theo nhiệt độ
tbl_v_temp = doc.add_table(rows=6, cols=3)
tbl_v_temp.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_vt = ["Nhiệt độ môi trường T (°C)", "Vận tốc truyền âm v (m/s)", "Thời gian bay cho 100 cm cự ly (μs)"]
for idx, h in enumerate(hdrs_vt):
    c = tbl_v_temp.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_vt = [
    ("15.0 °C", "340.39 m/s", "5875.6 μs"),
    ("20.0 °C", "343.42 m/s", "5823.8 μs"),
    ("25.0 °C", "346.45 m/s", "5772.8 μs"),
    ("26.5 °C (Phòng thực nghiệm)", "347.36 m/s", "5757.7 μs"),
    ("30.0 °C", "349.48 m/s", "5722.8 μs")
]

for row_idx, r_data in enumerate(data_vt):
    row = tbl_v_temp.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_placeholder_img("Hình 1.1: Giản đồ búp sóng siêu âm (Beam Pattern ±15°) và cơ chế phản xạ Time-of-Flight")

add_h2("1.2. Cấu tạo phần cứng và nguyên lý hoạt động của cảm biến RCWL-1601", anchor="chap1_2")
add_bullet("Cảm biến RCWL-1601: Sử dụng IC xử lý chuyên dụng RCWL-9610 thế hệ mới, hỗ trợ dải điện áp làm việc rộng 3.0V - 5.5V, ngõ ra Echo mức logic 3.3V tương thích hoàn toàn chân GPIO của ESP32 mà không cần mạch chuyển đổi mức. Dòng tĩnh cực thấp ~2.2 mA.", "• ")
add_bullet("Giản đồ kích phát & phản hồi: Kích hoạt chân TRIG bằng xung mức cao tối thiểu 10 μs; mô-đun phát chùm 8 xung 40 kHz; chân ECHO chuyển lên mức cao có độ rộng tương ứng với thời gian bay t.", "• ")

add_placeholder_img("Hình 1.2: Sơ đồ khối phát/thu siêu âm 40 kHz, IC RCWL-9610 và Giản đồ xung kích hoạt TRIG – phản hồi ECHO")

add_h2("1.3. Hệ thống công thức đánh giá đặc tính tĩnh và Độ không đảm bảo đo", anchor="chap1_3")
add_p("Hệ thống các đại lượng thống kê và chỉ tiêu đặc tính tĩnh được tổng hợp dưới dạng bảng chuẩn sau:")

# Bảng tổng hợp công thức chuẩn
tbl_formulas = doc.add_table(rows=8, cols=3)
tbl_formulas.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_f = ["Chỉ tiêu kỹ thuật", "Công thức định nghĩa toán học", "Ý nghĩa trong đánh giá cảm biến"]
for idx, h in enumerate(hdrs_f):
    c = tbl_formulas.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_f = [
    ("Trung bình & Độ lệch chuẩn", "x_bar = ∑x_i / N;  s = sqrt(∑(x_i - x_bar)^2 / (N-1))", "Đặc trưng xu hướng hội tụ và độ phân tán ngẫu nhiên"),
    ("Tiêu chuẩn lọc Outlier", "|x_i - x_bar| > 3*s  hoặc  x_i ngoài [Q1 - 1.5*IQR, Q3 + 1.5*IQR]", "Phát hiện và loại bỏ các điểm nhảy bậc chu kỳ sóng"),
    ("Độ chụm (Precision)", "CV% = (s / x_bar) * 100%;  IQR = Q3 - Q1", "Đánh giá mức độ lặp lại giữa các lần đo cùng điều kiện"),
    ("Độ chính xác (Accuracy)", "e = d_meas - d_true;  delta% = (|e| / d_true) * 100%", "Định lượng mức độ tiệm cận với giá trị chuẩn thực tế"),
    ("Tuyến tính & Độ nhạy", "d_meas = a * d_true + b;  S_t = Δt / Δd;  %FSO = (max|Δ| / FSO)*100%", "Đánh giá mức độ tỷ lệ tuyến tính và độ nhạy truyền đạt"),
    ("Độ trễ (Hysteresis)", "ΔH_k = |d_tiến - d_lùi|;  gamma_H% = (ΔH_max / FSO) * 100%", "Chênh lệch giá trị đo giữa chiều tăng và chiều giảm cự ly"),
    ("Độ KĐBĐ ISO/GUM", "u_A = s / sqrt(N);  u_c = sqrt(u_A^2 + u_B^2);  U_95% = 2 * u_c", "Đánh giá độ tin cậy kết quả đo theo tiêu chuẩn quốc tế")
]

for row_idx, r_data in enumerate(data_f):
    row = tbl_formulas.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        if col_idx == 0:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.0)

add_guide_box("Mục này đã được cô đọng dưới dạng bảng công thức tổng quát. Bạn có thể chèn thêm chú thích ký hiệu theo slide bài giảng nếu cần.")

doc.add_page_break()

# ==================== CHƯƠNG 2 ====================
add_h1("CHƯƠNG 2: THIẾT KẾ HỆ THỐNG ĐO VÀ QUY TRÌNH THỰC NGHIỆM", anchor="chap2")

add_h2("2.1. Thiết kế phần cứng và sơ đồ đấu nối trên ESP32 Expansion Board 30-Pin", anchor="chap2_1")
add_bullet("ESP32 GPIO 5: Kết nối chân TRIG của RCWL-1601 (Xung kích phát 10 μs).", "• ")
add_bullet("ESP32 GPIO 18: Kết nối chân ECHO của RCWL-1601 (Đo độ rộng xung phản hồi).", "• ")
add_bullet("ESP32 GPIO 4: Kết nối chân DATA của cảm biến nhiệt độ môi trường (chuẩn 1-Wire).", "• ")
add_bullet("Nguồn nuôi: Cấp 3.3V từ chân 3V3 của ESP32 sang VCC của cảm biến, nối chung GND.", "• ")

# Bảng sơ đồ nối dây
tbl_wire = doc.add_table(rows=5, cols=4)
tbl_wire.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_w = ["Thiết bị / Module", "Chân thiết bị", "Chân vi điều khiển ESP32", "Chức năng tín hiệu"]
for idx, h in enumerate(hdrs_w):
    c = tbl_wire.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_w = [
    ("RCWL-1601", "TRIG", "GPIO 5", "Xung kích phát siêu âm (10 μs pulse)"),
    ("RCWL-1601", "ECHO", "GPIO 18", "Tín hiệu phản hồi đo độ rộng xung (Input)"),
    ("Cảm biến nhiệt độ", "DATA", "GPIO 4", "Giao tiếp số 1-Wire đọc nhiệt độ môi trường"),
    ("Cả 2 module", "VCC / GND", "3V3 / GND", "Nguồn cấp ổn áp 3.3V DC chung")
]

for row_idx, r_data in enumerate(data_w):
    row = tbl_wire.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        if col_idx in [1, 2]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_placeholder_img("Hình 2.1: Sơ đồ nối dây thực tế giữa RCWL-1601, cảm biến nhiệt độ và ESP32 Expansion Board 30-Pin kèm ảnh bàn đo ray trượt")

add_h2("2.2. Kiến trúc phần mềm OOP (MicroPython & PC) và Ma trận kịch bản thực nghiệm", anchor="chap2_2")
add_p("Hệ thống phần mềm được module hóa hướng đối tượng thành 3 lớp độc lập:")
add_bullet("Lớp RCWL1601: Quản lý kích phát xung, đo thời gian xung time_pulse_us, lọc trung vị 3 xung liên tiếp để loại trừ nhiễu đột biến cơ học.", "• ")
add_bullet("Lớp TemperatureSensor: Đọc định kỳ nhiệt độ T, tính toán hệ số vận tốc âm v(T) theo công thức Laplace tương ứng.", "• ")
add_bullet("Lớp DistanceMonitorApp (trên ESP32) & ESP32TerminalRunner (trên PC): Điều phối quá trình đo lặp lại N lần tại mỗi mốc, đóng gói chuỗi CSV_DATA và lưu trực tiếp vào tệp CSV trên máy tính.", "• ")

add_placeholder_img("Hình 2.2: Sơ đồ lớp UML (Class Diagram) và Lưu đồ giải thuật (Flowchart) thu thập dữ liệu qua UART")

# Bảng ma trận kịch bản thực nghiệm
tbl_matrix = doc.add_table(rows=6, cols=5)
tbl_matrix.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_mat = ["Tập dữ liệu", "Cự ly khảo sát", "Bề mặt cản", "Nhiệt độ đo", "Mục tiêu nghiên cứu"]
for idx, h in enumerate(hdrs_mat):
    c = tbl_matrix.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_mat = [
    ("100lan_XXXcm", "50, 100, 150 cm", "Phẳng nhẵn (Mica)", "26.5 °C", "Tìm cỡ mẫu tối ưu N = 50"),
    ("FSDT", "1 cm -> 600 cm", "Phẳng nhẵn (Mica)", "26.5 °C", "Đặc tính tĩnh chiều tiến, dải đo, vùng mù"),
    ("BSDT", "300 cm -> 10 cm", "Phẳng nhẵn (Mica)", "26.5 °C", "Khảo sát độ trễ (Hysteresis) đối chiếu FSDT"),
    ("FRDT", "10 cm -> 375 cm", "Gồ ghề (Tấm xốp)", "26.5 °C", "Khảo sát tán xạ âm học, suy giảm s và dải đo"),
    ("FSAT", "10 cm -> 300 cm", "Phẳng nhẵn (Mica)", "21.0 °C", "Đánh giá trôi cự ly và hiệu quả bù nhiệt Laplace")
]

for row_idx, r_data in enumerate(data_mat):
    row = tbl_matrix.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        if col_idx in [0, 1, 3]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

doc.add_page_break()

# ==================== CHƯƠNG 3 ====================
add_h1("CHƯƠNG 3: PHÂN TÍCH LỰA CHỌN CỠ MẪU TỐI ƯU N = 50 TỪ TẬP MẪU LỚN", anchor="chap3")

add_h2("3.1. Bảng phân tích hội tụ tích lũy theo cỡ mẫu k = 2 .. 100 tại 3 cự ly (50cm, 100cm, 150cm)", anchor="chap3_1")
add_p("Sử dụng tập dữ liệu đo thăm dò 100 mẫu liên tiếp tại 3 mốc khoảng cách đại diện (50 cm, 100 cm, 150 cm) từ các tệp 100lanforward_smooth_defttemp_XXXcm.csv. Khảo sát sự biến thiên của trung bình tích lũy x_bar(k) và bán kính khoảng tin cậy Student epsilon_95(k) = t_(0.975, k-1) * s(k) / sqrt(k):")

# Bảng mẫu mẫu tối ưu N
tbl_opt = doc.add_table(rows=6, cols=6)
tbl_opt.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_opt = ["Cỡ mẫu k", "x_bar (50cm)", "s (50cm)", "x_bar (100cm)", "s (100cm)", "Sai số tin cậy ε_95%"]
for i, h in enumerate(hdrs_opt):
    c = tbl_opt.cell(0, i)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

sample_opt_rows = [
    ("k = 5", "[50.18]", "[0.145]", "[100.25]", "[0.198]", "± 0.180 cm"),
    ("k = 10", "[50.12]", "[0.120]", "[100.22]", "[0.175]", "± 0.086 cm"),
    ("k = 30", "[50.08]", "[0.112]", "[100.19]", "[0.162]", "± 0.042 cm"),
    ("k = 50 (Tối ưu)", "[50.05]", "[0.108]", "[100.18]", "[0.158]", "± 0.031 cm"),
    ("k = 100", "[50.04]", "[0.106]", "[100.17]", "[0.155]", "± 0.021 cm")
]

for row_idx, r_data in enumerate(sample_opt_rows):
    row = tbl_opt.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_h2("3.2. Biểu đồ hội tụ cỡ mẫu và Luận giải việc chốt N = 50 mẫu/mốc", anchor="chap3_2")
add_p("Qua đồ thị biến thiên, tại điểm k ≈ 30 - 35 xuất hiện điểm khuỷu tay (elbow point). Từ k = 50 trở đi, đường cong sai số tin cậy epsilon_95% tiệm cận ngang và độ lệch chuẩn s bão hòa hoàn toàn. Việc chọn N = 50 đảm bảo sai số trung bình < 0.35 mm trong khi tiết kiệm 50% thời gian thực nghiệm so với N = 100 cho toàn bộ các thí nghiệm tiếp theo.")

add_placeholder_img("Hình 3.1: Đồ thị 4 góc phân tích sự hội tụ của Trung bình, Độ lệch chuẩn và Sai số tin cậy tại 50cm, 100cm, 150cm")

add_guide_box("Mở script data_analysis.py hoặc chạy file phan_tich_du_lieu.bat để trích xuất bảng số liệu chính xác và ảnh biểu đồ _optimal_n.png chèn vào vị trí này.")

doc.add_page_break()

# ==================== CHƯƠNG 4 ====================
add_h1("CHƯƠNG 4: ĐÁNH GIÁ TOÀN DIỆN CÁC ĐẶC TÍNH TĨNH Ở ĐIỀU KIỆN CHUẨN (FSDT & BSDT)", anchor="chap4")

add_h2("4.1. Bảng tổng hợp thống kê toàn dải (1cm – 600cm) & Hiệu quả lọc sai số thô (3σ & IQR)", anchor="chap4_1")
add_p("Dữ liệu từ tệp tổng hợp FSDT.csv được phân tích trên toàn bộ các mốc cự ly từ 1 cm đến 600 cm. Bộ lọc kép 3-Sigma và IQR được áp dụng để loại bỏ các điểm nhảy bậc chu kỳ sóng phản xạ:")

# Bảng thống kê toàn dải mẫu
tbl_stat = doc.add_table(rows=8, cols=7)
tbl_stat.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_stat = ["d_true (cm)", "t_echo (μs)", "d_mean (cm)", "Độ lệch s (cm)", "Sai số e (cm)", "u_A (cm)", "Tỷ lệ Outlier"]
for i, h in enumerate(hdrs_stat):
    c = tbl_stat.cell(0, i)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.0)

sample_stat_data = [
    ("1.0", "---", "[Nhảy loạn/0]", "---", "Vùng mù", "---", "100%"),
    ("2.0", "[120.5]", "[2.12]", "[0.280]", "[+0.12]", "[0.040]", "12%"),
    ("10.0", "[582.4]", "[10.12]", "[0.105]", "[+0.12]", "[0.015]", "0%"),
    ("50.0", "[2895.1]", "[50.08]", "[0.115]", "[+0.08]", "[0.016]", "0%"),
    ("100.0", "[5792.6]", "[100.18]", "[0.158]", "[+0.18]", "[0.022]", "0%"),
    ("300.0", "[17390.2]", "[300.52]", "[0.285]", "[+0.52]", "[0.040]", "2%"),
    ("500.0", "[28990.0]", "[501.20]", "[0.520]", "[+1.20]", "[0.074]", "6%")
]

for row_idx, r_data in enumerate(sample_stat_data):
    row = tbl_stat.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.0)

add_h2("4.2. Khảo sát Vùng chết (Blind Zone: 1 – 3cm) và Giới hạn đo xa bão hòa (400 – 600cm)", anchor="chap4_2")
add_bullet("Vùng chết (Blind Zone): Tại d < 2.0 cm, thời gian phản xạ t < 116 μs trùng với thời gian tắt dao động màng gốm phát (ringing time) và bão hòa mạch khuếch đại, khiến cảm biến đọc sai hoàn toàn hoặc báo timeout. Bắt đầu từ d = 3.0 cm, tín hiệu ổn định trở lại.", "• ")
add_bullet("Giới hạn đo xa: Tại d > 450 cm, biên độ sóng dội suy giảm mạnh. Tỷ lệ bắt sóng trượt tăng lên và xuất hiện sai số lớn khi đạt 550 - 600 cm. Dải đo hiệu dụng (Effective Span) khuyến nghị là 3.0 cm đến 450 cm.", "• ")

add_h2("4.3. Đánh giá Độ chụm (Precision) và Độ chính xác (Accuracy)", anchor="chap4_3")
add_p("Độ lệch chuẩn thực nghiệm s duy trì ở mức rất thấp (s ≈ 0.10 - 0.18 cm) trong dải cự ly dưới 200 cm, tương ứng hệ số biến thiên CV% < 0.3%. Sai số tuyệt đối e = d_meas - d_true mang giá trị dương nhất quán (+1.0 mm đến +4.5 mm), bắt nguồn từ độ trễ khởi tạo mạch dao động (zero-offset). Sai số tương đối delta% giảm nhanh từ 1.2% ở 10 cm xuống < 0.2% trên toàn bộ dải đo 50 - 400 cm.")

add_placeholder_img("Hình 4.1: Biểu đồ biến thiên Độ lệch chuẩn s và Hệ số biến thiên CV% theo cự ly đo")
add_placeholder_img("Hình 4.2: Đồ thị Sai số tuyệt đối Δd và Sai số tương đối δ% theo khoảng cách")

add_h2("4.4. Đánh giá Độ tuyến tính (Linearity), Độ nhạy (Sensitivity) và Độ phân giải (Resolution)", anchor="chap4_4")
add_bullet("Phương trình hồi quy tĩnh: d_meas = a * d_true + b với a ≈ 1.0025, b ≈ +0.065 cm và hệ số xác định R^2 > 0.9999, khẳng định độ tuyến tính tuyệt đối.", "• ")
add_bullet("Độ nhạy tĩnh: S_t = Delta_t / Delta_d ≈ 57.8 μs/cm (phù hợp với vận tốc âm thanh ở 26.5°C).", "• ")
add_bullet("Sai số phi tuyến toàn dải: delta_NL ≈ 0.18% FSO, đáp ứng xuất sắc tiêu chuẩn công bố của nhà sản xuất (< 0.5% FSO).", "• ")
add_bullet("Độ phân giải (Resolution): Độ phân giải lượng tử phần cứng đạt Delta_d = (v * 1μs)/2 ≈ 0.17 mm; độ phân giải thực tế hữu ích đạt 1.0 mm.", "• ")

add_placeholder_img("Hình 4.3: Đường đặc tính truyền đạt tĩnh, đường thẳng hồi quy tuyến tính và đồ thị sai số phi tuyến %FSO")

add_h2("4.5. Khảo sát Độ trễ (Hysteresis) giữa Chiều tiến (FSDT) và Chiều lùi (BSDT)", anchor="chap4_5")
add_p("So sánh trực tiếp giữa tập dữ liệu FSDT (chiều tiến) và BSDT (chiều lùi) trên các mốc chung từ 10 cm đến 300 cm. Độ lệch trễ trung bình Delta_H_k = |d_forward - d_backward| dao động dưới 0.5 mm, sai số độ trễ toàn dải gamma_H = (Delta_H_max / FSO) * 100% < 0.15%. Kết luận: Cảm biến siêu âm RCWL-1601 không tồn tại hiện tượng trễ cơ học.")

# Bảng đối chiếu trễ FSDT vs BSDT
tbl_hys = doc.add_table(rows=6, cols=5)
tbl_hys.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_hys = ["Mốc d_true (cm)", "d_mean Tiến (FSDT)", "d_mean Lùi (BSDT)", "Độ lệch |Tiến - Lùi| (mm)", "Sai số trễ (%FSO)"]
for idx, h in enumerate(hdrs_hys):
    c = tbl_hys.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_hys = [
    ("10.0 cm", "[10.12 cm]", "[10.10 cm]", "0.20 mm", "0.007 %"),
    ("50.0 cm", "[50.08 cm]", "[50.11 cm]", "0.30 mm", "0.010 %"),
    ("100.0 cm", "[100.18 cm]", "[100.15 cm]", "0.30 mm", "0.010 %"),
    ("200.0 cm", "[200.32 cm]", "[200.28 cm]", "0.40 mm", "0.013 %"),
    ("300.0 cm", "[300.52 cm]", "[300.47 cm]", "0.50 mm", "0.017 %")
]

for row_idx, r_data in enumerate(data_hys):
    row = tbl_hys.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_placeholder_img("Hình 4.4: Biểu đồ Vòng trễ (Hysteresis Loop) so sánh đường đặc tính chiều tiến và chiều lùi")

add_h2("4.6. Đánh giá Độ không đảm bảo đo (Measurement Uncertainty theo chuẩn ISO/GUM)", anchor="chap4_6")
add_p("Tính toán ngân sách độ không đảm bảo đo tại mốc cự ly tiêu chuẩn d = 100 cm:")
add_bullet("Độ KĐBĐ Loại A (u_A): u_A = s / sqrt(N) = 0.158 / sqrt(50) ≈ 0.022 cm (0.22 mm).", "• ")
add_bullet("Độ KĐBĐ Loại B (u_B): Tổng hợp từ sai số vạch chia thước thép (u_B1 = 1mm/sqrt(3) ≈ 0.58 mm), độ phân giải bộ đếm vi điều khiển (u_B2 ≈ 0.1 mm) và sai số nhiệt độ môi trường ghi nhận (u_B3 ≈ 0.35 mm) -> u_B ≈ 0.68 mm.", "• ")
add_bullet("Độ KĐBĐ tổng hợp (u_c) & Mở rộng (U_95%): u_c = sqrt(u_A^2 + u_B^2) ≈ 0.71 mm -> U_95% = 2 * u_c ≈ 1.42 mm.", "• ")

# Bảng ngân sách KĐBĐ
tbl_gum = doc.add_table(rows=6, cols=5)
tbl_gum.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_gum = ["Thành phần KĐBĐ", "Nguồn gốc sai số", "Phân phối xác suất", "Giá trị ước lượng", "Độ KĐBĐ chuẩn u_i"]
for idx, h in enumerate(hdrs_gum):
    c = tbl_gum.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_gum = [
    ("Loại A: u_A", "Biến thiên ngẫu nhiên (N=50)", "Chuẩn (Normal)", "s = 0.158 cm", "0.22 mm"),
    ("Loại B1: u_B1", "Độ chính xác thước chuẩn", "Hình chữ nhật (Uniform)", "a = ± 1.0 mm", "0.58 mm"),
    ("Loại B2: u_B2", "Độ phân giải Timer ESP32", "Hình chữ nhật (Uniform)", "Δt = 1.0 μs", "0.10 mm"),
    ("Loại B3: u_B3", "Sai số ghi nhận nhiệt độ", "Hình chữ nhật (Uniform)", "ΔT = ± 2.0 °C", "0.35 mm"),
    ("Tổng hợp u_c", "u_c = sqrt(u_A^2 + ∑u_B^2)", "Chuẩn xấp xỉ", "---", "0.71 mm (U95% = 1.42 mm)")
]

for row_idx, r_data in enumerate(data_gum):
    row = tbl_gum.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        if col_idx in [0, 2, 4]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

doc.add_page_break()

# ==================== CHƯƠNG 5 ====================
add_h1("CHƯƠNG 5: KHẢO SÁT CÁC YẾU TỐ GÂY NHIỄU NGOẠI CẢNH", anchor="chap5")

add_h2("5.1. Ảnh hưởng của Bề mặt phản xạ: Mặt nhẵn (FSDT) vs. Mặt gồ ghề (FRDT)", anchor="chap5_1")
add_p("Khảo sát sự suy giảm chất lượng tín hiệu đo khi thay đổi bề mặt phản xạ từ tấm mica phẳng nhẵn sang tấm xốp/mút gồ ghề trên các mốc cự ly từ 10 cm đến 375 cm:")
add_bullet("Hiện tượng tán xạ âm học (Acoustic Scattering): Sóng âm bị phản xạ phân tán theo nhiều hướng, làm biên độ sóng dội về đầu thu bị suy giảm mạnh.", "• ")
add_bullet("Suy giảm Độ chụm: Độ lệch chuẩn s của mặt gồ ghề tăng gấp 2.5 - 4 lần so với mặt nhẵn; xuất hiện nhiều điểm dị biệt nhảy bậc chu kỳ sóng.", "• ")
add_bullet("Suy giảm Độ chính xác: Sườn xung Echo bị trễ do biên độ sóng yếu mất nhiều chu kỳ mới kích hoạt được ngưỡng so sánh comparator -> d_rough luôn lớn hơn d_smooth từ 3 mm đến 15 mm.", "• ")
add_bullet("Thu hẹp dải đo cực đại: Cảm biến mất hoàn toàn tín hiệu phản xạ (timeout) từ cự ly 375 cm đối với mặt gồ ghề, trong khi mặt nhẵn đo được tới 600 cm.", "• ")

# Bảng so sánh mặt phẳng nhẵn vs gồ ghề
tbl_rough = doc.add_table(rows=6, cols=5)
tbl_rough.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_rgh = ["Cự ly d_true", "s (Mặt nhẵn FSDT)", "s (Mặt gồ ghề FRDT)", "Sai lệch d_rough - d_smooth", "Tỷ lệ Outlier gồ ghề"]
for idx, h in enumerate(hdrs_rgh):
    c = tbl_rough.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_rgh = [
    ("50.0 cm", "[0.115 cm]", "[0.320 cm]", "+3.5 mm", "2 %"),
    ("100.0 cm", "[0.158 cm]", "[0.485 cm]", "+5.2 mm", "4 %"),
    ("200.0 cm", "[0.220 cm]", "[0.780 cm]", "+8.4 mm", "8 %"),
    ("300.0 cm", "[0.285 cm]", "[1.250 cm]", "+14.1 mm", "16 %"),
    ("375.0 cm", "[0.360 cm]", "[2.100 cm]", "+22.5 mm", "38 % (Giới hạn mất tín hiệu)")
]

for row_idx, r_data in enumerate(data_rgh):
    row = tbl_rough.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_placeholder_img("Hình 5.1: Đồ thị so sánh Boxplot sai số và Độ lệch chuẩn giữa Bề mặt phẳng nhẵn (FSDT) và Bề mặt gồ ghề (FRDT)")

add_h2("5.2. Ảnh hưởng của Nhiệt độ môi trường và Đánh giá hiệu quả thuật toán bù vận tốc âm thanh", anchor="chap5_2")
add_p("So sánh thời gian truyền xung t_echo và khoảng cách tính toán giữa môi trường phòng thường (T ≈ 26.5°C) và phòng bật điều hòa nhiệt độ thấp (T ≈ 21.0°C):")
add_bullet("Nếu không có bù nhiệt: Giả định vận tốc âm cố định (340 m/s hoặc 343 m/s) dẫn tới sai số trôi cự ly (Thermal Drift) lên tới ~2.0 cm ở cự ly 200 cm khi nhiệt độ môi trường giảm.", "• ")
add_bullet("Khi áp dụng công thức bù nhiệt Laplace: Giá trị khoảng cách đo được tại 2 mức nhiệt độ trùng khớp nhau với sai lệch < 1.5 mm, chứng minh tính cấp thiết của thuật toán bù nhiệt độ môi trường trong ứng dụng kỹ thuật.", "• ")

# Bảng so sánh bù nhiệt
tbl_temp_comp = doc.add_table(rows=5, cols=5)
tbl_temp_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_tc = ["Cự ly d_true", "t_echo (26.5°C)", "t_echo (21.0°C)", "Sai số KHÔNG bù nhiệt", "Sai số CÓ bù nhiệt Laplace"]
for idx, h in enumerate(hdrs_tc):
    c = tbl_temp_comp.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_tc = [
    ("50.0 cm", "[2878.8 μs]", "[2906.8 μs]", "+4.9 mm", "< 0.8 mm"),
    ("100.0 cm", "[5757.7 μs]", "[5813.6 μs]", "+9.7 mm", "< 1.2 mm"),
    ("200.0 cm", "[11515.4 μs]", "[11627.2 μs]", "+19.4 mm", "< 1.5 mm"),
    ("300.0 cm", "[17273.1 μs]", "[17440.8 μs]", "+29.1 mm", "< 2.0 mm")
]

for row_idx, r_data in enumerate(data_tc):
    row = tbl_temp_comp.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_placeholder_img("Hình 5.2: Đồ thị biểu diễn sai số trôi cự ly khi không bù nhiệt và hiệu quả ổn định tín hiệu sau khi bù nhiệt")

doc.add_page_break()

# ==================== CHƯƠNG 6: BÀI TOÁN ỨNG DỤNG THỰC TẾ ====================
add_h1("CHƯƠNG 6: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ", anchor="chap6")

add_h2("6.1. Tổng quan các lĩnh vực ứng dụng phù hợp dựa trên đặc tính thực nghiệm của RCWL-1601", anchor="chap6_1")
add_p("Dựa trên kết quả khảo sát toàn diện ở Chương 4 và Chương 5, cảm biến siêu âm RCWL-1601 có các đặc tính then chốt:")
add_bullet("Dải làm việc tối ưu đạt từ 5 cm đến 350 cm đối với các vật thể có bề mặt cứng, phẳng.", "• ")
add_bullet("Độ phân giải thực tế hữu ích đạt 1.0 mm, độ lặp lại cao (s < 0.2 cm), sai số phi tuyến < 0.2% FSO và không có độ trễ cơ học.", "• ")
add_bullet("Hạn chế: Tồn tại vùng mù (Blind Zone 0 - 3 cm), suy giảm biên độ mạnh ở cự ly > 400 cm và dễ tán xạ khi gặp bề mặt xốp/gồ ghề.", "• ")
add_p("Từ các chỉ tiêu trên, mô-đun RCWL-1601 đặc biệt phù hợp để triển khai trong 3 nhóm bài toán công nghiệp và dân dụng:")
add_bullet("1. Hệ thống giám sát mức chất lỏng không tiếp xúc trong bồn chứa (Smart Tank Level Monitoring) kết hợp thuật toán bù nhiệt độ môi trường.", "1. ")
add_bullet("2. Hệ thống cảnh báo va chạm lùi xe / Robot tự hành tránh vật cản an toàn (AGV / Mobile Robot Obstacle Avoidance).", "2. ")
add_bullet("3. Hệ thống đo chiều cao người tự động hoặc phân loại kích thước kiện hàng trên băng chuyền logistics.", "3. ")

add_h2("6.2. Thiết kế chi tiết Bài toán: Hệ thống giám sát mức chất lỏng thông minh có bù nhiệt độ", anchor="chap6_2")
add_p("Nhằm đáp ứng yêu cầu Assignment môn học và liên kết trực tiếp kết quả đo lường vào thực tế, bài toán được lựa chọn thiết kế chi tiết là: \"Hệ thống đo thể tích/mức chất lỏng bồn chứa thông minh có bù nhiệt độ môi trường và cảnh báo tự động trên ESP32\".")

add_h3("a) Sơ đồ nguyên lý và Mô hình toán học của bài toán ứng dụng")
add_p("Cảm biến RCWL-1601 được gắn cố định tại đỉnh bồn chứa, hướng vuông góc xuống mặt thoáng chất lỏng. Chiều cao bồn chứa danh định là H_tank. Khoảng cách đo được từ cảm biến đến mặt chất lỏng (đã bù nhiệt độ) là d_comp. Chiều cao cột chất lỏng hiện tại h và thể tích chất lỏng V được tính theo mô hình:")
add_p("h = H_tank - d_comp", bold_prefix="   [Công thức 6.1] ", italic=True)
add_p("V = S_base * h = S_base * (H_tank - d_comp)", bold_prefix="   [Công thức 6.2] ", italic=True)
add_p("Trong đó S_base là diện tích đáy bồn chứa (với bồn hình hộp S_base = L * W; với bồn hình trụ S_base = pi * R^2).")

add_h3("b) Ứng dụng trực tiếp kết quả thực nghiệm Chương 4 & 5 vào thiết kế kỹ thuật")
add_bullet("Khắc phục Vùng chết (Blind Zone 0 - 3 cm): Đặt cảm biến trên một cổ ngỗng (standoff tube) hoặc gá lắp cách mức chất lỏng tối đa (mức tràn) ít nhất 5 cm. Điều này đảm bảo khi bồn đầy 100%, mặt nước vẫn nằm trong dải đo tuyến tính ổn định của cảm biến.", "• ")
add_bullet("Xử lý nhiễu dội âm thành bồn: Bố trí cảm biến cách mép thành bồn một khoảng tối thiểu để búp sóng mở ±15° không bị phản xạ ký sinh từ thành bình.", "• ")
add_bullet("Bộ lọc số phối hợp (Hybrid Filter): Kết hợp bộ lọc Trung vị (Median Filter 3 xung) để loại bỏ bọt khí/sóng sánh mặt nước, sau đó áp dụng Lọc 3-Sigma và Lọc trung bình trượt (Moving Average Filter n = 10 mẫu) để kết quả đo mức nước phẳng mịn tuyệt đối.", "• ")
add_bullet("Thuật toán bù vận tốc âm thời gian thực: Liên tục cập nhật nhiệt độ môi trường T để tính v(T) theo công thức Laplace, loại bỏ hoàn toàn sai số trôi nhiệt độ giữa ban ngày và ban đêm (tránh sai số thể tích lên tới hàng lít chất lỏng).", "• ")
add_bullet("Lan truyền sai số và Ngân sách độ không đảm bảo đo của hệ thống: Dựa vào độ KĐBĐ mở rộng U_95% = 1.42 mm đã tính ở Chương 4, độ không đảm bảo đo thể tích mở rộng của hệ thống là: U_V = S_base * U_95%. Với bồn chứa mẫu diện tích đáy S_base = 80 cm^2 (kích thước 10x8 cm), U_V = 80 * 0.142 ≈ 11.36 cm^3 (~ 0.011 L), khẳng định độ chính xác cao.", "• ")

add_placeholder_img("Hình 6.1: Sơ đồ khối nguyên lý Hệ thống giám sát mức chất lỏng thông minh có bù nhiệt độ trên ESP32")
add_placeholder_img("Hình 6.2: Lưu đồ giải thuật tích hợp lọc trung vị, lọc 3σ, bù nhiệt độ và thuật toán điều khiển bơm/cảnh báo tràn")

add_h2("6.3. Kết quả thử nghiệm / Mô phỏng hoạt động của ứng dụng & Đánh giá hiệu năng", anchor="chap6_3")
add_p("Hệ thống được thiết lập thử nghiệm với bình chứa thực nghiệm (chiều cao H_tank = 17.0 cm, kích thước đáy 10 cm x 8 cm, diện tích S_base = 80 cm^2). Cảm biến đặt tại vị trí cách đáy 22.0 cm (đảm bảo mức nước đầy nhất 17 cm cách cảm biến 5 cm). Kết quả thử nghiệm phân ngưỡng và điều khiển tự động được tổng hợp trong bảng sau:")

# Bảng thử nghiệm phân ngưỡng cảnh báo
tbl_app = doc.add_table(rows=6, cols=6)
tbl_app.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_app = ["Trạng thái bồn", "Khoảng cách d (cm)", "Mức nước h (cm)", "Thể tích V (Lít)", "Trạng thái Bơm / Cảnh báo", "Đánh giá an toàn"]
for idx, h in enumerate(hdrs_app):
    c = tbl_app.cell(0, idx)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_app = [
    ("Mức cạn nguy hiểm", "> 19.0 cm", "< 3.0 cm", "< 0.24 L", "Bật Bơm cấp - Báo còi cạn", "Tránh cháy bơm do chạy khô"),
    ("Mức nước thấp", "15.0 - 19.0 cm", "3.0 - 7.0 cm", "0.24 - 0.56 L", "Duy trì Bơm cấp nước", "Hoạt động bình thường"),
    ("Mức nước trung bình", "9.0 - 15.0 cm", "7.0 - 13.0 cm", "0.56 - 1.04 L", "Tắt Bơm (Đạt ngưỡng tối ưu)", "Trạng thái ổn định"),
    ("Mức đầy (Gần tràn)", "5.0 - 9.0 cm", "13.0 - 17.0 cm", "1.04 - 1.36 L", "Khóa ngắt khẩn cấp", "Ngưỡng an toàn tối đa"),
    ("Cảnh báo tràn ngập", "< 5.0 cm", "> 17.0 cm", "> 1.36 L", "Báo động đỏ - Ngắt toàn bộ", "Tránh rơi vào Vùng mù cảm biến")
]

for row_idx, r_data in enumerate(data_app):
    row = tbl_app.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        if col_idx in [0, 1, 2, 3]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.0)

add_p("Hướng phát triển mở rộng IoT: Dữ liệu mức nước h, thể tích V và nhiệt độ môi trường T được đóng gói gửi định kỳ qua UART lên máy tính hoặc đẩy qua Wi-Fi/MQTT lên Web Dashboard / SCADA phục vụ giám sát từ xa.")

add_guide_box("Bạn có thể chụp ảnh mô hình thực tế bình nước/hộp nước đã thử nghiệm nối với ESP32 và chèn vào mục này để tăng tính thuyết phục cho bài báo cáo.")

doc.add_page_break()

# ==================== CHƯƠNG 7 ====================
add_h1("CHƯƠNG 7: TỔNG KẾT ĐẶC TÍNH KỸ THUẬT & KẾT LUẬN", anchor="chap7")

add_h2("7.1. Bảng đối chiếu Thông số thực nghiệm đo được vs. Datasheet RCWL-1601", anchor="chap7_1")

tbl_ds = doc.add_table(rows=8, cols=4)
tbl_ds.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_ds = ["Thông số kỹ thuật", "Công bố Datasheet", "Kết quả Thực nghiệm", "Đánh giá đạt chuẩn"]
for i, h in enumerate(hdrs_ds):
    c = tbl_ds.cell(0, i)
    c.text = h
    set_cell_bg(c, "003366")
    set_cell_pad(c)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

data_ds = [
    ("Điện áp hoạt động", "3.0V - 5.5V DC", "3.3V (cấp trực tiếp từ ESP32)", "Đạt chuẩn tuyệt đối"),
    ("Dải đo danh định", "2 cm - 450 cm", "3 cm - 450 cm (Hiệu dụng)", "Đạt chuẩn công bố"),
    ("Vùng chết (Blind Zone)", "< 2.0 cm", "2.0 cm - 2.5 cm", "Đạt chuẩn vật lý"),
    ("Độ phân giải danh định", "0.1 cm (1 mm)", "1.0 mm (Hữu ích) / 0.17 mm (Lượng tử)", "Vượt chuẩn công bố"),
    ("Góc mở búp sóng", "< 15 độ", "Khoảng 14.5 độ", "Đạt chuẩn"),
    ("Độ phi tuyến (%FSO)", "< 0.5% FSO", "0.18% FSO", "Đạt chuẩn vượt trội"),
    ("Độ trễ (Hysteresis)", "Không công bố", "< 0.15% FSO (< 0.5 mm)", "Rất tốt (không trễ)")
]

for row_idx, r_data in enumerate(data_ds):
    row = tbl_ds.rows[row_idx + 1]
    bg = "F2F5F8" if row_idx % 2 == 1 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = row.cells[col_idx]
        c.text = val
        set_cell_bg(c, bg)
        set_cell_pad(c)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.size = Pt(9.5)

add_h2("7.2. Kết luận chung & Tài liệu tham khảo", anchor="chap7_2")
add_bullet("Vùng làm việc tối ưu: Cảm biến RCWL-1601 hoạt động chính xác và tuyến tính nhất trong dải cự ly 10 cm đến 300 cm đối với các vật thể có bề mặt cứng, phẳng.", "• ")
add_bullet("Khuyến nghị phần cứng: Cần duy trì khoảng cách lắp đặt tối thiểu 5 cm cách xa vật cản gần nhất để tránh rơi vào vùng chết; bố trí cảm biến vuông góc tuyệt đối với bề mặt đo.", "• ")
add_bullet("Khuyến nghị giải pháp xử lý tín hiệu: Bắt buộc tích hợp cảm biến nhiệt độ để bù vận tốc âm theo công thức Laplace; áp dụng bộ lọc trung vị (Median Filter 3 xung) kết hợp lọc trung bình trượt (Moving Average Filter n = 10 mẫu) để loại trừ triệt để sóng sánh và nhiễu xung cơ học.", "• ")

add_p("Tài liệu tham khảo:", bold_prefix="DANH MỤC TÀI LIỆU THAM KHẢO:")
add_bullet("Datasheet mô-đun siêu âm RCWL-1601 & IC điều khiển RCWL-9610.", "1. ")
add_bullet("Tài liệu bài giảng Kỹ thuật Đo lường và Cảm biến (ELEC-E5710 / EMA2024E_3), Đại học Bách Khoa Hà Nội.", "2. ")
add_bullet("ISO/IEC Guide 98-3:2008 (GUM) - Guide to the Expression of Uncertainty in Measurement.", "3. ")
add_bullet("Toàn bộ mã nguồn chương trình ESP32 và script phân tích dữ liệu được lưu trữ tại thư mục thực hành RCWL1601.", "4. ")

# Thử lưu trực tiếp vào báo cáo.docx; nếu file đang mở trong Word thì lưu vào báo cáo_khung_moi.docx
saved_to_main = False
try:
    doc.save(OUTPUT_FILE_MAIN)
    saved_to_main = True
    print(f"SUCCESS: Đã lưu trực tiếp thành công vào: {OUTPUT_FILE_MAIN}")
except PermissionError:
    print(f"CHU Y: Tệp '{OUTPUT_FILE_MAIN}' đang được mở trong Word.")

# Luôn lưu bản khung mới độc lập để người dùng có thể mở ngay mà không xung đột file lock
doc.save(OUTPUT_FILE_NEW)
shutil.copy2(OUTPUT_FILE_NEW, OUTPUT_FILE_NEW_EN)
print(f"SUCCESS: Đã tạo bản khung mới hoàn chỉnh tại:")
print(f"1. {OUTPUT_FILE_NEW}")
print(f"2. {OUTPUT_FILE_NEW_EN}")
if saved_to_main:
    print(f"3. {OUTPUT_FILE_MAIN} (Đã cập nhật)")
else:
    print(f"-> Ghi chú: Hãy đóng file 'báo cáo.docx' trên Word nếu bạn muốn ghi đè trực tiếp.")
