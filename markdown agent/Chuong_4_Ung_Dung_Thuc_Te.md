# CHƯƠNG 4: XÂY DỰNG VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG THỰC TẾ

Trên cơ sở kết quả khảo sát thực nghiệm ở Chương 3, Chương 4 xây dựng mô hình hệ thống ứng dụng thực tế: **Giám sát mức và thể tích chất lỏng thông minh trên mô hình bình chứa chế tạo từ chai nước ngọt 2L cắt, kết hợp bơm chìm mini 6V trên vi điều khiển ESP32**.

---

## 4.1. Tổng quan tiềm năng ứng dụng từ kết quả thực nghiệm của RCWL-1601

### 4.1.1. Các đặc tính đo lường cốt lõi định hình không gian ứng dụng

Bốn đặc trưng đo lường cốt lõi của RCWL-1601 từ Chương 3 đóng vai trò định hình giải pháp thiết kế:
1. **Dải làm việc tuyến tính ($5 – 350\text{ cm}$):** Hệ số tương quan $R^2 > 0.9999$, sai số tương đối $< \pm 0.35\%$, độ lệch chuẩn $s < 0.4\text{ mm}$ ở cự ly gần trong điều kiện phòng thường chuẩn hóa $27.0^\circ\text{C}$.
2. **Vùng chết vật lý ($0 – 3\text{ cm}$):** Hiện tượng dao động dư (ringing) khiến cảm biến mất tín hiệu khi cự ly $< 3\text{ cm}$, đòi hỏi cơ cấu gá đo cách ly mặt nước tối thiểu $5\text{ cm}$.
3. **Phản xạ gương mặt chất lỏng:** Mặt thoáng chất lỏng là gương phản xạ âm học lý tưởng, tối ưu hóa tỷ số tín hiệu trên nhiễu (SNR) khi chùm sóng vuông góc mặt nước.

---

## 4.2. Thiết kế hệ thống giám sát mức và thể tích bình chứa chai 2L

### 4.2.1. Mô hình hình học và chuyển đổi toán học bình chứa chai 2L

Mô hình sử dụng chai nước ngọt 2L cắt phần chóp côn tạo thành bình trụ đáy phẳng: chiều cao thân $H_{\text{bình}} = 17.0\text{ cm}$, đường kính trong $D = 10.0\text{ cm}$ (bán kính $R = 5.0\text{ cm}$). Diện tích tiết diện đáy $S_{\text{base}}$ và dung tích tối đa $V_{\max}$ của thân bình xác định theo (4.1) và (4.2):

$$S_{\text{base}} = \pi \cdot R^2 = \pi \cdot 5.0^2 \approx 78.54\text{ cm}^2 \tag{4.1}$$

$$V_{\max} = S_{\text{base}} \cdot H_{\text{bình}} = 78.54 \cdot 17.0 \approx 1335.2\text{ cm}^3 \approx 1335\text{ mL} \tag{4.2}$$

![Hình 4.1: Sơ đồ nguyên lý mô hình bình chứa chai 2L](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_4/hinh_4_1_so_do_nguyen_ly_binh_2l.png)

*Hình 4.1: Sơ đồ nguyên lý mô hình bình chứa chai 2L cắt ($H = 17\text{ cm}$, $D = 10\text{ cm}$) và cơ cấu gá cảm biến RCWL-1601.*

Từ sơ đồ nguyên lý Hình 4.1, mô hình chuyển đổi thời gian bay $t_{\text{echo}}$ sang mức nước $h(t)$ và thể tích $V(t)$ thực hiện theo chuỗi (4.3) – (4.6):

$$v(T) = 331.3 + 0.606 \cdot T \quad (\text{m/s}) \tag{4.3}$$

$$d_{\text{comp}}(t) = \frac{v(T) \cdot t_{\text{echo}}}{2} \tag{4.4}$$

$$h(t) = H_{\text{tổng}} - d_{\text{comp}}(t) = 22.0 - d_{\text{comp}}(t) \tag{4.5}$$

$$V(t) = S_{\text{base}} \cdot h(t) = \pi R^2 \cdot [H_{\text{tổng}} - d_{\text{comp}}(t)] \tag{4.6}$$

---

### 4.2.2. Vận dụng 4 phát hiện thực nghiệm vào thiết kế hệ thống

