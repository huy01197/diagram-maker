"""
diagram-maker: Streaming Topology Compiler
Chuyên trách các hệ thống Streaming thời gian thực tốc độ cao (< 16ms),
hội tụ Fan-In bất đối xứng và cơ chế truyền tải đường ray kép (Dual-Rail: WebSocket + REST Failover).
"""

from ..core.palette import (
    COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_PURPLE,
    TEXT_MAIN, TEXT_MUTED, CARD_BG, BORDER_BASE
)
from ..core.base import render_html_document
from ..core.mockups import render_mini_treemap

class StreamingTopologyCompiler:
    def __init__(self, spec):
        self.spec = spec
        self.width = spec.get("width", 1320)
        self.height = spec.get("height", 915)

    def compile(self):
        title = self.spec.get("title", "Streaming Topology Architecture")
        eyebrow = self.spec.get("eyebrow", "STREAMING TOPOLOGY · DUAL-RAIL PIPELINE")
        metrics = self.spec.get("metrics", [])
        footer_notes = self.spec.get("footer_notes", [])

        # Build SVG Body
        body = []

        # Column Titles at Y=32
        body.append(f'<text x="50" y="32" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">1. NGUỒN TIẾP NHẬN &amp; BẢO MẬT</text>')
        body.append(f'<text x="390" y="32" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">2. LÕI HỘI TỤ FAN-IN &amp; BỘ NHỚ RAM O(1)</text>')
        body.append(f'<text x="940" y="32" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="11" font-weight="700" letter-spacing="0.08em">3. TRẠM TRÌNH CHIẾU CLIENT &amp; TRỰC QUAN</text>')

        # CONNECTIONS (Bézier curves)
        # Ingress -> Fan In
        body.append(f'<path d="M 320 185 L 372 185" stroke="{COLOR_CYAN}" stroke-width="2" marker-end="url(#arrow-cyan)" />')
        body.append(f'<path d="M 320 400 C 355 400, 355 240, 372 240" fill="none" stroke="{COLOR_PURPLE}" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#arrow-purple)" />')
        body.append(f'<path d="M 320 625 C 360 625, 360 640, 372 640" fill="none" stroke="{COLOR_AMBER}" stroke-width="2" marker-end="url(#arrow-amber)" />')

        # Core Internal Vertical Connectors
        body.append(f'<path d="M 590 280 L 590 322" stroke="{COLOR_CYAN}" stroke-width="2" marker-end="url(#arrow-cyan)" />')
        body.append(f'<path d="M 590 515 L 590 557" stroke="{COLOR_CYAN}" stroke-width="2" marker-end="url(#arrow-cyan)" />')

        # DUAL-RAIL HIGHWAY
        # Primary Rail (Emerald)
        body.append(f'<path d="M 800 370 C 865 370, 885 105, 932 105" fill="none" stroke="{COLOR_EMERALD}" stroke-width="2.5" marker-end="url(#arrow-emerald)" />')
        # Failover Rail (Amber)
        body.append(f'<path d="M 800 480 C 865 480, 885 710, 932 710" fill="none" stroke="{COLOR_AMBER}" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrow-amber)" />')

        # Internal Right Column Connectors (with generous 65px vertical gaps)
        body.append(f'<path d="M 1120 165 L 1120 222" stroke="{COLOR_EMERALD}" stroke-width="2" marker-end="url(#arrow-emerald)" />')
        body.append(f'<path d="M 1120 500 L 1120 557" stroke="{COLOR_AMBER}" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#arrow-amber)" />')

        # Badges in open spaces (Zero obstruction!)
        body.append(f"""
          <g transform="translate(820, 140)">
            <rect x="0" y="0" width="100" height="22" rx="4" fill="#064e3b" stroke="{COLOR_EMERALD}" stroke-width="1" />
            <circle cx="12" cy="11" r="3.5" fill="#34d399" />
            <text x="24" y="15" fill="#a7f3d0" font-family="var(--font-mono)" font-size="9" font-weight="700">&lt; 16MS LIVE</text>
            <text x="50" y="-6" fill="#34d399" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">PRIMARY STREAM</text>
          </g>
          <g transform="translate(820, 455)">
            <rect x="0" y="0" width="100" height="22" rx="4" fill="#451a03" stroke="{COLOR_AMBER}" stroke-width="1" />
            <circle cx="12" cy="11" r="3.5" fill="#fbbf24" />
            <text x="24" y="15" fill="#fde68a" font-family="var(--font-mono)" font-size="9" font-weight="700">REST 2.5S</text>
            <text x="50" y="-6" fill="#fbbf24" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">FAILOVER POLLING</text>
          </g>
        """)

        # CARDS RENDERING
        # Zone 1 (Left: Ingress)
        body.append(self._render_ingress_cards())
        # Zone 2 (Center: Fan-in Core & RAM Store)
        body.append(self._render_core_cards())
        # Zone 3 (Right: WebSocket Hub & ECharts Canvas)
        body.append(self._render_presentation_cards())

        svg_content = "\n".join(body)
        return render_html_document(title, eyebrow, metrics, svg_content, footer_notes, self.width, self.height)

    def _render_ingress_cards(self):
        return f"""
        <!-- Ingress Card 1: SignalR -->
        <g transform="translate(50, 75)">
          <rect width="270" height="155" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="14" y="14" width="86" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="57" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SIGNALR HUB</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">SSI FastConnect</text>
          <text x="14" y="78" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Lắng nghe kênh X:ALL, MI:ALL</text>
          <text x="14" y="100" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Tần suất &gt; 2.500 tick / giây</text>
          <rect x="14" y="122" width="242" height="18" rx="3" fill="#082f49" />
          <text x="135" y="134.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="9" font-weight="600" text-anchor="middle">STREAMING TICK CHỦ ĐỘNG</text>
        </g>

        <!-- Ingress Card 2: RSA Auth -->
        <g transform="translate(50, 290)">
          <rect width="270" height="165" rx="8" fill="{CARD_BG}" stroke="{COLOR_PURPLE}" stroke-width="1.2" />
          <rect x="14" y="14" width="86" height="18" rx="3" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
          <text x="57" y="26.5" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">BẢO MẬT RSA</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">Khóa Ký Số &amp; JWT</text>
          <text x="14" y="78" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Đọc config.json &amp; PrivateKey</text>
          <text x="14" y="100" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Ký số chuẩn hóa SHA-256</text>
          <text x="14" y="122" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="28" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Tự động cấp &amp; gia hạn Token</text>
          <rect x="14" y="137" width="242" height="16" rx="3" fill="#2e1065" />
        </g>

        <!-- Ingress Card 3: Cold Start -->
        <g transform="translate(50, 520)">
          <rect width="270" height="165" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.2" />
          <rect x="14" y="14" width="86" height="18" rx="3" fill="#451a03" stroke="#b45309" stroke-width="1" />
          <text x="57" y="26.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">KHỞI TẠO 0MS</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">Quét Lùi 10 Ngày</text>
          <text x="14" y="78" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Quét lùi tránh ngày nghỉ lễ</text>
          <text x="14" y="100" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="100" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Tải snapshot giá tham chiếu</text>
          <text x="14" y="122" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="28" y="122" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Dự phòng VNDirect finfo API</text>
          <rect x="14" y="137" width="242" height="16" rx="3" fill="#451a03" />
        </g>
        """

    def _render_core_cards(self):
        return f"""
        <!-- Core Card 1: Fan-in Worker -->
        <g transform="translate(380, 75)">
          <rect width="420" height="195" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="16" y="14" width="102" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="67" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">FAN-IN WORKER</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">Phễu Thu Gom &amp; Giải Mã Tick Tốc Độ Cao</text>
          
          <!-- 3 mini boxes -->
          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="120" height="42" rx="4" fill="#061826" stroke="#0c4a6e" stroke-width="1" />
            <text x="60" y="17" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">GÓI TIN X (KHỚP)</text>
            <text x="60" y="31" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">Giá khớp, Vol, Mua/bán</text>

            <rect x="134" y="0" width="120" height="42" rx="4" fill="#061826" stroke="#0c4a6e" stroke-width="1" />
            <text x="194" y="17" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">GÓI TIN MI (CHỈ SỐ)</text>
            <text x="194" y="31" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">VN-Index, VN30, HNX30</text>

            <rect x="268" y="0" width="120" height="42" rx="4" fill="#061826" stroke="#0c4a6e" stroke-width="1" />
            <text x="328" y="17" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">TÍNH % BIẾN ĐỘNG</text>
            <text x="328" y="31" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">So sánh giá Ref Snapshot</text>
          </g>

          <rect x="16" y="125" width="388" height="20" rx="4" fill="#082f49" />
          <text x="210" y="138.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="9.5" font-weight="600" text-anchor="middle">DECODE REAL-TIME TRONG LUỒNG ASYNC &lt; 0.05MS</text>
        </g>

        <!-- Core Card 2: In-Memory RAM Store -->
        <g transform="translate(380, 325)">
          <rect width="420" height="185" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="16" y="14" width="112" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="72" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">IN-MEMORY STORE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">Kho Dữ Liệu RAM O(1) &amp; Khóa An Toàn Mutex</text>
          
          <text x="16" y="80" fill="#38bdf8" font-family="var(--font-mono)" font-size="10.5" font-weight="700">HASH-MAP O(1):</text>
          <text x="120" y="80" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Quản lý tức thời trạng thái hơn 700 mã cổ phiếu 3 sàn</text>

          <text x="16" y="108" fill="#38bdf8" font-family="var(--font-mono)" font-size="10.5" font-weight="700">MUTEX LOCK:</text>
          <text x="105" y="108" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Khóa Thread-safe ngăn chặn race condition giữa nạp và đọc</text>

          <text x="16" y="136" fill="#38bdf8" font-family="var(--font-mono)" font-size="10.5" font-weight="700">ZERO DISK I/O:</text>
          <text x="125" y="136" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">Hoàn toàn không ghi đĩa trong phiên, loại bỏ nghẽn I/O</text>

          <rect x="16" y="152" width="388" height="14" rx="3" fill="#0c4a6e" />
        </g>

        <!-- Core Card 3: Sector Classifier -->
        <g transform="translate(380, 560)">
          <rect width="420" height="205" rx="8" fill="{CARD_BG}" stroke="{BORDER_BASE}" stroke-width="1.2" />
          <rect x="16" y="14" width="102" height="18" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1" />
          <text x="67" y="26.5" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">VS-SECTOR CORE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">Phân Loại 15 Nhóm Ngành &amp; Thước Đo Độ Rộng</text>
          
          <!-- Sector Tag Pills -->
          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="70" height="20" rx="3" fill="#1e293b" /><text x="35" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">Ngân Hàng</text>
            <rect x="76" y="0" width="75" height="20" rx="3" fill="#1e293b" /><text x="113.5" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">Bất Động Sản</text>
            <rect x="157" y="0" width="70" height="20" rx="3" fill="#1e293b" /><text x="192" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">Thép - VLXD</text>
            <rect x="233" y="0" width="75" height="20" rx="3" fill="#1e293b" /><text x="270.5" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">Chứng Khoán</text>
            <rect x="314" y="0" width="74" height="20" rx="3" fill="#1e293b" /><text x="351" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">+11 Ngành Khác</text>
          </g>

          <!-- 5-Color Spectrum Bar -->
          <g transform="translate(16, 96)">
            <rect x="0" y="0" width="74" height="22" rx="3" fill="#7c3aed" /><text x="37" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">TRẦN (+6.9%)</text>
            <rect x="78" y="0" width="74" height="22" rx="3" fill="#059669" /><text x="115" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">TĂNG GIÁ</text>
            <rect x="156" y="0" width="74" height="22" rx="3" fill="#d97706" /><text x="193" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">THAM CHIẾU</text>
            <rect x="234" y="0" width="74" height="22" rx="3" fill="#dc2626" /><text x="271" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">GIẢM GIÁ</text>
            <rect x="312" y="0" width="76" height="22" rx="3" fill="#0284c7" /><text x="350" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">SÀN (-6.9%)</text>
          </g>

          <text x="16" y="142" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
          <text x="28" y="142" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Tính toán tỷ trọng diện tích dựa trên Giá trị giao dịch (Turnover Value)</text>

          <text x="16" y="162" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
          <text x="28" y="162" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Thống kê phân bổ dòng tiền độ rộng thị trường: Số mã Trần/Tăng/TC/Giảm/Sàn</text>

          <text x="16" y="182" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
          <text x="28" y="182" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">Tự động sắp xếp Top ngành thanh khoản cao nhất toàn thị trường</text>
        </g>
        """

    def _render_presentation_cards(self):
        return f"""
        <!-- Presentation Card 1: WebSocket Hub -->
        <g transform="translate(940, 75)">
          <rect width="330" height="90" rx="8" fill="{CARD_BG}" stroke="{COLOR_EMERALD}" stroke-width="1.5" />
          <rect x="14" y="12" width="134" height="16" rx="3" fill="#064e3b" />
          <text x="81" y="23.5" fill="#34d399" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">FASTCONNECT LIVE HUB</text>
          <text x="14" y="44" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="13" font-weight="700">Máy Chủ aiohttp &amp; WebSocket /ws</text>
          <text x="14" y="62" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">1.</text>
          <text x="26" y="62" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Cổng 8050: Tự động giải phóng cổng cũ (1-Click Play)</text>
          <text x="14" y="78" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">2.</text>
          <text x="26" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Đẩy gói tin vi sai delta 60 FPS về toàn bộ client</text>
        </g>

        <!-- Presentation Card 2: ECharts Treemap Canvas (Y: 230 to 500, generous 65px gaps) -->
        <g transform="translate(940, 230)">
          <rect width="330" height="270" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="14" y="12" width="112" height="16" rx="3" fill="#082f49" />
          <text x="70" y="23.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">ECHARTS 5.4 CANVAS</text>
          <text x="14" y="44" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="13.5" font-weight="700">Giao Diện Bản Đồ Nhiệt Toàn Cảnh (Treemap)</text>

          <!-- Embedded Mini Treemap Mockup -->
          {render_mini_treemap(10, 48, 310, 105)}

          <g transform="translate(14, 160)">
            <text x="0" y="16" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="10" y="16" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Hook ZRender Centroid: Căn giữa nhãn cổ phiếu trong ô</text>
            <text x="0" y="34" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="10" y="34" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Tự động ẩn text khi ô &lt; 38px để chống tràn diện tích</text>
            <text x="0" y="52" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="10" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Hiệu ứng Flash Update chớp sáng khi có tick mới (&lt; 16ms)</text>
            <text x="0" y="70" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="10" y="70" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Thước đo độ rộng 3 màu: Trần/Tăng, Tham chiếu, Giảm/Sàn</text>
          </g>
        </g>

        <!-- Presentation Card 3: Polling Fallback (Y: 565 to 695, generous 65px gap) -->
        <g transform="translate(940, 565)">
          <rect width="330" height="130" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.5" />
          <rect x="14" y="12" width="134" height="16" rx="3" fill="#451a03" />
          <text x="81" y="23.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">FAILOVER &amp; INSPECTOR</text>
          <text x="14" y="44" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="13" font-weight="700">Chế Độ Polling Live &amp; Bảng Soi Thông Số</text>
          <text x="14" y="65" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="9.5">1.</text>
          <text x="26" y="65" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Tự chuyển POLLING LIVE (chu kỳ 2.5s) khi đứt mạng</text>
          <text x="14" y="85" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="9.5">2.</text>
          <text x="26" y="85" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="10.5">Drawer phụ: Top 6 ngành hút tiền, độ rộng thị trường</text>
          <rect x="14" y="102" width="302" height="16" rx="3" fill="#451a03" />
          <text x="165" y="113.5" fill="#fde68a" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">TỰ ĐỘNG THỬ KẾT NỐI LẠI (AUTO-RECONNECT) MỖI 3S</text>
        </g>
        """
