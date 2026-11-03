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
add_bullet_p("Sử dụng thước đo tiêu chuẩn có độ chia milimét tiêu chuẩn (độ không đảm bảo đo u_B1 = 0.289 mm) làm chuẩn chiều dài đối chứng.", "• Phương pháp đo so sánh trực tiếp: ")
add_bullet_p("Tại mỗi mốc cự ly chuẩn, thực hiện lặp lại N lần đo độc lập trong điều kiện môi trường ổn định để đánh giá độ phân tán ngẫu nhiên và tính toán độ không đảm bảo đo Loại A (u_A).", "• Phương pháp đo lặp thống kê: ")
add_bullet_p("Nhiệt độ môi trường phòng thực nghiệm được giám sát liên tục bằng nhiệt kế. Dữ liệu nhiệt độ được ghi nhận đồng bộ vào từng mẫu đo để áp dụng thuật toán bù vận tốc sóng âm Laplace.", "• Phương pháp kiểm soát và bù trừ điều kiện môi trường: ")
add_bullet_p("Toàn bộ dữ liệu thô (thời gian bay t, cự ly đo d, nhiệt độ T) được ESP32 truyền về máy tính tự động ghi lưu thành các tệp định dạng CSV.", "• Phương pháp thu thập dữ liệu tự động hóa: ")

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
    ("VCC", "3V3 (ESP32)", "Cấp nguồn nuôi cảm biến", "3.3 V DC (Dòng tĩnh < 3 mA)"),
    ("GND", "GND (ESP32)", "Nối đất chung hệ thống", "0 V (Mass tham chiếu)"),
    ("TRIG", "GPIO 5 (ESP32)", "Ngõ vào kích phát xung siêu âm", "Mức logic 3.3 V (Xung kích ≥ 10 μs)"),
    ("ECHO", "GPIO 18 (ESP32)", "Ngõ ra phản hồi thời gian bay ToF", "Mức logic 3.3 V (Độ rộng xung tỷ lệ thuận ToF)")
]

table_pin = doc.add_table(rows=len(pin_data)+1, cols=4)
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
add_bullet_p("Khoảng cách chuẩn d_true được xác định thủ công bằng thước dây đo chuẩn có độ chia nhỏ nhất đến milimet. Thước được căng thẳng giữa hai mép bàn để định vị chính xác từng mốc cự ly đo trước khi người thực nghiệm phát lệnh kích hoạt cảm biến đo và ghi nhận chuỗi dữ liệu trên máy tính.", "3. Căn chỉnh cự ly bằng thước đo tiêu chuẩn: ")

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
    ("Bề mặt phản xạ", "Mặt trước nhẵn (Gạch 40x40 cm)", "Mặt trước nhẵn (Gạch 40x40 cm)", "Mặt sau gồ ghề (Gạch 40x40 cm)", "Mặt trước nhẵn (Gạch 40x40 cm)"),
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
sc_headers = ["Tham số khảo sát", "Trường hợp 1: FSDT (Chuẩn)", "Trường hợp 2: BSDT (Trễ)", "Trường hợp 3: FRDT (Gồ ghề)", "Trường hợp 4: FSAT (Nhiệt độ)"]

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
add_equation_box("ε_95%(k) = t_{0.975}(k - 1) · [ s(k) / √k ]", "2.1")
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
if os.path.exists(IMAGE_PATH):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(IMAGE_PATH, width=Cm(15.0))
    
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
                    r.font.color.rgb = RGBColor(128, 0, 0)

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

doc.save(FILE_PATH)
print(f"Nối thành công Chương 2 vào tệp Word: {FILE_PATH}")
