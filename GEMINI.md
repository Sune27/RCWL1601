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

### 1.5. Quy tắc Trình bày Chi tiết trên Đồ thị (Bắt buộc)
* **Ký hiệu điểm dữ liệu (Markers):** Luôn sử dụng các hình học phân biệt rõ ràng cho các chuỗi dữ liệu trên đường vẽ (Ví dụ: hình tròn `marker='o'`, hình vuông `marker='s'`, hình tam giác `marker='^'`).
* **Tuyệt đối không vẽ mũi tên chỉ điểm:** Không sử dụng các mũi tên chú thích (`annotate` với `arrowprops`) chĩa trực tiếp vào các điểm dữ liệu trên đồ thị để giữ khung hình thoáng, chuyên nghiệp và tránh rối mắt.
* **Không tô bóng/ký hiệu các vùng phân dải:** Không sử dụng `axvspan` hay các mảng màu phân vùng (vùng dốc, vùng bão hòa, vùng chuyển tiếp...) đè lên dữ liệu đo lường.
* **Thuật ngữ đo lường chuẩn xác:** Tuyệt đối không sử dụng từ ngữ "điểm khuỷu tay" (elbow point) trên đồ thị và báo cáo. Thay vào đó sử dụng các thuật ngữ đo lường chính quy: "Điểm dừng bão hòa sai số", "Ngưỡng tốc độ biến thiên $|d\varepsilon/dk| \approx 0$", hoặc ghi trực tiếp mốc "N = 50".

---

## 2. QUY CHUẨN ĐỊNH DẠNG VÀ THAO TÁC VỚI TÀI LIỆU WORD (.DOCX) DÀNH CHO BÁO CÁO

### 2.0. QUY TẮC KÍCH HOẠT TIỀN TỐ "DOCX" VÀ AN TOÀN TIẾN TRÌNH WORD
> [!IMPORTANT]
> **1. Quy tắc Tiền tố `docx` ở đầu câu lệnh:**
> - Antigravity CHỈ ĐƯỢC PHÉP chỉnh sửa tệp Word (`.docx`) hoặc can thiệp/chạy các kịch bản xuất bản Word (`xuat_word_chuan.py`) KHI VÀ CHỈ KHI câu lệnh (prompt) của người dùng **có chữ `docx` ở đầu** (ví dụ: `"docx hãy gộp hai bản báo cáo vào 1"`, `"docx cập nhật mục 2.4 vào word"`).
> - Nếu câu lệnh KHÔNG có tiền tố `docx` ở đầu: Tuyệt đối không chỉnh sửa mã nguồn xuất Word hay ghi đè tệp Word.
>
> **2. Quy tắc Kiểm tra An toàn Tiến trình Word đang mở:**
> - Trước khi thực hiện bất kỳ thao tác nào liên quan tới file Word, Antigravity phải kiểm tra xem người dùng có đang mở ứng dụng Word hay không (kiểm tra tiến trình `WINWORD` hoặc file khóa `~$...docx`).
> - **Nếu Word đang mở:** DỪNG LẠI NGAY LẬP TỨC và đưa ra thông báo: *"Vui lòng lưu và tắt ứng dụng Word để Antigravity có thể cập nhật tài liệu!"*. Tuyệt đối không tự ý ép ghi đè hoặc tự động sinh tệp phụ khi chưa có yêu cầu.

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

