# CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM

---

## 1.1. NGUYÊN LÝ ĐO KHOẢNG CÁCH THỜI GIAN BAY VÀ MÔ HÌNH BÙ NHIỆT ĐỘ MÔI TRƯỜNG

### 1.1.1. Phương trình lan truyền sóng siêu âm thời gian bay
Phương pháp đo khoảng cách bằng sóng siêu âm dựa trên nguyên lý đo thời gian bay (Time-of-Flight - ToF). Module cảm biến phát ra một chuỗi xung kích siêu âm hình sin ở tần số 40 kHz. Sóng âm lan truyền trong không gian tự do với vận tốc $v$, gặp mặt phẳng vật cản và phản xạ dội ngược trở lại đầu thu. Đầu thu áp điện chuyển đổi năng lượng dao động cơ học của sóng âm dội về thành tín hiệu điện áp phản hồi.

Khoảng cách $d$ từ cảm biến đến vật cản được xác định từ thời gian bay tổng cộng $t$ của sóng âm theo phương trình:

$$d = \frac{v \cdot t}{2} \tag{1.1}$$

Trong đó:
- $d$: Khoảng cách đo từ mặt trước màng rung cảm biến đến bề mặt phản xạ (m);
- $v$: Vận tốc truyền sóng âm trong không khí (m/s);
- $t$: Thời gian bay khứ hồi (s).

---

### 1.1.2. Sự ảnh hưởng của nhiệt độ tới vận tốc âm thanh
Trong chất khí lý tưởng, sóng âm lan truyền dưới dạng sóng dọc thông qua quá trình nén và giãn nở đoạn nhiệt. Vận tốc truyền sóng âm:

$$v = \sqrt{\frac{\gamma \cdot R \cdot T_K}{M}} \tag{1.2}$$

Trong đó: $\gamma$ là hệ số đoạn nhiệt của không khí khô ($\gamma \approx 1.402$); $R$ là hằng số khí lý tưởng phổ quát ($R = 8.314\text{ J/(mol}\cdot\text{K)}$); $M$ là khối lượng mol biểu kiến trung bình của không khí khô ($M \approx 0.028964\text{ kg/mol}$); $T_K$ là nhiệt độ tuyệt đối của môi trường (K).

Khai triển chuỗi Taylor bậc nhất của vận tốc sóng âm quanh điểm chuẩn $0^\circ\text{C}$ ($T_0 = 273.15\text{ K}$, $v_0 \approx 331.3\text{ m/s}$) ta thu được phương trình:

$$v(T) = 331.3 + 0.606 \cdot T \quad (\text{m/s}) \tag{1.3}$$

---

### 1.1.3. Sự suy hao năng lượng sóng âm theo cự ly
Năng lượng và biên độ áp suất âm $p(d)$ của sóng âm suy giảm mạnh theo khoảng cách do:
1. **Phân kỳ hình học:** Do chùm sóng âm phát đi theo dạng hình nón. Mật độ công suất âm suy giảm tỷ lệ nghịch với bình phương khoảng cách: $I(d) \sim 1/d^2$.
2. **Ma sát với không khí:** Quá trình truyền sóng gây ma sát trong chất khí, làm suy hao năng lượng.

---

## 1.2. ĐẶC TÍNH VÀ THÔNG SỐ CỦA MODULE RCWL-1601

### 1.2.1. Giản đồ xung kích hoạt và phản hồi thời gian bay
Module RCWL-1601 giao tiếp với vi điều khiển ESP32 thông qua giao thức xung kỹ thuật số hai chân (Trigger và Echo):
- **Bước 1 - Kích hoạt xung (Trigger Pulse):** Vi điều khiển chủ động kéo chân `TRIG` lên mức logic CAO để phát lệnh đo.
- **Bước 2 - Phát chùm sóng siêu âm:** Khi nhận được xung `TRIG`, cảm biến phát chuỗi 8 chu kỳ xung siêu âm dạng sóng vuông ở tần số 40 kHz. Đồng thời, chân `ECHO` được kéo lên mức CAO để báo hiệu bắt đầu chu kỳ bay.
- **Bước 3 - Thu nhận sóng phản xạ và ngắt xung (Echo Pulse):** Sóng âm dội về tác động lên màng thu và cảm biến ghi nhận thay đổi. Ngay sau đó, IC lập tức kéo chân `ECHO` xuống mức THẤP.
- **Bước 4 - Đo thời gian bay ToF:** Độ rộng mức cao của xung `ECHO` ($t_{\text{echo}}$) tỷ lệ thuận chính xác với thời gian bay hai chiều $t$ của sóng âm.

