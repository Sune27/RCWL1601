# CHƯƠNG 2: THIẾT KẾ THỰC NGHIỆM

---

## 2.1. MỤC TIÊU VÀ PHƯƠNG PHÁP LUẬN THỰC NGHIỆM

### 2.1.1. Mục tiêu thực nghiệm
Mục tiêu cốt lõi của Chương 2 là thiết kế và chuẩn hóa toàn bộ quy trình đo lường thực nghiệm cho module cảm biến siêu âm RCWL-1601 trên vi điều khiển ESP32, đảm bảo số liệu thu thập được có độ tin cậy khoa học cao và loại trừ tối đa các sai số hệ thống do môi trường và thiết bị. Cụ thể, hệ thống thực nghiệm được thiết kế nhằm đạt được các mục tiêu sau:
1. **Kiểm chứng dải đo thực tế và vùng chết:** Đánh giá giới hạn đo cực cận (vùng chết dưới $5\text{ cm}$) và khả năng đo xa thực tế trên bề mặt phản xạ phẳng nhẵn so với thông số định mức $400\text{ cm}$ theo Datasheet của nhà sản xuất.
2. **Khảo sát toàn diện các chỉ tiêu đo lường tĩnh học:** Thu thập dữ liệu chuẩn hóa phục vụ việc tính toán các đặc tính tĩnh học theo tiêu chuẩn quốc tế ISO/GUM (độ chụm, độ chính xác, độ nhạy thực tế, độ phân giải, độ tuyến tính, độ trễ và đánh giá tổng hợp độ không đảm bảo đo mở rộng).
3. **Định lượng các yếu tố gây nhiễu môi trường:** Đánh giá định lượng tác động của hiện tượng tán xạ sóng âm trên bề mặt gồ ghề (`FRDT`) so với bề mặt phẳng nhẵn (`FSDT`), cũng như tác động của sự thay đổi nhiệt độ môi trường (`FSDT` phòng thường $31^\circ\text{C}$ vs. `FSAT` phòng điều hòa $20^\circ\text{C}$) lên hiện tượng trôi cự ly (Thermal Drift).
4. **Xác lập bộ tham số thực nghiệm cho bài toán ứng dụng:** Làm cơ sở dữ liệu thực nghiệm chuẩn xác để tính toán thiết kế chiều cao lắp đặt, chuỗi bộ lọc số và thuật toán bù nhiệt độ cho hệ thống đo mức chất lỏng bồn chứa thông minh ở Chương 4.

---

### 2.1.2. Phương pháp luận thực nghiệm
Phương pháp luận được áp dụng là **phương pháp đo so sánh trực tiếp với vật chuẩn (Direct Comparison with Standard)**:
- **Chuẩn so sánh (Reference Standard):** Khoảng cách thực $d_{\text{true}}$ được xác lập bằng thước đo tiêu chuẩn có độ chia nhỏ nhất đến milimet với sai số giới hạn $\Delta_{\text{ruler}} = \pm 1\text{ mm}$ ($\pm 0.1\text{ cm}$).
- **Đối tượng đo (Measurement Object):** Khoảng cách đo được $d$ suy ra từ thời gian bay ToF của chùm sóng siêu âm phát ra từ cảm biến RCWL-1601, được vi điều khiển ESP32 số hóa với độ phân giải thời gian $1\text{ }\mu\text{s}$ và cập nhật thuật toán bù nhiệt độ môi trường Laplace $v(T) = 331.3 + 0.606 \cdot T$.
- **Nguyên tắc lặp lại:** Tại mỗi mốc cự ly đặt chuẩn $d_{\text{true}}$, phép đo được kích hoạt lặp lại nhiều lần trong cùng một trạng thái ổn định cơ khí và nhiệt độ để phục vụ phân tích thống kê ngẫu nhiên.

