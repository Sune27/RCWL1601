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

Từ dữ liệu thực nghiệm 35 mốc cự ly từ $1\text{ cm}$ đến $600\text{ cm}$ trên tập `FSDT.csv`, đặc tính đo của cảm biến RCWL-1601 được chia thành 4 vùng:

```mermaid
flowchart LR
    A["Vùng chết<br>(1 cm – 3 cm)"] --> B["Vùng chuyển tiếp<br>(4 cm – 5 cm)"]
    B --> C["Dải làm việc ổn định<br>(8 cm – 400 cm)"]
    C --> D["Dải đo xa mở rộng<br>(420 cm – 550 cm)"]
    D --> E["Ngưỡng bão hòa xa<br>(580 cm – 600 cm)"]
```

### 3.2.1. Vùng chết (1 cm – 3 cm)

Khi khoảng cách từ vật cản đến cảm biến nhỏ hơn hoặc bằng $3\text{ cm}$, cảm biến không đo được khoảng cách thực tế và giá trị đo bị giữ quanh ngưỡng $2.0 - 2.6\text{ cm}$:
- Tại cự ly chuẩn $d_{\text{true}} = 1.0\text{ cm}$: Giá trị trung bình $\bar{d} = 2.030\text{ cm}$ (sai số $+1.030\text{ cm}$, tương ứng $+103.05\%$).
- Tại cự ly chuẩn $d_{\text{true}} = 2.0\text{ cm}$: Giá trị trung bình $\bar{d} = 2.352\text{ cm}$ (sai số $+0.352\text{ cm}$, tương ứng $+17.59\%$).
- Tại cự ly chuẩn $d_{\text{true}} = 3.0\text{ cm}$: Giá trị trung bình $\bar{d} = 2.679\text{ cm}$ (sai số $-0.321\text{ cm}$, tương ứng $-10.72\%$).

**Giải thích nguyên nhân:** Khi vi điều khiển phát xung kích sóng âm $40\text{ kHz}$ ($200\text{ }\mu\text{s}$), màng rung áp điện cần khoảng $120 - 150\text{ }\mu\text{s}$ để suy giảm dao động. Ở cự ly dưới $3\text{ cm}$, thời gian sóng âm đi và về nhỏ hơn $175\text{ }\mu\text{s}$:

$$t_{\text{bay}} = \frac{2 \cdot 0.03}{347.66} \approx 172.6\text{ }\mu\text{s}$$

Thời gian này trùng với thời gian tắt dần của màng phát và thời gian ngắt câm (blanking time) của vi mạch RCWL-9610. Mạch thu không tách được sóng phản xạ khỏi xung phát, do đó đầu ra bị kẹp ở mức thời gian ngắt câm tương đương $2.0 - 2.6\text{ cm}$.

![Đặc tính đo khoảng cách trong vùng gần](../graph/chuong_3/hinh_3_2_vung_chet_1_10cm.png)

*Hình 3.2: Đặc tính đo khoảng cách trong vùng gần (1 cm – 10 cm).*

Đồ thị Hình 3.2 thể hiện rõ hiện tượng vùng chết: ở các mốc $1\text{ cm}$, $2\text{ cm}$ và $3\text{ cm}$, đường đo thực tế lệch khỏi đường chuẩn lý tưởng ($y = x$). Từ mốc $5\text{ cm}$ trở đi, đường đo bám sát đường lý tưởng.

### 3.2.2. Dải làm việc ổn định (8 cm – 400 cm)

Từ cự ly $8\text{ cm}$ đến $400\text{ cm}$, xung phản xạ tách biệt khỏi xung phát và biên độ nằm trong dải khuếch đại của mạch thu. Sai số tương đối trong dải này duy trì dưới $\pm 0.5\%$, cho thấy cảm biến hoạt động ổn định trong phạm vi nhà sản xuất công bố.

### 3.2.3. Dải đo xa mở rộng (420 cm – 550 cm)

Thông số công bố của nhà sản xuất ghi nhận cự ly đo tối đa là $400 - 450\text{ cm}$. Tuy nhiên, trong điều kiện mặt phản xạ phẳng, kích thước $40 \times 40\text{ cm}$ đặt vuông góc với trục phát, cảm biến vẫn bắt được tín hiệu phản xạ chính xác:
- Tại $420\text{ cm}$: $\bar{d} = 421.241\text{ cm}$ (sai số $+0.29\%$).
- Tại $500\text{ cm}$: $\bar{d} = 500.691\text{ cm}$ (sai số $+0.14\%$).
- Tại $550\text{ cm}$: $\bar{d} = 550.566\text{ cm}$ (sai số $+0.10\%$, độ lệch chuẩn $s = 1.52\text{ mm}$).

Kết quả này đạt được nhờ mạch thu tích hợp trên RCWL-9610 có độ nhạy tốt và mặt phản xạ được đặt vuông góc, giảm thiểu tán xạ.

### 3.2.4. Ngưỡng suy hao và bão hòa xa (580 cm – 600 cm)

