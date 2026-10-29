# ĐỀ CƯƠNG CHI TIẾT BÁO CÁO THỰC NGHIỆM (QUY MÔ 30 – 35 TRANG)
**Học phần:** Kỹ thuật Đo lường và Cảm biến (`EMA2024E_3`)  
**Đề tài:** Thiết kế hệ thống thu thập dữ liệu, khảo sát thực nghiệm các đặc tính đo lường và xây dựng bài toán ứng dụng cho cảm biến khoảng cách siêu âm RCWL-1601 kết hợp bù nhiệt độ môi trường trên ESP32

---

## Tổng quan phân bổ dung lượng (31 – 34 trang chuẩn A4)

| Phần / Chương | Nội dung trọng tâm | Số trang dự kiến |
| :--- | :--- | :---: |
| **Mở đầu & Danh mục** | Trang bìa, Mục lục, Danh mục bảng biểu, Danh mục hình vẽ, Ký hiệu viết tắt (`FSDT`, `FRDT`, `BSDT`...) | **2.5 – 3 trang** |
| **Chương 1** | Cơ sở lý thuyết về đo lường sóng siêu âm, cảm biến RCWL-1601, mô hình truyền sóng có bù nhiệt độ và lý thuyết xử lý số liệu thực nghiệm | **4 – 4.5 trang** |
| **Chương 2** | Thiết kế hệ thống đo phần cứng RCWL-1601, kiến trúc phần mềm OOP (MicroPython & PC) và quy trình thực nghiệm | **3.5 – 4 trang** |
| **Chương 3** | Cơ sở thống kê lựa chọn cỡ mẫu tối ưu $N = 50$ từ tập dữ liệu khảo sát 100 mẫu (`100lan...`) | **3 – 3.5 trang** |
| **Chương 4** | **Khảo sát toàn diện các Đặc tính tĩnh chuẩn (`FSDT` & `BSDT`):** Dải đo & Vùng chết, Lọc sai số thô ($3\sigma$ & $\text{IQR}$), Độ chụm (Precision), Độ chính xác (Accuracy), Độ tuyến tính (Linearity), Độ nhạy (Sensitivity), Độ phân giải (Resolution), Độ trễ (Hysteresis) và Độ không đảm bảo đo ($u_A, u_B, u_c, U_{95\%}$) | **8.5 – 9 trang** |
| **Chương 5** | **Khảo sát các yếu tố gây nhiễu ngoại cảnh:** Ảnh hưởng của Bề mặt phản xạ (`FRDT` vs. `FSDT`) và Ảnh hưởng của Nhiệt độ môi trường (Phòng thường vs. Phòng điều hòa) | **4 – 4.5 trang** |
| **Chương 6** | **Triển khai các bài toán Ứng dụng thực tế của hệ thống cảm biến RCWL-1601 có bù nhiệt độ môi trường (Theo yêu cầu Assignment)** | **4 – 4.5 trang** |
| **Chương 7** | Tổng kết bảng thông số thực nghiệm so với Datasheet & Kết luận | **1.5 – 2 trang** |
| **Tổng cộng** | **Toàn văn báo cáo** | **31 – 35 trang** |

---

## Chi tiết triển khai từng Chương (Đã tinh gọn để dành 4–4.5 trang cho Chương 6: Ứng dụng)

### PHẦN MỞ ĐẦU (2.5 – 3 trang)
1. **Trang bìa & Lời nói đầu (1 trang):** Đặt vấn đề về nhu cầu đo khoảng cách không tiếp xúc trong công nghiệp/robot và bài toán đánh giá độ tin cậy, đặc tính tĩnh của cảm biến siêu âm RCWL-1601.
2. **Mục lục, Danh mục Hình vẽ, Danh mục Bảng biểu & Quy ước mã hóa tập dữ liệu (1.5 – 2 trang):**
   - `100lanforward_smooth_defttemp_XXXcm`: Đo thăm dò $100$ lần ở $50\text{ cm}, 100\text{ cm}, 150\text{ cm}$.
   - `FSDT` (*Forward – Smooth – Default Temp*): Chiều tiến, bề mặt phẳng nhẵn, nhiệt độ phòng.
   - `BSDT` (*Backward – Smooth – Default Temp*): Chiều lùi, bề mặt phẳng nhẵn, nhiệt độ phòng.
   - `FRDT` (*Forward – Rough – Default Temp*): Chiều tiến, bề mặt gồ ghề, nhiệt độ phòng.
   - `FSAT` (*Forward – Smooth – Air-con Temp*): Chiều tiến, bề mặt nhẵn, nhiệt độ phòng bật điều hòa.

