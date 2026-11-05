# CHƯƠNG 2: THIẾT KẾ VÀ BỐ TRÍ THỰC NGHIỆM

---

## 2.1. MỤC TIÊU THỰC NGHIỆM

### 2.1.1. Mục tiêu thực nghiệm
Nghiên cứu thực nghiệm được thiết kế nhằm mục đích kiểm chứng các đặc tính đo lường của module cảm biến siêu âm RCWL-1601: Khảo sát dải đo thực tế, định lượng độ chụm và độ chính xác, đánh giá độ tuyến tính, đánh giá ảnh hưởng của nhiệt độ môi trường, đánh giá ảnh hưởng của bề mặt phản xạ, đánh giá độ trễ

---

## 2.2. THIẾT KẾ PHẦN CỨNG VÀ KHÔNG GIAN THỰC NGHIỆM

### 2.2.1. Thiết kế phần cứng và sơ đồ kết nối điện
Module cảm biến siêu âm RCWL-1601 được kết nối trực tiếp với vi điều khiển ESP32. Các đường tín hiệu TRIG và ECHO giao tiếp trực tiếp với các chân GPIO của ESP32 ở mức logic 3.3 V.

Bảng 2.1: Sơ đồ kết nối phần cứng giữa cảm biến RCWL-1601 và vi điều khiển ESP32

| Chân RCWL-1601 | Chân ESP32 | Chức năng kỹ thuật |
| :---: | :---: | :--- |
| **VCC** | **3V3** | Cấp nguồn nuôi cảm biến |
| **GND** | **GND** | Nối đất chung hệ thống |
| **TRIG** | **GPIO 5** | Ngõ vào kích phát xung siêu âm |
| **ECHO** | **GPIO 18** | Ngõ ra phản hồi thời gian bay ToF |

---

### 2.2.2. Thiết kế không gian thực nghiệm
• Chiều cao bàn đo 85 cm: Hệ thống cảm biến và vật đo được đặt trên hai bàn thí nghiệm có độ cao 85.0 cm so với mặt sàn phòng đo.

• Phòng đo: Thực nghiệm được bố trí dọc theo hành lang kín gió dài 10 m, chiều rộng 2.8 m. Cảm biến đặt cách tường bên ít nhất 1.4 m. Trong suốt quá trình đo, hệ thống cửa được đóng kín tránh gió lùa và biến thiên nhiệt độ đột ngột.

---

### 2.2.3. Bố trí mô hình và định vị thiết bị đo
Để đảm bảo phép đo đạt độ chính xác cao, mô hình thực nghiệm được bố trí:
1. Cố định cảm biến: RCWL-1601 được cắm cố định vững chắc trên breadboard, sát mép bàn, hướng hai mắt phát - thu trực diện ra ngoài.
2. Vật thể phản xạ mục tiêu: Vật thể đo chuẩn là một viên gạch kích thước 40 cm × 40 cm có mặt trước phẳng nhẵn và mặt sau gồ ghề. Viên gạch được dựng thẳng đứng sát mép của chiếc bàn có cùng chiều cao 85 cm. Khi tiến hành đo, viên gạch luôn được căn chỉnh vuông góc với mặt bàn và đối diện với trục phát của cảm biến.
3. Căn chỉnh cự ly bằng thước đo tiêu chuẩn: Khoảng cách chuẩn d_true được xác định thủ công bằng thước dây. 

---

## 2.3. CÁC TRƯỜNG HỢP ĐO VÀ ĐIỀU KIỆN THỰC NGHIỆM

Để đánh giá đầy đủ, độc lập và toàn diện các đặc tính kỹ thuật, nghiên cứu thiết lập 4 trường hợp đo chuyên biệt với các điều kiện môi trường tương ứng:

| Tham số | FSDT | BSDT | FRDT | FSAT |
| :--- | :---: | :---: | :---: | :---: |
| **Bề mặt phản xạ** | Mặt nhẵn | Mặt nhẵn | Mặt gồ ghề | Mặt nhẵn |
| **Chiều di chuyển** | Tiến (1 – 600 cm) | Lùi (300 – 10 cm) | Tiến (10 – 375 cm) | Tiến (10 – 300 cm) |
| **Số mốc cự ly** | 35 | 19 | 23 | 19 |
| **Nhiệt độ môi trường** | 27.0 °C | 27.0 °C | 27.0 °C | 20.0 °C |
| **Tổng số mẫu** | 1.750 | 950 | 1.150 | 950 |
| **Mục đích** | Khảo sát toàn dải, độ chụm, độ chính xác, độ nhạy | Khảo sát độ trễ | Khảo sát tán xạ bề mặt | Khảo sát trôi nhiệt độ |

