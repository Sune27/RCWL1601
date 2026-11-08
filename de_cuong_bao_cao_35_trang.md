# ĐỀ CƯƠNG CHI TIẾT BÁO CÁO THỰC NGHIỆM (QUY MÔ 30 – 35 TRANG)
**Học phần:** Kỹ thuật Đo lường và Cảm biến (`EMA2024E_3`)  
**Đề tài:** Thiết kế hệ thống thu thập dữ liệu, khảo sát thực nghiệm các đặc tính đo lường và xây dựng bài toán ứng dụng cho cảm biến khoảng cách siêu âm RCWL-1601 kết hợp bù nhiệt độ môi trường trên ESP32

---

## Bố cục tổng thể & Phân bổ dung lượng (31 – 34 trang chuẩn A4)

Bố cục báo cáo được chuẩn hóa thành 5 Chương trọng tâm, quy tụ mạch lạc thành hai trụ cột cốt lõi: **Thiết kế thực nghiệm** (Chương 2) và **Phân tích kết quả thực nghiệm** (Chương 3):

| Phần / Chương | Nội dung trọng tâm | Số trang dự kiến |
| :--- | :--- | :---: |
| **Mở đầu & Danh mục** | Trang bìa, Lời nói đầu, Mục lục, Danh mục bảng biểu, Danh mục hình vẽ, Ký hiệu & Quy ước mã hóa tập dữ liệu (`FSDT`, `FRDT`, `BSDT`, `FSAT`) | **2.5 – 3 trang** |
| **Chương 1** | **Cơ sở lý thuyết đo lường và cảm biến siêu âm:** Mô hình sóng siêu âm ToF, cơ chế bù nhiệt độ Laplace $v(T)$, cấu tạo IC RCWL-9610 và cơ sở lý thuyết xử lý số liệu thực nghiệm | **4 – 4.5 trang** |
| **Chương 2** | **THIẾT KẾ THỰC NGHIỆM:** Thiết kế phần cứng ESP32 + RCWL-1601, kiến trúc phần mềm OOP (MicroPython/PC), thiết kế ma trận kịch bản đo và nghiên cứu thống kê lựa chọn cỡ mẫu tối ưu $N = 50$ (từ khảo sát mẫu lớn 100 lần) | **6 – 6.5 trang** |
| **Chương 3** | **PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM:** Tiền xử lý & lọc sai số thô, khảo sát Dải đo & Vùng chết, Đánh giá toàn diện các đặc tính tĩnh (Precision, Accuracy, Linearity, Sensitivity, Resolution, Hysteresis), Phân tích yếu tố ngoại cảnh (Bề mặt phản xạ, Nhiệt độ môi trường), Đánh giá tổng hợp độ không đảm bảo đo và Đối chiếu Datasheet | **12 – 13 trang** |
| **Chương 4** | **Xây dựng và phân tích bài toán Ứng dụng thực tế:** Giám sát mức và thể tích chất lỏng thông minh trên mô hình bình chứa chai 2L cắt, kết hợp bơm chìm mini 6V trên ESP32 | **4 – 4.5 trang** |
| **Chương 5** | **Kết luận và Kiến nghị:** Tổng kết các kết quả đạt được, vùng làm việc tin cậy, khuyến nghị kỹ thuật giải pháp xử lý tín hiệu và Tài liệu tham khảo | **1.5 – 2 trang** |
| **TỔNG CỘNG** | **Toàn văn báo cáo khoa học (A4 chuẩn)** | **30 – 34.5 trang** |

---

## Chi tiết nội dung triển khai từng Chương

