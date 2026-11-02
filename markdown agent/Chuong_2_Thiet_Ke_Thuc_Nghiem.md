# CHƯƠNG 2: THIẾT KẾ THỰC NGHIỆM

---

## 2.1. MỤC TIÊU VÀ PHƯƠNG PHÁP LUẬN THỰC NGHIỆM

### 2.1.1. Mục tiêu thực nghiệm
Mục tiêu cốt lõi của Chương 2 là thiết kế và chuẩn hóa toàn bộ quy trình đo lường thực nghiệm cho module cảm biến siêu âm RCWL-1601 trên vi điều khiển ESP32, đảm bảo số liệu thu thập được có độ tin cậy khoa học cao và loại trừ tối đa các sai số hệ thống do môi trường và thiết bị. Cụ thể, hệ thống thực nghiệm được thiết kế nhằm đạt được các mục tiêu sau:
1. **Kiểm chứng dải đo thực tế và vùng chết:** Đánh giá giới hạn đo cực cận (vùng chết dưới $5\text{ cm}$) và khả năng đo xa thực tế trên bề mặt phản xạ phẳng nhẵn so với thông số định mức $400\text{ cm}$ theo Datasheet của nhà sản xuất.
2. **Khảo sát toàn diện các chỉ tiêu đo lường tĩnh học:** Thu thập dữ liệu chuẩn hóa phục vụ việc tính toán các đặc tính tĩnh học theo tiêu chuẩn quốc tế ISO/GUM (độ chụm, độ chính xác, độ nhạy thực tế, độ phân giải, độ tuyến tính, độ trễ và ngân sách độ không đảm bảo đo mở rộng).
3. **Định lượng các yếu tố gây nhiễu môi trường:** Đánh giá định lượng tác động của hiện tượng tán xạ sóng âm trên bề mặt gồ ghề (`FRDT`) so với bề mặt phẳng nhẵn (`FSDT`), cũng như tác động của sự thay đổi nhiệt độ môi trường (`FSDT` phòng thường $31^\circ\text{C}$ vs. `FSAT` phòng điều hòa $20^\circ\text{C}$) lên hiện tượng trôi cự ly (Thermal Drift).
4. **Xác lập bộ tham số thực nghiệm cho bài toán ứng dụng:** Làm cơ sở dữ liệu thực nghiệm chuẩn xác để tính toán thiết kế chiều cao lắp đặt, chuỗi bộ lọc số và thuật toán bù nhiệt độ cho hệ thống đo mức chất lỏng bồn chứa thông minh ở Chương 4.

---

### 2.1.2. Phương pháp luận thực nghiệm
Phương pháp luận được áp dụng là **phương pháp đo so sánh trực tiếp với vật chuẩn (Direct Comparison with Standard)**:
- **Chuẩn so sánh (Reference Standard):** Khoảng cách thực $d_{\text{true}}$ được xác lập bằng hệ thống ray trượt cơ khí thẳng hàng có gắn thước chuẩn chia vạch milimet với sai số giới hạn $\Delta_{\text{ruler}} = \pm 1\text{ mm}$ ($\pm 0.1\text{ cm}$).
- **Đối tượng đo (Measurement Object):** Khoảng cách đo được $d$ suy ra từ thời gian bay ToF của chùm sóng siêu âm phát ra từ cảm biến RCWL-1601, được vi điều khiển ESP32 số hóa với độ phân giải thời gian $1\text{ }\mu\text{s}$ và cập nhật thuật toán bù nhiệt độ môi trường Laplace $v(T) = 331.3 + 0.606 \cdot T$.
- **Nguyên tắc lặp lại:** Tại mỗi mốc cự ly đặt chuẩn $d_{\text{true}}$, phép đo được kích hoạt lặp lại nhiều lần trong cùng một trạng thái ổn định cơ khí và nhiệt độ để phục vụ phân tích thống kê ngẫu nhiên.

```
       [ Ray trượt dẫn hướng cơ khí chuẩn hóa & Thước vạch mm ]
  |===================================================================|
  [Cảm biến RCWL-1601] ------------ Sóng ToF -----------> [Bia phản xạ]
  (Cố định tại gốc 0 cm)                                  (Dịch chuyển d_true)
            |
      (GPIO 5 & 18)
            v
  [Vi điều khiển ESP32] ===== Cáp UART/COM =====> [Máy tính thu thập CSV]
```

