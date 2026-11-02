# QUY CHUẨN DỰ ÁN VÀ HƯỚNG DẪN ĐỊNH DẠNG BÁO CÁO KHOA HỌC
Học phần: Kỹ thuật Đo lường và Cảm biến (EMA2024E_3)
Đề tài: Nghiên cứu, Đánh giá Thực nghiệm Cảm biến Siêu âm RCWL-1601 và Ứng dụng Bồn chứa Thông minh

> Tệp tài liệu này là quy chuẩn tối cao cho Antigravity (và các tác nhân AI/kỹ sư tham gia dự án). Bất kỳ phiên bản Antigravity nào khi mở thư mục dự án này trên mọi thiết bị đều phải tuân thủ nghiêm ngặt các nguyên tắc dưới đây.

---

## 1. QUY CHUẨN ĐỒ HỌA VÀ TẠO ĐỒ THỊ KỸ THUẬT (PYTHON / MATPLOTLIB)

Khi tạo mới hoặc cập nhật các đồ thị phân tích dữ liệu, các kịch bản Python phải tuân theo cấu hình chuẩn hóa sau:

### 1.1. Thiết lập Font chữ và Khử lỗi hiển thị Tiếng Việt
* **Font chữ bắt buộc:** Sử dụng `Times New Roman`, hỗ trợ hiển thị ký tự Unicode tiếng Việt hoàn hảo, tuyệt đối không bị lỗi ô vuông (mojibake).
* **Cấu hình chuẩn trong mã nguồn:**
  ```python
  import matplotlib.pyplot as plt

  plt.rcParams['font.family'] = 'Segoe UI'
  plt.rcParams['font.size'] = 10
  plt.rcParams['axes.titlesize'] = 11
  plt.rcParams['axes.labelsize'] = 10
  plt.rcParams['xtick.labelsize'] = 9
  plt.rcParams['ytick.labelsize'] = 9
  plt.rcParams['legend.fontsize'] = 9
  plt.rcParams['figure.titlesize'] = 12
  ```

### 1.2. Độ phân giải và Tỷ lệ khung hình (Aspect Ratio)
* **Độ phân giải xuất bản:** Luôn xuất ảnh với `dpi=300`.
* **Kích thước khung hình (`figsize`):**
  * **Đồ thị đơn một trục:** `figsize=(8, 4.5)` hoặc `figsize=(10, 5)`.
  * **Đồ thị kép 2 cột (Subplots ngang):** `figsize=(11, 4.5)` (dùng cho so sánh tiến/lùi, nhẵn/nhám, 32°C/20°C).
  * **Đồ thị 2 tầng (Subplots dọc xếp chồng, chung trục X):** `figsize=(10, 6.5)`.

### 1.3. Bảng màu khoa học (Scientific Color Palette)
* **Màu chính (Primary / Dữ liệu chuẩn):** Xanh lam đậm `#1f77b4`
* **Màu đối chứng (Secondary / Dữ liệu đối sánh):** Màu cam `#ff7f0e`
* **Màu đạt chuẩn / Đã lọc sạch (Pass / Filtered):** Xanh lá cây `#2ca02c` hoặc `#27ae60`
* **Màu cảnh báo / Sai số / Ngoại lai (Warning / Error):** Màu đỏ `#d62728` hoặc `#c0392b`
* **Màu trung tính / Hàng rào / Dung sai:** Màu xám đậm `#7f7f7f` hoặc tím `#9467bd`

### 1.4. Quy ước Đặt tên tệp và Lưu trữ
* Toàn bộ đồ thị xuất ra phải được lưu vào thư mục `graph/`.
* Cú pháp đặt tên: `hinh_<so_chuong>_<stt>_<ten_ngan_khong_dau>.png`
  *(Ví dụ: `hinh_3_1_loc_sai_so_tho.png`, `hinh_4_1_nguyen_ly_bon_chua.png`)*.

---

## 2. QUY CHUẨN ĐỊNH DẠNG TÀI LIỆU WORD (.DOCX) DÀNH CHO BÁO CÁO