### PHẦN MỞ ĐẦU (2.5 – 3 trang)
1. **Trang bìa & Lời nói đầu (1 trang):** Đặt vấn đề về tính cấp thiết của đo khoảng cách không tiếp xúc bằng sóng siêu âm trong tự động hóa, robot và công nghiệp; mục tiêu khảo sát kiểm chứng thực nghiệm cảm biến giá rẻ RCWL-1601.
2. **Mục lục, Danh mục Hình vẽ, Danh mục Bảng biểu (1 trang).**
3. **Quy ước mã hóa tập dữ liệu thực nghiệm (0.5 – 1 trang):**
   - `100lanforward_smooth_defttemp_XXXcm`: Tập dữ liệu thăm dò $100$ lần đo tại $50\text{ cm}, 100\text{ cm}, 150\text{ cm}$ để khảo sát quy luật hội tụ thống kê.
   - `FSDT` (*Forward – Smooth – Default Temp*): Chuỗi đo cự ly tiến (1 cm $\to$ 600 cm, 35 mốc), bề mặt nhẵn phẳng, nhiệt độ phòng tự nhiên.
   - `BSDT` (*Backward – Smooth – Default Temp*): Chuỗi đo cự ly lùi (300 cm $\to$ 10 cm, 19 mốc), bề mặt nhẵn phẳng, nhiệt độ phòng tự nhiên (khảo sát độ trễ Hysteresis).
   - `FRDT` (*Forward – Rough – Default Temp*): Chuỗi đo cự ly tiến (10 cm $\to$ 375 cm, 23 mốc), bề mặt gồ ghề (khảo sát tán xạ phản xạ).
   - `FSAT` (*Forward – Smooth – Air-con Temp*): Chuỗi đo cự ly tiến (10 cm $\to$ 300 cm, 19 mốc), bề mặt nhẵn phẳng, phòng điều hòa nhiệt độ thấp $\sim 20^\circ\text{C}$ (khảo sát trôi nhiệt và thuật toán bù vận tốc âm).

---

### CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM (4 – 4.5 trang)
- **1.1. Nguyên lý đo khoảng cách Time-of-Flight (ToF) và Mô hình bù nhiệt độ môi trường (1.5 trang):**
  - Phương trình lan truyền sóng siêu âm ToF và công thức thực nghiệm Laplace bù nhiệt độ môi trường:

$$d = \frac{v(T) \cdot t}{2}, \quad v(T) = 331.3 \sqrt{1 + \frac{T}{273.15}} \approx 331.3 + 0.606 \cdot T \quad (\text{m/s})$$

  - Phân tích cơ chế suy hao năng lượng sóng âm theo quy luật bình phương khoảng cách ($I \propto 1/d^2$), hiện tượng suy giảm tín hiệu theo độ ẩm, và đặc tính hướng tính chùm tia phản xạ (góc mở búp sóng $\pm 15^\circ$).
- **1.2. Cấu tạo phần cứng và nguyên lý hoạt động của module RCWL-1601 (1 trang):**
  - Sơ đồ khối tích hợp vi mạch RCWL-9610 (bộ tạo dao động $40\text{ kHz}$, khuếch đại tín hiệu phản hồi, bộ so sánh điện áp).
  - Giản đồ thời gian phát xung kích hoạt `TRIG` ($10\text{ }\mu\text{s}$) và độ rộng xung phản hồi `ECHO` tỷ lệ thuận với ToF.
  - Thông số kỹ thuật định mức theo Datasheet của nhà sản xuất (Dải đo lý thuyết 2 cm – 400 cm, độ chính xác danh định 0.5 cm).
