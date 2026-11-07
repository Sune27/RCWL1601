# -*- coding: utf-8 -*-
"""
Kịch bản nối tiếp Chương 5 (Kết luận và Kiến nghị) và Tài liệu tham khảo vào tệp Word hiện có (Bao_Cao_Thuc_Nghiem_RCWL1601.docx)
Tuân thủ nghiêm ngặt quy chuẩn GEMINI.md (Rules 1–22):
- Heading 1: 16pt, Bold, C_NAVY (#003366)
- Heading 2: 14pt, Bold, C_NAVY (#003366)
- Heading 3: 13pt, Bold, C_MAROON (#800000)
- Body text: 13pt, Line spacing 1.35, Space after 5pt, Justified, First-line indent 1.0cm
- Bullet & Numbered points: 13pt, Line spacing 1.35, Justified, Hanging indent
- Công thức hồi quy tuyến tính bậc 1: Đối tượng toán học OMML chuẩn Word Equation
- Tài liệu tham khảo: 11 tài liệu chính thống đã kiểm chứng (JCGM 100:2008, TCVN 9595-3:2013, ISO/IEC 17025:2017, Kinsler, Bohn, RCWL-1601/9610, ESP32 TRM v5.2, Tukey, Doebelin, Montgomery & Runger, Phan Quốc Phô & Nguyễn Đức Chiến)
"""

import os
import sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "Bao_Cao_Thuc_Nghiem_RCWL1601.docx")

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
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.35
    if indent_cm > 0:
        p.paragraph_format.first_line_indent = Cm(indent_cm)
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        format_run(r_bold, size_pt=13, bold=True, color=C_BLACK)
    r_text = p.add_run(text)
    format_run(r_text, size_pt=13, bold=False, color=C_BLACK)
    return p


def add_bullet(text, bold_prefix="", bullet_char="• ", left_cm=1.25, hanging_cm=0.4):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.left_indent = Cm(left_cm)
    p.paragraph_format.first_line_indent = Cm(-hanging_cm)
    r_b = p.add_run(bullet_char)
    format_run(r_b, size_pt=13, bold=True, color=C_BLACK)
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        format_run(r_bold, size_pt=13, bold=True, color=C_BLACK)
    r_text = p.add_run(text)
    format_run(r_text, size_pt=13, bold=False, color=C_BLACK)
    return p


