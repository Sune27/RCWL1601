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

### 2.4.1. Bản chất bài toán tối ưu cỡ mẫu trong đo lường siêu âm
Trong kỹ thuật đo lường, kết quả đo khoảng cách thực nghiệm không thể là một giá trị đơn độc, mà luôn được biểu diễn dưới dạng một khoảng tin cậy:

$$d \in [\bar{d} - \varepsilon, \, \bar{d} + \varepsilon] \iff d = \bar{d} \pm \varepsilon$$

Trong đó:
- $\bar{d}$: Giá trị trung bình mẫu quan sát.
- $\varepsilon$: Bán kính sai số ngẫu nhiên giới hạn của giá trị trung bình ở mức xác suất tin cậy $95\%$.

Theo lý thuyết xác suất thống kê và phân phối Student, bán kính sai số $\varepsilon$ được xác định theo mô hình:

$$\varepsilon(N) = t_{0.975, \, N-1} \cdot \frac{s}{\sqrt{N}}$$

Trong biểu thức trên:
1. Độ lệch chuẩn thực nghiệm $s$ phản ánh bản chất nhiễu phần cứng và độ tán xạ sóng âm thực tế của cảm biến trong không khí.
2. Thừa số $\frac{1}{\sqrt{N}}$ đóng vai trò nén sai số: số lần đo lặp lại $N$ càng lớn thì sai số ngẫu nhiên $\varepsilon$ càng thu hẹp.

**Mâu thuẫn kỹ thuật dẫn tới bài toán tối ưu:**
- Nếu muốn sai số $\varepsilon$ nhỏ tối đa $\to$ Cần tăng số lần đo $N$ thật lớn.
- Tuy nhiên, khi $N$ tăng cao $\to$ Thời gian đo kéo dài, tải tính toán tăng, và nguy hiểm nhất là dẫn tới hiện tượng **trôi nhiệt độ môi trường** (Thermal Drift). Khi nhiệt độ không khí thay đổi (dù chỉ $0.5 - 1.0^\circ\text{C}$), vận tộc âm thanh $v(T)$ sẽ thay đổi và tạo ra sai số hệ thống ngược lại.
- Đồng thời, do quy luật hàm số mũ ngược $\frac{1}{\sqrt{N}}$, tốc độ thu hẹp sai số sẽ giảm dần (hiệu suất biên giảm dần).
- $\Rightarrow$ **Mục tiêu kỹ thuật:** Xác định kích thước mẫu tối ưu $N$ sao cho:
  1. Sai số ngẫu nhiên $\varepsilon_{95\%}$ nhỏ hơn dung sai cho phép của thước đo chuẩn đối chứng ($\pm 0.5\text{ mm}$).
  2. Tốc độ suy giảm sai số đã chạm ngưỡng dừng bão hòa ($|d\varepsilon/dN| \approx 0$).
  3. Thời gian đo $T_{\text{total}}$ đủ ngắn để môi trường vi khí hậu được coi là bất biến.

---

### 2.4.2. Dữ liệu thực nghiệm và Phân tích đạo hàm hội tụ

#### A. Dữ liệu thực nghiệm
Chuỗi thí nghiệm lấy mẫu liên tục 100 lần đo tại 3 cự ly thực nghiệm tiêu biểu: gần ($50\text{ cm}$), trung bình ($100\text{ cm}$) và xa ($150\text{ cm}$) ở chu kỳ lấy mẫu $50\text{ ms}$ (tần số $20\text{ Hz}$, nhiệt độ kiểm soát $27.0^\circ\text{C}$). Dữ liệu được lưu trữ tập trung tại bảng tổng hợp:
- **`du_lieu_tong_hop/mau_100.csv`** (bảng 100 dòng $\times$ 3 cột: `d_50cm_cm`, `d_100cm_cm`, `d_150cm_cm`).

#### B. Thuật toán tính toán và Đạo hàm sai phân
Thuật toán duyệt cỡ mẫu $k$ từ $2$ đến $100$ trên tệp `mau_100.csv`:
1. Tính trung bình tích lũy $\bar{d}(k)$ và độ lệch chuẩn tích lũy $s(k)$.
2. Tra phân vị Student $t_{0.975, k-1}$ và tính bán kính sai số $\varepsilon_{95\%}(k)$ theo đơn vị milimet ($\text{mm}$).
3. Tính đạo hàm sai phân bậc 1 theo từng bước mẫu $k$:
   $$\frac{d\varepsilon_{95\%}}{dk} \approx \Delta\varepsilon_{95\%}(k) = \varepsilon_{95\%}(k) - \varepsilon_{95\%}(k-1) \quad (\text{mm/bước})$$

Toàn bộ kết quả tính toán được phân tách chuẩn hóa thành 3 tệp độc lập lưu trong thư mục `du_lieu_tong_hop/chuong_2/`:
- **`du_lieu_tong_hop/chuong_2/hoi_tu_50cm.csv`**
- **`du_lieu_tong_hop/chuong_2/hoi_tu_100cm.csv`**
- **`du_lieu_tong_hop/chuong_2/hoi_tu_150cm.csv`**

Mỗi tệp gồm 6 cột dữ liệu: `k`, `t_student_95`, `mean_cm`, `s_mm`, `epsilon95_mm`, và đạo hàm `d_epsilon95_mm` đặt liền kề.

#### C. Hệ thống Đồ thị và Bảng số liệu hội tụ