- **1.3. Cơ sở lý thuyết xử lý số liệu thực nghiệm và Đánh giá độ không đảm bảo đo (1.5 – 2 trang):**
  - Hệ thống công thức thống kê mô tả: Kỳ vọng mẫu $\bar{x}$, Trung vị $\text{Med}$, Độ lệch chuẩn thực nghiệm $s$, Khoảng tứ phân vị $\text{IQR} = Q_3 - Q_1$.
  - Tiêu chuẩn phát hiện và loại trừ sai số thô: Nguyên lý $3\sigma$ (phân phối chuẩn Gauss) và hàng rào $1.5 \cdot \text{IQR}$ (Boxplot).
  - Định nghĩa toán học các đặc tính đo lường tĩnh: Độ chụm ($\text{CV}\%$), Độ chính xác ($\Delta d$, $\delta\%$), Hồi quy tuyến tính bằng phương pháp bình phương bé nhất ($\hat{y} = ax + b$, hệ số xác định $R^2$, độ nhạy thực nghiệm $S_t$, sai số phi tuyến $\delta_{\text{NL}}\%$), Độ phân giải ($\Delta d_{\min}$), Độ trễ ($\Delta H_{\max}$, $\gamma_H\%$).
  - Phương pháp đánh giá Độ không đảm bảo đo theo tiêu chuẩn quốc tế ISO/GUM: Độ không đảm bảo chuẩn Loại A ($u_A$), Loại B ($u_B$), Độ không đảm bảo chuẩn tổng hợp ($u_c$) và Độ không đảm bảo đo mở rộng ($U_{95\%}$).

---

### CHƯƠNG 2: THIẾT KẾ THỰC NGHIỆM (6 – 6.5 trang)
*(Hợp nhất toàn bộ phương pháp luận thiết kế thực nghiệm: Phần cứng, Phần mềm, Ma trận kịch bản đo và Cơ sở xác định cỡ mẫu tối ưu)*

- **2.1. Mục tiêu và Phương pháp luận thực nghiệm (0.5 trang):**
  - Xác lập mục tiêu khảo sát: Đánh giá độ tin cậy thực tế, kiểm chứng dải đo ngoài Datasheet, xác định ngưỡng làm việc tối ưu và định lượng các yếu tố gây nhiễu môi trường.
- **2.2. Thiết kế hệ thống phần cứng và Mô hình gá đặt đo lường (1.5 trang):**
  - Sơ đồ nguyên lý đấu nối cảm biến RCWL-1601 với vi điều khiển ESP32 30-Pin (`TRIG` nối `GPIO 5`, `ECHO` nối `GPIO 18`, nguồn cấp `3.3V` và `GND`).
  - Thiết kế đồ gá thực nghiệm: Ray trượt cơ khí căn chỉnh trục đo thẳng hàng vuông góc với vật cản, vạch chuẩn milimet đối chiếu cự ly thực $d_{\text{true}}$.
  - Ảnh chụp mô hình thực nghiệm thực tế và giải pháp chống rung cơ học cho cảm biến.
- **2.3. Kiến trúc phần mềm OOP và Giải thuật thu thập dữ liệu (1.5 trang):**
  - Kiến trúc phần mềm hướng đối tượng OOP chia module rõ ràng:
    + Lớp `RCWL1601` trên MicroPython (ESP32): Điều khiển xung `TRIG`, ngắt timer độ phân giải $1\text{ }\mu\text{s}$ bắt sườn xung `ECHO`, tích hợp công thức Laplace $v(T)$ bù nhiệt độ tức thời.
    + Lớp `ESP32TerminalRunner` / `DistanceMonitorApp` trên PC: Giao tiếp nối tiếp UART/COM port, tự động ghi dữ liệu vào các file CSV chuẩn cấu trúc `t,distance_cm,temperature_c`.
  - Lưu đồ thuật toán lấy mẫu và cơ chế giám sát chu kỳ đo để tránh sóng siêu âm dội ngược lặp lại (Inter-ping Echo).
- **2.4. Thiết kế Ma trận Kịch bản thực nghiệm (1 trang):**
  - Bảng tổng hợp ma trận 4 kịch bản thực nghiệm (`FSDT`, `BSDT`, `FRDT`, `FSAT`) với đầy đủ các tham số điều kiện ngoại cảnh:
    + Vật liệu bề mặt phản xạ: Bảng foamex phẳng nhẵn vs. Tấm xốp gồ ghề khúc xạ tán xạ.
    + Hướng tiếp cận: Chiều tiến (Forward) vs. Chiều lùi (Backward).
    + Nhiệt độ môi trường: Phòng mặc định ($27.0^\circ\text{C}$) vs. Phòng điều hòa ($20^\circ\text{C}$).
    + Số lượng mốc khoảng cách và cự ly chi tiết của từng kịch bản.
