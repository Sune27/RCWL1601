# CHƯƠNG 1: CƠ SỞ LÝ THUYẾT ĐO LƯỜNG VÀ CẢM BIẾN SIÊU ÂM

---

## 1.1. NGUYÊN LÝ ĐO KHOẢNG CÁCH THỜI GIAN BAY VÀ MÔ HÌNH BÙ NHIỆT ĐỘ MÔI TRƯỜNG

### 1.1.1. Phương trình lan truyền sóng siêu âm thời gian bay
Phương pháp đo cự ly bằng sóng siêu âm không tiếp xúc dựa trên nguyên lý thời gian bay (Time-of-Flight - ToF). Khi module cảm biến được kích hoạt, đầu phát phát ra một chùm xung sóng cơ học tần số siêu âm lan truyền dọc theo trục đo trong không khí. Khi gặp bề mặt vật cản đặt vuông góc với phương truyền, sóng âm phản xạ ngược trở lại và được đầu thu tiếp nhận rồi chuyển đổi thành tín hiệu điện.

Khoảng cách hình học từ mặt cảm biến đến bề mặt phản xạ $d$ được xác định thông qua thời gian truyền khứ hồi $t$ của sóng âm theo phương trình:

$$d = \frac{v \cdot t}{2}$$

Trong đó:
- $d$: Khoảng cách một chiều cần đo từ cảm biến đến bề mặt phản xạ (đơn vị: $\text{m}$ hoặc $\text{cm}$).
- $t$: Tổng thời gian lan truyền khứ hồi của chùm sóng siêu âm từ lúc phát sóng đến lúc nhận lại sóng phản xạ (đơn vị: $\text{s}$ hoặc $\mu\text{s}$). Hệ số chia $2$ xuất hiện do sóng âm phải đi qua quãng đường khứ hồi $2d$.
- $v$: Vận tốc lan truyền của sóng siêu âm trong môi trường không khí (đơn vị: $\text{m/s}$).

---

### 1.1.2. Mô hình toán học bù nhiệt độ môi trường cho vận tốc âm thanh
Trong thực tế đo lường, vận tốc lan truyền của sóng âm $v$ không phải là một hằng số cố định. Sóng siêu âm là sóng cơ học (sóng dọc lan truyền thông qua sự nén dãn tuần hoàn của các phân tử môi trường đàn hồi). Do đó, vận tốc truyền sóng phụ thuộc trực tiếp vào khối lượng riêng và hệ số đàn hồi đoạn nhiệt của không khí, vốn thay đổi chủ yếu theo nhiệt độ tuyệt đối $T_K$ theo phương trình Laplace:

$$v = \sqrt{\gamma \cdot R_{\text{spec}} \cdot T_K}$$

Trong đó:
- $\gamma = 1.402$: Hệ số đoạn nhiệt của không khí.
- $R_{\text{spec}} = 287.05 \text{ J/(kg}\cdot\text{K)}$: Hằng số khí đặc trưng của không khí khô.
- $T_K = T + 273.15$: Nhiệt độ tuyệt đối của môi trường đo (đơn vị: Kelvin $\text{K}$, với $T$ là nhiệt độ bách phân $^\circ\text{C}$).

Tại điều kiện nhiệt độ chuẩn $0^\circ\text{C}$ ($273.15\text{ K}$), vận tốc sóng âm trong không khí khô là $v_0 \approx 331.3\text{ m/s}$. Khai triển chuỗi Taylor bậc nhất quanh điểm $T = 0^\circ\text{C}$, ta thu được công thức thực nghiệm Laplace dùng trong kỹ thuật đo lường:

$$v(T) = v_0 \cdot \sqrt{1 + \frac{T}{273.15}} \approx 331.3 + 0.606 \cdot T \quad (\text{m/s})$$

Khi kết hợp mô hình bù nhiệt Laplace vào phương trình ToF, công thức khoảng cách hiệu chỉnh theo nhiệt độ môi trường trở thành:

$$d = \frac{(331.3 + 0.606 \cdot T) \cdot t}{2}$$