*Bảng 2.2: Bảng tổng hợp các trường hợp đo và thông số thực nghiệm*

---

## 2.4. XÁC ĐỊNH CỠ MẪU TỐI ƯU

### 2.4.1. Tối ưu cỡ mẫu
Trong kỹ thuật đo lường, kết quả đo khoảng cách thực nghiệm không thể là một giá trị đơn độc, mà luôn được biểu diễn dưới dạng một khoảng tin cậy: $d \in [\bar{d} - \varepsilon, \, \bar{d} + \varepsilon]$ (tương đương $d = \bar{d} \pm \varepsilon$), trong đó $\bar{d}$ là trung bình mẫu và $\varepsilon$ là bán kính sai số ngẫu nhiên giới hạn của giá trị trung bình ở mức tin cậy $95\%$.

Theo lý thuyết xác suất thống kê và phân phối Student, bán kính sai số $\varepsilon$ được xác định bởi mô hình:

$$\varepsilon(N) = \frac{t_{0.975, \, N-1} \cdot s}{\sqrt{N}} \quad (2.1)$$

Trong đó: $s$ là độ lệch chuẩn thực nghiệm đại diện cho độ tán xạ và nhiễu phần cứng thực tế trong môi trường truyền sóng; thừa số $1/\sqrt{N}$ đóng vai trò nén sai số khi tăng số lần đo lặp $N$. 

Mâu thuẫn đặt ra là: muốn sai số $\varepsilon$ cực nhỏ thì phải tăng $N$ thật lớn, nhưng $N$ càng lớn thì thời gian đo càng dài. Mục tiêu bài toán là xác định kích thước mẫu $N$ tối ưu để sai số $\varepsilon < 0.5\text{ mm}$ (dung sai vạch chia thước), tốc độ đạo hàm đạt ngưỡng dừng bão hòa ($|d\varepsilon/dN| \approx 0$), và thời gian đo đủ ngắn.

---

### 2.4.2. Phân tích dữ liệu thực nghiệm

Thực nghiệm tiến hành đo liên tục 100 lần tại 3 cự ly: 50 cm, 100 cm và 150 cm (nhiệt độ 27.0°C). Dữ liệu được lưu trữ tại “du_lieu_tong_hop/mau_100.csv”. Tính độ lệch chuẩn tích lũy $s(k)$, bán kính sai số $\varepsilon_{95\%}(k)$ và đạo hàm bậc 1. Kết quả tính toán được ghi lại trong “du_lieu_tong_hop/chuong_2”

![Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu](../graph/chuong_2/hinh_2_1_hoi_tu_sai_so_N.png)

*Hình 2.1: Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu.*

Đánh giá từ đồ thị Hình 2.1: Khi số lần đo $k$ tăng từ 2 đến khoảng 30, bán kính sai số ngẫu nhiên $\varepsilon_{95\%}$ giảm nhanh ở cả 3 cự ly. Từ $k \ge 40 - 50$, đường cong bắt đầu đi ngang và hội tụ ổn định. 

![Tốc độ biến thiên sai số theo cỡ mẫu k](../graph/chuong_2/hinh_2_2_dao_ham_diem_khuyu_tay.png)

*Hình 2.2: Tốc độ biến thiên sai số |dε_95%/dk| theo cỡ mẫu k.*

Đánh giá từ đồ thị Hình 2.2: Đồ thị thể hiện tốc độ suy giảm sai số $|d\varepsilon_{95\%}/dk|$ sau mỗi lần đo bổ sung. Ở các giá trị $k < 20$, tốc độ biến thiên cực lớn, cho thấy việc tăng số lần đo ở giai đoạn đầu giảm sai số rất hiệu quả. Khi $k$ tiến dần đến 50, tốc độ biến thiên giảm nhanh, đường đồ thị chuyển sang đi ngang, việc đo thêm sau mốc 50 hầu như không làm sai số giảm hiệu quả như ban đầu.

Kết luận: Dựa trên các phân tích và đánh giá từ hai đồ thị và bảng số liệu nêu trên, nhóm nghiên cứu đưa ra quyết định lựa chọn cỡ mẫu $N = 50$ cho toàn bộ các phép đo thực nghiệm.
