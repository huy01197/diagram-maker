# diagram-maker

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero_External-blue?style=flat-square)]()
[![Render Engine](https://img.shields.io/badge/Render_Engine-100%25_Vector_SVG-purple?style=flat-square)]()
[![Design Standard](https://img.shields.io/badge/Design-Institutional_Financial_Terminal-089981?style=flat-square)]()
[![Topology Engine](https://img.shields.io/badge/Topologies-Streaming_%7C_Closed--Loop_%7C_Medallion-f59e0b?style=flat-square)]()

Bộ công cụ tự động hóa toàn trình (End-to-End Architecture Engine) giúp biên dịch các tệp đặc tả JSON AST thành **Sơ đồ Kiến trúc Vector SVG & HTML độc lập** theo chuẩn thiết kế **Institutional Financial Terminal** (tương đương Bloomberg, TradingView, TCBS).

Hệ thống loại bỏ hoàn toàn các mẫu sơ đồ cột rập khuôn đơn điệu, thay thế bằng **Topology Chuyên Biệt Theo Bản Chất Hệ Thống** (Streaming Fan-In, Closed-Loop Event Pipeline, Medallion Columnar Lakehouse), tích hợp các **Micro-Mockup Trực Quan** (Treemap, Candlestick OHLC, 4-Pane Plotly Chart) và thuật toán định tuyến **Zero-Collision Bezier Routing**.

---

## 1. Triết Lý Thiết Kế & Điểm Nhấn Kỹ Thuật

### A. Chuẩn Mực Institutional Financial Terminal
* **Bảng màu Neo-Dark chuẩn mực:** Phông nền sâu đa tầng (`#070a12`, `#0c121e`, `#1b253b`) kết hợp các gam màu chức năng biểu đạt luồng dữ liệu: Xanh lục Emerald (`#089981`), Xanh Cyan (`#06b6d4`), Xanh Sky (`#38bdf8`), Vàng Amber (`#f59e0b`), Tím Purple (`#a855f7`), Đỏ Rose (`#f23645`).
* **Quy tắc Zero-Emoji Tuyệt Đối:** Loại bỏ toàn bộ biểu tượng cảm xúc và icon hoạt họa rực rỡ; giao diện hoàn toàn sử dụng Typography nghiêm túc (`-apple-system`, `Geist Mono`), huy hiệu trạng thái (status badges), và ký hiệu toán học/kỹ thuật.
* **Định Dạng Tiếng Việt Chuẩn Mực:** 100% nhãn, mô tả và chỉ số được hiển thị bằng tiếng Việt chuẩn ngữ pháp, dấu thanh rõ ràng, đầy đủ ngữ cảnh chuyên ngành tài chính - công nghệ.

### B. Kiến Trúc Đa Topology (Dynamic Multi-Topology Engine)
Thay vì ép buộc mọi hệ thống vào một cấu trúc 4-tầng hoặc 5-tầng cột dọc tĩnh, `diagram-maker` nhận diện và phân phối theo cấu trúc topology tối ưu:
1. **Streaming Fan-In & Dual-Rail Pipeline:** Dành cho các hệ thống tiếp nhận thị trường thời gian thực, kết hợp kênh đẩy chính và kênh dự phòng, quản lý trạng thái bộ nhớ O(1) và kết xuất trực quan treemap.
2. **Closed-Loop Interactive Event Pipeline:** Dành cho các bot giao dịch và ứng dụng tương tác, có luồng yêu cầu người dùng, kiểm soát tần suất (Rate Limiter), bộ đệm kép SQLite, chiến lược định lượng và đường cao tốc phản hồi (feedback highway).
3. **Medallion Columnar Lakehouse & Quant Terminal:** Dành cho các hệ thống Big Data định lượng, qua các tầng chuẩn hóa Bronze -> Silver (Parquet) -> Gold (Feature Store) -> Platinum (Terminal 4 khung nhìn).

### C. Cơ Chế Zero-Collision & Định Tuyến Bezier
* **Khoảng Cách Hành Lang (Corridor Clearance Rule):** Đảm bảo khoảng cách tối thiểu giữa các khối xử lý $W_{\text{corridor}} \ge 110\text{px}$ để chứa trọn vẹn nhãn giao thức (pill badge $100\text{px}$) mà không gây chồng đè đường viền.
* **Định Tuyến Bezier Động:** Tính toán tiếp điểm xuất phát và tiếp điểm đích với hai điểm điều khiển cân xứng:
  $$C_1 = (x_1 + dx \times 0.5, y_1), \quad C_2 = (x_2 - dx \times 0.5, y_2)$$
* **Lưới Tọa Độ Dot-Grid & Hiệu Ứng Glow Vector:** Toàn bộ SVG sử dụng bộ lọc phát sáng mềm (`feGaussianBlur`), bóng đổ thẻ xử lý và nền chấm dot-grid tinh tế.

### D. Tích Hợp Micro-Mockup Đồ Họa Vector
Mỗi sơ đồ kiến trúc được nhúng trực tiếp một mockup vector mô phỏng giao diện đích thực tế:
* **Heatmap Treemap Mockup:** Thể hiện trực quan tỷ lệ vốn hóa và sắc thái tăng/giảm (+6.8% VCB, +4.2% FPT, -1.8% HPG).
* **Candlestick OHLC Mockup:** Thể hiện nến tăng xanh/giảm đỏ, bóng nến (wicks), đường trung bình MA20/MA50, khối lượng Volume và huy hiệu BUY CANSLIM.
* **4-Pane Plotly Mockup:** Thể hiện đa khung nhìn đồng bộ thời gian (Candles + MA, Volume + VWAP, MACD Histogram, RSI 30/70).

---

## 2. Hình Ảnh Trực Quan Từ Các Dự Án Thực Tế

### A. Vietnam Stock Real-Time Heatmap
* **Topology:** Streaming Fan-In & Dual-Rail Pipeline (`vietnam_stock_heatmap.json`)
* **Đặc điểm:** Tách biệt kênh đẩy SignalR SSI (2.500+ tick/s) và Polling Live 2.5s, RAM Store Thread-safe Mutex O(1) < 0.12ms, ma trận 15 nhóm ngành VS-Sector và Canvas Treemap ECharts 60 FPS.

<p align="center">
  <img src="assets/vietnam_stock_heatmap.png" width="100%" alt="Vietnam Stock Heatmap Architecture" />
</p>

---

### B. Telegram Stock Bot
* **Topology:** Closed-Loop Interactive Event Pipeline (`telegram_stock_bot.json`)
* **Đặc điểm:** Tiếp nhận lệnh Telegram `/chart FPT`, Token Bucket Rate Limiter, In-Memory Fast Cache + SQLite 100 phiên, Lõi CANSLIM đa chỉ báo (Xu hướng, Động lượng, Bùng nổ Vol), Trình vẽ đồ thị nến mplfinance nhúng trực tiếp và đường cao tốc gửi ảnh phản hồi người dùng.

<p align="center">
  <img src="assets/telegram_stock_bot.png" width="100%" alt="Telegram Stock Bot Architecture" />
</p>

---

### C. Vietnamese Stock Analysis Terminal
* **Topology:** Medallion Columnar Lakehouse & Quant Terminal (`vietnamese_stock_analysis.json`)
* **Đặc điểm:** Tầng Bronze (Ingestion CafeF ZIP), Tầng Silver (Kho dữ liệu cột Snappy Parquet nén -85% dung lượng, tốc độ đọc gấp 10 lần), Tầng Gold (Feature Store & Sector Breadth Matrix) và Tầng Platinum (Streamlit Terminal với mockup 4 panel nến, volume, MACD, RSI).

<p align="center">
  <img src="assets/vietnamese_stock_analysis.png" width="100%" alt="Vietnamese Stock Analysis Architecture" />
</p>

---

## 3. Cấu Trúc Cây Thư Mục Dự Án

```
diagram-maker/
├── main.py                        # Điểm khởi chạy 1-Click & CLI Entrypoint
├── requirements.txt               # Danh mục phụ thuộc (Zero External Dependencies)
├── LICENSE                        # Giấy phép nguồn mở MIT
├── README.md                      # Tài liệu kỹ thuật chi tiết
│
├── src/                           # Mã nguồn kiến trúc lõi (Core Engine)
│   ├── __init__.py                # Xuất các lớp và hàm biên dịch chính
│   ├── engine.py                  # DiagramEngine: Bộ điều phối tự động phân loại Topology
│   ├── cli.py                     # Trình xử lý dòng lệnh đa năng
│   ├── compiler.py                # GraphCompiler: Trình biên dịch kế thừa (4/5-tier column)
│   ├── slide_compiler.py          # SlideCompiler: Trình biên dịch slide thuyết trình
│   │
│   ├── core/                      # Các module thành phần hạ tầng
│   │   ├── __init__.py
│   │   ├── palette.py             # Bảng màu Institutional Dark chuẩn mực
│   │   ├── base.py                # SVG defs, dotGrid canvas, CSS shell tự co giãn
│   │   ├── geometry.py            # Dây nối Bezier, huy hiệu pill badge chống va chạm
│   │   └── mockups.py             # Thư viện vi mô (Mini Treemap, Candlestick, 4-Pane Chart)
│   │
│   └── topologies/                # Trình biên dịch kiến trúc chuyên biệt
│       ├── __init__.py
│       ├── streaming_topology.py  # Trình biên dịch luồng Streaming thời gian thực
│       ├── interactive_loop.py    # Trình biên dịch vòng lặp phản hồi Bot tương tác
│       └── medallion_lakehouse.py # Trình biên dịch hồ dữ liệu cột Medallion Lakehouse
│
├── specs/                         # Thư mục đặc tả cấu trúc JSON (AST Specs)
│   ├── samples/                   # File mẫu kiểm thử đơn giản
│   │   ├── sample_diagram.json
│   │   └── sample_slide.json
│   └── projects/                  # Đặc tả thực tế các hệ thống chứng khoán
│       ├── vietnam_stock_heatmap.json      # Topology Streaming
│       ├── telegram_stock_bot.json         # Topology Closed-Loop
│       ├── vietnamese_stock_analysis.json  # Topology Medallion
│       ├── vietnam_stock_heatmap_5tier.json
│       ├── telegram_stock_bot_5tier.json
│       └── vietnamese_stock_analysis_5tier.json
│
├── output/                        # Tệp HTML vector độc lập sau khi biên dịch
│   ├── vietnam_stock_heatmap.html
│   ├── telegram_stock_bot.html
│   ├── vietnamese_stock_analysis.html
│   └── ...
│
└── assets/                        # Ảnh chụp độ phân giải cao đã qua kiểm định DevTools
    ├── vietnam_stock_heatmap.png
    ├── telegram_stock_bot.png
    └── vietnamese_stock_analysis.png
```

---

## 4. Hướng Dẫn Sử Dụng & Vận Hành CLI

### Yêu Cầu Môi Trường
* **Python >= 3.10**
* **Không cần bất kỳ thư viện bên ngoài nào** (100% Python Standard Library).

### 1-Click Biên Dịch Toàn Bộ
Để tự động quét và biên dịch tất cả các tệp đặc tả JSON trong thư mục `specs/`:
```bash
python3 main.py --all
```
Hoặc chạy trực tiếp không đối số:
```bash
python3 main.py
```

### Biên Dịch Riêng Biệt Từng Tệp Đặc Tả
```bash
# Biên dịch sơ đồ luồng Heatmap
python3 main.py specs/projects/vietnam_stock_heatmap.json -o output/vietnam_stock_heatmap.html

# Biên dịch sơ đồ Bot tương tác Telegram
python3 main.py specs/projects/telegram_stock_bot.json -o output/telegram_stock_bot.html

# Biên dịch sơ đồ Kho dữ liệu phân tích định lượng
python3 main.py specs/projects/vietnamese_stock_analysis.json -o output/vietnamese_stock_analysis.html
```

### Mở Xem Trực Tiếp Trên Trình Duyệt
```bash
open output/vietnam_stock_heatmap.html
open output/telegram_stock_bot.html
open output/vietnamese_stock_analysis.html
```

---

## 5. Quy Chuẩn Đặc Tả Cấu Trúc JSON (DSL AST)

Mỗi sơ đồ kiến trúc được định nghĩa tường minh qua tệp JSON AST. Dưới đây là mẫu khai báo một hệ thống Topology:

```json
{
  "title": "Tên Hệ Thống - Phụ Đề Kiến Trúc Kỹ Thuật",
  "eyebrow": "TÊN TOPOLOGY · PHÂN HẠNG VẬN HÀNH",
  "topology": "streaming",
  "width": 1320,
  "height": 915,
  "metrics": [
    { "label": "Độ Trễ Tick Khớp", "value": "< 16 ms (60 FPS)", "color": "#34d399" },
    { "label": "Thông Lượng Stream", "value": "2.500+ Tick/Giây", "color": "#38bdf8" },
    { "label": "Truy Vấn RAM Store", "value": "O(1) < 0.12 ms", "color": "#38bdf8" },
    { "label": "Truyền Dẫn Kép", "value": "WebSocket + REST", "color": "#fbbf24" }
  ],
  "footer_notes": [
    {
      "color": "#38bdf8",
      "title": "TIẾP NHẬN DỮ LIỆU",
      "desc": "Mô tả chi tiết cách thức tiếp nhận dữ liệu thời gian thực."
    },
    {
      "color": "#34d399",
      "title": "LÕI XỬ LÝ TRUNG TÂM",
      "desc": "Mô tả thuật toán xử lý dữ liệu và cấu trúc bộ nhớ."
    }
  ]
}
```

---

## 6. Mở Rộng & Bổ Sung Topology Mới

Để tạo thêm một kiến trúc topology mới (ví dụ: `MicroservicesMesh` hoặc `OrderBookMatching`):
1. Tạo trình biên dịch mới tại `src/topologies/my_new_topology.py` kế thừa cấu trúc từ `src/core/base.py` và `src/core/geometry.py`.
2. Đăng ký tên topology vào `TOPOLOGY_REGISTRY` trong `src/engine.py`:
   ```python
   TOPOLOGY_REGISTRY["my_new_topology"] = MyNewTopologyCompiler
   ```
3. Khai báo tệp JSON tương ứng với thuộc tính `"topology": "my_new_topology"`.
4. Chạy `python3 main.py specs/projects/my_project.json`.

---

## 7. Giấy Phép (License)

Dự án được phân phối dưới giấy phép mã nguồn mở [MIT License](LICENSE).