```
       [ Thước đo chuẩn vạch milimet căng giữa hai mép bàn ]
  |===================================================================|
  [RCWL-1601 trên Breadboard] ---------- Sóng ToF ----------> [Viên gạch 40x40 cm]
  (Sát mép bàn 1, độ cao 85 cm)                              (Mép bàn 2, vuông góc mặt bàn)
            |
      (GPIO 5 & 18)
            v
  [Vi điều khiển ESP32] ===== Cáp UART/COM =====> [Máy tính thu thập CSV]
```

---

## 2.2. THIẾT KẾ PHẦN CỨNG VÀ KHÔNG GIAN THỰC NGHIỆM

### 2.2.1. Thiết kế phần cứng và sơ đồ kết nối điện
Hệ thống đo lường sử dụng module cảm biến siêu âm RCWL-1601 kết nối trực tiếp với vi điều khiển ESP32. Cảm biến được cấp nguồn trực tiếp từ chân 3V3 của ESP32. Các đường tín hiệu TRIG và ECHO giao tiếp trực tiếp với các chân GPIO của ESP32 ở mức logic 3.3V mà không cần mạch chuyển đổi mức logic.

Sơ đồ kết nối phần cứng chi tiết:

| Chân RCWL-1601 | Chân ESP32 | Chức năng kỹ thuật |
| :---: | :---: | :--- |
| **`VCC`** | **`3V3`** | Cấp nguồn nuôi cảm biến |
| **`GND`** | **`GND`** | Nối đất chung |
| **`TRIG`** | **`GPIO 5`** | Ngõ vào kích phát xung |
| **`ECHO`** | **`GPIO 18`** | Ngõ ra phản hồi thời gian bay |

---

### 2.2.2. Thiết kế không gian và kiểm soát điều kiện môi trường thực nghiệm
Đặc tính sóng siêu âm có hình nón đòi hỏi không gian đo phải được tính toán để loại trừ các phản xạ phụ:
- **Chiều cao bàn đo ($H_{	ext{table}} = 85	ext{ cm}$):** Hệ thống cảm biến và viên gạch phản xạ được đặt trên hai bàn thí nghiệm có độ cao $H_{	ext{table}} = 85.0	ext{ cm}$ so với mặt sàn phòng đo, đảm bảo búp sóng không quét chạm vào nền sàn.
- **Nhiệt độ phòng đo và vi khí hậu:** Thực nghiệm được bố trí dọc theo hành lang kín gió dài 10 m, chiều rộng 2.8 m. Cảm biến đặt cách tường bên ít nhất 1.4 m. Trong suốt quá trình đo, hệ thống cửa được đóng kín tránh gió lùa và biến thiên nhiệt độ đột ngột.

---

### 2.2.3. Bố trí mô hình và định vị thiết bị đo
Để đảm bảo phép đo đạt độ chính xác cao và hạn chế tối đa sai số góc lệch trục, mô hình thực nghiệm được bố trí khoa học và chắc chắn:
1. **Cố định cảm biến tại vị trí mốc đo gốc:** Module cảm biến RCWL-1601 được cắm cố định vững chắc trên breadboard. Breadboard gắn cảm biến cùng vi điều khiển ESP32 và máy tính thu thập dữ liệu được đặt trên bàn có độ cao khoảng $85	ext{ cm}$ so với mặt sàn. Cảm biến được bố trí ở sát mép bàn, hướng hai mắt phát - thu trực diện ra ngoài.
2. **Vật thể phản xạ mục tiêu:** Vật thể đo chuẩn là một viên gạch kích thước $40 	imes 40	ext{ cm}$ có hai mặt với đặc tính bề mặt khác nhau: mặt trước phẳng nhẵn và mặt sau gồ ghề. Viên gạch được dựng thẳng đứng sát mép của chiếc bàn có cùng chiều cao $85	ext{ cm}$. Khi tiến hành đo, viên gạch luôn được căn chỉnh vuông góc với mặt bàn và đối diện trực diện với trục phát của cảm biến.
3. **Căn chỉnh cự ly bằng thước đo tiêu chuẩn:** Khoảng cách chuẩn $d_{	ext{true}}$ được xác định thủ công bằng thước dây đo chuẩn có độ chia nhỏ nhất đến milimet. Thước được căng thẳng giữa hai mép bàn để định vị chính xác từng mốc cự ly đo trước khi người thực nghiệm phát lệnh kích hoạt cảm biến đo và ghi nhận chuỗi dữ liệu trên máy tính.

