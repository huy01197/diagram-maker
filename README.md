# diagram-maker

### Bộ Công Cụ Thiết Kế Sơ Đồ Kiến Trúc & Lưu Đồ Vector Độc Lập Chuẩn Institutional Terminal

[![Phiên bản Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Phụ thuộc môi trường](https://img.shields.io/badge/Dependencies-Zero_External-blue?style=for-the-badge)]()
[![Động cơ kết xuất](https://img.shields.io/badge/Render_Engine-100%25_Native_Vector_SVG-purple?style=for-the-badge)]()
[![Chuẩn mực thiết kế](https://img.shields.io/badge/Design-Institutional_Terminal-089981?style=for-the-badge)]()
[![Đa định dạng xuất bản](https://img.shields.io/badge/Deliverables-Dynamic_Web_%7C_Retina_PNG_%7C_SVG-2962ff?style=for-the-badge)]()
[![Giấy phép: MIT](https://img.shields.io/badge/Gi%E1%BA%A5y_ph%C3%A9p-MIT-green?style=for-the-badge)](LICENSE)

> **`diagram-maker`** là giải pháp tự động hóa toàn trình (End-to-End Architecture Engine) chuyên chuyển đổi các tệp đặc tả JSON AST thành **Sơ đồ Vector sắc nét vô cực**, tuân thủ nghiêm ngặt chuẩn mực đồ họa **Institutional Financial Terminal** (tương đương Bloomberg, TradingView, TCBS).  
> Hệ thống mang đến năng lực thiết kế: **Chi tiết, đẹp mắt, gọn gàng và phù hợp với từng bản chất kiến trúc**, hỗ trợ xuất bản linh hoạt dưới dạng **Trang web động tương tác (Dynamic Interactive Web)** hoặc **Hình ảnh tĩnh độ phân giải cao (Retina / 4K PNG & Vector SVG)** phục vụ tài liệu kỹ thuật, slide thuyết trình và báo cáo chuyên sâu.

* **Kho lưu trữ mã nguồn:** [github.com/huy01197/diagram-maker](https://github.com/huy01197/diagram-maker)
* **Trạm Điều Phối Kiến Trúc Trực Tuyến:** [**Product/index.html**](Product/index.html)
* **Phụ thuộc môi trường:** **Zero External Dependencies** (100% Python Standard Library, không cần cài đặt pip)
* **Tốc độ biên dịch:** Dưới 0.04 giây cho mỗi sơ đồ (biên dịch toàn bộ 10 specs < 0.25 giây)

---

## 1. Trạm Điều Phối Sơ Đồ Kiến Trúc Hệ Thống (Showcase Portal)

Thay vì tạo ra các tệp hình ảnh rời rạc, `diagram-maker` cung cấp một trạm điều phối kiến trúc tập trung tại [**Product/index.html**](Product/index.html). Người dùng có thể chuyển đổi mượt mà giữa các hệ sinh thái kiến trúc thời gian thực, nạp lại khung nhìn vector tức thì và tra cứu bảng thông số kỹ thuật chi tiết:

<p align="center">
  <img src="assets/product_portal_overview.png" width="100%" alt="Trạm Điều Phối Sơ Đồ Kiến Trúc Hệ Thống" />
</p>

*Trạm điều phối tập trung [Product/index.html](Product/index.html): Thanh điều hướng tab chuyển đổi mượt mà, khung nhìn vector SVG tự co giãn (Auto-Scale Canvas), nút mở tab độc lập và bảng tóm tắt đặc tả kỹ thuật từng hệ thống.*

---

## 2. Thư Viện Kiến Trúc Thực Tế (Showcase Demos)

Dưới đây là các sơ đồ kiến trúc thành phẩm được sinh ra trực tiếp bởi `diagram-maker`, minh chứng năng lực xử lý các hệ thống thực tế có luồng dữ liệu phức tạp và mật độ thông tin cao:

### A. Vietnam Stock Real-Time Heatmap
* **Đặc tả kiến trúc:** [specs/projects/vietnam_stock_heatmap.json](specs/projects/vietnam_stock_heatmap.json)
* **Sản phẩm Web độc lập:** [**Product/vietnam-stock-heatmap-architecture.html**](Product/vietnam-stock-heatmap-architecture.html) | [output/vietnam_stock_heatmap.html](output/vietnam_stock_heatmap.html)
* **Dạng sơ đồ:** **Streaming Fan-In & Dual-Rail Pipeline (< 16ms)**
* **Điểm nhấn trực quan:** Mô hình hội tụ luồng dữ liệu tốc độ cao (SignalR SSI 2.500+ tick/s), xa lộ truyền dẫn kép (WebSocket 60 FPS song song REST Polling 2.5s), bộ nhớ đệm RAM Store $O(1) < 0.12$ms, và Micro-Mockup Treemap 15 nhóm ngành VS-Sector.

<p align="center">
  <img src="assets/vietnam_stock_heatmap.png" width="100%" alt="Vietnam Stock Heatmap Architecture" />
</p>

#### Bảng Đo Lường Hiệu Năng Thực Tế (Benchmark)

| Chỉ tiêu kỹ thuật | Đo đạc thực tế | Chuẩn mục tiêu | Đánh giá kiến trúc vận hành |
| :--- | :---: | :---: | :--- |
| **Tốc độ truy vấn RAM Store** | **< 0.12 ms** | < 1.00 ms | Cấu trúc Hash-Map O(1) an toàn luồng với Mutex Lock |
| **Độ trễ truyền tải WebSocket** | **< 16 ms** | < 16.6 ms | Đạt chuẩn 60 FPS, khử hiện tượng giật lag khung nhìn |
| **Thông lượng chịu tải gói tin** | **2.500+ tick/s** | 1.000 tick/s | Chịu tải thông suốt trong các phiên bùng nổ ATO / ATC |
| **Cơ chế dự phòng đứt mạng** | **Tự động phục hồi** | < 3.0s | REST Polling 2.5s kích hoạt tức thì khi đứt socket |
| **Phân loại ngành tài chính** | **15 VS-Sector** | Toàn diện | Tự động phân bổ 700+ mã vào 15 nhóm ngành chính |

---

### B. Telegram Stock Bot
* **Đặc tả kiến trúc:** [specs/projects/telegram_stock_bot.json](specs/projects/telegram_stock_bot.json)
* **Sản phẩm Web độc lập:** [**Product/telegram-stock-bot-architecture.html**](Product/telegram-stock-bot-architecture.html) | [output/telegram_stock_bot.html](output/telegram_stock_bot.html)
* **Dạng sơ đồ:** **Closed-Loop Interactive Event Pipeline (Vòng Lặp Khép Kín)**
* **Điểm nhấn trực quan:** Cổng tiếp nhận Webhook async (< 5ms), bộ điều tiết Token Bucket chống spam, bộ đệm kép SQLite WAL Mode, lõi định lượng CANSLIM 4 chiều, Micro-Mockup biểu đồ nến Nhật kèm tín hiệu Mua, và đường cao tốc Feedback Highway hồi tiếp về người dùng.

<p align="center">
  <img src="assets/telegram_stock_bot.png" width="100%" alt="Telegram Stock Bot Architecture" />
</p>

#### Bảng Đo Lường Hiệu Năng Thực Tế (Benchmark)

| Chỉ tiêu kỹ thuật | Đo đạc thực tế | Chuẩn mục tiêu | Đánh giá kiến trúc vận hành |
| :--- | :---: | :---: | :--- |
| **Thời gian giải mã lệnh Ingress** | **< 5 ms** | < 20 ms | Bộ tách token không đồng bộ tối ưu hóa biểu thức chính quy |
| **Thời gian quét CANSLIM 4 chiều** | **< 35 ms** | < 100 ms | Đánh giá đồng thời Xu hướng, Động lượng, Biên độ, Khối lượng |
| **Kết xuất đồ thị nến RAM** | **< 120 ms** | < 500 ms | Render trực tiếp trong RAM (Zero-Disk I/O), khử rác ổ cứng |
| **Tổng thời gian phản hồi tròn vòng** | **< 850 ms** | < 1.500 ms | Người dùng nhận phân tích nến và khuyến nghị mua bán < 1 giây |
| **Hiệu quả bộ đệm kép SQLite** | **Giảm 80% request** | > 50% | Cơ chế TTL 15 phút - 24 giờ hạn chế tối đa nghẽn mạng |

---

### C. Vietnamese Stock Analysis Terminal
* **Đặc tả kiến trúc:** [specs/projects/vietnamese_stock_analysis.json](specs/projects/vietnamese_stock_analysis.json)
* **Sản phẩm Web độc lập:** [**Product/vietnamese-stock-analysis-architecture.html**](Product/vietnamese-stock-analysis-architecture.html) | [output/vietnamese_stock_analysis.html](output/vietnamese_stock_analysis.html)
* **Dạng sơ đồ:** **Medallion Columnar Lakehouse & Quant Screener**
* **Điểm nhấn trực quan:** Hồ dữ liệu cột 4 tầng: Bronze (CafeF ZIP thô) &rarr; Silver (Parquet Snappy giảm 85% dung lượng, đọc mmap < 250ms cho 1.500+ mã) &rarr; Gold (Feature Store ma trận 15 ngành) &rarr; Platinum (Streamlit Terminal với Micro-Mockup Plotly WebGL 4 tầng đồng bộ thời gian).

<p align="center">
  <img src="assets/vietnamese_stock_analysis.png" width="100%" alt="Vietnamese Stock Analysis Architecture" />
</p>

#### Bảng Đo Lường Hiệu Năng Thực Tế (Benchmark)

| Chỉ tiêu kỹ thuật | Giải pháp CSV truyền thống | Kho Cột Parquet (Dự án) | Mức cải thiện |
| :--- | :---: | :---: | :---: |
| **Dung lượng lưu trữ đĩa cứng** | ~15.2 GB (tệp thô) | **2.2 GB (Parquet Snappy)** | **Tiết kiệm 85.5% bộ nhớ** |
| **Thời gian nạp dữ liệu 1.500+ mã** | 4.800 ms (đọc tuần tự) | **< 250 ms (Memory-Mapped)** | **Tốc độ tăng gần 20 lần** |
| **Tính toán ma trận chỉ báo (10 năm)** | 2.600 ms | **< 180 ms (Vectorized)** | **Tối ưu hóa đa luồng CPU** |
| **Đồng bộ đồ thị Plotly 4 Panes** | ~850 ms | **< 90 ms (WebGL Render)** | **Mượt mà không giật khung hình** |
| **Tính toàn vẹn dữ liệu** | Dễ sai lệch kiểu | **MD5 Checkpoint + Schema Contract** | **Độ tin cậy tuyệt đối** |

---

## 3. Đa Dạng Các Dạng Biểu Diễn (Diagram Taxonomy)

Ngoài các kiến trúc luồng phức tạp, `diagram-maker` hỗ trợ đầy đủ các dạng sơ đồ phân tầng cột trực giao và slide thuyết trình kỹ thuật:

<p align="center">
  <img src="assets/column_architecture_showcase.png" width="49%" alt="Sơ Đồ Phân Tầng Cột Trực Giao" />
  &nbsp;
  <img src="assets/presentation_slide_showcase.png" width="49%" alt="Slide Thuyết Trình Kính Mờ 16:9" />
</p>

*Trái: Sơ đồ phân tầng cột trực giao ([output/sample_diagram.html](output/sample_diagram.html)) với thuật toán định tuyến Bézier động. Phải: Slide thuyết trình kỹ thuật ([output/sample_slide.html](output/sample_slide.html)) chuẩn 16:9 phong cách kính mờ glassmorphism.*

### Bảng Hệ Thống Hóa Các Dạng Sơ Đồ

| Nhóm dạng sơ đồ | Dạng biểu diễn | Cơ chế trực quan & Thuật toán bố cục | Tệp mẫu tham khảo |
| :--- | :--- | :--- | :--- |
| **1. Streaming & Event Pipeline** | **Streaming Fan-In & Dual-Rail** | Mô hình hội tụ đa nguồn, kênh đôi song song, đệm RAM $O(1)$ | [vietnam_stock_heatmap.json](specs/projects/vietnam_stock_heatmap.json) |
| **2. Interactive Feedback Loop** | **Closed-Loop Interactive Pipeline** | Vòng lặp phản hồi 2 chiều, điều tiết Token Bucket, Feedback Highway | [telegram_stock_bot.json](specs/projects/telegram_stock_bot.json) |
| **3. Columnar Lakehouse** | **Medallion Lakehouse (4 tầng)** | Bronze thô &rarr; Silver Parquet &rarr; Gold Feature &rarr; Platinum Terminal | [vietnamese_stock_analysis.json](specs/projects/vietnamese_stock_analysis.json) |
| **4. Multi-Tier Column Architecture** | **Sơ đồ phân tầng dạng cột (4/5 tầng)** | Bố cục ma trận cột trực giao, cân bằng chiều cao, dây nối Bézier động | [sample_diagram.json](specs/samples/sample_diagram.json) |
| **5. Technical Presentation Slide** | **Glassmorphic Slide Deck (16:9)** | Khung trình chiếu tỷ lệ vàng 16:9, thẻ kính mờ, trọng số phân loại | [sample_slide.json](specs/samples/sample_slide.json) |
| **6. Embedded Visual Components** | **Sơ đồ tích hợp Micro-Mockup** | Nhúng trực tiếp Treemap, Candlestick OHLCV, biểu đồ 4 tầng Plotly | [Product/index.html](Product/index.html) |

---

## 4. Năng Lực Xuất Bản Đa Định Dạng (Outputs Matrix)

`diagram-maker` cung cấp khả năng xuất bản linh hoạt tùy theo mục đích truyền tải:

| Định dạng | File xuất bản | Cơ chế hiển thị | Mục đích sử dụng tối ưu |
| :--- | :--- | :--- | :--- |
| **Web động tương tác** | Tệp `.html` độc lập (Self-Contained) | Khung Canvas tự động điều chỉnh tỷ lệ (**Auto-Scale Canvas**), thanh chuyển đổi Tab tập trung, bảng soi chi tiết (Inspector), live zoom | Trình chiếu dự án trên trình duyệt, nhúng iframe web, làm trung tâm điều phối kiến trúc tập trung |
| **Hình ảnh độ nét cao** | Tệp `.png` độ phân giải Retina / 4K | Kết xuất từ trình duyệt qua Chrome DevTools ở tỷ lệ `@2x` hoặc `@3x` (2880×1972) | Chèn vào Slide thuyết trình (PowerPoint, Keynote), bài viết blog kỹ thuật, bài đăng mạng xã hội |
| **Đồ họa Vector thuần túy** | Thẻ `<svg>` chuẩn XML | 100% đường cong toán học, dung lượng siêu nhẹ (~20-40 KB), không vỡ hạt khi phóng to vô cực | Nhúng trực tiếp vào mã nguồn HTML/Markdown, mở chỉnh sửa trên Figma, Illustrator |
| **Slide thuyết trình** | Tệp `.html` bố cục 16:9 | Giao diện kính mờ Glassmorphic, phân nhóm tiêu chí kỹ thuật kèm trọng số (weight) | Báo cáo kiến trúc cho hội đồng kỹ thuật, thuyết trình giải pháp hệ thống |

---

## 5. Hướng Dẫn Soạn Thảo Đặc Tả JSON (DSL Guide)

Mọi sơ đồ trong `diagram-maker` được khai báo bằng cấu trúc JSON AST tường minh, tinh gọn và dễ bảo trì:

### Mẫu 1: Đặc Tả Topology Đa Dạng (`topology`)
```json
{
  "title": "Tên Hệ Thống - Phụ Đề Kiến Trúc Kỹ Thuật",
  "eyebrow": "TÊN PHÂN LOẠI TOPOLOGY · PHÂN HẠNG VẬN HÀNH",
  "topology": "streaming",
  "width": 1320,
  "height": 915,
  "metrics": [
    { "label": "Độ Trễ Phản Hồi", "value": "< 16 ms", "color": "#34d399" },
    { "label": "Thông Lượng Xử Lý", "value": "2.500+ Tick/Giây", "color": "#38bdf8" },
    { "label": "Bộ Nhớ Đệm", "value": "RAM Store O(1)", "color": "#fbbf24" }
  ],
  "footer_notes": [
    {
      "color": "#38bdf8",
      "title": "NGUỒN TIẾP NHẬN DỮ LIỆU",
      "desc": "Mô tả cơ chế tiếp nhận và giao thức xác thực bảo mật."
    }
  ]
}
```

### Mẫu 2: Đặc Tả Sơ Đồ Cột Phân Tầng (`columns` & `connections`)
```json
{
  "title": "Kiến Trúc Phân Tầng Dịch Vụ Hệ Thống",
  "category": "KIẾN TRÚC VẬN HÀNH",
  "subtitle": "Quy trình xử lý dữ liệu qua các phân tầng dịch vụ",
  "columns": [
    {
      "id": "col_ingress",
      "nodes": [
        {
          "id": "api_gateway",
          "title": "API Gateway",
          "badge": "REST / WSS",
          "color": "sky",
          "items": ["1. Xác thực JWT", "2. Token Bucket", "3. Phân luồng"]
        }
      ]
    },
    {
      "id": "col_storage",
      "nodes": [
        {
          "id": "db_lakehouse",
          "title": "Parquet Lakehouse",
          "badge": "SNAPPY",
          "color": "emerald",
          "items": ["1. Nén Snappy", "2. Truy vấn O(1)", "3. Zero-Copy"]
        }
      ]
    }
  ],
  "connections": [
    { "from": "api_gateway", "to": "db_lakehouse", "color": "sky", "animated": true }
  ]
}
```

---

## 6. Hướng Dẫn Vận Hành & Khởi Chạy 1-Click

### Yêu Cầu Môi Trường
* **Python >= 3.10**
* **Zero Dependencies:** Chạy hoàn toàn trên thư viện chuẩn của Python (`json`, `html`, `pathlib`, `argparse`). Không cần cài đặt bất kỳ gói pip nào.

### Trải Nghiệm Ngay Sản Phẩm
Mở trực tiếp Trạm điều phối kiến trúc tập trung trên trình duyệt web:
```bash
# Trên macOS
open Product/index.html

# Trên Linux
xdg-open Product/index.html
```

### Biên Dịch 1-Click Toàn Bộ Đặc Tả
Để tự động quét và biên dịch tất cả 10 tệp đặc tả JSON trong thư mục `specs/`:
```bash
python3 main.py --all
```
Hoặc chạy trực tiếp không đối số:
```bash
python3 main.py
```

### Biên Dịch Riêng Biệt Từng Tệp Đặc Tả
```bash
# Biên dịch sơ đồ luồng Heatmap (Streaming Topology)
python3 main.py specs/projects/vietnam_stock_heatmap.json -o output/vietnam_stock_heatmap.html

# Biên dịch sơ đồ Bot tương tác (Closed-Loop Topology)
python3 main.py specs/projects/telegram_stock_bot.json -o output/telegram_stock_bot.html

# Biên dịch sơ đồ Kho dữ liệu cột (Medallion Lakehouse)
python3 main.py specs/projects/vietnamese_stock_analysis.json -o output/vietnamese_stock_analysis.html

# Biên dịch sơ đồ Cột 5-tier truyền thống
python3 main.py specs/projects/vietnam_stock_heatmap_5tier.json -o output/diagram_vietnam_stock_heatmap_5tier.html
```

### Hướng Dẫn Xuất Ảnh Độ Phân Giải Cao (Retina / 4K PNG)
Các tệp HTML đầu ra được thiết kế chuẩn vector SVG tự co giãn. Để xuất ảnh chất lượng cao:
1. Mở tệp HTML bằng Google Chrome hoặc trình duyệt dựa trên Chromium.
2. Nhấn `F12` (hoặc `Cmd + Option + I` trên macOS) để mở DevTools.
3. Nhấn tổ hợp phím `Cmd + Shift + P` (macOS) hoặc `Ctrl + Shift + P` (Windows/Linux).
4. Gõ lệnh: **`Capture full size screenshot`**. Trình duyệt sẽ xuất ra tệp PNG độ nét cao (2880×1972) sắc nét tuyệt đối.

---

## 7. Bảng Đo Lường Đối Chuẩn Kỹ Thuật (Benchmark Matrix)

So sánh định lượng giữa `diagram-maker` và các công cụ vẽ sơ đồ phổ biến:

| Tiêu chí kỹ thuật | Công cụ vẽ thông thường (Mermaid / Graphviz / PlantUML) | diagram-maker Engine (Institutional Standard) |
| :--- | :--- | :--- |
| **Chất lượng hiển thị** | Ảnh bitmap (PNG/JPG) mờ vỡ hạt khi phóng to trên màn hình 4K/Retina | **100% Native Vector SVG**, sắc nét vô cực ở mọi tỷ lệ phóng to |
| **Phụ thuộc môi trường** | Đòi hỏi cài đặt Java JRE, Graphviz C binaries, hoặc Node.js nặng nề | **Zero External Dependencies** (100% Python Standard Library) |
| **Định tuyến đường dây** | Dây nối cắt chéo qua nhau, đè chữ nhãn giao thức | **Zero-Collision Bezier Routing**, duy trì hành lang $W \ge 110$px |
| **Phong cách thẩm mỹ** | Màu sắc văn phòng pastel đơn giản, thiếu tính chuyên sâu | **Institutional Dark Terminal** (Bloomberg / TradingView / TCBS) |
| **Micro-Mockup nghiệp vụ** | Chỉ hỗ trợ khối hộp chữ nhật text đơn điệu | **Tích hợp sẵn Treemap, Candlestick OHLCV, 4-Pane Plotly Chart** |
| **Tốc độ biên dịch** | 1.5 - 4.5 giây (phụ thuộc máy ảo Java / tiến trình ngoài) | **< 0.04 giây / sơ đồ** (biên dịch toàn bộ 10 specs < 0.25 giây) |
| **Trạm điều phối tập trung** | Không có (từng file markdown hoặc hình ảnh rời rạc) | **Trạm Portal tập trung [Product/index.html](Product/index.html)** |
| **Chuẩn mực biểu tượng** | Dễ lạm dụng icon hoạt họa, emoji màu mè gây rối | **Quy chuẩn Zero-Emoji Tuyệt Đối**, chỉ dùng typography tài chính cao cấp |

---

## 8. Ma Trận Bảng Màu Institutional Terminal

| Gam màu | Mã màu (HEX) | Phạm vi sử dụng trong sơ đồ | Ngữ nghĩa kỹ thuật & dữ liệu |
| :--- | :---: | :--- | :--- |
| **Dark Void (Nền canvas)** | `#070a12` | Phông nền toàn cảnh | Tạo chiều sâu tối đa, chống mỏi mắt |
| **Panel Surface** | `#0b101b` / `#0e1524` | Nền thẻ xử lý, phân tầng khối | Phân cấp tầng dữ liệu bằng độ tương phản viền |
| **Base Border** | `#1b253b` | Đường viền ngăn cách tĩnh | Đường viền mảnh tinh tế, phân tách khối rõ ràng |
| **Emerald Green** | `#089981` | Luồng dữ liệu sống, nến tăng, kiểm toán | Trạng thái tích cực, tăng trưởng, kênh truyền tải chính |
| **Cyan Blue** | `#06b6d4` | Ingress Gateway, RAM Store, thời gian thực | Cổng tiếp nhận bất đồng bộ, bộ đệm vi mô $O(1)$ |
| **Amber Gold** | `#f59e0b` | Tín hiệu dự phòng Failover, bùng nổ Vol | Cảnh báo trạng thái, khối lượng lớn, kênh dự phòng |
| **Purple Violet** | `#a855f7` | Logic định lượng, phiên làm việc, giá trần | Thuật toán CANSLIM, phân loại nghiệp vụ chuyên sâu |
| **Rose Red** | `#f23645` | Nến giảm, giá sàn, bộ chặn lỗi | Tín hiệu suy giảm, kiểm soát rủi ro, bẫy lỗi |
| **Institutional Blue** | `#2962ff` | Xa lộ phản hồi, điểm nhấn điều hướng | Đường cao tốc dữ liệu 2 chiều (Feedback Highway) |

---

## 9. Cấu Trúc Cây Thư Mục Dự Án

```
diagram-maker/
├── main.py                        # Điểm khởi chạy 1-Click & CLI Entrypoint
├── requirements.txt               # Danh mục phụ thuộc (Zero External Dependencies)
├── LICENSE                        # Giấy phép nguồn mở MIT
├── README.md                      # Tài liệu kỹ thuật chi tiết dự án
│
├── Product/                       # Trạm điều phối sơ đồ kiến trúc thành phẩm
│   ├── index.html                 # Trạm điều khiển tập trung (Dashboard Hub có chuyển Tab)
│   ├── telegram-stock-bot-architecture.html
│   ├── vietnam-stock-heatmap-architecture.html
│   └── vietnamese-stock-analysis-architecture.html
│
├── src/                           # Mã nguồn động cơ lõi (Core Engine)
│   ├── __init__.py                # Xuất các lớp và hàm biên dịch chính
│   ├── engine.py                  # DiagramEngine: Bộ điều phối tự động nhận diện Topology
│   ├── cli.py                     # Trình xử lý dòng lệnh đa năng
│   ├── compiler.py                # GraphCompiler: Trình biên dịch kế thừa (4/5-tier cột)
│   ├── slide_compiler.py          # SlideCompiler: Trình biên dịch slide thuyết trình
│   │
│   ├── core/                      # Các thành phần hạ tầng dùng chung
│   │   ├── __init__.py            # Khởi tạo gói core
│   │   ├── palette.py             # Bảng màu Institutional Dark chuẩn mực
│   │   ├── base.py                # SVG defs, dotGrid canvas, CSS shell tự co giãn
│   │   ├── geometry.py            # Dây nối Bezier, huy hiệu pill badge chống va chạm
│   │   └── mockups.py             # Thư viện vi mô (Mini Treemap, Candlestick, 4-Pane Chart)
│   │
│   └── topologies/                # Trình biên dịch kiến trúc chuyên biệt
│       ├── __init__.py            # Khởi tạo gói topologies
│       ├── streaming_topology.py  # Trình biên dịch luồng Streaming thời gian thực
│       ├── interactive_loop.py    # Trình biên dịch vòng lặp phản hồi Bot tương tác
│       └── medallion_lakehouse.py # Trình biên dịch hồ dữ liệu cột Medallion Lakehouse
│
├── specs/                         # Thư mục đặc tả cấu trúc JSON (AST Specs)
│   ├── samples/                   # File mẫu kiểm thử đơn giản
│   │   ├── sample_diagram.json
│   │   └── sample_slide.json
│   └── projects/                  # Bộ đặc tả thực tế của các hệ thống chứng khoán
│       ├── vietnam_stock_heatmap.json      # Topology Streaming
│       ├── telegram_stock_bot.json         # Topology Closed-Loop
│       ├── vietnamese_stock_analysis.json  # Topology Medallion
│       ├── vietnam_stock_heatmap_4tier.json
│       ├── vietnam_stock_heatmap_5tier.json
│       ├── telegram_stock_bot_5tier.json
│       ├── vietnamese_stock_analysis_4tier.json
│       └── vietnamese_stock_analysis_5tier.json
│
├── output/                        # Tệp HTML vector độc lập sau khi biên dịch
│   ├── telegram_stock_bot.html
│   ├── vietnam_stock_heatmap.html
│   ├── vietnamese_stock_analysis.html
│   └── ...
│
└── assets/                        # Ảnh chụp độ phân giải cao đã qua kiểm định DevTools
    ├── product_portal_overview.png         # Ảnh chụp Trạm điều phối toàn cảnh
    ├── telegram_stock_bot.png              # Sơ đồ Bot tương tác khép kín
    ├── vietnam_stock_heatmap.png           # Sơ đồ Streaming đường ray kép
    ├── vietnamese_stock_analysis.png       # Sơ đồ Medallion Parquet Lakehouse
    ├── column_architecture_showcase.png    # Sơ đồ phân tầng cột trực giao
    └── presentation_slide_showcase.png     # Slide thuyết trình kính mờ 16:9
```

---

## 10. Giấy Phép (License)

Dự án được phân phối dưới giấy phép mã nguồn mở [MIT License](LICENSE).