def add_numbered_item(num_str, bold_prefix, text, left_cm=0.75, hanging_cm=0.5, italic_prefix=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.left_indent = Cm(left_cm)
    p.paragraph_format.first_line_indent = Cm(-hanging_cm)
    r_num = p.add_run(num_str + " ")
    format_run(r_num, size_pt=13, bold=True, color=C_BLACK)
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        format_run(r_bold, size_pt=13, bold=True, italic=italic_prefix, color=C_BLACK)
    if text:
        r_text = p.add_run(text)
        format_run(r_text, size_pt=13, bold=False, color=C_BLACK)
    return p


def add_reference_item(ref_num, authors_bold, title_italic, rest_text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(1.5)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-1.0)
    r_num = p.add_run(ref_num + " ")
    format_run(r_num, size_pt=13, bold=True, color=C_BLACK)
    r_auth = p.add_run(authors_bold)
    format_run(r_auth, size_pt=13, bold=True, color=C_BLACK)
    if title_italic:
        r_tit = p.add_run(title_italic)
        format_run(r_tit, size_pt=13, italic=True, color=C_BLACK)
    r_rest = p.add_run(rest_text)
    format_run(r_rest, size_pt=13, bold=False, color=C_BLACK)
    return p


print("Bắt đầu nối Chương 5 vào Bao_Cao_Thuc_Nghiem_RCWL1601.docx...")

doc.add_page_break()

add_h1("CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ")
add_h2("5.1. Kết luận chung về đề tài")

add_body(
    "Đề tài nghiên cứu, khảo sát thực nghiệm các đặc tính đo lường của module cảm biến khoảng cách siêu âm RCWL-1601 trên nền tảng vi điều khiển 32-bit ESP32 và xây dựng hệ thống ứng dụng giám sát mức chất lỏng thông minh trong khuôn khổ học phần Kỹ thuật Đo lường và Cảm biến (EMA2024E_3) đã hoàn thành toàn diện các mục tiêu khoa học và kỹ thuật đề ra:"
)

add_numbered_item("1.", "Xây dựng thành công hệ thống đo lường thực nghiệm chuẩn hóa:", "")
add_bullet(
    "Thiết lập mô hình thực nghiệm trên hai bàn đo cao 85.0 cm đặt dọc theo hành lang kín gió dài 10 m (rộng 2.8 m, cách tường bên tối thiểu 1.4 m) nhằm loại trừ hoàn toàn phản xạ phụ từ mặt sàn và vách tường trong góc mở chùm sóng 15°. Cảm biến RCWL-1601 được cố định trên breadboard sát mép bàn; vật thể phản xạ mục tiêu là viên gạch chuẩn kích thước 40 cm × 40 cm (mặt trước phẳng nhẵn và mặt sau gồ ghề) dựng thẳng đứng vuông góc 90° với trục phát sóng; cự ly chuẩn d_true được xác lập bằng thước dây tiêu chuẩn.",
    bold_prefix="Phương thức bố trí và định vị thiết bị đo: "
)
add_bullet(
    "Kết nối trực tiếp RCWL-1601 với vi điều khiển ESP32 ở mức logic 3.3 V, cấu hình bộ định thời phần cứng đo thời gian bay ToF với độ phân giải 1 μs (Δd_LSB ≈ 0.174 mm).",
    bold_prefix="Giao tiếp phần cứng và thu thập dữ liệu: "
)
add_bullet(
    "Từ chuỗi đo thăm dò 100 lần liên tiếp tại 3 mốc cự ly (50 cm, 100 cm, 150 cm), phân tích bán kính sai số ngẫu nhiên ε_95%(k) theo phân phối Student và tốc độ biến thiên |dε_95%/dk| đã chứng minh cỡ mẫu N = 50 lần đo là tối ưu, đảm bảo ε_95% < 0.5 mm (nhỏ hơn nửa độ chia thước chuẩn) và đạt ngưỡng dừng bão hòa sai số (|dε/dk| ≈ 0).",
    bold_prefix="Tối ưu hóa cỡ mẫu thống kê: "
)

add_numbered_item("2.", "Khảo sát định lượng toàn diện các đặc tính tĩnh và các yếu tố ảnh hưởng vật lý:", "")
add_bullet(
    "Trên tổng số 4.800 mẫu đo thuộc 4 trường hợp thực nghiệm (FSDT, BSDT, FRDT, FSAT), giải thuật lọc IQR (Tukey's Fences) đã phát hiện và loại bỏ chính xác 235 mẫu ngoại lai (4.90%), giữ lại 4.565 mẫu hợp lệ (95.10%), giúp kéo độ lệch chuẩn tại vùng biên 580 – 600 cm từ 346.05 – 2621.02 mm về mức ổn định 0.09 – 4.0 mm.",
    bold_prefix="Tiền xử lý và lọc sai số thô bằng Khoảng tứ phân vị (IQR): "
)
add_bullet(
    "Xác định rõ 4 phân vùng làm việc trên mặt phẳng nhẵn: Vùng chết vật lý (0 – 3 cm, kết quả bị kẹp ở 2.03 – 2.68 cm do dao động dư màng gốm áp điện 150 μs và mạch ngắt câm nội của IC RCWL-9610), Dải đo tuyến tính ổn định (5 – 400 cm), Dải đo xa vượt định mức (420 – 550 cm, vượt 22% so với trần công bố 450 cm của nhà sản xuất) và Ngưỡng bão hòa xa (580 – 600 cm, tràn thời gian bay tại 824.56 cm). Chốt dải làm việc tin cậy thực tế trên mặt nhẵn là 10 cm – 550 cm.",
    bold_prefix="Phân vùng dải đo thực tế: "
)
add_bullet(
    "Trên toàn dải hữu ích 1 – 550 cm (33 mốc), độ lệch chuẩn đạt s < 0.4 mm ở cự ly gần và sai số chuẩn trung bình SE = s/√n luôn được nén phẳng dưới 0.5726 mm (32/33 mốc đạt SE < 0.45 mm). Trong dải 50 – 550 cm, sai số tuyệt đối nằm trong khoảng [-5.71, +14.02] mm và sai số tương đối hội tụ chặt trong dải [-0.57%, +0.35%].",
    bold_prefix="Độ chụm và Độ chính xác cao: "
)
add_bullet(
    "Phân chia 34 mốc đo theo tỷ lệ 70% Huấn luyện (24 mốc) và 30% Kiểm thử độc lập (10 mốc). Kết quả đối sánh xác nhận phương trình hồi quy tuyến tính Bậc 1:",
    bold_prefix="Độ tuyến tính (Linearity): "
)

p_eq = doc.add_paragraph()
p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
omml_eq = (
    '<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
    '<m:oMath>'
    '<m:sSub><m:e><m:acc><m:accPr><m:chr m:val="&#x0302;"/></m:accPr><m:e><m:r><m:t>y</m:t></m:r></m:e></m:acc></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub>'
    '<m:r><m:t> = 1.00273 &#x22C5; x &#x2212; 0.48427   </m:t></m:r>'
    '<m:r><m:rPr><m:nor/></m:rPr><m:t>(cm)</m:t></m:r>'
    '</m:oMath>'
    '</m:oMathPara>'
)
p_eq._p.append(parse_xml(omml_eq))

add_body(
    "đạt tổng sai số tuyệt đối tích lũy thấp nhất trên tập kiểm thử (∑|e| = 41.07 mm), vượt trội so với mô hình Bậc 2 và Bậc 3 (∑|e| = 47.45 mm) và phản ánh đúng độ thụt lùi cơ khí ≈ 4.84 mm của màng rung áp điện.",
    indent_cm=1.25
)
add_bullet(
    "Khảo sát đối xứng giữa Chiều tiến (FSDT) và Chiều lùi (BSDT) trên 19 mốc chung (10 – 300 cm) ghi nhận độ lệch trễ cực đại ΔH_max = 1.6598 cm tại 200 cm, tương ứng sai số trễ tương đối γ_H,test = 0.553% (trên thang 300 cm) và γ_H,FS = 0.302% (trên toàn dải 550 cm), khẳng định bản chất phi trễ nội tại của phép đo sóng âm ToF.",
    bold_prefix="Độ trễ hai chiều (Hysteresis): "
)
add_bullet(
    "Tán xạ khuếch tán trên mặt gạch gồ ghề (FRDT) làm độ lệch chuẩn s tăng gấp 3 – 26 lần so với mặt nhẵn và thu hẹp giới hạn đo từ 550 cm xuống 350 cm (chớm mất xung ở 350 cm và mất hoàn toàn tín hiệu từ 375 – 380 cm).",
    bold_prefix="Ảnh hưởng của bề mặt phản xạ: "
)
add_bullet(
    "Đối chứng giữa nhiệt độ phòng chuẩn hóa 27.0 °C (v = 347.662 m/s) và phòng lạnh 20.0 °C (v = 343.420 m/s) cho thấy nếu không bù nhiệt, kết quả đo bị phóng đại +1.235% quãng đường (trôi tới +39.92 mm tại 280 cm). Khi kích hoạt bù nhiệt Laplace thời gian thực v(T) = 331.3 + 0.606 · T, sai số trôi nhiệt hàng xentimét bị triệt tiêu hoàn toàn, kéo Δx về dao động quanh 0 mm (14/14 mốc từ 80 – 300 cm đạt |δ%| ≤ 0.57%).",
    bold_prefix="Ảnh hưởng của nhiệt độ và hiệu quả bù nhiệt Laplace: "
)
add_bullet(
    "Kết hợp đầy đủ thành phần Loại A (u_A = s/√N) và Loại B (u_B1 ≈ 0.289 mm từ thước chuẩn, u_B2 ≈ 0.050 mm từ bộ đếm Timer ESP32, u_B3(d) ≈ 0.000503 · d mm từ cảm biến nhiệt độ). Độ không đảm bảo đo mở rộng (k = 2, mức tin cậy 95%) đạt U_95% ≤ 0.77 mm ở cự ly gần (d ≤ 50 cm) và luôn duy trì dưới ±5.57 mm trên toàn dải đo đến 550 cm.",
    bold_prefix="Đánh giá tổng hợp độ không đảm bảo đo theo chuẩn ISO/GUM: "
)

add_numbered_item("3.", "Hiện thực hóa thành công mô hình ứng dụng thực tế (Chương 4):", "")
add_bullet(
    "Chế tạo và vận hành thành công mô hình hệ thống giám sát mức và thể tích chất lỏng thông minh trên bình chứa từ chai nước ngọt 2L cắt (H_bình = 17.0 cm, đường kính trong D = 10.0 cm, bán kính R = 5.0 cm, diện tích đáy S_base ≈ 78.54 cm², dung tích tối đa V_max ≈ 1335.2 mL), kết hợp bơm chìm mini 6 V, cảm biến nhiệt độ DHT11 (T ≈ 30.8 °C) và khối chỉ thị LED Xanh/Đỏ trên vi điều khiển ESP32."
)
add_bullet("Vận dụng trực tiếp 4 phát hiện thực nghiệm cốt lõi vào thiết kế:")
add_numbered_item(
    "(1)",
    "Bố trí cơ cấu gá cao H_gá = 5.0 cm trên miệng bình (H_tổng = 22.0 cm): ",
    "Khi mức nước chạm ngưỡng ngắt bơm cao nhất (h = 14.0 cm), khoảng cách đo vẫn đạt d = 8.0 cm > 3.0 cm, triệt tiêu hoàn toàn nguy cơ rơi vào vùng chết.",
    left_cm=1.75, hanging_cm=0.5, italic_prefix=True
)
add_numbered_item(
    "(2)",
    "Bù nhiệt độ Laplace thời gian thực qua DHT11: ",
    "Khử sai số trôi vận tốc truyền âm theo vi khí hậu phòng đo.",
    left_cm=1.75, hanging_cm=0.5, italic_prefix=True
)
add_numbered_item(
    "(3)",
    "Chuỗi lọc số thích nghi 2 tầng: ",
    "Kết hợp lọc Khoảng tứ phân vị IQR (N = 5) loại bỏ 100% xung gai bọt khí đột biến và lọc Trung bình trượt (Moving Average, W = 7) nén dao động sóng gợn mặt nước từ ±0.7 cm xuống dưới ±0.08 cm.",
    left_cm=1.75, hanging_cm=0.5, italic_prefix=True
)
add_numbered_item(
    "(4)",
    "Lan truyền độ không đảm bảo đo thể tích theo chuẩn ISO/GUM: ",
    "Kết hợp độ không đảm bảo đo bán kính bình (u_R = 0.04 cm) và mức nước (u_h = 0.071 cm); tại mốc vận hành chuẩn h = 10.1 cm (V = 792.5 mL), đạt u_c(V) = ±13.8 mL và U_95%(V) = ±27.7 mL (k = 2), tương ứng độ không đảm bảo tương đối δ_V = ±3.49% < 5%.",
    left_cm=1.75, hanging_cm=0.5, italic_prefix=True
)
add_bullet(
    "Thiết lập phân cấp 4 ngưỡng trạng thái an toàn (Low-Low h ≤ 2.5 cm, Low 2.5 < h ≤ 5.0 cm, Normal 5.0 < h < 14.0 cm, High-High h ≥ 14.0 cm) tích hợp cơ chế trễ ngưỡng (hysteretic deadband) chống rung giật tiếp điểm rơ-le, bảo vệ bơm chống chạy khan và chống tràn tự động."
)

add_h2("5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật")
add_h3("5.2.1. Đánh giá ưu điểm và hạn chế của cảm biến RCWL-1601")
add_body(
    "Từ các kết quả nghiên cứu lý thuyết và kiểm chứng thực nghiệm chuyên sâu, các ưu điểm nổi bật và hạn chế vật lý của module cảm biến RCWL-1601 được đúc kết như sau:"
)

p_pro = doc.add_paragraph()
p_pro.paragraph_format.space_before = Pt(4)
p_pro.paragraph_format.space_after = Pt(2)
r_pro = p_pro.add_run("• Ưu điểm nổi bật:")
format_run(r_pro, size_pt=13, bold=True, color=C_NAVY)

add_numbered_item("1.", "Hiệu quả kinh tế cao: ", "Chi phí phần cứng thấp nhưng đạt độ chính xác và độ chụm tiệm cận cảm biến công nghiệp khi được chuẩn hóa bằng thuật toán lọc số và bù nhiệt.", left_cm=1.25, hanging_cm=0.5, italic_prefix=True)
add_numbered_item("2.", "Tương thích trực tiếp hệ nhúng 3.3 V: ", "Hoạt động ổn định với mức điện áp logic 3.3 V của vi điều khiển ESP32 mà không cần mạch chuyển mức điện áp.", left_cm=1.25, hanging_cm=0.5, italic_prefix=True)
add_numbered_item("3.", "Tầm đo mở rộng vượt trội trên mặt phẳng nhẵn: ", "Tầng khuếch đại của vi mạch RCWL-9610 cho phép thu nhận sóng phản xạ gương tin cậy tới 550 cm.", left_cm=1.25, hanging_cm=0.5, italic_prefix=True)
add_numbered_item("4.", "Phương pháp đo không tiếp xúc: ", "Phù hợp cho bài toán giám sát mức chất lỏng, tránh ăn mòn hóa học và bám cặn lên bề mặt cảm biến.", left_cm=1.25, hanging_cm=0.5, italic_prefix=True)

p_con = doc.add_paragraph()
p_con.paragraph_format.space_before = Pt(4)
p_con.paragraph_format.space_after = Pt(2)
r_con = p_con.add_run("• Hạn chế vật lý:")
format_run(r_con, size_pt=13, bold=True, color=C_MAROON)

add_numbered_item("1.", "Vùng chết vật lý 0 – 3 cm: ", "Mất khả năng đo chính xác khi vật thể áp sát mặt cảm biến dưới 3 cm do dao động dư cơ học của màng gốm áp điện.", left_cm=1.25, hanging_cm=0.5, italic_prefix=True)
add_numbered_item("2.", "Suy hao mạnh trên bề mặt gồ ghề/nhám: ", "Tán xạ khuếch tán làm độ lệch chuẩn tăng gấp 3 – 26 lần và thu hẹp cự ly đo tin cậy từ 550 cm xuống còn 350 cm.", left_cm=1.25, hanging_cm=0.5, italic_prefix=True)
add_numbered_item("3.", "Độ nhạy nhiệt độ môi trường lớn: ", "Vận tốc âm thanh biến thiên 0.606 m/s trên mỗi 1 °C, gây sai số trôi tỷ lệ thuận với khoảng cách nếu không có cảm biến nhiệt độ bù trừ.", left_cm=1.25, hanging_cm=0.5, italic_prefix=True)

add_h3("5.2.2. Khuyến nghị kỹ thuật khi triển khai thực tế")
add_body(
    "Để khai thác tối đa độ tin cậy và độ chính xác của module RCWL-1601 trong các ứng dụng thực tế, nhóm nghiên cứu đề xuất 4 khuyến nghị kỹ thuật trọng tâm:"
)
add_numbered_item("1.", "Bố trí khoảng cách ly vượt vùng chết và tránh phản xạ thành bồn: ", "Luôn lắp đặt cảm biến cao hơn mức chất lỏng tối đa tối thiểu 5 – 10 cm để đảm bảo mặt thoáng không bao giờ xâm nhập vùng chết 0 – 3 cm. Đồng thời, đặt cảm biến cách thành bồn tối thiểu R_cone = d · tan(7.5°) ≈ 0.13 · d hoặc sử dụng ống dẫn hướng sóng tĩnh (stilling well) để chùm sóng mở 15° không bắt phản xạ giả từ vách đứng.")
add_numbered_item("2.", "Bắt buộc tích hợp bù nhiệt độ Laplace thời gian thực: ", "Luôn bố trí cảm biến nhiệt độ (như DHT11 hoặc DS18B20) gần không gian truyền sóng để cập nhật động v(T) = 331.3 + 0.606 · T trước mỗi chu kỳ đo, triệt tiêu sai số trôi nhiệt độ theo thời tiết ngày/đêm.")
add_numbered_item("3.", "Ứng dụng chuỗi lọc số thích nghi 2 tầng: ", "Kết hợp tầng lọc Khoảng tứ phân vị IQR (N = 5) để cắt bỏ các xung ngoại lai đột biến do bọt khí hoặc mất xung phản hồi với tầng lọc Trung bình trượt (Moving Average, W = 7) để làm mịn dao động sóng gợn mặt thoáng khi bơm nạp/xả.")
add_numbered_item("4.", "Thiết lập điều khiển có dải trễ ngưỡng (Hysteretic Deadband): ", "Áp dụng dải trễ logic giữa ngưỡng bật bơm và ngưỡng ngắt bơm nhằm chống hiện tượng đóng cắt liên tục gây rung giật và phóng điện hồ quang tại tiếp điểm rơ-le (relay chattering) khi mặt nước dao động quanh ranh giới cảnh báo, đồng thời cách ly nguồn động lực của máy bơm khỏi nguồn 3.3 V của vi điều khiển.")

add_h2("5.3. Tài liệu tham khảo")
add_reference_item("[1]", "JCGM 100:2008 (ISO/IEC Guide 98-3:2008), ", "Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM 1995 with minor corrections)", ", Joint Committee for Guides in Metrology (BIPM, IEC, IFCC, ILAC, ISO, IUPAC, IUPAP, OIML), Sèvres, France, 2008.")
add_reference_item("[2]", "TCVN 9595-3:2013 (ISO/IEC Guide 98-3:2008), ", "Độ không đảm bảo đo — Phần 3: Hướng dẫn trình bày độ không đảm bảo đo (GUM:1995)", ", Bộ Khoa học và Công nghệ, Hà Nội, 2013.")
add_reference_item("[3]", "ISO/IEC 17025:2017 (TCVN ISO/IEC 17025:2017), ", "General requirements for the competence of testing and calibration laboratories (Yêu cầu chung về năng lực của phòng thử nghiệm và hiệu chuẩn)", ", International Organization for Standardization, Geneva, Switzerland, 2017.")
add_reference_item("[4]", "L. E. Kinsler, A. R. Frey, A. B. Coppens, and J. V. Sanders, ", "Fundamentals of Acoustics", ", 4th Edition, John Wiley & Sons, Inc., New York, 2000, ISBN: 978-0-471-84789-2.")
add_reference_item("[5]", "D. A. Bohn, “Environmental Effects on the Speed of Sound,” ", "Journal of the Audio Engineering Society (JAES)", ", vol. 36, no. 4, pp. 223–231, April 1988.")
add_reference_item("[6]", "Wuxi Richen IoT Technology Co., Ltd. (RCWL) & Adafruit Industries, ", "RCWL-1601 Open-Type Ultrasonic Distance Sensor Module & RCWL-9610 Ultrasonic Ranging IC Technical Specification", ", Adafruit Product ID 4007 / RCWL-9610 Datasheet Rev 1.0, 2019–2022.")
add_reference_item("[7]", "Espressif Systems, ", "ESP32 Technical Reference Manual", ", Version 5.2, Espressif Systems (Shanghai) Co., Ltd., 2024.")
add_reference_item("[8]", "J. W. Tukey, ", "Exploratory Data Analysis", ", Addison-Wesley Publishing Company, Reading, Massachusetts, 1977, ISBN: 978-0-201-07616-5.")
add_reference_item("[9]", "E. O. Doebelin, ", "Measurement Systems: Application and Design", ", 5th Edition, McGraw-Hill, New York, 2003, ISBN: 978-0-07-243886-4.")
add_reference_item("[10]", "D. C. Montgomery and G. C. Runger, ", "Applied Statistics and Probability for Engineers", ", 7th Edition, John Wiley & Sons, Inc., Hoboken, New Jersey, 2018, ISBN: 978-1-119-40036-3.")
add_reference_item("[11]", "Phan Quốc Phô, Nguyễn Đức Chiến, ", "Giáo trình Cảm biến", ", Nhà xuất bản Khoa học và Kỹ thuật, Hà Nội, 2012.")

doc.save(FILE_PATH)
print("Hoàn tất nối tiếp Chương 5 vào Bao_Cao_Thuc_Nghiem_RCWL1601.docx thành công!")
