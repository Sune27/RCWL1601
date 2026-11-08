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

### 1.3.1. Các đại lượng thống kê mô tả mẫu đo
Tại mỗi mốc cự ly chuẩn, thực hiện lặp lại $N$ lần đo độc lập trong điều kiện môi trường ổn định, thu được tập mẫu đo khoảng cách: $X = \{x_1, x_2, \dots, x_N\}$. Các đại lượng thống kê cơ bản bao gồm:

• **Giá trị trung bình mẫu:** Đại diện cho giá trị xu thế trung tâm của tập mẫu đo lặp:
$$\bar{x} = \frac{1}{N} \sum_{i=1}^N x_i \tag{1.4}$$

• **Độ lệch chuẩn mẫu thực nghiệm:** Đại diện cho mức độ phân tán ngẫu nhiên của các giá trị đo quanh giá trị trung bình:
$$s = \sqrt{\frac{1}{N - 1} \sum_{i=1}^N (x_i - \bar{x})^2} \tag{1.5}$$

• **Giá trị trung vị mẫu (Median):** Giá trị chia đôi tập dữ liệu đã sắp xếp thứ tự: $\text{Med} = x_{\left(\frac{N+1}{2}\right)}$ với $N$ lẻ. Giá trị trung vị có tính chất thống kê bền vững, hoàn toàn không bị ảnh hưởng bởi các xung nhiễu đột biến cực đoan.

---

### 1.3.2. Lọc sai số thô bằng Khoảng tứ phân vị (IQR)
Trong đo đạc thực nghiệm sóng siêu âm, các xung nhiễu điện từ, bọt khí bề mặt, góc phản xạ dị thường hoặc hiện tượng mất xung phản hồi ở cự ly xa (dẫn đến tràn thời gian bay bão hòa) có thể tạo ra các mẫu đo ngoại lai có giá trị sai lệch nghiêm trọng. Nhóm lựa chọn phương pháp Lọc Khoảng tứ phân vị (Interquartile Range - IQR) làm giải thuật lọc số:

$$\text{IQR} = Q_3 - Q_1 \tag{1.6}$$

Cận dưới và Cận trên được xác định theo:

$$\text{LF} = Q_1 - 1.5 \cdot \text{IQR}, \quad \text{UF} = Q_3 + 1.5 \cdot \text{IQR} \tag{1.7}$$

Mẫu đo $x_i$ được chấp nhận là giá trị hợp lệ nếu nằm trong khoảng:

$$\text{LF} \le x_i \le \text{UF} \tag{1.8}$$

---

### 1.3.3. Hệ thống công thức đánh giá các Đặc tính tĩnh của cảm biến

1. **Độ chụm và Sai số chuẩn trung bình:** Đánh giá mức độ lặp lại nhất quán của phép đo thông qua độ lệch chuẩn thực nghiệm mẫu $s$ và sai số chuẩn của giá trị trung bình $\text{SE} = s / \sqrt{N}$ (phản ánh độ chụm của ước lượng trung bình mẫu $\bar{x}$ khi thực hiện $N$ lần đo lặp độc lập).

2. **Sai số đo lường:** Đánh giá mức độ sai lệch giữa giá trị đo trung bình và giá trị chuẩn:
   - Sai số tuyệt đối: $\Delta d = \bar{d} - d_{\text{true}}$
   - Sai số tương đối: $\delta\% = \left(\frac{\Delta d}{d_{\text{true}}}\right) \cdot 100\%$

3. **Độ tuyến tính và Sai số phi tuyến (Linearity):** Đánh giá mức độ bám sát của đặc tính tĩnh thực nghiệm với đường thẳng lý thuyết $\hat{y} = a \cdot x + b$. Áp dụng phương pháp bình phương bé nhất dưới dạng phương trình ma trận chuẩn tắc, vector hệ số hồi quy được giải trực tiếp theo:

$$\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y} \tag{1.9}$$

5. **Độ trễ (Hysteresis):** Phản ánh sự bất đối xứng của giá trị đo tại cùng một điểm cự ly khi tiếp cận theo hai hướng ngược nhau (Chiều tiến Forward và Chiều lùi Backward): $\Delta H_k = |\bar{d}_{\text{forward}, k} - \bar{d}_{\text{backward}, k}|$. Sai số trễ tương đối toàn dải: $\gamma_H\% = \left(\frac{\max_k \Delta H_k}{d_{\text{FS}}}\right) \cdot 100\%$.

---

### 1.3.4. Đánh giá Độ không đảm bảo đo

• **Độ không đảm bảo đo Loại A ($u_A$):** Đánh giá bằng phương pháp phân tích thống kê chuỗi quan sát lặp lại: $u_A = s / \sqrt{N}$.

• **Độ không đảm bảo đo Loại B ($u_B$):** Độ không đảm bảo chuẩn thành phần là: $u_B = a / \sqrt{3}$, trong đó $a$ là nửa khoảng dung sai cho phép.

• **Độ không đảm bảo đo chuẩn tổng hợp ($u_c$):** Kết hợp toàn bộ các thành phần theo định luật lan truyền sai số: $u_c = \sqrt{u_A^2 + \sum u_{B, j}^2}$.

• **Độ không đảm bảo đo mở rộng ($U_{95\%}$):** Mở rộng khoảng tin cậy với hệ số phủ $k_p = 2$ (tương ứng mức tin cậy xấp xỉ 95% đối với bậc tự do lớn): $U_{95\%} = k_p \cdot u_c = 2 \cdot u_c$.

Kết quả đo hoàn chỉnh của phép đo khoảng cách được biểu diễn:

$$Y = \bar{d} \pm U_{95\%} \tag{1.10}$$