---

### CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM (4 – 4.5 trang)
- **1.1. Nguyên lý đo khoảng cách Time-of-Flight (ToF) và Mô hình bù nhiệt độ vận tốc âm thanh (1.5 trang):**
  - Phương trình đo khoảng cách và công thức thực nghiệm Laplace bù nhiệt độ môi trường (đơn vị $\text{m/s}$):

$$d = \frac{v(T) \cdot t}{2}, \quad v(T) = 331.3 \sqrt{1 + \frac{T}{273.15}} \approx 331.3 + 0.606 \cdot T$$

  - Phân tích sự suy hao năng lượng sóng âm theo khoảng cách ($I \propto 1/d^2$) và góc mở chùm tia ($\pm 15^\circ$).
- **1.2. Cấu tạo phần cứng và nguyên lý hoạt động của cảm biến RCWL-1601 (1 trang):**
  - Sơ đồ khối phát/thu siêu âm $40\text{ kHz}$, giản đồ xung kích hoạt `TRIG` – phản hồi `ECHO`, và đặc tính kỹ thuật định mức theo Datasheet.
- **1.3. Hệ thống công thức đánh giá đặc tính tĩnh và Độ không đảm bảo đo (1.5 – 2 trang):**
  - Tóm tắt ngắn gọn dưới dạng bảng công thức: Trung bình $\bar{x}$, Trung vị $\text{Med}$, Độ lệch chuẩn mẫu $s$, Khoảng tứ phân vị $\text{IQR} = Q_3 - Q_1$, Tiêu chuẩn lọc sai số thô $3\sigma$, Độ chụm ($\text{CV}\%$), Độ chính xác ($\Delta d$, $\delta\%$), Hồi quy tuyến tính ($\hat{y} = ax + b$, $R^2$, độ nhạy $S_t$, sai số phi tuyến $\delta_{\text{NL}}\%$), Độ phân giải ($\Delta d_{\min}$), Độ trễ ($\Delta H_{\max}$, $\gamma_H\%$) và Độ không đảm bảo đo theo chuẩn ISO/GUM ($u_A, u_B, u_c, U_{95\%}$).

---

### CHƯƠNG 2: THIẾT KẾ HỆ THỐNG ĐO VÀ QUY TRÌNH THỰC NGHIỆM (3.5 – 4 trang)
- **2.1. Thiết kế phần cứng và sơ đồ đấu nối trên ESP32 Expansion Board 30-Pin (1.5 trang):**
  - Sơ đồ nối dây cảm biến RCWL-1601 với ESP32 (`GPIO 5` - `TRIG`, `GPIO 18` - `ECHO`, nguồn cấp `3.3V` & `GND`) và ảnh chụp mô hình gá đặt thí nghiệm thực tế.
- **2.2. Kiến trúc phần mềm OOP (MicroPython & PC) và Ma trận kịch bản thực nghiệm (2 – 2.5 trang):**

---

### CHƯƠNG 3: PHÂN TÍCH LỰA CHỌN SỐ LẦN ĐO TỐI ƯU N = 50 TỪ TẬP MẪU LỚN (3 – 3.5 trang)
*(Sử dụng 3 file `100lanforward_smooth_defttemp_050cm.csv`, `100cm.csv`, `150cm.csv`)*
- **3.1. Bảng phân tích hội tụ tích lũy theo cỡ mẫu k = 2 .. 100 tại 3 cự ly (50 cm, 100 cm, 150 cm) (1 trang).**
- **3.2. Biểu đồ hội tụ cỡ mẫu và Luận giải việc chốt N = 50 mẫu/mốc (2 – 2.5 trang):**
  - Ghép gọn biểu đồ hội tụ $\bar{x}(k)$, $s(k)$ và bán kính khoảng tin cậy Student $\varepsilon_{95\%}(k)$ của 3 cự ly:

$$\varepsilon_{95\%}(k) = t_{0.975, k-1} \cdot \frac{s(k)}{\sqrt{k}}$$

  - Chứng minh tại $N = 50$, cả 3 mốc đều đã vượt qua điểm khuỷu tay ($k \approx 30 - 35$), đạt độ ổn định tiệm cận và tiết kiệm 50% thời gian đo cho toàn bộ các thí nghiệm sau.

---

### CHƯƠNG 4: ĐÁNH GIÁ TOÀN DIỆN CÁC ĐẶC TÍNH TĨNH Ở ĐIỀU KIỆN CHUẨN (`FSDT` & `BSDT`) (8.5 – 9 trang)
*(Trình bày bằng Bảng tổng hợp và Đồ thị, chỉ rõ lấy số liệu phân tích từ file cụ thể. Các yếu tố dưới đây là tham khảo và có thể thiếu, linh hoạt bổ sung thêm nếu cần)*

- **4.1. Bảng tổng hợp thống kê toàn dải (1 cm – 600 cm) & Hiệu quả lọc sai số thô ($3\sigma$ & $\text{IQR}$) (1.5 trang):**
  - Bảng tổng hợp các mốc khoảng cách trước và sau khi lọc sai số thô $3\sigma$ / $\text{IQR}$.
- **4.2. Khảo sát Vùng chết (Blind Zone: 1 – 3 cm) và Giới hạn đo xa bão hòa (400 – 600 cm) (1 trang):**
- **4.3. Đánh giá Độ chụm (Precision: $s, \text{CV}\%, \text{IQR}$) và Độ chính xác (Accuracy: $\Delta d, \delta\%$) (2 trang):**
  - Phân tích và biểu diễn đồ thị biến thiên của Độ lệch chuẩn $s$, $\text{CV}\%$, Sai số tuyệt đối $\Delta d = \bar{d} - d_{\text{true}}$ và Sai số tương đối $\delta\%$ theo khoảng cách.
- **4.4. Đánh giá Độ tuyến tính (Linearity), Độ nhạy (Sensitivity) và Độ phân giải (Resolution) (1.5 trang):**
  - Phương trình hồi quy $\bar{d} = a \cdot d_{\text{true}} + b$ và $\bar{t} = S_t \cdot d_{\text{true}} + t_0$; tính độ nhạy thực nghiệm $S_t\text{ }(\mu\text{s/cm})$, hệ số $R^2$, sai số phi tuyến $\delta_{\text{NL}}\%$ và đối chiếu Độ phân giải lý thuyết ($\approx 0.0175\text{ cm}$) với Độ phân giải thực tế.
- **4.5. Khảo sát Độ trễ (Hysteresis) giữa Chiều tiến (`FSDT`) và Chiều lùi (`BSDT`) (1.5 trang):**
  - Bảng đối chiếu 8 mốc (`010cm` $\to$ `300cm`), tính $\Delta H_k = |\bar{d}_{\text{forward}} - \bar{d}_{\text{backward}}|$, $\Delta H_{\max}$, $\gamma_H\%$ và vẽ Đồ thị Vòng trễ (Hysteresis Loop).
- **4.6. Đánh giá Độ không đảm bảo đo (Measurement Uncertainty: $u_A, u_B, u_c, U_{95\%}$) (1 trang):**
  - Bảng tổng hợp ngân sách độ không đảm bảo đo (Uncertainty Budget) gồm Loại A ($u_A = s/\sqrt{50}$) và Loại B ($u_B$ từ thước chuẩn $\pm 1\text{ mm}$, sai số bộ đếm thời gian vi điều khiển $1\text{ }\mu\text{s}$, độ không đảm bảo của giá trị nhiệt độ môi trường ghi nhận).

---

### CHƯƠNG 5: KHẢO SÁT CÁC YẾU TỐ GÂY NHIỄU NGOẠI CẢNH (4 – 4.5 trang)
- **5.1. Ảnh hưởng của Bề mặt phản xạ (Reflective Surface): Bề mặt nhẵn (`FSDT`) vs. Bề mặt gồ ghề (`FRDT`) (2 – 2.5 trang):**
  - Phân tích hiện tượng tán xạ sóng âm trên bề mặt gồ ghề làm tăng $s$, tăng sai số dương $\Delta d$ và giảm cự ly đo cực đại xuống $375\text{ cm}$ (kèm biểu đồ so sánh trực quan).
