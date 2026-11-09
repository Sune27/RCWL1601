# HƯỚNG DẪN XÂY DỰNG PHẦN CỨNG & NẠP CODE HỆ THỐNG GIÁM SÁT MỰC NƯỚC (BÌNH 2L)
**Học phần:** Kỹ thuật đo lường và cảm biến (EMA2024E_3)  
**Phần ứng dụng:** Chương 4 – Hệ thống giám sát mực nước và dung tích chất lỏng thông minh bằng ESP32 & RCWL-1601  
**Địa chỉ thư mục:** `D:\đo lường\thực hành đo lường\RCWL1601\ứng dụng`

---

## 1. TỔNG QUAN HỆ THỐNG

Hệ thống được thiết kế nhằm giải quyết bài toán đo lường mức chất lỏng liên tục không tiếp xúc và tính toán thể tích tức thời trong bồn chứa hình trụ (sử dụng chai nước ngọt 2L tiêu chuẩn). 

### Điểm nổi bật về giải pháp kỹ thuật:
1. **Khắc phục vùng mù siêu âm ($< 3.0\text{ cm}$):** Thiết kế giá gá nâng cao cảm biến cách ly $H_{\text{gá}} = 5.0\text{ cm}$ so với miệng bình. Dù mực nước dâng đầy miệng bình, cự ly đo ToF vẫn luôn $\ge 5.0\text{ cm}$, loại trừ hoàn toàn hiện tượng rung dư (*ringing effect*).
2. **Bù trôi vận tốc truyền âm thời gian thực theo nhiệt độ:** Sử dụng cảm biến DHT11 đo nhiệt độ không khí $T$ bên trên mặt thoáng để cập nhật động vận tốc âm theo công thức Laplace thực nghiệm:
   $$v(T) = 331.3 + 0.606 \cdot T \quad (\text{m/s})$$
3. **Chuỗi lọc thích nghi 2 tầng (2-Stage Filtering):**
   - *Tầng 1 (Lọc ngoại lai IQR - Interquartile Range):* Loại bỏ tức thời các xung gai phản xạ giả do bọt khí sủi tăm hoặc phản xạ vách bình ($W=5$).
   - *Tầng 2 (Lọc trung bình trượt Moving Average):* Khử dao động sóng gợn bề mặt khi máy bơm cấp nước xả ($W=7$).
4. **Đánh giá độ không đảm bảo đo chuẩn tổng hợp và mở rộng theo ISO/GUM:**
   - Lan truyền sai số bán kính đáy bình $u(R) = 0.04\text{ cm}$ và mức nước $u_c(h) = 0.071\text{ cm}$:
     $$u_c^2(V) = (2\pi R h \cdot u(R))^2 + (\pi R^2 \cdot u_c(h))^2$$
   - Độ không đảm bảo đo mở rộng mức tin cậy 95% ($k=2$): $U_{95\%}(V) = 2 \cdot u_c(V)$.
5. **Điều khiển bơm với vòng trễ Hysteresis chống rung giật:**
   - Đóng ngắt máy bơm chìm 6V qua Module Relay Opto cách ly.
   - Vòng trễ $0.5\text{ cm}$ chống hiện tượng tiếp điểm rơ-le bật tắt liên tục (*relay chattering*).

---

## 2. DANH MỤC LINH KIỆN & PHẦN CỨNG (BOM)

