# Kiến Trúc Đồ Họa & Hệ Thống Thiết Kế Sơ Đồ Kỹ Thuật (Architecture Design System)

Tài liệu này chuẩn hóa toàn bộ các nguyên tắc, thuật toán hình học và kỹ thuật trực quan hóa được phát triển trong dự án `diagram-maker`. Tất cả các sơ đồ kiến trúc mới hoặc cập nhật phải tuân thủ nghiêm ngặt các quy chuẩn dưới đây để đảm bảo chất lượng hiển thị chuẩn Institutional Financial Terminal (tương đương Bloomberg, TradingView, TCBS).

---

## 1. Kỹ Thuật Ghép Cổng Ảo (Virtual Port Coupling Pattern)

### A. Vấn Đề Kỹ Thuật & Cơ Chế Giải Quyết
- **Vấn đề:** Khi các luồng dữ liệu liên tầng (Cross-Tier Pipelines) phải băng qua các hành lang hẹp (Corridors), việc vẽ các đường dây dài (Highways) thường dẫn đến hiện tượng giao cắt đường dây (Line Crossings), đè chữ nhãn giao thức và làm rối loạn thị giác người đọc.
- **Cơ chế:** Phân tách đường truyền vật lý thành cặp **Cổng ghép nối ảo (Virtual Port Junctions)**:
  - **Cổng phát (Source Port):** Đặt tại mép xuất tín hiệu của khối nguồn.
  - **Cổng thu (Receiver Port):** Đặt tại mép tiếp nhận của khối đích.
  - **Ký tự định danh (Port ID):** Sử dụng các chữ cái chuẩn hóa `A`, `B`, `C`, `D`, `E`, `F`...

### B. Bảng Màu Chuẩn Hóa Đa Cổng (`PORT_PALETTE`)
Hệ thống sử dụng bảng màu chức năng trong `src/core/palette.py`:

| Cổng | Gam Màu | Mã HEX | Chức Năng Hệ Thống Đại Diện |
| :---: | :--- | :---: | :--- |
| **A** | Purple (Tím) | `#a855f7` | Lõi định lượng, tính toán thuật toán, chuỗi logic O(1) |
| **B** | Emerald (Xanh ngọc) | `#089981` | Luồng Live Stream thời gian thực, đồng bộ Lakehouse |
| **C** | Cyan (Xanh lam) | `#06b6d4` | Nạp dữ liệu thô (Ingestion), truy cập bộ nhớ tức thời |
| **D** | Amber (Hổ phách) | `#f59e0b` | Cơ chế dự phòng (Failover), lưu trữ đệm, Polling Drawer |
| **E** | Blue (Xanh dương) | `#2962ff` | Điều hướng Gateway, Dispatcher, giao diện người dùng |
| **F** | Rose (Đỏ hồng) | `#f23645` | Ngắt mạch (Circuit Breaker), cảnh báo rủi ro, dị thường |

### C. Giao Diện Lập Trình (Python API)
Hàm `render_port_junction` trong `src/core/base.py`:
```python
def render_port_junction(cx, cy, port_id, label, color=None, is_source=True, text_pos="bottom"):
    """
    - cx, cy: Tọa độ tâm của cổng ghép ảo.
    - port_id: Ký tự định danh (A, B, C, D, E, F...).
    - label: Nhãn mô tả tín hiệu (ví dụ: SO LỌC, HỒ PARQUET, LIVE WS).
    - color: Mã màu HEX. Nếu để None, tự động tra cứu qua get_port_color(port_id).
    - is_source: True nếu là cổng phát, False nếu là cổng thu.
    - text_pos: Vị trí nhãn text (bottom, top, left, right).
    """
```

### D. Tương Tác Đồng Bộ Đa Điểm (Interactive Dynamic Pulse)
- Khi người dùng rê chuột (`mouseenter`) vào bất kỳ cổng nào có `data-port="A"`, bộ điều khiển JavaScript trong `src/core/base.py` sẽ tự động kích hoạt class `.port-pulse` trên **toàn bộ các cổng có cùng định danh trên toàn sơ đồ**.
- Hiệu ứng phát quang `@keyframes portPulseAnim` kết hợp `<filter id="portGlow">` giúp người xem nhận biết tức thời hai điểm liên kết logic mà không cần đường nối vật lý.

### E. Quy Tắc Bố Trí Không Gian Khi Có Nhiều Cổng
1. **So le vị trí nhãn (Staggered Labeling):** Đối với 2 cổng gần nhau trong cùng một hành lang, cổng phía trên đặt `text_pos="top"`, cổng phía dưới đặt `text_pos="bottom"`.
2. **Khoảng cách tối thiểu:** Duy trì bước nhảy trục $\Delta y \ge 30\text{ px}$ giữa hai tâm cổng liền kề.

---