- **5.2. Ảnh hưởng của Nhiệt độ môi trường (Phòng thường vs. Phòng điều hòa) và Đánh giá hiệu quả thuật toán bù vận tốc âm thanh (2 trang):**
  - Đối chiếu thời gian bay $\bar{t}\text{ }(\mu\text{s})$ ở 2 mức nhiệt độ thực tế (nhiệt độ phòng tự nhiên vs. nhiệt độ phòng điều hòa ghi nhận trong tập dữ liệu), định lượng sai số trôi cự ly nếu giả định vận tốc âm thanh cố định ($v = 340\text{ m/s}$ hoặc $343\text{ m/s}$) so với khi áp dụng công thức bù nhiệt Laplace $v(T)$.

---

### CHƯƠNG 6: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ (4 – 4.5 trang)
*(Chương dành riêng cho yêu cầu Ứng dụng của Assignment — liên kết trực tiếp các kết quả khảo sát ở Chương 4 & 5 vào thiết kế kỹ thuật thực tế)*

- **6.1. Tổng quan các lĩnh vực ứng dụng phù hợp dựa trên đặc tính thực nghiệm của RCWL-1601 (1 trang):**
  - Dựa vào dải làm việc tốt nhất đã tìm được ở Chương 4 ($5\text{ cm} - 350\text{ cm}$, độ phân giải $\sim 1 - 2\text{ mm}$, chịu ảnh hưởng bề mặt gồ ghề ở xa), phân tích phạm vi ứng dụng trong:
    1. **Hệ thống đo và giám sát mức chất lỏng không tiếp xúc trong bồn chứa (Smart Tank Level Monitoring)** *(kết hợp thuật toán bù nhiệt độ môi trường)*.
    2. **Hệ thống cảnh báo va chạm lùi xe / Robot tự hành tránh vật cản (AGV / Mobile Robot Obstacle Avoidance).**
    3. **Hệ thống đo chiều cao người / kích thước kiện hàng tự động trên băng chuyền.**
- **6.2. Thiết kế chi tiết 1 Bài toán Ứng dụng tiêu biểu (2 – 2.5 trang):**
  *(Ví dụ chọn: **"Hệ thống đo thể tích/mức nước bồn chứa thông minh có bù nhiệt độ và cảnh báo tràn trên ESP32"** hoặc **"Hệ thống cảnh báo khoảng cách an toàn đa cấp độ"**)*:
  - **Sơ đồ nguyên lý & Mô hình toán học của bài toán ứng dụng:**
    - Công thức tính chiều cao cột chất lỏng $h = H_{\text{tank}} - d_{\text{compensated}}$ và thể tích $V = S_{\text{base}} \cdot h$.
  - **Ứng dụng trực tiếp kết quả thực nghiệm Chương 4 & 5 vào thiết kế:**
    - Lắp cảm biến cách mặt nước tối đa bao nhiêu để tránh **Vùng chết $0 - 3\text{ cm}$** (lắp cao hơn mức tràn tối thiểu $5\text{ cm}$).
    - Áp dụng **bộ lọc Trung vị + Lọc $3\sigma$ + Trung bình trượt** và **thuật toán bù vận tốc sóng âm theo nhiệt độ môi trường** để khử sóng gợn mặt nước và sự thay đổi nhiệt độ ngày/đêm.
    - Xác định **sai số thể tích $\Delta V$ và độ không đảm bảo đo $U_V$** của toàn hệ thống ứng dụng dựa trên $U_{95\%}$ đã tính ở Chương 4!
- **6.3. Kết quả thử nghiệm / Mô phỏng hoạt động của ứng dụng & Đánh giá hiệu năng (1 trang):**
  - Bảng kết quả thử nghiệm phân ngưỡng cảnh báo hoặc đo mức thực tế và hướng mở rộng IoT (đẩy dữ liệu từ ESP32 qua Wi-Fi/MQTT lên Dashboard).

---

### CHƯƠNG 7: TỔNG KẾT ĐẶC TÍNH KỸ THUẬT & KẾT LUẬN (1.5 – 2 trang)
- **7.1. Bảng đối chiếu Thông số thực nghiệm đo được vs. Datasheet RCWL-1601 (1 trang).**
- **7.2. Kết luận chung & Tài liệu tham khảo (0.5 – 1 trang).**
