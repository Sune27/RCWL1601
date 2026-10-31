# BÁO CÁO THỰC NGHIỆM ĐO LƯỜNG VÀ CẢM BIẾN

**BỘ GIÁO DỤC VÀ ĐÀO TẠO**  
**TRƯỜNG ĐẠI HỌC BÁCH KHOA HÀ NỘI**  
*(Hoặc tên Trường/Khoa của bạn - có thể tùy chỉnh)*  
**VIỆN CƠ KHÍ / TRƯỜNG CƠ KHÍ**  

---

<br>

<div align="center">

# BÁO CÁO THỰC NGHIỆM HỌC PHẦN
## KỸ THUẬT ĐO LƯỜNG VÀ CẢM BIẾN (MÃ HP: `EMA2024E_3`)

<br>

### ĐỀ TÀI:
### KHẢO SÁT THỰC NGHIỆM ĐẶC TÍNH ĐO LƯỜNG CỦA CẢM BIẾN SIÊU ÂM RCWL-1601 CÓ BÙ NHIỆT ĐỘ MÔI TRƯỜNG TRÊN VI ĐIỀU KHIỂN ESP32 VÀ ỨNG DỤNG ĐO MỨC BỒN CHỨA THÔNG MINH

<br><br>

**Giảng viên hướng dẫn:** *TS. / ThS. [Điền tên Giảng viên]*  
**Lớp học phần:** EMA2024E_3  
**Nhóm sinh viên thực hiện:**
1. Sinh viên 1: [Họ và tên] - MSSV: [MSSV]
2. Sinh viên 2: [Họ và tên] - MSSV: [MSSV]
3. Sinh viên 3: [Họ và tên] - MSSV: [MSSV]

<br><br>

*Hà Nội, Tháng 10 Năm 2026*

</div>

<br>

---

\newpage

# LỜI NÓI ĐẦU

Trong tiến trình tự động hóa công nghiệp và phát triển các hệ thống điều khiển thông minh (Industry 4.0, Robotics, Internet of Things - IoT), bài toán đo lường cự ly, vị trí và mức chất lỏng không tiếp xúc đóng vai trò mang tính sống còn. Các hệ thống cảnh báo va chạm của xe tự hành (AGV), trạm phân loại kích thước sản phẩm trên băng tải tự động, hay các bồn chứa hóa chất kín đều đòi hỏi phương pháp đo đạc không tiếp xúc vật lý nhằm tránh ăn mòn, tránh gây nhiễu loạn dòng chảy và đảm bảo an toàn vận hành liên tục.

Trong số các công nghệ đo khoảng cách hiện nay (Laser LiDAR, Radar sóng milimet, Cảm biến quang học hồng ngoại và Siêu âm), **cảm biến siêu âm (Ultrasonic Sensor)** nổi bật lên như một giải pháp tối ưu nhờ sự cân bằng xuất sắc giữa chi phí sản xuất thấp, độ an toàn tuyệt đối với con người và khả năng thích nghi cao với đa dạng vật liệu mục tiêu (không phụ thuộc vào độ trong suốt hay màu sắc quang học của bề mặt như cảm biến quang). Module cảm biến siêu âm **RCWL-1601** tích hợp vi mạch xử lý chuyên dụng RCWL-9610 là dòng cảm biến thế hệ mới, vận hành linh hoạt ở cả điện áp 3.3V và 5V, có tiềm năng thay thế vượt trội cho dòng HC-SR04 truyền thống trong các ứng dụng vi điều khiển hiện đại như ESP32.

Tuy nhiên, trong kỹ thuật đo lường chính xác, cảm biến siêu âm luôn phải đối mặt với các thách thức nội tại:
1. Vận tốc truyền sóng âm trong không khí phụ thuộc phi tuyến vào **nhiệt độ môi trường**, gây trôi điểm đo (thermal drift) từ vài milimet đến hàng centimet khi thời tiết biến đổi.
2. Bản chất bề mặt phản xạ (phẳng nhẵn hay gồ ghề khúc xạ) gây tán xạ năng lượng âm, làm suy giảm nghiêm trọng độ chụm (precision) và cự ly đo xa cực đại.
3. Độ trễ (hysteresis) giữa chiều tiến và chiều lùi, cùng dải vùng chết (blind zone) ở cự ly quá gần do hiện tượng bão hòa đầu thu và dội âm đa hướng.