> **Nhận xét định lượng về sai số trôi nhiệt:**  
> Cứ mỗi khi nhiệt độ môi trường thay đổi $\Delta T = 1^\circ\text{C}$, vận tốc âm thanh sẽ thay đổi tương ứng khoảng $\Delta v \approx 0.606\text{ m/s}$ (tương đương biến thiên $\sim 0.18\%$).  
> Nếu một hệ thống đo cự ly cố định vận tốc âm thanh ở mức mặc định chuẩn phòng $v = 340\text{ m/s}$ ($T \approx 14.3^\circ\text{C}$) mà thực hiện đo ở nhiệt độ phòng thực tế $31^\circ\text{C}$ ($v \approx 350.1\text{ m/s}$), sai số trôi cự ly hệ thống sẽ là:
> $$\delta_{\text{drift}}\% = \frac{350.1 - 340}{350.1} \times 100\% \approx 2.88\%$$
> Ở cự ly đo xa $300\text{ cm}$, sai số trôi điểm đo lên tới gần **$8.7\text{ cm}$**. Đây là một sai số hệ thống rất lớn không thể chấp nhận trong các bài toán đo mức công nghiệp. Do đó, việc đo và cập nhật nhiệt độ môi trường $T$ vào thuật toán xử lý là điều kiện bắt buộc để đảm bảo độ chính xác của cảm biến siêu âm.

---

### 1.1.3. Sự suy hao năng lượng sóng âm theo cự ly đo
Khi chùm sóng siêu âm phát ra truyền đi trong không khí, mật độ năng lượng và biên độ áp suất sóng phản xạ tiếp nhận tại đầu thu bị suy giảm mạnh do hai cơ chế vật lý:
1. **Suy giảm hình học theo cự ly ($I \propto 1/d^2$):** Vì mặt sóng lan tỏa trong không gian ba chiều, mật độ năng lượng sóng phản xạ quay về mặt cảm biến tỷ lệ nghịch với bình phương khoảng cách khứ hồi $1/(2d)^2$.
2. **Sự hấp thụ âm của môi trường:** Không khí hấp thụ một phần năng lượng sóng cơ chuyển hóa thành nhiệt năng theo định luật hàm mũ $\exp(-2\alpha d)$, trong đó hệ số suy hao $\alpha$ tăng nhanh theo tần số sóng (ở tần số $40\text{ kHz}$, $\alpha \approx 1.2 - 1.4\text{ dB/m}$ tại độ ẩm thông thường).

Hệ quả là ở cự ly càng xa (như mốc $150\text{ cm}$ hoặc trên $400\text{ cm}$), biên độ tín hiệu sóng phản xạ dội về đầu thu càng nhỏ. Điều này làm giảm tỷ số tín hiệu trên nhiễu, khiến bộ so sánh điện áp ở đầu thu dễ bị trượt chu kỳ sóng hoặc dẫn tới hiện tượng mất tín hiệu ở cự ly giới hạn trên $580\text{ cm}$.

---

## 1.2. ĐẶC TÍNH HOẠT ĐỘNG VÀ THÔNG SỐ DANH ĐỊNH CỦA MODULE RCWL-1601

Module cảm biến siêu âm **RCWL-1601** là thiết bị đo khoảng cách thế hệ mới được trang bị vi mạch tích hợp chuyên dụng RCWL-9610. Điểm cải tiến của RCWL-1601 so với module HC-SR04 truyền thống là khả năng tương thích nguồn điện kép ($3.3\text{V}$ và $5\text{V}$) với dòng tĩnh rất thấp ($< 3\text{ mA}$), cho phép kết nối trực tiếp với các chân GPIO của vi điều khiển ESP32 ($3.3\text{V}$) mà không cần mạch chuyển đổi mức điện áp.

### 1.2.1. Giản đồ xung kích hoạt và phản hồi thời gian bay
Quá trình giao tiếp thu phát tín hiệu giữa vi điều khiển và module RCWL-1601 diễn ra theo chu trình 4 bước:

```
Vi điều khiển (ESP32)             Module RCWL-1601                Môi trường không khí
  [Chân TRIG]                       [Đầu phát]                         [Vật cản]
      |                                   |                                |
  ----|--[ Xung High ≥ 10 µs ]--|---------|                                |
                                          |                                |
                                          |-- Phát chùm 8 xung 40 kHz ---->| (Sóng truyền)
                                          |                                |       |
                                          |                                |       | (Sóng phản xạ)
                                          |<------- Nhận sóng phản xạ -----|-------|
                                     [Đầu thu]
                                          |
  [Chân ECHO]                             |
  ____|--[ Mức Cao (HIGH): Độ rộng t = ToF ]--|____________________________
```

