# BÁO CÁO THỰC NGHIỆM ĐO LƯỜNG VÀ CẢM BIẾN

**BỘ GIÁO DỤC VÀ ĐÀO TẠO**  
**TRƯỜNG ĐẠI HỌC CÔNG NGHỆ**  
**KHOA CƠ HỌC KỸ THUẬT VÀ TỰ ĐỘNG HÓA**  

---

<br>

<div align="center">

# BÁO CÁO THỰC NGHIỆM HỌC PHẦN
## KỸ THUẬT ĐO LƯỜNG VÀ CẢM BIẾN (MÃ HP: `EMA2024E_3`)

<br>

### ĐỀ TÀI:
### KHẢO SÁT THỰC NGHIỆM ĐẶC TÍNH ĐO LƯỜNG CỦA CẢM BIẾN SIÊU ÂM RCWL-1601

<br><br>

**Giảng viên:** TS. Đinh Trần Hiệp  
**Lớp học phần:** EMA2024E_3  
**Nhóm sinh viên thực hiện:**
1. [Họ và tên Sinh viên 1] - MSSV: [Điền MSSV 1]
2. [Họ và tên Sinh viên 2] - MSSV: [Điền MSSV 2]
3. [Họ và tên Sinh viên 3] - MSSV: [Điền MSSV 3]

<br><br>

*HÀ NỘI, THÁNG 11 NĂM 2026*

</div>

<br>

---

\newpage

# LỜI NÓI ĐẦU

Trong tiến trình tự động hóa công nghiệp và phát triển các hệ thống điều khiển thông minh, bài toán đo lường cự ly, vị trí và mức chất lỏng không tiếp xúc đóng vai trò mang tính sống còn. Các hệ thống cảnh báo va chạm của xe tự hành AGV trong nhà máy, trạm phân loại kích thước bao bì kiện hàng trên băng tải logistics, hay các bồn chứa hóa chất ăn mòn đều đòi hỏi phương pháp đo đạc không tiếp xúc vật lý nhằm tránh hỏng hóc cơ học, tránh gây nhiễm bẩn dung dịch và bảo đảm khả năng vận hành liên tục 24/7.

Trong số các công nghệ đo khoảng cách hiện nay (Laser LiDAR, Radar sóng milimét, Cảm biến quang học hồng ngoại và Siêu âm), cảm biến siêu âm nổi lên như một giải pháp cân bằng tối ưu giữa chi phí sản xuất cực thấp, độ bền cơ học cao, không phụ thuộc vào màu sắc hay độ trong suốt của vật thể phản xạ, và đặc biệt an toàn cho người vận hành.

Module cảm biến siêu âm RCWL-1601 thế hệ mới là phiên bản nâng cấp phần cứng vượt trội so với dòng cảm biến kinh điển HC-SR04. Được tích hợp vi mạch điều khiển chuyên dụng RCWL-9610, RCWL-1601 hoàn toàn tương thích mức logic 3.3 V của vi điều khiển ESP32. Bên cạnh đó, việc vận tốc lan truyền sóng âm trong không khí phụ thuộc vào nhiệt độ môi trường là nguồn gốc của sai số trôi cự ly lớn trong điều kiện khí hậu nóng ẩm tại Việt Nam.

Xuất phát từ yêu cầu thực tiễn của học phần Kỹ thuật Đo lường và Cảm biến, nhóm sinh viên đã lựa chọn và thực hiện đề tài: 'Khảo sát thực nghiệm đặc tính đo lường của cảm biến siêu âm RCWL-1601'. Mục tiêu của báo cáo bao gồm:

1. Khảo sát toàn diện đặc tính tĩnh và động học của cảm biến RCWL-1601 trên giàn thực nghiệm chuẩn hóa: xác định dải đo, độ chụm, độ chính xác, đánh giá độ không đảm bảo đo mở rộng.
2. Khảo sát các hiện tượng vật lý chuyên sâu ảnh hưởng đến phép đo siêu âm: độ trễ (Hysteresis), hiện tượng tán xạ trên bề mặt gồ ghề, và hiệu quả bù trôi vận tốc sóng âm Laplace theo nhiệt độ.
3. Xây dựng chuỗi lọc số (Khoảng tứ phân vị IQR) và thiết kế hệ thống: 'Giám sát mức và thể tích bồn chứa thông minh có bù nhiệt độ trên ESP32'.