---

### 1.2.2. Bảng thông số kỹ thuật của RCWL-1601

#### Bảng 1.1: Bảng thông số kỹ thuật của module cảm biến siêu âm RCWL-1601

| Thông số kỹ thuật | Giá trị công bố |
| :--- | :---: |
| **Điện áp hoạt động ($V_{\text{CC}}$)** | $2.8\text{ V} - 5.5\text{ V}$ (Một chiều - DC) |
| **Dòng điện tiêu thụ tĩnh** | $< 2\text{ mA}$ |
| **Dòng điện cực đại khi phát** | $\approx 15\text{ mA} - 20\text{ mA}$ |
| **Tần số sóng siêu âm** | $40\text{ kHz} \pm 1.0\text{ kHz}$ |
| **Dải đo công bố** | $2\text{ cm} - 400\text{ cm}$ (hoặc $450\text{ cm}$) |
| **Độ phân giải lý thuyết** | $1\text{ mm}$ |
| **Góc mở chùm sóng âm** | $\approx 15^\circ$ |
| **Tín hiệu kích hoạt (TRIG)** | Xung mức CAO (HIGH) $\ge 10\text{ }\mu\text{s}$ |
| **Tín hiệu phản hồi (ECHO)** | Độ rộng xung mức CAO (PWM) |

---

## 1.3. CƠ SỞ LÝ THUYẾT XỬ LÝ SỐ LIỆU ĐO LƯỜNG VÀ ĐỘ KHÔNG ĐẢM BẢO ĐO

Để chuyển hóa tập dữ liệu mẫu đo thô rời rạc thành các đặc tính kỹ thuật định lượng có độ tin cậy khoa học cao, cần xây dựng một hệ thống công thức toán học đo lường chuẩn mực.

### 1.3.1. Các đại lượng thống kê mô tả mẫu đo
Tại mỗi mốc cự ly khảo sát, thực hiện lặp lại phép đo trong cùng điều kiện thực nghiệm ổn định với cỡ mẫu $N$ lần đo. Ký hiệu tập giá trị đo được là dãy số liệu thực nghiệm:

$$\{x_1, x_2, x_3, \dots, x_N\}$$

Các đại lượng thống kê mô tả đặc trưng cho xu hướng tập trung và độ phân tán của mẫu bao gồm:

1. **Giá trị Trung bình cộng mẫu ($\bar{x}$):** Đại diện cho xu hướng tập trung của kết quả đo:
   $$\bar{x} = \frac{1}{N} \sum_{i=1}^N x_i$$

2. **Giá trị Trung vị mẫu ($\text{Med}$):** Là giá trị nằm chính giữa chuỗi số liệu sau khi đã được sắp xếp tăng dần $x_{(1)} \le x_{(2)} \le \dots \le x_{(N)}$:
   $$\text{Med} = \begin{cases} x_{\left(\frac{N+1}{2}\right)} & \text{khi } N \text{ lẻ} \\ \frac{1}{2} \left( x_{\left(\frac{N}{2}\right)} + x_{\left(\frac{N}{2} + 1\right)} \right) & \text{khi } N \text{ chẵn} \end{cases}$$
   *Ưu điểm đo lường:* Trung vị mang tính bất biến cao, không bị kéo lệch bởi các điểm nhiễu ngoại lai đột biến như giá trị trung bình cộng $\bar{x}$.

3. **Phương sai mẫu thực nghiệm ($s^2$):** Đo lường mức độ biến thiên ngẫu nhiên quanh giá trị trung bình (hiệu chỉnh Bessel chia cho $N - 1$):
   $$s^2 = \frac{1}{N - 1} \sum_{i=1}^N (x_i - \bar{x})^2$$

4. **Độ lệch chuẩn thực nghiệm ($s$):** Thước đo chuẩn mực cho độ tán xạ của phép đo lường:
   $$s = \sqrt{s^2} = \sqrt{\frac{1}{N - 1} \sum_{i=1}^N (x_i - \bar{x})^2}$$

5. **Khoảng tứ phân vị ($\text{IQR}$):** Khoảng cách bao phủ $50\%$ số lượng mẫu đo ở vùng lõi trung tâm:
   $$\text{IQR} = Q_3 - Q_1$$
   Trong đó $Q_1$ (phân vị 25%) và $Q_3$ (phân vị 75%) là các tứ phân vị mẫu.

---

