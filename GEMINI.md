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

16. **Quy chuẩn Nội dung Mục 2.3 và 2.4 (Chương 2):**
   - **Mục 2.3: CÁC TRƯỜNG HỢP ĐO VÀ ĐIỀU KIỆN THỰC NGHIỆM**
     * Đoạn mở đầu: *"Để đánh giá đầy đủ, độc lập và toàn diện các đặc tính kỹ thuật, nghiên cứu thiết lập 4 trường hợp đo chuyên biệt với các điều kiện môi trường tương ứng:"*
     * Tiêu đề bảng: `Bảng 2.2: Bảng tổng hợp các trường hợp đo và thông số thực nghiệm`
     * Cấu trúc Bảng 2.2: Gồm **5 cột** (`Tham số`, `FSDT`, `BSDT`, `FRDT`, `FSAT`) và **6 hàng thông số**:
       1. `Bề mặt phản xạ` (`Mặt nhẵn`, `Mặt nhẵn`, `Mặt gồ ghề`, `Mặt nhẵn`)
       2. `Chiều di chuyển` (`Tiến (1 – 600 cm)`, `Lùi (300 – 10 cm)`, `Tiến (10 – 375 cm)`, `Tiến (10 – 300 cm)`)
       3. `Số mốc cự ly` (`35`, `19`, `23`, `19`)
       4. `Nhiệt độ môi trường` (`27.0 °C`, `27.0 °C`, `27.0 °C`, `20.0 °C`)
       5. `Tổng số mẫu` (`1.750`, `950`, `1.150`, `950`)
       6. `Mục đích` (`Khảo sát toàn dải, độ chụm, độ chính xác, độ nhạy`, `Khảo sát độ trễ`, `Khảo sát tán xạ bề mặt`, `Khảo sát trôi nhiệt độ`)
       *(Loại bỏ hàng "Số lần đo lặp N" khỏi Bảng 2.2 để tránh trùng lặp với Mục 2.4).*
   - **Mục 2.4: XÁC ĐỊNH CỠ MẪU TỐI ƯU**
     * **2.4.1. Tối ưu cỡ mẫu:**
       - Tiêu đề: `2.4.1. Tối ưu cỡ mẫu` (rút ngắn từ *"Bản chất bài toán tối ưu cỡ mẫu trong đo lường siêu âm"*).
       - Khái niệm khoảng tin cậy: $d \in [\bar{d} - \varepsilon, \, \bar{d} + \varepsilon]$ (tương đương $d = \bar{d} \pm \varepsilon$).
       - Mô hình Student: $\varepsilon(N) = \frac{t_{0.975, \, N-1} \cdot s}{\sqrt{N}}$ (2.1).
       - Diễn giải ngắn gọn về $s$, $1/\sqrt{N}$ và bài toán tối ưu sai số $\varepsilon < 0.5\text{ mm}$ cùng ngưỡng dừng bão hòa đạo hàm $|d\varepsilon/dN| \approx 0$.
     * **2.4.2. Phân tích dữ liệu thực nghiệm:**
       - Tiêu đề: `2.4.2. Phân tích dữ liệu thực nghiệm`.
       - Đoạn văn dẫn chứng chuỗi đo 100 lần tại 3 mốc (50 cm, 100 cm, 150 cm) tại `du_lieu_tong_hop/mau_100.csv` và thư mục `du_lieu_tong_hop/chuong_2`.
       - **Hình 2.1:** Caption rút gọn: `Hình 2.1: Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu.` Đoạn nhận xét cô đọng về xu hướng giảm nhanh ở $k < 30$ và hội tụ ổn định từ $k \ge 40 - 50$.
       - **Hình 2.2:** Caption: `Hình 2.2: Tốc độ biến thiên sai số |dε_95%/dk| theo cỡ mẫu k.` Đoạn nhận xét chỉ rõ đạo hàm suy giảm mạnh khi $k < 20$ và bão hòa đi ngang khi $k \to 50$.
       - **Loại bỏ Bảng 2.3:** Bỏ hoàn toàn Bảng 2.3 và đoạn đánh giá bảng để văn bản tập trung trực quan vào 2 đồ thị.
       - **Kết luận cỡ mẫu:** Đúc kết thành 1 câu duy nhất: *"Kết luận: Dựa trên các phân tích và đánh giá từ hai đồ thị và bảng số liệu nêu trên, nhóm nghiên cứu đưa ra quyết định lựa chọn cỡ mẫu N = 50 cho toàn bộ các phép đo thực nghiệm."* (loại bỏ hoàn toàn danh sách 3 gạch đầu dòng dài dòng).