| STT | Tên linh kiện / Thiết bị | Thông số kỹ thuật | Số lượng | Vai trò trong hệ thống |
|:---:|:---|:---|:---:|:---|
| 1 | **ESP32 DevKit V1** | Vi điều khiển 32-bit dual-core, 240MHz, tích hợp WiFi/BLE | 1 mạch | Xử lý trung tâm, lọc số, tính toán ISO/GUM, điều khiển I/O |
| 2 | **Cảm biến siêu âm RCWL-1601** | Điện áp 3.3V – 5.0V, dải đo 2 cm – 450 cm, ToF chính xác | 1 cái | Phát và thu sóng ToF đo khoảng cách mặt thoáng $d$ |
| 3 | **Cảm biến DHT11** | Đo nhiệt độ phòng (0 - 50°C, độ chính xác ±1°C) | 1 cái | Bù nhiệt độ môi trường truyền sóng $v(T)$ |
| 4 | **Module Relay 5V 1 kênh** | Cách ly quang Opto PC817, tiếp điểm chịu dòng 10A/250VAC | 1 module | Điều khiển đóng/cắt nguồn cấp bơm chìm |
| 5 | **Bơm chìm mini DC** | Điện áp 3V – 6V, công suất 1.2W, lưu lượng ~100 L/h | 1 cái | Đặt chìm đáy bồn, bơm cấp/xả nước thử nghiệm |
| 6 | **Nguồn củ sạc ngoài 5V/2A** | DC Jack hoặc USB 5V rời | 1 bộ | Cấp nguồn riêng cho Relay và Bơm (chống sụt áp ESP32) |
| 7 | **Bình chứa 2L (Chai soda)** | Đường kính $D = 10.0\text{ cm}$, bán kính $R = 5.0\text{ cm}$ | 1 vỏ | Thân bồn chứa chất lỏng thực nghiệm |
| 8 | **Đèn LED chỉ thị** | 1 LED Đỏ (Cảnh báo/Nguy hiểm), 1 LED Xanh (Bình thường) | 2 con | Chỉ thị trạng thái mực nước trực quan |
| 9 | **Điện trở hạn dòng 220Ω** | Công suất 1/4W | 2 con | Mắc nối tiếp bảo vệ chân GPIO nối LED |
| 10 | **Dây cắm Testboard & Khung gá** | Dây cắm đực-đực, đực-cái, mica/gỗ gá ToF cao 5cm | 1 bộ | Đấu nối mạch và cố định cơ khí |

---

## 3. BẢNG NỐI DÂY CHI TIẾT (PINOUT MAPPING) - HỖ TRỢ BẢNG MỞ RỘNG (G - V - S)

> [!IMPORTANT]
> **Quy ước 3 hàng chân trên Shield mở rộng ESP32:**
> - **Hàng S (Signal):** Chân tín hiệu / dữ liệu (nối trực tiếp với các chân GPIO của ESP32).
> - **Hàng V (Voltage):** Chân dương nguồn cấp (+5V hoặc +3.3V).
> - **Hàng G (Ground):** Chân mass / âm nguồn (GND).