### 1.3.2. Tiêu chuẩn phát hiện và lọc sai số thô bằng Khoảng tứ phân vị (IQR)
Trong đo đạc thực nghiệm sóng siêu âm, các xung nhiễu điện từ, bọt khí bề mặt, góc phản xạ dị thường hoặc hiện tượng mất xung phản hồi ở cự ly xa (dẫn đến tràn thời gian bay bão hòa) có thể tạo ra các mẫu đo ngoại lai (sai số thô) có giá trị sai lệch nghiêm trọng so với bản chất thực.

Hệ thống lựa chọn phương pháp thống kê phi tham số bền vững dựa trên **Khoảng tứ phân vị (Interquartile Range - IQR)** kết hợp hệ hàng rào Tukey (Tukey's Fences) làm giải thuật lọc số chuẩn hóa duy nhất:

$$\text{IQR} = Q_3 - Q_1$$

Cận dưới (Lower Fence) và Cận trên (Upper Fence) được xác định theo:

$$LF = Q_1 - 1.5 \cdot \text{IQR}, \quad UF = Q_3 + 1.5 \cdot \text{IQR}$$

Mẫu đo $x_i$ được chấp nhận là giá trị hợp lệ nếu nằm trong khoảng:

$$x_i \in [LF, \, UF] \iff Q_1 - 1.5 \cdot \text{IQR} \le x_i \le Q_3 + 1.5 \cdot \text{IQR}$$

Mọi mẫu đo nằm ngoài khoảng $[LF, \, UF]$ đều bị loại bỏ hoàn toàn trước khi đưa vào tính toán các chỉ số thống kê đo lường. Phương pháp này có ưu thế vượt trội do tính chất bền vững (robust statistics), hoàn toàn miễn nhiễm với các mẫu tràn thời gian cực trị ($824.6\text{ cm}$) và triệt tiêu triệt để hiện tượng che khuất ngoại lai (masking effect).

---

### 1.3.3. Hệ thống công thức đánh giá các Đặc tính tĩnh của cảm biến

Các đặc tính kỹ thuật tĩnh của cảm biến RCWL-1601 được đánh giá dựa trên tập dữ liệu chuẩn đã làm sạch thông qua các tiêu chí đo lường học:

#### 1. Độ chụm
Độ chụm thể hiện mức độ lặp lại nhất quán giữa các kết quả đo độc lập ở cùng một cự ly và điều kiện đo. Được định lượng thông qua:
- Độ lệch chuẩn thực nghiệm $s$ (càng nhỏ độ chụm càng cao).
- **Hệ số biến thiên ($\text{CV}\%$):** Chuẩn hóa mức độ tán xạ theo giá trị đo để so sánh độ chụm giữa cự ly gần và cự ly xa:
  $$\text{CV}\% = \frac{s}{\bar{x}} \times 100\%$$

#### 2. Độ chính xác và Sai số đo lường
Độ chính xác thể hiện mức độ sai lệch giữa giá trị trung bình đo được $\bar{d}$ so với giá trị cự ly thực $d_{\text{true}}$ (được xác định bằng thước vạch chuẩn mm cơ khí):
- **Sai số tuyệt đối ($\Delta d$):**
  $$\Delta d = \bar{d} - d_{\text{true}}$$
- **Sai số tương đối ($\delta\%$):**
  $$\delta\% = \frac{\Delta d}{d_{\text{true}}} \times 100\% = \frac{\bar{d} - d_{\text{true}}}{d_{\text{true}}} \times 100\%$$

#### 3. Độ nhạy thực nghiệm
Độ nhạy $S$ của cảm biến phản ánh tỷ lệ biến thiên của đại lượng ngõ ra (thời gian ToF $\bar{t}$ tính bằng $\mu\text{s}$) trên sự thay đổi của đại lượng ngõ vào (khoảng cách $d_{\text{true}}$ tính bằng $\text{cm}$):

$$S_t = \frac{\Delta \bar{t}}{\Delta d_{\text{true}}} \quad (\mu\text{s/cm})$$

Về mặt lý thuyết, độ nhạy thuần túy của phép đo ToF hai chiều liên hệ trực tiếp với vận tốc sóng âm:
$$S_{t,\text{theory}} = \frac{2}{v(T)} \times 10^4 \quad (\mu\text{s/cm})$$
*(Tại $T = 31^\circ\text{C}$, $v \approx 350.1\text{ m/s} \to S_{t,\text{theory}} \approx 57.13\text{ }\mu\text{s/cm}$)*. Trong khảo sát thực nghiệm, độ nhạy thực tế được xác định thông qua hệ số góc của đường hồi quy tuyến tính thời gian ToF theo khoảng cách.

#### 4. Độ tuyến tính và Sai số phi tuyến
Độ tuyến tính đánh giá mức độ bám sát của đặc tính tĩnh thực nghiệm với đường thẳng lý thuyết thông qua mô hình hồi quy tuyến tính:

$$\hat{y} = a \cdot x + b$$

Áp dụng phương pháp bình phương bé nhất dưới dạng phương trình ma trận, với $K$ mốc cự ly thực nghiệm $(x_1, y_1), (x_2, y_2), \dots, (x_K, y_K)$, vector các hệ số hồi quy $\hat{\boldsymbol{\beta}} = \begin{bmatrix} a \\ b \end{bmatrix}$ được xác định trực tiếp theo công thức chuẩn tắc:

$$\hat{\boldsymbol{\beta}} = \begin{bmatrix} a \\ b \end{bmatrix} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}$$