---

## 2.2. THIẾT KẾ PHẦN CỨNG, MÔ HÌNH GÁ ĐẶT VÀ KHÔNG GIAN THỰC NGHIỆM

### 2.2.1. Thiết kế phần cứng và sơ đồ kết nối điện
Hệ thống phần cứng đo lường gồm hai khối chính: Module cảm biến siêu âm RCWL-1601 và Board mạch vi điều khiển ESP32 NodeMCU 30 chân.

Nhờ vi mạch chuyên dụng RCWL-9610 trên module RCWL-1601 hỗ trợ dải điện áp làm việc rộng từ $3.0\text{V} - 5.5\text{V}$, module có thể hoạt động hoàn toàn ở mức điện áp logic $3.3\text{V}$. Điều này cho phép kết nối trực tiếp chân tín hiệu của module với các chân GPIO của ESP32 mà không cần qua mạch chia áp điện trở hay IC chuyển đổi mức logic (Logic Level Shifter), giúp đường truyền xung nhọn $10\text{ }\mu\text{s}$ và sườn xung `ECHO` không bị méo dạng hay trễ pha do hằng số thời gian ký sinh $RC$.

Sơ đồ kết nối phần cứng chi tiết:

| Chân RCWL-1601 | Chân ESP32 NodeMCU | Chức năng kỹ thuật | Ghi chú mức điện áp |
| :---: | :---: | :--- | :---: |
| **`VCC`** | **`3V3`** | Cấp nguồn nuôi cảm biến | $3.3\text{V DC}$ (dòng tĩnh $< 3\text{ mA}$) |
| **`GND`** | **`GND`** | Nối đất chung | $0\text{V}$ |
| **`TRIG`** | **`GPIO 5`** | Ngõ vào kích phát xung | Mức logic $3.3\text{V}$ (xung kích $\ge 10\text{ }\mu\text{s}$) |
| **`ECHO`** | **`GPIO 18`** | Ngõ ra phản hồi thời gian bay | Mức logic $3.3\text{V}$ (độ rộng tỷ lệ thuận ToF) |

---

### 2.2.2. Thiết kế mô hình gá đặt cơ khí
Để đảm bảo phép đo đạt độ chính xác cao nhất và loại trừ triệt để sai số góc đặt (Cosine Error), mô hình gá đặt cơ khí được chế tạo với các yêu cầu kỹ thuật nghiêm ngặt:
1. **Ray dẫn hướng thẳng hàng:** Sử dụng hệ ray trượt nhôm định hình dài, bề mặt định vị phẳng tuyệt đối, trên thân gắn dải thước đo hợp kim có vạch chia chuẩn milimet chính xác.
2. **Đồ gá cảm biến cố định tại gốc:** Module RCWL-1601 được gắn cố định chắc chắn trên một khối gá đỡ gia công chính xác bằng nhựa cứng, đảm bảo trục đối xứng của loa phát và loa thu siêu âm song song chính xác với phương của ray trượt. Gốc tọa độ $0\text{ cm}$ của thước đo được căn chỉnh trùng khớp với mặt phẳng bề mặt kim loại của màng loa siêu âm.
3. **Giá đỡ bia phản xạ vuông góc:** Tấm bia phản xạ được lắp trên một con trượt cơ khí di động. Con trượt có cữ khóa cố định vị trí vặn ren để giữ bia phản xạ không bị rung lắc trong quá trình đo, đồng thời bề mặt tấm bia luôn được giữ vuông góc chính xác $90^\circ$ với trục phát sóng siêu âm.

---

### 2.2.3. Thiết kế không gian và kiểm soát điều kiện môi trường thực nghiệm
Trong đo lường bằng sóng siêu âm, chùm sóng phát ra có dạng búp sóng hình nón với góc mở hiệu dụng khoảng $\pm 15^\circ$. Nếu không gian thực nghiệm không được tính toán kỹ lưỡng, sóng âm ở các cự ly xa sẽ va đập vào mặt sàn, trần nhà hoặc tường hai bên, tạo ra hiện tượng giao thoa sóng nhiều đường (Multi-path Interference) và gây tín hiệu giả dội về sớm. Do đó, không gian thực nghiệm được thiết kế và kiểm soát theo các tiêu chuẩn kỹ thuật sau:

1. **Độ cao nâng kệ đặt cảm biến ($h_{\text{shelf}} \ge 75\text{ cm}$):**  
   Toàn bộ hệ thống ray trượt và cảm biến được đặt trên hệ khung bàn thí nghiệm có độ cao cách mặt sàn nhà $75\text{ cm}$.  
   *Cơ sở tính toán hình học:* Tại cự ly đo xa $300\text{ cm}$, bán kính mở rộng của chùm tia siêu âm ước tính là $R = d \cdot \tan(15^\circ) \approx 300 \cdot 0.268 \approx 80\text{ cm}$. Việc đặt cảm biến ở độ cao $75 - 80\text{ cm}$ so với sàn đảm bảo vùng rìa chùm tia không bị quét chạm sớm vào mặt sàn nhà gây sai lệch thời gian bắt xung ToF.
2. **Không gian phòng đo thông thoáng:**  
   Thí nghiệm được bố trí dọc theo trục hành lang/phòng thí nghiệm thông thoáng có chiều dài khả dụng $> 7\text{ m}$ (đáp ứng cự ly đo xa nhất $600\text{ cm}$). Khoảng cách từ trục đo đến các bức tường và vật cản hai bên tối thiểu $> 1.5\text{ m}$ để triệt tiêu hoàn toàn phản xạ phụ từ vách tường.
3. **Kiểm soát vi khí hậu và nhiệt độ môi trường:**  
   - Không gian phòng kín, không có quạt gió hoặc luồng gió lùa thổi trực tiếp tạt ngang trục đo (nhằm tránh làm lệch hướng lan truyền của chùm sóng và tránh tạo ra các xoáy khí cục bộ gây biến thiên bất thường của vận tốc âm thanh).
   - Nhiệt độ môi trường được ghi nhận liên tục tại vị trí đo bằng thiết bị nhiệt kế điện tử chuẩn. Quá trình đo kịch bản phòng điều hòa (`FSAT`) được kích hoạt sau khi phòng đã bật điều hòa ổn định ít nhất 30 phút để nhiệt độ toàn phòng đạt trạng thái cân bằng nhiệt đồng nhất tại $20.0^\circ\text{C}$.

---

## 2.3. THIẾT KẾ MA TRẬN KỊCH BẢN THỰC NGHIỆM

Để kiểm chứng toàn diện đặc tính của cảm biến siêu âm trong các điều kiện làm việc thực tế khác nhau, hệ thống thực nghiệm được chia thành **4 bộ kịch bản đo chính thức** với đầy đủ các tham số môi trường và hình học:

| Tham số khảo sát | Kịch bản 1: `FSDT` *(Bộ dữ liệu chuẩn)* | Kịch bản 2: `BSDT` *(Khảo sát trễ)* | Kịch bản 3: `FRDT` *(Khảo sát bề mặt)* | Kịch bản 4: `FSAT` *(Khảo sát nhiệt độ)* |
| :--- | :---: | :---: | :---: | :---: |
| **Bề mặt phản xạ** | Phẳng nhẵn (Tấm composite) | Phẳng nhẵn (Tấm composite) | Gồ ghề nhấp nhô (Tấm xốp) | Phẳng nhẵn (Tấm composite) |
| **Chiều di chuyển** | Tiến ($1\text{ cm} \to 600\text{ cm}$) | Lùi ($300\text{ cm} \to 10\text{ cm}$) | Tiến ($10\text{ cm} \to 375\text{ cm}$) | Tiến ($10\text{ cm} \to 300\text{ cm}$) |
| **Nhiệt độ môi trường** | Phòng thường ($31.0 - 32.0^\circ\text{C}$) | Phòng thường ($31.0 - 32.0^\circ\text{C}$) | Phòng thường ($31.0 - 32.0^\circ\text{C}$) | Phòng điều hòa ($20.0^\circ\text{C}$) |
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