1. **Ngôn ngữ:** Thuần Việt học thuật, trang trọng, chính xác. Loại bỏ các từ tiếng Anh kèm theo trong ngoặc đơn nếu không phải là tên riêng chuẩn quốc tế (như ISO/GUM, ESP32, GPIO, IQR, ToF). Tuyệt đối không dịch thô cụm từ 'Uncertainty Budget' thành 'ngân sách độ không đảm bảo đo' (do từ 'ngân sách' chỉ dùng cho tài chính/tiền tệ); bắt buộc dùng chuẩn mực: **'Bảng tổng hợp độ không đảm bảo đo'** (cho bảng biểu số liệu) hoặc **'Phân tích / Đánh giá tổng hợp độ không đảm bảo đo'** (cho tiêu đề và câu văn).
2. **Phương pháp lọc ngoại lai:** Chọn duy nhất **Khoảng tứ phân vị (IQR - Tukey's Fences)** làm giải thuật lọc số chuẩn hóa, không dùng lẫn lộn $3\sigma$.
3. **Mô hình toán học:** Công nhận trực tiếp các công thức hồi quy ma trận $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$, công thức Laplace, công thức Student $t_{0.975}$ mà không cần diễn giải chứng minh vi tích phân dài dòng.
4. **Quy chuẩn Nhiệt độ Môi trường Mặc định (Default Temp):**
   - Toàn bộ các tập dữ liệu mặc định (`FSDT`, `BSDT`, `FRDT`, `100lanforward_smooth_defttemp_...`) được quy ước và chuẩn hóa tại mức nhiệt độ phòng mặc định **27.0°C** ($v(27.0^\circ\text{C}) = 347.662\text{ m/s}$, $S_{t,\text{theory}} \approx 57.5271\text{ }\mu\text{s/cm}$).
   - Kịch bản phòng điều hòa (`FSAT`) được thiết lập tại **20.0°C** ($v(20.0^\circ\text{C}) = 343.420\text{ m/s}$), tạo độ chênh lệch thực nghiệm $\Delta T = 7.0^\circ\text{C}$ phục vụ đánh giá thuật toán bù nhiệt Laplace.
   - Mọi hàm khởi tạo MicroPython (`rcwl1601.py`, `main.py`) mặc định `temperature_c = 27.0` và `default_temp_c = 27.0`.

5. **Quy tắc An toàn Git:**
   - **TUYỆT ĐỐI KHÔNG tự ý chạy lệnh `git commit` hoặc `git push`** khi chưa có sự đồng ý trực tiếp từ người dùng.
   - Luôn đưa ra gợi ý **Suggested Commit Message** ngắn gọn, chuyên nghiệp bằng tiếng Việt ở cuối mỗi câu trả lời.

6. **Quy chuẩn Mô hình Bố trí Thực nghiệm:**
   - **Tuyệt đối không dùng cụm từ 'gá đặt cơ khí'** (do mang tính gia công cơ khí nặng không phù hợp bối cảnh thí nghiệm điện tử). Sử dụng các cụm từ chuẩn kỹ thuật đo lường tự nhiên: **'Bố trí mô hình và định vị thiết bị đo'** hoặc **'Phương thức bố trí và cố định thiết bị'**.
   - **Cấu hình phần cứng thực tế:** Cảm biến RCWL-1601 được cắm cố định trên bo mạch thử nghiệm (breadboard), đặt sát mép bàn cao khoảng 85 cm cùng vi điều khiển ESP32 và máy tính thu thập dữ liệu.
   - **Vật thể đo chuẩn:** Viên gạch kích thước $40 \times 40\text{ cm}$ có hai mặt với đặc tính đối lập: mặt trước phẳng nhẵn và mặt sau gồ ghề nhấp nhô. Viên gạch được dựng đứng sát mép của một chiếc bàn thứ hai cao 85 cm, luôn được căn chỉnh vuông góc ($90^\circ$) với mặt bàn và đối diện trực diện với cảm biến.
   - **Xác định cự ly chuẩn:** Dùng thước đo milimét / thước dây tiêu chuẩn căng giữa hai mép bàn để xác lập chính xác từng mốc cự ly rồi kích hoạt cảm biến từ máy tính.

7. **Quy chuẩn Tên gọi Các trường hợp Đo lường:**
   - Tuyệt đối không dùng cụm từ thiếu tự nhiên **'ma trận kịch bản thực nghiệm'**.
   - Bắt buộc sử dụng cụm từ thuần kỹ thuật đo lường: **'Các trường hợp đo và điều kiện thực nghiệm'** (cho tiêu đề Mục 2.3) và **'Bảng tổng hợp các trường hợp đo và thông số thực nghiệm'** (cho Bảng 2.2). Các cột bảng gọi là: *Trường hợp 1 (FSDT)*, *Trường hợp 2 (BSDT)*, *Trường hợp 3 (FRDT)*, *Trường hợp 4 (FSAT)*.



8. **Quy tắc Thao tác Tệp Word (Bắt buộc Tiền tố `docx` & Dừng khi Word mở):**

   - Chỉ được phép chỉnh sửa mã nguồn xuất Word hoặc can thiệp tệp Word khi câu lệnh của người dùng bắt đầu bằng chữ `docx`.

   - Nếu phát hiện ứng dụng Word đang mở, lập tức dừng lại và thông báo nhắc người dùng tắt Word trước khi tiếp tục.

9. **Quy chuẩn Đồ thị Độ không đảm bảo đo (ISO/GUM):**
   - Tách thành **2 đồ thị riêng biệt** để đảm bảo tỷ lệ quan sát trực quan (do thành phần $u_A$ rất nhỏ từ $0.008\text{ mm}$ so với $U_{95\%}$ lên tới $5.57\text{ mm}$):
     * Đồ thị 1 ([Hình 3.9](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_9_do_khong_dam_bao_do_loai_a_b.png)): Biểu đồ phân rã độ không đảm bảo đo Loại A ($u_A$) và Loại B ($u_B$) theo khoảng cách chuẩn.
     * Đồ thị 2 ([Hình 3.10](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_10_do_khong_dam_bao_do_tong_hop_mo_rong.png)): Biểu đồ độ không đảm bảo đo chuẩn tổng hợp ($u_c$) và độ không đảm bảo đo mở rộng ($U_{95\%}$, $k=2$) theo ISO/GUM.
   - **Tuyệt đối không vẽ mũi tên:** Không chèn ký hiệu mũi tên (`↑`, `↓`) vào các hộp văn bản ghi chú và không dùng marker tam giác nhọn (dễ nhầm với mũi tên).

10. **Quy chuẩn Bảng Đối sánh Datasheet vs Thực nghiệm (Bảng 3.7):**
   - Chỉ đối chiếu các **chỉ tiêu kỹ thuật đo lường thực tế** mà nhà sản xuất có công bố định mức (Dải đo, Vùng chết, Độ chính xác, Độ phân giải ToF, Khả năng bù nhiệt độ).
   - **Xóa bỏ các thông số điện nguồn** không liên quan và không đo kiểm: Điện áp hoạt động ($V_{\text{CC}}$), Dòng điện tiêu thụ ($I$).
   - **Xóa bỏ toàn bộ các hàng ghi "Không công bố":** Tuyệt đối không đưa vào bảng các dòng như $R^2$, Độ phi tuyến, Độ lệch chuẩn $s$, Độ trễ $\gamma_H$, Tầm đo mặt xốp khi Datasheet không cung cấp thông số đối chứng.

11. **Quy chuẩn Cố định Nội dung Lời nói đầu (Preface):**
   - Nội dung phần **LỜI NÓI ĐẦU** đã được tinh chỉnh cô đọng và cố định chuẩn mực như sau (tuyệt đối không tự ý thêm bớt hay ghi đè lại văn phong cũ):
     * **Đoạn 1:** Khái quát vai trò đo cự ly không tiếp xúc trong công nghiệp (AGV, băng tải logistics, bồn chứa ăn mòn, vận hành liên tục 24/7).
     * **Đoạn 2:** Đánh giá ưu thế của cảm biến siêu âm (chi phí cực thấp, bền cơ học, không phụ thuộc màu sắc, an toàn).
     * **Đoạn 3:** Giới thiệu module RCWL-1601 tương thích logic 3.3V ESP32 và ảnh hưởng nhiệt độ môi trường gây trôi cự ly tại Việt Nam.
     * **Đoạn 4:** Tuyên bố đề tài học phần.
     * **3 Mục tiêu cốt lõi:**
       1. Khảo sát toàn diện đặc tính tĩnh và động học của cảm biến RCWL-1601 trên giàn thực nghiệm chuẩn hóa: xác định dải đo, độ chụm, độ chính xác, đánh giá độ không đảm bảo đo mở rộng.
       2. Khảo sát các hiện tượng vật lý chuyên sâu ảnh hưởng đến phép đo siêu âm: độ trễ (Hysteresis), hiện tượng tán xạ trên bề mặt gồ ghề, và hiệu quả bù trôi vận tốc sóng âm Laplace theo nhiệt độ.
       3. Xây dựng chuỗi lọc số (Khoảng tứ phân vị IQR) và thiết kế hệ thống: 'Giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ trên ESP32'.
     * (Không liệt kê 5 chương ở cuối Lời nói đầu nhằm giữ bố cục súc tích, trang trọng).

12. **Quy chuẩn Bảng Quy ước Dữ liệu (Bảng 0.1) và Cấu trúc Thư mục:**
   - **Tiêu đề mục quy ước (Heading 1):** Bắt buộc dùng `BẢNG QUY ƯỚC KÝ HIỆU VÀ DỮ LIỆU THỰC NGHIỆM` (không thêm chữ "CẤU TRÚC").
   - **Tiêu đề bảng:** Bắt buộc dùng `Bảng 0.1: Bảng quy ước tên 4 tập dữ liệu thực nghiệm chuẩn hóa của đề tài`.
   - **Cấu trúc Bảng 0.1:** Bảng có đúng **4 cột** chuẩn hóa ký hiệu trực quan (loại bỏ cự ly chi tiết và mục đích dài dòng):
     * Cột 1: `Ký hiệu mã` (`FSDT`, `BSDT`, `FRDT`, `FSAT`)
     * Cột 2: `Chiều dịch chuyển` (`Tiến (Forward)`, `Lùi (Backward)`)
     * Cột 3: `Bề mặt phản xạ` (`Phẳng nhẵn bóng (Smooth)`, `Nhám gồ ghề (Rough)`)
     * Cột 4: `Nhiệt độ môi trường` (`27.0 °C`, `20.0 °C`)
   - **Mô tả cấu trúc thư mục dữ liệu:** Tiêu đề `Cấu trúc tổ chức dữ liệu dự án:` gồm 3 gạch đầu dòng ngắn gọn:
     * `• Thư mục 'result/': Lưu trữ toàn bộ các tệp dữ liệu thô ban đầu. Mỗi tệp bao gồm 50 dòng với 3 cột thông tin chuẩn hóa: thời gian bay t (μs), khoảng cách đo được distance_cm và nhiệt độ temperature_c.`
     * `• Thư mục 'du_lieu_tong_hop/': Lưu trữ các tệp dữ liệu tổng hợp và tính toán. Toàn bộ các phân tích định lượng, khớp hàm và đánh giá độ không đảm bảo đo ở Chương 3 đều được thực thi trực tiếp từ thư mục này.`
     * `• Thư mục ‘graph/’: Lưu trữ figure các đồ thị được sử dụng trong bài báo cáo này.`

13. **Quy chuẩn Nội dung Mục 1.1 và 1.2 (Chương 1):**
   - **Mục 1.1: NGUYÊN LÝ ĐO KHOẢNG CÁCH THỜI GIAN BAY VÀ MÔ HÌNH BÙ NHIỆT ĐỘ MÔI TRƯỜNG**
     * 1.1.1: Phương trình lan truyền sóng siêu âm thời gian bay $d = \frac{v \cdot t}{2}$ (1.1). Đoạn giải thích ngắn gọn, súc tích (bỏ các diễn giải lặp lại).
     * 1.1.2: Tiêu đề chuẩn: `1.1.2. Sự ảnh hưởng của nhiệt độ tới vận tốc âm thanh`. Bao gồm phương trình Laplace $v = \sqrt{\frac{\gamma R T_K}{M}}$ (1.2) và khai triển Taylor $v(T) = 331.3 + 0.606 \cdot T$ (1.3). Bỏ đoạn văn dài phân tích sai số trôi cự ly lý thuyết.
     * 1.1.3: Tiêu đề chuẩn: `1.1.3. Sự suy hao năng lượng sóng âm theo cự ly`. Gồm đúng 2 gạch đầu dòng cô đọng: (1) Phân kỳ hình học $I(d) \sim 1/d^2$; (2) Ma sát với không khí gây suy hao năng lượng.
   - **Mục 1.2: ĐẶC TÍNH VÀ THÔNG SỐ CỦA MODULE RCWL-1601**
     * Tiêu đề mục: `1.2. ĐẶC TÍNH VÀ THÔNG SỐ CỦA MODULE RCWL-1601` (không dùng "ĐẶC TÍNH HOẠT ĐỘNG").
     * 1.2.1: Giản đồ xung kích hoạt và phản hồi ToF: Trình bày 4 bước ngắn gọn (TRIG $\ge 10\mu\text{s}$, Phát 8 xung 40 kHz, Nhận sóng phản xạ ngắt ECHO, Đo độ rộng ToF).
     * 1.2.2: Tiêu đề `1.2.2. Bảng thông số kỹ thuật của RCWL-1601` và `Bảng 1.1: Bảng thông số kỹ thuật của module cảm biến siêu âm RCWL-1601`. Bảng gồm 9 thông số kỹ thuật chuẩn hóa (Dải đo công bố $2 - 400\text{ cm}$, độ phân giải $1\text{ mm}$, góc mở $\approx 15^\circ$, v.v.).

14. **Quy chuẩn Nội dung Mục 1.3 (Chương 1):**
   - **Mục 1.3: CƠ SỞ LÝ THUYẾT XỬ LÝ SỐ LIỆU ĐO LƯỜNG VÀ ĐỘ KHÔNG ĐẢM BẢO ĐO** (loại bỏ `(ISO/GUM)` khỏi tiêu đề).
   - **1.3.1. Các đại lượng thống kê mô tả mẫu đo:**
     * Giá trị trung bình mẫu $\bar{x} = \frac{1}{N}\sum_{i=1}^N x_i$ (1.4).
     * Độ lệch chuẩn mẫu thực nghiệm $s = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (x_i - \bar{x})^2}$ (1.5).
     * Giá trị trung vị mẫu (Median): $\text{Med} = x_{\left(\frac{N+1}{2}\right)}$ với $N$ lẻ, bền vững trước ngoại lai.
   - **1.3.2. Lọc sai số thô bằng Khoảng tứ phân vị (IQR):**
     * Tiêu đề: `1.3.2. Lọc sai số thô bằng Khoảng tứ phân vị (IQR)` (loại bỏ cụm "Tiêu chuẩn phát hiện và").
     * Công thức: $\text{IQR} = Q_3 - Q_1$ (1.6); $\text{LF} = Q_1 - 1.5 \cdot \text{IQR}, \text{UF} = Q_3 + 1.5 \cdot \text{IQR}$ (1.7); Điều kiện chấp nhận: $x_i \in [\text{LF}, \text{UF}]$ (1.8).
     * Bỏ hoàn toàn đoạn văn diễn giải masking effect dài dòng phía sau công thức.
   - **1.3.3. Hệ thống công thức đánh giá các Đặc tính tĩnh của cảm biến:**
     * Mục 1: `1. Độ chụm và Sai số chuẩn trung bình:` Độ lệch chuẩn $s$ và sai số chuẩn $\text{SE} = s / \sqrt{N}$.
     * Mục 2: `2. Sai số đo lường:` Sai số tuyệt đối $\Delta d = \bar{d} - d_{\text{true}}$, sai số tương đối $\delta\%$.
     * Mục 3: `3. Độ tuyến tính và Sai số phi tuyến (Linearity):` Ma trận hồi quy $\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ (1.9).
     * Mục 5: `5. Độ trễ (Hysteresis):` $\Delta H_k = |\bar{d}_{\text{forward}, k} - \bar{d}_{\text{backward}, k}|$, sai số trễ toàn dải $\gamma_H\%$.
     * **Loại bỏ hoàn toàn:** Mục 4 (Độ nhạy Sensitivity) và Mục 6 (Độ phân giải Resolution) cùng các diễn giải $R^2$ thừa thãi.
   - **1.3.4. Đánh giá Độ không đảm bảo đo:**
     * Tiêu đề: `1.3.4. Đánh giá Độ không đảm bảo đo` (loại bỏ đoạn văn dẫn nhập ISO/IEC Guide 98-3).
     * 4 gạch đầu dòng cô đọng: Loại A ($u_A = s / \sqrt{N}$); Loại B ($u_B = a / \sqrt{3}$); Tổng hợp ($u_c = \sqrt{u_A^2 + \sum u_{B,j}^2}$); Mở rộng ($U_{95\%} = 2 \cdot u_c$ với $k_p=2$).
     * Biểu diễn kết quả: $Y = \bar{d} \pm U_{95\%}$ (1.10).

