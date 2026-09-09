"""
diagram-maker: Interactive Loop Topology Compiler
Chuyên trách các hệ thống phân tích định lượng tương tác khép kín 2 chiều (Closed-Loop Bot & Engine):
Telegram Gateway -> Session Dispatcher -> Data & SQLite Cache -> Quant CANSLIM -> Mini Candlestick -> User Feedback.
Hỗ trợ song ngữ (Bilingual: vi/en) chuẩn Institutional Financial Terminal.
"""

from ..core.palette import (
    COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_PURPLE, COLOR_ROSE, COLOR_BLUE,
    TEXT_MAIN, TEXT_MUTED, CARD_BG, SUBCARD_BG, BORDER_BASE
)
from ..core.base import render_html_document
from ..core.mockups import render_mini_candlestick_chart

class InteractiveLoopCompiler:
    def __init__(self, spec):
        self.spec = spec
        self.width = spec.get("width", 1320)
        self.height = spec.get("height", 915)
        self.is_en = spec.get("locale") == "en" or spec.get("lang") == "en"

    def compile(self):
        title = self.spec.get("title", "Closed-Loop Interactive Pipeline Architecture")
        eyebrow = self.spec.get("eyebrow", "EVENT-DRIVEN CLOSED-LOOP PIPELINE · QUANTITATIVE BOT ENGINE")
        metrics = self.spec.get("metrics", [])
        footer_notes = self.spec.get("footer_notes", [])

        body = []

        # Column Titles at Top
        col1 = "1. USER INTERACTION &amp; INGRESS GATEWAY" if self.is_en else "1. GIAO TIẾP NGƯỜI DÙNG &amp; CỔNG BẢO MẬT"
        col2 = "2. COMMAND DISPATCHER &amp; CACHE ENGINE" if self.is_en else "2. ĐIỀU PHỐI LỆNH &amp; ĐỘNG CƠ DỮ LIỆU ĐỆM"
        col3 = "3. QUANT ENGINE &amp; CANDLESTICK RENDERER" if self.is_en else "3. LÕI ĐỊNH LƯỢNG &amp; TRÌNH XUẤT ĐỒ THỊ"

        body.append(f'<text x="45" y="36" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">{col1}</text>')
        body.append(f'<text x="410" y="36" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">{col2}</text>')
        body.append(f'<text x="850" y="36" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">{col3}</text>')

        # CONNECTIONS
        # 1. Line: User Client -> Ingress Gateway
        body.append(f'<path d="M 165 275 L 165 338" stroke="{COLOR_CYAN}" stroke-width="2" marker-end="url(#arrow-cyan)" />')
        # 2. Line: Ingress Gateway -> Rate Limiter
        body.append(f'<path d="M 165 520 L 165 588" stroke="{COLOR_CYAN}" stroke-width="2" marker-end="url(#arrow-cyan)" />')
        # 3. Line: Rate Limiter -> Command Dispatcher (Wide Smooth Bezier through Corridor 1)
        body.append(f'<path d="M 295 680 C 375 680, 345 190, 402 190" fill="none" stroke="{COLOR_PURPLE}" stroke-width="2" marker-end="url(#arrow-purple)" />')
        # 4. Line: Command Dispatcher -> Data Engine
        body.append(f'<path d="M 575 305 L 575 363" stroke="{COLOR_PURPLE}" stroke-width="2" marker-end="url(#arrow-purple)" />')
        # 5. Line: Data Engine -> Strategy Engine (Wide Smooth Bezier through Corridor 2)
        body.append(f'<path d="M 740 480 C 815 480, 790 215, 842 215" fill="none" stroke="{COLOR_AMBER}" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrow-amber)" />')
        # 6. Line: Strategy Engine -> Visual Chart Renderer
        body.append(f'<path d="M 1070 345 L 1070 403" stroke="{COLOR_EMERALD}" stroke-width="2" marker-end="url(#arrow-emerald)" />')
        # 7. CLOSED-LOOP FEEDBACK HIGHWAY: From Renderer back to User!
        body.append(f'<path d="M 850 780 C 790 780, 770 850, 680 850 L 50 850 C 26 850, 16 820, 16 750 L 16 230 C 16 175, 26 175, 38 175" fill="none" stroke="{COLOR_BLUE}" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrow-blue)" />')

        # CONNECTOR PILL BADGES
        p1 = "1. COMMAND /c, /top" if self.is_en else "1. GỬI LỆNH /c, /top"
        p2 = "2. RATE LIMIT TOKEN"
        p3 = "3. DISPATCH" if self.is_en else "3. CHUYỂN TIẾP"
        p4 = "4. QUERY DATA" if self.is_en else "4. TRUY VẤN DỮ LIỆU"
        p5 = "5. LOAD OHLCV CANDLES" if self.is_en else "5. NẠP NẾN OHLCV"
        p6 = "6. SIGNALS &amp; INDICATORS" if self.is_en else "6. TÍN HIỆU &amp; CHỈ BÁO"
        p7 = "7. RETURN CANDLESTICK CHART (SEND PHOTO) TO USER" if self.is_en else "7. PHẢN HỒI KẾT QUẢ &amp; ẢNH ĐỒ THỊ NẾN (SEND PHOTO) TỚI USER"

        body.append(f"""
          <!-- Pill 1: beside Line 1 -->
          <g transform="translate(178, 296)">
            <rect x="0" y="0" width="108" height="20" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="54" y="14" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{p1}</text>
          </g>

          <!-- Pill 2: beside Line 2 -->
          <g transform="translate(178, 545)">
            <rect x="0" y="0" width="110" height="20" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="55" y="14" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{p2}</text>
          </g>

          <!-- Pill 3: In Corridor 1 at Y=425 -->
          <g transform="translate(302, 425)">
            <rect x="0" y="0" width="100" height="22" rx="4" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
            <text x="50" y="15" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{p3}</text>
          </g>

          <!-- Pill 4: beside Line 4 in gap -->
          <g transform="translate(585, 325)">
            <rect x="0" y="0" width="126" height="20" rx="4" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
            <text x="63" y="14" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{p4}</text>
          </g>

          <!-- Pill 5: In Corridor 2 at Y=315 -->
          <g transform="translate(746, 315)">
            <rect x="0" y="0" width="115" height="22" rx="4" fill="#451a03" stroke="#d97706" stroke-width="1" />
            <text x="57" y="15" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{p5}</text>
          </g>

          <!-- Pill 6: beside Line 6 in gap -->
          <g transform="translate(1082, 365)">
            <rect x="0" y="0" width="128" height="20" rx="4" fill="#064e3b" stroke="#059669" stroke-width="1" />
            <text x="64" y="14" fill="#34d399" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{p6}</text>
          </g>

          <!-- Pill 7: on Feedback Rail in bottom corridor -->
          <g transform="translate(220, 839)">
            <rect x="0" y="0" width="410" height="22" rx="4" fill="#1e1b4b" stroke="#4338ca" stroke-width="1" />
            <circle cx="12" cy="11" r="3.5" fill="#38bdf8" />
            <text x="26" y="15" fill="#a5b4fc" font-family="var(--font-mono)" font-size="9.5" font-weight="700">{p7}</text>
          </g>
        """)

        # CARDS
        body.append(self._render_zone1())
        body.append(self._render_zone2())
        body.append(self._render_zone3())

        svg_content = "\n".join(body)
        return render_html_document(title, eyebrow, metrics, svg_content, footer_notes, self.width, self.height)

    def _render_zone1(self):
        if self.is_en:
            c1_t = "Telegram User &amp; Client App"
            c1_1 = 'Query stock candle: <tspan fill="' + COLOR_CYAN + '" font-family="var(--font-mono)">/c FPT, /c VHM</tspan>'
            c1_2 = 'Scan CANSLIM breakouts: <tspan fill="' + COLOR_AMBER + '" font-family="var(--font-mono)">/top</tspan>'
            c1_3 = 'Configure price alerts: <tspan fill="' + COLOR_PURPLE + '" font-family="var(--font-mono)">/alert</tspan>'
            c1_4 = "Receive instant chart analysis"
            c1_b = "TELEGRAM BOT API V20+ ASYNC"

            c2_b = "INGRESS GATEWAY"
            c2_t = "Ingress Gateway &amp; Token Auth"
            c2_1 = "Async Webhook / Parallel Polling"
            c2_2 = "Command Parameter Tokenizer"
            c2_3 = "Validate BOT_TOKEN environment var"
            c2_bot = "INGRESS DECODING LATENCY &lt; 5MS"

            c3_b = "SECURITY &amp; ANTI-SPAM"
            c3_t = "Command Rate Limiter"
            c3_1 = "Token Bucket algorithm per User ID"
            c3_2 = "Safe threshold: Max 5 queries / min"
            c3_3 = "Anti-spam DDoS &amp; pool defense"
            c3_bot = "TOKEN BUCKET DEFENSE LEAKY"
        else:
            c1_t = "Người Dùng &amp; App Telegram"
            c1_1 = 'Gửi lệnh tra cứu: <tspan fill="' + COLOR_CYAN + '" font-family="var(--font-mono)">/c FPT, /c VHM</tspan>'
            c1_2 = 'Quét bùng nổ CANSLIM: <tspan fill="' + COLOR_AMBER + '" font-family="var(--font-mono)">/top</tspan>'
            c1_3 = 'Cài cảnh báo chủ động: <tspan fill="' + COLOR_PURPLE + '" font-family="var(--font-mono)">/alert</tspan>'
            c1_4 = "Nhận ảnh phân tích nến tức thì"
            c1_b = "TELEGRAM BOT API V20+ ASYNC"

            c2_b = "INGRESS GATEWAY"
            c2_t = "Cổng Tiếp Nhận &amp; Token Auth"
            c2_1 = "Webhook Async / Polling song song"
            c2_2 = "Bộ tách tham số lệnh (Tokenizer)"
            c2_3 = "Xác thực BOT_TOKEN biến môi trường"
            c2_bot = "THỜI GIAN GIẢI MÃ INGRESS &lt; 5MS"

            c3_b = "SECURITY &amp; ANTI-SPAM"
            c3_t = "Bộ Điều Tiết Tần Suất Lệnh"
            c3_1 = "Thuật toán Token Bucket per User ID"
            c3_2 = "Ngưỡng an toàn: Tối đa 5 lệnh / phút"
            c3_3 = "Chống spam làm cạn kết nối mạng"
            c3_bot = "TOKEN BUCKET DEFENSE LEAKY"

        return f"""
        <!-- Zone 1: Card 1 User Client -->
        <g transform="translate(45, 80)">
          <rect width="250" height="195" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect width="250" height="3" rx="1.5" fill="{COLOR_CYAN}" />
          <rect x="14" y="14" width="86" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="57" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">USER CLIENT</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="13.5" font-weight="700">{c1_t}</text>
          <text x="14" y="78" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10" font-weight="700">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_1}</text>
          <text x="14" y="100" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10" font-weight="700">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_2}</text>
          <text x="14" y="122" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10" font-weight="700">3.</text>
          <text x="28" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_3}</text>
          <text x="14" y="144" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10" font-weight="700">4.</text>
          <text x="28" y="144" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_4}</text>
          <rect x="14" y="165" width="222" height="18" rx="3" fill="#082f49" />
          <text x="125" y="177.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c1_b}</text>
        </g>

        <!-- Zone 1: Card 2 Ingress Gateway -->
        <g transform="translate(45, 345)">
          <rect width="250" height="175" rx="8" fill="{CARD_BG}" stroke="{BORDER_BASE}" stroke-width="1.2" />
          <rect x="14" y="14" width="112" height="18" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1" />
          <text x="70" y="26.5" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{c2_b}</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="13.5" font-weight="700">{c2_t}</text>
          <text x="14" y="78" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_1}</text>
          <text x="14" y="100" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_2}</text>
          <text x="14" y="122" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="28" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_3}</text>
          <rect x="14" y="145" width="222" height="18" rx="3" fill="#111827" />
          <text x="125" y="157.5" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c2_bot}</text>
        </g>

        <!-- Zone 1: Card 3 Rate Limiter -->
        <g transform="translate(45, 595)">
          <rect width="250" height="175" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.2" />
          <rect x="14" y="14" width="130" height="18" rx="3" fill="#451a03" stroke="#b45309" stroke-width="1" />
          <text x="79" y="26.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{c3_b}</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="13.5" font-weight="700">{c3_t}</text>
          <text x="14" y="78" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_1}</text>
          <text x="14" y="100" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_2}</text>
          <text x="14" y="122" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="28" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_3}</text>
          <rect x="14" y="145" width="222" height="18" rx="3" fill="#451a03" />
          <text x="125" y="157.5" fill="#fcd34d" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c3_bot}</text>
        </g>
        """

    def _render_zone2(self):
        if self.is_en:
            c4_t = "Command Dispatcher &amp; Session State"
            sb1_t, sb1_d = "/c COMMAND", "Candle Lookup"
            sb2_t, sb2_d = "/top COMMAND", "CANSLIM Screener"
            sb3_t, sb3_d = "/alert COMMAND", "Price Alerts"
            c4_l1 = "Route tasks to Data Engine or Quant Screener"
            c4_l2 = "Manage per-user Session Context states"
            c4_l3 = "Non-blocking asyncio.create_task task queue"

            c5_t = "Data Adapter &amp; Dual SQLite Cache"
            c5_sub1_1 = "Fetch real-time OHLCV candles via REST API"
            c5_sub1_2 = "Auto-rotate Headers &amp; User-Agent (Bypass WAF)"
            c5_sub1_3 = "Exponential Backoff retry mechanism"
            c5_sub1_4 = "Standardize candles: Open, High, Low, Close, Vol"

            c5_sub2_1 = '<tspan fill="#34d399" font-family="var(--font-mono)">stock_ohlcv table:</tspan> Store 100 recent sessions'
            c5_sub2_2 = '<tspan fill="#34d399" font-family="var(--font-mono)">user_watchlist table:</tspan> Store tracked portfolios'
            c5_sub2_3 = '<tspan fill="#34d399" font-family="var(--font-mono)">TTL policy:</tspan> 15m in-session, 24h off-session'
            c5_sub2_4 = 'Reduces external API traffic by <tspan fill="' + COLOR_EMERALD + '" font-weight="700">&gt; 80%</tspan>'
            c5_sub2_5 = "WAL concurrency mode: non-blocking read/write"
        else:
            c4_t = "Lõi Điều Phối Lệnh &amp; Quản Lý Phiên"
            sb1_t, sb1_d = "LỆNH /c", "Tra cứu nến"
            sb2_t, sb2_d = "LỆNH /top", "Lọc CANSLIM"
            sb3_t, sb3_d = "LỆNH /alert", "Cảnh báo giá"
            c4_l1 = "Định tuyến tác vụ tới Động cơ Dữ liệu hoặc Bộ lọc"
            c4_l2 = "Quản lý ngữ cảnh Session Context từng người dùng"
            c4_l3 = "Hàng đợi asyncio.create_task không nghẽn luồng chính"

            c5_t = "Động Cơ Dữ Liệu &amp; Đệm Kép SQLite"
            c5_sub1_1 = "Kéo nến OHLCV thời gian thực qua REST API"
            c5_sub1_2 = "Tự động xoay Header &amp; User-Agent (Bypass WAF)"
            c5_sub1_3 = "Cơ chế tự động Retry với Exponential Backoff"
            c5_sub1_4 = "Chuẩn hóa dữ liệu nến: Open, High, Low, Close, Vol"

            c5_sub2_1 = '<tspan fill="#34d399" font-family="var(--font-mono)">Bảng stock_ohlcv:</tspan> Lưu trữ nến 100 phiên gần nhất'
            c5_sub2_2 = '<tspan fill="#34d399" font-family="var(--font-mono)">Bảng user_watchlist:</tspan> Lưu danh mục theo dõi'
            c5_sub2_3 = '<tspan fill="#34d399" font-family="var(--font-mono)">Cơ chế TTL:</tspan> 15p trong phiên, 24h ngoài phiên'
            c5_sub2_4 = 'Cắt giảm hơn <tspan fill="' + COLOR_EMERALD + '" font-weight="700">80%</tspan> lưu lượng gọi API ngoài'
            c5_sub2_5 = "Chế độ ghi WAL đọc/ghi đồng thời không khóa"

        return f"""
        <!-- Zone 2: Card 4 Dispatcher -->
        <g transform="translate(410, 80)">
          <rect width="330" height="225" rx="8" fill="{CARD_BG}" stroke="{COLOR_PURPLE}" stroke-width="1.5" />
          <rect x="16" y="14" width="144" height="18" rx="3" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
          <text x="88" y="26.5" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">COMMAND DISPATCHER</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">{c4_t}</text>

          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="92" height="32" rx="4" fill="#140e2b" stroke="#3b206e" stroke-width="1" />
            <text x="46" y="14" fill="#c084fc" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{sb1_t}</text>
            <text x="46" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">{sb1_d}</text>

            <rect x="102" y="0" width="92" height="32" rx="4" fill="#140e2b" stroke="#3b206e" stroke-width="1" />
            <text x="148" y="14" fill="#c084fc" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{sb2_t}</text>
            <text x="148" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">{sb2_d}</text>

            <rect x="204" y="0" width="92" height="32" rx="4" fill="#140e2b" stroke="#3b206e" stroke-width="1" />
            <text x="250" y="14" fill="#c084fc" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{sb3_t}</text>
            <text x="250" y="26" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">{sb3_d}</text>
          </g>

          <text x="16" y="126" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="126" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c4_l1}</text>
          <text x="16" y="148" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="148" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c4_l2}</text>
          <text x="16" y="170" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="170" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c4_l3}</text>

          <rect x="16" y="193" width="298" height="18" rx="3" fill="#2e1065" />
          <text x="165" y="205.5" fill="#e9d5ff" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">ASYNCIO EVENT LOOP &middot; NON-BLOCKING ROUTER</text>
        </g>

        <!-- Zone 2: Card 5 Data Engine -->
        <g transform="translate(410, 365)">
          <rect width="330" height="405" rx="8" fill="{CARD_BG}" stroke="{BORDER_BASE}" stroke-width="1.2" />
          <rect x="16" y="14" width="148" height="18" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1" />
          <text x="90" y="26.5" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">DATA ADAPTER &amp; CACHE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14.5" font-weight="700">{c5_t}</text>

          <!-- Subcard 1 -->
          <g transform="translate(16, 68)">
            <rect width="298" height="120" rx="6" fill="{SUBCARD_BG}" stroke="{BORDER_BASE}" stroke-width="1" />
            <rect x="10" y="10" width="136" height="16" rx="3" fill="#082f49" />
            <text x="78" y="21.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">SSI &amp; TCBS DCHART API</text>
            <text x="12" y="44" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="44" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub1_1}</text>
            <text x="12" y="64" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="64" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub1_2}</text>
            <text x="12" y="84" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="84" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub1_3}</text>
            <text x="12" y="104" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="104" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub1_4}</text>
          </g>

          <!-- Subcard 2 -->
          <g transform="translate(16, 202)">
            <rect width="298" height="150" rx="6" fill="{SUBCARD_BG}" stroke="{COLOR_EMERALD}" stroke-width="1" />
            <rect x="10" y="10" width="168" height="16" rx="3" fill="#064e3b" />
            <text x="94" y="21.5" fill="#34d399" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">SQLITE CACHE (data_cache/stock.db)</text>
            <text x="12" y="44" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="44" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub2_1}</text>
            <text x="12" y="66" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="66" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub2_2}</text>
            <text x="12" y="88" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="88" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub2_3}</text>
            <text x="12" y="110" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="110" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub2_4}</text>
            <text x="12" y="132" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
            <text x="24" y="132" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">{c5_sub2_5}</text>
          </g>

          <rect x="16" y="368" width="298" height="18" rx="3" fill="#064e3b" />
          <text x="165" y="380.5" fill="#a7f3d0" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">ZERO DISK OVERHEAD &middot; LOCAL CACHE HIT &gt; 82%</text>
        </g>
        """

    def _render_zone3(self):
        if self.is_en:
            c6_t = "CANSLIM Quant Engine &amp; Signal Filter"
            t1_t, t1_sub, t1_desc = "TREND", "EMA 20/50/200", "Golden Cross"
            t2_t, t2_sub, t2_desc = "MOMENTUM", "RSI (14) &amp; MACD", "Overbought/Sold"
            t3_t, t3_sub, t3_desc = "VOLATILITY", "Bollinger (20,2)", "Squeeze Band"
            t4_t, t4_sub, t4_desc = "VOL BREAKOUT", "Vol &gt; 150% MA20", "Pocket Pivot"

            c6_l1 = "Automated CANSLIM quantitative scoring (100-point scale)"
            c6_l2 = "Early detection of Pocket Pivot in tight base consolidations"
            c6_l3 = 'Actionable signal recommendations: <tspan fill="' + COLOR_EMERALD + '" font-weight="700">BUY</tspan>, <tspan fill="' + COLOR_AMBER + '" font-weight="700">HOLD</tspan>, <tspan fill="' + COLOR_ROSE + '" font-weight="700">SELL</tspan>'
            c6_l4 = "Built-in Backtest module verifying Win Rate and Sharpe Ratio"
            c6_bot = "FULL INDICATOR SCAN &amp; COMPUTATION &lt; 35MS"

            c7_t = "Japanese Candlestick Renderer &amp; Dispatcher"
            c7_l1 = 'Integrated <tspan fill="#34d399" font-family="var(--font-mono)">mplfinance / matplotlib</tspan>: High-fidelity candle rendering'
            c7_l2 = "Text synthesis: Packages CANSLIM advice, Stop-loss and Target"
            c7_l3 = 'Direct image dispatch via Telegram: <tspan fill="' + COLOR_CYAN + '" font-family="var(--font-mono)">bot.send_photo(chat_id, photo)</tspan>'
            c7_l4 = "Closed-loop bidirectional interaction cycle under 1 second"
            c7_bot = "RENDER &amp; RETURN CANDLESTICK CHART TO USER IN &lt; 120MS"
        else:
            c6_t = "Lõi Định Lượng &amp; Bộ Lọc Tín Hiệu CANSLIM"
            t1_t, t1_sub, t1_desc = "XU HƯỚNG", "EMA 20/50/200", "Golden Cross"
            t2_t, t2_sub, t2_desc = "ĐỘNG LƯỢNG", "RSI (14) &amp; MACD", "Quá Mua / Bán"
            t3_t, t3_sub, t3_desc = "BIÊN ĐỘ", "Bollinger (20,2)", "Nút Cổ Chai"
            t4_t, t4_sub, t4_desc = "BÙNG NỔ VOL", "Vol &gt; 150% MA20", "Pocket Pivot"

            c6_l1 = "Chấm điểm kỹ thuật tự động theo chuẩn CANSLIM (Thang 100)"
            c6_l2 = "Phát hiện sớm điểm mua Pocket Pivot trong nền giá tích lũy chặt"
            c6_l3 = 'Tín hiệu khuyến nghị chuẩn xác: <tspan fill="' + COLOR_EMERALD + '" font-weight="700">MUA</tspan>, <tspan fill="' + COLOR_AMBER + '" font-weight="700">GIỮ</tspan>, <tspan fill="' + COLOR_ROSE + '" font-weight="700">BÁN</tspan>'
            c6_l4 = "Tích hợp mô-đun Backtest kiểm tra tỷ lệ Win Rate và Sharpe Ratio"
            c6_bot = "THỜI GIAN QUÉT VÀ TÍNH TOÁN TOÀN BỘ CHỈ BÁO &lt; 35MS"

            c7_t = "Trình Vẽ Biểu Đồ Nến Nhật &amp; Đóng Gói Phản Hồi"
            c7_l1 = 'Tích hợp thư viện <tspan fill="#34d399" font-family="var(--font-mono)">mplfinance / matplotlib</tspan>: Sinh ảnh nến chất lượng cao'
            c7_l2 = "Bộ ghép văn bản: Đóng gói khuyến nghị CANSLIM, Stop-loss và Target"
            c7_l3 = 'Gửi ảnh trực tiếp qua Telegram: <tspan fill="' + COLOR_CYAN + '" font-family="var(--font-mono)">bot.send_photo(chat_id, photo)</tspan>'
            c7_l4 = "Khép kín toàn bộ chu trình tương tác hai chiều trong thời gian dưới 1 giây"
            c7_bot = "RENDER &amp; TRẢ ẢNH ĐỒ THỊ NẾN CHO USER TRONG &lt; 120MS"

        return f"""
        <!-- Zone 3: Card 6 Strategy Engine -->
        <g transform="translate(850, 80)">
          <rect width="430" height="265" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.5" />
          <rect x="16" y="14" width="142" height="18" rx="3" fill="#451a03" stroke="#b45309" stroke-width="1" />
          <text x="87" y="26.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">STRATEGY ENGINE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">{c6_t}</text>

          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="94" height="48" rx="4" fill="#181206" stroke="#451a03" stroke-width="1" />
            <text x="47" y="16" fill="#fbbf24" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{t1_t}</text>
            <text x="47" y="32" fill="{TEXT_MAIN}" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{t1_sub}</text>
            <text x="47" y="42" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{t1_desc}</text>

            <rect x="101" y="0" width="94" height="48" rx="4" fill="#181206" stroke="#451a03" stroke-width="1" />
            <text x="148" y="16" fill="#fbbf24" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{t2_t}</text>
            <text x="148" y="32" fill="{TEXT_MAIN}" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{t2_sub}</text>
            <text x="148" y="42" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{t2_desc}</text>

            <rect x="202" y="0" width="94" height="48" rx="4" fill="#181206" stroke="#451a03" stroke-width="1" />
            <text x="249" y="16" fill="#fbbf24" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{t3_t}</text>
            <text x="249" y="32" fill="{TEXT_MAIN}" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{t3_sub}</text>
            <text x="249" y="42" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{t3_desc}</text>

            <rect x="303" y="0" width="95" height="48" rx="4" fill="#181206" stroke="#451a03" stroke-width="1" />
            <text x="350" y="16" fill="#fbbf24" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{t4_t}</text>
            <text x="350" y="32" fill="#34d399" font-family="var(--font-mono)" font-size="9.5" font-weight="700" text-anchor="middle">{t4_sub}</text>
            <text x="350" y="42" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8" text-anchor="middle">{t4_desc}</text>
          </g>

          <text x="16" y="142" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="142" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c6_l1}</text>
          <text x="16" y="164" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="164" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c6_l2}</text>
          <text x="16" y="186" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="186" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c6_l3}</text>
          <text x="16" y="208" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="208" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c6_l4}</text>

          <rect x="16" y="228" width="398" height="18" rx="3" fill="#451a03" />
          <text x="215" y="240.5" fill="#fcd34d" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c6_bot}</text>
        </g>

        <!-- Zone 3: Card 7 Candlestick Renderer -->
        <g transform="translate(850, 410)">
          <rect width="430" height="415" rx="8" fill="{CARD_BG}" stroke="{COLOR_EMERALD}" stroke-width="1.5" />
          <rect x="16" y="14" width="162" height="18" rx="3" fill="#064e3b" stroke="#059669" stroke-width="1" />
          <text x="97" y="26.5" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">VISUAL CANDLESTICK RENDERER</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">{c7_t}</text>

          <!-- Mini Candlestick Mockup -->
          {render_mini_candlestick_chart(16, 68, 398, 180, "FPT", "91.50 (+4.2%)", is_en=self.is_en)}

          <text x="16" y="270" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="270" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c7_l1}</text>
          <text x="16" y="294" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="294" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c7_l2}</text>
          <text x="16" y="318" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="318" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c7_l3}</text>
          <text x="16" y="342" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="10">&bull;</text>
          <text x="28" y="342" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c7_l4}</text>

          <rect x="16" y="378" width="398" height="18" rx="3" fill="#064e3b" />
          <text x="215" y="390.5" fill="#a7f3d0" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c7_bot}</text>
        </g>
        """
