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

Để đánh giá đầy đủ, độc lập và toàn diện các đặc tính kỹ thuật của cảm biến trong các điều kiện làm việc khác nhau, hệ thống thực nghiệm thiết lập **4 trường hợp đo chuyên biệt** với các tham số môi trường và hình học đối chứng:

| Tham số | FSDT (Chuẩn) | BSDT (Trễ) | FRDT (Nhám) | FSAT (Nhiệt độ) |
| :--- | :---: | :---: | :---: | :---: |
| **Bề mặt phản xạ** | Mặt nhẵn | Mặt nhẵn | Mặt gồ ghề | Mặt nhẵn |
| **Chiều di chuyển** | Tiến ($1 – 600\text{ cm}$) | Lùi ($300 – 10\text{ cm}$) | Tiến ($10 – 375\text{ cm}$) | Tiến ($10 – 300\text{ cm}$) |
| **Số mốc cự ly** | 35 | 19 | 23 | 19 |
| **Nhiệt độ môi trường** | $27.0^\circ\text{C}$ | $27.0^\circ\text{C}$ | $27.0^\circ\text{C}$ | $20.0^\circ\text{C}$ |
| **Số lần đo lặp N** | 50 | 50 | 50 | 50 |
| **Tổng số mẫu** | 1.750 | 950 | 1.150 | 950 |
| **Mục đích** | Toàn dải, độ chụm, độ chính xác, độ nhạy | Khảo sát độ trễ (Hysteresis) | Khảo sát tán xạ bề mặt | Khảo sát trôi nhiệt độ |

*Bảng 2.2: Bảng tổng hợp các trường hợp đo và thông số thực nghiệm*

---

## 2.4. XÁC ĐỊNH CỠ MẪU TỐI ƯU

### 2.4.1. Bản chất bài toán tối ưu cỡ mẫu trong đo lường siêu âm
Trong kỹ thuật đo lường, kết quả đo khoảng cách thực nghiệm không thể là một giá trị đơn độc, mà luôn được biểu diễn dưới dạng một khoảng tin cậy:

$$d \in [\bar{d} - \varepsilon, \, \bar{d} + \varepsilon] \iff d = \bar{d} \pm \varepsilon$$

Trong đó $\bar{d}$ là trung bình mẫu và $\varepsilon$ là bán kính sai số ngẫu nhiên giới hạn của giá trị trung bình ở mức tin cậy $95\%$. Theo phân phối Student, bán kính sai số $\varepsilon$ được xác định theo mô hình:

$$\varepsilon(N) = t_{0.975, \, N-1} \cdot \frac{s}{\sqrt{N}}$$

Trong đó: $s$ là độ lệch chuẩn đại diện cho độ tán xạ và nhiễu phần cứng thực tế trong môi trường truyền sóng; thừa số $1/\sqrt{N}$ đóng vai trò nén sai số khi tăng số lần đo lặp $N$. Mâu thuẫn đặt ra là: muốn sai số $\varepsilon$ cực nhỏ thì phải tăng $N$ thật lớn, nhưng $N$ càng lớn thì thời gian đo càng dài và nguy cơ trôi nhiệt độ môi trường càng cao. Mục tiêu bài toán là xác định kích thước mẫu $N$ tối ưu để sai số $\varepsilon < 0.5\text{ mm}$ (dung sai vạch chia thước), tốc độ đạo hàm đạt ngưỡng dừng bão hòa ($|d\varepsilon/dN| \approx 0$), và thời gian đo đủ ngắn để môi trường vi khí hậu được coi là bất biến.

---

### 2.4.2. Phân tích dữ liệu thực nghiệm

Thực nghiệm tiến hành đo liên tục 100 lần tại 3 cự ly: $50\text{ cm}$, $100\text{ cm}$ và $150\text{ cm}$ (nhiệt độ $27.0^\circ\text{C}$). Dữ liệu được lưu trữ tại bảng tổng hợp `du_lieu_tong_hop/mau_100.csv`. Thuật toán duyệt $k$ từ 2 đến 100 trên tệp `mau_100.csv` để tính độ lệch chuẩn tích lũy $s(k)$, bán kính sai số $\varepsilon_{95\%}(k)$ và đạo hàm bậc 1. Toàn bộ kết quả được phân tách thành 3 tệp độc lập trong thư mục `du_lieu_tong_hop/chuong_2/`: `hoi_tu_50cm.csv`, `hoi_tu_100cm.csv` và `hoi_tu_150cm.csv`.

![Đồ thị hội tụ bán kính sai số Student 95%](../graph/chuong_2/hinh_2_1_hoi_tu_sai_so_N.png)

*Hình 2.1: Bán kính sai số ngẫu nhiên theo tích lũy cỡ mẫu tại 3 cự ly.*

**Đánh giá từ đồ thị Hình 2.1:** Khi số lần đo $k$ tăng từ 2 đến khoảng 30, bán kính sai số ngẫu nhiên $\varepsilon_{95\%}$ giảm nhanh ở cả 3 cự ly do hệ số Student giảm và mẫu số $\sqrt{k}$ tăng. Từ $k \ge 40 - 50$, đường cong bắt đầu đi ngang và hội tụ ổn định. Tại $k = 50$, bán kính sai số ở cự ly $50\text{ cm}$ là $\pm 0.03\text{ mm}$, ở $100\text{ cm}$ là $\pm 0.11\text{ mm}$, và ở $150\text{ cm}$ là $\pm 0.40\text{ mm}$; tất cả đều nhỏ hơn giới hạn dung sai của thước cơ khí ($\pm 0.5\text{ mm}$).