15. **Quy chuẩn Nội dung Mục 2.1 và 2.2 (Chương 2):**
   - **Tiêu đề Chương 2:** `CHƯƠNG 2: THIẾT KẾ VÀ BỐ TRÍ THỰC NGHIỆM` (loại bỏ từ "HỆ THỐNG").
   - **Mục 2.1: MỤC TIÊU THỰC NGHIỆM** (loại bỏ cụm "VÀ PHƯƠNG PHÁP LUẬN THỰC NGHIỆM").
     * **2.1.1. Mục tiêu thực nghiệm:** Thu gọn thành 1 đoạn văn duy nhất, không dùng danh sách đánh số:
       *"Nghiên cứu thực nghiệm được thiết kế nhằm mục đích kiểm chứng các đặc tính đo lường của module cảm biến siêu âm RCWL-1601: Khảo sát dải đo thực tế, định lượng độ chụm và độ chính xác, đánh giá độ tuyến tính, đánh giá ảnh hưởng của nhiệt độ môi trường, đánh giá ảnh hưởng của bề mặt phản xạ, đánh giá độ trễ"*
     * **Loại bỏ hoàn toàn Mục 2.1.2** (Phương pháp luận thực nghiệm và sơ đồ khối ToF ASCII).
   - **Mục 2.2: THIẾT KẾ PHẦN CỨNG VÀ KHÔNG GIAN THỰC NGHIỆM**
     * **2.2.1. Thiết kế phần cứng và sơ đồ kết nối điện:**
       - Đoạn văn mở đầu ngắn gọn: *"Module cảm biến siêu âm RCWL-1601 được kết nối trực tiếp với vi điều khiển ESP32. Các đường tín hiệu TRIG và ECHO giao tiếp trực tiếp với các chân GPIO của ESP32 ở mức logic 3.3 V."* (loại bỏ câu dài về vi mạch RCWL-9610 và dải điện áp).
       - Tiêu đề bảng: `Bảng 2.1: Sơ đồ kết nối phần cứng giữa cảm biến RCWL-1601 và vi điều khiển ESP32`.
       - Bảng gồm 3 cột chuẩn: `Chân RCWL-1601`, `Chân ESP32`, `Chức năng kỹ thuật` (4 hàng: `VCC` - `3V3`, `GND` - `GND`, `TRIG` - `GPIO 5`, `ECHO` - `GPIO 18`).
     * **2.2.2. Thiết kế không gian thực nghiệm:**
       - Tiêu đề ngắn gọn: `2.2.2. Thiết kế không gian thực nghiệm` (loại bỏ cụm "và kiểm soát điều kiện môi trường thực nghiệm").
       - Loại bỏ câu văn dẫn nhập hình nón sóng âm. Gồm đúng 2 gạch đầu dòng:
         1. `• Chiều cao bàn đo 85 cm: Hệ thống cảm biến và vật đo được đặt trên hai bàn thí nghiệm có độ cao 85.0 cm so với mặt sàn phòng đo.`
         2. `• Phòng đo: Thực nghiệm được bố trí dọc theo hành lang kín gió dài 10 m, chiều rộng 2.8 m. Cảm biến đặt cách tường bên ít nhất 1.4 m. Trong suốt quá trình đo, hệ thống cửa được đóng kín tránh gió lùa và biến thiên nhiệt độ đột ngột.`
     * **2.2.3. Bố trí mô hình và định vị thiết bị đo:**
       - Đoạn mở đầu ngắn gọn: *"Để đảm bảo phép đo đạt độ chính xác cao, mô hình thực nghiệm được bố trí:"*
       - Gồm 3 mục đánh số:
         1. `1. Cố định cảm biến: RCWL-1601 được cắm cố định vững chắc trên breadboard, sát mép bàn, hướng hai mắt phát - thu trực diện ra ngoài.`
         2. `2. Vật thể phản xạ mục tiêu: Vật thể đo chuẩn là một viên gạch kích thước 40 cm × 40 cm có mặt trước phẳng nhẵn và mặt sau gồ ghề. Viên gạch được dựng thẳng đứng sát mép của chiếc bàn có cùng chiều cao 85 cm. Khi tiến hành đo, viên gạch luôn được căn chỉnh vuông góc với mặt bàn và đối diện với trục phát của cảm biến.`
         3. `3. Căn chỉnh cự ly bằng thước đo tiêu chuẩn: Khoảng cách chuẩn d_true được xác định thủ công bằng thước dây. `