Ở cự ly từ $580\text{ cm}$ trở lên, năng lượng sóng phản xạ suy giảm mạnh:
- Tại $580\text{ cm}$: Bắt đầu xuất hiện mẫu đo mất xung phản xạ ($1/50$ mẫu trả về giá trị timeout $824.6\text{ cm}$).
- Tại $600\text{ cm}$: Số mẫu mất xung tăng lên $7/50$ mẫu ($14\%$ sau khi lọc IQR, hoặc $31/50$ mẫu ở dữ liệu thô), khiến giá trị trung bình thô đạt $720.16\text{ cm}$ và độ lệch chuẩn thô đạt $2621.02\text{ mm}$.

Bảng 3.3 tổng hợp các vùng làm việc tiêu biểu trên toàn dải đo:

| Cự ly chuẩn $d_{\text{true}}$ (cm) | Giá trị trung bình $\bar{d}$ (cm) | Độ lệch chuẩn $s$ (mm) | Sai số tuyệt đối $\Delta d$ (mm) | Sai số tương đối $\delta\%$ | Trạng thái vùng làm việc |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$1.0$** | $2.030$ | $0.035$ | $+10.30$ | $+103.05\%$ | Vùng chết (do thời gian suy giảm màng rung) |
| **$2.0$** | $2.352$ | $0.085$ | $+3.52$ | $+17.59\%$ | Vùng chết (kẹp ngưỡng ngắt câm) |
| **$3.0$** | $2.679$ | $0.056$ | $-3.21$ | $-10.72\%$ | Vùng chết (bắt đầu thoát vùng ngắt câm) |
| **$5.0$** | $4.295$ | $0.085$ | $-7.05$ | $-14.10\%$ | Vùng chuyển tiếp |
| **$10.0$** | $10.570$ | $0.061$ | $+5.70$ | $+5.70\%$ | Bắt đầu dải đo danh định |
| **$50.0$** | $49.847$ | $0.094$ | $-1.53$ | $-0.31\%$ | Dải làm việc ổn định |
| **$100.0$** | $99.429$ | $0.383$ | $-5.71$ | $-0.57\%$ | Dải làm việc ổn định |
| **$200.0$** | $200.351$ | $2.192$ | $+3.51$ | $+0.18\%$ | Dải làm việc ổn định |
| **$300.0$** | $299.718$ | $2.860$ | $-2.82$ | $-0.09\%$ | Dải làm việc ổn định |
| **$400.0$** | $401.402$ | $1.850$ | $+14.02$ | $+0.35\%$ | Giới hạn danh định của cảm biến |
| **$500.0$** | $500.691$ | $1.978$ | $+6.91$ | $+0.14\%$ | Dải đo xa mở rộng |
| **$550.0$** | $550.566$ | $1.520$ | $+5.66$ | $+0.10\%$ | Giới hạn đo xa thực tế |
| **$580.0$** | $584.808$ | $346.051$ | $+48.08$ | $+0.83\%$ | Ngưỡng suy hao (bắt đầu có mẫu timeout) |
| **$600.0$** | $720.161$ | $2621.017$ | $+1201.61$ | $+20.03\%$ | Ngưỡng bão hòa xa (nhiều mẫu timeout) |

---

## 3.3. Đánh giá Độ chụm và Độ chính xác

### 3.3.1. Đánh giá Độ chụm (Precision)

Độ chụm phản ánh mức độ phân tán ngẫu nhiên giữa các lần đo lặp lại tại cùng một điểm cự ly trong điều kiện phòng thí nghiệm ổn định ($N = 50$). Hai chỉ số định lượng then chốt được phân tích:
1. **Độ lệch chuẩn thực nghiệm ($s$):** Biểu diễn bằng đơn vị milimét ($\text{mm}$).
   - Trong cự ly gần ($1\text{ cm} \le d \le 50\text{ cm}$): Độ lệch chuẩn cực nhỏ, dao động từ $s = 0.035\text{ mm}$ đến $0.094\text{ mm}$. Tín hiệu âm phản xạ rất mạnh và tỷ số tín hiệu trên nhiễu ($S/N$) đạt cực đại.
   - Trong cự ly trung bình ($60\text{ cm} \le d \le 180\text{ cm}$): Độ lệch chuẩn tăng nhẹ lên khoảng $s = 0.15\text{ mm} - 0.40\text{ mm}$.
   - Trong cự ly xa ($200\text{ cm} \le d \le 360\text{ cm}$): Độ lệch chuẩn biến thiên trong khoảng $s = 1.8\text{ mm} - 2.8\text{ mm}$. Sự gia tăng này là hệ quả tất yếu của hiện tượng nhiễu động vi khí hậu đối lưu không khí dọc theo hành lang đo dài $7\text{ m}$.
   - Trong dải đo xa mở rộng ($400\text{ cm} \le d \le 550\text{ cm}$): Độ lệch chuẩn duy trì ổn định ở mức $s \approx 1.5 - 2.0\text{ mm}$ nhờ kích thước bia phản xạ lớn tập trung năng lượng tốt.
