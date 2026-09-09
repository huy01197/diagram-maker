"""
diagram-maker: Medallion Lakehouse Topology Compiler
Chuyên trách các hệ sinh thái xử lý dữ liệu lớn, hồ dữ liệu cột Parquet và trạm phân tích định lượng đa tầng:
Bronze (Raw ZIP) -> Silver (Snappy Parquet) -> Gold (Feature Store & Sector Matrix) -> Platinum (Streamlit 4-Pane Terminal).
Hỗ trợ song ngữ (Bilingual: vi/en) chuẩn Institutional Financial Terminal.
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
        self.width = spec.get("width", 1440)
        self.height = spec.get("height", 920)
        self.is_en = spec.get("locale") == "en" or spec.get("lang") == "en"

    def compile(self):
        title = self.spec.get("title", "Vietnamese Stock Analysis - Medallion Lakehouse")
        eyebrow = self.spec.get("eyebrow", "MEDALLION LAKEHOUSE · QUANT ENGINE")
        metrics = self.spec.get("metrics", [])
        footer_notes = self.spec.get("footer_notes", [])

        body = []

        # Column Header Titles at Top
        col1 = "1. BRONZE TIER: RAW INGESTION &amp; HISTORY" if self.is_en else "1. TẦNG BRONZE: TIẾP NHẬN THÔ &amp; LỊCH SỬ"
        col2 = "2. SILVER &amp; GOLD TIER: PARQUET LAKEHOUSE &amp; QUANT" if self.is_en else "2. TẦNG SILVER &amp; GOLD: HỒ CỘT PARQUET &amp; ĐỊNH LƯỢNG"
        col3 = "3. PLATINUM TIER: STREAMLIT MULTI-PANE TERMINAL" if self.is_en else "3. TẦNG PLATINUM: STREAMLIT MULTI-PANE TERMINAL"

        body.append(f'<text x="45" y="36" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">{col1}</text>')
        body.append(f'<text x="435" y="36" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">{col2}</text>')
        body.append(f'<text x="930" y="36" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">{col3}</text>')

        # STEP 1: RENDER CARDS FIRST (Substrate layer)
        body.append(self._render_bronze_layer())
        body.append(self._render_silver_gold_layer())
        body.append(self._render_platinum_layer())

        # STEP 2: RENDER CONNECTIONS (Circuit traces - Orthogonal Manhattan with Rounded Corners matching user sample)
        # Line 1: Card 1 -> Card 2 (Vertical straight down at X=200)
        body.append(f'<path d="M 200 325 L 200 423" stroke="{COLOR_AMBER}" stroke-width="2" marker-end="url(#arrow-amber)" />')

        # Line 2: Card 2 -> Card 3 (Orthogonal Manhattan turn North into Corridor 1 bus X=395)
        body.append(f'<path d="M 355 515 H 387 Q 395 515, 395 507 V 203 Q 395 195, 403 195 H 433" fill="none" stroke="{COLOR_CYAN}" stroke-width="2" marker-end="url(#arrow-cyan)" />')

        # Line 3: Card 3 -> Card 4 (Vertical straight down at X=640)
        body.append(f'<path d="M 640 375 L 640 443" stroke="{COLOR_PURPLE}" stroke-width="2" marker-end="url(#arrow-purple)" />')

        # Line 4: Card 4 -> Card 5 (Orthogonal Manhattan turn North into Corridor 2 Track A X=875)
        body.append(f'<path d="M 845 530 H 867 Q 875 530, 875 522 V 183 Q 875 175, 883 175 H 928" fill="none" stroke="{COLOR_PURPLE}" stroke-width="2" marker-end="url(#arrow-purple)" />')

        # Line 5: Card 3 -> Card 6 (DASHED Orthogonal Manhattan turn South into Corridor 2 Track B X=900, matching dashed sample)
        body.append(f'<path d="M 845 235 H 892 Q 900 235, 900 243 V 492 Q 900 500, 908 500 H 928" fill="none" stroke="{COLOR_EMERALD}" stroke-width="2.2" stroke-dasharray="6 4" marker-end="url(#arrow-emerald)" />')

        # STEP 3: RENDER PILL BADGES ON TOP (Transceiver chips mounted directly on wires)
        p1 = "PARALLEL UNPACK" if self.is_en else "GIẢI NÉN ĐA LUỒNG"
        p3 = "O(1) TIME SERIES" if self.is_en else "CHUỖI THỜI GIAN O(1)"

        body.append(f"""
          <!-- Pill 1: Centered on Line 1 (X=200, Y=374) -->
          <g transform="translate(142, 363)">
            <rect x="0" y="0" width="116" height="22" rx="4" fill="#451a03" stroke="#b45309" stroke-width="1" />
            <text x="58" y="15" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{p1}</text>
          </g>

          <!-- Pill 2: Mounted on Corridor 1 Bus (X=395, Y=355) -->
          <g transform="translate(357, 344)">
            <rect x="0" y="0" width="76" height="22" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="38" y="15" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">PARQUET</text>
          </g>

          <!-- Pill 3: Centered on Line 3 (X=640, Y=410) -->
          <g transform="translate(575, 399)">
            <rect x="0" y="0" width="130" height="22" rx="4" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
            <text x="65" y="15" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{p3}</text>
          </g>

          <!-- Pill 4: Mounted on Track A Bus (X=875, Y=355) -->
          <g transform="translate(837, 344)">
            <rect x="0" y="0" width="76" height="22" rx="4" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
            <text x="38" y="15" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SCREENER</text>
          </g>

          <!-- Pill 5: Mounted on Track B Dashed Bus (X=900, Y=430) -->
          <g transform="translate(854, 419)">
            <rect x="0" y="0" width="92" height="22" rx="4" fill="#064e3b" stroke="#059669" stroke-width="1" />
            <text x="46" y="15" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SYNC 4 PANES</text>
          </g>
        """)

        svg_content = "\n".join(body)
        return render_html_document(title, eyebrow, metrics, svg_content, footer_notes, self.width, self.height)

    def _render_bronze_layer(self):
        if self.is_en:
            c1_t = "Raw Data Lake CafeF ZIP"
            c1_1 = "Daily batch archive: CafeF Upto ZIP"
            c1_2 = "Covers 10+ years of historical market ticks"
            c1_3 = "1,500+ listed tickers: HSX, HNX, UPCoM"
            c1_4_label = "Log download history into:"
            c1_4_file = "download_history.json"
            c1_5 = "MD5 checksum packet verification"
            c1_bot = "RAW STORAGE &gt; 15GB CSV ARCHIVE"

            c2_t = "Unpack &amp; Schema Normalization"
            c2_1 = "Multi-threaded parallel ZIP extraction"
            c2_2 = "Strip empty rows &amp; numeric anomalies"
            c2_3 = "Standardize columns: Ticker, Date, O, H, L, C, V"
            c2_4 = "Adjust for splits, cash/stock dividends"
            c2_5 = "Deduplicate records by Date / Ticker"
            c2_rule = "Integrity score 99.98%"
            c2_bot = "PROCESS 10M ROWS IN &lt; 4.2 SECONDS"
        else:
            c1_t = "Hồ Dữ Liệu Thô CafeF ZIP"
            c1_1 = "Tải tệp nén hàng ngày: CafeF Upto ZIP"
            c1_2 = "Bao phủ 10+ năm lịch sử toàn thị trường"
            c1_3 = "1.500+ mã niêm yết: HSX, HNX, UPCoM"
            c1_4_label = "Ghi nhận nhật ký tải vào:"
            c1_4_file = "download_history.json"
            c1_5 = "Kiểm tra tính toàn vẹn gói tin bằng MD5"
            c1_bot = "RAW STORAGE &gt; 15GB CSV LỊCH SỬ"

            c2_t = "Giải Nén &amp; Làm Sạch Schema"
            c2_1 = "Giải nén ZIP đa luồng song song"
            c2_2 = "Lọc bỏ dòng trống, định dạng sai số"
            c2_3 = "Chuẩn hóa cột: Ticker, Date, O, H, L, C, V"
            c2_4 = "Hiệu chỉnh giá chia tách cổ tức &amp; quyền mua"
            c2_5 = "Khử trùng lặp (Deduplication) theo Ngày/Mã"
            c2_rule = "Đạt chuẩn toàn vẹn 99.98%"
            c2_bot = "XỬ LÝ 10 TRIỆU BẢN GHI &lt; 4.2 GIÂY"

        return f"""
        <!-- Card 1: CafeF Ingestion Scanner -->
        <g transform="translate(45, 75)">
          <rect width="310" height="250" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.5" />
          <rect width="310" height="3" rx="1.5" fill="{COLOR_AMBER}" />
          <rect x="16" y="14" width="106" height="18" rx="3" fill="#451a03" stroke="#b45309" stroke-width="1" />
          <text x="69" y="26.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">BRONZE LAYER 01</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c1_t}</text>
          
          <text x="16" y="78" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">1.</text>
          <text x="30" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_1}</text>
          
          <text x="16" y="100" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">2.</text>
          <text x="30" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_2}</text>
          
          <text x="16" y="122" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">3.</text>
          <text x="30" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_3}</text>
          
          <text x="16" y="144" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">4.</text>
          <text x="30" y="144" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_4_label}</text>
          <rect x="30" y="150" width="144" height="16" rx="3" fill="#1e293b" stroke="#334155" stroke-width="0.8" />
          <text x="102" y="161.5" fill="#fcd34d" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c1_4_file}</text>
          
          <text x="16" y="186" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10" font-weight="700">5.</text>
          <text x="30" y="186" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_5}</text>
          
          <rect x="16" y="214" width="278" height="20" rx="3" fill="#451a03" />
          <text x="155" y="227.5" fill="#fcd34d" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c1_bot}</text>
        </g>

        <!-- Card 2: Unpacker Worker -->
        <g transform="translate(45, 425)">
          <rect width="310" height="370" rx="8" fill="{CARD_BG}" stroke="{BORDER_BASE}" stroke-width="1.2" />
          <rect x="16" y="14" width="116" height="18" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1" />
          <text x="74" y="26.5" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">ETL EXTRACTOR</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c2_t}</text>
          
          <text x="16" y="78" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="30" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_1}</text>
          
          <text x="16" y="100" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="30" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_2}</text>
          
          <text x="16" y="122" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="30" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_3}</text>
          
          <text x="16" y="144" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">4.</text>
          <text x="30" y="144" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_4}</text>
          
          <text x="16" y="166" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">5.</text>
          <text x="30" y="166" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_5}</text>

          <g transform="translate(16, 192)">
            <rect width="278" height="118" rx="6" fill="{SUBCARD_BG}" stroke="{BORDER_BASE}" stroke-width="1" />
            <text x="12" y="22" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9" font-weight="700">DATA CLEANING RULES:</text>
            <text x="12" y="42" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5">&bull; Date format: YYYY-MM-DD</text>
            <text x="12" y="62" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5">&bull; Close &gt; 0, Volume &gt;= 0</text>
            <text x="12" y="82" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5">&bull; High &gt;= Low, High &gt;= Open</text>
            <text x="12" y="102" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="8.5">&bull; {c2_rule}</text>
          </g>

          <rect x="16" y="332" width="278" height="20" rx="3" fill="#111827" />
          <text x="155" y="345.5" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c2_bot}</text>
        </g>
        """

    def _render_silver_gold_layer(self):
        if self.is_en:
            c3_t = "Apache Parquet Columnar Lake"
            sb1_t, sb1_d = "SNAPPY COMPRESS", "-85% Disk Size"
            sb2_t, sb2_d = "COLUMN STORE", "10x Read Speed"
            sb3_t, sb3_d = "MMAP ACCESS", "Zero RAM Bloat"
            c3_l1 = "Partition Parquet lake by Ticker / Calendar Year"
            c3_l2 = "Integrated DuckDB / PyArrow: Sub-second columnar querying"
            c3_l3 = "Historical query filter latency &lt; 250ms"
            c3_l4 = "Eliminates disk I/O bottlenecks of legacy CSV files"
            c3_l5 = "Supports Append-only daily synchronization"
            c3_bot = "QUERY 1,500+ TICKERS IN &lt; 250MS"

            c4_t = "Quant Feature Store &amp; Market Breadth"
            sec1_hdr = "PARALLEL TECHNICAL INDICATOR COMPUTATION:"
            sec1_l1 = '<tspan fill="' + COLOR_CYAN + '" font-family="var(--font-mono)">Trend:</tspan> SMA 20, 50, 200, EMA 10, 20'
            sec1_l2 = '<tspan fill="' + COLOR_AMBER + '" font-family="var(--font-mono)">Momentum:</tspan> RSI(14), MACD(12,26,9) Histogram'
            sec1_l3 = '<tspan fill="' + COLOR_EMERALD + '" font-family="var(--font-mono)">Volatility &amp; Vol:</tspan> Bollinger Bands, ATR, VWAP'
            sec1_sub = "Vectorized NumPy / Pandas acceleration"

            sec2_hdr = "15-SECTOR CAPITAL FLOW BREADTH MATRIX:"
            sec2_l1 = "Turnover Weight capital flow distribution"
            sec2_l2 = "Ratio of Advancing / Declining / 52-Week Highs"
            sec2_l3 = "Auto-detection of leading market wave sectors"
            sec2_sub = "Dynamically updated per trading session"
            c4_bot = "FEATURE STORE READY FOR QUANT MODELS"
        else:
            c3_t = "Hồ Lưu Trữ Cột Apache Parquet"
            sb1_t, sb1_d = "SNAPPY NÉN", "-85% Dung Lượng"
            sb2_t, sb2_d = "LƯU TRỮ CỘT", "Tốc Độ Đọc 10x"
            sb3_t, sb3_d = "MMAP ACCESS", "Không Tải Hết RAM"
            c3_l1 = "Phân vùng lưu trữ Parquet theo Ticker / Niên độ"
            c3_l2 = "Tích hợp DuckDB / PyArrow: Truy vấn cột siêu tốc"
            c3_l3 = "Độ trễ truy vấn lọc dữ liệu lịch sử &lt; 250ms"
            c3_l4 = "Loại bỏ hoàn toàn nghẽn cổ chai I/O tệp CSV lớn"
            c3_l5 = "Hỗ trợ cập nhật nạp nối thêm (Append-only daily sync)"
            c3_bot = "TRUY VẤN CỘT 1.500+ MÃ CỔ PHIẾU TRONG &lt; 250MS"

            c4_t = "Lõi Định Lượng &amp; Độ Rộng Thị Trường"
            sec1_hdr = "TÍNH TOÁN CHỈ BÁO KỸ THUẬT ĐỒNG THỜI:"
            sec1_l1 = '<tspan fill="' + COLOR_CYAN + '" font-family="var(--font-mono)">Xu Hướng:</tspan> SMA 20, 50, 200, EMA 10, 20'
            sec1_l2 = '<tspan fill="' + COLOR_AMBER + '" font-family="var(--font-mono)">Động Lượng:</tspan> RSI(14), MACD(12,26,9) Histogram'
            sec1_l3 = '<tspan fill="' + COLOR_EMERALD + '" font-family="var(--font-mono)">Biến Động &amp; Khối Lượng:</tspan> Bollinger Bands, ATR, VWAP'
            sec1_sub = "Tối ưu hóa vector hóa (Vectorized NumPy / Pandas)"

            sec2_hdr = "MA TRẬN ĐỘ RỘNG DÒNG TIỀN 15 NGÀNH:"
            sec2_l1 = "Phân bổ tỷ trọng dòng tiền (Turnover Weight)"
            sec2_l2 = "Tỷ lệ mã Tăng / Giảm / Vượt đỉnh 52 tuần"
            sec2_l3 = "Tự động phát hiện ngành dẫn sóng thị trường"
            sec2_sub = "Cập nhật động theo phiên giao dịch"
            c4_bot = "FEATURE STORE SẴN SÀNG CHO MÔ HÌNH QUANT"

        return f"""
        <!-- Card 3: Silver Parquet Lakehouse -->
        <g transform="translate(435, 75)">
          <rect width="410" height="300" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="16" y="14" width="112" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="72" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SILVER LAYER 02</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">{c3_t}</text>

          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="118" height="34" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="59" y="15" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{sb1_t}</text>
            <text x="59" y="28" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{sb1_d}</text>

            <rect x="130" y="0" width="118" height="34" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="189" y="15" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{sb2_t}</text>
            <text x="189" y="28" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{sb2_d}</text>

            <rect x="260" y="0" width="118" height="34" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="319" y="15" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{sb3_t}</text>
            <text x="319" y="28" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{sb3_d}</text>
          </g>

          <text x="16" y="128" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="128" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l1}</text>
          <text x="16" y="150" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="150" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l2}</text>
          <text x="16" y="172" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="172" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l3}</text>
          <text x="16" y="194" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="194" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l4}</text>
          <text x="16" y="216" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="216" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l5}</text>

          <rect x="16" y="252" width="378" height="20" rx="3" fill="#082f49" />
          <text x="205" y="265.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c3_bot}</text>
        </g>

        <!-- Card 4: Gold Feature Store -->
        <g transform="translate(435, 445)">
          <rect width="410" height="350" rx="8" fill="{CARD_BG}" stroke="{COLOR_PURPLE}" stroke-width="1.5" />
          <rect x="16" y="14" width="108" height="18" rx="3" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
          <text x="70" y="26.5" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">GOLD LAYER 03</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">{c4_t}</text>

          <g transform="translate(16, 68)">
            <rect width="378" height="106" rx="6" fill="{SUBCARD_BG}" stroke="{BORDER_BASE}" stroke-width="1" />
            <text x="12" y="22" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700">{sec1_hdr}</text>
            <text x="12" y="42" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; {sec1_l1}</text>
            <text x="12" y="62" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; {sec1_l2}</text>
            <text x="12" y="82" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; {sec1_l3}</text>
            <text x="12" y="98" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9">{sec1_sub}</text>
          </g>

          <g transform="translate(16, 186)">
            <rect width="378" height="106" rx="6" fill="{SUBCARD_BG}" stroke="{COLOR_PURPLE}" stroke-width="1" />
            <text x="12" y="22" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700">{sec2_hdr}</text>
            <text x="12" y="42" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; {sec2_l1}</text>
            <text x="12" y="62" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; {sec2_l2}</text>
            <text x="12" y="82" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">&bull; {sec2_l3}</text>
            <text x="12" y="98" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="9">{sec2_sub}</text>
          </g>

          <rect x="16" y="308" width="378" height="20" rx="3" fill="#2e1065" />
          <text x="205" y="321.5" fill="#e9d5ff" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c4_bot}</text>
        </g>
        """

    def _render_platinum_layer(self):
        if self.is_en:
            c5_t = "Streamlit Financial Terminal &amp; Screener"
            sb1_t, sb1_d = "TICKER FILTER", "1,500+ Tickers"
            sb2_t, sb2_d = "TECH SCREENER", "Golden Cross, RSI"
            sb3_t, sb3_d = "DATA EXPORT", "Excel/CSV/Parquet"
            sb4_t, sb4_d = "DARK THEME", "Bloomberg Standard"
            c5_l1 = "Real-time stock lookup combined with persistent Streamlit Cache"
            c5_l2 = "Inspector: Top turnover, Top gainers/losers, sector capital flows"
            c5_l3 = "Dynamic technical indicator parameter tweaking directly on UI"
            c5_bot = "STREAMLIT ASYNC DASHBOARD &middot; INTERACTION LATENCY &lt; 150MS"

            c6_t = "Synchronized 4-Pane Technical Chart Canvas"
            c6_l1 = "Synchronized X time-axis across all 4 chart panes during Zoom / Pan"
            c6_l2 = "Comprehensive multi-parameter tooltips upon mouse hover (Hover Inspector)"
            c6_l3 = "Ultra-smooth rendering of 2,000+ historical candles via Plotly WebGL"
            c6_bot = "PLOTLY WEBGL 4-PANE SYNCED RENDERING IN &lt; 90MS"
        else:
            c5_t = "Streamlit Financial Terminal &amp; Screener"
            sb1_t, sb1_d = "BỘ LỌC MÃ", "1.500+ CP Niêm Yết"
            sb2_t, sb2_d = "LỌC KỸ THUẬT", "Golden Cross, RSI"
            sb3_t, sb3_d = "XUẤT DỮ LIỆU", "Excel / CSV / Parquet"
            sb4_t, sb4_d = "DARK THEME", "Bloomberg Chuẩn"
            c5_l1 = "Tra cứu cổ phiếu theo thời gian thực kết hợp bộ nhớ đệm Streamlit Cache"
            c5_l2 = "Bảng soi Top thanh khoản, Top tăng/giảm và dòng tiền theo ngành"
            c5_l3 = "Tùy biến tham số chỉ báo kỹ thuật linh hoạt ngay trên giao diện web"
            c5_bot = "STREAMLIT ASYNC DASHBOARD &middot; ĐỘ TRỄ TƯƠNG TÁC &lt; 150MS"

            c6_t = "Đồ Thị Kỹ Thuật Đa Tầng 4 Panes Đồng Bộ"
            c6_l1 = "Đồng bộ trục thời gian X giữa 4 Panes đồ thị khi phóng to (Zoom) / Cuộn (Pan)"
            c6_l2 = "Hiển thị Tooltip đa thông số chi tiết khi rê chuột (Hover Inspector)"
            c6_l3 = "Render mượt mà 2.000+ phiên nến lịch sử bằng Plotly WebGL Engine"
            c6_bot = "PLOTLY WEBGL RENDER 4 PANES ĐỒNG BỘ TRONG &lt; 90MS"

        return f"""
        <!-- Card 5: Streamlit Financial Terminal -->
        <g transform="translate(930, 75)">
          <rect width="465" height="245" rx="8" fill="{CARD_BG}" stroke="{COLOR_BLUE}" stroke-width="1.5" />
          <rect x="16" y="14" width="134" height="18" rx="3" fill="#1e1b4b" stroke="#4338ca" stroke-width="1" />
          <text x="83" y="26.5" fill="#818cf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">PLATINUM LAYER 04</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">{c5_t}</text>

          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="102" height="34" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="51" y="15" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{sb1_t}</text>
            <text x="51" y="28" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{sb1_d}</text>

            <rect x="111" y="0" width="102" height="34" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="162" y="15" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{sb2_t}</text>
            <text x="162" y="28" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{sb2_d}</text>

            <rect x="222" y="0" width="102" height="34" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="273" y="15" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{sb3_t}</text>
            <text x="273" y="28" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{sb3_d}</text>

            <rect x="333" y="0" width="100" height="34" rx="4" fill="#0d1424" stroke="#1b253b" stroke-width="1" />
            <text x="383" y="15" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{sb4_t}</text>
            <text x="383" y="28" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{sb4_d}</text>
          </g>

          <text x="16" y="130" fill="{COLOR_BLUE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="130" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c5_l1}</text>
          <text x="16" y="152" fill="{COLOR_BLUE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="152" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c5_l2}</text>
          <text x="16" y="174" fill="{COLOR_BLUE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="174" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c5_l3}</text>

          <rect x="16" y="206" width="433" height="20" rx="3" fill="#1e1b4b" />
          <text x="232" y="219.5" fill="#c7d2fe" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c5_bot}</text>
        </g>

        <!-- Card 6: Multi-Pane Chart Canvas -->
        <g transform="translate(930, 350)">
          <rect width="465" height="445" rx="8" fill="{CARD_BG}" stroke="{COLOR_EMERALD}" stroke-width="1.5" />
          <rect x="16" y="14" width="168" height="18" rx="3" fill="#064e3b" stroke="#059669" stroke-width="1" />
          <text x="100" y="26.5" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">PLOTLY MULTI-PANE ENGINE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">{c6_t}</text>

          <!-- 4-Pane Mini Chart Mockup (width=433 inside 465 card) -->
          {render_mini_multipane_chart(16, 68, 433, 235, "VCB", "96.80 (+3.2%)", is_en=self.is_en)}

          <text x="16" y="332" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="332" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c6_l1}</text>
          <text x="16" y="354" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="354" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c6_l2}</text>
          <text x="16" y="376" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="376" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c6_l3}</text>

          <rect x="16" y="406" width="433" height="20" rx="3" fill="#064e3b" />
          <text x="232" y="419.5" fill="#a7f3d0" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c6_bot}</text>
        </g>
        """