Trong đó:
- $\mathbf{X} = \begin{bmatrix} x_1 & 1 \\ x_2 & 1 \\ \vdots & \vdots \\ x_K & 1 \end{bmatrix} \in \mathbb{R}^{K \times 2}$: Ma trận thiết kế, chứa giá trị cự ly đặt chuẩn $d_{\text{true}}$ và cột hệ số tự do.
- $\mathbf{Y} = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_K \end{bmatrix} \in \mathbb{R}^{K \times 1}$: Vector các giá trị đo thực nghiệm tương ứng (khoảng cách trung bình $\bar{d}$ hoặc thời gian bay $\bar{t}$).
- Các ma trận thành phần được tính toán theo:
  $$\mathbf{X}^T \mathbf{X} = \begin{bmatrix} \sum_{k=1}^K x_k^2 & \sum_{k=1}^K x_k \\ \sum_{k=1}^K x_k & K \end{bmatrix}, \quad \mathbf{X}^T \mathbf{Y} = \begin{bmatrix} \sum_{k=1}^K x_k y_k \\ \sum_{k=1}^K y_k \end{bmatrix}$$
  $$(\mathbf{X}^T \mathbf{X})^{-1} = \frac{1}{K \sum_{k=1}^K x_k^2 - \left(\sum_{k=1}^K x_k\right)^2} \begin{bmatrix} K & -\sum_{k=1}^K x_k \\ -\sum_{k=1}^K x_k & \sum_{k=1}^K x_k^2 \end{bmatrix}$$

Công thức ma trận trên cho phép tính toán trực tiếp hệ số góc $a$ (độ nhạy dốc) và hệ số chặn $b$ (độ lệch gốc) trong các script xử lý dữ liệu.

- **Hệ số xác định ($R^2$):** Đánh giá mức độ phù hợp tuyến tính ($0 \le R^2 \le 1$, $R^2 \to 1$ thể hiện tuyến tính tuyệt đối):
  $$R^2 = 1 - \frac{\sum_{k=1}^K (y_k - \hat{y}_k)^2}{\sum_{k=1}^K (y_k - \bar{y})^2}$$
- **Sai số phi tuyến cực đại ($\delta_{\text{NL}}\%$):**
  $$\delta_{\text{NL}}\% = \frac{\max_{k} |\bar{d}_k - \hat{d}_k|}{d_{\text{F.S.}}} \times 100\%$$
  *(với $d_{\text{F.S.}}$ là giá trị cực đại toàn dải đo)*.

#### 5. Độ trễ
Độ trễ phản ánh sự bất đối xứng của giá trị đo tại cùng một điểm cự ly khi tiếp cận theo hai hướng ngược nhau: Chiều tiến và Chiều lùi.
- Sai lệch trễ tại mốc thứ $k$:
  $$\Delta H_k = |\bar{d}_{\text{forward}, k} - \bar{d}_{\text{backward}, k}|$$
- **Độ trễ cực đại toàn dải ($\Delta H_{\max}$):**
  $$\Delta H_{\max} = \max_{k} \{\Delta H_k\}$$
- **Sai số trễ tương đối toàn dải ($\gamma_H\%$):**
  $$\gamma_H\% = \frac{\Delta H_{\max}}{d_{\text{F.S.}}} \times 100\%$$

#### 6. Độ phân giải
Độ phân giải là đại lượng đo nhỏ nhất mà hệ thống có thể phân biệt và đáp ứng được.
- **Độ phân giải lý thuyết ($\Delta d_{\text{res}}$):** Bị giới hạn bởi độ phân giải của bộ đếm thời gian vi điều khiển ESP32 ($\Delta t_{\min} = 1\text{ }\mu\text{s}$):
  $$\Delta d_{\text{res, theory}} = \frac{v \cdot \Delta t_{\min}}{2} \approx \frac{343\text{ m/s} \times 10^{-6}\text{ s}}{2} \approx 0.0172\text{ cm} \quad (\approx 0.172\text{ mm})$$