- **2.5. Cơ sở thống kê và Thực nghiệm xác định Cỡ mẫu tối ưu $N = 50$ (1.5 – 2 trang):**
  *(Phân tích từ 3 file dữ liệu khảo sát 100 lần đo: `100lanforward_smooth_defttemp_050cm.csv`, `100cm.csv`, `150cm.csv`)*
  - Khảo sát sự hội tụ của Trung bình lũy tích $\bar{x}(k)$, Độ lệch chuẩn lũy tích $s(k)$ và Bán kính khoảng tin cậy Student $\varepsilon_{95\%}(k)$ khi tăng dần cỡ mẫu từ $k = 2 \to 100$:

$$\varepsilon_{95\%}(k) = t_{0.975, k-1} \cdot \frac{s(k)}{\sqrt{k}}$$

  - Đồ thị đường cong hội tụ tại 3 mốc cự ly tiêu biểu (gần, trung bình, xa: 50 cm, 100 cm, 150 cm).
  - Luận giải khoa học việc chốt cỡ mẫu $N = 50$ mẫu/mốc: Sau điểm khuỷu tay ($k \approx 30 - 35$), giá trị $\bar{x}$ và $s$ dao động tiệm cận dưới $\pm 0.05\%$, bán kính sai số $\varepsilon_{95\%}$ đạt mức cực nhỏ; việc đo 50 lần vừa đảm bảo độ tin cậy thống kê cao ($> 95\%$), vừa giảm thiểu $50\%$ thời gian và khối lượng thao tác cho toàn bộ gần 100 lượt thí nghiệm sau.

---

### CHƯƠNG 3: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM (12 – 13 trang)
*(Trụ cột trọng tâm của báo cáo: Toàn bộ quá trình xử lý, phân tích số liệu từ các tập dữ liệu tổng hợp `FSDT.csv`, `BSDT.csv`, `FRDT.csv`, `FSAT.csv`)*

- **3.1. Tiền xử lý dữ liệu và Đánh giá hiệu quả lọc sai số thô (1.5 trang):**
  - So sánh trực quan dữ liệu thô trước và sau khi áp dụng thuật toán lọc sai số thô ($3\sigma$ và $\text{IQR}$).
  - Đánh giá khả năng loại trừ nhiễu đột biến (outliers) do phản xạ phụ, đối chiếu giá trị Mean $\bar{x}$ và Median $\text{Med}$ chứng minh độ tin cậy của tập mẫu sau lọc.
- **3.2. Khảo sát Dải đo thực tế, Vùng chết (Blind Zone) và Giới hạn bão hòa xa (1.5 trang):**
  - **Vùng chết (1 cm – 3 cm):** Phân tích dữ liệu thực tế tại `001cm`, `002cm`, `003cm` (hiện tượng đầu thu bị bão hòa năng lượng, phản xạ nhiều lần giữa mặt cảm biến và vật thể, khiến kết quả đo bị sai lệch cố định lên $\sim 2.0 - 2.6\text{ cm}$).
  - **Dải đo tuyến tính ổn định (5 cm – 400 cm):** Tín hiệu phản hồi rõ ràng, ổn định cao.
  - **Giới hạn đo xa vượt định mức (420 cm – 550 cm):** Phân tích hiện tượng cảm biến vẫn đo tốt vượt ngưỡng $400\text{ cm}$ của Datasheet lên đến $550\text{ cm}$ trên bề mặt nhẵn phẳng (lợi thế của vi mạch RCWL-9610 khuếch đại nhạy).
  - **Ngưỡng suy hao & bão hòa (580 cm – 600 cm):** Sóng âm phản xạ bị suy giảm vượt quá ngưỡng phát hiện của IC, dẫn đến hiện tượng timeout và tràn thời gian bay (trả về giá trị bão hòa $\sim 825\text{ cm}$).