---

\newpage

# QUY ƯỚC MÃ HÓA VÀ TỔ CHỨC DỮ LIỆU THỰC NGHIỆM

Toàn bộ dữ liệu thực nghiệm trong nghiên cứu được phân tách rõ ràng thành hai cấp độ lưu trữ: **Tập dữ liệu thô (Raw Datasets)** lưu trong thư mục `result/` và **Tập dữ liệu tổng hợp (Aggregated Datasets)** lưu trong thư mục `du_lieu_tong_hop/`.

### 1. Bảng quy ước định danh 4 tập dữ liệu thực nghiệm chuẩn hóa của đề tài:

| Ký hiệu mã | Chiều dịch chuyển | Bề mặt phản xạ | Nhiệt độ môi trường | Mục đích khảo sát đo lường |
| :---: | :---: | :---: | :---: | :--- |
| **`FSDT`** | Tiến (Forward)<br>$1\text{ cm} \to 600\text{ cm}$ | Phẳng nhẵn bóng<br>(Specular) | $27.0^\circ\text{C}$<br>(Nhiệt độ phòng) | Khảo sát đặc tính tĩnh toàn dải, xác định vùng chết ($1 \div 3\text{ cm}$), độ chụm, độ chính xác, độ tuyến tính và phân tích tổng hợp độ không đảm bảo đo ISO/GUM. |
| **`BSDT`** | Lùi (Backward)<br>$300\text{ cm} \to 10\text{ cm}$ | Phẳng nhẵn bóng<br>(Specular) | $27.0^\circ\text{C}$<br>(Nhiệt độ phòng) | Đối chiếu với chuỗi tiến `FSDT` để đánh giá đặc tính động học, hiện tượng trễ cơ - điện (Hysteresis) và tính toán sai số trễ tương đối $\gamma_H\%$. |
| **`FRDT`** | Tiến (Forward)<br>$10\text{ cm} \to 375\text{ cm}$ | Gồ ghề nhám xốp<br>(Diffuse) | $27.0^\circ\text{C}$<br>(Nhiệt độ phòng) | Đánh giá hiện tượng tán xạ khuếch tán, độ suy giảm tỷ số $S/N$ và giới hạn tầm đo trên bề mặt xốp. |
| **`FSAT`** | Tiến (Forward)<br>$10\text{ cm} \to 300\text{ cm}$ | Phẳng nhẵn bóng<br>(Specular) | $20.0^\circ\text{C}$<br>(Phòng điều hòa) | Khảo sát độ trôi cự ly do vận tốc âm và kiểm chứng hiệu quả thuật toán bù nhiệt Laplace. |

---

### 2. Phân định cấu trúc tổ chức dữ liệu dự án:

- **Thư mục `result/`:** Lưu trữ toàn bộ các tệp dữ liệu thô ban đầu được ghi nhận trực tiếp từ vi điều khiển ESP32 theo từng mốc cự ly đơn lẻ. Mỗi tệp bao gồm 50 dòng đo lường với 3 trường thông tin chuẩn hóa: thời gian bay hai chiều $t$ ($\mu\text{s}$), khoảng cách đo được `distance_cm` ($\text{cm}$) và nhiệt độ môi trường ghi nhận `temperature_c` ($^\circ\text{C}$). Quy ước đặt tên tệp: `<MÃ_TẬP>_<XXX>cm.csv` (ví dụ: `FSDT_010cm.csv`, `FSDT_100cm.csv`).
- **Thư mục `du_lieu_tong_hop/`:** Lưu trữ các tệp dữ liệu tổng hợp đã được hợp nhất. Mỗi tệp tổ chức cấu trúc bảng ma trận với các cột là các mốc cự ly khảo sát và các hàng là 50 lần đo tương ứng. Toàn bộ các phân tích định lượng, hồi quy ma trận và đánh giá độ không đảm bảo đo ở Chương 3 đều được thực thi trực tiếp từ thư mục này.