17. **Quy chuẩn Nội dung Mục 3.1 và 3.2 (Chương 3):**
   - **Đoạn dẫn nhập Chương 3:** Rút gọn thành 1 câu duy nhất: *"Chương 3 trình bày việc xử lý số liệu và phân tích kết quả đo từ dữ liệu thực nghiệm: "*
   - **Mục 3.1: Tiền xử lý dữ liệu và Đánh giá hiệu quả lọc sai số thô bằng Khoảng tứ phân vị (IQR)**
     * **3.1.1. Khung tiền xử lý và cơ chế hình thành ngoại lai trong phép đo siêu âm:**
       - Trình bày trực tiếp quy tắc chuyển mẫu ngoại lai ngoài `[LF, UF]` thành `NaN`.
       - Loại bỏ 2 gạch đầu dòng giải thích nguyên nhân dài dòng (xung timeout, tán xạ nhiều đường).
     * **3.1.2. Tổng hợp kết quả lọc:**
       - Tiêu đề: `3.1.2. Tổng hợp kết quả lọc` (loại bỏ cụm *"ngoại lai trên toàn bộ 4 tập dữ liệu thực nghiệm"*).
       - Dẫn chứng bảng thống kê `du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv` và 4 file clean.
       - Tiêu đề bảng: `Bảng 3.1: Tổng hợp kết quả xử lý sai số thô bằng Khoảng tứ phân vị (IQR) trên toàn bộ 4.800 mẫu đo.`
       - Cấu trúc Bảng 3.1: Gồm đúng **8 cột** (loại bỏ cột *"Số mốc cự ly"*): `Tệp dữ liệu`, `Điều kiện đo`, `Tổng mẫu`, `Mốc có ngoại lai`, `Mẫu ngoại lai`, `Tỷ lệ (%)`, `Mẫu hợp lệ`, `Tỷ lệ hợp lệ (%)`.
       - Đoạn nhận xét sau Bảng 3.1 gom thành một đoạn văn duy nhất, không dùng bullet points.
     * **3.1.3. Đánh giá hiệu quả sau khi lọc:**
       - Tiêu đề ngắn gọn: `3.1.3. Đánh giá hiệu quả sau khi lọc`.
       - **Hình 3.1:** `Hình 3.1: Độ lệch chuẩn trước và sau khi lọc IQR.`
       - Nhận xét đồ thị: Phân tích đường trước lọc (tăng mạnh ở 580 cm và 600 cm do timeout) và đường sau lọc (ổn định 0.09 - 4.0 mm).
       - **Bảng 3.2:** `Bảng 3.2: Đối chiếu độ lệch chuẩn trước và sau khi lọc IQR tại các mốc tiêu biểu.` Gồm 6 cột: `Khoảng cách chuẩn`, `Độ lệch chuẩn thô`, `Độ lệch chuẩn sạch`, `Tỷ lệ giảm s`, `Số mẫu ngoại lai`, `Nguyên nhân hiện tượng`.
   - **Mục 3.2: Khảo sát Dải đo thực tế**
     * Tiêu đề: `3.2. Khảo sát Dải đo thực tế` (loại bỏ cụm *"Vùng chết và Giới hạn bão hòa xa"*).
     * Đoạn mở đầu: Trình bày gọn gàng công thức sai số tuyệt đối $\Delta d = \bar{d} - d_{\text{chuẩn}}$ và sai số tương đối $\delta = \frac{\bar{d} - d_{\text{chuẩn}}}{d_{\text{chuẩn}}} \times 100\%$.
     * **Hình 3.2:** `Hình 3.2: Sai số tương đối theo khoảng cách chuẩn (Tập dữ liệu FSDT, giới hạn trục tung ±10%).`
     * **Phân chia 4 vùng làm việc:** Gói gọn trong một câu văn khái quát 4 phân vùng: Vùng chết (0 cm – 3 cm), Dải đo tuyến tính ổn định (5 cm – 400 cm), Dải đo xa vượt định mức (420 cm – 550 cm), Ngưỡng bão hòa xa (580 cm – 600 cm). **Loại bỏ toàn bộ các tiểu mục 3.2.1, 3.2.2, 3.2.3, 3.2.4** để tránh dàn trải.
     * **Kết luận dải đo:** *"Kết luận: Dải làm việc tin cậy và đạt chuẩn độ chính xác cao của cảm biến RCWL-1601 trong thực tế là từ 10 cm đến 550 cm."*
     * **Bảng 3.3:** `Bảng 3.3: Tổng hợp các vùng làm việc và đặc tính đo thực nghiệm trên toàn dải đo.`
       - Gồm **5 cột** chuẩn (loại bỏ cột *"Phân vùng làm việc"*): `Khoảng cách chuẩn`, `Giá trị trung bình`, `Sai số tuyệt đối`, `Sai số tương đối`, `Độ lệch chuẩn s`.