| Linh kiện | Chân linh kiện | Nối với chân ESP32 / Shield | Màu dây khuyên dùng | Chức năng tín hiệu |
|:---|:---|:---|:---:|:---|
| **RCWL-1601** | VCC | **Chân 5V hoặc 3V3 (Hàng V)** | Đỏ | Cấp nguồn nuôi cảm biến ToF |
| | GND | **Chân GND (Hàng G)** | Đen | Nối mass chung |
| | TRIG | **GPIO 5 (Hàng S)** | Xanh dương | Xung kích hoạt phát siêu âm (10µs) |
| | ECHO | **GPIO 18 (Hàng S)** | Xanh da trời | Xung phản hồi ToF độ rộng tỉ lệ thời gian |
| **DHT11** | VCC | **Chân 3V3 hoặc 5V (Hàng V)** | Đỏ | Nguồn cấp cho cảm biến nhiệt |
| | GND | **Chân GND (Hàng G)** | Đen | Nối mass chung |
| | DATA | **GPIO 4 (Hàng S)** | Xanh lá | Tín hiệu 1-Wire đọc nhiệt độ phòng |
| **Module Relay 5V** | VCC | **Chân 5V (Hàng V)** | Đỏ | Nguồn nuôi cuộn hút relay |
| | GND | **Chân GND (Hàng G)** | Đen | Nối mass chung |
| | IN | **GPIO 23 (Hàng S)** | Cam | Tín hiệu điều khiển đóng ngắt bơm (Active LOW) |
| **Bơm chìm 6V** | Dây dương (+) | Chân **NO** (Normally Open) của Relay | Đỏ | Tiếp điểm thường mở đóng khi bơm chạy |
| | Dây âm (-) | **Chân GND nguồn ngoài / Shield (Hàng G)** | Đen | Dây âm nguồn bơm |
| **Nguồn 5V ngoài**| Cực dương (+) | Chân **COM** của Module Relay | Đỏ | Đưa nguồn 5V ngoài vào công tắc relay |
| | Cực âm (-) | **Chân GND nguồn ngoài / Shield (Hàng G)** | Đen | Nối chung mass toàn hệ thống |
| **LED Đỏ (Nguy cấp/Tràn)** | Anode (+) | **GPIO 21 (Hàng S)** *(qua trở 220Ω)* | Nâu / Đỏ | Sáng khi mức nước vào vùng cảnh báo/nguy hiểm |
| | Cathode (-) | **Chân GND (Hàng G)** | Đen | Nối mass |
| **LED Xanh (An toàn)** | Anode (+) | **GPIO 19 (Hàng S)** *(qua trở 220Ω)* | Xanh lục | Sáng khi mức nước ở ngưỡng an toàn bình thường |
| | Cathode (-) | **Chân GND (Hàng G)** | Đen | Nối mass |

