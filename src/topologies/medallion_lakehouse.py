"""
diagram-maker: Medallion Lakehouse Topology Compiler
Chuyên trách các hệ sinh thái xử lý dữ liệu lớn, hồ dữ liệu cột Parquet và trạm phân tích định lượng đa tầng:
Bronze (Raw ZIP) -> Silver (Snappy Parquet) -> Gold (Feature Store & Sector Matrix) -> Platinum (Streamlit 4-Pane Terminal).
"""

from ..core.palette import (
    COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_PURPLE, COLOR_BLUE,
    TEXT_MAIN, TEXT_MUTED, CARD_BG, SUBCARD_BG, BORDER_BASE
)
from ..core.base import render_html_document
from ..core.mockups import render_mini_multipane_chart

class MedallionLakehouseCompiler:
    def __init__(self, spec):
        self.spec = spec
        self.width = spec.get("width", 1320)
        self.height = spec.get("height", 915)

    def compile(self):
        title = self.spec.get("title", "Medallion Parquet Lakehouse Architecture")
        eyebrow = self.spec.get("eyebrow", "MEDALLION ARCHITECTURE · COLUMNAR LAKEHOUSE · MULTI-PANE QUANT ENGINE")
        metrics = self.spec.get("metrics", [])
        footer_notes = self.spec.get("footer_notes", [])

        body = []

        # Column Header Titles at Top
        body.append(f'<text x="45" y="36" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">1. TẦNG BRONZE: TIẾP NHẬN THÔ &amp; LỊCH SỬ</text>')
        body.append(f'<text x="400" y="36" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">2. TẦNG SILVER &amp; GOLD: HỒ CỘT PARQUET &amp; ĐỊNH LƯỢNG</text>')
        body.append(f'<text x="830" y="36" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">3. TẦNG PLATINUM: STREAMLIT MULTI-PANE TERMINAL</text>')

        # CONNECTIONS
        # 1. Line: CafeF Scanner -> Unpacker Worker
        body.append(f'<path d="M 175 320 L 175 410" stroke="{COLOR_AMBER}" stroke-width="2" marker-end="url(#arrow-amber)" />')
        # 2. Line: Unpacker Worker -> Silver Parquet Lakehouse
        body.append(f'<path d="M 305 530 C 365 530, 350 200, 392 200" fill="none" stroke="{COLOR_CYAN}" stroke-width="2" marker-end="url(#arrow-cyan)" />')
        # 3. Line: Silver Parquet Lakehouse -> Gold Quant Feature Store
        body.append(f'<path d="M 565 375 L 565 442" stroke="{COLOR_PURPLE}" stroke-width="2" marker-end="url(#arrow-purple)" />')
        # 4. Line: Gold Quant -> Terminal Screener
        body.append(f'<path d="M 730 520 C 785 520, 770 180, 822 180" fill="none" stroke="{COLOR_PURPLE}" stroke-width="2" marker-end="url(#arrow-purple)" />')
        # 5. Line: Silver Lakehouse -> Multi-Pane Candlestick Chart
        body.append(f'<path d="M 730 250 C 785 250, 775 510, 822 510" fill="none" stroke="{COLOR_EMERALD}" stroke-width="2.2" stroke-dasharray="6 3" marker-end="url(#arrow-emerald)" />')

        # CONNECTOR PILL BADGES
        body.append(f"""
          <!-- Pill 1: Between Card 1 and Card 2 -->
          <g transform="translate(188, 355)">
            <rect x="0" y="0" width="102" height="20" rx="4" fill="#451a03" stroke="#b45309" stroke-width="1" />
            <text x="51" y="14" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">GIẢI NÉN ĐA LUỒNG</text>
          </g>

          <!-- Pill 2: In Corridor 1 at Y=415 -->
          <g transform="translate(315, 415)">
            <rect x="0" y="0" width="76" height="22" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="38" y="15" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">PARQUET</text>
          </g>

          <!-- Pill 3: In gap between Silver and Gold -->
          <g transform="translate(578, 398)">
            <rect x="0" y="0" width="128" height="20" rx="4" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
            <text x="64" y="14" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">CHUỖI THỜI GIAN O(1)</text>
          </g>

          <!-- Pill 4: In Corridor 2 at Y=310 -->
          <g transform="translate(742, 310)">
            <rect x="0" y="0" width="76" height="22" rx="4" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
            <text x="38" y="15" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SCREENER</text>
          </g>

          <!-- Pill 5: In Corridor 2 at Y=435 -->
          <g transform="translate(738, 435)">
            <rect x="0" y="0" width="84" height="22" rx="4" fill="#064e3b" stroke="#059669" stroke-width="1" />
            <text x="42" y="15" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SYNC 4 PANES</text>
          </g>
        """)

        # CARDS
        body.append(self._render_bronze_layer())
        body.append(self._render_silver_gold_layer())
        body.append(self._render_platinum_layer())

        svg_content = "\n".join(body)
        return render_html_document(title, eyebrow, metrics, svg_content, footer_notes, self.width, self.height)

    def _render_bronze_layer(self):
        return f"""
        <!-- Card 1: CafeF Ingestion Scanner -->
        <g transform="translate(45, 80)">
          <rect width="260" height="240" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.5" />
          <rect width="260" height="3" rx="1.5" fill="{COLOR_AMBER}" />
          <rect x="14" y="14" width="102" height="18" rx="3" fill="#451a03" stroke="#b45309" stroke-width="1" />
          <text x="65" y="26.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">BRONZE LAYER 01</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">Hồ Dữ Liệu Thô CafeF ZIP</text>
          <text x="14" y="78" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Tải tệp nén hàng ngày: CafeF Upto ZIP</text>
          <text x="14" y="100" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Bao phủ 10+ năm lịch sử toàn thị trường</text>
          <text x="14" y="122" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">3.</text>
          <text x="28" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">1.500+ mã niêm yết: HSX, HNX, UPCoM</text>
          <text x="14" y="144" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">4.</text>
          <text x="28" y="144" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Ghi nhận lịch sử tải vào download_history.json</text>
          <text x="14" y="166" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">5.</text>
          <text x="28" y="166" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Kiểm tra tính toàn vẹn gói tin bằng MD5</text>
          <rect x="14" y="200" width="232" height="18" rx="3" fill="#451a03" />
          <text x="130" y="212.5" fill="#fcd34d" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">RAW STORAGE &gt; 15GB CSV LỊCH SỬ</text>
        </g>

        <!-- Card 2: Unpacker Worker -->
        <g transform="translate(45, 415)">
          <rect width="260" height="355" rx="8" fill="{CARD_BG}" stroke="{BORDER_BASE}" stroke-width="1.2" />
          <rect x="14" y="14" width="112" height="18" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1" />
          <text x="70" y="26.5" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">ETL EXTRACTOR</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">Giải Nén &amp; Làm Sạch Schema</text>
          <text x="14" y="78" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Giải nén ZIP đa luồng song song</text>
          <text x="14" y="100" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Lọc bỏ dòng trống, định dạng sai số</text>
          <text x="14" y="122" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="28" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Chuẩn hóa cột: Ticker, Date, O, H, L, C, V</text>
          <text x="14" y="144" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">4.</text>
          <text x="28" y="144" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Hiệu chỉnh giá chia tách cổ tức &amp; quyền mua</text>
          <text x="14" y="166" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">5.</text>
          <text x="28" y="166" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Khử trùng lặp (Deduplication) theo Ngày/Mã</text>

          <g transform="translate(14, 192)">
            <rect width="232" height="110" rx="6" fill="{SUBCARD_BG}" stroke="{BORDER_BASE}" stroke-width="1" />
            <text x="10" y="20" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9" font-weight="700">DATA CLEANING RULES:</text>
            <text x="10" y="38" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5">&bull; Date format: YYYY-MM-DD</text>
            <text x="10" y="56" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5">&bull; Close &gt; 0, Volume &gt;= 0</text>
            <text x="10" y="74" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5">&bull; High &gt;= Low, High &gt;= Open</text>
            <text x="10" y="92" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="8.5">&bull; Đạt chuẩn toàn vẹn 99.98%</text>
          </g>

          <rect x="14" y="320" width="232" height="18" rx="3" fill="#111827" />
          <text x="130" y="332.5" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">XỬ LÝ 10 TRIỆU BẢN GHI &lt; 4.2 GIÂY</text>
        </g>
        """

    def _render_silver_gold_layer(self):
        return f"""
        <!-- Card 3: Silver Parquet Lakehouse -->
        <g transform="translate(400, 80)">
          <rect width="330" height="295" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="16" y="14" width="106" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="69" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SILVER LAYER 02</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">Hồ Lưu Trữ Cột Apache Parquet</text>

          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="94" height="32" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="47" y="14" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SNAPPY NÉN</text>
            <text x="47" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">-85% Dung Lượng</text>

            <rect x="102" y="0" width="94" height="32" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="149" y="14" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">LƯU TRỮ CỘT</text>
            <text x="149" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">Tốc Độ Đọc 10x</text>

            <rect x="204" y="0" width="94" height="32" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="251" y="14" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">MMAP ACCESS</text>
            <text x="251" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">Không Tải Hết RAM</text>
          </g>

          <text x="16" y="126" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="126" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Phân vùng lưu trữ Parquet theo Ticker / Niên độ</text>
          <text x="16" y="148" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="148" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Tích hợp DuckDB / PyArrow: Truy vấn cột siêu tốc</text>
          <text x="16" y="170" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="170" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Độ trễ truy vấn lọc dữ liệu lịch sử &lt; 250ms</text>
          <text x="16" y="192" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="192" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Loại bỏ hoàn toàn nghẽn cổ chai I/O tệp CSV lớn</text>
          <text x="16" y="214" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="214" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Hỗ trợ cập nhật nạp nối thêm (Append-only daily sync)</text>

          <rect x="16" y="248" width="298" height="18" rx="3" fill="#082f49" />
          <text x="165" y="260.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">TRUY VẤN CỘT 1.500+ MÃ CỔ PHIẾU TRONG &lt; 250MS</text>
        </g>

        <!-- Card 4: Gold Feature Store -->
        <g transform="translate(400, 445)">
          <rect width="330" height="325" rx="8" fill="{CARD_BG}" stroke="{COLOR_PURPLE}" stroke-width="1.5" />
          <rect x="16" y="14" width="102" height="18" rx="3" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
          <text x="67" y="26.5" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">GOLD LAYER 03</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">Lõi Định Lượng &amp; Độ Rộng Thị Trường</text>

          <g transform="translate(16, 68)">
            <rect width="298" height="98" rx="6" fill="{SUBCARD_BG}" stroke="{BORDER_BASE}" stroke-width="1" />
            <text x="10" y="20" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700">TÍNH TOÁN CHỈ BÁO KỸ THUẬT ĐỒNG THỜI:</text>
            <text x="10" y="38" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; <tspan fill="{COLOR_CYAN}" font-family="var(--font-mono)">Xu Hướng:</tspan> SMA 20, 50, 200, EMA 10, 20</text>
            <text x="10" y="56" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; <tspan fill="{COLOR_AMBER}" font-family="var(--font-mono)">Động Lượng:</tspan> RSI(14), MACD(12,26,9) Histogram</text>
            <text x="10" y="74" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; <tspan fill="{COLOR_EMERALD}" font-family="var(--font-mono)">Biến Động &amp; Khối Lượng:</tspan> Bollinger Bands, ATR, VWAP</text>
            <text x="10" y="90" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9">Tối ưu hóa vector hóa (Vectorized NumPy / Pandas)</text>
          </g>

          <g transform="translate(16, 178)">
            <rect width="298" height="98" rx="6" fill="{SUBCARD_BG}" stroke="{COLOR_PURPLE}" stroke-width="1" />
            <text x="10" y="20" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700">MA TRẬN ĐỘ RỘNG DÒNG TIỀN 15 NGÀNH:</text>
            <text x="10" y="38" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; Phân bổ tỷ trọng dòng tiền (Turnover Weight)</text>
            <text x="10" y="56" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; Tỷ lệ mã Tăng / Giảm / Vượt đỉnh 52 tuần</text>
            <text x="10" y="74" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; Tự động phát hiện ngành dẫn sóng thị trường</text>
            <text x="10" y="90" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="9">Cập nhật động theo phiên giao dịch</text>
          </g>

          <rect x="16" y="288" width="298" height="18" rx="3" fill="#2e1065" />
          <text x="165" y="300.5" fill="#e9d5ff" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">FEATURE STORE SẴN SÀNG CHO MÔ HÌNH QUANT</text>
        </g>
        """

    def _render_platinum_layer(self):
        return f"""
        <!-- Card 5: Streamlit Financial Terminal -->
        <g transform="translate(830, 80)">
          <rect width="450" height="235" rx="8" fill="{CARD_BG}" stroke="{COLOR_BLUE}" stroke-width="1.5" />
          <rect x="16" y="14" width="128" height="18" rx="3" fill="#1e1b4b" stroke="#4338ca" stroke-width="1" />
          <text x="80" y="26.5" fill="#818cf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">PLATINUM LAYER 04</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">Streamlit Financial Terminal &amp; Screener</text>

          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="100" height="32" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="50" y="14" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">BỘ LỌC MÃ</text>
            <text x="50" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">1.500+ CP Niêm Yết</text>

            <rect x="108" y="0" width="100" height="32" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="158" y="14" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">LỌC KỸ THUẬT</text>
            <text x="158" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">Golden Cross, RSI</text>

            <rect x="216" y="0" width="100" height="32" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="266" y="14" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">XUẤT DỮ LIỆU</text>
            <text x="266" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">Excel / CSV / Parquet</text>

            <rect x="324" y="0" width="94" height="32" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="371" y="14" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">DARK THEME</text>
            <text x="371" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">Bloomberg Chuẩn</text>
          </g>

          <text x="16" y="126" fill="{COLOR_BLUE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="126" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Tra cứu cổ phiếu theo thời gian thực kết hợp bộ nhớ đệm Streamlit Cache</text>
          <text x="16" y="148" fill="{COLOR_BLUE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="148" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Bảng soi Top thanh khoản, Top tăng/giảm và dòng tiền theo ngành</text>
          <text x="16" y="170" fill="{COLOR_BLUE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="170" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Tùy biến tham số chỉ báo kỹ thuật linh hoạt ngay trên giao diện web</text>

          <rect x="16" y="198" width="418" height="18" rx="3" fill="#1e1b4b" />
          <text x="225" y="210.5" fill="#c7d2fe" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">STREAMLIT ASYNC DASHBOARD &middot; ĐỘ TRỄ TƯƠNG TÁC &lt; 150MS</text>
        </g>

        <!-- Card 6: Multi-Pane Chart Canvas -->
        <g transform="translate(830, 345)">
          <rect width="450" height="425" rx="8" fill="{CARD_BG}" stroke="{COLOR_EMERALD}" stroke-width="1.5" />
          <rect x="16" y="14" width="162" height="18" rx="3" fill="#064e3b" stroke="#059669" stroke-width="1" />
          <text x="97" y="26.5" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">PLOTLY MULTI-PANE ENGINE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">Đồ Thị Kỹ Thuật Đa Tầng 4 Panes Đồng Bộ</text>

          <!-- 4-Pane Mini Chart Mockup -->
          {render_mini_multipane_chart(16, 68, 418, 235, "VCB", "96.80 (+3.2%)")}

          <text x="16" y="325" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="325" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Đồng bộ trục thời gian X giữa 4 Panes đồ thị khi phóng to (Zoom) / Cuộn (Pan)</text>
          <text x="16" y="347" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="347" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Hiển thị Tooltip đa thông số chi tiết khi rê chuột (Hover Inspector)</text>
          <text x="16" y="369" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="369" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Render mượt mà 2.000+ phiên nến lịch sử bằng Plotly WebGL Engine</text>

          <rect x="16" y="392" width="418" height="18" rx="3" fill="#064e3b" />
          <text x="225" y="404.5" fill="#a7f3d0" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">PLOTLY WEBGL RENDER 4 PANES ĐỒNG BỘ TRONG &lt; 90MS</text>
        </g>
        """
