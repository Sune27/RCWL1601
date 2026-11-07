# CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ

---

## 5.1. Kết luận chung về đề tài

Đề tài nghiên cứu, khảo sát thực nghiệm các đặc tính đo lường của module cảm biến khoảng cách siêu âm RCWL-1601 trên nền tảng vi điều khiển 32-bit ESP32 và xây dựng hệ thống ứng dụng giám sát mức chất lỏng thông minh trong khuôn khổ học phần **Kỹ thuật Đo lường và Cảm biến (EMA2024E_3)** đã hoàn thành toàn diện các mục tiêu khoa học và kỹ thuật đề ra:

1. **Xây dựng thành công hệ thống đo lường thực nghiệm chuẩn hóa:**
   - **Phương thức bố trí và định vị thiết bị đo:** Thiết lập mô hình thực nghiệm trên hai bàn đo cao $85.0\text{ cm}$ đặt dọc theo hành lang kín gió dài $10\text{ m}$ (rộng $2.8\text{ m}$, cách tường bên tối thiểu $1.4\text{ m}$) nhằm loại trừ hoàn toàn phản xạ phụ từ mặt sàn và vách tường trong góc mở chùm sóng $15^\circ$. Cảm biến RCWL-1601 được cố định trên breadboard sát mép bàn; vật thể phản xạ mục tiêu là viên gạch chuẩn kích thước $40\text{ cm} \times 40\text{ cm}$ (mặt trước phẳng nhẵn và mặt sau gồ ghề) dựng thẳng đứng vuông góc $90^\circ$ với trục phát sóng; cự ly chuẩn $d_{\text{true}}$ được xác lập bằng thước dây tiêu chuẩn.
   - **Giao tiếp phần cứng và thu thập dữ liệu:** Kết nối trực tiếp RCWL-1601 với vi điều khiển ESP32 ở mức logic $3.3\text{ V}$, cấu hình bộ định thời phần cứng đo thời gian bay ToF với độ phân giải $1\text{ }\mu\text{s}$ ($\Delta d_{\text{LSB}} \approx 0.174\text{ mm}$).
   - **Tối ưu hóa cỡ mẫu thống kê:** Từ chuỗi đo thăm dò $100$ lần liên tiếp tại $3$ mốc cự ly ($50\text{ cm}, 100\text{ cm}, 150\text{ cm}$), phân tích bán kính sai số ngẫu nhiên $\varepsilon_{95\%}(k)$ theo phân phối Student và tốc độ biến thiên $|d\varepsilon_{95\%}/dk|$ đã chứng minh cỡ mẫu $N = 50$ lần đo là tối ưu, đảm bảo $\varepsilon_{95\%} < 0.5\text{ mm}$ (nhỏ hơn nửa độ chia thước chuẩn) và đạt ngưỡng dừng bão hòa sai số ($|d\varepsilon/dk| \approx 0$).