18. **Quy chuẩn Nội dung Mục 3.4 (Chương 3): Đánh giá Độ tuyến tính (Linearity):**
   - **Tiêu đề phân cấp:**
     * Heading 2: `3.4. Đánh giá Độ tuyến tính (Linearity)`
     * Heading 3: `3.4.1. Đánh giá Độ tuyến tính (Linearity)` (loại bỏ cụm *"Hồi quy đa thức và"*).
   - **Nội dung lý thuyết và thiết lập mô hình:**
     * Trình bày ngắn gọn định nghĩa độ tuyến tính, quy trình phân chia 70% Train (24 mốc) và 30% Test (10 mốc) trên toàn dải đo (1.0 cm đến 580.0 cm).
     * Thiết lập hệ phương trình 3 mô hình hồi quy: Bậc 1 ($y = a_1 x + b_1$), Bậc 2 ($y = a_2 x^2 + b_2 x + c_2$), Bậc 3 ($y = a_3 x^3 + b_3 x^2 + c_3 x + d_3$).
     * Dẫn chứng tệp kiểm thử: `"du_lieu_tong_hop\chuong_3\ [3.4].FSDT_split_70_30.csv"`.
     * Liệt kê chính xác phương trình hồi quy của 3 mô hình:
       - Bậc 1 (Tuyến tính): $\hat{y}_1 = 1.00273 \cdot x - 0.48427\text{ (cm)}$.
       - Bậc 2: $\hat{y}_2 = 3.56559 \cdot 10^{-6} \cdot x^2 + 1.00103 \cdot x - 0.37940\text{ (cm)}$.
       - Bậc 3: $\hat{y}_3 = -1.04345 \cdot 10^{-7} \cdot x^3 + 8.50580 \cdot 10^{-5} \cdot x^2 + 0.98551 \cdot x - 0.00036\text{ (cm)}$.
     * Ghi chú dẫn chứng tệp cơ sở dữ liệu: `Ghi chú: Toàn bộ các tổng ma trận chuẩn tắc phục vụ tính toán được lưu trữ trong tệp cơ sở dữ liệu “du_lieu_tong_hop/chuong_3/cac_tong_hoi_quy.csv”.`
     * **Loại bỏ hoàn toàn:** Phương trình ma trận OLS $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}$ (Phương trình 3.1) và các chuỗi số liệt kê tổng ma trận dài dòng.
   - **Bảng biểu và Đồ thị đối sánh:**
     * Giải thích ngắn gọn lý do phóng đại thang đo sai số lên mức milimét để phân biệt các mô hình.
     * **Bảng 3.4:** `Bảng 3.4: Đối sánh sai số dự đoán của 3 mô hình hồi quy trên 10 mốc kiểm thử độc lập.` Gồm đúng 8 cột: `Mốc Test x`, `y thực tế`, `ŷ Bậc 1`, `e Bậc 1`, `ŷ Bậc 2`, `e Bậc 2`, `ŷ Bậc 3`, `e Bậc 3`.
     * **Hình 3.3:** `Hình 3.3: So sánh sai số tuyệt đối tại các mốc kiểm thử của 3 mô hình hồi quy.`
     * **Hình 3.4:** `Hình 3.4: Biểu đồ miền tích lũy sai số tuyệt đối trên 10 mốc kiểm thử độc lập.`
   - **Đánh giá và Kết luận lựa chọn mô hình:**
     * Phân tích trực quan đồ thị Hình 3.3 và biểu đồ miền Hình 3.4: Mô hình Bậc 1 có đường tích lũy sai số gần như đi ngang phẳng lì từ 50 cm đến 450 cm (tổng sai số tích lũy toàn dải 41.07 mm), trong khi mô hình Bậc 3 leo dốc rất đứng tại dải giữa (tổng tích lũy 47.45 mm).
     * **Kết luận chọn mô hình:** *"Vậy thì ta thấy phương trình tuyến tính Bậc 1 y = 1.00273 · x - 0.48427 phù hợp nhất để làm phương trình đặc tính tĩnh chuẩn của hệ thống đo RCWL-1601."*
     * **Loại bỏ hoàn toàn:**
       - Công thức phi tuyến $\pm \frac{\Delta L_{\max}}{\text{FSO}} \times 100\%$ và tính toán Non-Linearity.
       - Bảng 3.5 (Bảng tổng hợp 4/5 tiêu chí khoa học quyết định lựa chọn mô hình).
       - Các phân tích lý thuyết dài dòng về hiện tượng quá khớp (Overfitting) và Runge.