1. **Vượt vùng chết cơ khí ($H_{\text{gá}} = 5.0\text{ cm}$):** Gá cảm biến cao $H_{\text{gá}} = 5.0\text{ cm}$ trên miệng chai. Khi nước nạp chạm ngưỡng ngắt bơm cao nhất ($h = 14.0\text{ cm}$), cự ly đo vẫn đạt $d = 22.0 - 14.0 = 8.0\text{ cm} > 3.0\text{ cm}$, triệt tiêu hoàn toàn nguy cơ mất tín hiệu do vùng chết.
2. **Bù nhiệt độ Laplace tự động:** Tích hợp DHT11 đo nhiệt độ thời gian thực để cập nhật động $v(T)$, khử sai số trôi cự ly do thời tiết.
3. **Chuỗi lọc số thích nghi 2 tầng:** Kết hợp lọc IQR ($N = 5$) triệt tiêu $100\%$ xung gai bọt khí và lọc Moving Average ($W = 7$) san phẳng sóng gợn khi bơm nạp.
4. **Lan truyền Độ không đảm bảo đo theo ISO/GUM:** Thể tích $V$ phụ thuộc vào bán kính $R$ ($u_R = 0.04\text{ cm}$ bằng thước kẹp) và mức nước $h$ ($u_h = 0.071\text{ cm}$ từ cảm biến). Theo chuẩn ISO/GUM, phương sai tổng hợp $u_c^2(V)$ và độ KĐBĐ mở rộng $U_{95\%}(V)$ ($k = 2$) xác định theo (4.7) và (4.8):

$$u_c^2(V) = c_R^2 \cdot u_R^2 + c_h^2 \cdot u_c^2(h) \tag{4.7}$$

$$U_{95\%}(V) = 2 \cdot u_c(V) = 2 \cdot \sqrt{(2\pi R h \cdot u_R)^2 + (S_{\text{base}} \cdot u_h)^2} \tag{4.8}$$

---

### 4.2.3. Bố trí mô hình thực nghiệm phần cứng thực tế

Mô hình thực nghiệm phần cứng được hiện thực hóa bao gồm vi điều khiển ESP32 gắn trên bảng mở rộng Sensor Shield (cấp nguồn và truyền dữ liệu qua cáp USB Serial), cảm biến nhiệt độ DHT11 bù vận tốc âm thời gian thực, cảm biến siêu âm RCWL-1601 đặt vuông góc với mặt thoáng chất lỏng, và khối LED chỉ thị trạng thái an toàn (LED Xanh) / cảnh báo mức nước (LED Đỏ) trên breadboard (Hình 4.4).

![Hình 4.4: Mô hình thực tế](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_4/hinh_4_4_mo_hinh_thuc_te_phan_cung.png)

*Hình 4.4: Mô hình thực tế.*

Thử nghiệm thực tế xác nhận: chuỗi thuật toán đo ToF kết hợp bù nhiệt độ phòng ($T \approx 30.8^\circ\text{C}$) và bộ lọc thích nghi vận hành chính xác, phản ánh nhạy bén sự biến thiên mức nước. Khi mức nước dâng cao áp sát miệng bình, đèn LED Đỏ lập tức kích hoạt cảnh báo nguy cơ tràn, minh chứng tính khả thi cao và độ tin cậy của giải pháp đo lường không tiếp xúc.

---

## 4.3. Kết quả thử nghiệm mô phỏng và Đánh giá hiệu năng ứng dụng

### 4.3.1. Mô phỏng động học quá trình bơm nạp và hiệu quả lọc sóng gợn

Quá trình bơm nạp nước vào bình 2L trong $t = 50\text{ giây}$ (mức nước dâng từ $h = 2.0\text{ cm}$ lên $14.5\text{ cm}$) được mô phỏng với tín hiệu thô $h_{\text{raw}}$ chứa dao động sóng gợn biên độ $\pm 0.7\text{ cm}$ và các xung gai bọt khí (Hình 4.2).

![Hình 4.2: Mô phỏng quá trình bơm nạp bình 2L và hiệu quả lọc sóng gợn](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_4/hinh_4_2_mo_phong_loc_song_gon_binh_2l.png)

*Hình 4.2: Mô phỏng quá trình bơm nạp bình 2L và hiệu quả lọc sóng gợn bằng chuỗi lọc thích nghi IQR + Moving Average.*

Đồ thị Hình 4.2 chứng minh hiệu quả chuỗi lọc: Tầng 1 (IQR) loại bỏ $100\%$ xung gai bọt khí đột biến; Tầng 2 (Moving Average) nén dao động sóng gợn từ $\pm 0.7\text{ cm}$ xuống dưới $\pm 0.08\text{ cm}$. Đường sau lọc $h_{\text{lọc}}$ (màu xanh lam) bám sát đường mức nước thực tế $h_{\text{true}}$ mà không gây trễ pha hay báo động giả.