![Đồ thị hội tụ bán kính sai số Student 95%](../graph/chuong_2/hinh_2_1_hoi_tu_sai_so_N.png)

*Hình 2.1: Quy luật hội tụ bán kính sai số Student 95% $\varepsilon_{95\%}(k)$ theo số mẫu $k$ tại 3 cự ly (50cm, 100cm, 150cm).*

![Tốc độ biến thiên sai số theo cỡ mẫu k](../graph/chuong_2/hinh_2_2_dao_ham_diem_khuyu_tay.png)

*Hình 2.2: Tốc độ biến thiên sai số $|d\varepsilon_{95\%}/dk|$ theo cỡ mẫu $k$ xác nhận trạng thái dừng bão hòa tại $N = 50$.*

Bảng số liệu đối chiếu trích xuất tại các mốc cỡ mẫu tiêu biểu:

| Cỡ mẫu $k$ | Hệ số Student $t_{0.975}$ | Mốc 50cm: $\varepsilon_{95\%}$ | Mốc 100cm: $\varepsilon_{95\%}$ | Mốc 150cm: $\varepsilon_{95\%}$ | Đạo hàm $|d\varepsilon/dk|$ tiêu biểu | Ý nghĩa vật lý thực nghiệm |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$k = 5$** | 2.776 | $\pm 0.12\text{ mm}$ | $\pm 0.12\text{ mm}$ | $\pm 0.15\text{ mm}$ | $\sim 0.07\text{ mm/bước}$ | Mẫu quá nhỏ, chưa xuất hiện các xung trượt chu kỳ sóng ở cự ly xa |
| **$k = 10$** | 2.262 | $\pm 0.06\text{ mm}$ | $\pm 0.06\text{ mm}$ | $\pm 0.12\text{ mm}$ | $\sim 0.016\text{ mm/bước}$ | Sai số giảm dốc nhưng tạo ảo giác ổn định sớm |
| **$k = 20$** | 2.086 | $\pm 0.05\text{ mm}$ | $\pm 0.17\text{ mm}$ | $\pm 0.07\text{ mm}$ | $\sim 0.004\text{ mm/bước}$ | Mốc 100cm bắt đầu nhảy bậc; mốc 150cm vẫn chưa bộc lộ trượt sóng |
| **$k = 30$** | 2.042 | $\pm 0.03\text{ mm}$ | $\pm 0.14\text{ mm}$ | $\pm 0.28\text{ mm}$ | $\sim 0.010\text{ mm/bước}$ | **Bắt đầu xuất hiện trượt chu kỳ:** $\varepsilon$ ở 150cm bật tăng vọt từ $0.07 \to 0.28\text{ mm}$ |
| **$k = 50$** | **2.009** | **$\pm 0.03\text{ mm}$** | **$\pm 0.11\text{ mm}$** | **$\pm 0.40\text{ mm}$** | **$\le 0.0005\text{ mm/bước}$** | **MỐC CHỐT TỐI ƯU:** Đã gom đủ các xung lỗi, đỉnh $\varepsilon \le 0.40\text{ mm} < 0.5\text{ mm}$ |
| **$k = 100$** | 1.984 | $\pm 0.02\text{ mm}$ | $\pm 0.08\text{ mm}$ | $\pm 0.27\text{ mm}$ | $\le 0.0002\text{ mm/bước}$ | Vùng bão hòa, giảm chậm dần |

---

### 2.4.3. Luận giải khoa học quyết định lựa chọn cỡ mẫu $N = 50$
Quyết định lựa chọn **$N = 50$ lần đo/mốc** cho toàn bộ các tập dữ liệu thực nghiệm được bảo vệ thông qua 3 luận cứ đo lường kỹ thuật:

1. **Thỏa mãn tiêu chuẩn dung sai đo lường:**
   - Tại $N = 50$, bán kính sai số ngẫu nhiên $\varepsilon_{95\%}$ ở cả 3 cự ly đều nhỏ hơn dung sai vạch chia của thước chuẩn cơ khí ($\pm 0.5\text{ mm}$): đạt $\pm 0.03\text{ mm}$ tại 50cm; $\pm 0.11\text{ mm}$ tại 100cm; và $\pm 0.40\text{ mm}$ tại 150cm.
2. **Điểm dừng đạo hàm tối ưu bão hòa:**
   - Đồ thị Hình 2.2 chứng minh tại $k = 50$, đạo hàm sai phân $|d\varepsilon/dk| \le 0.0005\text{ mm/bước} \approx 0$, xác nhận đường cong đã bước vào vùng phẳng bão hòa. Việc tăng số lần đo lên $N = 100$ chỉ giảm thêm $0.03\text{ mm}$ ở mốc 100cm (hoàn toàn nhỏ hơn độ phân giải phần cứng vi điều khiển $\approx 0.175\text{ mm}$).
3. **Bảo toàn tính ổn định vi khí hậu:**
   - Với tần số lấy mẫu $20\text{ Hz}$ (chu kỳ $50\text{ ms}$), việc đo $N = 50$ lần chỉ mất đúng $T_{\text{total}} = 50 \times 50\text{ ms} = 2.5\text{ giây}$. Khoảng thời gian $2.5\text{ giây}$ đủ ngắn để nhiệt độ phòng và luồng không khí được coi là bất biến, loại trừ hoàn toàn nguy cơ trôi nhiệt độ môi trường trong phiên đo.