19. **Quy chuẩn Nội dung Mục 3.6 (Chương 3): Phân tích ảnh hưởng của Bề mặt phản xạ:**
   - **Tiêu đề phân cấp:**
     * Heading 2: `3.6. Phân tích ảnh hưởng của Bề mặt phản xạ`
     * Heading 3: `3.6.1. Tác động của tán xạ bề mặt lên độ chụm (Precision) và độ chính xác (Accuracy)`
     * Heading 3: `3.6.2. Suy hao năng lượng và thu hẹp giới hạn đo do tán xạ`
   - **Mở đầu Mục 3.6:** Rút gọn thành 1 câu: *"Để khảo sát ảnh hưởng của bề mặt (Mục 1.1.3, Chương 1), thí nghiệm đối chứng được thực hiện ở cùng nhiệt độ phòng mặc định 27.0 °C (v = 347.662 m/s) trên hai mặt của cùng một viên gạch 40 cm × 40 cm (Mục 2.2 và Mục 2.3, Chương 2): Số liệu thống kê trên 22 mốc chung (10 cm – 350 cm) “du_lieu_tong_hop/chuong_3/ thong_ke_chuong_3.csv”.*
   - **Mục 3.6.1:**
     * Sử dụng mô hình đồ thị bia ngắm (Bullseye plot) để trực quan hóa Accuracy & Precision thay vì các đồ thị đường $s$ và $\text{SE}$ cũ.
     * **Hình 3.7a:** `Hình 3.7a: Bia ngắm Accuracy & Precision giữa tại các mốc 10 cm, 50 cm, 60 cm, 120 cm và 180 cm.`
     * **Hình 3.7b:** `Hình 3.7b: Accuracy & Precision giữa tại các mốc 220 cm, 240 cm, 260 cm, 280 cm và 350 cm.`
     * Nhận xét trực quan: Mặt phẳng nhẵn thể hiện độ chụm vượt trội (các điểm luôn gom chặt thành cụm tròn nhỏ sát tâm với độ lệch chuẩn $s$ nhỏ); mặt gồ ghề tán xạ làm $s$ tăng gấp từ 3 đến 26 lần và điểm $\bar{x}$ dạt lệch xa hồng tâm.
   - **Mục 3.6.2:**
     * **Bảng số liệu đối sánh độ chụm:** Gồm 3 cột: `Mốc cự ly (cm)`, `FSDT - std sạch (mm)`, `FRDT - std sạch (mm)` tại 7 mốc: 10 cm, 100 cm, 200 cm, 300 cm, 350 cm, 375 cm (FSDT 2.508 mm, FRDT 2140.734 mm), 380 cm (FSDT 5.531 mm, FRDT Mất tín hiệu).
     * Phân tích sụt giảm cự ly: Chớm mất xung tại 350 cm trên mặt gồ ghề, mất hoàn toàn xung tại phép đo 375 cm.
     * **Kết luận Mục 3.6:** *"Kết luận: Bề mặt gồ ghề thu hẹp dải đo từ 550 cm xuống 350 cm. Với chất lỏng tĩnh phẳng nhẵn trong bồn kín, cảm biến RCWL-1601 dùng được toàn dải xa; với vật liệu rắn dạng hạt, bề mặt nhám xốp hoặc mặt thoáng gợn sóng mạnh, chiều cao lắp đặt tối đa nên giới hạn dưới 300 – 350 cm (cơ sở cho thiết kế ở Chương 4)."*
   - **Loại bỏ hoàn toàn:** Các phân tích lý thuyết dài dòng về tán xạ đa tia ở cự ly gần ($10 \div 60\text{ cm}$), dịch chuyển đỉnh trượt chu kỳ trên dải trung bình, và các đồ thị đường $s$ và $\text{SE}$ cũ (`hinh_3_7a_do_lech_chuan_be_mat.png`, `hinh_3_7b_sai_so_chuan_be_mat.png`).

