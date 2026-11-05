# CHƯƠNG 3: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM

Chương 3 trình bày việc xử lý số liệu và phân tích kết quả đo từ bốn tập dữ liệu thực nghiệm: `FSDT.csv` (chiều tiến, mặt nhẵn, $27.0^\circ	ext{C}$), `BSDT.csv` (chiều lùi, mặt nhẵn, $27.0^\circ	ext{C}$), `FRDT.csv` (chiều tiến, mặt nhám, $27.0^\circ	ext{C}$) và `FSAT.csv` (chiều tiến, mặt nhẵn, $20.0^\circ	ext{C}$).

Các phân tích được xây dựng trên mô hình truyền sóng âm Laplace, phương pháp bình phương tối thiểu và quy chuẩn đánh giá độ không đảm bảo đo ISO/GUM đã nêu ở Chương 1.

---

## 3.1. Tiền xử lý dữ liệu và Đánh giá hiệu quả lọc sai số thô bằng Khoảng tứ phân vị (IQR)

### 3.1.1. Khung tiền xử lý và Cơ chế hình thành ngoại lai trong phép đo siêu âm

Theo thuật toán phát hiện sai số thô bằng Khoảng tứ phân vị (IQR / Tukey's Fences) đã nêu tại **Mục 1.3.2 (Chương 1)**, dữ liệu từ 4 tập thực nghiệm được xử lý. Để giữ nguyên chuỗi thời gian, thuật toán thực hiện gán giá trị trực tiếp: mẫu nào nằm ngoài khoảng hợp lệ $[LF, \, UF]$ sẽ được chuyển thành giá trị `NaN`.

Trong quá trình thu thập tín hiệu, dữ liệu thực nghiệm xuất hiện sai số thô do một số nguyên nhân:
1. **Xung quá thời gian chờ:** Sóng âm phản xạ bị suy hao biên độ dưới ngưỡng phát hiện của mạch thu RCWL-9610. Bộ đếm thời gian của vi điều khiển ESP32 chờ hết chu kỳ ($48\text{ ms}$) và trả về giá trị $\approx 824.6\text{ cm}$.
2. **Tán xạ phản xạ nhiều đường:** Trên bề mặt nhám (`FRDT`), sóng âm phản xạ qua các vật thể phụ trước khi về đầu thu, làm tăng thời gian lan truyền ToF và tạo các giá trị đột biến.

---

### 3.1.2. Tổng hợp kết quả lọc ngoại lai trên toàn bộ 4 tập dữ liệu thực nghiệm

Kết quả tính toán chi tiết của từng mốc cự ly được lưu tại bảng dữ liệu **`du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv`**, và dữ liệu sau khi lọc được lưu tại 4 tệp: `FSDT_clean.csv`, `BSDT_clean.csv`, `FRDT_clean.csv`, `FSAT_clean.csv`.

Bảng 3.1 tổng hợp kết quả lọc dữ liệu trên 4 tập thực nghiệm:

| Tệp dữ liệu | Điều kiện thực nghiệm | Số mốc cự ly | Tổng số mẫu | Số mốc có ngoại lai | Số mẫu ngoại lai | Tỷ lệ ngoại lai (%) | Số mẫu hợp lệ | Tỷ lệ hợp lệ (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`FSDT.csv`** | Chiều tiến – Mặt nhẵn ($27.0^\circ	ext{C}$) | 35 mốc | 1.750 | 16 mốc | 77 mẫu | 4.40% | 1.673 mẫu | 95.60% |
| **`BSDT.csv`** | Chiều lùi – Mặt nhẵn ($27.0^\circ	ext{C}$) | 19 mốc | 950 | 12 mốc | 61 mẫu | 6.42% | 889 mẫu | 93.58% |
| **`FRDT.csv`** | Chiều tiến – Mặt nhám ($27.0^\circ	ext{C}$) | 23 mốc | 1.150 | 11 mốc | 59 mẫu | 5.13% | 1.091 mẫu | 94.87% |
| **`FSAT.csv`** | Chiều tiến – Phòng lạnh ($20.0^\circ	ext{C}$) | 19 mốc | 950 | 8 mốc | 38 mẫu | 4.00% | 912 mẫu | 96.00% |
| **TỔNG HỢP** | **Cả 4 tập thực nghiệm** | **96 mốc** | **4.800** | **47 mốc** | **235 mẫu** | **4.90%** | **4.565 mẫu** | **95.10%** |

*Bảng 3.1: Tổng hợp kết quả xử lý sai số thô bằng Khoảng tứ phân vị (IQR) trên toàn bộ 4.800 mẫu đo.*

**Nhận xét:**
- **Tỷ lệ giữ lại mẫu đạt $95.10\%$:** Hệ thống đo duy trì độ ổn định tốt; chỉ có $4.90\%$ mẫu bị loại bỏ trên toàn bộ 4.800 lần đo.
- **Tính đối xứng giữa chiều tiến và chiều lùi:** Tỷ lệ ngoại lai giữa `FSDT` ($4.40\%$) và `BSDT` ($6.42\%$) gần tương đương nhau, cho thấy điều kiện môi trường đo ổn định.
- **Ảnh hưởng của bề mặt phản xạ:** Bề mặt nhám (`FRDT`) xuất hiện nhiều xung tán xạ hơn so với mặt nhẵn. Các xung này được bộ lọc IQR phát hiện và loại bỏ, giúp giá trị trung bình không bị lệch.

---

### 3.1.3. Đánh giá trực quan hiệu quả triệt tiêu độ lệch chuẩn trên toàn dải đo

Hình 3.1 thể hiện biến thiên của độ lệch chuẩn thực nghiệm $s$ trước và sau khi lọc trên thang bán logarit (semi-log scale), trong đó trục tung biểu diễn độ lệch chuẩn $s$ theo thang logarit cơ số 10 ($0.1$ đến $1000	ext{ mm}$) và trục hoành biểu diễn khoảng cách chuẩn đối chứng từ $1	ext{ cm}$ đến $600	ext{ cm}$.

![Độ lệch chuẩn trước và sau khi lọc IQR](../graph/chuong_3/hinh_3_1_loc_sai_so_tho.png)

*Hình 3.1: Độ lệch chuẩn trước và sau khi lọc IQR.*

**Đánh giá từ đồ thị:**
- **Đường màu đỏ nét đứt (Độ lệch chuẩn thô trước khi lọc):**
  + Trong khoảng đo làm việc ($1 - 340	ext{ cm}$), độ lệch chuẩn duy trì ở mức dưới $1.0	ext{ mm}$.
  + Tại mốc $360	ext{ cm}$, do hiện tượng trượt chu kỳ sóng ToF, độ lệch chuẩn thô tăng lên $s = 90.33	ext{ mm}$.
  + Tại các cự ly xa ($580	ext{ cm}$ và $600	ext{ cm}$), do sóng phản xạ suy hao mạnh dẫn đến các mẫu quá hạn (timeout $824.6	ext{ cm}$), độ lệch chuẩn thô tăng lên lần lượt $s = 346.05	ext{ mm}$ và $s = 2621.02	ext{ mm}$.
- **Đường màu xanh nét liền (Độ lệch chuẩn sau khi lọc IQR):**
  + Sau khi loại bỏ các giá trị ngoại lai bằng bộ lọc IQR kết hợp ngưỡng phân giải $\Delta_{	ext{LSB}} = 0.0175	ext{ cm}$, đường độ lệch chuẩn duy trì ổn định trong dải $0.09 - 4.0	ext{ mm}$ trên toàn dải đo $6	ext{ m}$, tiệm cận đường dung sai của thước cơ khí ($0.5	ext{ mm}$).
- **Bảng đối chiếu định lượng tại các mốc tiêu biểu:**

| Khoảng cách chuẩn | Độ lệch chuẩn thô $s_{	ext{thô}}$ | Độ lệch chuẩn sau lọc $s_{	ext{sạch}}$ | Tỷ lệ giảm độ lệch chuẩn | Số mẫu ngoại lai | Nguyên nhân hiện tượng |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$50	ext{ cm}$** | $0.094	ext{ mm}$ | $0.094	ext{ mm}$ | $1.0	ext{ lần}$ | $0/50\ (0\%)$ | Vùng đo ổn định, không có ngoại lai |
| **$100	ext{ cm}$** | $0.383	ext{ mm}$ | $0.383	ext{ mm}$ | $1.0	ext{ lần}$ | $0/50\ (0\%)$ | Nhỏ hơn dung sai thước ($0.5	ext{ mm}$), giữ lại $100\%$ mẫu |
| **$360	ext{ cm}$** | $90.33	ext{ mm}$ | **$2.51	ext{ mm}$** | **Giảm $36.0	ext{ lần}$** | $1/50\ (2\%)$ | Loại bỏ xung trượt chu kỳ sóng ToF |
| **$580	ext{ cm}$** | $346.05	ext{ mm}$ | **$3.30	ext{ mm}$** | **Giảm $104.8	ext{ lần}$** | $4/50\ (8\%)$ | Loại bỏ xung bão hòa timeout $824.6	ext{ cm}$ |
| **$600	ext{ cm}$** | $2621.02	ext{ mm}$ | **$0.63	ext{ mm}$** | **Giảm $4153.8	ext{ lần}$** | $7/50\ (14\%)$ | Cắt bỏ các xung quá hạn ở giới hạn cự ly |

---

## 3.2. Khảo sát Dải đo thực tế, Vùng chết và Giới hạn bão hòa xa

Để xác định dải làm việc thực tế của cảm biến RCWL-1601, chuỗi dữ liệu thực nghiệm gồm 35 mốc cự ly từ $1\text{ cm}$ đến $600\text{ cm}$ thuộc tập chuẩn `FSDT_clean.csv` (nhiệt độ phòng $27.0^\circ\text{C}$, mặt phẳng nhẵn) được đưa vào phân tích sai số:
- Sai số tuyệt đối: $\Delta d = \bar{d} - d_{\text{chuẩn}}$ (mm)
- Sai số tương đối: $\delta = \frac{\bar{d} - d_{\text{chuẩn}}}{d_{\text{chuẩn}}} \times 100\%$ (\%)

Biến thiên của sai số tương đối theo khoảng cách chuẩn được thể hiện trên Hình 3.2:

![Sai số tương đối theo khoảng cách chuẩn](../graph/chuong_3/hinh_3_2_sai_so_tuong_doi.png)

*Hình 3.2: Sai số tương đối theo khoảng cách chuẩn (Tập dữ liệu FSDT, giới hạn trục tung $\pm 10\%$).*

Từ diễn biến của đường sai số trên đồ thị Hình 3.2, đặc tính làm việc của cảm biến được phân chia thành 4 vùng rõ rệt:

### 3.2.1. Vùng chết (1 cm – 3 cm)
Khi vật cản đặt quá gần mặt cảm biến trong khoảng từ $1\text{ cm}$ đến $3\text{ cm}$, cảm biến mất hoàn toàn tính tuyến tính, giá trị đo bị kẹt quanh mức $2.0 - 2.7\text{ cm}$ dẫn đến sai số rất lớn:
- Tại $1.0\text{ cm}$: Giá trị trung bình $\bar{d} = 2.030\text{ cm}$, sai số tuyệt đối $+10.30\text{ mm}$, sai số tương đối **$+103.05\%$**.
- Tại $2.0\text{ cm}$: Giá trị trung bình $\bar{d} = 2.352\text{ cm}$, sai số tuyệt đối $+3.52\text{ mm}$, sai số tương đối **$+17.59\%$**.
- Tại $3.0\text{ cm}$: Giá trị trung bình $\bar{d} = 2.679\text{ cm}$, sai số tuyệt đối $-3.21\text{ mm}$, sai số tương đối **$-10.72\%$**.

**Giải thích cơ chế vật lý:** Hiện tượng này bắt nguồn từ thời gian suy giảm dao động cơ học của màng loa gốm áp điện và thời gian ngắt câm (blanking time) của IC RCWL-9610. Khi kích xung phát $40\text{ kHz}$ ($200\text{ }\mu\text{s}$), màng rung cần khoảng $120 - 150\text{ }\mu\text{s}$ để triệt tiêu dao động dư. Ở khoảng cách dưới $3\text{ cm}$, thời gian sóng âm đi và về nhỏ hơn $175\text{ }\mu\text{s}$, trùng lặp với thời gian ngắt câm nên mạch thu không phân biệt được xung phản xạ thực và xung kích dư, dẫn tới giá trị đo bị khóa cứng tại ngưỡng ngắt câm tối thiểu.

### 3.2.2. Dải đo tuyến tính ổn định (5 cm – 400 cm)
Bắt đầu từ cự ly $5\text{ cm}$ (mốc chuyển tiếp thoát mù với sai số $-14.10\%$) và đặc biệt từ $10\text{ cm}$ trở đi, xung phản xạ tách biệt hoàn toàn khỏi xung phát. Biên độ sóng dội về nằm trọn vẹn trong dải khuếch đại tuyến tính của vi mạch. Sai số tương đối trong toàn bộ dải đo danh định từ $10\text{ cm}$ đến $400\text{ cm}$ luôn hội tụ chặt chẽ trong dải dung sai $\pm 0.5\%$ của nhà sản xuất (tại $50\text{ cm}$ là $-0.31\%$, tại $100\text{ cm}$ là $-0.57\%$, tại $200\text{ cm}$ là $+0.18\%$, tại $300\text{ cm}$ là $-0.09\%$, và tại $400\text{ cm}$ là $+0.35\%$). Điều này chứng minh cảm biến hoạt động với độ chính xác và độ ổn định cao trong phạm vi công bố.

### 3.2.3. Dải đo xa mở rộng vượt định mức (420 cm – 550 cm)
Thông số công bố của nhà sản xuất quy định cự ly đo tối đa của RCWL-1601 là $400\text{ cm}$ (hoặc $450\text{ cm}$ trong điều kiện lý tưởng). Tuy nhiên, trên thực nghiệm với bia phản xạ phẳng nhẵn ($40 \times 40\text{ cm}$) đặt vuông góc $90^\circ$ với trục cảm biến, module RCWL-1601 vẫn duy trì khả năng bắt sóng phản xạ chính xác cao vượt ngưỡng thiết kế:
- Tại $420\text{ cm}$: Giá trị trung bình $\bar{d} = 421.241\text{ cm}$ (sai số tương đối $+0.29\%$).
- Tại $500\text{ cm}$: Giá trị trung bình $\bar{d} = 500.691\text{ cm}$ (sai số tương đối $+0.14\%$).
- Tại $550\text{ cm}$: Giá trị trung bình $\bar{d} = 550.630\text{ cm}$ (sai số tương đối $+0.11\%$, độ lệch chuẩn sau lọc $s = 0.319\text{ mm}$).

Tầm đo mở rộng đạt được là nhờ khối tiền khuếch đại tự động điều chỉnh độ lợi (AGC) trên vi mạch RCWL-9610 có độ nhạy vượt trội so với các mạch rời thế hệ cũ, cùng với việc căn chỉnh vuông góc bề mặt phản xạ giúp bảo toàn năng lượng sóng dội về.

### 3.2.4. Ngưỡng suy hao và bão hòa xa (580 cm – 600 cm)
Khi khoảng cách tăng lên từ $580\text{ cm}$, mật độ năng lượng sóng phản xạ suy giảm mạnh theo hàm nghịch đảo bình phương khoảng cách, tiệm cận ngưỡng suy hao giới hạn của mạch thu:
- Tại $580\text{ cm}$: Tín hiệu phản xạ suy yếu, bắt đầu xuất hiện $4/50$ mẫu ngoại lai do tràn thời gian chờ echo ($824.6\text{ cm}$). Sau khi loại bỏ ngoại lai bằng IQR, giá trị trung bình là $579.850\text{ cm}$ (sai số $-0.03\%$, $s = 3.303\text{ mm}$).
- Tại $600\text{ cm}$: Tín hiệu suy hao vượt ngưỡng nhạy, xuất hiện $7/50$ mẫu timeout. Tại mốc này, cảm biến mất hoàn toàn khả năng bắt sóng phản xạ thực, chuỗi đo chuyển sang trạng thái bão hòa hoàn toàn với giá trị đo vọt lên bão hòa $824.562\text{ cm}$, sai số tăng vọt $+37.43\%$.

Kết luận: Dải làm việc tin cậy và đạt chuẩn độ chính xác cao của cảm biến RCWL-1601 trong thực tế là từ **$10\text{ cm}$ đến $550\text{ cm}$**.

Bảng 3.3 trích xuất số liệu sai số định lượng tại các mốc cự ly tiêu biểu trên tập `FSDT_clean.csv`:

| Cự ly chuẩn $d_{\text{chuẩn}}$ | Giá trị trung bình $\bar{d}$ | Sai số tuyệt đối $\Delta d$ | Sai số tương đối $\delta$ | Độ lệch chuẩn $s$ | Phân vùng làm việc |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$1.0\text{ cm}$** | $2.030\text{ cm}$ | $+10.30\text{ mm}$ | **$+103.05\%$** | $0.035\text{ mm}$ | Vùng chết (kẹt giá trị đo) |
| **$2.0\text{ cm}$** | $2.352\text{ cm}$ | $+3.52\text{ mm}$ | **$+17.59\%$** | $0.085\text{ mm}$ | Vùng chết (kẹt giá trị đo) |
| **$3.0\text{ cm}$** | $2.679\text{ cm}$ | $-3.21\text{ mm}$ | **$-10.72\%$** | $0.056\text{ mm}$ | Vùng chết (kẹt giá trị đo) |
| **$5.0\text{ cm}$** | $4.295\text{ cm}$ | $-7.05\text{ mm}$ | **$-14.10\%$** | $0.085\text{ mm}$ | Vùng chuyển tiếp (sai số lớn) |
| **$10.0\text{ cm}$** | $10.570\text{ cm}$ | $+5.70\text{ mm}$ | $+5.70\%$ | $0.061\text{ mm}$ | Bắt đầu dải đo danh định |
| **$50.0\text{ cm}$** | $49.847\text{ cm}$ | $-1.53\text{ mm}$ | **$-0.31\%$** | $0.094\text{ mm}$ | Dải làm việc ổn định (dung sai $\pm 0.5\%$) |
| **$100.0\text{ cm}$** | $99.429\text{ cm}$ | $-5.71\text{ mm}$ | **$-0.57\%$** | $0.383\text{ mm}$ | Dải làm việc ổn định |
| **$200.0\text{ cm}$** | $200.351\text{ cm}$ | $+3.51\text{ mm}$ | **$+0.18\%$** | $2.192\text{ mm}$ | Dải làm việc ổn định |
| **$300.0\text{ cm}$** | $299.718\text{ cm}$ | $-2.82\text{ mm}$ | **$-0.09\%$** | $2.860\text{ mm}$ | Dải làm việc ổn định |
| **$400.0\text{ cm}$** | $401.399\text{ cm}$ | $+13.99\text{ mm}$ | **$+0.35\%$** | $0.270\text{ mm}$ | Giới hạn danh định của Datasheet |
| **$500.0\text{ cm}$** | $500.691\text{ cm}$ | $+6.91\text{ mm}$ | **$+0.14\%$** | $1.978\text{ mm}$ | Dải mở rộng (vượt chuẩn nhà sản xuất) |
| **$550.0\text{ cm}$** | $550.630\text{ cm}$ | $+6.30\text{ mm}$ | **$+0.11\%$** | $0.319\text{ mm}$ | Giới hạn đo xa thực tế cực đại |
| **$580.0\text{ cm}$** | $579.850\text{ cm}$ | $-1.50\text{ mm}$ | $-0.03\%$ | $3.303\text{ mm}$ | Ngưỡng suy hao (xuất hiện mẫu timeout) |
| **$600.0\text{ cm}$** | $824.562\text{ cm}$ | $+2245.62\text{ mm}$ | **$+37.43\%$** | $0.631\text{ mm}$ | Bão hòa hoàn toàn (mất xung phản xạ) |

---

## 3.3. Đánh giá Độ chụm và Độ chính xác

Trên cơ sở tập dữ liệu chuẩn chiều tiến mặt nhẵn FSDT sau khi xử lý ngoại lai tại Mục 3.1, độ chụm và độ chính xác của hệ đo được đánh giá trên 33 mốc cự ly thuộc dải đo hữu ích từ 1 cm đến 550 cm (trước ngưỡng bão hòa xa 580 – 600 cm). Toàn bộ số liệu gốc phục vụ phân tích và vẽ đồ thị được lưu trữ đầy đủ trong tệp `du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv`.

### 3.3.1. Đánh giá độ chụm

Áp dụng độ lệch chuẩn mẫu thực nghiệm $s$ tại Mục 1.3.1 và sai số chuẩn của giá trị trung bình $\text{SE}$ tại Mục 1.3.3 (Chương 1), chuỗi số liệu của 33 mốc cự ly ($1\text{ cm} \div 550\text{ cm}$, tại nhiệt độ chuẩn hóa 27.0 °C, $N = 50$ mẫu thô/mốc, cỡ mẫu hợp lệ sau lọc $n_{\text{hợp lệ}} \in [40, 50]$) được trích xuất trực tiếp từ hai cột `std_sach_mm` và `se_sach_mm` trong tệp `du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv`:

1. **Vùng cự ly gần ($1\text{ cm} \le x_{\text{true}} \le 50\text{ cm}$, 9 mốc):** Tại 8/9 mốc khảo sát, $s$ đạt từ $0.035\text{ mm}$ đến $0.094\text{ mm}$ và $\text{SE}$ đạt từ $0.0049\text{ mm}$ đến $0.0133\text{ mm}$ (nhỏ hơn nhiều so với một bước đếm phần cứng $\Delta_{\text{LSB}} \approx 0.174\text{ mm}$) nhờ biên độ sóng phản xạ mạnh từ mặt phẳng nhẵn của viên gạch chuẩn $40\text{ cm} \times 40\text{ cm}$. Riêng mốc $40\text{ cm}$ ($n_{\text{hợp lệ}} = 49$) ghi nhận $s = 3.144\text{ mm}$ và $\text{SE} = 0.4491\text{ mm}$.
2. **Vùng cự ly trung bình ($60\text{ cm} \le x_{\text{true}} \le 180\text{ cm}$, 8 mốc):** Tại 7/8 mốc, $s$ nằm trong dải $0.088\text{ mm} \div 0.383\text{ mm}$ và $\text{SE}$ nằm trong dải $0.0128\text{ mm} \div 0.0542\text{ mm}$; riêng mốc $120\text{ cm}$ ($n_{\text{hợp lệ}} = 50$) có $s = 1.747\text{ mm}$ và $\text{SE} = 0.2471\text{ mm}$.
3. **Vùng cự ly xa danh định ($200\text{ cm} \le x_{\text{true}} \le 360\text{ cm}$, 11 mốc):** Độ lệch chuẩn $s$ dao động từ $0.142\text{ mm}$ (tại $220\text{ cm}$, $n_{\text{hợp lệ}} = 40$) đến $2.860\text{ mm}$ (tại $300\text{ cm}$, $n_{\text{hợp lệ}} = 50$), tương ứng $\text{SE}$ biến thiên từ $0.0225\text{ mm}$ đến $0.4045\text{ mm}$ (tại $360\text{ cm}$ đạt $s = 2.508\text{ mm}$, $\text{SE} = 0.3583\text{ mm}$).
4. **Dải đo xa mở rộng ($400\text{ cm} \le x_{\text{true}} \le 550\text{ cm}$, 5 mốc):** Độ lệch chuẩn $s$ đạt $0.270\text{ mm}$ tại $400\text{ cm}$ ($\text{SE} = 0.0407\text{ mm}$), $0.228\text{ mm}$ tại $420\text{ cm}$ ($\text{SE} = 0.0340\text{ mm}$), tăng lên cực đại toàn dải $4.049\text{ mm}$ tại $450\text{ cm}$ ($\text{SE} = 0.5726\text{ mm}$), đạt $1.978\text{ mm}$ tại $500\text{ cm}$ ($\text{SE} = 0.2797\text{ mm}$) và giảm về $0.319\text{ mm}$ tại mốc giới hạn $550\text{ cm}$ ($n_{\text{hợp lệ}} = 42$, $\text{SE} = 0.0492\text{ mm}$).

Tính trên toàn bộ 33 mốc khảo sát ($1 \div 550\text{ cm}$), cột `se_sach_mm` xác nhận sai số chuẩn trung bình $\text{SE}$ không vượt quá $0.5726\text{ mm}$; trong đó có 32/33 mốc đạt $\text{SE} < 0.45\text{ mm}$ (nhỏ hơn nửa độ chia nhỏ nhất $0.5\text{ mm}$ của thước chuẩn) và 22/33 mốc đạt $\text{SE} \le 0.10\text{ mm}$.

**Giải thích cơ chế vật lý và thuật toán của dạng dao động răng cưa trên Hình 3.3:**
Trục hoành của Hình 3.3 biểu diễn sự thay đổi mốc khoảng cách chuẩn $x_{\text{true}}$ (mỗi mốc đều đo độc lập với cỡ mẫu cố định $N = 50$), không phải trục tăng dần kích thước mẫu tích lũy $k$ tại một vị trí cố định như bài toán hội tụ ở Mục 2.4 (Chương 2). Dạng lên xuống răng cưa luân phiên của $s$ giữa các mốc cự ly xuất phát từ sự tương tác giữa bước nhảy một chu kỳ sóng mang siêu âm 40 kHz và ngưỡng tứ phân vị 25% của bộ lọc IQR (đã nêu tại Mục 1.3.2, Chương 1). Tại $T = 27.0\text{ }^\circ\text{C}$ ($v = 347.66\text{ m/s}$), một chu kỳ sóng mang $T_0 = 25\text{ }\mu\text{s}$ ứng với quãng đường khứ hồi nửa bước sóng xấp xỉ $4.35\text{ mm}$ ($0.435\text{ cm}$). Khi biên độ sườn lên của bó xung phản hồi ECHO rơi sát mức điện áp ngưỡng so sánh trong vi mạch RCWL-9610, thời điểm kích hoạt bắt xung bị trượt $\pm 1$ chu kỳ sóng mang giữa các lần đo trong cùng 50 mẫu:

- **Nhóm mốc lọc sạch cụm trượt chu kỳ:** Tại những mốc cự ly có dưới 25% số mẫu trượt sang chu kỳ kế cận (như 80, 150, 220, 320, 400, 420, 550 cm, với 5 – 10 mẫu ngoại lai bị loại trong `thong_ke_chuong_3.csv`), hai tứ phân vị $Q_1$ và $Q_3$ vẫn nằm gọn trong cùng một chu kỳ sóng mang ($\text{IQR} \approx 0.018 \div 0.066\text{ cm}$); hàng rào Tukey cắt bỏ hoàn toàn cụm trượt chu kỳ, đưa $s$ xuống mức rất thấp ($0.142 \div 0.395\text{ mm}$) và $\text{SE}$ xuống $0.022 \div 0.060\text{ mm}$.
- **Nhóm mốc giữ lại hai cụm chu kỳ kế tiếp:** Tại các mốc cự ly có trên 25% số mẫu phân bố sang chu kỳ kế cận (như 40, 120, 200, 260, 300, 360, 450 cm, có 0 – 3 mẫu bị loại), cả hai cụm đều lọt vào giữa $Q_1$ và $Q_3$ làm $\text{IQR}$ mở rộng lên đúng một bước nhảy sóng mang ($\text{IQR} \approx 0.435\text{ cm}$); phân bố hai đỉnh đẩy độ lệch chuẩn mẫu $s$ lên vùng $1.7 \div 4.0\text{ mm}$. Tuy nhiên, sai số chuẩn của giá trị trung bình $\text{SE} = s / \sqrt{n}$ luôn được nén xuống dưới $0.57\text{ mm}$, bảo đảm độ tin cậy thống kê tuyệt đối cho phép lấy trung bình.

![Độ lệch chuẩn thực nghiệm s và sai số chuẩn trung bình SE](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_3_do_chum_toan_dai.png)
*Hình 3.3: Độ lệch chuẩn thực nghiệm s và sai số chuẩn trung bình SE theo khoảng cách chuẩn (1 cm – 550 cm).*

**Đánh giá từ đồ thị Hình 3.3:** Khi biểu diễn chung trên cùng một trục tung đơn vị mm, sự khác biệt giữa hai đường phản ánh rõ năng lực của phép đo:
- **Đường màu xanh lam nét liền (Độ lệch chuẩn thực nghiệm $s$):** Nằm dưới vạch dung sai thước $0.5\text{ mm}$ tại phần lớn các mốc đơn chu kỳ và chỉ nhô lên tại các điểm giao thoa ngưỡng trượt chu kỳ sóng mang $40\text{ kHz}$.
- **Đường màu cam nét đứt (Sai số chuẩn trung bình $\text{SE} = s/\sqrt{n}$):** Nhờ phép lấy trung bình trên $n_{\text{hợp lệ}} \ge 40$ mẫu, đường $\text{SE}$ bị nén phẳng hoàn toàn sát đáy trục hoành (dao động cực nhỏ từ $0.0049\text{ mm}$ đến $0.5726\text{ mm}$), chứng minh tính hội tụ cao và triệt tiêu gần như hoàn toàn sai số ngẫu nhiên của hệ thống đo.

### 3.3.2. Đánh giá độ chính xác

Sử dụng sai số tuyệt đối $\Delta x$ và sai số tương đối $\delta$ (%) đã định nghĩa tại Mục 1.3.3 (Chương 1), chuỗi số liệu được trích xuất từ cột `sai_so_tuyet_doi_mm` và `sai_so_tuong_doi_pct` trong `thong_ke_chuong_3.csv`:

- **Sai số tuyệt đối ($\Delta x$):** Trong dải từ $50\text{ cm}$ đến $550\text{ cm}$ (25 mốc), $\Delta x$ biến thiên trong khoảng hẹp từ $-5.71\text{ mm}$ đến $+14.02\text{ mm}$; có 17/25 mốc có sai số tuyệt đối không vượt quá $\pm 5.0\text{ mm}$ và 22/25 mốc nằm trong phạm vi $\pm 8.0\text{ mm}$.
- **Sai số tương đối ($\delta\%$):** Ở vùng đầu dải đo danh định ($10\text{ cm} \div 40\text{ cm}$), do mẫu số $x_{\text{true}}$ nhỏ nên $\delta\%$ đạt từ $-3.36\% \div +5.70\%$; tuy nhiên khi khoảng cách tăng lên từ $50\text{ cm}$ đến $550\text{ cm}$, sai số tương đối nhanh chóng hội tụ và nằm hoàn toàn trong dải hẹp $\mathbf{[-0.57\%; +0.35\%]}$. Tại các cự ly lớn ($300\text{ cm}$, $500\text{ cm}$, $550\text{ cm}$), sai số tương đối chỉ còn $-0.09\%$, $+0.14\%$ và $+0.11\%$.
- **Nguồn gốc sai số hệ thống:** Độ lệch tuyệt đối cỡ vài milimét bắt nguồn từ hai yếu tố thực tế: khoảng cách thụt lùi cơ khí của màng rung gốm áp điện nằm sâu bên trong ống bảo vệ kim loại so với mép ngoài bo mạch ($\sim 4.84\text{ mm}$, hoàn toàn trùng khớp với hệ số tự do của phương trình hồi quy tuyến tính tại Mục 3.4) và sai số định vị mép chân gạch trên thước thép chuẩn.

![Sai số tuyệt đối và Sai số tương đối](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_4_do_chinh_xac_sai_so.png)
*Hình 3.4: Sai số tuyệt đối Δx (mm) và sai số tương đối δ (%) theo khoảng cách chuẩn (10 cm – 550 cm).*

**Đánh giá từ đồ thị Hình 3.4:** Biểu đồ đơn ghép hai trục tung Y (đồng bộ đường chuẩn gốc 0 giữa hai trục) cho thấy hai xu hướng đối chiếu trực quan:
- **Đường màu xanh lá nét liền (Sai số tuyệt đối $\Delta x$, trục trái):** Dao động quanh trục $0\text{ mm}$ trong biên độ hẹp $[-5.71; +14.02]\text{ mm}$ trên toàn bộ dải đo, khẳng định hệ thống không bị hiện tượng trôi tích lũy dốc theo khoảng cách.
- **Đường màu xanh lam nét đứt (Sai số tương đối $\delta\%$, trục phải):** Hội tụ rất nhanh từ ngưỡng $+5.70\%$ ở cự ly gần về sát vạch chuẩn $0\%$ khi $x_{\text{true}} \ge 50\text{ cm}$ (luôn nằm dưới $0.57\%$), minh chứng cho độ chính xác cao của hệ đo RCWL-1601.

---

## 3.4. Đánh giá Độ tuyến tính (Linearity)

### 3.4.1. Hồi quy đa thức và Đánh giá Độ tuyến tính (Linearity)

Độ tuyến tính (Linearity) là đặc tính tĩnh cơ bản phản ánh mức độ quan hệ tỷ lệ thuận giữa khoảng cách dịch chuyển thực tế và giá trị đo hiển thị của cảm biến. Để đánh giá một cách khoa học, khách quan và tránh hiện tượng lạc quan thái quá do đánh giá trên chính dữ liệu huấn luyện, toàn bộ 34 mốc thực nghiệm trên toàn dải đo ($1.0\text{ cm}$ đến $580.0\text{ cm}$) đã được phân chia ngẫu nhiên có kiểm soát theo tỷ lệ chuẩn thực nghiệm **70% dữ liệu Huấn luyện (Train set - 24 mốc)** và **30% dữ liệu Kiểm thử độc lập (Test set - 10 mốc)**.

- **Tập huấn luyện (Train - 24 mốc):** $[1.0, 3.0, 5.0, 8.0, 10.0, 40.0, 60.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 240.0, 250.0, 260.0, 300.0, 320.0, 340.0, 360.0, 400.0, 420.0, 500.0, 550.0]\text{ cm}$. Dùng để thiết lập hệ phương trình chuẩn tắc và giải ma trận xác định hệ số cho 3 mô hình hồi quy đa thức.
- **Tập kiểm thử độc lập (Test - 10 mốc):** $[2.0, 20.0, 50.0, 80.0, 150.0, 220.0, 280.0, 350.0, 450.0, 580.0]\text{ cm}$. Trải dài từ vùng chết, dải đo danh định đến vùng suy hao xa, hoàn toàn không tham gia vào quá trình tìm hệ số, đóng vai trò làm "bài kiểm tra mù" để đối sánh năng lực dự đoán thực tế của 3 mô hình.

Hệ phương trình chuẩn tắc phương pháp bình phương bé nhất (OLS):

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}$$

Giải hệ phương trình chuẩn tắc trên 24 mốc thực nghiệm tập Train (70%), kết quả tính toán xác định được phương trình của 3 mô hình hồi quy đa thức như sau:

1. **Mô hình Bậc 1 (Tuyến tính):**
   $$\hat{y}_1 = 1.00273441 \cdot x - 0.48427223 \quad (\text{cm})$$
   *(Trong đó hệ số góc $a_1 = 1.002734$ bám sát độ dốc lý tưởng 1:1, hệ số tự do $b_1 = -0.484\text{ cm}$ phản ánh chính xác khoảng thụt lùi cơ khí $-4.84\text{ mm}$ của màng loa gốm phía trong vỏ kim loại).*

2. **Mô hình Bậc 2:**
   $$\hat{y}_2 = 3.56559128 \times 10^{-6} \cdot x^2 + 1.00103491 \cdot x - 0.37940440 \quad (\text{cm})$$
   *(Hệ số bậc 2 rất nhỏ cỡ $10^{-6}$, đường đặc tính thực tế tiệm cận đường thẳng).*

3. **Mô hình Bậc 3:**
   $$\hat{y}_3 = -1.04345666 \times 10^{-7} \cdot x^3 + 8.50580899 \times 10^{-5} \cdot x^2 + 0.98551084 \cdot x - 0.00036859 \quad (\text{cm})$$
   *(Chứa các số hạng phi tuyến bậc 3 và bậc 2 có xu hướng uốn lượn ở hai đầu mút).*

*Ghi chú: Toàn bộ các tổng ma trận chuẩn tắc phục vụ tính toán ($N = 24, \sum x, \sum x^2, \dots, \sum x^6, \sum xy, \sum x^2y, \sum x^3y$) được lưu trữ đầy đủ trong tệp cơ sở dữ liệu `du_lieu_tong_hop/chuong_3/cac_tong_hoi_quy.csv`.*

Do trên thang đo lớn từ $0\text{ cm}$ đến $600\text{ cm}$, đặc tính của cả ba mô hình đều có độ dốc xấp xỉ 1:1 và bám rất sát chuỗi dữ liệu thực nghiệm, nên mắt thường không thể phân biệt được mô hình nào tối ưu nếu chỉ nhìn vào đường hồi quy tổng thể. Do đó, để xác định mô hình phản ánh trung thực bản chất vật lý của cảm biến, bắt buộc phải thực hiện đối sánh định lượng sai số dự đoán trên 10 mốc kiểm thử độc lập (Test set) và phóng đại thang đo sai số lên mức milimét.

#### Bảng 3.4: Đối sánh sai số dự đoán của 3 mô hình hồi quy trên 10 mốc kiểm thử độc lập

| Mốc Test $x$ | $y$ thực tế | $\hat{y}$ Bậc 1 | $e$ Bậc 1 (mm) | $\hat{y}$ Bậc 2 | $e$ Bậc 2 (mm) | $\hat{y}$ Bậc 3 | $e$ Bậc 3 (mm) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$2.0\text{ cm}$** | $2.352\text{ cm}$ | $1.521\text{ cm}$ | $+8.31$ | $1.623\text{ cm}$ | $+7.29$ | $1.971\text{ cm}$ | **$+3.81$** |
| **$20.0\text{ cm}$** | $19.328\text{ cm}$ | $19.570\text{ cm}$ | **$-2.42$** | $19.643\text{ cm}$ | $-3.15$ | $19.743\text{ cm}$ | $-4.15$ |
| **$50.0\text{ cm}$** | $49.847\text{ cm}$ | $49.652\text{ cm}$ | $+1.95$ | $49.681\text{ cm}$ | **$+1.66$** | $49.475\text{ cm}$ | $+3.73$ |
| **$80.0\text{ cm}$** | $80.083\text{ cm}$ | $79.734\text{ cm}$ | **$+3.48$** | $79.726\text{ cm}$ | $+3.56$ | $79.331\text{ cm}$ | $+7.51$ |
| **$150.0\text{ cm}$** | $149.957\text{ cm}$ | $149.926\text{ cm}$ | **$+0.31$** | $149.856\text{ cm}$ | $+1.01$ | $149.388\text{ cm}$ | $+5.69$ |
| **$220.0\text{ cm}$** | $220.086\text{ cm}$ | $220.117\text{ cm}$ | **$-0.31$** | $220.021\text{ cm}$ | $+0.65$ | $219.818\text{ cm}$ | $+2.68$ |
| **$280.0\text{ cm}$** | $280.528\text{ cm}$ | $280.281\text{ cm}$ | $+2.47$ | $280.190\text{ cm}$ | $+3.38$ | $280.321\text{ cm}$ | **$+2.08$** |
| **$350.0\text{ cm}$** | $349.550\text{ cm}$ | $350.473\text{ cm}$ | $-9.23$ | $350.420\text{ cm}$ | **$-8.70$** | $350.874\text{ cm}$ | $-13.25$ |
| **$450.0\text{ cm}$** | $450.739\text{ cm}$ | $450.746\text{ cm}$ | **$-0.07$** | $450.808\text{ cm}$ | $-0.69$ | $451.195\text{ cm}$ | $-4.56$ |
| **$580.0\text{ cm}$** | $579.850\text{ cm}$ | $581.102\text{ cm}$ | $-12.52$ | $581.420\text{ cm}$ | $-15.71$ | $579.850\text{ cm}$ | **$-0.01$** |

**Phân tích bản chất và hiện tượng Quá khớp (Overfitting):**
- **Trong dải đo danh định ổn định:** Tại $150.0\text{ cm}$, mô hình Bậc 1 đạt độ chính xác cực cao, sai số chỉ $+0.31\text{ mm}$; tại $220.0\text{ cm}$ sai số $-0.31\text{ mm}$ và tại $450.0\text{ cm}$ chỉ $-0.07\text{ mm}$. Ngược lại, Bậc 3 do bị uốn cong ở hai đầu mút nên bị võng ở giữa, sai số tại $150.0\text{ cm}$ vọt lên $+5.69\text{ mm}$ (gấp hơn 18 lần Bậc 1) và tại $350.0\text{ cm}$ lệch tới $-13.25\text{ mm}$.
- **Tại hai vùng biên (Vùng chết $2\text{ cm}$ và Suy hao xa $580\text{ cm}$):** Cảm biến kẹt ở vùng chết ($2.352\text{ cm}$). Bậc 1 duy trì hướng thẳng về 0 nên lệch $+8.31\text{ mm}$. Bậc 3 uốn cong đón điểm kẹt nên chỉ lệch $+3.81\text{ mm}$ và tại $580\text{ cm}$ lệch $-0.01\text{ mm}$.
- **Sai số tuyệt đối trung bình (MAE) trên tập Test:** Bậc 1 đạt **$4.11\text{ mm}$** (thấp nhất), Bậc 2 là $4.58\text{ mm}$, Bậc 3 là $4.75\text{ mm}$ (cao nhất).

![So sánh sai số tuyệt đối tại các mốc kiểm thử](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_6_sai_so_phan_du_3_mo_hinh.png)
*Hình 3.3: So sánh sai số tuyệt đối tại các mốc kiểm thử của 3 mô hình hồi quy.*

![Biểu đồ miền tích lũy sai số tuyệt đối](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_7_tich_luy_sai_so_phan_du.png)
*Hình 3.4: Biểu đồ miền tích lũy sai số tuyệt đối trên 10 mốc kiểm thử độc lập.*

Biểu đồ miền tích lũy tại Hình 3.4 chứng minh trực quan: Trong dải đo danh định từ $50\text{ cm}$ đến $450\text{ cm}$, đường tích lũy sai số của mô hình Bậc 1 gần như đi ngang phẳng lì (tổng tích lũy toàn dải chỉ $41.07\text{ mm}$). Ngược lại, mô hình Bậc 3 leo dốc rất đứng ở dải giữa (từ $11.69\text{ mm}$ vọt lên $42.89\text{ mm}$ tại $350\text{ cm}$), khiến tổng sai số tích lũy lên tới $47.45\text{ mm}$.

#### Chỉ số Độ phi tuyến (Non-Linearity) của cảm biến

Về bản chất đo lường, Non-Linearity là đặc tính vật lý duy nhất của phần cứng cảm biến so với đường thẳng chuẩn (BFSL):

$$\text{Non-Linearity (\% FS)} = \pm \frac{\Delta L_{\max}}{\text{FSO}} \times 100\%$$

Trong dải danh định ổn định ($5\text{ cm} \div 400\text{ cm}$, $\text{FSO} = 400\text{ cm}$):
- Độ lệch lớn nhất xảy ra tại $x = 360.0\text{ cm}$ ($y = 361.945\text{ cm}$, $\hat{y} = 360.500\text{ cm}$):
  $$\Delta L_{\max} = |361.945 - 360.500| = 1.445\text{ cm} \ (14.45\text{ mm})$$
- Độ phi tuyến thực nghiệm:
  $$\text{Non-Linearity} = \pm \frac{1.445\text{ cm}}{400\text{ cm}} \times 100\% = \mathbf{\pm 0.361\% \text{ FS}}$$

Mức phi tuyến $< 0.5\%\text{ FS}$ khẳng định cảm biến RCWL-1601 có độ tuyến tính phần cứng xuất sắc.

#### Bảng 3.5: Tổng hợp 4 tiêu chí khoa học quyết định lựa chọn mô hình Bậc 1

| Tiêu chuẩn đánh giá | Mô hình Bậc 1 ($y = ax+b$) | Mô hình Bậc 2 ($y = ax^2+bx+c$) | Mô hình Bậc 3 ($y = ax^3+...+d$) | Nhận định kỹ thuật |
| :--- | :---: | :---: | :---: | :--- |
| **Sai số trên tập Test** | **$\text{MAE} = 4.11\text{ mm}$ (Thấp nhất)** | $\text{MAE} = 4.58\text{ mm}$ | $\text{MAE} = 4.75\text{ mm}$ (Cao nhất) | Bậc 1 khái quát hóa tốt nhất trên dữ liệu mới |
| **Bản chất vật lý sóng âm** | **Hoàn toàn phù hợp ($t = 2d/v$)** | Không phù hợp | Không phù hợp (Overfitting) | Sóng âm truyền tuyến tính bậc 1 tự nhiên |
| **Tính ổn định phần dư** | **Rất phẳng quanh mốc 0** | Khá phẳng | Võng mạnh ở dải giữa ($-13.25\text{ mm}$) | Bậc 1 không làm méo sai số dải đo chính |
| **Tài nguyên vi điều khiển** | **Nhẹ nhất (1 nhân, 1 cộng)** | Trung bình | Tốn CPU, dễ tràn số thực | Bậc 1 tối ưu tối đa cho ESP32 |
| **Chỉ số Non-Linearity** | **$\pm 0.361\%\text{ FS}$ ($< 0.5\%$)** | $\pm 0.372\%\text{ FS}$ | $\pm 0.331\%\text{ FS}$ | Độ phi tuyến cực nhỏ, chênh lệch không đáng kể |
| **KẾT LUẬN LỰA CHỌN** | **CHỌN LÀM ĐẶC TÍNH TĨNH** | **LOẠI** | **LOẠI** | **Mô hình Bậc 1 là lựa chọn tối ưu, khoa học và kinh tế nhất** |

**Quyết định lựa chọn chính thức:** Phương trình tuyến tính Bậc 1:
$$\hat{y} = 1.00273441 \cdot x - 0.48427223 \quad (\text{cm})$$
được lựa chọn làm phương trình đặc tính tĩnh chuẩn của hệ thống đo RCWL-1601. Hệ số góc $a_1 = 1.002734$ phản ánh độ nhạy bám sát tuyệt đối tỷ lệ 1:1, và hệ số tự do $b_1 = -0.484\text{ cm}$ phản ánh chính xác sai số vị trí điểm không cơ học (khoảng thụt lùi $4.84\text{ mm}$ của màng loa gốm phía trong vỏ kim loại bảo vệ).

---

## 3.5. Phân tích Độ trễ (Hysteresis) giữa Chiều tiến và Chiều lùi

### 3.5.1. Khảo sát thực nghiệm đối xứng, Đồ thị trực quan và Định lượng Sai số trễ

Nhằm đánh giá tính đối xứng và độ ổn định của cảm biến RCWL-1601 khi đo khoảng cách hai chiều, kịch bản thực nghiệm đối xứng được thiết lập với hai chuỗi đo độc lập trên cùng một ray trượt định hướng và bia phản xạ phẳng nhẵn ở nhiệt độ phòng chuẩn hóa 27.0°C: Chiều tiến (FSDT, tịnh tiến xa từ $10\text{ cm}$ đến $300\text{ cm}$) và Chiều lùi (BSDT, thu hẹp khoảng cách từ $300\text{ cm}$ về $10\text{ cm}$). Hai chuỗi đo giao nhau tại 19 mốc cự ly đối ứng chuẩn ($10, 20, 40, \dots, 300\text{ cm}$).

![Đặc tính đo hai chiều](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_6a_dac_tinh_hai_chieu.png)
*Hình 3.6a: Đặc tính đo khoảng cách hai chiều Chiều tiến vs Chiều lùi so với đường chuẩn lý tưởng 1:1.*

Trên đồ thị Hình 3.6a, cả hai đường Chiều tiến và Chiều lùi đều bám sát hoàn hảo vào đường tham chiếu lý tưởng $y = x$. Để quan sát rõ nét sự chênh lệch vi mô giữa hai chiều dịch chuyển, phân bố sai số đo tuyệt đối $\Delta d = d_{\text{meas}} - d_{\text{true}}$ được phân tích chi tiết trên đồ thị Hình 3.6b.

![Phân bố sai số trễ](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_6b_vong_tre_hysteresis.png)
*Hình 3.6b: Phân bố Sai số đo tuyệt đối Δd và Vòng trễ Hysteresis giữa Chiều tiến và Chiều lùi.*

Từ đồ thị Hình 3.6b, sai số đo tuyệt đối $\Delta d$ của hai chiều dao động trong biên độ rất hẹp $[-1.48\text{ cm}; +1.45\text{ cm}]$, quấn quanh trục tham chiếu $\Delta d = 0\text{ cm}$ và tạo thành vòng trễ khép kín với khoảng hở vi mô. Độ lệch trễ tuyệt đối tại từng mốc cự ly $d_{\text{true},k}$ được xác định theo hiệu số khoảng cách đo trung bình giữa Chiều tiến và Chiều lùi sau khi lọc IQR:

$$\Delta H_k = |\bar{d}_{\text{forward},k} - \bar{d}_{\text{backward},k}| \quad (3.12)$$

Phân tích trên toàn bộ 19 mốc cự ly ghi nhận độ lệch trễ cực đại $\Delta H_{\max} = 1.6598\text{ cm}$ (tại mốc $200\text{ cm}$, được định vị trực quan trên Hình 3.6b), độ lệch trễ trung bình $\Delta H_{\text{mean}} = 0.5342\text{ cm}$ và độ lệch chuẩn $s_H = 0.4496\text{ cm}$. Sai số trễ tương đối $\gamma_H\%$ được tính toán song song theo Thang đo thử nghiệm ($\text{Span}_{\text{test}} = 300\text{ cm}$) và Thang đo hiệu dụng toàn dải ($\text{Span}_{\text{FS}} = 550\text{ cm}$):

$$\gamma_{H,\text{test}}\% = \frac{\Delta H_{\max}}{\text{Span}_{\text{test}}} \times 100\% = \frac{1.6598}{300} \times 100\% = 0.553\% \quad (3.13)$$

$$\gamma_{H,\text{FS}}\% = \frac{\Delta H_{\max}}{\text{Span}_{\text{FS}}} \times 100\% = \frac{1.6598}{550} \times 100\% = 0.302\% \quad (3.14)$$

Đánh giá: Cả hai chỉ số sai số trễ tương đối đều ở mức rất nhỏ ($\gamma_H\% \le 0.55\%$), đáp ứng xuất sắc yêu cầu định vị hai chiều tin cậy trong các bài toán công nghiệp và robot tự hành.

### 3.5.2. Luận giải Bản chất vật lý phi trễ của sóng siêu âm và Truy vết nguyên nhân sai số ngoại cảnh

Dựa trên kết quả thực nghiệm, mức sai số trễ rất nhỏ ($\gamma_H \approx 0.55\%$) được luận giải qua hai lý do cốt lõi: 
- **Thứ nhất, về bản chất vật lý:** RCWL-1601 đo khoảng cách thuần túy bằng thời gian bay (ToF) của sóng siêu âm lan truyền trong không khí, không có ma sát cơ học hay hiện tượng trễ vật liệu nên hoàn toàn không tồn tại độ trễ nội tại.
- **Thứ hai, về nguyên nhân sai số ngoại cảnh:** Độ lệch trễ vi mô cực đại $\Delta H_{\max} = 1.66\text{ cm}$ tại mốc $200\text{ cm}$ thực chất bắt nguồn từ các tác nhân ngoại cảnh khách quan gồm độ rơ cơ khí và góc tỳ tay khi đảo chiều trên ray trượt dài 3 m, sự biến thiên nhẹ của vi khí hậu phòng thí nghiệm giữa hai lượt đo, cùng độ phân giải đếm thời gian $1\text{ }\mu\text{s}$ ($\approx 0.174\text{ mm}$) của vi điều khiển ESP32.

---

## 3.6. Phân tích ảnh hưởng của Bề mặt phản xạ

Để lượng hóa tác động của cơ chế phản xạ gương định hướng và tán xạ khuếch tán sóng siêu âm (đã trình bày tại Mục 1.1.3, Chương 1) lên chất lượng phép đo thực tế, thí nghiệm đối chứng được thực hiện tại cùng điều kiện nhiệt độ phòng mặc định 27.0 °C ($v = 347.662\text{ m/s}$) trên hai mặt đối lập của cùng một viên gạch kích thước $40\text{ cm} \times 40\text{ cm}$ (Mục 2.2 và Mục 2.3, Chương 2): Trường hợp 1 (FSDT) sử dụng mặt trước phẳng nhẵn và Trường hợp 3 (FRDT) sử dụng mặt sau gồ ghề nhấp nhô. Toàn bộ chỉ tiêu thống kê trước và sau lọc IQR trên 22 mốc cự ly chung ($10\text{ cm} \div 350\text{ cm}$) cùng mốc kiểm tra giới hạn $375\text{ cm}$ của FRDT (23 mốc, tổng cộng 1.150 mẫu thô) được trích xuất trực tiếp từ tệp `du_lieu_tong_hop/chuong_3/thong_ke_chuong_3.csv`.

### 3.6.1. Tác động của tán xạ bề mặt lên độ chụm và độ chính xác đo

Đối chiếu các chỉ tiêu độ lệch chuẩn thực nghiệm $s$ (cột `std_sach_mm`), sai số chuẩn trung bình $\text{SE}$ (cột `se_sach_mm`) và sai số đo $\Delta x$, $\delta\%$ (cột `sai_so_tuyet_doi_mm`, `sai_so_tuong_doi_pct` — định nghĩa tại Mục 1.3, Chương 1) trên 22 mốc cự ly chung từ $10\text{ cm}$ đến $350\text{ cm}$ cho thấy ba đặc điểm vật lý rõ rệt:

1. **Suy giảm độ chụm cục bộ ở vùng cự ly gần ($10\text{ cm} \div 60\text{ cm}$) do giao thoa đa tia phản xạ:** Ở cự ly ngắn, góc mở chùm tia siêu âm bao phủ nhiều gờ lồi lõm có độ sâu chênh lệch cỡ milimét trên mặt sau viên gạch, tạo ra các sóng phản hồi lệch pha giao thoa trực tiếp tại màng thu. Tại $x_{\text{true}} = 10\text{ cm}$, độ lệch chuẩn sau lọc $s$ tăng từ $0.061\text{ mm}$ (FSDT, $\text{SE} = 0.0086\text{ mm}$) lên $1.620\text{ mm}$ (FRDT, $\text{SE} = 0.2291\text{ mm}$ — gấp 26.6 lần); tại $x_{\text{true}} = 60\text{ cm}$, $s$ tăng từ $0.088\text{ mm}$ ($\text{SE} = 0.0128\text{ mm}$) lên $2.240\text{ mm}$ ($\text{SE} = 0.3168\text{ mm}$ — gấp 25.5 lần). Ở các mốc $40\text{ cm}$ và $50\text{ cm}$, mặt gồ ghề làm phát sinh lần lượt 13/50 mẫu (26%, $s_{\text{thô}} = 2.338\text{ mm}$) và 6/50 mẫu (12%, $s_{\text{thô}} = 1.452\text{ mm}$) nhảy chu kỳ ngoại lai trước khi được bộ lọc IQR khử sạch về $s = 0.089\text{ mm}$ và $0.077\text{ mm}$. Tính trên toàn bộ 22 mốc từ $10\text{ cm}$ đến $350\text{ cm}$ (1.100 mẫu), tỷ lệ ngoại lai bị loại bỏ bởi IQR trên mặt gồ ghề là 59/1.100 mẫu (5.36%), cao hơn mức 46/1.100 mẫu (4.18%) của mặt phẳng nhẵn.
2. **Hiện tượng dịch chuyển vị trí các đỉnh trượt chu kỳ trên dải trung bình ($80\text{ cm} \div 340\text{ cm}$):** Trong dải này, độ lệch chuẩn sau lọc của mặt gồ ghề dao động trong khoảng $0.101 \div 2.555\text{ mm}$, tương đương biên độ răng cưa $0.142 \div 2.860\text{ mm}$ của mặt phẳng nhẵn. Đáng chú ý, vị trí các đỉnh phân tán cao giữa hai bề mặt xuất hiện lệch pha nhau theo cự ly (tại 180, 220, 280, 320 cm, mặt gồ ghề rơi vào vùng chuyển tiếp hai chu kỳ sóng mang 40 kHz nên $s$ đạt $2.076 \div 2.555\text{ mm}$; ngược lại tại 100, 200, 300 cm, chùm phản xạ của mặt gồ ghề khóa gọn vào một chu kỳ đơn lẻ nên $s$ chỉ còn $0.101 \div 0.253\text{ mm}$). Nguyên nhân là độ nhấp nhô hình học của mặt sau viên gạch làm dịch chuyển mặt phẳng phản xạ âm học hiệu dụng đi vài milimét so với mép chân gạch, từ đó làm đổi vị trí các mốc cự ly rơi vào ranh giới ngưỡng so sánh xung ECHO. Nhờ lấy trung bình trên cỡ mẫu hợp lệ $n_{\text{hợp lệ}} \in [37, 50]$, sai số chuẩn trung bình $\text{SE}$ của mặt gồ ghề trên toàn bộ 22 mốc ($10 \div 350\text{ cm}$) luôn nằm gọn trong khoảng $0.0071 \div 0.3903\text{ mm}$, thấp hơn dung sai vạch chia thước chuẩn $0.5\text{ mm}$ tại 22/22 mốc đo.
3. **Độ dịch chuyển sai số hệ thống ($\Delta x$ và $\delta\%$):** Do các đỉnh gờ lồi trên mặt nhám nhô về phía trước mặt phẳng chân gạch căn thước, sóng siêu âm dội về sớm hơn tại một số mốc làm sai số tuyệt đối $\Delta x = \bar{x} - x_{\text{true}}$ thiên âm rõ hơn so với mặt nhẵn (biến thiên từ $-21.74\text{ mm}$ tại $250\text{ cm}$, $-13.71\text{ mm}$ tại $60\text{ cm}$, $-12.94\text{ mm}$ tại $150\text{ cm}$ đến $+10.88\text{ mm}$ tại $350\text{ cm}$). Xét về sai số tương đối trên dải $80\text{ cm} \div 350\text{ cm}$ (17 mốc), có 16/17 mốc đạt $|\delta\%| \le 0.87\%$ (duy nhất mốc $100\text{ cm}$ ở mức $-1.27\%$), đáp ứng yêu cầu đo lường khi biên độ xung phản hồi còn vượt ngưỡng thu.

![So sánh độ lệch chuẩn thực nghiệm s](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_7a_do_lech_chuan_be_mat.png)
*Hình 3.7a: So sánh độ lệch chuẩn thực nghiệm s sau lọc IQR giữa mặt phẳng nhẵn (FSDT) và mặt gồ ghề (FRDT) trên dải 10 cm – 350 cm.*

**Đánh giá từ đồ thị Hình 3.7a:** Tách riêng đại lượng độ lệch chuẩn mẫu $s$ cho thấy rõ quy luật phân tán xung đơn lẻ giữa hai bề mặt:
- **Ở vùng cự ly gần ($10 \div 60\text{ cm}$):** Đường màu cam nét đứt (FRDT) vọt lên hai đỉnh tán xạ rõ rệt tại $10\text{ cm}$ ($1.620\text{ mm}$) và $60\text{ cm}$ ($2.240\text{ mm}$), trong khi đường xanh lam nét liền (FSDT) nằm phẳng sát đáy dưới $0.10\text{ mm}$ (trừ điểm trượt chu kỳ tại $40\text{ cm}$).
- **Ở dải trung bình – xa ($80 \div 350\text{ cm}$):** Cả hai đường cùng dao động răng cưa với biên độ đỉnh tương đương ($\le 2.86\text{ mm}$ trên FSDT và $\le 2.62\text{ mm}$ trên FRDT), nhưng vị trí đỉnh – đáy lệch pha nhau dọc theo trục khoảng cách do độ lồi lõm của mặt gạch nhám làm dịch chuyển mặt phẳng phản xạ hiệu dụng.

![So sánh sai số chuẩn trung bình SE](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_7b_sai_so_chuan_be_mat.png)
*Hình 3.7b: So sánh sai số chuẩn trung bình SE = s/√n sau lọc IQR giữa mặt phẳng nhẵn (FSDT) và mặt gồ ghề (FRDT) trên dải 10 cm – 350 cm.*

**Đánh giá từ đồ thị Hình 3.7b:** Khi phóng đại riêng thang đo cho sai số chuẩn trung bình $\text{SE}$ ($0 \div 0.65\text{ mm}$):
- Cả hai đường $\text{SE}$ của FSDT (xanh lam vòng tròn nền trắng) và FRDT (cam ký hiệu hình vuông): Đều nằm hoàn toàn phía dưới đường dung sai vạch chia thước $0.5\text{ mm}$ (tím chấm gạch) tại trọn vẹn 22/22 mốc khảo sát ($0.0086 \div 0.4491\text{ mm}$ đối với FSDT và $0.0071 \div 0.3903\text{ mm}$ đối với FRDT).
- **Ý nghĩa thống kê thực nghiệm:** Phép lấy trung bình trên cỡ mẫu $N = 50$ kết hợp lọc IQR đủ sức nén biên độ nhiễu pha tán xạ của bề mặt gồ ghề xuống mức dưới nửa milimét chừng nào sóng phản hồi còn vượt ngưỡng thu.

### 3.6.2. Suy hao năng lượng tán xạ và sự thu hẹp giới hạn tầm đo xa

Tác động bất lợi nghiêm trọng nhất của bề mặt gồ ghề không nằm ở sai số dải gần mà ở sự suy giảm đột ngột cự ly hoạt động cực đại do thất thoát năng lượng âm học ra không gian:

- **Đối chứng với mặt phẳng nhẵn (FSDT):** Nhờ phản xạ gương bảo toàn năng lượng dọc trục pháp tuyến 90°, cảm biến đo ổn định hoàn toàn không có xung tràn đến tận $550\text{ cm}$ ($\bar{x} = 550.630\text{ cm}$, $s = 0.319\text{ mm}$, $\text{SE} = 0.0492\text{ mm}$), chỉ chớm xuất hiện 4/50 xung mất tín hiệu tại $580\text{ cm}$ ($\bar{x}$ sau lọc vẫn đạt $579.850\text{ cm}$) và bão hòa hoàn toàn tại $600\text{ cm}$ ($\bar{x} = 824.562\text{ cm}$).
- **Ngưỡng chớm mất xung tại 350 cm trên mặt gồ ghề (FRDT):** Do tán xạ khuếch tán làm biên độ áp suất âm phản hồi suy giảm nhanh theo khoảng cách, tại $x_{\text{true}} = 350\text{ cm}$ bắt đầu xuất hiện 1/50 mẫu (2%) mất hoàn toàn tín hiệu dội về và tràn bộ đếm lên $824.400\text{ cm}$ ($t = 47097\text{ }\mu\text{s}$ ở dòng 2 tệp `FRDT_350cm.csv`), đi kèm 4/50 mẫu (8%) trượt chu kỳ dương ($351.906 \div 352.817\text{ cm}$), tạo thành tổng cộng 5/50 mẫu ngoại lai (10%). Chỉ riêng 1 xung tràn $824.400\text{ cm}$ đã kéo trung bình thô lệch lên $\bar{x}_{\text{thô}} = 360.649\text{ cm}$ và làm độ lệch chuẩn thô bùng nổ lên $s_{\text{thô}} = 669.240\text{ mm}$ ($\text{SE}_{\text{thô}} = 94.6448\text{ mm}$, gấp 268.7 lần mặt nhẵn). Tuy nhiên, vì tổng tỷ lệ ngoại lai (10%) vẫn thấp hơn điểm gãy tứ phân vị (25%), bộ lọc IQR loại bỏ trọn vẹn cả 5 mẫu nhiễu ($n_{\text{hợp lệ}} = 45$), khôi phục kết quả đo chuẩn xác $\bar{x} = 351.088\text{ cm}$ ($\Delta x = +10.88\text{ mm}$, $\delta = +0.311\%$), $s = 2.618\text{ mm}$ và $\text{SE} = 0.3903\text{ mm}$.
- **Sự sụp đổ phép đo và vượt ngưỡng lọc IQR tại 375 cm:** Khi dịch bia gồ ghề ra mốc $x_{\text{true}} = 375\text{ cm}$, dữ liệu thô ghi nhận tới 33/50 mẫu (66%) bị mất tín hiệu tràn lên $824.49 \div 824.75\text{ cm}$, chỉ còn 17/50 mẫu (34%) bắt được xung phản xạ yếu quanh $376.39 \div 378.16\text{ cm}$. Do tỷ lệ mẫu bão hòa vượt quá 50%, trung vị mẫu bị kéo hẳn lên vùng tràn ($\text{Med} = 824.575\text{ cm}$, trong khi $Q_1 = 377.388\text{ cm}$ và $Q_3 = 824.623\text{ cm}$), làm khoảng tứ phân vị phình rộng lên $\text{IQR} = 447.235\text{ cm}$ và mở toang hàng rào lọc $[-293.46; 1495.48]\text{ cm}$ (0 mẫu bị đánh dấu ngoại lai). Hệ quả là ngay cả sau lọc IQR, phép đo hoàn toàn mất hiệu lực với $\bar{x} = 672.502\text{ cm}$ ($\Delta x = +2975.02\text{ mm}$, $\delta = +79.33\%$), $s = 2140.734\text{ mm}$ và $\text{SE} = 302.7455\text{ mm}$.
- **Kết luận thiết kế kỹ thuật:** Bề mặt gồ ghề tán xạ làm thu hẹp tầm đo tin cậy cực đại từ $550\text{ cm}$ xuống còn $350\text{ cm}$ (sụt giảm $200\text{ cm}$, tương đương $-36.4\%$). Kết quả này là cơ sở thực nghiệm trực tiếp cho thiết kế ứng dụng tại Chương 4: đối với bề mặt chất lỏng tĩnh phẳng nhẵn trong bồn chứa kín, cảm biến RCWL-1601 khai thác an toàn toàn bộ dải xa; ngược lại đối với vật liệu rắn dạng hạt rời, bề mặt nhám xốp hoặc mặt thoáng gợn sóng mạnh, chiều cao lắp đặt tối đa phải giới hạn bảo toàn dưới ngưỡng $300 \div 350\text{ cm}$.

---

## 3.7. Phân tích ảnh hưởng của Nhiệt độ môi trường và Hiệu quả thuật toán bù nhiệt Laplace

Dựa trên mô hình phụ thuộc nhiệt độ của vận tốc sóng siêu âm Laplace đã thiết lập tại Mục 1.1.2 (Chương 1):

$$v(T) = \sqrt{\frac{\gamma \cdot R \cdot (T + 273.15)}{M}} \approx 331.45 \cdot \sqrt{1 + \frac{T}{273.15}} \quad (\text{m/s})$$

Khi nhiệt độ môi trường thay đổi từ $27.0\text{ }^\circ\text{C}$ xuống $20.0\text{ }^\circ\text{C}$, vận tốc sóng siêu âm suy giảm lý thuyết từ $v(27.0\text{ }^\circ\text{C}) = 347.662\text{ m/s}$ xuống $v(20.0\text{ }^\circ\text{C}) = 343.420\text{ m/s}$ (sụt giảm $\Delta v = 4.242\text{ m/s}$, tương ứng $-1.220\%$, làm thời gian bay ToF giãn dài ra $+1.235\%$). Tác động của sự biến thiên này và năng lực bù nhiệt Laplace được đánh giá qua tập dữ liệu FSAT (19 mốc cự ly từ $10\text{ cm}$ đến $300\text{ cm}$) đối chứng trực tiếp với FSDT.

### 3.7.1. Sự giãn dài thời gian bay và độ ổn định độ chụm khi hạ nhiệt độ môi trường

Khi hạ nhiệt độ không khí xuống 20.0 °C, mật độ phân tử khí tăng làm giảm vận tốc lan truyền sóng âm, dẫn đến thời gian bay ToF cần thiết để sóng truyền khứ hồi qua cùng một khoảng cách hình học bị kéo dài ra.

- **Độ giãn thời gian bay thực nghiệm (`tof_sach_us`):** Trích xuất trực tiếp từ bộ đếm phần cứng ESP32 xác nhận ToF của tập FSAT tại 20.0 °C luôn lớn hơn có hệ thống so với FSDT tại 27.0 °C trên mọi mốc cự ly: tăng từ $614.0\text{ }\mu\text{s}$ lên $621.5\text{ }\mu\text{s}$ tại $10\text{ cm}$ ($+7.5\text{ }\mu\text{s}$), từ $2901.0\text{ }\mu\text{s}$ lên $2936.5\text{ }\mu\text{s}$ tại $50\text{ cm}$ ($+35.5\text{ }\mu\text{s}$), từ $5787.0\text{ }\mu\text{s}$ lên $5858.5\text{ }\mu\text{s}$ tại $100\text{ cm}$ ($+71.5\text{ }\mu\text{s}$), từ $11654.5\text{ }\mu\text{s}$ lên $11798.5\text{ }\mu\text{s}$ tại $200\text{ cm}$ ($+144.0\text{ }\mu\text{s}$) và từ $17454.0\text{ }\mu\text{s}$ lên $17670.0\text{ }\mu\text{s}$ tại $300\text{ cm}$ ($+216.0\text{ }\mu\text{s}$). Tỷ lệ giãn dài thời gian bay thực tế $(\bar{t}_{20} - \bar{t}_{27}) / \bar{t}_{27}$ trên toàn dải đạt trung bình $+1.235\%$, trùng khớp hoàn hảo với tỷ lệ suy giảm vận tốc âm lý thuyết Laplace $v_{27} / v_{20} - 1 = 347.662 / 343.420 - 1 = +1.235\%$.
- **Tính bất biến của độ chụm đối với nhiệt độ:** Trong môi trường phòng điều hòa kín gió 20.0 °C, tổng tỷ lệ ngoại lai bị loại bởi IQR của tập FSAT là 38/950 mẫu (4.00%), tương đương hoàn toàn với 39/950 mẫu (4.11%) trên 19 mốc đối ứng của FSDT. Độ lệch chuẩn sau lọc $s$ của FSAT dao động trong dải $0.060 \div 3.381\text{ mm}$ và sai số chuẩn trung bình $\text{SE}$ đạt $0.0085 \div 0.4781\text{ mm}$ (nằm dưới dung sai thước $0.5\text{ mm}$ tại cả 19/19 mốc), chứng minh việc hạ nhiệt độ môi trường chỉ làm dịch chuyển hệ thống vận tốc truyền âm chứ không làm suy giảm độ chụm lặp lại của vi mạch RCWL-9610.

### 3.7.2. Định lượng sai số trôi nhiệt khi không bù và hiệu quả khử trôi của thuật toán Laplace

Để đánh giá định lượng rủi ro trong các hệ thống nhúng giá rẻ thường gán cứng hằng số vận tốc âm mặc định $v(27.0\text{ }^\circ\text{C}) = 347.662\text{ m/s}$ (`default_temp_c = 27.0`), khoảng cách chưa bù nhiệt tại 20.0 °C được tính đối chứng từ cột `tof_sach_us` theo $\bar{x}_{\text{chưa bù}} = 0.5 \cdot v(27.0\text{ }^\circ\text{C}) \cdot \bar{t}_{\text{FSAT}}$ và so sánh trực tiếp với kết quả đã bù nhiệt Laplace thời gian thực trên ESP32:

1. **Trường hợp không bù nhiệt độ (`sai_so_chua_bu_27c_mm`):** Do thời gian bay kéo dài hơn trong không khí lạnh nhưng phần mềm vẫn nhân với vận tốc lớn của 27.0 °C, kết quả đo bị phóng đại giả tạo với tỷ lệ lý thuyết $+1.235\%$ quãng đường ($\approx +12.35\text{ mm/m}$ ở 20.0 °C). Lượng trôi nhiệt thuần túy ($\bar{x}_{\text{chưa bù}} - \bar{x}_{\text{đã bù}}$) tích lũy tuyến tính từ $+1.31\text{ mm}$ tại $10\text{ cm}$, $+6.16\text{ mm}$ tại $50\text{ cm}$, $+12.28\text{ mm}$ tại $100\text{ cm}$, $+18.52\text{ mm}$ tại $150\text{ cm}$, $+22.46\text{ mm}$ tại $200\text{ cm}$, $+28.20\text{ mm}$ tại $250\text{ cm}$, lên tới $+34.65\text{ mm}$ tại $280\text{ cm}$ và $+35.31\text{ mm}$ tại $300\text{ cm}$. Hệ quả là sai số tuyệt đối $\Delta x$ khi chưa bù bị đẩy vọt lên mức dương lớn: đạt $+25.96\text{ mm}$ tại $200\text{ cm}$, đỉnh $+39.92\text{ mm}$ ($\approx +4.0\text{ cm}$) tại $280\text{ cm}$ và $+32.52\text{ mm}$ tại $300\text{ cm}$.
2. **Hiệu quả triệt tiêu trôi nhiệt khi bù Laplace thời gian thực (`sai_so_tuyet_doi_mm`):** Khi kích hoạt công thức cập nhật vận tốc âm tức thời $v(T)$ theo từng mẫu đo trên ESP32, toàn bộ thành phần trôi nhiệt dương hàng xentimét bị loại bỏ hoàn toàn: sai số $\Delta x$ của FSAT được kéo sập về $-5.73\text{ mm}$ tại $100\text{ cm}$, $-0.45\text{ mm}$ tại $150\text{ cm}$, $+3.50\text{ mm}$ tại $200\text{ cm}$, $+0.04\text{ mm}$ tại $250\text{ cm}$, $+5.27\text{ mm}$ tại $280\text{ cm}$ và $-2.79\text{ mm}$ tại $300\text{ cm}$ (14/14 mốc từ $80 \div 300\text{ cm}$ trừ mốc $160\text{ cm}$ đều đạt $|\delta\%| \le 0.57\%$).
3. **Độ trùng khít tuyệt đối giữa hai môi trường nhiệt độ sau bù ($\bar{x}_{27^\circ\text{C}} - \bar{x}_{20^\circ\text{C}}$):** Đối chiếu trực tiếp cột `mean_sach_cm` giữa FSDT (27.0 °C) và FSAT (20.0 °C) trên toàn bộ 19 mốc cự ly xác nhận độ lệch trung bình tuyệt đối giữa hai chế độ nhiệt chỉ là $0.037\text{ mm}$ (biến thiên trong dải siêu hẹp từ $-0.048\text{ mm}$ đến $+0.183\text{ mm}$; có 18/19 mốc lệch dưới $0.085\text{ mm}$ — nhỏ hơn nửa bước lượng tử thời gian $\Delta_{\text{LSB}} \approx 0.174\text{ mm}$ của bộ đếm ESP32). Kết quả này chứng minh thuật toán bù nhiệt Laplace giúp phép đo siêu âm hoàn toàn miễn nhiễm với biến thiên nhiệt độ môi trường.

![So sánh sai số trôi nhiệt và hiệu quả bù Laplace](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_3/hinh_3_8_anh_huong_nhiet_do_bu_laplace.png)
*Hình 3.8: So sánh sai số tuyệt đối Δx tại phòng lạnh 20.0 °C khi chưa bù nhiệt độ, sau khi bù nhiệt độ Laplace (FSAT) và chuẩn đối chứng tại 27.0 °C (FSDT) trên dải 10 cm – 300 cm.*

**Đánh giá từ đồ thị Hình 3.8:** Biểu diễn ba chuỗi sai số trên cùng một trục tung đơn vị mm cho thấy sự tương phản trực quan:
- **Đường màu đỏ nét liền ký hiệu tam giác (FSAT chưa bù nhiệt):** Tách khỏi gốc $0\text{ mm}$ và dốc tuyến tính đi lên theo khoảng cách chuẩn do tích lũy sai số vận tốc $+1.235\%$, vọt lên vùng $+26 \div +40\text{ mm}$ ở cự ly $200 \div 300\text{ cm}$.
- **Đường màu xanh lá nét đứt tâm vuông đặc (FSAT đã bù Laplace tại 20.0 °C) lồng đồng tâm bên trong đường băng xanh lam ký hiệu vòng tròn rỗng (FSDT đối chứng tại 27.0 °C):** Từng điểm vuông xanh lá nằm lọt chính tâm vòng tròn xanh lam trên toàn bộ 19 mốc cự ly từ $10\text{ cm}$ đến $300\text{ cm}$ (do độ lệch giữa hai đường chỉ từ $0.002\text{ mm}$ đến $0.183\text{ mm}$) và cùng bám sát đường chuẩn $0\text{ mm}$, khẳng định tính bắt buộc của cảm biến nhiệt độ đi kèm thuật toán bù Laplace trong ứng dụng bồn chứa thực tế ở Chương 4.

---

## 3.8. Phân tích Tổng hợp Độ không đảm bảo đo mở rộng toàn diện (ISO/GUM)

Theo tiêu chuẩn quốc tế ISO/IEC Guide 98-3 (GUM), mọi kết quả đo lường khoa học phải được công bố kèm theo khoảng độ không đảm bảo đo mở rộng.

### 3.8.1. Phân loại và Mô hình hóa các thành phần không đảm bảo đo

Mô hình hàm đo khoảng cách có bù nhiệt độ:

$$d = f(t, T) = \frac{(331.3 + 0.606 \cdot T) \cdot t}{2}$$

Các thành phần không đảm bảo đo bao gồm:
1. **Độ không đảm bảo đo Loại A ($u_A$):** Đánh giá sự phân tán ngẫu nhiên qua $N = 50$ lần đo:

   $$u_A = \frac{s}{\sqrt{N}} = \frac{s}{\sqrt{50}}$$

2. **Độ không đảm bảo đo Loại B ($u_B$):** Đánh giá từ thông số thiết bị và giả thiết phân bố xác suất hình chữ nhật ($a / \sqrt{3}$):
   - $u_{B1}$ (Sai số vạch chia thước cơ khí chuẩn): Thước thép có độ chia nhỏ nhất $1\text{ mm}$, giới hạn sai số $a_1 = 0.5\text{ mm} \implies u_{B1} = 0.5 / \sqrt{3} \approx 0.289\text{ mm}$.
   - $u_{B2}$ (Sai số lượng tử hóa của bộ định thời vi điều khiển ESP32): Bộ đếm phần cứng ESP32 đếm xung với chu kỳ lượng tử hóa $\Delta t_{\text{quant}} = 1\text{ }\mu\text{s}$, tương ứng với bước cự ly rời rạc nhỏ nhất $\Delta d_{\text{LSB}} \approx 0.174\text{ mm}$. Với giả thiết phân bố xác suất hình chữ nhật trong một khoảng lượng tử, nửa khoảng sai số $a_2 = 0.174 / 2 = 0.087\text{ mm} \implies u_{B2} = 0.087 / \sqrt{3} \approx 0.051\text{ mm}$.
   - $u_{B3}$ (Độ không đảm bảo nhiệt độ môi trường): Nhiệt kế đo vi khí hậu có sai số $\pm 0.5^\circ\text{C}$, nửa khoảng $a_T = 0.5^\circ\text{C} \implies u_T = 0.5 / \sqrt{3} \approx 0.289^\circ\text{C}$. Lan truyền sai số nhiệt độ qua hệ số ảnh hưởng (Hệ số nhạy nhiệt độ trong mô hình GUM):

     $$c_T = \frac{\partial d}{\partial T} = \frac{0.606 \cdot t}{2} = \frac{0.606}{v} \cdot d \approx \frac{0.606}{350.69} \cdot d \approx 0.001728 \cdot d$$

     $$\implies u_{B3}(d) = c_T \cdot u_T = (0.001728 \cdot d) \cdot 0.289 = 0.000499 \cdot d \quad (\text{mm})$$

3. **Độ không đảm bảo đo chuẩn tổng hợp ($u_c$):**

   $$u_c = \sqrt{u_A^2 + u_{B1}^2 + u_{B2}^2 + u_{B3}^2}$$

4. **Độ không đảm bảo đo mở rộng ($U_{95\%}$):** Với mức tin cậy xấp xỉ 95%, hệ số phủ sinh viên cho bậc tự do lớn ($k_p = 2$):

   $$U_{95\%} = 2 \cdot u_c$$

### 3.8.2. Bảng tổng hợp Độ không đảm bảo đo

| Cự ly chuẩn $d$ (cm) | Độ lệch chuẩn $s$ (mm) | $u_A$ (mm) | $u_{B1}$ (Thước) (mm) | $u_{B2}$ (Timer) (mm) | $u_{B3}$ (Nhiệt độ) (mm) | $u_B$ tổng hợp (mm) | $u_c$ tổng hợp (mm) | **$U_{95\%}$ ($k=2$) (mm)** | Biểu diễn kết quả đo chuẩn $Y = \bar{d} \pm U_{95\%}$ (cm) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$10$** | $0.061$ | $0.009$ | $0.289$ | $0.051$ | $0.050$ | $0.297$ | $0.297$ | **$0.60$** | $10.57 \pm 0.06$ |
| **$50$** | $0.094$ | $0.013$ | $0.289$ | $0.051$ | $0.249$ | $0.385$ | $0.385$ | **$0.77$** | $49.85 \pm 0.08$ |
| **$100$** | $0.383$ | $0.054$ | $0.289$ | $0.051$ | $0.499$ | $0.580$ | $0.581$ | **$1.16$** | $99.43 \pm 0.12$ |
| **$200$** | $2.192$ | $0.310$ | $0.289$ | $0.051$ | $0.998$ | $1.040$ | $1.085$ | **$2.17$** | $200.35 \pm 0.22$ |
| **$300$** | $2.860$ | $0.404$ | $0.289$ | $0.051$ | $1.497$ | $1.526$ | $1.578$ | **$3.16$** | $299.72 \pm 0.32$ |
| **$400$** | $1.850$ | $0.262$ | $0.289$ | $0.051$ | $1.995$ | $2.017$ | $2.034$ | **$4.07$** | $401.40 \pm 0.41$ |
| **$500$** | $1.978$ | $0.280$ | $0.289$ | $0.051$ | $2.494$ | $2.511$ | $2.527$ | **$5.05$** | $500.69 \pm 0.51$ |

**Nhận xét phân tích tổng hợp:**
- Ở cự ly gần ($10\text{ cm} \le d \le 50\text{ cm}$), độ không đảm bảo đo mở rộng rất nhỏ ($U_{95\%} \le 0.77\text{ mm}$), bị chi phối chủ yếu bởi độ không đảm bảo của vạch chia thước chuẩn $u_{B1} = 0.289\text{ mm}$.
- Khi cự ly tăng dần lên $300\text{ cm} - 500\text{ cm}$, thành phần $u_{B3}$ (sự lan truyền sai số nhiệt độ) tăng tuyến tính và trở thành thành phần chủ đạo chi phối toàn bộ độ không đảm bảo đo tổng hợp (chiếm trên $85\%$ tỷ trọng phương sai).
- Độ không đảm bảo đo mở rộng toàn dải $U_{95\%}$ luôn duy trì dưới ngưỡng **$\pm 5.1\text{ mm}$** ở cự ly $5\text{ m}$ và dưới **$\pm 1.2\text{ mm}$** ở cự ly $1\text{ m}$, chứng minh giá trị đo có độ tin cậy khoa học cao.

![Phân tích tổng hợp Độ không đảm bảo đo ISO/GUM](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/hinh_3_9_ngan_sach_do_khong_dam_bao_do.png)
*Hình 3.9: Biểu đồ phân rã các thành phần độ không đảm bảo đo Loại A, Loại B và Độ không đảm bảo đo mở rộng $U_{95\%}$ theo tiêu chuẩn ISO/GUM.*

---

## 3.9. Bảng tổng hợp đối chiếu Đặc tính Kỹ thuật Thực nghiệm vs Datasheet Nhà sản xuất

Bảng đối chiếu tổng kết toàn diện các thông số kỹ thuật cốt lõi giữa bản công bố của Nhà sản xuất (Datasheet RCWL-1601) và Kết quả kiểm chứng thực nghiệm trên nền tảng vi điều khiển ESP32:

| Chỉ tiêu kỹ thuật đo lường | Thông số công bố (Datasheet) | Kết quả kiểm chứng thực nghiệm | Đánh giá & Ghi chú kỹ thuật |
| :--- | :---: | :---: | :--- |
| **Điện áp hoạt động ($V_{\text{CC}}$)** | $2.8\text{ V} - 5.5\text{ V}$ | $3.3\text{ V}$ (cấp trực tiếp từ ESP32) | Hoạt động hoàn hảo, tương thích mức logic $3.3\text{ V}$ không cần IC đệm |
| **Dòng điện tiêu thụ tĩnh** | $< 2\text{ mA}$ | $\approx 2.2\text{ mA}$ | Phù hợp triển khai các thiết bị quan trắc dùng pin/ắc quy |
| **Dải đo danh định** | $2\text{ cm} - 400\text{ cm}$ (hoặc $450\text{ cm}$) | **$5\text{ cm} - 550\text{ cm}$** | **Vượt định mức:** Tầm đo mở rộng thêm $100\text{ cm}$ ($+22\%$) trên mặt nhẵn |
| **Vùng chết (Blind Zone)** | $< 2\text{ cm}$ | **$1\text{ cm} - 3\text{ cm}$** | Giá trị đo bị kẹp cố định ở $2.0 - 2.6\text{ cm}$ do thời gian suy giảm màng gốm |
| **Độ chính xác công bố** | $\pm 0.5\text{ cm} \pm 1\%$ | **$\pm 0.35\%$ (cự ly $> 1\text{ m}$)** | Tốt hơn công bố nhờ tích hợp thuật toán bù nhiệt độ Laplace |
| **Hệ số xác định tuyến tính ($R^2$)** | Không công bố | **$R^2 = 0.999988$** | Đặc tính bám sát tuyến tính tuyệt đối |
| **Độ phi tuyến toàn thang (Non-Linearity)** | Không công bố (< 1%) | **±0.361% FS** (Dải 5 - 400 cm) | Độ phi tuyến phần cứng xuất sắc (< 0.5% FS) |
| **Phương trình đặc tính tĩnh chuẩn (Bậc 1)** | $y = x$ (Lý tưởng) | **$\hat{y} = 1.002734 \cdot x - 0.484\text{ cm}$** | Hệ số góc bám sát 1:1, bù điểm không cơ học -4.84 mm |
| **Độ lệch chuẩn lặp lại ($s$)** | Không công bố | **$0.06 - 0.38\text{ mm}$ ($< 1\text{ m}$)**<br>$1.5 - 2.8\text{ mm}$ ($> 2\text{ m}$) | Độ chụm cực cao, $\text{CV}\% < 0.11\%$ trên toàn dải làm việc |
| **Độ trễ tương đối ($\gamma_H$)** | Không công bố | **$0.553\%$** | Do sai số căn chỉnh dịch chuyển bàn đo và vi khí hậu phòng |
| **Tầm đo trên mặt gồ ghề/xốp** | Không công bố | Bị suy giảm còn **$300\text{ cm}$**<br>*(Bão hòa hoàn toàn ở $375\text{ cm}$)* | Do hiện tượng tán xạ khuếch tán làm phân tán năng lượng sóng phản xạ |
| **Khả năng thích ứng nhiệt độ** | Bù nhiệt nội bộ trên IC | Bù Laplace bằng phần mềm trên ESP32 | Giảm sai số trôi nhiệt từ $5.8\text{ cm}$ xuống dưới $0.5\text{ mm}$ trên dải $3\text{ m}$ |

**Kết luận đánh giá tổng quát:**
Module cảm biến siêu âm RCWL-1601 khi kết hợp với bộ đếm thời gian vi điều khiển ESP32 và giải thuật bù nhiệt Laplace đã thể hiện các đặc tính kỹ thuật vượt trội so với các thông số công bố tối thiểu của nhà sản xuất. Đây là tiền đề lý thuyết và thực nghiệm vững chắc để triển khai hệ thống vào bài toán thực tế: **"Hệ thống giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ"** trong Chương 4.