*Bản vẽ trực quan độ phân giải 300 DPI:* Xem tệp [so_do_noi_day_phan_cung.png](file:///D:/%C4%91o%20l%C6%B0%E1%BB%9Dng/th%E1%BB%B1c%20h%C3%A0nh%20%C4%91o%20l%C6%B0%E1%BB%9Dng/RCWL1601/%E1%BB%A9ng%20d%E1%BB%A5ng/so_do_noi_day_phan_cung.png).

---

## 4. GIA CÔNG CƠ KHÍ BỒN CHỨA & LẮP ĐẶT GIÁ GÁ CẢM BIẾN

### Bước 1: Chuẩn bị bồn chứa 2L
1. Sử dụng chai nước ngọt 2L bằng nhựa trong suốt, đáy phẳng hoặc đáy 5 cánh gia cố.
2. Dùng dao rọc giấy cắt bỏ phần miệng chai thuôn nhọn ở độ cao tính từ đáy lên $H_{\text{bình}} = 17.0\text{ cm}$. Lúc này, bồn chứa trở thành một ống trụ tròn đều có đường kính trong $D = 10.0\text{ cm}$ (bán kính $R = 5.0\text{ cm}$, tiết diện ngang $S_{\text{base}} = \pi \cdot 5^2 \approx 78.54\text{ cm}^2$).
3. Dùng thước khắc vạch mm dọc thân chai để đối chiếu kết quả đo trực quan (hiệu chuẩn).

### Bước 2: Thiết kế giá gá cảm biến nâng cao (Tránh vùng mù 3 cm)
- Cảm biến RCWL-1601 có vùng mù $d_{\min} \approx 2.5 - 3.0\text{ cm}$ do hiện tượng dao động dư của màng gốm áp điện.
- Gia công một thanh đỡ chữ U (bằng mica hoặc que kem gỗ/3D print) bắt cố định vào miệng bình sao cho bề mặt phát siêu âm nằm cao hơn miệng bình một khoảng đúng bằng:
  $$H_{\text{gá}} = 5.0\text{ cm}$$
- Khi đó, tổng khoảng cách từ cảm biến tới đáy bình là:
  $$H_{\text{tổng}} = H_{\text{bình}} + H_{\text{gá}} = 17.0 + 5.0 = 22.0\text{ cm}$$
- **Hiệu quả:**
  + Khi bình cạn khô ($h = 0\text{ cm}$): Khoảng cách ToF là $d = 22.0\text{ cm}$.
  + Khi bình đầy tràn ($h = 17.0\text{ cm}$): Khoảng cách ToF là $d = 5.0\text{ cm} > 3.0\text{ cm}$. Cảm biến **không bao giờ rơi vào vùng mù**, đảm bảo đo đạc tin cậy 100% trên toàn bộ thang đo.
- Cố định cảm biến sao cho 2 mắt phát/thu hướng thẳng đứng, vuông góc $90^\circ$ với mặt nước để tránh sóng âm phản xạ xiên ra ngoài vách.

### Bước 3: Đặt bơm chìm và ống ti-ô
- Cố định máy bơm chìm sát đáy bình chai bằng chân mút cao su (hút rung động).
- Luồn ống dẫn nước mềm ($\phi 6\text{mm}$) xả ngược ra bình chứa phụ để chạy tuần hoàn khép kín.

---

## 5. HƯỚNG DẪN NẠP CODE CHO ESP32

Người dùng có thể lựa chọn 1 trong 2 phương pháp nạp code dưới đây:

### CÁCH 1: Nạp mã nguồn C/C++ bằng Arduino IDE (Khuyên dùng)
1. Cài đặt **Arduino IDE** (phiên bản 2.x hoặc 1.8.x).
2. Vào `File` $\to$ `Preferences`, dán URL quản lý board ESP32 vào ô *Additional boards manager URLs*:
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
3. Mở `Tools` $\to$ `Board` $\to$ `Boards Manager...`, tìm kiếm `esp32` của *Espressif Systems* và nhấn **Install**.
4. Mở `Sketch` $\to$ `Include Library` $\to$ `Manage Libraries...`, tìm và cài đặt:
   - **DHT sensor library** (Adafruit)
   - **Adafruit Unified Sensor** (Adafruit)
5. Mở file [GiamSatMucNuoc_ESP32.ino](file:///D:/%C4%91o%20l%C6%B0%E1%BB%9Dng/th%E1%BB%B1c%20h%C3%A0nh%20%C4%91o%20l%C6%B0%E1%BB%9Dng/RCWL1601/%E1%BB%A9ng%20d%E1%BB%A5ng/GiamSatMucNuoc_ESP32.ino) trong thư mục này.
6. Chọn Board: `Tools` $\to$ `Board` $\to$ `ESP32 Arduino` $\to$ `DOIT ESP32 DEVKIT V1`.
7. Cắm cáp Micro-USB nối ESP32 vào máy tính, chọn đúng cổng COM (`Tools` $\to$ `Port`).
8. Nhấn nút **Upload** ($\rightarrow$). Chờ nạp thành công (100%).
9. Mở **Serial Monitor** với tốc độ Baudrate `115200` để quan sát chuỗi JSON bắn về máy tính.

---

### CÁCH 2: Nạp mã nguồn Python bằng MicroPython / Thonny IDE
1. Cài đặt **Thonny IDE** từ trang chủ thonny.org.
2. Tải firmware MicroPython cho ESP32 (`esp32-idf4-....bin`) và nạp vào ESP32 thông qua trình nạp firmware tích hợp trong Thonny (`Tools` $\to$ `Options` $\to$ `Interpreter` $\to$ `Install or update MicroPython`).
3. Mở 2 file sau trong thư mục `ứng dụng`:
   - [rcwl1601.py](file:///D:/%C4%91o%20l%C6%B0%E1%BB%9Dng/th%E1%BB%B1c%20h%C3%A0nh%20%C4%91o%20l%C6%B0%E1%BB%9Dng/RCWL1601/%E1%BB%A9ng%20d%E1%BB%A5ng/rcwl1601.py) (Driver giao tiếp ToF thời gian thực)
   - [app_chuong4_giam_sat_bon.py](file:///D:/%C4%91o%20l%C6%B0%E1%BB%9Dng/th%E1%BB%B1c%20h%C3%A0nh%20%C4%91o%20l%C6%B0%E1%BB%9Dng/RCWL1601/%E1%BB%A9ng%20d%E1%BB%A5ng/app_chuong4_giam_sat_bon.py) (Chương trình giám sát chính)
4. Lưu cả 2 file trực tiếp vào bộ nhớ flash của mạch ESP32 (lưu dưới tên `rcwl1601.py` và `main.py`). Khi đó, mỗi lần bật nguồn, ESP32 sẽ tự động chạy chương trình giám sát mà không cần cắm máy tính.

---

## 6. HƯỚNG DẪN CHẠY BỘ TEST & GIAO DIỆN PC (LIVE DASHBOARD)

Tệp [test_giam_sat_pc.py](file:///D:/%C4%91o%20l%C6%B0%E1%BB%9Dng/th%E1%BB%B1c%20h%C3%A0nh%20%C4%91o%20l%C6%B0%E1%BB%9Dng/RCWL1601/%E1%BB%A9ng%20d%E1%BB%A5ng/test_giam_sat_pc.py) được xây dựng nhằm thu thập dữ liệu thời gian thực từ cổng Serial USB của ESP32, vẽ đồ thị động và ghi file CSV.

### Bước 1: Cài đặt thư viện Python trên PC
Mở Command Prompt (cmd) hoặc PowerShell trên máy tính:
```bash
pip install pyserial matplotlib
```

### Bước 2: Khởi chạy bộ giám sát
Chạy lệnh trực tiếp với cổng COM tương ứng (ví dụ `COM3`, `COM4`...):
```bash
python "D:\đo lường\thực hành đo lường\RCWL1601\ứng dụng\test_giam_sat_pc.py" COM4
```
*(Nếu không điền cổng COM, script sẽ mặc định kiểm tra `COM3`; nếu không có ESP32 cắm vào, script sẽ tự động chuyển sang **Chế độ Mô phỏng (Simulation)** để sinh viên xem trước đồ thị).*

### Bước 3: Xem giao diện và xuất báo cáo
- Cửa sổ đồ thị sẽ mở ra gồm 2 đồ thị liên hoàn:
  1. **Đồ thị trên:** Mức nước thô $h_{\text{raw}}$ (chấm mờ) so sánh với mức nước sau lọc $h_{\text{lọc}}$ (đường đặc xanh), đồng thời hiển thị 3 vạch đỏ cảnh báo an toàn: Cạn khẩn cấp ($2.5\text{ cm}$), Báo cạn ($5.0\text{ cm}$), Tràn khẩn cấp ($14.0\text{ cm}$).
  2. **Đồ thị dưới:** Thể tích chất lỏng $V(t)$ (đơn vị mL) kèm dải phủ màu bán trong suốt biểu diễn miền dung sai mở rộng tin cậy $95\%$ theo chuẩn ISO/GUM ($V \pm U_{95\%}(V)$) và chỉ thị trạng thái Bơm ON/OFF.
- Dữ liệu đo đạc liên tục được tự động ghi vào tệp CSV: `result_test_ung_dung.csv` tại chính thư mục này.

---

## 7. CẤU TRÚC THƯ MỤC `ứng dụng`

```
D:\đo lường\thực hành đo lường\RCWL1601\ứng dụng\
│
├── HUONG_DAN_CAI_DAT_VA_KET_NOI.md    # Hướng dẫn chi tiết kỹ thuật phần cứng & nạp code (File này)
├── so_do_noi_day_phan_cung.png        # Bản vẽ sơ đồ đấu nối dây mạch điện chi tiết (300 DPI)
│
├── GiamSatMucNuoc_ESP32.ino           # Firmware C/C++ chạy bằng Arduino IDE cho ESP32
├── app_chuong4_giam_sat_bon.py        # Firmware Python (MicroPython) nạp trực tiếp vào ESP32
├── rcwl1601.py                        # Thư viện Driver đo ToF chính xác cao cho MicroPython
│
├── test_giam_sat_pc.py                # Dashboard Python giám sát trực quan thời gian thực trên PC
├── result_test_ung_dung.csv           # File nhật ký CSV lưu dữ liệu đo tự động (tạo khi chạy test)
│
├── hinh_4_1_nguyen_ly_bon_chua.png    # Hình 4.1: Nguyên lý cấu trúc hình học bồn chứa 2L & giá gá 5cm
├── hinh_4_2_mo_phong_loc_song_gon.png # Hình 4.2: Đánh giá hiệu quả chuỗi lọc số thích nghi 2 tầng IQR+MA
├── hinh_4_3_danh_gia_sai_so_the_tich.png # Hình 4.3: Đánh giá sai số thể tích và dải tin cậy mở rộng ISO/GUM
├── hinh_4_4_mo_hinh_thuc_te.png       # Hình 4.4: Hình ảnh chụp thực tế mô hình đo thực nghiệm 2L & LED
├── hinh_thuc_te_1.jpg                 # Ảnh chụp phần cứng ESP32, Shield và breadboard LED
├── hinh_thuc_te_2.jpg                 # Ảnh chụp thử nghiệm đo ToF trên bình 2L với LED Đỏ cảnh báo
├── hinh_thuc_te_3.jpg                 # Ảnh chụp góc chiếu thẳng đứng từ trên xuống mặt nước 2L
└── video_demo_giam_sat_muc_nuoc_27s.mp4 # Video clip thực nghiệm 27 giây ghi lại quá trình đo & cảnh báo LED
```

---

## 8. XỬ LÝ SỰ CỐ THƯỜNG GẶP (TROUBLESHOOTING)

1. **ESP32 bị sập nguồn / khởi động lại liên tục khi rơ-le đóng:**
   - *Nguyên nhân:* Bơm mini lấy nguồn chung từ chân 3V3/5V của ESP32 gây sụt điện áp mạch nguồn.
   - *Khắc phục:* Bắt buộc tách riêng nguồn 5V/2A nuôi Bơm và Relay. Nối dây âm GND nguồn ngoài về GND ESP32 để thông mass.
2. **Cảm biến RCWL-1601 báo khoảng cách $0\text{ cm}$ hoặc timeout:**
   - *Nguyên nhân:* Dây TRIG/ECHO lỏng hoặc bị cắm nhầm chân logic (GPIO 5 và GPIO 18).
   - *Khắc phục:* Kiểm tra lại tiếp xúc chân cắm, thử cấp nguồn 5V cho RCWL-1601 nếu dây cắm dài.
3. **Mặt nước bị sóng gợn mạnh khi bơm chạy khiến số đo nhảy liên tục:**
   - *Nguyên nhân:* Dòng nước xả trực tiếp vào vùng phản xạ của chùm sóng siêu âm ($15^\circ$).
   - *Khắc phục:* Ống xả nước nên cho chảy sát mép vách bình chai; chuỗi lọc số 2 tầng (IQR + MA) trong code đã được tối ưu sẵn để triệt tiêu trên 90% biên độ sóng gợn này.


---

## 7. LINK VIDEO THỰC NGHIỆM MINH CHỨNG VÀ TRÌNH CHIẾU
- **Link Google Drive xem trực tuyến:** [https://drive.google.com/file/d/1q7BDve7W911czojQXaRA-I49W2jXUlJU/view?usp=sharing](https://drive.google.com/file/d/1q7BDve7W911czojQXaRA-I49W2jXUlJU/view?usp=sharing)
- **Tệp video ghép song song tinh gọn (cục bộ):** ideo_ghep_song_song_thuc_nghiem_va_do_thi.mp4 (2126x720, không chữ, không nền, đồng bộ khóa nhịp 1:1)
- **Tệp video ghép chuẩn 16:9 1080p (cục bộ):** ideo_ghep_song_song_1080p.mp4 (1920x1080)