Khi kết xuất hoặc định dạng tệp Microsoft Word (`.docx`), phải tuân thủ chuẩn trình bày luận văn kỹ thuật đại học:

### 2.1. Cài đặt Trang in (Page Setup - Khổ A4)
* **Khổ giấy:** A4 ($210\text{ mm} \times 297\text{ mm}$).
* **Căn lề chuẩn (Margins):**
  * Lề Trái (Left - khoảng trống đóng gáy): **$3.0\text{ cm}$** ($30\text{ mm}$)
  * Lề Phải (Right): **$2.0\text{ cm}$** ($20\text{ mm}$)
  * Lề Trên (Top): **$2.0\text{ cm}$** ($20\text{ mm}$)
  * Lề Dưới (Bottom): **$2.0\text{ cm}$** ($20\text{ mm}$)
* **Hướng trang:** Mặc định Portrait (Dọc). Các bảng số liệu quá rộng có thể ngắt phân vùng (Section Break) sang Landscape (Ngang).

### 2.2. Định dạng Văn bản Thường (Body Text / Normal)
* **Font chữ:** **Times New Roman**
* **Cỡ chữ:** **13 pt** (chuẩn mực dễ đọc nhất cho tiếng Việt có dấu)
* **Màu chữ:** Tự động (Black / `#000000`)
* **Căn lề đoạn văn:** Căn đều hai bên (**Justified**)
* **Thụt lề dòng đầu tiên (First Line Indent):** **$1.0\text{ cm}$**
* **Dãn dòng (Line Spacing):** **$1.3\text{ lines}$** đến **$1.5\text{ lines}$**
* **Dãn đoạn (Spacing):**
  * Before (Cách đoạn trước): **$0\text{ pt}$**
  * After (Cách đoạn sau): **$4\text{ pt} - 6\text{ pt}$**

### 2.3. Hệ thống Phân cấp Đề mục (Heading Hierarchy & Navigation Pane)
* **Bắt buộc áp dụng Style gốc của Word:** Mọi tiêu đề Chương, Mục và Tiểu mục bắt buộc phải được gán trực tiếp các kiểu dáng chuẩn (`style='Heading 1'`, `style='Heading 2'`, `style='Heading 3'`), tuyệt đối không sử dụng đoạn văn thường `Normal` rồi chỉnh cỡ chữ thủ công.
* **Tác dụng:** Giúp thanh điều hướng **Navigation Pane** (mở bằng `Ctrl + F` hoặc thẻ `View -> Navigation Pane`) tự động hiển thị cây thư mục đề mục tương tác, cho phép người đọc nhấp chuột để nhảy ngay tới từng phần của báo cáo, đồng thời hỗ trợ cập nhật Mục lục tự động (`TOC`) chính xác 100%.
* **Kỹ thuật lập trình trong Python (python-docx):**
  ```python
  # CHUẨN: Dùng trực tiếp hàm add_heading hoặc gán style Heading
  doc.add_heading("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM", level=1)
  doc.add_heading("1.1. NGUYÊN LÝ ĐO KHOẢNG CÁCH THỜI GIAN BAY", level=2)
  doc.add_heading("1.1.1. Phương trình lan truyền sóng siêu âm thời gian bay", level=3)

  # TUYỆT ĐỐI KHÔNG: Dùng add_paragraph() rồi gán font đậm (Word sẽ coi là Normal và bỏ qua khỏi Navigation Pane)
  ```