1. **Xung kích hoạt (`TRIG`):** Vi điều khiển xuất một xung điện áp mức cao có độ rộng tối thiểu $10\text{ }\mu\text{s}$ đưa vào chân `TRIG` của module.
2. **Phát chùm xung siêu âm:** Ngay khi nhận được sườn xuống của xung kích, vi mạch trên cảm biến tự động kích hoạt bộ chuyển đổi gốm áp điện phát một chùm gồm 8 chu kỳ xung sóng cơ học tần số $40\text{ kHz}$ dạng sóng vuông ra môi trường.
3. **Thu sóng phản xạ & Bắt thời gian ToF (`ECHO`):** Đồng thời tại thời điểm chùm xung được phát đi, chân `ECHO` của module được kéo lên mức cao logic. Chân `ECHO` duy trì mức cao này liên tục cho tới khi đầu thu tiếp nhận được chùm sóng phản xạ dội về từ vật cản, lúc này chân `ECHO` lập tức hạ xuống mức thấp.
4. **Xác định thời gian ToF:** Khoảng thời gian chân `ECHO` duy trì ở mức cao chính là thời gian sóng truyền khứ hồi $t$. Vi điều khiển sử dụng ngắt timer phần cứng với độ phân giải $1\text{ }\mu\text{s}$ để ghi nhận chính xác giá trị $t$.

---

### 1.2.2. Bảng thông số kỹ thuật danh định của RCWL-1601 (Theo Datasheet)

Bảng thông số định mức kỹ thuật do nhà sản xuất công bố được tổng hợp làm cơ sở tham chiếu nhằm đối chiếu, đánh giá và kiểm chứng với số liệu khảo sát thực nghiệm ở Chương 3:

| Thông số kỹ thuật | Giá trị định mức danh định (Datasheet) | Đơn vị / Ghi chú |
| :--- | :---: | :---: |
| **Điện áp hoạt động** | $3.0 - 5.5$ | $\text{V DC}$ (Hỗ trợ mức $3.3\text{V}$ của ESP32) |
| **Dòng điện làm việc tĩnh** | $\le 3.0$ | $\text{mA}$ |
| **Tần số phát sóng siêu âm** | $40 \pm 1$ | $\text{kHz}$ |
| **Dải đo danh định** | $2.0 - 400.0$ | $\text{cm}$ |
| **Góc mở bức xạ sóng hiệu dụng** | $\le 15$ | Độ ($^\circ$) |
| **Độ chính xác công bố** | $\pm 0.5$ | $\text{cm}$ |
| **Độ phân giải lý thuyết** | $0.1 - 0.3$ | $\text{cm}$ |
| **Độ rộng xung kích `TRIG` tối thiểu** | $10$ | $\mu\text{s}$ |
| **Thời gian chu kỳ kích đo khuyến nghị** | $\ge 50$ | $\text{ms}$ (Tránh nhiễu dội âm lặp) |

---

## 1.3. CƠ SỞ LÝ THUYẾT XỬ LÝ SỐ LIỆU ĐO LƯỜNG VÀ ĐỘ KHÔNG ĐẢM BẢO ĐO (ISO/GUM)

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

### 1.3.2. Tiêu chuẩn phát hiện và lọc sai số thô
Trong đo đạc thực nghiệm, các xung nhiễu điện từ, tạp âm môi trường hoặc góc phản xạ dị thường có thể tạo ra các mẫu đo có giá trị sai lệch nghiêm trọng so với bản chất thực. Hai phương pháp lọc sai số thô chuẩn được sử dụng gồm:

1. **Nguyên lý $3\sigma$ (Tiêu chuẩn Chauvenet / 3-Sigma Gauss):**  
   Dựa trên tính chất của phân phối chuẩn Gauss, một mẫu đo $x_i$ bị coi là sai số thô và bị loại bỏ nếu nằm ngoài dải tin cậy $99.73\%$:
   $$|x_i - \bar{x}| > 3s \iff x_i \notin [\bar{x} - 3s, \; \bar{x} + 3s]$$

2. **Tiêu chuẩn hàng rào Tukey ($\text{IQR}$ / Biểu đồ hộp):**  
   Phương pháp phi tham số không phụ thuộc vào giả định phân phối chuẩn. Mẫu đo $x_i$ bị loại bỏ nếu rơi ra ngoài hàng rào giới hạn:
   $$x_i \notin [Q_1 - 1.5 \cdot \text{IQR}, \; Q_3 + 1.5 \cdot \text{IQR}]$$

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

### 1.3.4. Đánh giá Độ không đảm bảo đo theo tiêu chuẩn ISO/GUM

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