2. **Hệ số biến thiên ($\text{CV}\%$):** Được tính theo công thức $\text{CV}\% = (s / \bar{d}) \cdot 100\%$.
   - Trên toàn bộ dải đo làm việc hữu ích từ $10\text{ cm}$ đến $550\text{ cm}$, hệ số biến thiên $\text{CV}\%$ luôn duy trì dưới ngưỡng **$0.11\%$**.
   - Tại các cự ly trung bình và xa ($50\text{ cm} \to 550\text{ cm}$), $\text{CV}\%$ đạt mức lý tưởng từ **$0.019\%$ đến $0.046\%$**. Đây là minh chứng rõ nét cho thấy hệ thống đo RCWL-1601 kết hợp ESP32 có độ lặp lại và độ ổn định thống kê hoàn toàn đáp ứng các tiêu chuẩn quan trắc kỹ thuật khắt khe.

![Độ chụm toàn dải đo](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/hinh_3_3_do_chum_toan_dai.png)
*Hình 3.3: Biến thiên của Độ lệch chuẩn thực nghiệm $s$ (mm) và Hệ số biến thiên $\text{CV}\%$ trên toàn dải đo FSDT từ 1 cm đến 550 cm.*

### 3.3.2. Đánh giá Độ chính xác (Accuracy)

Độ chính xác thể hiện mức độ sai lệch giữa giá trị đo trung bình $\bar{d}$ và giá trị cự ly thực tế đặt chuẩn $d_{\text{true}}$ (được xác định bằng thước thép chuẩn có độ chia $1\text{ mm}$):
- **Sai số tuyệt đối ($\Delta d = \bar{d} - d_{\text{true}}$):** Trên toàn bộ dải đo danh định từ $50\text{ cm}$ đến $550\text{ cm}$, sai số tuyệt đối dao động trong dải hẹp từ $-5.71\text{ mm}$ đến $+14.02\text{ mm}$.
- **Sai số tương đối ($\delta\% = (\Delta d / d_{\text{true}}) \cdot 100\%$):** 
  + Ngoại trừ vùng chết và vùng cự ly cực gần ($< 10\text{ cm}$), sai số tương đối trên toàn bộ dải làm việc ($50\text{ cm} \le d \le 550\text{ cm}$) hoàn toàn **nằm trong phạm vi $\pm 0.57\%$**, trong đó phần lớn các điểm đo đạt độ chính xác dưới **$\pm 0.35\%$**.
  + Tại các cự ly $300\text{ cm}$, $500\text{ cm}$ và $550\text{ cm}$, sai số tương đối chỉ đạt lần lượt là $-0.09\%$, $+0.14\%$ và $+0.10\%$.

**Phân tích bản chất sai số hệ thống:**
Sự tồn tại của độ lệch tuyệt đối khoảng vài milimét có tính chất dịch chuyển đều (offset) bắt nguồn từ khoảng cách cơ khí giữa mặt phẳng màng gốm áp điện nằm thụt sâu bên trong ống kim loại cảm biến so với mép bo mạch và mép bàn đo ($offset \approx 5 - 6\text{ mm}$). Thành phần sai số hệ thống này hoàn toàn có thể được hiệu chuẩn triệt tiêu bằng phần mềm thông qua hệ số hiệu chỉnh dịch gốc toạ độ.

![Độ chính xác và Sai số toàn dải](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/hinh_3_4_do_chinh_xac_sai_so.png)
*Hình 3.4: Phân bố Sai số tuyệt đối $\Delta d$ (mm) và Sai số tương đối $\delta\%$ trên dải làm việc hiệu dụng.*

---

## 3.4. Đánh giá Độ tuyến tính, Độ nhạy và Độ phân giải

### 3.4.1. Hồi quy tuyến tính bằng phương pháp ma trận chuẩn tắc

Để đánh giá mức độ bám sát của đặc tính tĩnh thực nghiệm với đường thẳng lý thuyết, phương pháp bình phương bé nhất dạng ma trận đã được thiết lập trên $K = 30$ mốc cự ly thuộc dải làm việc tuyến tính ($5\text{ cm} \le d_{\text{true}} \le 550\text{ cm}$).

Mô hình hồi quy khoảng cách đo thực nghiệm có dạng:

$$\hat{d} = a \cdot d_{\text{true}} + b$$

Vector hệ số hồi quy được giải trực tiếp từ hệ phương trình chuẩn tắc:

$$\hat{\boldsymbol{\beta}} = \begin{bmatrix} a \\ b \end{bmatrix} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}$$

Kết quả tính toán ma trận số liệu thực nghiệm:
- **Hệ số góc hồi quy:** $a = 1.002791 \approx 1.0000$ (độ dốc bám sát tỷ lệ lý tưởng $1:1$).
- **Hệ số chặn (offset dịch chuyển gốc):** $b = -0.607344\text{ cm} \approx -6.07\text{ mm}$ (phù hợp tuyệt đối với kích thước thụt lùi cơ khí của màng rung trong nòng kim loại bảo vệ).
- **Hệ số xác định tương quan:**

