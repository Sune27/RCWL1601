# CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ

---

## 5.1. Kết luận chung về đề tài

Đề tài nghiên cứu và đánh giá thực nghiệm cảm biến khoảng cách siêu âm RCWL-1601 trên nền tảng vi điều khiển ESP32 trong khuôn khổ học phần **Kỹ thuật Đo lường và Cảm biến (EMA2024E_3)** đã hoàn thành toàn diện các mục tiêu khoa học và kỹ thuật:

1. **Xây dựng thành công hệ thống đo lường thực nghiệm chuẩn hóa:**
   - Thiết lập giàn thử nghiệm cơ khí với ray trượt định hướng dài $7\text{ m}$, con trỏ đọc vạch chia $1\text{ mm}$, cơ cấu giữ bia phản xạ vuông góc $90^\circ$ và độ cao giá đỡ $75\text{ cm}$ triệt tiêu hoàn toàn sóng dội từ mặt sàn.
   - Kết nối trực tiếp RCWL-1601 với ESP32 ở mức logic $3.3\text{ V}$, cấu hình bộ định thời phần khớp đo ToF với độ phân giải $1\text{ }\mu\text{s}$ ($\Delta d_{\text{LSB}} \approx 0.174\text{ mm}$).
   - Chứng minh cỡ mẫu $N = 50$ lần đo là tối ưu tuyệt đối, cân bằng hoàn hảo giữa việc thu hẹp khoảng tin cậy Student $95\%$ ($\varepsilon_{95\%} \le 0.05\text{ mm}$) và duy trì tần suất quét thời gian thực.

2. **Khảo sát định lượng toàn diện các đặc tính tĩnh và động:**
   - **Đặc tính tuyến tính ($5 – 400\text{ cm}$):** Phương trình hồi quy OLS bậc 1 đạt $\hat{y} = 1.00273 \cdot x - 0.48427\text{ (cm)}$ với $R^2 > 0.9999$. Kiểm chứng mù trên 10 mốc Test độc lập khẳng định Bậc 1 vượt trội hơn Bậc 2 và Bậc 3 trên cả chỉ số sai số tuyệt đối ($\sum |e| = 41.07\text{ mm}$) lẫn sai số bình phương ($\text{MSE} = 33.90\text{ mm}^2$). Độ phi tuyến cực đại chỉ đạt $\pm 0.361\%\text{ FS}$.
   - **Tầm đo mở rộng & Vùng chết:** Đo ổn định tới $550\text{ cm}$ trên mặt phẳng nhẵn (vượt $22\%$ so với datasheet $450\text{ cm}$). Xác định chính xác vùng chết vật lý $0 – 3\text{ cm}$ do dao động dư của màng gốm ($150\text{ }\mu\text{s}$) và ngưỡng ngắt câm của vi mạch RCWL-9610.
   - **Độ chụm và Độ chính xác cao:** Độ lệch chuẩn $s < 0.4\text{ mm}$ ở cự ly gần, $\text{CV}\% < 0.11\%$ trên toàn dải đo, độ không lặp lại $\le \pm 0.143\%\text{ FS}$. Vòng trễ thực nghiệm cực nhỏ $\gamma_H = 0.553\%$, chủ yếu do độ rơ cơ khí.
   - **Khử trôi nhiệt bằng thuật toán Laplace:** Sai số trôi nhiệt $+1.235\%$ do môi trường lạnh ($20^\circ\text{C}$ vs $27^\circ\text{C}$, trôi tới $+4\text{ cm}$ tại $2.8\text{ m}$) được kéo hoàn toàn về quanh đường $0\text{ mm}$ nhờ tự động cập nhật động $v(T) = 331.3 + 0.606 \cdot T$.
   - **Ngân sách Độ không đảm bảo đo chuẩn hóa (ISO/GUM):** Tổng hợp đầy đủ Loại A ($u_A \le 0.40\text{ mm}$) và Loại B ($u_{B1}, u_{B2}, u_{B3}$). Độ không đảm bảo đo mở rộng đạt $U_{95\%} \le 0.77\text{ mm}$ ở cự ly gần ($d \le 50\text{ cm}$) và duy trì dưới $\pm 5.57\text{ mm}$ trên toàn dải xa $550\text{ cm}$.