- **3.3. Đánh giá Độ chụm (Precision) và Độ chính xác (Accuracy) (2 trang):**
  - **Độ chụm (Precision):** Biểu diễn biến thiên của Độ lệch chuẩn $s$, Khoảng tứ phân vị $\text{IQR}$ và Hệ số biến thiên $\text{CV}\%$ theo khoảng cách ($d_{\text{true}} = 1\text{ cm} \to 550\text{ cm}$). Chứng minh $\text{CV}\% < 0.2\%$ trên phần lớn dải đo.
  - **Độ chính xác (Accuracy):** Tính toán Sai số tuyệt đối $\Delta d = \bar{d} - d_{\text{true}}$ và Sai số tương đối $\delta\% = (\Delta d / d_{\text{true}}) \cdot 100\%$. Phân tích thành phần sai số hệ thống (Systematic Error) do offset lắp đặt và trôi vận tốc sóng âm.
- **3.4. Đánh giá Độ tuyến tính (Linearity), Độ nhạy (Sensitivity) và Độ phân giải (Resolution) (2 trang):**
  - Phương trình hồi quy khoảng cách đo thực nghiệm: $\bar{d} = a \cdot d_{\text{true}} + b$ với hệ số tương quan $R^2 \approx 0.9999$.
  - Phương trình hồi quy thời gian bay thực nghiệm: $\bar{t} = S_t \cdot d_{\text{true}} + t_0$. Tính ra **Độ nhạy thực tế** $S_t\text{ }(\mu\text{s/cm})$ và đối chiếu với độ nhạy lý thuyết ($S_{t,\text{theory}} = 2/v \approx 57.1\text{ }\mu\text{s/cm}$).
  - Sai số phi tuyến cực đại $\delta_{\text{NL}}\%$ trên toàn dải làm việc.
  - Đánh giá **Độ phân giải thực nghiệm** dựa trên độ biến thiên nhỏ nhất của bộ đếm thời gian vi điều khiển ($1\text{ }\mu\text{s} \to \Delta d_{\min} \approx 0.0175\text{ cm}$) so với độ tán xạ thực tế của cảm biến.
- **3.5. Phân tích Độ trễ (Hysteresis) giữa Chiều tiến và Chiều lùi (1.5 trang):**
  *(Đối chiếu tập dữ liệu `FSDT` và `BSDT` trên 19 mốc đo chung từ 10 cm đến 300 cm)*
  - Lập bảng sai lệch chiều đo: $\Delta H_k = |\bar{d}_{\text{forward}} - \bar{d}_{\text{backward}}|$.
  - Xác định độ trễ cực đại $\Delta H_{\max}$ và Sai số trễ tương đối $\gamma_H\% = (\Delta H_{\max} / d_{\text{F.S.}}) \cdot 100\%$.
  - Vẽ và phân tích đồ thị **Vòng trễ (Hysteresis Loop)**; kết luận bản chất không có trễ cơ học trong cảm biến siêu âm (sai lệch chủ yếu do rơ lắc ray trượt cơ khí hoặc biến thiên nhỏ của nhiệt độ môi trường theo thời gian).
- **3.6. Phân tích ảnh hưởng của Bề mặt phản xạ (Reflective Surface) (1.5 trang):**
  *(Đối chiếu tập dữ liệu `FSDT` - Mặt nhẵn vs. `FRDT` - Mặt gồ ghề trên 23 mốc đo từ 10 cm đến 375 cm)*
  - Hiện tượng tán xạ sóng âm (Diffuse Scattering): Mặt gồ ghề làm phân tán năng lượng sóng phản xạ về mọi hướng, dẫn đến suy giảm tỷ số $S/N$.
  - Tác động lên Độ chụm: Độ lệch chuẩn $s_{\text{rough}}$ tăng gấp $2 - 5$ lần so với $s_{\text{smooth}}$, xuất hiện nhiều mẫu ngoại lai.
  - Tác động lên Cự ly đo xa: Bề mặt gồ ghề làm triệt tiêu sóng phản xạ ở cự ly xa, khiến dải đo thực tế bị thu hẹp đáng kể (chỉ đạt tối đa $375\text{ cm}$ thay vì $> 550\text{ cm}$).
  - Biểu đồ so sánh Boxplot và Error-bar trực quan giữa hai bề mặt.