2. **Khảo sát định lượng toàn diện các đặc tính tĩnh và các yếu tố ảnh hưởng vật lý:**
   - **Tiền xử lý và lọc sai số thô bằng Khoảng tứ phân vị (IQR):** Trên tổng số $4.800$ mẫu đo thuộc $4$ trường hợp thực nghiệm (`FSDT`, `BSDT`, `FRDT`, `FSAT`), giải thuật lọc IQR (Tukey's Fences) đã phát hiện và loại bỏ chính xác $235$ mẫu ngoại lai ($4.90\%$), giữ lại $4.565$ mẫu hợp lệ ($95.10\%$), giúp kéo độ lệch chuẩn tại vùng biên $580 – 600\text{ cm}$ từ $346.05 – 2621.02\text{ mm}$ về mức ổn định $0.09 – 4.0\text{ mm}$.
   - **Phân vùng dải đo thực tế:** Xác định rõ $4$ phân vùng làm việc trên mặt phẳng nhẵn: Vùng chết vật lý ($0 – 3\text{ cm}$, kết quả bị kẹp ở $2.03 – 2.68\text{ cm}$ do dao động dư màng gốm áp điện $150\text{ }\mu\text{s}$ và mạch ngắt câm nội của IC RCWL-9610), Dải đo tuyến tính ổn định ($5 – 400\text{ cm}$), Dải đo xa vượt định mức ($420 – 550\text{ cm}$, vượt $22\%$ so với trần công bố $450\text{ cm}$ của nhà sản xuất) và Ngưỡng bão hòa xa ($580 – 600\text{ cm}$, tràn thời gian bay tại $824.56\text{ cm}$). Chốt dải làm việc tin cậy thực tế trên mặt nhẵn là **$10\text{ cm} – 550\text{ cm}$**.
   - **Độ chụm và Độ chính xác cao:** Trên toàn dải hữu ích $1 – 550\text{ cm}$ ($33$ mốc), độ lệch chuẩn đạt $s < 0.4\text{ mm}$ ở cự ly gần và sai số chuẩn trung bình $\text{SE} = s/\sqrt{n}$ luôn được nén phẳng dưới $0.5726\text{ mm}$ ($32/33$ mốc đạt $\text{SE} < 0.45\text{ mm}$). Trong dải $50 – 550\text{ cm}$, sai số tuyệt đối nằm trong khoảng $[-5.71, +14.02]\text{ mm}$ và sai số tương đối hội tụ chặt trong dải $[-0.57\%, +0.35\%]$.
   - **Độ tuyến tính (Linearity):** Phân chia $34$ mốc đo theo tỷ lệ $70\%$ Huấn luyện ($24$ mốc) và $30\%$ Kiểm thử độc lập ($10$ mốc). Kết quả đối sánh xác nhận phương trình hồi quy tuyến tính Bậc 1:
     $$\hat{y}_1 = 1.00273 \cdot x - 0.48427 \quad (\text{cm})$$
     đạt tổng sai số tuyệt đối tích lũy thấp nhất trên tập kiểm thử ($\sum |e| = 41.07\text{ mm}$), vượt trội so với mô hình Bậc 2 và Bậc 3 ($\sum |e| = 47.45\text{ mm}$) và phản ánh đúng độ thụt lùi cơ khí $\approx 4.84\text{ mm}$ của màng rung áp điện.
   - **Độ trễ hai chiều (Hysteresis):** Khảo sát đối xứng giữa Chiều tiến (`FSDT`) và Chiều lùi (`BSDT`) trên $19$ mốc chung ($10 – 300\text{ cm}$) ghi nhận độ lệch trễ cực đại $\Delta H_{\max} = 1.6598\text{ cm}$ tại $200\text{ cm}$, tương ứng sai số trễ tương đối $\gamma_{H,\text{test}} = 0.553\%$ (trên thang $300\text{ cm}$) và $\gamma_{H,\text{FS}} = 0.302\%$ (trên toàn dải $550\text{ cm}$), khẳng định bản chất phi trễ nội tại của phép đo sóng âm ToF.
   - **Ảnh hưởng của bề mặt phản xạ:** Tán xạ khuếch tán trên mặt gạch gồ ghề (`FRDT`) làm độ lệch chuẩn $s$ tăng gấp $3 – 26$ lần so với mặt nhẵn và thu hẹp giới hạn đo từ $550\text{ cm}$ xuống **$350\text{ cm}$** (chớm mất xung ở $350\text{ cm}$ và mất hoàn toàn tín hiệu từ $375 – 380\text{ cm}$).
   - **Ảnh hưởng của nhiệt độ và hiệu quả bù nhiệt Laplace:** Đối chứng giữa nhiệt độ phòng chuẩn hóa $27.0^\circ\text{C}$ ($v = 347.662\text{ m/s}$) và phòng lạnh $20.0^\circ\text{C}$ ($v = 343.420\text{ m/s}$) cho thấy nếu không bù nhiệt, kết quả đo bị phóng đại $+1.235\%$ quãng đường (trôi tới $+39.92\text{ mm}$ tại $280\text{ cm}$). Khi kích hoạt bù nhiệt Laplace thời gian thực $v(T) = 331.3 + 0.606 \cdot T$, sai số trôi nhiệt hàng xentimét bị triệt tiêu hoàn toàn, kéo $\Delta x$ về dao động quanh $0\text{ mm}$ ($14/14$ mốc từ $80 – 300\text{ cm}$ đạt $|\delta\%| \le 0.57\%$).
   - **Đánh giá tổng hợp độ không đảm bảo đo theo chuẩn ISO/GUM:** Kết hợp đầy đủ thành phần Loại A ($u_A = s/\sqrt{N}$) và Loại B ($u_{B1} \approx 0.289\text{ mm}$ từ thước chuẩn, $u_{B2} \approx 0.050\text{ mm}$ từ bộ đếm Timer ESP32, $u_{B3}(d) \approx 0.000503 \cdot d\text{ mm}$ từ cảm biến nhiệt độ). Độ không đảm bảo đo mở rộng ($k = 2$, mức tin cậy $95\%$) đạt $U_{95\%} \le 0.77\text{ mm}$ ở cự ly gần ($d \le 50\text{ cm}$) và luôn duy trì dưới $\pm 5.57\text{ mm}$ trên toàn dải đo đến $550\text{ cm}$.

3. **Hiện thực hóa thành công mô hình ứng dụng thực tế (Chương 4):**
   - Chế tạo và vận hành thành công mô hình hệ thống giám sát mức và thể tích chất lỏng thông minh trên bình chứa từ chai nước ngọt $2\text{L}$ cắt ($H_{\text{bình}} = 17.0\text{ cm}$, đường kính trong $D = 10.0\text{ cm}$, bán kính $R = 5.0\text{ cm}$, diện tích đáy $S_{\text{base}} \approx 78.54\text{ cm}^2$, dung tích tối đa $V_{\max} \approx 1335.2\text{ mL}$), kết hợp bơm chìm mini $6\text{ V}$, cảm biến nhiệt độ DHT11 ($T \approx 30.8^\circ\text{C}$) và khối chỉ thị LED Xanh/Đỏ trên vi điều khiển ESP32.
   - Vận dụng trực tiếp $4$ phát hiện thực nghiệm cốt lõi vào thiết kế:
     1. *Bố trí cơ cấu gá cao $H_{\text{gá}} = 5.0\text{ cm}$ trên miệng bình ($H_{\text{tổng}} = 22.0\text{ cm}$):* Khi mức nước chạm ngưỡng ngắt bơm cao nhất ($h = 14.0\text{ cm}$), khoảng cách đo vẫn đạt $d = 8.0\text{ cm} > 3.0\text{ cm}$, triệt tiêu hoàn toàn nguy cơ rơi vào vùng chết.
     2. *Bù nhiệt độ Laplace thời gian thực qua DHT11:* Khử sai số trôi vận tốc truyền âm theo vi khí hậu phòng đo.
     3. *Chuỗi lọc số thích nghi $2$ tầng:* Kết hợp lọc Khoảng tứ phân vị IQR ($N = 5$) loại bỏ $100\%$ xung gai bọt khí đột biến và lọc Trung bình trượt (Moving Average, $W = 7$) nén dao động sóng gợn mặt nước từ $\pm 0.7\text{ cm}$ xuống dưới $\pm 0.08\text{ cm}$.
     4. *Lan truyền độ không đảm bảo đo thể tích theo chuẩn ISO/GUM:* Kết hợp độ không đảm bảo đo bán kính bình ($u_R = 0.04\text{ cm}$) và mức nước ($u_h = 0.071\text{ cm}$); tại mốc vận hành chuẩn $h = 10.1\text{ cm}$ ($V = 792.5\text{ mL}$), đạt $u_c(V) = \pm 13.8\text{ mL}$ và $U_{95\%}(V) = \pm 27.7\text{ mL}$ ($k = 2$), tương ứng độ không đảm bảo tương đối $\delta_V = \pm 3.49\% < 5\%$.
   - Thiết lập phân cấp $4$ ngưỡng trạng thái an toàn (`Low-Low` $h \le 2.5\text{ cm}$, `Low` $2.5 < h \le 5.0\text{ cm}$, `Normal` $5.0 < h < 14.0\text{ cm}$, `High-High` $h \ge 14.0\text{ cm}$) tích hợp cơ chế trễ ngưỡng (hysteretic deadband) chống rung giật tiếp điểm rơ-le, bảo vệ bơm chống chạy khan và chống tràn tự động.

---

## 5.2. Đánh giá ưu nhược điểm và Khuyến nghị kỹ thuật

### 5.2.1. Đánh giá ưu điểm và hạn chế của cảm biến RCWL-1601

* **Ưu điểm nổi bật:**
  1. *Hiệu quả kinh tế cao:* Chi phí phần cứng thấp nhưng đạt độ chính xác và độ chụm tiệm cận cảm biến công nghiệp khi được chuẩn hóa bằng thuật toán lọc số và bù nhiệt.
  2. *Tương thích trực tiếp hệ nhúng $3.3\text{ V}$:* Hoạt động ổn định với mức điện áp logic $3.3\text{ V}$ của vi điều khiển ESP32 mà không cần mạch chuyển mức điện áp.
  3. *Tầm đo mở rộng vượt trội trên mặt phẳng nhẵn:* Tầng khuếch đại của vi mạch RCWL-9610 cho phép thu nhận sóng phản xạ gương tin cậy tới $550\text{ cm}$.
  4. *Phương pháp đo không tiếp xúc:* Phù hợp cho bài toán giám sát mức chất lỏng, tránh ăn mòn hóa học và bám cặn lên bề mặt cảm biến.

* **Hạn chế vật lý:**
  1. *Vùng chết vật lý $0 – 3\text{ cm}$:* Mất khả năng đo chính xác khi vật thể áp sát mặt cảm biến dưới $3\text{ cm}$ do dao động dư cơ học của màng gốm áp điện.
  2. *Suy hao mạnh trên bề mặt gồ ghề/nhám:* Tán xạ khuếch tán làm độ lệch chuẩn tăng gấp $3 – 26$ lần và thu hẹp cự ly đo tin cậy từ $550\text{ cm}$ xuống còn $350\text{ cm}$.
  3. *Độ nhạy nhiệt độ môi trường lớn:* Vận tốc âm thanh biến thiên $0.606\text{ m/s}$ trên mỗi $1^\circ\text{C}$, gây sai số trôi tỷ lệ thuận với khoảng cách nếu không có cảm biến nhiệt độ bù trừ.

### 5.2.2. Khuyến nghị kỹ thuật khi triển khai thực tế

Để khai thác tối đa độ tin cậy và độ chính xác của module RCWL-1601 trong các ứng dụng thực tế, nhóm nghiên cứu đề xuất $4$ khuyến nghị kỹ thuật trọng tâm:

1. **Bố trí khoảng cách ly vượt vùng chết và tránh phản xạ thành bồn:** Luôn lắp đặt cảm biến cao hơn mức chất lỏng tối đa tối thiểu $5 – 10\text{ cm}$ để đảm bảo mặt thoáng không bao giờ xâm nhập vùng chết $0 – 3\text{ cm}$. Đồng thời, đặt cảm biến cách thành bồn tối thiểu $R_{\text{cone}} = d \cdot \tan(7.5^\circ) \approx 0.13 \cdot d$ hoặc sử dụng ống dẫn hướng sóng tĩnh (stilling well) để chùm sóng mở $15^\circ$ không bắt phản xạ giả từ vách đứng.
2. **Bắt buộc tích hợp bù nhiệt độ Laplace thời gian thực:** Luôn bố trí cảm biến nhiệt độ (như DHT11 hoặc DS18B20) gần không gian truyền sóng để cập nhật động $v(T) = 331.3 + 0.606 \cdot T$ trước mỗi chu kỳ đo, triệt tiêu sai số trôi nhiệt độ theo thời tiết ngày/đêm.
3. **Ứng dụng chuỗi lọc số thích nghi $2$ tầng:** Kết hợp tầng lọc Khoảng tứ phân vị IQR ($N = 5$) để cắt bỏ các xung ngoại lai đột biến do bọt khí hoặc mất xung phản hồi với tầng lọc Trung bình trượt (Moving Average, $W = 7$) để làm mịn dao động sóng gợn mặt thoáng khi bơm nạp/xả.
4. **Thiết lập điều khiển có dải trễ ngưỡng (Hysteretic Deadband):** Áp dụng dải trễ logic giữa ngưỡng bật bơm và ngưỡng ngắt bơm nhằm chống hiện tượng đóng cắt liên tục gây rung giật và phóng điện hồ quang tại tiếp điểm rơ-le (relay chattering) khi mặt nước dao động quanh ranh giới cảnh báo, đồng thời cách ly nguồn động lực của máy bơm khỏi nguồn $3.3\text{ V}$ của vi điều khiển.

---

## 5.3. Tài liệu tham khảo

1. **JCGM 100:2008 (ISO/IEC Guide 98-3:2008)**, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM 1995 with minor corrections)*, Joint Committee for Guides in Metrology (BIPM, IEC, IFCC, ILAC, ISO, IUPAC, IUPAP, OIML), Sèvres, France, 2008.
2. **TCVN 9595-3:2013 (ISO/IEC Guide 98-3:2008)**, *Độ không đảm bảo đo — Phần 3: Hướng dẫn trình bày độ không đảm bảo đo (GUM:1995)*, Bộ Khoa học và Công nghệ, Hà Nội, 2013.
3. **ISO/IEC 17025:2017 (TCVN ISO/IEC 17025:2017)**, *General requirements for the competence of testing and calibration laboratories (Yêu cầu chung về năng lực của phòng thử nghiệm và hiệu chuẩn)*, International Organization for Standardization, Geneva, Switzerland, 2017.
4. **L. E. Kinsler, A. R. Frey, A. B. Coppens, and J. V. Sanders**, *Fundamentals of Acoustics*, 4th Edition, John Wiley & Sons, Inc., New York, 2000, ISBN: 978-0-471-84789-2.
5. **D. A. Bohn**, "Environmental Effects on the Speed of Sound," *Journal of the Audio Engineering Society (JAES)*, vol. 36, no. 4, pp. 223–231, April 1988.
6. **Wuxi Richen IoT Technology Co., Ltd. (RCWL) & Adafruit Industries**, *RCWL-1601 Open-Type Ultrasonic Distance Sensor Module & RCWL-9610 Ultrasonic Ranging IC Technical Specification*, Adafruit Product ID 4007 / RCWL-9610 Datasheet Rev 1.0, 2019–2022.
7. **Espressif Systems**, *ESP32 Technical Reference Manual*, Version 5.2, Espressif Systems (Shanghai) Co., Ltd., 2024.
8. **J. W. Tukey**, *Exploratory Data Analysis*, Addison-Wesley Publishing Company, Reading, Massachusetts, 1977, ISBN: 978-0-201-07616-5.
9. **E. O. Doebelin**, *Measurement Systems: Application and Design*, 5th Edition, McGraw-Hill, New York, 2003, ISBN: 978-0-07-243886-4.
10. **D. C. Montgomery and G. C. Runger**, *Applied Statistics and Probability for Engineers*, 7th Edition, John Wiley & Sons, Inc., Hoboken, New Jersey, 2018, ISBN: 978-1-119-40036-3.
11. **Phan Quốc Phô, Nguyễn Đức Chiến**, *Giáo trình Cảm biến*, Nhà xuất bản Khoa học và Kỹ thuật, Hà Nội, 2012.