3. **Hiện thực hóa thành công mô hình ứng dụng thực tế (Chương 4):**
   - Chế tạo và vận hành thành công mô hình giám sát mức và thể tích chất lỏng trên bình chứa chai nước ngọt 2L cắt ($H = 17\text{ cm}, D = 10\text{ cm}$) kết hợp bơm chìm mini 6V trên ESP32.
   - Vận dụng sáng tạo 4 phát hiện thực nghiệm: cơ cấu gá cao $5\text{ cm}$ vượt vùng chết, bù nhiệt Laplace qua DHT11, chuỗi lọc 2 tầng (IQR + Moving Average) nén sóng gợn từ $\pm 0.7\text{ cm}$ xuống dưới $\pm 0.08\text{ cm}$, và lan truyền độ KĐBĐ thể tích theo ISO/GUM đạt $\delta_V = \pm 3.49\% < 5\%$.
   - Phân cấp 4 ngưỡng trạng thái (Low-Low, Low, Normal, High-High) với cơ chế trễ ngưỡng (hysteretic deadband) chống rung giật relay, điều khiển bơm an toàn chống cạn và chống tràn.

---

## 5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật

### 5.2.1. Đánh giá ưu điểm và hạn chế của cảm biến RCWL-1601

* **Ưu điểm nổi bật:**
  1. *Hiệu quả kinh tế cao:* Chi phí linh kiện thấp nhưng đạt độ chính xác và độ lặp lại tiệm cận cảm biến công nghiệp khi được chuẩn hóa thuật toán xử lý dữ liệu.
  2. *Tương thích tối ưu hệ nhúng $3.3\text{ V}$:* Hoạt động trực tiếp với chân logic của ESP32 mà không cần IC chuyển đổi mức điện áp.
  3. *Tầm đo vượt trội trên mặt phẳng:* Tầng khuếch đại tự động của vi mạch RCWL-9610 cho phép bắt sóng tới $550\text{ cm}$.
  4. *Đo không tiếp xúc:* Lý tưởng cho môi trường chất lỏng, tránh ăn mòn và bám bẩn.
* **Hạn chế vật lý:**
  1. *Vùng chết $0 – 3\text{ cm}$:* Mất hoàn toàn khả năng đo khi vật thể áp sát đầu thu/phát.
  2. *Suy hao mạnh trên bề mặt tán xạ:* Cự ly đo tin cậy bị co hẹp từ $550\text{ cm}$ xuống $350\text{ cm}$ trên mặt gồ ghề/xốp.
  3. *Độ nhạy nhiệt độ cao:* Vận tốc âm phụ thuộc chặt vào nhiệt độ môi trường không khí.

### 5.2.2. Khuyến nghị kỹ thuật khi triển khai thực tế

Để khai thác tối đa hiệu năng của module RCWL-1601 trong công nghiệp và dân dụng:
1. **Thiết kế cơ khí:** Luôn thiết kế cơ cấu gá cảm biến cao hơn mức chất lỏng tối đa tối thiểu $5 – 10\text{ cm}$ để triệt tiêu hoàn toàn nguy cơ rơi vào vùng chết. Bố trí cảm biến tránh xa thành bình để chùm sóng âm $15^\circ$ không bắt phản xạ giả.
2. **Bù nhiệt độ thời gian thực:** Bắt buộc tích hợp cảm biến nhiệt độ (như DHT11, DS18B20) đặt gần đường truyền sóng để cập nhật động $v(T)$, loại bỏ sai số trôi cự ly theo thời tiết.
3. **Chuỗi lọc số thích nghi:** Áp dụng kết hợp lọc IQR ($N = 5$) triệt tiêu xung ngoại lai bọt khí và lọc Trung bình trượt (Moving Average, $W = 7$) san phẳng sóng gợn mặt nước.
4. **Điều khiển có trễ ngưỡng:** Ứng dụng dải trễ logic (hysteretic deadband) khi đóng cắt bơm/van nhằm chống hiện tượng rung giật relay (chattering) kéo dài tuổi thọ thiết bị.

---

## 5.3. Tài liệu tham khảo

1. **JCGM 100:2008**, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)*, Joint Committee for Guides in Metrology.
2. **ISO/IEC 17025:2017**, *General requirements for the competence of testing and calibration laboratories*, International Organization for Standardization.
3. **Kinsler, L. E., Frey, A. R., Coppens, A. B., & Sanders, J. V. (2000)**, *Fundamentals of Acoustics*, 4th Edition, John Wiley & Sons, New York.
4. **Wuxi Ri-Chow Technology Co., Ltd. (2019)**, *RCWL-1601 Ultrasonic Distance Measurement Module Datasheet & RCWL-9610 IC Technical Specification*, Rev 1.2.
5. **Espressif Systems (2023)**, *ESP32 Technical Reference Manual*, Version 5.0, Espressif Systems Co., Ltd.
6. **Tukey, J. W. (1977)**, *Exploratory Data Analysis*, Addison-Wesley Publishing Company, Reading, Mass.