20. **Quy chuẩn Nội dung Mục 3.7 và 3.8 (Chương 3):**
   - **Mục 3.7: Phân tích ảnh hưởng của Nhiệt độ môi trường:**
     * Tiêu đề: `3.7. Phân tích ảnh hưởng của Nhiệt độ môi trường` (loại bỏ cụm *"và Hiệu quả thuật toán bù nhiệt Laplace"*).
     * Mở đầu: Trình bày gọn trong 1 câu: *"Để đánh giá sự ảnh hưởng của nhiệt độ, thí nghiệm đối chứng được thực hiện trên mặt phẳng nhẵn dọc 19 mốc cự ly từ 10 cm đến 300 cm ở nhiệt độ phòng và nhiệt độ điều hòa. Số liệu được lấy từ tệp “du_lieu_tong_hop/chuong_3/ thong_ke_chuong_3.csv”.*
     * Tiểu mục duy nhất: `3.7.1. Định lượng sai số trôi nhiệt và hiệu quả khử trôi của thuật toán Laplace` (loại bỏ tiểu mục cũ về Sự giãn dài thời gian bay).
     * Đối chứng định lượng:
       - Khi không bù nhiệt: kết quả đo bị phóng đại $+1.235\%$ quãng đường ($+12.28\text{ mm}$ tại $100\text{ cm}$, $+22.46\text{ mm}$ tại $200\text{ cm}$, cực đại $+39.92\text{ mm}$ tại $280\text{ cm}$).
       - Khi bù nhiệt Laplace: triệt tiêu trôi nhiệt hàng xentimét, $\Delta x$ dao động quanh $0\text{ mm}$ ($-5.73\text{ mm}$ tại $100\text{ cm}$, $+3.50\text{ mm}$ tại $200\text{ cm}$, $-2.79\text{ mm}$ tại $300\text{ cm}$), giúp 14/14 mốc ($80 \div 300\text{ cm}$) đạt $|\delta\%| \le 0.57\%$.
     * **Hình 3.8:** `Hình 3.8: So sánh sai số tuyệt đối Δx tại phòng lạnh 20.0 °C trước và sau khi kích hoạt thuật toán bù nhiệt độ Laplace trên dải 10 cm – 300 cm.`
     * Đánh giá đồ thị: Phân tích đường màu đỏ nét liền (Chưa bù nhiệt) và đường màu xanh lá nét đứt (Đã bù nhiệt Laplace), khẳng định bù Laplace là bắt buộc.
   - **Mục 3.8: Tổng hợp Độ không đảm bảo đo:**
     * Tiêu đề: `3.8. Tổng hợp Độ không đảm bảo đo` (loại bỏ cụm *"và Đối chiếu Đặc tính Kỹ thuật Thực nghiệm vs Datasheet"*).
     * Tiểu mục duy nhất: `3.8.1. Đánh giá Độ không đảm bảo đo mở rộng toàn dải` (loại bỏ cụm *"(ISO/GUM)"*).
     * Định nghĩa các thành phần: Trình bày trực tiếp $u_A = s/\sqrt{N}$, công thức phân bố chữ nhật $u_B = a/\sqrt{3}$, liệt kê cụ thể $u_{B1} \approx 0.289\text{ mm}$, $u_{B2} \approx 0.050\text{ mm}$, $u_{B3}(d) \approx 0.000503 \cdot d\text{ (mm)}$, và công thức mở rộng $U_{95\%} = 2 \cdot u_c$.
     * **Bảng 3.6:** `Bảng 3.6: Bảng tổng hợp các thành phần Độ không đảm bảo đo theo tiêu chuẩn.`
       - Gồm đúng **9 cột** (loại bỏ cột *$u_B\text{ tổng}$*): `Cự ly chuẩn d`, `Độ lệch chuẩn s`, `u_A`, `u_B1 (Thước)`, `u_B2 (Timer)`, `u_B3 (Nhiệt độ)`, `u_c tổng`, `U_95% (k=2)`, `Kết quả đo chuẩn Y`.
     * **Hình 3.9:** `Hình 3.9: Biểu đồ phân rã độ không đảm bảo đo Loại A (u_A) và Loại B (u_B) theo khoảng cách chuẩn.`
     * **Nhận xét & Kết luận đánh giá tổng quát:** Nhận xét sự chuyển dịch từ $u_{B1}$ ở cự ly gần sang $u_{B3}$ ở cự ly xa, toàn dải $U_{95\%} \le \pm 5.57\text{ mm}$. Đoạn kết luận tổng quát kết thúc Chương 3 khẳng định RCWL-1601 kết hợp ESP32 và bù Laplace đạt đặc tính vượt trội Datasheet, sẵn sàng triển khai vào ứng dụng bồn chứa ở Chương 4.
     * **Loại bỏ hoàn toàn:** Hình 3.10 (Biểu đồ $u_c$ và $U_{95\%}$), Tiểu mục 3.8.2 và Bảng 3.7 (Bảng đối chiếu Datasheet).