---

## 2.3. CÁC TRƯỜNG HỢP ĐO VÀ ĐIỀU KIỆN THỰC NGHIỆM

Để đánh giá đầy đủ, độc lập và toàn diện các đặc tính kỹ thuật của cảm biến trong các điều kiện làm việc khác nhau, hệ thống thực nghiệm thiết lập **4 trường hợp đo chuyên biệt** với các tham số môi trường và hình học đối chứng:

| Tham số khảo sát | Trường hợp 1: `FSDT` *(Đo chuẩn)* | Trường hợp 2: `BSDT` *(Khảo sát trễ)* | Trường hợp 3: `FRDT` *(Mặt gồ ghề)* | Trường hợp 4: `FSAT` *(Nhiệt độ thấp)* |
| :--- | :---: | :---: | :---: | :---: |
| **Bề mặt phản xạ** | Mặt trước nhẵn (Viên gạch $40 \times 40\text{ cm}$) | Mặt trước nhẵn (Viên gạch $40 \times 40\text{ cm}$) | Mặt sau gồ ghề (Viên gạch $40 \times 40\text{ cm}$) | Mặt trước nhẵn (Viên gạch $40 \times 40\text{ cm}$) |
| **Chiều di chuyển** | Tiến ($1\text{ cm} \to 600\text{ cm}$) | Lùi ($300\text{ cm} \to 10\text{ cm}$) | Tiến ($10\text{ cm} \to 375\text{ cm}$) | Tiến ($10\text{ cm} \to 300\text{ cm}$) |
| **Nhiệt độ môi trường** | Phòng thường ($27.0^\circ\text{C}$) | Phòng thường ($27.0^\circ\text{C}$) | Phòng thường ($27.0^\circ\text{C}$) | Phòng điều hòa ($20.0^\circ\text{C}$) |
| **Số lần đo/mốc ($N$)** | $50$ lần đo | $50$ lần đo | $50$ lần đo | $50$ lần đo |
| **Số mốc cự ly ($K$)** | **35 mốc** | **19 mốc** | **23 mốc** | **19 mốc** |
| **Tổng số mẫu đo** | $1.750$ mẫu | $950$ mẫu | $1.150$ mẫu | $950$ mẫu |
| **Mục đích chính** | Khảo sát đặc tính tĩnh toàn dải | Đánh giá độ trễ Hysteresis Loop | Đánh giá tán xạ suy giảm biên độ | Khảo sát trôi nhiệt & bù Laplace |

---

## 2.4. CƠ SỞ THỐNG KÊ VÀ THỰC NGHIỆM XÁC ĐỊNH CỠ MẪU TỐI ƯU N = 50

Trong thiết kế thực nghiệm đo lường, việc lựa chọn số lần đo lặp lại $N$ tại mỗi điểm đo là một quyết định kỹ thuật mang tính chiến lược:
- Nếu chọn $N$ quá nhỏ ($N < 15$): Sai số ngẫu nhiên lớn, độ không đảm bảo đo cao, kết quả không đủ độ tin cậy để đại diện cho bản chất cảm biến.
- Nếu chọn $N$ quá lớn ($N \ge 100$): Tốn kém thời gian thao tác, tăng nguy cơ gây trôi nhiệt độ môi trường theo thời gian, đồng thời hiệu quả giảm sai số thu được không đáng kể.

Để giải quyết mâu thuẫn này một cách khoa học, nhóm nghiên cứu đã tiến hành một thí nghiệm thăm dò quy mô lớn gồm $100$ lần đo liên tục tại 3 cự ly thực nghiệm tiêu biểu: cự ly gần ($50\text{ cm}$), cự ly trung bình ($100\text{ cm}$) và cự ly xa ($150\text{ cm}$) lưu trong 3 file dữ liệu `100lanforward_smooth_defttemp_050cm.csv`, `100cm.csv`, `150cm.csv`.

