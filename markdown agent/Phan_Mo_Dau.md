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

# MỤC LỤC

*(Nhấp chuột phải vào vùng mục lục trong file Word và chọn 'Update Field' để cập nhật tự động toàn bộ số trang)*

---

\newpage

# BẢNG QUY ƯỚC KÝ HIỆU VÀ DỮ LIỆU THỰC NGHIỆM

#### Bảng 0.1: Bảng quy ước tên 4 tập dữ liệu thực nghiệm chuẩn hóa của đề tài

| Ký hiệu mã | Chiều dịch chuyển | Bề mặt phản xạ | Nhiệt độ môi trường |
| :---: | :---: | :---: | :---: |
| **`FSDT`** | Tiến (Forward) | Phẳng nhẵn bóng<br>(Smooth) | $27.0^\circ\text{C}$ |
| **`BSDT`** | Lùi (Backward) | Phẳng nhẵn bóng<br>(Smooth) | $27.0^\circ\text{C}$ |
| **`FRDT`** | Tiến (Forward) | Nhám gồ ghề<br>(Rough) | $27.0^\circ\text{C}$ |
| **`FSAT`** | Tiến (Forward) | Phẳng nhẵn bóng<br>(Smooth) | $20.0^\circ\text{C}$ |

---

### Cấu trúc tổ chức dữ liệu dự án:

- **Thư mục 'result/':** Lưu trữ toàn bộ các tệp dữ liệu thô ban đầu. Mỗi tệp bao gồm 50 dòng với 3 cột thông tin chuẩn hóa: thời gian bay $t$ ($\mu\text{s}$), khoảng cách đo được `distance_cm` và nhiệt độ `temperature_c`.
- **Thư mục 'du_lieu_tong_hop/':** Lưu trữ các tệp dữ liệu tổng hợp và tính toán. Toàn bộ các phân tích định lượng, khớp hàm và đánh giá độ không đảm bảo đo ở Chương 3 đều được thực thi trực tiếp từ thư mục này.
- **Thư mục 'graph/':** Lưu trữ figure các đồ thị được sử dụng trong bài báo cáo này.