21. **Quy chuẩn Nội dung Chương 4: Xây dựng và Phân tích Bài toán Ứng dụng Thực tế:**
   - **Mục tiêu & Định hướng bài toán:**
     * Chuyển hóa toàn bộ các phát hiện đo lường ở Chương 3 vào việc giải quyết bài toán vật lý - kỹ thuật cụ thể: **Giám sát mức và thể tích chất lỏng thông minh trên mô hình bình chứa chai 2L cắt, kết hợp bơm chìm mini 6V trên vi điều khiển ESP32**.
     * Đối tượng mô hình: Chai nước ngọt 2L cắt bỏ chóp côn tạo thành bình trụ đứng đáy phẳng: $H_{\text{bình}} = 17.0\text{ cm}$, đường kính trong $D = 10.0\text{ cm}$ (bán kính $R = 5.0\text{ cm}$), gá cảm biến cao $H_{\text{gá}} = 5.0\text{ cm}$ trên miệng chai ($H_{\text{tổng}} = 22.0\text{ cm}$).
   - **Cấu trúc phân cấp Chương 4:**
     * Heading 1: `CHƯƠNG 4: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ`
     * Heading 2: `4.1. Tổng quan tiềm năng ứng dụng từ kết quả thực nghiệm của RCWL-1601`
       - Heading 3: `4.1.1. Các đặc tính đo lường cốt lõi định hình không gian ứng dụng` (Dải tuyến tính $5 – 350\text{ cm}$, Vùng chết vật lý $0 – 3\text{ cm}$, Độ nhạy nhiệt độ $+0.606\text{ m/s/}^\circ\text{C}$, Phản xạ gương mặt thoáng chất lỏng).
       - Heading 3: `4.1.2. Định hướng bài toán và lựa chọn bài toán trọng tâm`.
     * Heading 2: `4.2. Thiết kế hệ thống giám sát mức và thể tích bình chứa chai 2L`
       - Heading 3: `4.2.1. Mô hình hình học và chuyển đổi toán học bình chứa chai 2L`:
         + Công thức (4.1): $S_{\text{base}} = \pi \cdot R^2 = \pi \cdot 5.0^2 \approx 78.54\text{ cm}^2$
         + Công thức (4.2): $V_{\max} = S_{\text{base}} \cdot H_{\text{bình}} = 78.54 \cdot 17.0 \approx 1335.2\text{ cm}^3 \approx 1335\text{ mL}$
         + **Hình 4.1:** `Hình 4.1: Sơ đồ nguyên lý mô hình bình chứa chai 2L cắt (H = 17 cm, D = 10 cm) và cơ cấu gá cảm biến RCWL-1601.`
         + Chuỗi công thức chuyển đổi ToF sang $h(t)$ và $V(t)$: (4.3) $v(T) = 331.3 + 0.606 \cdot T$, (4.4) $d_{\text{comp}}(t) = v(T) \cdot t_{\text{echo}} / 2$, (4.5) $h(t) = 22.0 - d_{\text{comp}}(t)$, (4.6) $V(t) = S_{\text{base}} \cdot h(t)$.
       - Heading 3: `4.2.2. Vận dụng 4 phát hiện thực nghiệm vào thiết kế hệ thống`:
         + 1. Vượt vùng chết cơ khí ($H_{\text{gá}} = 5.0\text{ cm}$, cự ly luôn $d \ge 8.0\text{ cm} > 3.0\text{ cm}$).
         + 2. Bù nhiệt độ Laplace tự động thời gian thực bằng cảm biến DHT11.
         + 3. Chuỗi lọc số thích nghi 2 tầng: Lọc IQR ($N = 5$) triệt tiêu xung gai bọt khí + Moving Average ($W = 7$) san phẳng sóng gợn khi bơm nạp.
         + 4. Lan truyền Độ không đảm bảo đo theo ISO/GUM: Công thức (4.7) $u_c^2(V) = c_R^2 \cdot u_R^2 + c_h^2 \cdot u_c^2(h)$ và (4.8) $U_{95\%}(V) = 2 \cdot u_c(V) = 2 \cdot \sqrt{(2\pi R h \cdot u_R)^2 + (S_{\text{base}} \cdot u_h)^2}$.
       - Heading 3: `4.2.3. Bố trí mô hình thực nghiệm phần cứng thực tế`:
         + Mô tả phần cứng: ESP32, Sensor Shield, DHT11 ($T \approx 30.8^\circ\text{C}$), RCWL-1601 vuông góc mặt nước, LED Xanh/Đỏ trên breadboard.
         + **Hình 4.4:** `Hình 4.4: Mô hình thực tế.`
     * Heading 2: `4.3. Kết quả thử nghiệm mô phỏng và Đánh giá hiệu năng ứng dụng`
       - Heading 3: `4.3.1. Mô phỏng động học quá trình bơm nạp và hiệu quả lọc sóng gợn`:
         + Quá trình nạp nước $t = 50\text{ s}$ ($h = 2.0 \to 14.5\text{ cm}$), dao động sóng gợn thô $\pm 0.7\text{ cm}$. Bộ lọc 2 tầng nén sai số xuống $< \pm 0.08\text{ cm}$.
         + **Hình 4.2:** `Hình 4.2: Mô phỏng quá trình bơm nạp bình 2L và hiệu quả lọc sóng gợn bằng chuỗi lọc thích nghi IQR + Moving Average.`
       - Heading 3: `4.3.2. Đánh giá thể tích chất lỏng tức thời và Độ không đảm bảo đo mở rộng`:
         + Đánh giá $U_{95\%}(V)$ theo mức nước $h$. Tại mốc vận hành chuẩn $h = 10.1\text{ cm}$: $V = 792.5\text{ mL}$, $u_c(V) = \pm 13.8\text{ mL}$, $U_{95\%}(V) = \pm 27.7\text{ mL}$ ($k = 2$), sai số tương đối $\delta_V = \pm 3.49\% < 5\%$.
         + **Hình 4.3:** `Hình 4.3: Đặc tính thể tích chất lỏng V và Đánh giá Độ không đảm bảo đo mở rộng U_95%(V) theo tiêu chuẩn ISO/GUM.`
       - Heading 3: `4.3.3. Phân cấp 4 ngưỡng cảnh báo an toàn và Kịch bản vận hành bơm mini 6V`:
         + **Bảng 4.1:** `Bảng 4.1: Phân cấp 4 ngưỡng trạng thái giám sát và kịch bản điều khiển bơm mini 6V` (gồm 6 cột: Cấp trạng thái, Mức nước $h$, Thể tích $V$, Tỷ lệ, Chỉ thị & Còi báo, Kịch bản điều khiển bơm 6V; phân thành 4 cấp: Cạn khẩn cấp Low-Low $\le 2.5\text{ cm}$, Cảnh báo cạn Low $2.5 < h \le 5.0\text{ cm}$, Bình thường Normal $5.0 < h < 14.0\text{ cm}$, Tràn khẩn cấp High-High $\ge 14.0\text{ cm}$).
         + Cơ chế trễ ngưỡng (hysteretic deadband): Tránh rung giật relay (chattering) khi mức nước dao động quanh ranh giới.