### 2.4.1. Cơ sở lý thuyết đường cong hội tụ Student 95%
Khi số mẫu đo tăng dần từ $k = 2 \to 100$, độ không đảm bảo đo ngẫu nhiên của giá trị trung bình $\bar{x}(k)$ ở mức xác suất tin cậy $95\%$ được định lượng bằng **Bán kính khoảng tin cậy Student 95% ($\varepsilon_{95\%}$)**:

$$\varepsilon_{95\%}(k) = t_{0.975, \, k-1} \cdot \frac{s(k)}{\sqrt{k}}$$

Trong đó:
- $k$: Cỡ mẫu tích lũy khảo sát ($k = 2, 3, \dots, 100$).
- $s(k) = \sqrt{\frac{1}{k-1} \sum_{i=1}^k (x_i - \bar{x}(k))^2}$: Độ lệch chuẩn thực nghiệm tính trên $k$ mẫu đầu tiên.
- $t_{0.975, \, k-1}$: Phân vị phân phối Student bậc tự do $k-1$ ứng với độ tin cậy hai phía $95\%$ (với $k=3 \to t=4.303$, $k=10 \to t=2.262$, $k=30 \to t=2.042$, $k=50 \to t=2.009$, $k=100 \to t=1.984$).

---

### 2.4.2. Biểu đồ hội tụ thực nghiệm và Bảng số liệu đối chiếu
Đồ thị biểu diễn sự biến thiên của bán kính khoảng tin cậy $\varepsilon_{95\%}(k)$ theo số lượng mẫu đo tích lũy $k$ tại 3 cự ly được thể hiện trên hình dưới đây:

![Đồ thị hội tụ bán kính khoảng tin cậy Student 95% và chốt N=50](../graph/bieu_do_chot_N50_student_t95.png)

*Hình 2.1: Quy luật hội tụ bán kính khoảng tin cậy Student 95% $\varepsilon_{95\%}(k)$ theo số mẫu $k$ tại 3 cự ly (50cm, 100cm, 150cm) và mốc chốt tối ưu N = 50.*

Bảng số liệu đối chiếu giá trị $\varepsilon_{95\%}(k)$ trích xuất tại các mốc cỡ mẫu tiêu biểu (đơn vị: milimet - $\text{mm}$):

| Cỡ mẫu khảo sát $k$ | Hệ số Student $t_{0.975}$ | Mốc 50cm: $\varepsilon_{95\%}$ (mm) | Mốc 100cm: $\varepsilon_{95\%}$ (mm) | Mốc 150cm: $\varepsilon_{95\%}$ (mm) | Nhận xét trạng thái kỹ thuật |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$k = 5$** | 2.776 | $\pm 0.11\text{ mm}$ | $\pm 0.62\text{ mm}$ | $\pm 1.25\text{ mm}$ | Sai số vượt ngưỡng dung sai cho phép ($> 0.5\text{ mm}$) |
| **$k = 10$** | 2.262 | $\pm 0.07\text{ mm}$ | $\pm 0.34\text{ mm}$ | $\pm 0.89\text{ mm}$ | Sai số đang giảm dốc đứng theo hàm $1/\sqrt{k}$ |
| **$k = 20$** | 2.086 | $\pm 0.04\text{ mm}$ | $\pm 0.21\text{ mm}$ | $\pm 0.58\text{ mm}$ | Mốc 50cm và 100cm bắt đầu phẳng, 150cm vẫn biến động |
| **$k = 30$** | 2.042 | $\pm 0.03\text{ mm}$ | $\pm 0.15\text{ mm}$ | $\pm 0.46\text{ mm}$ | **Chạm điểm khuỷu tay (Elbow Point)** |
| **$k = 50$** | **2.009** | **$\pm 0.03\text{ mm}$** | **$\pm 0.11\text{ mm}$** | **$\pm 0.40\text{ mm}$** | **MỐC CHỐT TỐI ƯU $N = 50$ (Tất cả đều $< 0.4\text{ mm}$)** |
| **$k = 100$** | 1.984 | $\pm 0.02\text{ mm}$ | $\pm 0.08\text{ mm}$ | $\pm 0.27\text{ mm}$ | Vùng bão hòa, chỉ giảm thêm $\approx 0.1\text{ mm}$ dù tốn gấp 2 lần mẫu |