- **3.7. Phân tích ảnh hưởng của Nhiệt độ môi trường và Hiệu quả thuật toán bù nhiệt (1.5 trang):**
  *(Đối chiếu tập dữ liệu `FSDT` - Phòng mặc định $27.0^\circ\text{C}$ vs. `FSAT` - Phòng điều hòa $20^\circ\text{C}$ trên 19 mốc đo)*
  - So sánh thời gian bay $\bar{t}\text{ }(\mu\text{s})$ tại cùng các cự ly hình học giữa hai mức nhiệt độ (chênh lệch nhiệt độ $\Delta T \approx 11 - 12^\circ\text{C}$ làm thay đổi vận tốc âm thanh $\approx 6.8\text{ m/s}$).
  - Định lượng sai số trôi cự ly (Thermal Drift Error) nếu giả định vận tốc âm thanh cố định không đổi ($v = 340\text{ m/s}$ hoặc $343\text{ m/s}$).
  - Chứng minh hiệu quả của thuật toán bù nhiệt độ Laplace $v(T)$: Giảm sai số trôi cự ly từ hàng centimet xuống dưới mức milimet, giữ độ chính xác đồng nhất ở các điều kiện nhiệt độ khác nhau.
- **3.8. Đánh giá Độ không đảm bảo đo mở rộng toàn diện (1 trang):**
  - Lập bảng tổng hợp độ không đảm bảo đo trên toàn dải đo:
    + Độ không đảm bảo Loại A ($u_A = s/\sqrt{N}$).
    + Độ không đảm bảo Loại B ($u_B$ gồm: sai số vạch thước chuẩn $\pm 1\text{ mm}$, độ phân giải thời gian ESP32 $1\text{ }\mu\text{s}$, độ không đảm bảo của giá trị nhiệt độ môi trường ghi nhận).
    + Độ không đảm bảo chuẩn tổng hợp: $u_c = \sqrt{u_A^2 + u_B^2}$.
    + Độ không đảm bảo đo mở rộng với hệ số phủ $k_p = 2$ (mức tin cậy 95%): $U_{95\%} = k_p \cdot u_c$.
- **3.9. Bảng tổng hợp đối chiếu Đặc tính Kỹ thuật Thực nghiệm vs. Datasheet Nhà sản xuất (1 trang):**
  - Bảng đối chiếu song song: Dải đo cực tiểu/cực đại, Vùng chết, Độ phân giải, Độ chụm trung bình, Sai số toàn dải, Tần số phát, Thời gian đáp ứng giữa Datasheet công bố và Kết quả khảo sát thực tế trên ESP32.

---

### CHƯƠNG 4: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ (4 – 4.5 trang)
*(Chương dành riêng cho yêu cầu Ứng dụng của Assignment — liên kết toàn diện kết quả đo lường ở Chương 3 vào bài toán kỹ thuật)*

- **4.1. Tổng quan tiềm năng ứng dụng từ kết quả thực nghiệm của RCWL-1601:**
  - 4.1.1. Các đặc tính đo lường cốt lõi định hình không gian ứng dụng:
    1. Dải làm việc tuyến tính (5 – 350 cm): R² > 0.9999, sai số tương đối < ±0.35%, độ lệch chuẩn s < 0.4 mm ở cự ly gần trong điều kiện chuẩn hóa 27.0°C.
    2. Vùng chết vật lý (0 – 3 cm): Hiện tượng dao động dư (ringing) đòi hỏi cơ cấu gá đo cách ly mặt nước tối thiểu 5 cm.
    3. Phản xạ gương mặt chất lỏng: Tối ưu hóa tỷ số tín hiệu trên nhiễu (SNR) khi chùm sóng vuông góc mặt nước.