- **Độ phân giải thực nghiệm:** Được đối chiếu với độ phân tán ngẫu nhiên thực tế tại các cự ly gần ($s \approx 0.03\text{ mm} - 0.1\text{ mm}$).

---

### 1.3.4. Đánh giá Độ không đảm bảo đo

Theo hướng dẫn chuẩn quốc tế về đánh giá độ không đảm bảo đo trong kỹ thuật (ISO/GUM), kết quả của một phép đo cự ly phải được biểu diễn kèm theo khoảng không đảm bảo đo tin cậy.

#### 1. Độ không đảm bảo đo chuẩn Loại A ($u_A$ - Thành phần ngẫu nhiên)
Được đánh giá bằng phương pháp thống kê từ tập $N$ lần đo lặp lại tại mỗi cự ly. Đại diện cho độ phân tán của giá trị trung bình $\bar{d}$:

$$u_A = \text{SE} = \frac{s}{\sqrt{N}} = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N(N - 1)}}$$

#### 2. Độ không đảm bảo đo chuẩn Loại B ($u_B$ - Thành phần hệ thống và thiết bị)
Được đánh giá dựa trên các thông số giới hạn sai số dung sai của thiết bị đo và điều kiện chuẩn ngoại vi, bao gồm 3 thành phần chính:

1. **Thành phần do thước vạch chuẩn cơ khí ($u_{B,\text{ruler}}$):**  
   Thước chuẩn có vạch chia milimet, giới hạn sai số cho phép $\Delta_{\text{ruler}} = \pm 1\text{ mm} = \pm 0.1\text{ cm}$. Giả định hàm phân phối xác suất đều:
   $$u_{B,\text{ruler}} = \frac{\Delta_{\text{ruler}}}{\sqrt{3}} = \frac{0.1\text{ cm}}{\sqrt{3}} \approx 0.0577\text{ cm}$$

2. **Thành phần do độ phân giải ngắt timer ESP32 ($u_{B,\text{timer}}$):**  
   Ngắt thời gian bắt xung có độ phân giải $\Delta t = 1\text{ }\mu\text{s}$, sai số cự ly tương ứng $\Delta_{\text{timer}} \approx \pm 0.0175\text{ cm}$. Với phân phối đều:
   $$u_{B,\text{timer}} = \frac{\Delta_{\text{timer}}}{\sqrt{3}} = \frac{0.0175\text{ cm}}{\sqrt{3}} \approx 0.0101\text{ cm}$$

3. **Thành phần do độ không đảm bảo của giá trị nhiệt độ môi trường ($u_{B,\text{temp}}$):**  
   Biến thiên nhiệt độ môi trường trong phòng trong suốt ca đo được kiểm soát trong khoảng dung sai $\Delta T = \pm 0.5^\circ\text{C}$. Độ nhạy trôi cự ly theo nhiệt độ là $\frac{\partial d}{\partial T} = \frac{0.606 \cdot t}{2} \approx \frac{0.606}{v} \cdot d \approx 0.00173 \cdot d$.  
   Độ không đảm bảo chuẩn tương ứng tại mỗi cự ly $d$:
   $$u_{B,\text{temp}}(d) = \frac{0.00173 \cdot d \cdot \Delta T}{\sqrt{3}}$$

Tổng hợp độ không đảm bảo đo Loại B theo luật lan truyền sai số:
$$u_B = \sqrt{u_{B,\text{ruler}}^2 + u_{B,\text{timer}}^2 + u_{B,\text{temp}}^2}$$

#### 3. Độ không đảm bảo đo chuẩn tổng hợp ($u_c$)
Kết hợp độ không đảm bảo Loại A và Loại B:

$$u_c = \sqrt{u_A^2 + u_B^2}$$

#### 4. Độ không đảm bảo đo mở rộng ($U_{95\%}$)
Để kết quả đo mang ý nghĩa thực tế trong công nghiệp, độ không đảm bảo chuẩn tổng hợp được nhân với hệ số phủ $k_p = 2$, tương ứng với mức xác suất tin cậy xấp xỉ $95\%$:

$$U_{95\%} = k_p \cdot u_c = 2 \cdot u_c$$

Kết quả phép đo cuối cùng được biểu diễn theo chuẩn mực quốc tế:
$$d = \bar{d} \pm U_{95\%} \quad (\text{với mức xác suất tin cậy } P = 95\%)$$
