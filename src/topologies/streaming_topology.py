"""
diagram-maker: Streaming Topology Compiler
Chuyên trách các hệ thống Streaming thời gian thực tốc độ cao (< 16ms),
hội tụ Fan-In bất đối xứng và cơ chế truyền tải đường ray kép (Dual-Rail: WebSocket + REST Failover).
Hỗ trợ song ngữ (Bilingual: vi/en) chuẩn Institutional Financial Terminal.
"""

from ..core.palette import (
    COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_PURPLE,
    TEXT_MAIN, TEXT_MUTED, CARD_BG, BORDER_BASE
)
from ..core.base import render_html_document, render_port_junction
from ..core.mockups import render_mini_treemap

class StreamingTopologyCompiler:
    def __init__(self, spec):
        self.spec = spec
        self.width = spec.get("width", 1440)
        self.height = spec.get("height", 810)
        self.is_en = spec.get("locale") == "en" or spec.get("lang") == "en"

    def compile(self):
        title = self.spec.get("title", "Streaming Topology Architecture")
        eyebrow = self.spec.get("eyebrow", "STREAMING TOPOLOGY · DUAL-RAIL PIPELINE")
        metrics = self.spec.get("metrics", [])
        footer_notes = self.spec.get("footer_notes", [])

        # Build SVG Body
        body = []

        # ----------------------------------------------------
        # 1. CARDS RENDERING (SUBSTRATE LAYER)
        # ----------------------------------------------------
        # Zone 1 (Left: Ingress)
        body.append(self._render_ingress_cards())
        # Zone 2 (Center: Fan-in Core & RAM Store)
        body.append(self._render_core_cards())
        # Zone 3 (Right: WebSocket Hub & ECharts Canvas)
        body.append(self._render_presentation_cards())

        # ----------------------------------------------------
        # 2. CONNECTIONS & HIGHWAY ARROWS (CIRCUIT LAYER)
        # ----------------------------------------------------
        body.append(self._render_connections())

        # ----------------------------------------------------
        # 3. CONNECTOR PILL BADGES (CALLOUT LAYER)
        # ----------------------------------------------------
        body.append(self._render_badges())

        svg_content = "\n".join(body)
        return render_html_document(title, eyebrow, metrics, svg_content, footer_notes, self.width, self.height)

    def _render_connections(self):
        body = []
        # 1. RSA Auth -> SSI FastConnect (Upward token flow within Col 1)
        body.append(f'<path d="M 180 255 L 180 203" stroke="{COLOR_PURPLE}" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#arrow-purple)" />')

        # 2. SSI FastConnect -> Fan-In Worker (Direct horizontal streaming feed at Y=115)
        body.append(f'<path d="M 315 115 L 408 115" stroke="{COLOR_CYAN}" stroke-width="2.5" marker-end="url(#arrow-cyan)" />')

        # 3. Quét Lùi 10 Ngày -> RAM Store (Orthogonal bus in Corridor 1 at X=362.5)
        body.append(f'<path d="M 315 595 L 354.5 595 Q 362.5 595 362.5 587 L 362.5 398 Q 362.5 390 370.5 390 L 408 390" fill="none" stroke="{COLOR_AMBER}" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrow-amber)" />')

        # 4. Col 2 Internal: Fan-In Worker -> RAM Store O(1) (Vertical straight down at X=620)
        body.append(f'<path d="M 620 245 L 620 283" stroke="{COLOR_CYAN}" stroke-width="2.5" marker-end="url(#arrow-cyan)" />')

        # 5. Col 2 Internal: RAM Store O(1) -> VS-Sector Classification (Vertical straight down at X=620)
        body.append(f'<path d="M 620 495 L 620 533" stroke="{COLOR_CYAN}" stroke-width="2.5" marker-end="url(#arrow-cyan)" />')

        # Corridor 2: Virtual Port Coupling (Decoupled Port A/B Pattern from Blueprint media_1788978341773.jpg)
        # Port (A): WebSocket Live Stream (< 16ms Live) RAM Store O(1) -> FastConnect Live Hub
        body.append(f'<path d="M 898 95 L 938 95" stroke="{COLOR_EMERALD}" stroke-width="2.5" marker-end="url(#arrow-emerald)" />')
        body.append(render_port_junction(885, 95, "A", "LIVE WS /ws" if self.is_en else "CỔNG /ws", COLOR_EMERALD, is_source=False, text_pos="top"))
        body.append(f'<path d="M 830 350 L 872 350" stroke="{COLOR_EMERALD}" stroke-width="2" />')
        body.append(render_port_junction(885, 350, "A", "WS STREAM" if self.is_en else "LUỒNG WS", COLOR_EMERALD, is_source=True, text_pos="top"))

        # Port (B): Failover Polling & REST State Snapshot (2.5s Cycle) RAM Store O(1) -> Polling Fallback
        body.append(f'<path d="M 830 440 L 872 440" stroke="{COLOR_AMBER}" stroke-width="2" />')
        body.append(render_port_junction(885, 440, "B", "REST SNAPSHOT" if self.is_en else "BỘ NHỚ REST", COLOR_AMBER, is_source=True, text_pos="bottom"))
        body.append(f'<path d="M 898 635 L 938 635" stroke="{COLOR_AMBER}" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrow-amber)" />')
        body.append(render_port_junction(885, 635, "B", "REST POLLING" if self.is_en else "DỰ PHÒNG REST", COLOR_AMBER, is_source=False, text_pos="bottom"))

        # 7. Live Hub -> ECharts Treemap Canvas (Direct downward 60 FPS delta broadcast)
        body.append(f'<path d="M 1167 155 L 1167 193" stroke="{COLOR_EMERALD}" stroke-width="2.5" marker-end="url(#arrow-emerald)" />')

        # 9. Market Breadth Feed: VS-Sector -> Polling Fallback & Inspector (Direct horizontal at Y=690)
        body.append(f'<path d="M 830 690 L 938 690" stroke="#64748b" stroke-width="1.8" stroke-dasharray="3 3" marker-end="url(#arrow-cyan)" />')
        return "\n".join(body)

    def _render_badges(self):
        body = []
        # Badge 1: Token Auth (on Line 1 at X=180, Y=229)
        b_auth = "JWT AUTH" if self.is_en else "TOKEN JWT"
        body.append(f"""
          <g transform="translate(138, 220)">
            <rect x="0" y="0" width="84" height="18" rx="3" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
            <text x="42" y="12.5" fill="#d8b4fe" font-family="var(--font-mono)" font-size="8" font-weight="700" text-anchor="middle">{b_auth}</text>
          </g>
        """)

        # Badge 2: Ingress Stream (on Line 2 at Y=115, centered in Corridor 1 at X=362.5)
        b_stream = "STREAM TICK" if self.is_en else "LUỒNG TICK"
        body.append(f"""
          <g transform="translate(324, 106)">
            <rect x="0" y="0" width="77" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="38.5" y="12.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="8" font-weight="700" text-anchor="middle">{b_stream}</text>
          </g>
        """)

        # Badge 3: Snapshot Ref Price (on Line 3 bus at X=362.5, Y=495)
        b_snap = "REF PRICE" if self.is_en else "GIÁ THAM CHIẾU"
        body.append(f"""
          <g transform="translate(320.5, 486)">
            <rect x="0" y="0" width="84" height="18" rx="3" fill="#451a03" stroke="#b45309" stroke-width="1" />
            <text x="42" y="12.5" fill="#fde68a" font-family="var(--font-mono)" font-size="7.5" font-weight="700" text-anchor="middle">{b_snap}</text>
          </g>
        """)

        # Badge 4: Delta Ticks Decode (on Line 4 at X=620, Y=264)
        b_delta = "DELTA TICKS" if self.is_en else "GÓI TIN DELTA"
        body.append(f"""
          <g transform="translate(577, 255)">
            <rect x="0" y="0" width="86" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="43" y="12.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="7.5" font-weight="700" text-anchor="middle">{b_delta}</text>
          </g>
        """)

        # Badge 5: Sector Matrix (on Line 5 at X=620, Y=514)
        b_sec = "SECTOR MAP" if self.is_en else "MA TRẬN NGÀNH"
        body.append(f"""
          <g transform="translate(573, 505)">
            <rect x="0" y="0" width="94" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
            <text x="47" y="12.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="7.5" font-weight="700" text-anchor="middle">{b_sec}</text>
          </g>
        """)

        # Badge 7: 60 FPS Delta Broadcast (on Line 7 at X=1167, Y=174)
        b_broadcast = "60 FPS BROADCAST" if self.is_en else "ĐẨY 60 FPS DELTA"
        body.append(f"""
          <g transform="translate(1112, 165)">
            <rect x="0" y="0" width="110" height="18" rx="3" fill="#064e3b" stroke="{COLOR_EMERALD}" stroke-width="1" />
            <text x="55" y="12.5" fill="#a7f3d0" font-family="var(--font-mono)" font-size="8" font-weight="700" text-anchor="middle">{b_broadcast}</text>
          </g>
        """)

        # Badge 9: Market Breadth Feed (on Line 9 at Y=690, centered at X=885)
        b_breadth = "BREADTH FEED" if self.is_en else "ĐỘ RỘNG TT"
        body.append(f"""
          <g transform="translate(837, 681)">
            <rect x="0" y="0" width="96" height="18" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1" />
            <text x="48" y="12.5" fill="#94a3b8" font-family="var(--font-mono)" font-size="7.5" font-weight="700" text-anchor="middle">{b_breadth}</text>
          </g>
        """)
        return "\n".join(body)

    def _render_ingress_cards(self):
        if self.is_en:
            c1_t = "SSI FastConnect"
            c1_1 = "Listen to X:ALL, MI:ALL channels"
            c1_2 = "Throughput &gt; 2,500 ticks / second"
            c1_b = "ACTIVE STREAMING INGRESS"

            c2_b = "RSA SECURITY"
            c2_t = "Digital Signature &amp; JWT"
            c2_1 = "Load config.json &amp; PrivateKey"
            c2_2 = "Standardized SHA-256 signing"
            c2_3 = "Auto token minting &amp; rotation"

            c3_b = "0MS COLD START"
            c3_t = "10-Day Historical Backfill"
            c3_1 = "Lookback skips holidays/weekends"
            c3_2 = "Load reference price snapshot"
            c3_3 = "Failover VNDirect finfo API"
        else:
            c1_t = "SSI FastConnect"
            c1_1 = "Lắng nghe kênh X:ALL, MI:ALL"
            c1_2 = "Tần suất &gt; 2.500 tick / giây"
            c1_b = "STREAMING TICK CHỦ ĐỘNG"

            c2_b = "BẢO MẬT RSA"
            c2_t = "Khóa Ký Số &amp; JWT"
            c2_1 = "Đọc config.json &amp; PrivateKey"
            c2_2 = "Ký số chuẩn hóa SHA-256"
            c2_3 = "Tự động cấp &amp; gia hạn Token"

            c3_b = "KHỞI TẠO 0MS"
            c3_t = "Quét Lùi 10 Ngày"
            c3_1 = "Quét lùi tránh ngày nghỉ lễ"
            c3_2 = "Tải snapshot giá tham chiếu"
            c3_3 = "Dự phòng VNDirect finfo API"

        return f"""
        <!-- Ingress Card 1: SignalR -->
        <g transform="translate(45, 35)">
          <rect width="270" height="165" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="14" y="14" width="86" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="57" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">SIGNALR HUB</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c1_t}</text>
          <text x="14" y="78" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c1_1}</text>
          <text x="14" y="102" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="102" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c1_2}</text>
          <rect x="14" y="128" width="242" height="20" rx="3" fill="#082f49" />
          <text x="135" y="141.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="9" font-weight="600" text-anchor="middle">{c1_b}</text>
        </g>

        <!-- Ingress Card 2: RSA Auth -->
        <g transform="translate(45, 255)">
          <rect width="270" height="185" rx="8" fill="{CARD_BG}" stroke="{COLOR_PURPLE}" stroke-width="1.2" />
          <rect x="14" y="14" width="86" height="18" rx="3" fill="#2e1065" stroke="#7c3aed" stroke-width="1" />
          <text x="57" y="26.5" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{c2_b}</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c2_t}</text>
          <text x="14" y="78" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c2_1}</text>
          <text x="14" y="102" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="102" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c2_2}</text>
          <text x="14" y="126" fill="{COLOR_PURPLE}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="28" y="126" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c2_3}</text>
          <rect x="14" y="150" width="242" height="20" rx="3" fill="#2e1065" />
          <text x="135" y="163" fill="#d8b4fe" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">ASYNC RE-AUTH THREAD</text>
        </g>

        <!-- Ingress Card 3: Cold Start -->
        <g transform="translate(45, 505)">
          <rect width="270" height="185" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.2" />
          <rect x="14" y="14" width="86" height="18" rx="3" fill="#451a03" stroke="#b45309" stroke-width="1" />
          <text x="57" y="26.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{c3_b}</text>
          <text x="14" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c3_t}</text>
          <text x="14" y="78" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">1.</text>
          <text x="28" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c3_1}</text>
          <text x="14" y="102" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">2.</text>
          <text x="28" y="102" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c3_2}</text>
          <text x="14" y="126" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="10">3.</text>
          <text x="28" y="126" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11.5">{c3_3}</text>
          <rect x="14" y="150" width="242" height="20" rx="3" fill="#451a03" />
          <text x="135" y="163" fill="#fde68a" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">SNAPSHOT CACHE MD5</text>
        </g>
        """

    def _render_core_cards(self):
        if self.is_en:
            c1_t = "High-Speed Ingestion &amp; Tick Decoder"
            b1_title = "PACKET X (MATCH)"
            b1_sub = "Match price, Vol, Side"
            b2_title = "PACKET MI (INDEX)"
            b2_sub = "VN-Index, VN30, HNX30"
            b3_title = "% CHANGE CALC"
            b3_sub = "Compare vs Ref Snapshot"
            c1_b = "REAL-TIME ASYNC DECODING IN THREAD &lt; 0.05MS"

            c2_t = "O(1) RAM Data Store &amp; Mutex Safety"
            c2_l1 = "Fast state for 700+ tickers across 3 exchanges"
            c2_l2 = "Thread-safe mutex lock prevents race conditions"
            c2_l3 = "No session disk writes to eliminate I/O lag"
            c2_b = "SUB-MILLISECOND IN-MEMORY LATENCY &lt; 0.12MS"

            c3_t = "15-Sector Classification &amp; Breadth Matrix"
            sec1, sec2, sec3, sec4, sec5 = "Banking", "Real Estate", "Steel &amp; Mat.", "Securities", "+11 Sectors"
            ce, ga, rf, lo, fl = "CEILING (+6.9%)", "GAIN", "REFERENCE", "LOSS", "FLOOR (-6.9%)"
            c3_l1 = "Dynamic area weighting based on Turnover Value"
            c3_l2 = "Capital breadth: Count Ceiling / Gain / Ref / Loss / Floor"
            c3_l3 = "Auto-sort top liquidity sectors across the market"
        else:
            c1_t = "Phễu Thu Gom &amp; Giải Mã Tick Tốc Độ Cao"
            b1_title = "GÓI TIN X (KHỚP)"
            b1_sub = "Giá khớp, Vol, Mua/bán"
            b2_title = "GÓI TIN MI (CHỈ SỐ)"
            b2_sub = "VN-Index, VN30, HNX30"
            b3_title = "TÍNH % BIẾN ĐỘNG"
            b3_sub = "So sánh giá Ref Snapshot"
            c1_b = "DECODE REAL-TIME TRONG LUỒNG ASYNC &lt; 0.05MS"

            c2_t = "Kho Dữ Liệu RAM O(1) &amp; Khóa An Toàn Mutex"
            c2_l1 = "Quản lý tức thời trạng thái hơn 700 mã cổ phiếu 3 sàn"
            c2_l2 = "Khóa Thread-safe loại bỏ hoàn toàn race condition"
            c2_l3 = "Không ghi đĩa trong phiên, triệt tiêu nghẽn I/O"
            c2_b = "TRUY VẤN BỘ NHỚ TRONG PHIÊN &lt; 0.12MS"

            c3_t = "Phân Loại 15 Nhóm Ngành &amp; Thước Đo Độ Rộng"
            sec1, sec2, sec3, sec4, sec5 = "Ngân Hàng", "Bất Động Sản", "Thép - VLXD", "Chứng Khoán", "+11 Ngành Khác"
            ce, ga, rf, lo, fl = "TRẦN (+6.9%)", "TĂNG GIÁ", "THAM CHIẾU", "GIẢM GIÁ", "SÀN (-6.9%)"
            c3_l1 = "Tính toán tỷ trọng diện tích dựa trên Giá trị giao dịch"
            c3_l2 = "Thống kê phân bổ dòng tiền: Số mã Trần/Tăng/TC/Giảm/Sàn"
            c3_l3 = "Tự động sắp xếp Top ngành thanh khoản cao nhất toàn sàn"

        return f"""
        <!-- Core Card 1: Fan-in Worker -->
        <g transform="translate(410, 35)">
          <rect width="420" height="210" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="16" y="14" width="102" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="67" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">FAN-IN WORKER</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">{c1_t}</text>
          
          <!-- 3 mini boxes -->
          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="122" height="46" rx="4" fill="#061826" stroke="#0c4a6e" stroke-width="1" />
            <text x="61" y="19" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{b1_title}</text>
            <text x="61" y="35" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">{b1_sub}</text>

            <rect x="132" y="0" width="122" height="46" rx="4" fill="#061826" stroke="#0c4a6e" stroke-width="1" />
            <text x="193" y="19" fill="#c084fc" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{b2_title}</text>
            <text x="193" y="35" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">{b2_sub}</text>

            <rect x="264" y="0" width="122" height="46" rx="4" fill="#061826" stroke="#0c4a6e" stroke-width="1" />
            <text x="325" y="19" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{b3_title}</text>
            <text x="325" y="35" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="8.5" text-anchor="middle">{b3_sub}</text>
          </g>

          <rect x="16" y="132" width="388" height="22" rx="4" fill="#082f49" />
          <text x="210" y="146.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="9.5" font-weight="600" text-anchor="middle">{c1_b}</text>
        </g>

        <!-- Core Card 2: In-Memory RAM Store -->
        <g transform="translate(410, 285)">
          <rect width="420" height="210" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="16" y="14" width="112" height="18" rx="3" fill="#082f49" stroke="#0284c7" stroke-width="1" />
          <text x="72" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">IN-MEMORY STORE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">{c2_t}</text>
          
          <g transform="translate(16, 76)">
            <text x="0" y="0" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" font-weight="700">HASH-MAP O(1):</text>
            <text x="100" y="0" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_l1}</text>

            <text x="0" y="26" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" font-weight="700">MUTEX LOCK:</text>
            <text x="88" y="26" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_l2}</text>

            <text x="0" y="52" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" font-weight="700">ZERO DISK I/O:</text>
            <text x="104" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_l3}</text>
          </g>

          <rect x="16" y="162" width="388" height="22" rx="3" fill="#082f49" />
          <text x="210" y="175.5" fill="#7dd3fc" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c2_b}</text>
        </g>

        <!-- Core Card 3: Sector Classifier -->
        <g transform="translate(410, 535)">
          <rect width="420" height="215" rx="8" fill="{CARD_BG}" stroke="{BORDER_BASE}" stroke-width="1.2" />
          <rect x="16" y="14" width="102" height="18" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1" />
          <text x="67" y="26.5" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">VS-SECTOR CORE</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="15" font-weight="700">{c3_t}</text>
          
          <!-- Sector Tag Pills -->
          <g transform="translate(16, 68)">
            <rect x="0" y="0" width="72" height="20" rx="3" fill="#1e293b" /><text x="36" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">{sec1}</text>
            <rect x="79" y="0" width="72" height="20" rx="3" fill="#1e293b" /><text x="115" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">{sec2}</text>
            <rect x="158" y="0" width="72" height="20" rx="3" fill="#1e293b" /><text x="194" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">{sec3}</text>
            <rect x="237" y="0" width="72" height="20" rx="3" fill="#1e293b" /><text x="273" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">{sec4}</text>
            <rect x="316" y="0" width="72" height="20" rx="3" fill="#1e293b" /><text x="352" y="13.5" fill="{TEXT_MUTED}" font-family="var(--font-sans)" font-size="9" text-anchor="middle">{sec5}</text>
          </g>

          <!-- 5-Color Spectrum Bar -->
          <g transform="translate(16, 96)">
            <rect x="0" y="0" width="74" height="22" rx="3" fill="#7c3aed" /><text x="37" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{ce}</text>
            <rect x="78" y="0" width="74" height="22" rx="3" fill="#059669" /><text x="115" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{ga}</text>
            <rect x="156" y="0" width="74" height="22" rx="3" fill="#d97706" /><text x="193" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{rf}</text>
            <rect x="234" y="0" width="74" height="22" rx="3" fill="#dc2626" /><text x="271" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{lo}</text>
            <rect x="312" y="0" width="76" height="22" rx="3" fill="#0284c7" /><text x="350" y="14.5" fill="#fff" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{fl}</text>
          </g>

          <text x="16" y="142" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
          <text x="28" y="142" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l1}</text>

          <text x="16" y="164" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
          <text x="28" y="164" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l2}</text>

          <text x="16" y="186" fill="{TEXT_MUTED}" font-family="var(--font-mono)" font-size="9.5">&bull;</text>
          <text x="28" y="186" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_l3}</text>
        </g>
        """

    def _render_presentation_cards(self):
        if self.is_en:
            c1_t = "aiohttp Server &amp; WebSocket /ws"
            c1_1 = "Port 8050: Auto port reclamation (1-Click Play)"
            c1_2 = "Broadcast delta packets at 60 FPS to all clients"

            c2_t = "Interactive Market Heatmap (Treemap)"
            c2_1 = "ZRender Centroid Hook: Centered ticker labels inside cells"
            c2_2 = "Auto-hide text when cell &lt; 38px to prevent overflow"
            c2_3 = "Flash Update visual pulse upon new tick arrival (&lt; 16ms)"
            c2_4 = "3-color market breadth meter: Gain, Ref, Loss"

            c3_b = "FAILOVER &amp; INSPECTOR"
            c3_t = "Polling Live Mode &amp; Inspector Drawer"
            c3_1 = "Auto-switch to POLLING LIVE (2.5s cycle) on disconnect"
            c3_2 = "Auxiliary drawer: Top 6 liquidity sectors &amp; market breadth"
            c3_bottom = "AUTOMATIC RECONNECT (AUTO-RECONNECT) EVERY 3S"
        else:
            c1_t = "Máy Chủ aiohttp &amp; WebSocket /ws"
            c1_1 = "Cổng 8050: Tự động giải phóng cổng cũ (1-Click Play)"
            c1_2 = "Đẩy gói tin vi sai delta 60 FPS về toàn bộ client"

            c2_t = "Giao Diện Bản Đồ Nhiệt Toàn Cảnh (Treemap)"
            c2_1 = "Hook ZRender Centroid: Căn giữa nhãn cổ phiếu trong ô"
            c2_2 = "Tự động ẩn text khi ô &lt; 38px để chống tràn diện tích"
            c2_3 = "Hiệu ứng Flash Update chớp sáng khi có tick mới (&lt; 16ms)"
            c2_4 = "Thước đo độ rộng 3 màu: Trần/Tăng, Tham chiếu, Giảm/Sàn"

            c3_b = "FAILOVER &amp; INSPECTOR"
            c3_t = "Chế Độ Polling Live &amp; Bảng Soi Thông Số"
            c3_1 = "Tự chuyển POLLING LIVE (chu kỳ 2.5s) khi đứt mạng"
            c3_2 = "Drawer phụ: Top 6 ngành hút tiền, độ rộng thị trường"
            c3_bottom = "TỰ ĐỘNG THỬ KẾT NỐI LẠI (AUTO-RECONNECT) MỖI 3S"

        return f"""
        <!-- Presentation Card 1: WebSocket Hub -->
        <g transform="translate(940, 35)">
          <rect width="455" height="120" rx="8" fill="{CARD_BG}" stroke="{COLOR_EMERALD}" stroke-width="1.5" />
          <rect x="16" y="14" width="134" height="18" rx="3" fill="#064e3b" />
          <text x="83" y="26.5" fill="#34d399" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">FASTCONNECT LIVE HUB</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c1_t}</text>
          <text x="16" y="76" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">1.</text>
          <text x="30" y="76" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_1}</text>
          <text x="16" y="98" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="9.5">2.</text>
          <text x="30" y="98" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c1_2}</text>
        </g>

        <!-- Presentation Card 2: ECharts Treemap Canvas -->
        <g transform="translate(940, 195)">
          <rect width="455" height="350" rx="8" fill="{CARD_BG}" stroke="{COLOR_CYAN}" stroke-width="1.5" />
          <rect x="16" y="14" width="112" height="18" rx="3" fill="#082f49" />
          <text x="72" y="26.5" fill="#38bdf8" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">ECHARTS 5.4 CANVAS</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c2_t}</text>

          <!-- Embedded Mini Treemap Mockup (width=423 strictly within card width 455) -->
          {render_mini_treemap(16, 62, 423, 120, is_en=self.is_en)}

          <g transform="translate(16, 202)">
            <text x="0" y="16" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="12" y="16" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_1}</text>
            <text x="0" y="40" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="12" y="40" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_2}</text>
            <text x="0" y="64" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="12" y="64" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_3}</text>
            <text x="0" y="88" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="9">&bull;</text>
            <text x="12" y="88" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c2_4}</text>
          </g>

          <rect x="16" y="312" width="423" height="22" rx="3" fill="#082f49" />
          <text x="227" y="326" fill="#7dd3fc" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">60 FPS REALTIME HEATMAP ENGINE</text>
        </g>

        <!-- Presentation Card 3: Polling Fallback (Y: 585 to 750) -->
        <g transform="translate(940, 585)">
          <rect width="455" height="165" rx="8" fill="{CARD_BG}" stroke="{COLOR_AMBER}" stroke-width="1.5" />
          <rect x="16" y="14" width="134" height="18" rx="3" fill="#451a03" />
          <text x="83" y="26.5" fill="#fbbf24" font-family="var(--font-mono)" font-size="8.5" font-weight="700" text-anchor="middle">{c3_b}</text>
          <text x="16" y="52" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="14" font-weight="700">{c3_t}</text>
          <text x="16" y="78" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="9.5">1.</text>
          <text x="30" y="78" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_1}</text>
          <text x="16" y="102" fill="{COLOR_AMBER}" font-family="var(--font-mono)" font-size="9.5">2.</text>
          <text x="30" y="102" fill="{TEXT_MAIN}" font-family="var(--font-sans)" font-size="11">{c3_2}</text>
          <rect x="16" y="130" width="423" height="22" rx="3" fill="#451a03" />
          <text x="227" y="144" fill="#fde68a" font-family="var(--font-mono)" font-size="8.5" font-weight="600" text-anchor="middle">{c3_bottom}</text>
        </g>
        """