![Tốc độ biến thiên sai số theo cỡ mẫu k](../graph/chuong_2/hinh_2_2_dao_ham_diem_khuyu_tay.png)

*Hình 2.2: Tốc độ biến thiên sai số |dε_95%/dk| theo cỡ mẫu k.*

**Đánh giá từ đồ thị Hình 2.2:** Đồ thị thể hiện tốc độ suy giảm sai số $|d\varepsilon_{95\%}/dk|$ sau mỗi lần đo bổ sung. Ở các giá trị $k < 20$, tốc độ biến thiên lớn (từ $0.05$ đến $0.15\text{ mm/bước}$), cho thấy việc tăng số lần đo ở giai đoạn đầu giảm sai số rất hiệu quả. Khi $k$ tiến dần đến 50, tốc độ biến thiên giảm nhanh về xấp xỉ 0 ($|d\varepsilon/dk| \le 0.0005\text{ mm/bước} \approx 0$), đồ thị chuyển sang trạng thái bão hòa, việc đo thêm sau mốc 50 hầu như không làm sai số giảm thêm.

Bảng số liệu đối chiếu trích xuất tại các mốc cỡ mẫu:

| Cỡ mẫu $k$ | Mốc 50cm ($\varepsilon_{95\%}$) | Mốc 100cm ($\varepsilon_{95\%}$) | Mốc 150cm ($\varepsilon_{95\%}$) | Nhận xét |
| :---: | :---: | :---: | :---: | :--- |
| **$k = 5$** | $\pm 0.12\text{ mm}$ | $\pm 0.12\text{ mm}$ | $\pm 0.15\text{ mm}$ | Mẫu nhỏ, sai số còn lớn |
| **$k = 10$** | $\pm 0.06\text{ mm}$ | $\pm 0.06\text{ mm}$ | $\pm 0.12\text{ mm}$ | Sai số giảm nhanh nhưng chưa phản ánh đủ biến động |
| **$k = 20$** | $\pm 0.05\text{ mm}$ | $\pm 0.17\text{ mm}$ | $\pm 0.07\text{ mm}$ | Sai số tiếp tục giảm, bắt đầu phân hóa theo cự ly |
| **$k = 30$** | $\pm 0.03\text{ mm}$ | $\pm 0.14\text{ mm}$ | $\pm 0.28\text{ mm}$ | Xuất hiện trượt chu kỳ sóng tại 150cm, sai số tăng lên |
| **$k = 50$ (Tối ưu)** | **$\pm 0.03\text{ mm}$** | **$\pm 0.11\text{ mm}$** | **$\pm 0.40\text{ mm}$** | **Mốc tối ưu:** Sai số nhỏ hơn $0.5\text{ mm}$ ở cả 3 cự ly, đạt bão hòa |
| **$k = 100$** | $\pm 0.02\text{ mm}$ | $\pm 0.08\text{ mm}$ | $\pm 0.27\text{ mm}$ | Vùng bão hòa, sai số hầu như không giảm thêm |

*Bảng 2.3: Bảng trích số liệu của bán kính sai số Student 95%*

**Đánh giá từ Bảng 2.3:** Số liệu định lượng xác nhận xu hướng hội tụ của phép đo. Việc tăng cỡ mẫu từ $k = 10$ lên $k = 50$ giúp giảm sai số hơn 2 lần ở cả 3 cự ly. Tuy nhiên, khi tăng từ $k = 50$ lên $k = 100$, sai số tại mốc 100 cm chỉ giảm thêm $0.03\text{ mm}$ (từ $0.11\text{ mm}$ xuống $0.08\text{ mm}$), giá trị này nhỏ hơn nhiều so với độ phân giải phần cứng của vi điều khiển ($\approx 0.175\text{ mm}$).

**Kết luận:** Dựa trên các phân tích và đánh giá từ hai đồ thị và bảng số liệu nêu trên, nhóm nghiên cứu đưa ra quyết định lựa chọn cỡ mẫu **$N = 50$** cho toàn bộ các phép đo thực nghiệm của đề tài với các lý do:
1. **Đạt tiêu chuẩn dung sai đo lường:** Tại $N = 50$, bán kính sai số ngẫu nhiên $\varepsilon_{95\%}$ ở cả 3 cự ly đều nhỏ hơn dung sai vạch chia của thước chuẩn cơ khí ($\pm 0.5\text{ mm}$): đạt $\pm 0.03\text{ mm}$ tại 50cm; $\pm 0.11\text{ mm}$ tại 100cm; và $\pm 0.40\text{ mm}$ tại 150cm.
2. **Điểm dừng đạo hàm tối ưu bão hòa:** Đồ thị Hình 2.2 chứng minh tại $k = 50$, đạo hàm sai phân $|d\varepsilon/dk| \le 0.0005\text{ mm/bước} \approx 0$, xác nhận đường cong đã bước vào vùng bão hòa. Việc tăng số lần đo lên $N = 100$ chỉ giảm thêm $0.03\text{ mm}$ ở mốc 100cm (nhỏ hơn độ phân giải phần cứng vi điều khiển $\approx 0.175\text{ mm}$).
3. **Bảo toàn tính ổn định vi khí hậu:** Với chu kỳ lấy mẫu $50\text{ ms}$ (tần số quét $20\text{ Hz}$), việc thu thập $N = 50$ mẫu chỉ mất đúng $T_{\text{total}} = 2.5\text{ giây}$ cho mỗi mốc cự ly. Khoảng thời gian $2.5\text{ giây}$ đủ ngắn để nhiệt độ phòng và vi khí hậu được coi là bất biến, loại trừ hiện tượng trôi nhiệt độ môi trường.