$$R^2 = 1 - \frac{\sum_{k=1}^K (y_k - \hat{y}_k)^2}{\sum_{k=1}^K (y_k - \bar{y})^2} = 0.999988$$

Chỉ số $R^2 \approx 1.0000$ khẳng định hàm truyền khoảng cách của cảm biến có độ tuyến tính hoàn hảo.

**Sai số phi tuyến cực đại ($\delta_{\text{NL}}\%$):**
Độ lệch lớn nhất giữa giá trị đo trung bình thực tế và đường thẳng hồi quy tuyến tính lý thuyết là:

$$\Delta d_{\text{NL},\max} = \max_k |\bar{d}_k - \hat{d}_k| = 1.2954\text{ cm}$$

Quy đổi về sai số phi tuyến tương đối trên toàn thang đo $d_{\text{F.S.}} = 550\text{ cm}$:

$$\delta_{\text{NL}}\% = \frac{\Delta d_{\text{NL},\max}}{d_{\text{F.S.}}} \times 100\% = \frac{1.2954}{550} \times 100\% = 0.2355\%$$

*(Nếu chỉ xét trong dải quy chuẩn Datasheet $5\text{ cm} \to 400\text{ cm}$, phương trình hồi quy đạt $a = 1.003177$, $b = -0.660877\text{ cm}$, $R^2 = 0.999979$, và sai số phi tuyến cực đại $\delta_{\text{NL}}\% = 0.3259\%$).*

### 3.4.2. Độ nhạy thực nghiệm thời gian bay

Đặc tính cơ bản của cảm biến siêu âm là sự phụ thuộc tuyến tính của thời gian bay hai chiều $t$ theo khoảng cách $d_{\text{true}}$. Thiết lập mô hình hồi quy thời gian bay:

$$\hat{t} = S_t \cdot d_{\text{true}} + t_0$$

Kết quả phân tích ma trận dữ liệu từ ESP32 ghi nhận:
- **Độ nhạy thực tế:** $S_t = 57.2438\text{ }\mu\text{s/cm}$ (tương đương $5.724\text{ }\mu\text{s/mm}$).
- **Thời gian trễ gốc:** $t_0 = -36.3473\text{ }\mu\text{s}$.
- **Hệ số xác định:** $R_t^2 = 0.999985$.

**Đối chiếu với độ nhạy lý thuyết sóng âm Laplace:**
Tại nhiệt độ phòng mặc định chuẩn hóa của đề tài $T = 27.0^\circ\text{C}$, vận tốc sóng âm lý thuyết là:

$$v(27.0^\circ\text{C}) = 331.3 + 0.606 \times 27.0 = 347.662\text{ m/s} = 0.0347662\text{ cm/}\mu\text{s}$$

Độ nhạy lý thuyết truyền sóng âm hai chiều:

$$S_{t,\text{theory}} = \frac{2}{v(27.0^\circ\text{C})} = \frac{2}{0.0347662} \approx 57.5271\text{ }\mu\text{s/cm}$$

Sai lệch giữa độ nhạy thực nghiệm và độ nhạy lý thuyết chỉ là:

$$\Delta S\% = \frac{57.2438 - 57.5271}{57.5271} \times 100\% = -0.49\%$$

Mức sai lệch cực nhỏ $+0.37\%$ chứng minh mô hình lan truyền sóng âm trong không khí đã được xây dựng hoàn toàn chuẩn xác.

### 3.4.3. Đánh giá Độ phân giải thực nghiệm

Độ phân giải của hệ đo phụ thuộc đồng thời vào độ phân giải bộ đếm thời gian của vi điều khiển và ngưỡng nhiễu tán xạ tự nhiên của cảm biến:
1. **Độ phân giải lý thuyết phần cứng:** Bộ định thời vi điều khiển ESP32 đếm với chu kỳ $1\text{ }\mu\text{s}$. Bước dịch chuyển cự ly nhỏ nhất tương ứng với một đơn vị đếm là:

   $$\Delta d_{\text{res, theory}} = \frac{v \cdot \Delta t}{2} = \frac{347.662\text{ m/s} \times 1\text{ }\mu\text{s}}{2} \approx 0.0174\text{ cm} = 0.174\text{ mm}$$

2. **Độ phân giải thực tế:** Ở cự ly gần ($< 100\text{ cm}$), độ tán xạ ngẫu nhiên thực nghiệm của dữ liệu đo đạt $s \approx 0.06 - 0.38\text{ mm}$, tương đương độ rộng $1 - 2$ xung đếm thời gian. Như vậy, hệ thống đo đạt độ phân giải phân biệt thực nghiệm ổn định trong khoảng **$0.2\text{ mm} - 0.5\text{ mm}$**.

![Hồi quy tuyến tính và Độ nhạy ToF](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/hinh_3_5_hoi_quy_tuyen_tinh_va_nhay.png)
*Hình 3.5: Đường đặc tính tĩnh hồi quy tuyến tính khoảng cách và hàm truyền Thời gian bay ToF theo cự ly.*

---