---

### 2.4.3. Luận giải khoa học quyết định lựa chọn cỡ mẫu $N = 50$
Dựa trên hình ảnh đồ thị và bảng số liệu thực nghiệm, quyết định lựa chọn $N = 50$ lần đo cho toàn bộ các thí nghiệm được bảo vệ thông qua 3 luận cứ khoa học then chốt:

1. **Vượt qua điểm khuỷu tay và đạt tiêu chuẩn dung sai kỹ thuật:**
   - Trong khoảng $k = 2 \to 30$, đường sai số $\varepsilon_{95\%}$ rơi dốc đứng. Từ $k \approx 30 - 35$ trở đi, đường cong đi qua điểm khuỷu tay và bắt đầu chuyển sang pha tiệm cận phẳng.
   - Tại mốc $N = 50$, bán kính sai số khoảng tin cậy của cả 3 cự ly đều nằm gọn dưới ngưỡng dung sai cho phép $\pm 0.5\text{ mm}$ ($\pm 0.03\text{ mm}$ ở cự ly $50\text{ cm}$, $\pm 0.11\text{ mm}$ ở cự ly $100\text{ cm}$, và $\pm 0.40\text{ mm}$ ở cự ly $150\text{ cm}$).
2. **Giải quyết hiện tượng trượt chu kỳ sóng ở cự ly xa:**
   - Quan sát đường cong mốc $150\text{ cm}$, ta thấy đường sai số vẫn còn gợn sóng biến động trong khoảng $k = 20 \to 35$. Hiện tượng này xuất phát từ bản chất vật lý: ở cự ly xa, biên độ sóng phản xạ suy giảm, khiến mạch so sánh điện áp ở đầu thu thỉnh thoảng bị trượt đúng một chu kỳ sóng siêu âm ($T = 1/40\text{ kHz} = 25\text{ }\mu\text{s} \to \Delta d \approx 4.3\text{ mm}$). 
   - Nếu chỉ đo $N = 20 - 30$ lần, các điểm trượt chu kỳ này sẽ kéo lệch giá trị trung bình. Phải đến khi đạt cỡ mẫu **$N \ge 45 - 50$**, số lượng mẫu lớn mới trung hòa và làm phẳng hoàn toàn các điểm đột biến này, đưa sai số về trạng thái bão hòa ổn định.
3. **Quy luật hiệu suất giảm dần (Diminishing Returns) và tối ưu hóa thời gian đo:**
   - So sánh giữa $N = 50$ và $N = 100$: Khi tăng gấp đôi số lần đo từ 50 lên 100 lần, sai số khoảng tin cậy chỉ giảm thêm một lượng không đáng kể là **$0.13\text{ mm}$** ở mốc $150\text{ cm}$ và **$0.03\text{ mm}$** ở mốc $100\text{ cm}$ (nhỏ hơn cả độ phân giải của bộ đếm thời gian vi điều khiển $\approx 0.17\text{ mm}$).
   - Trong khi đó, việc tăng lên 100 lần đo sẽ làm tăng tổng số lượt đo của toàn bộ đề tài từ $4.800$ lần lên gần $10.000$ lần, kéo dài thời gian thí nghiệm và làm tăng nguy cơ trôi nhiệt độ phòng.

$\Rightarrow$ **Kết luận:** Lựa chọn **$N = 50$ lần đo/mốc** là điểm cân bằng hoàn hảo nhất giữa tính khả thi thực nghiệm và độ chính xác đo lường khoa học, bảo đảm độ tin cậy $95\%$ cho toàn bộ các tập dữ liệu `FSDT`, `BSDT`, `FRDT`, `FSAT`.