Xuất phát từ yêu cầu thực tiễn của học phần **Kỹ thuật Đo lường và Cảm biến (`EMA2024E_3`)**, nhóm nghiên cứu đã xây dựng đề tài: *"Khảo sát thực nghiệm đặc tính đo lường của cảm biến siêu âm RCWL-1601 có bù nhiệt độ môi trường trên vi điều khiển ESP32 và ứng dụng đo mức bồn chứa thông minh"*.

Mục tiêu cốt lõi của nghiên cứu bao gồm:
- **Xây dựng hệ thống thu thập thực nghiệm:** Thiết kế đồ gá đo lường cơ khí chính xác và lập trình vi điều khiển ESP32 giao tiếp máy tính để tự động hóa toàn bộ quá trình thu thập tín hiệu thời gian thực.
- **Khảo sát toàn diện các chỉ tiêu tĩnh học:** Đánh giá thực nghiệm các đặc tính đo lường theo tiêu chuẩn quốc tế (ISO/GUM) gồm: Dải đo thực tế, Vùng chết (Blind Zone), Độ chụm (Precision), Độ chính xác (Accuracy), Độ nhạy thực tế (Sensitivity), Độ phân giải (Resolution) và Độ tuyến tính (Linearity).
- **Khảo sát tính trễ (Hysteresis):** Định lượng sai lệch đo lường giữa chiều tiến (Forward) và chiều lùi (Backward), xây dựng đồ thị Vòng trễ thực nghiệm.
- **Định lượng các yếu tố gây nhiễu môi trường:** Đánh giá mức độ suy giảm tín hiệu trên bề mặt gồ ghề tán xạ so với bề mặt phẳng nhẵn; định lượng sai số trôi cự ly do biến thiên nhiệt độ môi trường (phòng thường vs. phòng điều hòa) và kiểm chứng hiệu quả ổn định của thuật toán bù nhiệt độ Laplace.
- **Thiết kế bài toán ứng dụng kỹ thuật:** Ứng dụng các thông số đo lường đã được kiểm chứng để xây dựng hoàn chỉnh **Hệ thống giám sát mức chất lỏng bồn chứa thông minh có bù nhiệt độ và phân ngưỡng cảnh báo tự động trên ESP32**.

Báo cáo được hoàn thành với sự nỗ lực nghiêm túc trong nghiên cứu lý thuyết, đo đạc thực nghiệm và xử lý số liệu thống kê. Nhóm sinh viên xin bày tỏ lòng biết ơn sâu sắc tới các Thầy/Cô bộ môn đã tận tình hướng dẫn và trang bị nền tảng kiến thức quý báu để nhóm hoàn thành công trình này.

---

\newpage

# QUY ƯỚC MÃ HÓA VÀ TỔ CHỨC DỮ LIỆU THỰC NGHIỆM

Toàn bộ dữ liệu thực nghiệm trong nghiên cứu được phân tách rõ ràng thành hai cấp độ lưu trữ: **Tập dữ liệu thô (Raw Datasets)** lưu trong thư mục `result/` và **Tập dữ liệu tổng hợp (Aggregated Datasets)** lưu trong thư mục `du_lieu_tong_hop/`.

### 1. Bảng tổng hợp các bộ kịch bản thực nghiệm:

Để dễ dàng phân biệt các điều kiện ngoại cảnh và tính chất bề mặt đo, tên các kịch bản thực nghiệm được mã hóa chuẩn hóa theo bảng sau:

| Ký hiệu kịch bản | Tên gọi đầy đủ | Đặc tính bề mặt | Nhiệt độ môi trường | Hướng đo | Cỡ mẫu & Mốc đo | Mục đích khảo sát đo lường |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **`100lan...`** | *Thăm dò hội tụ mẫu lớn* | Phẳng nhẵn | Phòng thường ($31^\circ\text{C}$) | Tiến | 100 mẫu/mốc<br>(3 mốc: 50, 100, 150 cm) | Khảo sát quy luật hội tụ sai số Student $\varepsilon_{95\%}$ để luận giải và xác lập cỡ mẫu thực nghiệm chuẩn $N = 50$ lần đo cho toàn bộ các thí nghiệm tiếp theo. |
| **`FSDT`** | *Forward Smooth Default Temp* | Phẳng nhẵn | Phòng thường ($31 - 32^\circ\text{C}$) | Tiến | 50 mẫu/mốc<br>(**35 mốc**: 001 cm $\to$ 600 cm) | **Bộ dữ liệu chuẩn cốt lõi:** Khảo sát vùng chết, dải đo xa cực đại, độ chụm, độ chính xác, độ tuyến tính, độ nhạy và ngân sách độ không đảm bảo đo. |
| **`BSDT`** | *Backward Smooth Default Temp* | Phẳng nhẵn | Phòng thường ($31 - 32^\circ\text{C}$) | Lùi | 50 mẫu/mốc<br>(**19 mốc**: 300 cm $\to$ 010 cm) | Đối chiếu trực tiếp với chuỗi tiến `FSDT` tại cùng 19 mốc để tính độ trễ cực đại $\Delta H_{\max}$, sai số trễ $\gamma_H\%$ và vẽ đồ thị Vòng trễ (Hysteresis Loop). |
| **`FRDT`** | *Forward Rough Default Temp* | Gồ ghề tán xạ | Phòng thường ($31 - 32^\circ\text{C}$) | Tiến | 50 mẫu/mốc<br>(**23 mốc**: 010 cm $\to$ 375 cm) | Đối chiếu với `FSDT` để định lượng hiện tượng tán xạ sóng âm làm tăng độ lệch chuẩn $s$, gây sai số dương và làm suy giảm cự ly đo xa cực đại. |
| **`FSAT`** | *Forward Smooth Air-con Temp* | Phẳng nhẵn | Điều hòa ($20^\circ\text{C}$) | Tiến | 50 mẫu/mốc<br>(**19 mốc**: 010 cm $\to$ 300 cm) | Đối chiếu với `FSDT` để định lượng sai số trôi cự ly (Thermal Drift) và kiểm chứng hiệu quả ổn định kết quả đo của thuật toán bù nhiệt độ Laplace $v(T)$. |

---

### 2. Tổ chức lưu trữ: Dữ liệu thô (`result/`) và Dữ liệu tổng hợp (`du_lieu_tong_hop/`):

#### A. Thư mục dữ liệu thô (`result/`):
Mỗi lần tiến hành đo tại một mốc cự ly cụ thể của một kịch bản, phần mềm thu thập tự động lưu riêng biệt thành một file CSV độc lập theo định dạng `<Kịch_bản>_<XXX>cm.csv` (ví dụ: `FSDT_010cm.csv`, `FSDT_050cm.csv`... với khoảng cách luôn được ghi chuẩn 3 chữ số).

Mỗi file thô chứa đúng 50 hàng dữ liệu liên tiếp (hoặc 100 hàng đối với tập thăm dò `100lan...`), có cấu trúc 3 trường thông tin:
```csv
t,distance_cm,temperature_c
2232.000,39.069596,31.0
2233.000,39.087100,31.0
2232.000,39.069596,31.0
...
```
- `t`: Thời gian bay khứ hồi (Time-of-Flight) của xung siêu âm bắt bằng ngắt timer phần cứng của vi điều khiển ESP32 (đơn vị: $\mu\text{s}$).
- `distance_cm`: Khoảng cách thực tế đã được thuật toán tính toán tức thời (đơn vị: $\text{cm}$).
- `temperature_c`: Giá trị nhiệt độ môi trường ghi nhận tương ứng tại thời điểm thực hiện phép đo (đơn vị: $^\circ\text{C}$).

#### B. Thư mục dữ liệu tổng hợp (`du_lieu_tong_hop/`):
Nhằm phục vụ phân tích so sánh toàn diện trên toàn dải đo, toàn bộ các file thô riêng rẽ trong `result/` sau khi kết thúc đợt đo được xử lý gom lại thành 4 bảng dữ liệu tổng hợp đại diện cho 4 kịch bản:
- `du_lieu_tong_hop/FSDT.csv` (Tổng hợp 35 mốc khoảng cách, bảng 50 dòng $\times$ 35 cột).
- `du_lieu_tong_hop/BSDT.csv` (Tổng hợp 19 mốc khoảng cách, bảng 50 dòng $\times$ 19 cột).
- `du_lieu_tong_hop/FRDT.csv` (Tổng hợp 23 mốc khoảng cách, bảng 50 dòng $\times$ 23 cột).
- `du_lieu_tong_hop/FSAT.csv` (Tổng hợp 19 mốc khoảng cách, bảng 50 dòng $\times$ 19 cột).

Trong mỗi file tổng hợp, mỗi cột tương ứng với một mốc khoảng cách đặt chuẩn (tiêu đề cột là `010cm, 020cm, 040cm...`), và 50 dòng phía dưới là 50 giá trị cự ly đo được rút ra trực tiếp từ cột `distance_cm` của file thô tương ứng. Cấu trúc bảng tổng hợp này giúp các script tính toán ma trận độ lệch chuẩn, vẽ đồ thị phân bố boxplot và tính sai số toàn dải diễn ra thuận tiện, nhất quán và minh bạch.
