# -*- coding: utf-8 -*-
"""
Kịch bản nối tiếp Chương 5 (Kết luận và Kiến nghị) vào tệp Word hiện có (Bao_Cao_Thuc_Nghiem_RCWL1601.docx)
Tuân thủ nghiêm ngặt quy chuẩn GEMINI.md:
- Heading 1: 16pt, Bold, C_NAVY
- Heading 2: 14pt, Bold, C_NAVY
- Heading 3: 13pt, Bold, C_MAROON
- Body text: 13pt, Line spacing 1.35, Space after 6pt, Justified, First-line indent 1.0cm
- Bullet points: 13pt, Line spacing 1.35, Space after 4pt, Justified, Hanging indent
- References: 13pt, Line spacing 1.35, Space after 4pt, Justified, Hanging indent
- Ngắt trang (Page Break) đầu chương để bắt đầu trang mới chuẩn chỉnh.
"""

import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = r"D:\ki5\[EMA2024E_3] Kỹ thuật đo lường và cảm biến\RCWL1601\Bao_Cao_Thuc_Nghiem_RCWL1601.docx"

doc = Document(FILE_PATH)

C_NAVY = RGBColor(0, 51, 102)     # #003366
C_MAROON = RGBColor(128, 0, 0)   # #800000
C_BLACK = RGBColor(0, 0, 0)

def format_run(run, font_name="Times New Roman", size_pt=13, bold=False, italic=False, color=None):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color

def add_h1(text):
    h = doc.add_heading(text, level=1)
    h.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    for r in h.runs:
        format_run(r, size_pt=16, bold=True, color=C_NAVY)
    return h

def add_h2(text):
    h = doc.add_heading(text, level=2)
    h.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    for r in h.runs:
        format_run(r, size_pt=14, bold=True, color=C_NAVY)
    return h

def add_h3(text):
    h = doc.add_heading(text, level=3)
    h.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(2)
    h.paragraph_format.keep_with_next = True
    for r in h.runs:
        format_run(r, size_pt=13, bold=True, color=C_MAROON)
    return h

def add_body(text, bold_prefix="", indent_cm=1.0):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.35
    if indent_cm > 0:
        p.paragraph_format.first_line_indent = Cm(indent_cm)
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        format_run(r_bold, size_pt=13, bold=True, color=C_BLACK)
    r_text = p.add_run(text)
    format_run(r_text, size_pt=13, bold=False, color=C_BLACK)
    return p

def add_bullet(text, bold_prefix="", bullet_char="• "):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.left_indent = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.4)
    r_b = p.add_run(bullet_char)
    format_run(r_b, size_pt=13, bold=True, color=C_BLACK)
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        format_run(r_bold, size_pt=13, bold=True, color=C_BLACK)
    r_text = p.add_run(text)
    format_run(r_text, size_pt=13, bold=False, color=C_BLACK)
    return p