| Cấp độ Style Word | Cỡ chữ | Kiểu dáng | Căn lề | Dãn đoạn (Before/After) | Ví dụ minh họa |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Title (Bìa / Tên đề tài)** | $18 - 20\text{ pt}$ | In hoa, Đậm | Căn giữa | $12\text{ pt} / 12\text{ pt}$ | **BÁO CÁO THỰC NGHIỆM ĐO LƯỜNG VÀ CẢM BIẾN** |
| **Heading 1 (Tên Chương)** | $16\text{ pt}$ | In hoa, Đậm | Căn giữa/trái | $16\text{ pt} / 10\text{ pt}$ *(Ngắt trang mới)* | **CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM** |
| **Heading 2 (Mục lớn X.Y)** | $14\text{ pt}$ | Chữ thường, Đậm | Căn trái | $12\text{ pt} / 6\text{ pt}$ | **1.1. NGUYÊN LÝ ĐO KHOẢNG CÁCH THỜI GIAN BAY VÀ MÔ HÌNH LAPLACE** |
| **Heading 3 (Tiểu mục X.Y.Z)** | $13\text{ pt}$ | Chữ thường, Đậm | Căn trái | $8\text{ pt} / 4\text{ pt}$ | **1.1.1. Phương trình lan truyền sóng siêu âm thời gian bay** |
| **Heading 4 (Mục con X.Y.Z.T)** | $13\text{ pt}$ | Chữ thường, Nghiêng đậm | Căn trái | $4\text{ pt} / 2\text{ pt}$ | *1.1.1.1. Hiện tượng suy hao năng lượng cự ly xa* |

### 2.4. Định dạng Bảng biểu (Tables)
* **Vị trí bảng:** Căn giữa trang (Center).
* **Tên bảng:** Đặt **ở TRÊN** bảng, In đậm, cỡ chữ $12\text{ pt}$, căn giữa hoặc căn trái theo bảng. Cú pháp: `Bảng <Chuong>.<STT>: <Tên bảng>`.
  *(Ví dụ: `Bảng 3.1: So sánh dữ liệu đo thô và sau khi áp dụng lọc IQR`).*
* **Dòng tiêu đề bảng (Header Row):**
  * Nền xám nhạt (`#EAEAEA` hoặc `#D9E1F2`), Chữ in đậm, căn giữa.
  * Bật thuộc tính `Repeat Header Rows on every page` để tự lặp lại tiêu đề khi bảng dài qua trang.
* **Dữ liệu trong bảng:** Cỡ chữ $11 - 12\text{ pt}$, căn giữa đối với số liệu/đơn vị, căn trái đối với nội dung văn bản.
* **Đường viền bảng:** Viền trên và dưới bảng nét đậm $1.0\text{ pt}$, viền phân tách tiêu đề $0.75\text{ pt}$, viền ngang giữa các dòng nét mảnh $0.5\text{ pt}$, hạn chế kẻ viền dọc (chuẩn IEEE/APA).

### 2.5. Định dạng Hình ảnh, Đồ thị & Sơ đồ (Figures)
* **Vị trí hình ảnh:** Căn giữa trang (Center), định dạng `In Line with Text` (tránh bị trôi hình khi chỉnh văn bản).
* **Tên hình (Caption):** Đặt **ở DƯỚI** hình, cỡ chữ $12\text{ pt}$, căn giữa. In đậm số hiệu, in nghiêng nội dung mô tả.
  *(Ví dụ: `Hình 3.1: Minh họa cơ chế lọc sai số thô bằng Khoảng tứ phân vị (IQR)...`).*
* **Kích thước ảnh:** Chiều rộng tối đa $15.5\text{ cm}$ (đảm bảo nằm trọn vẹn trong vùng in của khổ A4 đã trừ lề).

### 2.6. Định dạng Công thức Toán học chuẩn Word Equation (`Alt + =` / OMML)
* **Bắt buộc dùng đối tượng Word Equation tự nhiên:** Toàn bộ công thức toán học đứng riêng dòng (display math) phải được tạo dưới dạng đối tượng toán học gốc của Microsoft Word (**Office Math Markup Language - OMML**, tương đương khi người dùng nhấn tổ hợp phím **`Alt + =`** trong Word). Tuyệt đối không dùng văn bản chữ nghiêng thông thường để gõ công thức.
* **Cấu trúc hiển thị:**
  * Có đầy đủ ký hiệu phân số toán học thực thụ ($\frac{a}{b}$), dấu căn bậc hai ($\sqrt{\dots}$), phép tính n-ary tích phân/tổng ($\sum$), chỉ số trên/dưới ($x_i, R^2$), ma trận khối ($\mathbf{X}^T\mathbf{X}$).
  * Căn giữa trang, font Cambria Math hoặc Times New Roman chuẩn toán học.
  * Đánh số thứ tự công thức sát lề phải: `(1.1)`, `(1.2)`,... để thuận tiện trích dẫn trong văn bản.
