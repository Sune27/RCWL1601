# -*- coding: utf-8 -*-
"""
Tái cấu trúc file Word Báo Cáo Thực Nghiệm theo ĐỀ CƯƠNG 35 TRANG MỚI (5 CHƯƠNG)
Bảo toàn 100% nội dung, công thức Toán học Math và các chỉnh sửa của người dùng.
"""

import os
import sys
import html
import copy
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

TARGET_DIR = r"D:\đo lường\thực hành đo lường\RCWL1601"
SRC_DOCX = os.path.join(TARGET_DIR, "báo cáo.docx")
OUT_DOCX = os.path.join(TARGET_DIR, "báo cáo.docx")

# Màu sắc chuẩn học thuật
C_NAVY = RGBColor(0, 51, 102)     # #003366
C_MAROON = RGBColor(128, 0, 0)   # #800000
C_GRAY = RGBColor(90, 90, 90)
C_DARK = RGBColor(40, 40, 40)
C_BLUE = RGBColor(29, 78, 216)

bm_counter = 2000

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

def make_h1(doc, text, anchor=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = C_NAVY
    
    if anchor:
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
        add_bookmark(p, anchor)
    return p

def make_h2(doc, text, anchor=None):
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
        p.add_run("   ")
        back_hl = parse_xml(
            f'<w:hyperlink {nsdecls("w")} w:anchor="toc_nav">'
            f'<w:r>'
            f'<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:color w:val="2563EB"/><w:sz w:val="16"/><w:i/></w:rPr>'
            f'<w:t>[↑ Về Mục Lục]</w:t>'
            f'</w:r>'
            f'</w:hyperlink>'
        )
        p._p.append(back_hl)
        add_bookmark(p, anchor)
    return p

def make_toc_entry(doc, title, anchor, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.05
    if level == 1:
        p.paragraph_format.space_before = Pt(3.5)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Inches(0)
        color = "003366"
        bold_tag = "<w:b/>"
        size = 20  # 10 pt
        prefix = "■ "
    else:
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Inches(0.2)
        color = "1D4ED8"
        bold_tag = ""
        size = 18  # 9 pt
        prefix = "   ▸ "

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
    return p

def make_p(doc, text, bold=False, italic=False, size=10, color=C_DARK, space_before=0, space_after=6, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    return p

def make_bullet(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(9.5)
    r.font.color.rgb = C_DARK
    return p

def rebuild_document():
    print(f"Reading source document: {SRC_DOCX}")
    doc_orig = Document(SRC_DOCX)
    body = doc_orig.element.body
    children = [copy.deepcopy(c) for c in body]
    
    # sectPr là phần tử cấu hình lề và trang cuối cùng
    sectPr = [c for c in children if c.tag.endswith('sectPr')][0]
    
    # Khởi tạo doc mới kế thừa mọi styles từ template
    doc = Document(SRC_DOCX)
    body = doc.element.body
    sectPr = body.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr')
    
    # Xóa toàn bộ các elements trừ sectPr để doc.sections[-1] luôn hợp lệ
    for c in list(body):
        if c is not sectPr:
            body.remove(c)
        
    def append_xml(el):
        sectPr.addprevious(copy.deepcopy(el))
        
    def append_range(start_idx, end_idx):
        for i in range(start_idx, end_idx):
            sectPr.addprevious(copy.deepcopy(children[i]))

    print("Rebuilding TRANG BÌA (Cover page)...")
    append_range(0, 10)  # Trang bìa của user giữ nguyên 100%

    print("Rebuilding MỤC LỤC TƯƠNG TÁC (5 Chương)...")
    p_toc_title = doc.add_paragraph()
    p_toc_title.paragraph_format.space_before = Pt(14)
    p_toc_title.paragraph_format.space_after = Pt(8)
    r_toc = p_toc_title.add_run("MỤC LỤC & PHỤ LỤC ĐIỀU HƯỚNG TƯƠNG TÁC")
    r_toc.font.name = 'Calibri'
    r_toc.font.size = Pt(14)
    r_toc.font.bold = True
    r_toc.font.color.rgb = C_NAVY
    add_bookmark(p_toc_title, "toc_nav")

    toc_entries = [
        ("TỔNG QUAN PHÂN BỔ DUNG LƯỢNG (31 – 35 TRANG) & DANH MỤC", "toc_phan_bo", 1),
        ("PHẦN MỞ ĐẦU & DANH MỤC QUY ƯỚC DỮ LIỆU", "sec_modau", 1),
        ("1. Lời nói đầu và Đặt vấn đề", "sec_modau_1", 2),
        ("2. Bảng quy ước mã hóa tập dữ liệu thực nghiệm", "sec_modau_2", 2),
        ("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM", "chap1", 1),
        ("1.1. Nguyên lý đo khoảng cách ToF và Mô hình bù nhiệt độ môi trường", "chap1_1", 2),
        ("1.2. Cấu tạo phần cứng và nguyên lý hoạt động của module RCWL-1601", "chap1_2", 2),
        ("1.3. Cơ sở lý thuyết xử lý số liệu thực nghiệm và Đánh giá độ không đảm bảo đo", "chap1_3", 2),
        ("CHƯƠNG 2: THIẾT KẾ THỰC NGHIỆM", "chap2", 1),
        ("2.1. Mục tiêu và Phương pháp luận thực nghiệm", "chap2_1", 2),
        ("2.2. Thiết kế hệ thống phần cứng và Mô hình gá đặt đo lường", "chap2_2", 2),
        ("2.3. Kiến trúc phần mềm OOP và Giải thuật thu thập dữ liệu", "chap2_3", 2),
        ("2.4. Thiết kế Ma trận Kịch bản thực nghiệm", "chap2_4", 2),
        ("2.5. Cơ sở thống kê và Thực nghiệm xác định Cỡ mẫu tối ưu N = 50", "chap2_5", 2),
        ("CHƯƠNG 3: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM", "chap3", 1),
        ("3.1. Tiền xử lý dữ liệu và Đánh giá hiệu quả lọc sai số thô", "chap3_1", 2),
        ("3.2. Khảo sát Dải đo thực tế, Vùng chết (Blind Zone) và Giới hạn bão hòa xa", "chap3_2", 2),
        ("3.3. Đánh giá Độ chụm (Precision) và Độ chính xác (Accuracy)", "chap3_3", 2),
        ("3.4. Đánh giá Độ tuyến tính (Linearity), Độ nhạy (Sensitivity) và Độ phân giải (Resolution)", "chap3_4", 2),
        ("3.5. Phân tích Độ trễ (Hysteresis) giữa Chiều tiến và Chiều lùi", "chap3_5", 2),
        ("3.6. Phân tích ảnh hưởng của Bề mặt phản xạ (Reflective Surface)", "chap3_6", 2),
        ("3.7. Phân tích ảnh hưởng của Nhiệt độ môi trường và Hiệu quả thuật toán bù nhiệt", "chap3_7", 2),
        ("3.8. Đánh giá Độ không đảm bảo đo mở rộng toàn diện", "chap3_8", 2),
        ("3.9. Bảng tổng hợp đối chiếu Đặc tính Kỹ thuật Thực nghiệm vs. Datasheet Nhà sản xuất", "chap3_9", 2),
        ("CHƯƠNG 4: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ", "chap4", 1),
        ("4.1. Tổng quan tiềm năng ứng dụng từ kết quả khảo sát thực nghiệm của RCWL-1601", "chap4_1", 2),
        ("4.2. Thiết kế chi tiết Bài toán tiêu biểu: Hệ thống giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ trên ESP32", "chap4_2", 2),
        ("4.3. Kết quả thử nghiệm / Mô phỏng hoạt động & Đánh giá hiệu năng ứng dụng", "chap4_3", 2),
        ("CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ", "chap5", 1),
        ("5.1. Kết luận chung về đề tài", "chap5_1", 2),
        ("5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật", "chap5_2", 2),
        ("5.3. Tài liệu tham khảo & Phụ lục", "chap5_3", 2)
    ]
    for title, anchor, lvl in toc_entries:
        make_toc_entry(doc, title, anchor, lvl)

    doc.add_page_break()

    print("Rebuilding TỔNG QUAN PHÂN BỔ DUNG LƯỢNG & DANH MỤC...")
    make_h1(doc, "TỔNG QUAN PHÂN BỔ DUNG LƯỢNG BÁO CÁO (31 – 35 TRANG)", "toc_phan_bo")
    make_p(doc, "Toàn văn báo cáo được thiết kế theo cấu trúc khung mới chuẩn học thuật (5 Chương), quy tụ mạch lạc thành hai trụ cột cốt lõi: Thiết kế thực nghiệm (Chương 2) và Phân tích kết quả thực nghiệm (Chương 3):")
    
    # Bảng phân bổ dung lượng 5 chương
    table_alloc = doc.add_table(rows=7, cols=3)
    table_alloc.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_alloc = [("Phần / Chương", 1.8), ("Nội dung trọng tâm", 4.3), ("Số trang dự kiến", 1.2)]
    for j, (h_text, w) in enumerate(headers_alloc):
        cell = table_alloc.cell(0, j)
        cell.width = Inches(w)
        cell.text = h_text
        set_cell_bg(cell, "003366")
        set_cell_pad(cell, top=100, bottom=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.runs[0]
        r.font.name = 'Calibri'
        r.font.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    data_alloc = [
        ("Mở đầu & Danh mục", "Trang bìa, Lời nói đầu, Mục lục, Danh mục bảng biểu, Danh mục hình vẽ, Ký hiệu & Quy ước mã hóa tập dữ liệu (FSDT, FRDT, BSDT, FSAT)", "2.5 – 3 trang"),
        ("Chương 1", "Cơ sở lý thuyết đo lường và cảm biến siêu âm: Mô hình sóng siêu âm ToF, cơ chế bù nhiệt độ Laplace v(T), cấu tạo IC RCWL-9610 và cơ sở lý thuyết xử lý số liệu thực nghiệm", "4 – 4.5 trang"),
        ("Chương 2", "THIẾT KẾ THỰC NGHIỆM: Thiết kế phần cứng ESP32 + RCWL-1601, kiến trúc phần mềm OOP (MicroPython/PC), thiết kế ma trận kịch bản đo và nghiên cứu thống kê lựa chọn cỡ mẫu tối ưu N = 50", "6 – 6.5 trang"),
        ("Chương 3", "PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM: Tiền xử lý & lọc sai số thô, khảo sát Dải đo & Vùng chết, Đánh giá toàn diện các đặc tính tĩnh (Precision, Accuracy, Linearity, Sensitivity, Resolution, Hysteresis), Phân tích yếu tố ngoại cảnh (Bề mặt phản xạ, Nhiệt độ môi trường), Ngân sách độ không đảm bảo đo và Đối chiếu Datasheet", "12 – 13 trang"),
        ("Chương 4", "Xây dựng và triển khai bài toán Ứng dụng thực tế: Hệ thống đo và giám sát mức chất lỏng bồn chứa thông minh có bù nhiệt độ môi trường và cảnh báo đa ngưỡng trên ESP32", "4 – 4.5 trang"),
        ("Chương 5", "Kết luận và Kiến nghị: Tổng kết các kết quả đạt được, vùng làm việc tin cậy, khuyến nghị kỹ thuật giải pháp xử lý tín hiệu và Tài liệu tham khảo", "1.5 – 2 trang")
    ]
    for row_idx, (c0, c1, c2) in enumerate(data_alloc, start=1):
        for col_idx, text_val in enumerate([c0, c1, c2]):
            cell = table_alloc.cell(row_idx, col_idx)
            cell.width = Inches(headers_alloc[col_idx][1])
            cell.text = text_val
            set_cell_pad(cell, top=70, bottom=70)
            if row_idx % 2 == 1:
                set_cell_bg(cell, "F8FAFC")
            p = cell.paragraphs[0]
            if col_idx in [0, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.runs[0]
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = C_NAVY
            elif col_idx == 2:
                r.font.bold = True
                r.font.color.rgb = C_MAROON
            else:
                r.font.color.rgb = C_DARK

    make_p(doc, "Danh mục Hình vẽ trong Báo cáo", bold=True, size=11, color=C_NAVY, space_before=12, space_after=4)
    figures_list = [
        "Hình 1.1: Giản đồ búp sóng siêu âm (Beam Pattern ±15°) và cơ chế phản xạ Time-of-Flight.",
        "Hình 1.2: Sơ đồ khối tích hợp vi mạch RCWL-9610 và Giản đồ xung kích hoạt TRIG – phản hồi ECHO.",
        "Hình 2.1: Sơ đồ phần cứng và kết nối kit ESP32 với RCWL-1601, cảm biến nhiệt độ DHT11 trên Expansion Board 30-Pin.",
        "Hình 2.2: Sơ đồ lớp UML (Class Diagram) và Lưu đồ giải thuật (Flowchart) thu thập dữ liệu tự động.",
        "Hình 2.3: Đồ thị 4 góc phân tích sự hội tụ của Trung bình, Độ lệch chuẩn, Trung vị và IQR theo cỡ mẫu k = 2..100.",
        "Hình 3.1: Đồ thị phân tán (Scatter Plot) và Hộp râu (Boxplot) minh họa hiệu quả phát hiện sai số thô (3σ & IQR).",
        "Hình 3.2: Đồ thị kiểm chứng Vùng chết (1 – 3 cm) và Ngưỡng bão hòa xa (400 – 600 cm).",
        "Hình 3.3: Biểu đồ biến thiên Độ lệch chuẩn s, IQR và Hệ số biến thiên CV% theo cự ly đo.",
        "Hình 3.4: Đồ thị Sai số tuyệt đối Δd và Sai số tương đối δ% theo khoảng cách đo.",
        "Hình 3.5: Đường đặc tính truyền đạt tĩnh, đường thẳng hồi quy tuyến tính và đồ thị phần dư.",
        "Hình 3.6: Biểu đồ Vòng trễ (Hysteresis Loop) so sánh đường đặc tính chiều tiến (FSDT) và chiều lùi (BSDT).",
        "Hình 3.7: Đồ thị so sánh Boxplot sai số và Độ lệch chuẩn giữa Bề mặt phẳng nhẵn (FSDT) và Mặt gồ ghề (FRDT).",
        "Hình 3.8: Đồ thị biểu diễn sai số trôi cự ly khi không bù nhiệt và hiệu quả ổn định tín hiệu sau khi bù nhiệt độ Laplace.",
        "Hình 4.1: Sơ đồ khối nguyên lý Hệ thống giám sát mức chất lỏng thông minh có bù nhiệt độ trên ESP32.",
        "Hình 4.2: Lưu đồ giải thuật tích hợp lọc trung vị, lọc 3σ, bù nhiệt độ và thuật toán điều khiển bơm nước tự động/thủ công."
    ]
    for fig in figures_list:
        make_bullet(doc, fig)

    make_p(doc, "Danh mục Bảng biểu trong Báo cáo", bold=True, size=11, color=C_NAVY, space_before=10, space_after=4)
    tables_list = [
        "Bảng 0.1: Bảng quy ước mã hóa tập dữ liệu thực nghiệm (FSDT, BSDT, FRDT, FSAT).",
        "Bảng 1.1: Bảng tra cứu mẫu vận tốc truyền âm trong không khí theo nhiệt độ môi trường.",
        "Bảng 1.2: Thông số kỹ thuật định mức của cảm biến siêu âm RCWL-1601.",
        "Bảng 1.3: Hệ thống công thức toán học thống kê và đánh giá đặc tính tĩnh cảm biến.",
        "Bảng 2.1: Sơ đồ chân kết nối phần cứng giữa cảm biến RCWL-1601 và kit ESP32.",
        "Bảng 2.2: Ma trận kịch bản thực nghiệm đo lường tổng thể.",
        "Bảng 2.3: Bảng phân tích hội tụ của x_bar, s và sai số tin cậy theo cỡ mẫu k = 2..100.",
        "Bảng 3.1: Bảng tổng hợp thống kê toàn dải (1 cm – 600 cm) và tỷ lệ lọc sai số thô.",
        "Bảng 3.2: Bảng phân tích dữ liệu thực tế tại vùng chết (1 – 3 cm) và giới hạn bão hòa xa.",
        "Bảng 3.3: Bảng chỉ tiêu độ chụm và độ chính xác trên các dải cự ly thực nghiệm.",
        "Bảng 3.4: Kết quả hồi quy tuyến tính, độ nhạy và độ phân giải thực tế.",
        "Bảng 3.5: Bảng đối chiếu thực nghiệm Chiều tiến (FSDT) và Chiều lùi (BSDT) xác định sai số trễ.",
        "Bảng 3.6: Đối chiếu chỉ tiêu kỹ thuật giữa Bề mặt phẳng nhẵn (FSDT) vs. Mặt gồ ghề (FRDT).",
        "Bảng 3.7: Bảng so sánh sai số đo khi Không bù nhiệt vs. Có bù nhiệt độ Laplace.",
        "Bảng 3.8: Ngân sách Độ không đảm bảo đo mở rộng theo chuẩn ISO/GUM tại mốc tiêu chuẩn.",
        "Bảng 3.9: Bảng tổng hợp đối chiếu Hồ sơ kỹ thuật thực nghiệm so với Datasheet Nhà sản xuất.",
        "Bảng 4.1: Bảng thử nghiệm phân ngưỡng cảnh báo mức nước và trạng thái điều khiển bơm ứng dụng."
    ]
    for tbl in tables_list:
        make_bullet(doc, tbl)

    doc.add_page_break()

    print("Rebuilding PHẦN MỞ ĐẦU & DANH MỤC QUY ƯỚC DỮ LIỆU...")
    make_h1(doc, "PHẦN MỞ ĐẦU & DANH MỤC QUY ƯỚC DỮ LIỆU", "sec_modau")
    make_h2(doc, "1. Lời nói đầu và Đặt vấn đề", "sec_modau_1")
    append_xml(children[77])  # User's opening intro text
    make_h2(doc, "2. Bảng quy ước mã hóa tập dữ liệu thực nghiệm", "sec_modau_2")
    append_xml(children[79])  # Intro text for dataset convention
    append_xml(children[80])  # Dataset table (6x3)
    append_xml(children[81])  # Spacing

    print("Rebuilding CHƯƠNG 1: CƠ SỞ LÝ THUYẾT...")
    make_h1(doc, "CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM", "chap1")
    make_h2(doc, "1.1. Nguyên lý đo khoảng cách ToF và Mô hình bù nhiệt độ môi trường", "chap1_1")
    append_range(84, 99)      # 100% user content: Math formula, bullets, sound speed table, fig 1.1
    make_h2(doc, "1.2. Cấu tạo phần cứng và nguyên lý hoạt động của module RCWL-1601", "chap1_2")
    append_range(100, 114)    # 100% user content: 4 steps, fig 1.2, specs table
    make_h2(doc, "1.3. Cơ sở lý thuyết xử lý số liệu thực nghiệm và Đánh giá độ không đảm bảo đo", "chap1_3")
    append_range(115, 119)    # Formulas table and text

    print("Rebuilding CHƯƠNG 2: THIẾT KẾ THỰC NGHIỆM...")
    make_h1(doc, "CHƯƠNG 2: THIẾT KẾ THỰC NGHIỆM", "chap2")
    
    # 2.1 Mục tiêu và Phương pháp luận
    make_h2(doc, "2.1. Mục tiêu và Phương pháp luận thực nghiệm", "chap2_1")
    make_p(doc, "Mục tiêu của chương này là thiết kế toàn diện quy trình thực nghiệm nhằm kiểm chứng các thông số kỹ thuật danh định của mô-đun siêu âm RCWL-1601, xác định dải đo hữu ích thực tế, đánh giá độ chụm, độ chính xác, độ tuyến tính, độ trễ và ảnh hưởng của môi trường (nhiệt độ, bề mặt phản xạ). Phương pháp luận dựa trên chuẩn đo lường quốc tế ISO/GUM, phương pháp lấy mẫu lặp lại thống kê và xử lý dữ liệu tự động hóa trên vi điều khiển ESP32.")

    # 2.2 Phần cứng (was old 2.1)
    make_h2(doc, "2.2. Thiết kế hệ thống phần cứng và Mô hình gá đặt đo lường", "chap2_2")
    append_range(121, 129)    # ESP32 pin bullets, connection table, fig 2.1 placeholder

    # 2.3 Phần mềm OOP (was old 2.2 part 1)
    make_h2(doc, "2.3. Kiến trúc phần mềm OOP và Giải thuật thu thập dữ liệu", "chap2_3")
    append_range(130, 134)    # OOP classes description
    append_xml(children[135])  # Figure box
    append_xml(children[136])  # Caption Hình 2.2

    # 2.4 Ma trận Kịch bản (was old 2.2 part 2)
    make_h2(doc, "2.4. Thiết kế Ma trận Kịch bản thực nghiệm", "chap2_4")
    make_p(doc, "Ma trận kịch bản thực nghiệm được thiết kế bao gồm 5 chuỗi đo kiểm chứng toàn diện các yếu tố: cỡ mẫu hội tụ, dải đo tĩnh, độ trễ cơ học, tán xạ bề mặt và ảnh hưởng của nhiệt độ môi trường:")
    append_xml(children[137])  # Table Tập dữ liệu
    append_xml(children[138])  # Spacing

    # 2.5 Cỡ mẫu tối ưu N = 50 (was old Chapter 3)
    make_h2(doc, "2.5. Cơ sở thống kê và Thực nghiệm xác định Cỡ mẫu tối ưu N = 50", "chap2_5")
    append_xml(children[141])  # Sample convergence text
    append_xml(children[142])  # Table Cỡ mẫu k
    append_xml(children[144])  # Elbow point analysis text
    append_xml(children[145])  # Spacing
    append_xml(children[146])  # Figure box
    make_p(doc, "Hình 2.3: Đồ thị 4 góc phân tích sự hội tụ của Trung bình, Độ lệch chuẩn, Trung vị và IQR theo cỡ mẫu k = 2..100", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)
    append_xml(children[148])  # Instruction box
    append_xml(children[149])  # Spacing

    print("Rebuilding CHƯƠNG 3: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM...")
    make_h1(doc, "CHƯƠNG 3: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM", "chap3")
    
    # 3.1 Tiền xử lý (was old 4.1)
    make_h2(doc, "3.1. Tiền xử lý dữ liệu và Đánh giá hiệu quả lọc sai số thô", "chap3_1")
    append_xml(children[153])  # Filtering text
    append_xml(children[154])  # Table FSDT full range
    make_p(doc, "Hình 3.1: Đồ thị phân tán (Scatter Plot) và Hộp râu (Boxplot) minh họa hiệu quả phát hiện sai số thô (3σ & IQR)", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)

    # 3.2 Vùng chết (was old 4.2)
    make_h2(doc, "3.2. Khảo sát Dải đo thực tế, Vùng chết (Blind Zone) và Giới hạn bão hòa xa", "chap3_2")
    append_xml(children[156])  # Blind zone text
    append_xml(children[157])  # Blind zone text
    make_p(doc, "Hình 3.2: Đồ thị kiểm chứng Vùng chết (1 – 3 cm) và Ngưỡng bão hòa xa (400 – 600 cm)", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)

    # 3.3 Độ chụm & Độ chính xác (was old 4.3)
    make_h2(doc, "3.3. Đánh giá Độ chụm (Precision) và Độ chính xác (Accuracy)", "chap3_3")
    append_xml(children[159])  # Precision text
    append_xml(children[160])  # Spacing
    append_xml(children[161])  # Fig box
    make_p(doc, "Hình 3.3: Biểu đồ biến thiên Độ lệch chuẩn s, IQR và Hệ số biến thiên CV% theo cự ly đo", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)
    append_xml(children[163])  # Spacing
    append_xml(children[164])  # Fig box
    make_p(doc, "Hình 3.4: Đồ thị Sai số tuyệt đối Δd và Sai số tương đối δ% theo khoảng cách đo", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)

    # 3.4 Độ tuyến tính & Độ nhạy (was old 4.4)
    make_h2(doc, "3.4. Đánh giá Độ tuyến tính (Linearity), Độ nhạy (Sensitivity) và Độ phân giải (Resolution)", "chap3_4")
    append_range(167, 171)    # 4 bullets: regression, sensitivity, non-linearity, resolution
    append_xml(children[171])  # Spacing
    append_xml(children[172])  # Fig box
    make_p(doc, "Hình 3.5: Đường đặc tính truyền đạt tĩnh, đường thẳng hồi quy tuyến tính và đồ thị phần dư", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)

    # 3.5 Độ trễ Hysteresis (was old 4.5)
    make_h2(doc, "3.5. Phân tích Độ trễ (Hysteresis) giữa Chiều tiến và Chiều lùi", "chap3_5")
    append_xml(children[175])  # Hysteresis text
    append_xml(children[176])  # Table Mốc d_true
    append_xml(children[177])  # Spacing
    append_xml(children[178])  # Fig box
    make_p(doc, "Hình 3.6: Biểu đồ Vòng trễ (Hysteresis Loop) so sánh đường đặc tính chiều tiến (FSDT) và chiều lùi (BSDT)", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)

    # 3.6 Bề mặt phản xạ (was old 5.1)
    make_h2(doc, "3.6. Phân tích ảnh hưởng của Bề mặt phản xạ (Reflective Surface)", "chap3_6")
    append_range(189, 194)    # Bullets on acoustic scattering
    append_xml(children[194])  # Table Cự ly d_true (FSDT vs FRDT)
    append_xml(children[195])  # Spacing
    append_xml(children[196])  # Fig box
    make_p(doc, "Hình 3.7: Đồ thị so sánh Boxplot sai số và Độ lệch chuẩn giữa Bề mặt phẳng nhẵn (FSDT) và Mặt gồ ghề (FRDT)", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)

    # 3.7 Nhiệt độ môi trường (was old 5.2)
    make_h2(doc, "3.7. Phân tích ảnh hưởng của Nhiệt độ môi trường và Hiệu quả thuật toán bù nhiệt", "chap3_7")
    append_range(199, 202)    # Bullets on temp effect
    append_xml(children[202])  # Table Temp comparison
    append_xml(children[203])  # Spacing
    append_xml(children[204])  # Fig box
    make_p(doc, "Hình 3.8: Đồ thị biểu diễn sai số trôi cự ly khi không bù nhiệt và hiệu quả ổn định tín hiệu sau khi bù nhiệt độ Laplace", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)
    append_xml(children[206])  # Spacing

    # 3.8 Độ không đảm bảo đo ISO/GUM (was old 4.6)
    make_h2(doc, "3.8. Đánh giá Độ không đảm bảo đo mở rộng toàn diện", "chap3_8")
    append_range(181, 185)    # Bullets u_A, u_B, u_c
    append_xml(children[185])  # Table GUM uncertainty
    append_xml(children[186])  # Spacing

    # 3.9 Đối chiếu Datasheet (was old 7.1)
    make_h2(doc, "3.9. Bảng tổng hợp đối chiếu Đặc tính Kỹ thuật Thực nghiệm vs. Datasheet Nhà sản xuất", "chap3_9")
    append_xml(children[245])  # Table Thông số kỹ thuật thực nghiệm vs Datasheet

    print("Rebuilding CHƯƠNG 4: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ...")
    make_h1(doc, "CHƯƠNG 4: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ", "chap4")
    
    # 4.1 Tiềm năng ứng dụng (was old 6.1)
    make_h2(doc, "4.1. Tổng quan tiềm năng ứng dụng từ kết quả khảo sát thực nghiệm của RCWL-1601", "chap4_1")
    append_range(209, 217)    # 3 applications bullets

    # 4.2 Thiết kế bồn chứa (was old 6.2)
    make_h2(doc, "4.2. Thiết kế chi tiết Bài toán tiêu biểu: \"Hệ thống giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ trên ESP32\"", "chap4_2")
    append_range(218, 221)    # Intro and mathematical model intro
    make_p(doc, "[Công thức 4.1] h = H_tank - d_comp", bold=True, color=C_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER)
    make_p(doc, "[Công thức 4.2] V = S_base * h = S_base * (H_tank - d_comp)", bold=True, color=C_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER)
    append_range(223, 231)    # Formula explanation and 5 technical solutions
    append_xml(children[231])  # Fig box 4.1
    make_p(doc, "Hình 4.1: Sơ đồ khối nguyên lý Hệ thống giám sát mức chất lỏng thông minh có bù nhiệt độ trên ESP32", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)
    append_xml(children[233])  # Spacing
    append_xml(children[234])  # Fig box 4.2
    make_p(doc, "Hình 4.2: Lưu đồ giải thuật tích hợp lọc trung vị, lọc 3σ, bù nhiệt độ và thuật toán điều khiển bơm nước tự động/thủ công", bold=True, italic=True, size=9.5, color=C_GRAY, align=WD_ALIGN_PARAGRAPH.CENTER)

    # 4.3 Thử nghiệm & Hiệu năng (was old 6.3)
    make_h2(doc, "4.3. Kết quả thử nghiệm / Mô phỏng hoạt động & Đánh giá hiệu năng ứng dụng", "chap4_3")
    append_xml(children[237])  # Setup description (H_tank = 17cm, 10x8cm)
    append_xml(children[238])  # Table Trạng thái bồn
    append_xml(children[239])  # IoT extension text
    append_xml(children[240])  # Instruction box
    append_xml(children[241])  # Spacing

    print("Rebuilding CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ...")
    make_h1(doc, "CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ", "chap5")
    
    # 5.1 Kết luận chung
    make_h2(doc, "5.1. Kết luận chung về đề tài", "chap5_1")
    make_p(doc, "Đề tài đã hoàn thành xuất sắc các mục tiêu đề ra: thiết kế thành công hệ thống thu thập dữ liệu tự động hóa kết nối ESP32 với mô-đun siêu âm RCWL-1601 và cảm biến nhiệt độ DHT11; xây dựng quy trình thực nghiệm chuẩn tắc với ma trận kịch bản đo toàn diện; luận giải khoa học về cỡ mẫu tối ưu N = 50; và đánh giá đầy đủ các đặc tính kỹ thuật tĩnh, động và độ không đảm bảo đo theo chuẩn quốc tế ISO/GUM. Đồng thời, kết quả khảo sát thực nghiệm đã được liên kết trực tiếp vào việc thiết kế bài toán ứng dụng thực tế đo mức bồn chứa thông minh có bù nhiệt độ môi trường.")

    # 5.2 Khuyến nghị kỹ thuật
    make_h2(doc, "5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật", "chap5_2")
    append_range(247, 250)    # Bullets on optimal zone, hardware, signal processing

    # 5.3 Tài liệu tham khảo & Phụ lục
    make_h2(doc, "5.3. Tài liệu tham khảo & Phụ lục", "chap5_3")
    append_range(250, 255)    # 4 references and code repository note

    # sectPr đã luôn được giữ ở cuối tài liệu body
    # doc.element.body.append(sectPr)

    print(f"Saving final document to: {OUT_DOCX}")
    doc.save(OUT_DOCX)
    print("SUCCESSFULLY REBUILT REPORT WITH 5 CHAPTERS!")

if __name__ == '__main__':
    rebuild_document()