- **4.2. Thiết kế hệ thống giám sát mức và thể tích bình chứa chai 2L:**
  - 4.2.1. Mô hình hình học và chuyển đổi toán học bình chứa chai 2L: Chai 2L cắt (H_bình = 17.0 cm, D = 10.0 cm, R = 5.0 cm, S_base ≈ 78.54 cm², V_max ≈ 1335 mL). Sơ đồ nguyên lý cơ cấu gá cảm biến cao H_gá = 5.0 cm (H_tổng = 22.0 cm) (Hình 4.1). Chuỗi chuyển đổi ToF sang h(t) và V(t) theo công thức (4.1) – (4.6).
  - 4.2.2. Vận dụng 4 phát hiện thực nghiệm vào thiết kế hệ thống:
    1. Vượt vùng chết cơ khí (H_gá = 5.0 cm, cự ly luôn d ≥ 8.0 cm > 3.0 cm).
    2. Bù nhiệt độ Laplace tự động thời gian thực bằng cảm biến DHT11 cập nhật động v(T).
    3. Chuỗi lọc số thích nghi 2 tầng: Lọc IQR (N = 5) triệt tiêu xung gai + Moving Average (W = 7) san phẳng sóng gợn.
    4. Lan truyền Độ không đảm bảo đo thể tích theo chuẩn ISO/GUM theo công thức (4.7) và (4.8).
  - 4.2.3. Bố trí mô hình thực nghiệm phần cứng thực tế: Hiện thực hóa trên vi điều khiển ESP32, Sensor Shield, DHT11 (T ≈ 30.8°C), RCWL-1601 và LED chỉ thị an toàn/cảnh báo trên breadboard (Hình 4.4).
- **4.3. Kết quả thử nghiệm mô phỏng và Đánh giá hiệu năng ứng dụng:**
  - 4.3.1. Mô phỏng động học quá trình bơm nạp và hiệu quả lọc sóng gợn: Quá trình bơm nạp t = 50s (h = 2.0 → 14.5 cm), nén dao động sóng gợn từ ±0.7 cm xuống dưới ±0.08 cm (Hình 4.2).
  - 4.3.2. Đánh giá thể tích chất lỏng tức thời và Độ không đảm bảo đo mở rộng U_95%(V): Tại mốc chuẩn h = 10.1 cm, V = 792.5 mL, U_95%(V) = ±27.7 mL (k = 2), sai số tương đối δ_V = ±3.49% < 5% (Hình 4.3).
  - 4.3.3. Phân cấp 4 ngưỡng cảnh báo an toàn và Kịch bản vận hành bơm mini 6V (Bảng 4.1): Phân cấp 4 trạng thái (Low-Low, Low, Normal, High-High) với cơ chế trễ ngưỡng (hysteretic deadband) chống rung giật relay.

---

### CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ (1.5 – 2 trang)
- **5.1. Kết luận chung về đề tài (0.5 – 1 trang):**
  - Tổng kết các mục tiêu đã hoàn thành: Xây dựng hệ thống thu thập tự động, làm chủ thuật toán xử lý dữ liệu chuẩn hóa, chứng minh năng lực đo thực tế của cảm biến RCWL-1601.
- **5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật (0.5 trang):**
  - Đánh giá: Giá thành rất thấp, độ nhạy cao, hoạt động vượt dải định mức trên bề mặt nhẵn ($> 550\text{ cm}$); nhược điểm là vùng chết $3\text{ cm}$ và suy giảm nhanh trên bề mặt gồ ghề/tán xạ xa.
  - Khuyến nghị giải pháp kỹ thuật khi triển khai thực tế trong công nghiệp.
- **5.3. Tài liệu tham khảo & Phụ lục (0.5 trang):**
  - Danh mục tài liệu tham khảo chuẩn IEEE / ISO GUM và trích dẫn mã nguồn thực nghiệm.