def add_numbered_item(num_str, bold_prefix, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.left_indent = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    
    r_num = p.add_run(num_str + " ")
    format_run(r_num, size_pt=13, bold=True, color=C_BLACK)
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        format_run(r_bold, size_pt=13, bold=True, color=C_BLACK)
    r_text = p.add_run(text)
    format_run(r_text, size_pt=13, bold=False, color=C_BLACK)
    return p

def add_reference_item(ref_num, text_bold, text_normal):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.left_indent = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    
    r_num = p.add_run(ref_num + " ")
    format_run(r_num, size_pt=13, bold=True, color=C_BLACK)
    if text_bold:
        r_bold = p.add_run(text_bold + " ")
        format_run(r_bold, size_pt=13, bold=True, color=C_BLACK)
    r_text = p.add_run(text_normal)
    format_run(r_text, size_pt=13, bold=False, color=C_BLACK)
    return p

print("Bắt đầu nối Chương 5 vào Bao_Cao_Thuc_Nghiem_RCWL1601.docx...")

# Ngắt trang trước khi bắt đầu Chương 5
doc.add_page_break()

# ==========================================================
# CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ
# ==========================================================
add_h1("CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ")

# 5.1. Kết luận chung về đề tài
add_h2("5.1. Kết luận chung về đề tài")

add_body(
    "Đề tài nghiên cứu và đánh giá thực nghiệm cảm biến khoảng cách siêu âm RCWL-1601 trên nền tảng vi điều khiển ESP32 trong khuôn khổ học phần Kỹ thuật Đo lường và Cảm biến (EMA2024E_3) đã hoàn thành toàn diện các mục tiêu khoa học và kỹ thuật:"
)

add_numbered_item(
    "1.",
    "Xây dựng thành công hệ thống đo lường thực nghiệm chuẩn hóa: ",
    "Thiết lập giàn thử nghiệm cơ khí với ray trượt định hướng dài 7 m, con trỏ đọc vạch chia 1 mm, cơ cấu giữ bia phản xạ vuông góc 90° và độ cao giá đỡ 75 cm triệt tiêu hoàn toàn sóng dội từ mặt sàn. Kết nối trực tiếp RCWL-1601 với ESP32 ở mức logic 3.3 V, cấu hình bộ định thời phần cứng đo ToF với độ phân giải 1 μs (Δd_LSB ≈ 0.174 mm). Chứng minh cỡ mẫu N = 50 lần đo là tối ưu tuyệt đối, cân bằng hoàn hảo giữa việc thu hẹp khoảng tin cậy Student 95% (ε_95% ≤ 0.05 mm) và duy trì tần suất quét thời gian thực."
)

add_numbered_item(
    "2.",
    "Khảo sát định lượng toàn diện các đặc tính tĩnh và động: ",
    "Phương trình hồi quy OLS bậc 1 đạt ŷ = 1.00273 · x - 0.48427 (cm) với R² > 0.9999 trên dải làm việc 5 – 400 cm. Kiểm chứng mù trên 10 mốc Test độc lập khẳng định Bậc 1 vượt trội hơn Bậc 2 và Bậc 3 trên cả chỉ số sai số tuyệt đối (∑|e| = 41.07 mm) lẫn sai số bình phương (MSE = 33.90 mm²); độ phi tuyến cực đại chỉ đạt ±0.361% FS. Cảm biến đo ổn định tới 550 cm trên mặt phẳng nhẵn (vượt 22% so với datasheet 450 cm), xác định chính xác vùng chết vật lý 0 – 3 cm do dao động dư của màng gốm (150 μs) và ngưỡng ngắt câm của vi mạch RCWL-9610. Độ lệch chuẩn lặp lại đạt s < 0.4 mm ở cự ly gần, hệ số biến thiên CV% < 0.11% trên toàn dải, độ không lặp lại ≤ ±0.143% FS, vòng trễ thực nghiệm cực nhỏ γ_H = 0.553%. Thuật toán bù nhiệt Laplace thời gian thực v(T) = 331.3 + 0.606 · T triệt tiêu trôi nhiệt hàng xentimét ở môi trường lạnh, kéo toàn bộ sai số về quanh đường 0 mm. Ngân sách độ không đảm bảo đo chuẩn hóa (ISO/GUM) xác định U_95% ≤ 0.77 mm ở cự ly gần (d ≤ 50 cm) và duy trì dưới ±5.57 mm trên toàn dải xa 550 cm."
)

add_numbered_item(
    "3.",
    "Hiện thực hóa thành công mô hình ứng dụng thực tế (Chương 4): ",
    "Chế tạo và vận hành thành công mô hình giám sát mức và thể tích chất lỏng trên bình chứa chai nước ngọt 2L cắt (H = 17 cm, D = 10 cm) kết hợp bơm chìm mini 6V trên vi điều khiển ESP32. Vận dụng sáng tạo 4 phát hiện thực nghiệm: cơ cấu gá cao 5 cm vượt vùng chết, bù nhiệt Laplace qua DHT11, chuỗi lọc 2 tầng (IQR + Moving Average) nén dao động sóng gợn từ ±0.7 cm xuống dưới ±0.08 cm, và lan truyền độ KĐBĐ thể tích theo ISO/GUM đạt δ_V = ±3.49% < 5%. Thiết lập phân cấp 4 ngưỡng trạng thái (Low-Low, Low, Normal, High-High) với cơ chế trễ ngưỡng (hysteretic deadband) chống rung giật relay, điều khiển bơm an toàn chống cạn và chống tràn."
)

# 5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật
add_h2("5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật")

# 5.2.1. Đánh giá ưu điểm và hạn chế của cảm biến RCWL-1601
add_h3("5.2.1. Đánh giá ưu điểm và hạn chế của cảm biến RCWL-1601")

add_body(
    "Từ các kết quả nghiên cứu lý thuyết và kiểm chứng thực nghiệm chuyên sâu, các ưu điểm nổi bật và hạn chế vật lý của module cảm biến RCWL-1601 được đúc kết như sau:"
)

p_pro = doc.add_paragraph()
p_pro.paragraph_format.space_before = Pt(2)
p_pro.paragraph_format.space_after = Pt(2)
r_pro = p_pro.add_run("Ưu điểm nổi bật:")
format_run(r_pro, size_pt=13, bold=True, color=C_NAVY)

add_bullet("Chi phí linh kiện thấp nhưng đạt độ chính xác và độ lặp lại tiệm cận cảm biến công nghiệp khi được chuẩn hóa thuật toán xử lý dữ liệu.", bold_prefix="Hiệu quả kinh tế cao: ")
add_bullet("Hoạt động trực tiếp với chân logic của vi điều khiển ESP32 mà không cần IC chuyển đổi mức điện áp.", bold_prefix="Tương thích tối ưu hệ nhúng 3.3 V: ")
add_bullet("Tầng tiền khuếch đại tự động điều chỉnh độ lợi của vi mạch RCWL-9610 cho phép bắt sóng tin cậy tới 550 cm trên mặt phản xạ phẳng.", bold_prefix="Tầm đo vượt trội trên mặt phẳng: ")
add_bullet("Lý tưởng cho môi trường đo mức chất lỏng, tránh hoàn toàn nguy cơ ăn mòn hóa học và bám dính cặn bẩn.", bold_prefix="Phương pháp đo không tiếp xúc: ")

p_con = doc.add_paragraph()
p_con.paragraph_format.space_before = Pt(4)
p_con.paragraph_format.space_after = Pt(2)
r_con = p_con.add_run("Hạn chế vật lý:")
format_run(r_con, size_pt=13, bold=True, color=C_MAROON)

add_bullet("Mất hoàn toàn tín hiệu đo khi vật thể áp sát đầu thu/phát dưới 3 cm do hiện tượng dao động dư cơ học.", bold_prefix="Vùng chết vật lý 0 – 3 cm: ")
add_bullet("Hiện tượng tán xạ khuếch tán làm độ lệch chuẩn tăng vọt gấp 15 – 26 lần và co hẹp cự ly đo tin cậy từ 550 cm xuống 350 cm.", bold_prefix="Suy hao mạnh trên bề mặt gồ ghề/xốp: ")
add_bullet("Vận tốc âm phụ thuộc chặt vào nhiệt độ không khí (0.606 m/s cho mỗi độ C), gây trôi sai số tích lũy hàng xentimét nếu không bù nhiệt.", bold_prefix="Độ nhạy nhiệt độ cao: ")

# 5.2.2. Khuyến nghị kỹ thuật khi triển khai thực tế
add_h3("5.2.2. Khuyến nghị kỹ thuật khi triển khai thực tế")

add_body(
    "Để khai thác tối đa độ tin cậy và độ chính xác của module RCWL-1601 trong môi trường sản xuất công nghiệp và dân dụng, các giải pháp kỹ thuật sau đây được khuyến nghị:"
)

add_numbered_item(
    "1.",
    "Thiết kế cơ khí: ",
    "Luôn thiết kế cơ cấu gá cảm biến cao hơn mức chất lỏng tối đa tối thiểu 5 – 10 cm để triệt tiêu hoàn toàn nguy cơ rơi vào vùng chết. Bố trí cảm biến tránh xa thành bình để chùm sóng âm hình nón 15° không bắt phản xạ giả từ vách bồn hoặc đường ống nạp liệu."
)

add_numbered_item(
    "2.",
    "Bù nhiệt độ thời gian thực: ",
    "Bắt buộc tích hợp cảm biến nhiệt độ (như DHT11, DS18B20) đặt gần đường truyền sóng để cập nhật động v(T) theo thời gian thực, loại bỏ hoàn toàn sai số trôi cự ly do thời tiết hoặc nhiệt độ môi trường biến đổi."
)

add_numbered_item(
    "3.",
    "Chuỗi lọc số thích nghi: ",
    "Áp dụng kết hợp lọc Khoảng tứ phân vị IQR (N = 5) triệt tiêu 100% xung ngoại lai bọt khí đột biến và lọc Trung bình trượt (Moving Average, W = 7) san phẳng sóng gợn mặt nước do bơm nạp, giữ tín hiệu đo êm dịu và chính xác."
)

add_numbered_item(
    "4.",
    "Điều khiển có trễ ngưỡng: ",
    "Thiết lập dải trễ logic (hysteretic deadband) khi đóng cắt bơm hoặc van điện từ nhằm chống hiện tượng rung giật relay (chattering) khi mức nước xao động quanh ngưỡng cảnh báo, giúp kéo dài tuổi thọ thiết bị chấp hành."
)

# 5.3. Tài liệu tham khảo
add_h2("5.3. Tài liệu tham khảo")

add_reference_item("[1]", "JCGM 100:2008,", "Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM), Joint Committee for Guides in Metrology (BIPM, IEC, IFCC, ILAC, ISO, IUPAC, IUPAP, OIML).")
add_reference_item("[2]", "ISO/IEC 17025:2017,", "General requirements for the competence of testing and calibration laboratories, International Organization for Standardization.")
add_reference_item("[3]", "Kinsler, L. E., Frey, A. R., Coppens, A. B., & Sanders, J. V. (2000),", "Fundamentals of Acoustics, 4th Edition, John Wiley & Sons, New York.")
add_reference_item("[4]", "Wuxi Ri-Chow Technology Co., Ltd. (2019),", "RCWL-1601 Ultrasonic Distance Measurement Module Datasheet & RCWL-9610 IC Technical Specification, Rev 1.2.")
add_reference_item("[5]", "Espressif Systems (2023),", "ESP32 Technical Reference Manual, Version 5.0, Espressif Systems Co., Ltd.")
add_reference_item("[6]", "Tukey, J. W. (1977),", "Exploratory Data Analysis, Addison-Wesley Publishing Company, Reading, Mass.")

# Lưu tài liệu
doc.save(FILE_PATH)
print("Hoàn tất nối tiếp Chương 5 vào Bao_Cao_Thuc_Nghiem_RCWL1601.docx thành công!")