* **Giải thích ký hiệu:** Đặt ngay bên dưới công thức, bắt đầu bằng *"Trong đó:"* (không thụt lề), các biến được liệt kê rõ ràng kèm đơn vị đo chuẩn SI.
* **Kỹ thuật lập trình chèn OMML trong Python (python-docx):**
  ```python
  from docx.oxml import parse_xml

  # Tạo đoạn văn căn giữa và chèn khối thẻ m:oMathPara / m:oMath
  p = doc.add_paragraph()
  p.alignment = WD_ALIGN_PARAGRAPH.CENTER
  wrapper_xml = (
      f'<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
      f'<m:oMath>{omml_xml_content}</m:oMath>'
      f'</m:oMathPara>'
  )
  p._p.append(parse_xml(wrapper_xml))
  ```

### 2.7. Header, Footer và Đánh số trang
* **Đầu trang (Header):** Ghi tên chương hoặc tên học phần viết hoa nhỏ, căn phải, có đường kẻ chỉ mờ bên dưới, cỡ $10\text{ pt}$.
* **Chân trang (Footer):** Đánh số trang căn giữa.
* **Quy tắc số trang:**
  * Trang bìa: Không đánh số trang.
  * Phần mở đầu (Lời cảm ơn, Mục lục, Danh mục hình/bảng): Đánh số La Mã thường (`i, ii, iii,...`).
  * Toàn bộ nội dung từ Chương 1 đến hết Chương 5: Đánh số tự nhiên (`1, 2, 3,...`).

---

## 3. NGUYÊN TẮC HỌC THUẬT VÀ NỘI DUNG DỰ ÁN

1. **Ngôn ngữ:** Thuần Việt học thuật, trang trọng, chính xác. Loại bỏ các từ tiếng Anh kèm theo trong ngoặc đơn nếu không phải là tên riêng chuẩn quốc tế (như ISO/GUM, ESP32, GPIO, IQR, ToF).
2. **Phương pháp lọc ngoại lai:** Chọn duy nhất **Khoảng tứ phân vị (IQR - Tukey's Fences)** làm giải thuật lọc số chuẩn hóa, không dùng lẫn lộn $3\sigma$.
3. **Mô hình toán học:** Công nhận trực tiếp các công thức hồi quy ma trận $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$, công thức Laplace, công thức Student $t_{0.975}$ mà không cần diễn giải chứng minh vi tích phân dài dòng.
4. **Quy chuẩn Nhiệt độ Môi trường Mặc định (Default Temp):**
   - Toàn bộ các tập dữ liệu mặc định (`FSDT`, `BSDT`, `FRDT`, `100lanforward_smooth_defttemp_...`) được quy ước và chuẩn hóa tại mức nhiệt độ phòng mặc định **27.0°C** ($v(27.0^\circ\text{C}) = 347.662\text{ m/s}$, $S_{t,\text{theory}} \approx 57.5271\text{ }\mu\text{s/cm}$).
   - Kịch bản phòng điều hòa (`FSAT`) được thiết lập tại **20.0°C** ($v(20.0^\circ\text{C}) = 343.420\text{ m/s}$), tạo độ chênh lệch thực nghiệm $\Delta T = 7.0^\circ\text{C}$ phục vụ đánh giá thuật toán bù nhiệt Laplace.
   - Mọi hàm khởi tạo MicroPython (`rcwl1601.py`, `main.py`) mặc định `temperature_c = 27.0` và `default_temp_c = 27.0`.

5. **Quy tắc An toàn Git:**
   - **TUYỆT ĐỐI KHÔNG tự ý chạy lệnh `git commit` hoặc `git push`** khi chưa có sự đồng ý trực tiếp từ người dùng.
   - Luôn đưa ra gợi ý **Suggested Commit Message** ngắn gọn, chuyên nghiệp bằng tiếng Việt ở cuối mỗi câu trả lời.