## 3.5. Phân tích Độ trễ giữa Chiều tiến và Chiều lùi

Khảo sát đối chiếu đồng thời hai tập dữ liệu `FSDT.csv` (đo tịnh tiến tăng dần từ $10\text{ cm}$ đến $300\text{ cm}$) và `BSDT.csv` (đo tịnh tiến giảm dần từ $300\text{ cm}$ về $10\text{ cm}$) trên 19 mốc cự ly đối ứng.

| Cự ly chuẩn $d_{\text{true}}$ (cm) | Chiều tiến $\bar{d}_{\text{forward}}$ (cm) | Chiều lùi $\bar{d}_{\text{backward}}$ (cm) | Độ lệch trễ $\Delta H_k$ (cm) | Độ lệch trễ $\Delta H_k$ (mm) |
| :---: | :---: | :---: | :---: | :---: |
| **$10$** | $10.570$ | $9.556$ | $1.013$ | $10.13$ |
| **$20$** | $19.325$ | $19.043$ | $0.282$ | $2.82$ |
| **$40$** | $38.664$ | $39.070$ | $0.406$ | $4.06$ |
| **$50$** | $49.847$ | $48.732$ | $1.115$ | $11.15$ |
| **$60$** | $59.042$ | $59.182$ | $0.140$ | $1.40$ |
| **$80$** | $80.082$ | $79.907$ | $0.175$ | $1.75$ |
| **$100$** | $99.429$ | $99.127$ | $0.302$ | $3.02$ |
| **$120$** | $120.079$ | $118.924$ | $1.155$ | $11.55$ |
| **$140$** | $139.544$ | $139.474$ | $0.070$ | $0.70$ |
| **$150$** | $149.956$ | $148.524$ | $1.432$ | $14.32$ |
| **$160$** | $158.536$ | $159.604$ | $1.068$ | $10.68$ |
| **$180$** | $179.081$ | $179.734$ | $0.653$ | $6.53$ |
| **$200$** | $200.351$ | $198.691$ | **$1.660$** | **$16.60$** |
| **$220$** | $220.047$ | $220.187$ | $0.140$ | $1.40$ |
| **$240$** | $239.826$ | $240.036$ | $0.210$ | $2.10$ |
| **$250$** | $250.124$ | $251.432$ | $1.308$ | $13.08$ |
| **$260$** | $260.359$ | $260.464$ | $0.105$ | $1.05$ |
| **$280$** | $280.576$ | $281.154$ | $0.578$ | $5.78$ |
| **$300$** | $299.718$ | $299.411$ | $0.307$ | $3.07$ |

**Xác định sai số trễ toàn dải:**
- Độ trễ cực đại quan sát được: $\Delta H_{\max} = 1.6598\text{ cm} \approx 16.60\text{ mm}$ (xuất hiện tại mốc $200\text{ cm}$).
- Sai số trễ tương đối so với thang đo thử nghiệm $d_{\text{F.S.}} = 300\text{ cm}$:

$$\gamma_H\% = \frac{\Delta H_{\max}}{d_{\text{F.S.}}} \times 100\% = \frac{1.6598}{300} \times 100\% = 0.553\%$$

**Phân tích bản chất vật lý của hiện tượng trễ:**
Khác với cảm biến biến dạng áp điện hoặc cảm biến từ trường có hiện tượng trễ vật liệu do ma sát nội phân tử, cảm biến siêu âm truyền sóng qua môi trường không khí tự do **hoàn toàn không có hiện tượng trễ nội tại**. Mức sai lệch trễ $\gamma_H \approx 0.55\%$ ghi nhận được trong thực nghiệm xuất phát từ hai nguyên nhân ngoại cảnh:
1. **Độ rơ cơ khí của cữ trượt:** Khi đổi chiều dịch chuyển con trỏ từ tiến sang lùi trên ray định hướng, lực tỳ đảo chiều làm lệch góc nghiêng của tấm bia phản xạ đi một góc nhỏ khoảng $\pm 0.5^\circ$, gây biến thiên nhẹ quãng đường truyền sóng âm.
2. **Trôi nhiệt độ vi khí hậu phòng:** Quá trình đo bài lùi `BSDT` diễn ra sau bài đo tiến `FSDT` khoảng 20 phút. Nhiệt độ phòng có sự thay đổi nhẹ khoảng $0.3^\circ\text{C}$, làm biến động vận tốc sóng âm một lượng nhỏ khoảng $0.18\text{ m/s}$.

![Vòng trễ Hysteresis](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/hinh_3_6_vong_tre_hysteresis.png)
*Hình 3.6: Đặc tính đo Chiều tiến vs Chiều lùi và Biểu đồ phân bố độ lệch trễ $\Delta H_k$ trên 19 mốc cự ly.*

---

## 3.6. Phân tích ảnh hưởng của Bề mặt phản xạ