22. **Quy chuẩn Nội dung Chương 5: Kết luận và Kiến nghị:**
   - **Độ dài và phong cách:** Trình bày ngắn gọn, cô đọng (khoảng 1.5 – 2 trang), tổng kết súc tích toàn bộ kết quả khoa học và kỹ thuật từ Chương 1 đến Chương 4, loại bỏ các diễn giải dài dòng.
   - **Cấu trúc phân cấp 3 mục chính:**
     * 5.1. Kết luận chung về đề tài: Gồm 3 khối tổng kết cô đọng: (1) Hệ thống thực nghiệm chuẩn hóa (bố trí trên hai bàn cao 85 cm, viên gạch chuẩn $40 \times 40\text{ cm}$, ESP32 $1\text{ }\mu\text{s}$, tối ưu $N = 50$ mẫu tin cậy 95%); (2) Đặc tính đo lường định lượng thực nghiệm (lọc IQR $4.800$ mẫu, OLS Bậc 1 $\hat{y} = 1.00273x - 0.48427\text{ cm}$ tối ưu trên tập Test 10 mốc với $\sum|e| = 41.07\text{ mm}$, đo xa 550 cm vượt 22% datasheet, vùng chết 0 - 3 cm, độ chụm cao $s < 0.4\text{ mm}$, $\text{SE} \le 0.57\text{ mm}$, trễ 0.553%, bù nhiệt Laplace $v(T)$, đánh giá tổng hợp độ không đảm bảo đo ISO/GUM $U_{95\%} \le 0.77\text{ mm}$ dải gần và $\le 5.57\text{ mm}$ toàn dải 550 cm); (3) Hiện thực hóa bài toán ứng dụng (bình chai 2L cắt $H = 17\text{ cm}, D = 10\text{ cm}$, bơm 6V, gá cao 5 cm vượt vùng chết, chuỗi lọc IQR + MA nén sóng gợn $< \pm 0.08\text{ cm}$, $U_{95\%}(V)$ đạt $\delta_V = \pm 3.49\% < 5\%$, điều khiển bơm 4 ngưỡng có trễ logic an toàn).
     * 5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật:
       - 5.2.1. Đánh giá ưu điểm và hạn chế của cảm biến RCWL-1601: Ưu điểm (chi phí thấp, tương thích 3.3V ESP32, đo xa 550 cm mặt nhẵn, đo không tiếp xúc); Hạn chế (vùng chết 0 - 3 cm, nhạy cảm nhiệt độ, suy hao trên mặt gồ ghề/xốp co hẹp còn 350 cm).
       - 5.2.2. Khuyến nghị kỹ thuật khi triển khai thực tế: 4 khuyến nghị then chốt: (1) Bố trí khoảng cách ly tối thiểu 5 - 10 cm vượt vùng chết và tránh vách bồn; (2) Tích hợp cảm biến bù nhiệt độ Laplace thời gian thực $v(T)$; (3) Chuỗi lọc số thích nghi IQR + Moving Average; (4) Điều khiển có dải trễ logic (deadband) chống rung giật relay.
     * 5.3. Tài liệu tham khảo: Danh mục trích dẫn chính thống chuẩn quốc tế và quốc gia (JCGM 100:2008 GUM, TCVN 9595-3:2013, ISO/IEC 17025:2017, Kinsler Acoustics, Bohn JAES 1988, Wuxi Richen IoT RCWL-1601/RCWL-9610 & Adafruit 4007, ESP32 Manual, Tukey EDA, Doebelin, Montgomery, Phan Quốc Phô & Nguyễn Đức Chiến - *Giáo trình Cảm biến*).