---

### 4.3.2. Đánh giá thể tích chất lỏng tức thời và Độ không đảm bảo đo mở rộng

Đặc tính thể tích tích lũy $V(h)$ và độ KĐBĐ mở rộng $U_{95\%}(V)$ theo chuẩn ISO/GUM được tổng hợp trên biểu đồ đơn trục kép Hình 4.3.

![Hình 4.3: Đặc tính thể tích chất lỏng V và Đánh giá Độ không đảm bảo đo mở rộng U_95%(V)](file:///D:/ki5/[EMA2024E_3]%20K%E1%BB%B9%20thu%E1%BA%ADt%20%C4%91o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20c%E1%BA%A3m%20bi%E1%BA%BFn/RCWL1601/graph/chuong_4/hinh_4_3_danh_gia_the_tich_va_do_khong_dam_bao_do.png)

*Hình 4.3: Đặc tính thể tích chất lỏng V và Đánh giá Độ không đảm bảo đo mở rộng U_95%(V) theo tiêu chuẩn ISO/GUM.*

Từ Hình 4.3, thể tích $V(h)$ tuyến tính hoàn hảo theo mức nước, dải tin cậy mở rộng $V \pm U_{95\%}(V)$ ôm sát đường định mức. Độ KĐBĐ $U_{95\%}(V)$ tăng từ $11.2\text{ mL}$ ($h = 1\text{ cm}$) lên $41.7\text{ mL}$ ($h = 16\text{ cm}$) do hệ số nhạy $c_R = 2\pi R h$ tăng theo chiều cao. Tại mốc vận hành chuẩn $h = 10.1\text{ cm}$: $V = 792.5\text{ mL}$, $u_c(V) = \pm 13.8\text{ mL}$, $U_{95\%}(V) = \pm 27.7\text{ mL}$ ($k = 2$), sai số tương đối $\delta_V = \pm 3.49\% < 5\%$, hoàn toàn đáp ứng tiêu chuẩn kiểm soát chất lỏng tự động trong công nghiệp và dân dụng.

---

### 4.3.3. Phân cấp 4 ngưỡng cảnh báo an toàn và Kịch bản vận hành bơm mini 6V

Nhằm bảo vệ bơm 6V chống cháy khi cạn nước và chống tràn bồn, bình chứa được phân thành 4 ngưỡng trạng thái có trễ logic (Bảng 4.1):

*Bảng 4.1: Phân cấp 4 ngưỡng trạng thái giám sát và kịch bản điều khiển bơm mini 6V*

| Cấp trạng thái | Mức nước ($h$) | Thể tích ($V$) | Tỷ lệ | Chỉ thị & Còi báo | Kịch bản điều khiển bơm 6V |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Cạn khẩn cấp (Low-Low)** | $h \le 2.5\text{ cm}$ | $V \le 196\text{ mL}$ | $< 15\%$ | LED Đỏ nháy + Còi BEEP | Khóa an toàn chống cháy: Bơm TẮT cưỡng bức |
| **Cảnh báo cạn (Low)** | $2.5 < h \le 5.0\text{ cm}$ | $196 < V \le 393\text{ mL}$ | $15 – 30\%$ | LED Vàng + Chuông nhắc | Bật chế độ sẵn sàng: Kích hoạt bơm nạp nước |
| **Bình thường (Normal)** | $5.0 < h < 14.0\text{ cm}$ | $393 < V < 1100\text{ mL}$ | $30 – 82\%$ | LED Xanh sáng ổn định | Vận hành ổn định: Duy trì cấp nước theo nhu cầu |
| **Tràn khẩn cấp (High-High)** | $h \ge 14.0\text{ cm}$ | $V \ge 1100\text{ mL}$ | $> 82\%$ | LED Đỏ sáng + Còi hú | Cắt bơm khẩn cấp: Ngắt relay nguồn bơm 6V |

Giải thuật điều khiển bơm 6V áp dụng cơ chế trễ ngưỡng (hysteretic deadband): Khi $h$ tụt dưới $5.0\text{ cm}$, hệ thống kích hoạt bơm nạp; bơm chạy liên tục đến khi chạm ngưỡng tràn $h = 14.0\text{ cm}$ mới ngắt relay; khi nước rút xuống dưới $14.0\text{ cm}$, bơm không tự bật lại nhằm tránh hiện tượng rung giật relay (chattering).