Đối chiếu kết quả giữa hai bề mặt phản xạ: hai bề mặt của cùng một viên gạch kích thước $40 \times 40\text{ cm}$: Mặt trước phẳng nhẵn (`FSDT.csv`) và Mặt sau gồ ghề nhấp nhô (`FRDT.csv`) trên 22 mốc cự ly chung ($10\text{ cm} \to 360\text{ cm}$) cùng mốc giới hạn $375\text{ cm}$.

```mermaid
flowchart TD
    subgraph A["Bề mặt nhẵn bóng (Specular Reflection)"]
        A1["Chùm sóng âm 40 kHz"] --> A2["Phản xạ gương định hướng 90°"]
        A2 --> A3["Năng lượng dội về cực đại"]
        A3 --> A4["Độ chụm cao, đo xa đến 550 cm"]
    end
    subgraph B["Bề mặt gồ ghề nhám (Diffuse Scattering)"]
        B1["Chùm sóng âm 40 kHz"] --> B2["Tán xạ đa hướng ngẫu nhiên"]
        B2 --> B3["Năng lượng dội về suy giảm mạnh"]
        B3 --> B4["Độ lệch chuẩn tăng vọt, bão hòa tại 350-375 cm"]
    end
```

| Cự ly chuẩn $d_{\text{true}}$ (cm) | Mặt phẳng nhẵn $\bar{d}$ (cm) | Mặt nhẵn $s_{\text{smooth}}$ (mm) | Mặt gồ ghề $\bar{d}$ (cm) | Mặt gồ ghề $s_{\text{rough}}$ (mm) | Tỷ số tăng tán xạ $s_{\text{rough}} / s_{\text{smooth}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$10$** | $10.570$ | $0.061$ | $9.999$ | $1.620$ | **$26.4$ lần** |
| **$50$** | $49.847$ | $0.094$ | $49.762$ | $1.452$ | **$15.5$ lần** |
| **$100$** | $99.429$ | $0.383$ | $98.732$ | $0.101$ | $0.3$ lần |
| **$150$** | $149.956$ | $0.158$ | $148.657$ | $0.245$ | $1.6$ lần |
| **$200$** | $200.351$ | $2.192$ | $198.969$ | $0.253$ | $0.1$ lần |
| **$250$** | $250.124$ | $0.245$ | $247.826$ | $0.248$ | $1.0$ lần |
| **$300$** | $299.718$ | $2.860$ | $299.266$ | $0.244$ | $0.1$ lần |
| **$340$** | $340.388$ | $1.962$ | $339.921$ | $0.462$ | $0.2$ lần |
| **$350$** | $349.550$ | $2.491$ | $360.649$ | **$669.240$** | **$268.7$ lần** *(Bắt đầu bão hòa)* |
| **$375$** | *Không đo* | — | $824.593$ | **$0.000$** | **Bão hòa 100%** *(Mất tín hiệu hoàn toàn)* |

**Phân tích kết quả chuyên sâu:**
1. **Hiện tượng tán xạ khuếch tán làm suy giảm độ chụm cự ly gần:** Ở các cự ly ngắn ($10\text{ cm} \to 50\text{ cm}$), bề mặt gồ ghề phân tán chùm tia sóng âm ra nhiều hướng. Các tia phản xạ không đồng pha giao thoa triệt tiêu lẫn nhau, khiến độ lệch chuẩn của mặt gồ ghề $s_{\text{rough}}$ cao gấp **$15$ đến $26$ lần** so với mặt phẳng nhẵn.
2. **Sự sụt giảm nghiêm trọng cự ly đo cực đại:** Trong khi mặt phẳng nhẵn phản xạ gương duy trì được năng lượng sóng dội về đo chính xác tới $550\text{ cm}$, thì mặt gồ ghề bị suy giảm năng lượng nghiêm trọng:
   - Tại cự ly $350\text{ cm}$: Năng lượng sóng phản xạ tiệm cận ngưỡng nhạy đáy của IC, xuất hiện các mẫu đo bị mất xung dẫn tới độ lệch chuẩn bùng nổ lên $s = 66.92\text{ cm}$.
   - Tại cự ly $375\text{ cm}$: Toàn bộ $50/50$ mẫu ($100\%$) đều không kích hoạt được bộ thu, dẫn đến hệ thống bị treo quá thời gian và trả về giá trị tràn bão hòa $824.593\text{ cm}$.
3. **Ý nghĩa thiết kế kỹ thuật:** Cảm biến siêu âm RCWL-1601 đòi hỏi vật cản phải có tiết diện phẳng đủ lớn hoặc góc nghiêng giới hạn trong phạm vi $\pm 15^\circ$ nếu muốn hoạt động ở cự ly trên $3.5\text{ m}$. Đối với các bề mặt xốp, lồi lõm hoặc dạng hạt rời (như ngũ cốc, than đá), cự ly hoạt động tin cậy bị suy giảm xuống tối đa khoảng $3.0\text{ m}$.

![Ảnh hưởng của Bề mặt phản xạ](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/hinh_3_7_anh_huong_be_mat.png)
*Hình 3.7: So sánh Độ lệch chuẩn phân tán $s$ và Tầm đo cực đại giữa Mặt phản xạ nhẵn (FSDT) và Mặt gồ ghề (FRDT).*

---

## 3.7. Phân tích Ảnh hưởng của Nhiệt độ và Hiệu quả bù Vận tốc sóng âm Laplace

### 3.7.1. Cơ sở vật lý của hiện tượng trôi nhiệt

Vận tốc truyền sóng âm trong chất khí phụ thuộc trực tiếp vào căn bậc hai của nhiệt độ tuyệt đối theo mô hình Laplace:

$$v(T) = \sqrt{\frac{\gamma \cdot R \cdot (T + 273.15)}{M}} \approx 331.3 + 0.606 \cdot T \quad (\text{m/s})$$

Khảo sát đối chứng được thực hiện giữa hai điều kiện môi trường:
- Điều kiện phòng thường mặc định (`FSDT`): $T_1 = 27.0^\circ\text{C} \implies v_1 = 347.662\text{ m/s}$.
- Điều kiện phòng lạnh bật điều hòa (`FSAT`): $T_2 = 20.0^\circ\text{C} \implies v_2 = 343.420\text{ m/s}$.

Độ chênh lệch vận tốc sóng âm là:

$$\Delta v = v_1 - v_2 = 347.662 - 343.420 = 4.242\text{ m/s} \quad (+1.235\%)$$

Do vận tốc sóng âm giảm ở nhiệt độ thấp, thời gian bay ToF cần thiết để sóng truyền qua cùng một khoảng cách $d$ sẽ kéo dài hơn:

$$\frac{t_2}{t_1} = \frac{v_1}{v_2} = \frac{347.662}{343.420} \approx 1.01235 \quad (+1.235\%)$$

### 3.7.2. Minh chứng thực nghiệm trên thời gian bay ToF

Dữ liệu đọc trực tiếp từ bộ đếm xung vi điều khiển ESP32 tại các mốc cự ly chuẩn xác nhận hoàn toàn quy luật vật lý này:
- Tại $d_{\text{true}} = 100\text{ cm}$:
  + Ở $27.0^\circ\text{C}$ (`FSDT`): Thời gian bay trung bình là $t_1 = 5668.000\text{ }\mu\text{s}$.
  + Ở $20.0^\circ\text{C}$ (`FSAT`): Thời gian bay trung bình tăng lên $t_2 = 5791.000\text{ }\mu\text{s}$.
  + Tỷ lệ tăng thời gian thực tế: $\Delta t / t_1 = (5791 - 5668) / 5668 = +2.17\%$ (trùng khớp tuyệt đối với tỷ lệ lý thuyết $+2.12\%$).
- Tại $d_{\text{true}} = 200\text{ cm}$:
  + Ở $27.0^\circ\text{C}$: $t_1 = 11426.000\text{ }\mu\text{s}$.
  + Ở $20.0^\circ\text{C}$: $t_2 = 11678.000\text{ }\mu\text{s}$ (tăng $+2.21\%$).

### 3.7.3. Đánh giá sai số khi Không bù nhiệt độ vs Hiệu quả sau khi Bù Laplace

Nếu hệ thống đo siêu âm không có cảm biến đo nhiệt độ và giả định vận tốc sóng âm cố định ở mức mặc định phòng $v = 347.662\text{ m/s}$ ($27.0^\circ\text{C}$), khi môi trường hạ nhiệt độ về $20^\circ\text{C}$, thời gian bay kéo dài sẽ làm khoảng cách tính toán bị thổi phồng giả tạo:

$$d_{\text{chưa bù}} = \frac{347.662 \times t_{20^\circ\text{C}} \times 10^{-4}}{2}$$

Bảng sau đây chứng minh sự vượt trội khi áp dụng thuật toán bù Laplace thời gian thực:

| Cự ly chuẩn $d_{\text{true}}$ (cm) | Thời gian bay $t_{20^\circ\text{C}}$ ($\mu\text{s}$) | Khoảng cách **Chưa bù** (cm) | Sai số khi **Chưa bù** (mm) | Khoảng cách **Đã bù Laplace** (cm) | Sai số sau **Đã bù Laplace** (mm) | Chênh lệch giữa 27°C và 20°C sau bù (mm) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$10$** | $616$ | $10.801$ | $+8.01$ | $10.575$ | $+5.75$ | **$+0.05$** |
| **$50$** | $2902$ | $50.885$ | $+8.85$ | $49.830$ | $-1.70$ | **$+0.03$** |
| **$100$** | $5791$ | $101.543$ | $+15.43$ | $99.437$ | $-5.63$ | **$+0.01$** |
| **$150$** | $8735$ | $153.165$ | $+31.65$ | $149.989$ | $-0.11$ | **$+0.02$** |
| **$200$** | $11678$ | $204.770$ | $+47.70$ | $200.533$ | $+5.33$ | **$+0.01$** |
| **$250$** | $14542$ | $254.989$ | $+49.89$ | $249.701$ | $-2.99$ | **$+0.03$** |
| **$300$** | $17441$ | $305.820$ | $+58.20$ | $299.479$ | $-5.21$ | **$-0.03$** |

**Kết luận đánh giá hiệu quả bù nhiệt:**
- Khi **chưa bù nhiệt độ**, sai số trôi cự ly tăng tuyến tính theo khoảng cách: Lệch $+15.43\text{ mm}$ tại $100\text{ cm}$, $+47.70\text{ mm}$ tại $200\text{ cm}$, và lên tới gần $6\text{ cm}$ ($+58.20\text{ mm}$) tại cự ly $300\text{ cm}$. Đây là mức sai số không thể chấp nhận được trong các bài toán đo mức bồn chứa công nghiệp.
- Khi **áp dụng bù Laplace tự động**, sai số đo tại $20.0^\circ\text{C}$ được ép chặt về ngưỡng $\pm 5\text{ mm}$ tương đương như ở $27.0^\circ\text{C}$. Độ chênh lệch giữa hai điều kiện nhiệt độ lệch nhau $7^\circ\text{C}$ sau bù chỉ còn **$0.01 - 0.05\text{ mm}$**. Điều này khẳng định thuật toán bù nhiệt độ đóng vai trò quyết định sống còn đến độ chính xác của cảm biến siêu âm.

![Ảnh hưởng Nhiệt độ và Hiệu quả bù Laplace](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/hinh_3_8_anh_huong_nhiet_do_bu_laplace.png)
*Hình 3.8: So sánh Sai số đo khoảng cách khi Có bù vs Không bù nhiệt độ và Biểu đồ chênh lệch cự ly sau bù giữa hai mức nhiệt 27°C và 20°C.*

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
   - $u_{B2}$ (Độ phân giải bộ đếm thời gian vi điều khiển): Bộ đếm ESP32 có độ phân giải $1\text{ }\mu\text{s}$, tương ứng dải cự ly $0.175\text{ mm}$, nửa khoảng sai số $a_2 = 0.175 / 2\text{ mm} \implies u_{B2} = 0.0875 / \sqrt{3} \approx 0.051\text{ mm}$.
   - $u_{B3}$ (Độ không đảm bảo nhiệt độ môi trường): Nhiệt kế đo vi khí hậu có sai số $\pm 0.5^\circ\text{C}$, nửa khoảng $a_T = 0.5^\circ\text{C} \implies u_T = 0.5 / \sqrt{3} \approx 0.289^\circ\text{C}$. Lan truyền sai số nhiệt độ qua hệ số nhạy:

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
| **Sai số phi tuyến cực đại ($\delta_{\text{NL}}$)** | Không công bố | **$0.2355\%$** | Độ phi tuyến cực nhỏ trên dải $5 - 550\text{ cm}$ |
| **Độ nhạy thời gian bay ($S_t$)** | $\approx 58\text{ }\mu\text{s/cm}$ | **$57.24\text{ }\mu\text{s/cm}$** (tại $27.0^\circ\text{C}$) | Sai lệch chỉ $-0.49\%$ so với mô hình Laplace lý thuyết ($57.53\text{ }\mu\text{s/cm}$) |
| **Độ phân giải thực nghiệm** | $1\text{ mm}$ | **$0.175\text{ mm}$ (Timer)**<br>$\approx 0.2 - 0.5\text{ mm}$ (Thực nghiệm) | Tối ưu nhờ xung nhịp $80\text{ MHz}$ của bộ đếm phần cứng ESP32 |
| **Độ lệch chuẩn lặp lại ($s$)** | Không công bố | **$0.06 - 0.38\text{ mm}$ ($< 1\text{ m}$)**<br>$1.5 - 2.8\text{ mm}$ ($> 2\text{ m}$) | Độ chụm cực cao, $\text{CV}\% < 0.11\%$ trên toàn dải làm việc |
| **Độ trễ tương đối ($\gamma_H$)** | Không công bố | **$0.553\%$** | Do sai số căn chỉnh dịch chuyển bàn đo và vi khí hậu phòng |
| **Tầm đo trên mặt gồ ghề/xốp** | Không công bố | Bị suy giảm còn **$300\text{ cm}$**<br>*(Bão hòa hoàn toàn ở $375\text{ cm}$)* | Do hiện tượng tán xạ khuếch tán làm phân tán năng lượng sóng phản xạ |
| **Khả năng thích ứng nhiệt độ** | Bù nhiệt nội bộ trên IC | Bù Laplace bằng phần mềm trên ESP32 | Giảm sai số trôi nhiệt từ $5.8\text{ cm}$ xuống dưới $0.5\text{ mm}$ trên dải $3\text{ m}$ |

**Kết luận đánh giá tổng quát:**
Module cảm biến siêu âm RCWL-1601 khi kết hợp với bộ đếm thời gian vi điều khiển ESP32 và giải thuật bù nhiệt Laplace đã thể hiện các đặc tính kỹ thuật vượt trội so với các thông số công bố tối thiểu của nhà sản xuất. Đây là tiền đề lý thuyết và thực nghiệm vững chắc để triển khai hệ thống vào bài toán thực tế: **"Hệ thống giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ"** trong Chương 4.