## 2. Hình Học Đối Xứng & Thu Gọn Chiều Cao Khung Nhìn (Tight-Fit Canvas)

### A. Triệt Tiêu Khoảng Chết Đáy (Dead Space Elimination)
- Loại bỏ hoàn toàn các dải Header Sector tĩnh trên background. Đẩy toàn bộ các thẻ hàng đầu lên tọa độ $y = 35$.
- **Quy tắc lề đối xứng tuyệt đối (Symmetrical Margin):**
  - Lề đỉnh: 35px
  - Lề đáy: 35px
  - Lề trái/phải: 45px
- **Công thức tính chiều cao Canvas chính xác:**
  $$H_{\\text{canvas}} = y_{\\max} + 35\\text{ px}$$
  - Với Medallion Lakehouse: $y_{\\max} = 760\\text{ px} \\implies H = 795\\text{ px}$.
  - Với Streaming Topology: $y_{\\max} = 775\\text{ px} \\implies H = 810\\text{ px}$.
- **Gắn kết liền mạch khối chú thích (Footer Notes):**
  - Đáy khung SVG và đỉnh của khối Footer Notes duy trì khoảng cách đệm `margin-top: 18px`.
  - Khắc phục triệt để hiện tượng sơ đồ chính và các thẻ chú thích bị cắt rời thành hai khu vực độc lập.

---

## 3. Quy Chuẩn Vi Mô Kiểu Chữ (Micro-Typography & Information Density)

1. **Thẻ Monospace Chứa Tên Tệp & Thông Số Kỹ Thuật:**
   - Đối với các chuỗi ký tự dài như tên tệp cấu hình (`download_history.json`, `config.json`), không in chung dòng văn bản thường.
   - Tách thành một chip tag riêng biệt với nền tối `#1e293b`, viền mảnh, phông `Geist Mono` màu hổ phách `#fbbf24`.
   - Khoảng cách an toàn từ mép chữ đến mép phải của thẻ luôn đảm bảo $\ge 40\text{ px}$.
2. **Tiêu Đề Cô Đọng & Eyebrow Taxonomy:**
   - Tiêu đề chính không vượt quá 50 ký tự, đi thẳng vào bản chất hệ thống.
   - Eyebrow Header đóng vai trò Thẻ phân loại kiến trúc (`TAXONOMY TAG`), viết hoa toàn bộ với dấu chấm giữa: `MEDALLION LAKEHOUSE · QUANT ENGINE`.

---

## 4. Khung Hiển Thị Trình Duyệt (Viewport Scaling & 1:1 Display)

1. **Container Độ Rộng Toàn Bản (Full-Width Desktop Display):**
   - Thiết lập `.container { width: 100%; max-width: 1540px; }` trong `src/core/base.py`.
   - Giúp canvas vector $1440 \times 795$ hiển thị ở tỷ lệ nguyên bản 1:1 siêu nét trên màn hình Full HD / 2K / 4K mà không bị co nhỏ (downscale).
2. **Khung Nhúng Iframe Trong Trạm Điều Phối (Portal Shell):**
   - Thiết lập `iframe { width: 100%; height: 1080px; }` trong `Product/index.html` và `Product/en/index.html` để bao trọn cả Header, Metrics, SVG Canvas và Footer Notes mà không sinh thanh cuộn kép.
3. **Kết Xuất Ảnh 2x Retina PNG:**
   - Luôn sử dụng Google Chrome Headless với tham số `--force-device-scale-factor=2 --window-size=1600,1200` để đảm bảo độ phân giải thực tế đạt $3200 \times 2400$.

---

## 5. Quy Chuẩn Institutional Financial Terminal

1. **Tuyệt Đối Không Sử Dụng Emoji / Icon Hoạt Họa:**
   - Không đưa emoji vào tiêu đề, nút bấm, nhãn chỉ số, commit log hay tài liệu kỹ thuật.
   - Thay thế bằng các ký hiệu hình học sắc sảo: chấm tròn vi mô `&bull;`, số thứ tự mono `1.`, `2.`, hoặc đường viền mảnh tinh tế.
2. **Màu Sắc Phục Vụ Dữ Liệu:**
   - Xanh ngọc (`#089981`): Luồng tăng trưởng, xác thực, Live Stream.
   - Đỏ hồng (`#f23645`): Luồng suy giảm, ngắt mạch rủi ro, cảnh báo sàn.
   - Hổ phách (`#f59e0b`): Cảnh báo, khối lượng giao dịch, cơ chế dự phòng.
   - Tím (`#a855f7`): Khối định lượng, logic O(1), phiên giao dịch.
   - Xanh cyan (`#06b6d4`): Cổng tiếp nhận, bộ nhớ đệm RAM O(1).
   - Xanh dương (`#2962ff`): Điều hướng, xa lộ phản hồi hồi tiếp.
