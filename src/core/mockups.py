"""
diagram-maker: Mini Visual Mockup Components Library
Thư viện các thành phần trực quan thu nhỏ (Visual Components) chuẩn Institutional Financial Terminal:
- Mini Treemap Canvas (Bản đồ nhiệt phân bổ ngành)
- Mini Candlestick Chart (Đồ thị nến Nhật OHLCV + MA + Volume + Tín hiệu Mua)
- Mini Multi-Pane Chart (Đồ thị kỹ thuật 4 tầng đồng bộ: Nến, Volume, MACD, RSI)
"""

from .palette import (
    COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_PURPLE, COLOR_ROSE, COLOR_BLUE,
    TEXT_MAIN, TEXT_DIM, BORDER_BASE
)

def render_mini_treemap(x, y, width=440, height=105, is_en=False):
    """Mô phỏng bản đồ nhiệt trực quan ECharts Treemap Mini Canvas chuẩn Institutional"""
    s_banking = "BANKING" if is_en else "NGÂN HÀNG"
    s_realestate = "REAL ESTATE" if is_en else "BẤT ĐỘNG SẢN"
    s_steel = "STEEL" if is_en else "THÉP"
    s_securities = "SECURITIES" if is_en else "CHỨNG KHOÁN"

    gap = 8
    avail = width - 2 * gap
    w1 = int(avail * 0.44)          # ~186px
    w2 = int(avail * 0.31)          # ~131px
    w3 = avail - w1 - w2            # ~107px

    x1 = 0
    x2 = x1 + w1 + gap
    x3 = x2 + w2 + gap

    h_main = height
    h_sub = int((height - 6) / 2)

    cell1_w = int((w1 - 18) / 2)
    cell2_w = w2 - 14

    return f"""
      <g transform="translate({x}, {y})">
        <!-- Sector 1: Ngân Hàng (Emerald) -->
        <g transform="translate({x1}, 0)">
          <rect width="{w1}" height="{h_main}" rx="5" fill="#064e3b" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <text x="8" y="15" fill="#34d399" font-family="var(--font-mono)" font-size="8.5" font-weight="700">{s_banking}</text>
          <rect x="7" y="22" width="{cell1_w}" height="{h_main - 29}" rx="3" fill="#042f2e" />
          <text x="{7 + cell1_w // 2}" y="{22 + (h_main - 29) // 2 - 2}" fill="#fff" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">VCB</text>
          <text x="{7 + cell1_w // 2}" y="{22 + (h_main - 29) // 2 + 15}" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">+3.2%</text>

          <rect x="{11 + cell1_w}" y="22" width="{cell1_w}" height="{h_main - 29}" rx="3" fill="#042f2e" />
          <text x="{11 + cell1_w + cell1_w // 2}" y="{22 + (h_main - 29) // 2 - 2}" fill="#fff" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">BID</text>
          <text x="{11 + cell1_w + cell1_w // 2}" y="{22 + (h_main - 29) // 2 + 15}" fill="#34d399" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">+1.8%</text>
        </g>

        <!-- Sector 2: Bất Động Sản (Rose) -->
        <g transform="translate({x2}, 0)">
          <rect width="{w2}" height="{h_main}" rx="5" fill="#4c0519" stroke="{COLOR_ROSE}" stroke-width="1.2" />
          <text x="8" y="15" fill="#fb7185" font-family="var(--font-mono)" font-size="8.5" font-weight="700">{s_realestate}</text>
          <rect x="7" y="22" width="{cell2_w}" height="{h_main - 29}" rx="3" fill="#881337" />
          <text x="{7 + cell2_w // 2}" y="{22 + (h_main - 29) // 2 - 2}" fill="#fff" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">VHM</text>
          <text x="{7 + cell2_w // 2}" y="{22 + (h_main - 29) // 2 + 15}" fill="#fecdd3" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">-2.4%</text>
        </g>

        <!-- Sector 3: Thép (Cyan) -->
        <g transform="translate({x3}, 0)">
          <rect width="{w3}" height="{h_sub}" rx="4" fill="#082f49" stroke="{COLOR_CYAN}" stroke-width="1" />
          <text x="8" y="13" fill="#7dd3fc" font-family="var(--font-mono)" font-size="7.5" font-weight="700">{s_steel}</text>
          <text x="{w3 - 8}" y="13" fill="#38bdf8" font-family="var(--font-mono)" font-size="8" font-weight="700" text-anchor="end">+2.1%</text>
          <text x="{w3 // 2}" y="{h_sub - 8}" fill="#fff" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">HPG</text>
        </g>

        <!-- Sector 4: Chứng Khoán (Purple) -->
        <g transform="translate({x3}, {h_sub + 6})">
          <rect width="{w3}" height="{h_sub}" rx="4" fill="#2e1065" stroke="{COLOR_PURPLE}" stroke-width="1" />
          <text x="8" y="13" fill="#d8b4fe" font-family="var(--font-mono)" font-size="7.5" font-weight="700">{s_securities}</text>
          <text x="{w3 - 8}" y="13" fill="#c084fc" font-family="var(--font-mono)" font-size="8" font-weight="700" text-anchor="end">+4.5%</text>
          <text x="{w3 // 2}" y="{h_sub - 8}" fill="#fff" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">SSI</text>
        </g>
      </g>
    """

def render_mini_candlestick_chart(x, y, width=398, height=180, ticker="FPT", price="91.50 (+4.2%)", is_en=False):
    """Mô phỏng biểu đồ nến Nhật OHLCV kèm đường MA và cột khối lượng Volume"""
    timeframe_label = "DAILY (D1)" if is_en else "KHUNG NGÀY (D1)"
    buy_badge = "BUY @ 91.5 (VOL +180%)" if is_en else "MUA @ 91.5 (VOL +180%)"
    return f"""
      <g transform="translate({x}, {y})">
        <!-- Container Box -->
        <rect width="{width}" height="{height}" rx="6" fill="#080c16" stroke="{BORDER_BASE}" stroke-width="1" />
        
        <!-- Header Bar -->
        <rect width="{width}" height="24" rx="6" fill="#0c121e" />
        <text x="10" y="16" fill="{TEXT_MAIN}" font-family="var(--font-mono)" font-size="9.5" font-weight="700">{ticker} &middot; {timeframe_label}</text>
        <text x="215" y="16" fill="#34d399" font-family="var(--font-mono)" font-size="9.5" font-weight="700">{price}</text>
        <text x="320" y="16" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="8">EMA20: 88.4</text>

        <!-- Chart Grid & Candles -->
        <g transform="translate(8, 30)">
          <line x1="0" y1="20" x2="345" y2="20" stroke="#141c2e" stroke-width="1" stroke-dasharray="2 2" />
          <line x1="0" y1="50" x2="345" y2="50" stroke="#141c2e" stroke-width="1" stroke-dasharray="2 2" />
          <line x1="0" y1="80" x2="345" y2="80" stroke="#141c2e" stroke-width="1" stroke-dasharray="2 2" />
          <line x1="0" y1="105" x2="345" y2="105" stroke="#1e293b" stroke-width="1" />

          <!-- Y-Axis Labels -->
          <text x="350" y="24" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7.5">93.0</text>
          <text x="350" y="54" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7.5">89.0</text>
          <text x="350" y="84" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7.5">85.0</text>
          <text x="350" y="130" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">VOL</text>

          <!-- Candlesticks & Volume Bars -->
          <line x1="15" y1="65" x2="15" y2="88" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="10" y="70" width="10" height="14" fill="{COLOR_EMERALD}" rx="1" />
          <rect x="10" y="125" width="10" height="15" fill="{COLOR_EMERALD}" opacity="0.6" />

          <line x1="45" y1="68" x2="45" y2="85" stroke="{COLOR_ROSE}" stroke-width="1.2" />
          <rect x="40" y="72" width="10" height="10" fill="{COLOR_ROSE}" rx="1" />
          <rect x="40" y="130" width="10" height="10" fill="{COLOR_ROSE}" opacity="0.6" />

          <line x1="75" y1="58" x2="75" y2="80" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="70" y="64" width="10" height="12" fill="{COLOR_EMERALD}" rx="1" />
          <rect x="70" y="122" width="10" height="18" fill="{COLOR_EMERALD}" opacity="0.6" />

          <line x1="105" y1="50" x2="105" y2="72" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="100" y="54" width="10" height="14" fill="{COLOR_EMERALD}" rx="1" />
          <rect x="100" y="118" width="10" height="22" fill="{COLOR_EMERALD}" opacity="0.6" />

          <line x1="135" y1="52" x2="135" y2="70" stroke="{COLOR_ROSE}" stroke-width="1.2" />
          <rect x="130" y="56" width="10" height="10" fill="{COLOR_ROSE}" rx="1" />
          <rect x="130" y="128" width="10" height="12" fill="{COLOR_ROSE}" opacity="0.6" />

          <line x1="165" y1="55" x2="165" y2="75" stroke="{COLOR_ROSE}" stroke-width="1.2" />
          <rect x="160" y="60" width="10" height="12" fill="{COLOR_ROSE}" rx="1" />
          <rect x="160" y="132" width="10" height="8" fill="{COLOR_ROSE}" opacity="0.6" />

          <line x1="195" y1="52" x2="195" y2="68" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="190" y="56" width="10" height="8" fill="{COLOR_EMERALD}" rx="1" />
          <rect x="190" y="133" width="10" height="7" fill="{COLOR_EMERALD}" opacity="0.6" />

          <line x1="225" y1="50" x2="225" y2="66" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="220" y="54" width="10" height="8" fill="{COLOR_EMERALD}" rx="1" />
          <rect x="220" y="134" width="10" height="6" fill="{COLOR_EMERALD}" opacity="0.6" />

          <line x1="255" y1="42" x2="255" y2="62" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="250" y="46" width="10" height="12" fill="{COLOR_EMERALD}" rx="1" />
          <rect x="250" y="124" width="10" height="16" fill="{COLOR_EMERALD}" opacity="0.6" />

          <!-- Breakout Candle -->
          <line x1="285" y1="18" x2="285" y2="48" stroke="{COLOR_EMERALD}" stroke-width="1.6" />
          <rect x="280" y="24" width="10" height="22" fill="{COLOR_EMERALD}" rx="1" filter="url(#blueGlow)" />
          <rect x="280" y="110" width="10" height="30" fill="{COLOR_EMERALD}" opacity="0.9" />

          <line x1="315" y1="12" x2="315" y2="30" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="310" y="16" width="10" height="10" fill="{COLOR_EMERALD}" rx="1" />
          <rect x="310" y="115" width="10" height="25" fill="{COLOR_EMERALD}" opacity="0.7" />

          <!-- MA Curves -->
          <path d="M 15 78 Q 75 70, 135 62 T 225 56 T 285 38 T 315 26" fill="none" stroke="{COLOR_CYAN}" stroke-width="1.8" />
          <path d="M 15 85 Q 105 80, 195 72 T 315 54" fill="none" stroke="{COLOR_AMBER}" stroke-width="1.5" stroke-dasharray="3 2" />

          <!-- Signal Badge -->
          <g transform="translate(195, 2)">
            <rect x="0" y="0" width="140" height="18" rx="3" fill="#064e3b" stroke="#34d399" stroke-width="1" />
            <text x="70" y="12.5" fill="#a7f3d0" font-family="var(--font-mono)" font-size="8" font-weight="700" text-anchor="middle">{buy_badge}</text>
          </g>
        </g>
      </g>
    """

def render_mini_multipane_chart(x, y, width=418, height=235, ticker="VCB", price="96.80 (+3.2%)", is_en=False):
    """Mô phỏng đồ thị kỹ thuật 4 tầng đồng bộ (Nến, Volume, MACD, RSI) chuẩn Plotly"""
    p1_label = "PANE 1: OHLCV CANDLES + MA20/50" if is_en else "PANE 1: NẾN OHLCV + MA20/MA50"
    p2_label = "PANE 2: VOLUME + VWAP"
    p3_label = "PANE 3: MACD (12, 26, 9)"
    p4_label = "PANE 4: RSI (14)"
    return f"""
      <g transform="translate({x}, {y})">
        <rect width="{width}" height="{height}" rx="6" fill="#080c16" stroke="{BORDER_BASE}" stroke-width="1" />
        
        <!-- Header Bar -->
        <rect width="{width}" height="22" rx="6" fill="#0c121e" />
        <text x="10" y="15" fill="{TEXT_MAIN}" font-family="var(--font-mono)" font-size="9.5" font-weight="700">{ticker} &middot; HOSE D1</text>
        <text x="250" y="15" fill="#34d399" font-family="var(--font-mono)" font-size="9.5" font-weight="700">{price}</text>
        <text x="350" y="15" fill="{COLOR_CYAN}" font-family="var(--font-mono)" font-size="8">PLOTLY SYNC</text>

        <!-- PANE 1: PRICE CANDLES & MA -->
        <g transform="translate(8, 26)">
          <rect width="365" height="85" fill="#080c16" />
          <line x1="0" y1="22" x2="365" y2="22" stroke="#141c2e" stroke-width="0.8" stroke-dasharray="2 2" />
          <line x1="0" y1="52" x2="365" y2="52" stroke="#141c2e" stroke-width="0.8" stroke-dasharray="2 2" />
          <text x="372" y="25" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">98.0</text>
          <text x="372" y="55" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">94.0</text>

          <!-- 10 Candlesticks -->
          <line x1="18" y1="50" x2="18" y2="70" stroke="{COLOR_ROSE}" stroke-width="1.2" />
          <rect x="14" y="54" width="8" height="12" fill="{COLOR_ROSE}" rx="1" />
          <line x1="48" y1="45" x2="48" y2="65" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="44" y="48" width="8" height="12" fill="{COLOR_EMERALD}" rx="1" />
          <line x1="78" y1="40" x2="78" y2="60" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="74" y="44" width="8" height="12" fill="{COLOR_EMERALD}" rx="1" />
          <line x1="108" y1="48" x2="108" y2="62" stroke="{COLOR_ROSE}" stroke-width="1.2" />
          <rect x="104" y="50" width="8" height="8" fill="{COLOR_ROSE}" rx="1" />
          <line x1="138" y1="42" x2="138" y2="58" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="134" y="46" width="8" height="8" fill="{COLOR_EMERALD}" rx="1" />
          <line x1="168" y1="36" x2="168" y2="54" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="164" y="40" width="8" height="10" fill="{COLOR_EMERALD}" rx="1" />
          <line x1="198" y1="38" x2="198" y2="52" stroke="{COLOR_ROSE}" stroke-width="1.2" />
          <rect x="194" y="41" width="8" height="7" fill="{COLOR_ROSE}" rx="1" />
          <line x1="228" y1="30" x2="228" y2="48" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="224" y="34" width="8" height="10" fill="{COLOR_EMERALD}" rx="1" />
          <line x1="258" y1="16" x2="258" y2="42" stroke="{COLOR_EMERALD}" stroke-width="1.5" />
          <rect x="254" y="20" width="8" height="18" fill="{COLOR_EMERALD}" rx="1" />
          <line x1="288" y1="10" x2="288" y2="30" stroke="{COLOR_EMERALD}" stroke-width="1.2" />
          <rect x="284" y="14" width="8" height="10" fill="{COLOR_EMERALD}" rx="1" />

          <path d="M 18 64 Q 78 54, 138 48 T 228 36 T 288 22" fill="none" stroke="{COLOR_CYAN}" stroke-width="1.6" />
          <path d="M 18 70 Q 108 65, 198 55 T 288 40" fill="none" stroke="{COLOR_AMBER}" stroke-width="1.3" stroke-dasharray="3 2" />
          <text x="6" y="12" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">{p1_label}</text>
        </g>

        <!-- Divider 1 -->
        <line x1="8" y1="113" x2="408" y2="113" stroke="#1b253b" stroke-width="1" />

        <!-- PANE 2: VOLUME & VWAP -->
        <g transform="translate(8, 115)">
          <rect width="365" height="35" fill="#080c16" />
          <text x="6" y="9" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">{p2_label}</text>
          <text x="372" y="24" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">VOL</text>

          <rect x="14" y="16" width="8" height="15" fill="{COLOR_ROSE}" opacity="0.6" />
          <rect x="44" y="14" width="8" height="17" fill="{COLOR_EMERALD}" opacity="0.6" />
          <rect x="74" y="18" width="8" height="13" fill="{COLOR_EMERALD}" opacity="0.6" />
          <rect x="104" y="22" width="8" height="9" fill="{COLOR_ROSE}" opacity="0.6" />
          <rect x="134" y="20" width="8" height="11" fill="{COLOR_EMERALD}" opacity="0.6" />
          <rect x="164" y="15" width="8" height="16" fill="{COLOR_EMERALD}" opacity="0.6" />
          <rect x="194" y="23" width="8" height="8" fill="{COLOR_ROSE}" opacity="0.6" />
          <rect x="224" y="12" width="8" height="19" fill="{COLOR_EMERALD}" opacity="0.7" />
          <rect x="254" y="4" width="8" height="27" fill="{COLOR_EMERALD}" opacity="0.9" />
          <rect x="284" y="8" width="8" height="23" fill="{COLOR_EMERALD}" opacity="0.8" />
          <path d="M 18 24 Q 108 22, 198 18 T 288 12" fill="none" stroke="{COLOR_PURPLE}" stroke-width="1.2" />
        </g>

        <!-- Divider 2 -->
        <line x1="8" y1="152" x2="408" y2="152" stroke="#1b253b" stroke-width="1" />

        <!-- PANE 3: MACD HISTOGRAM -->
        <g transform="translate(8, 154)">
          <rect width="365" height="38" fill="#080c16" />
          <line x1="0" y1="20" x2="365" y2="20" stroke="#1e293b" stroke-width="0.8" />
          <text x="6" y="9" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">PANE 3: MACD (12, 26, 9)</text>
          <text x="372" y="24" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">MACD</text>

          <rect x="14" y="20" width="6" height="7" fill="{COLOR_ROSE}" />
          <rect x="44" y="20" width="6" height="4" fill="{COLOR_ROSE}" />
          <rect x="74" y="17" width="6" height="3" fill="{COLOR_EMERALD}" />
          <rect x="104" y="18" width="6" height="2" fill="{COLOR_ROSE}" />
          <rect x="134" y="15" width="6" height="5" fill="{COLOR_EMERALD}" />
          <rect x="164" y="12" width="6" height="8" fill="{COLOR_EMERALD}" />
          <rect x="194" y="14" width="6" height="6" fill="{COLOR_EMERALD}" />
          <rect x="224" y="9" width="6" height="11" fill="{COLOR_EMERALD}" />
          <rect x="254" y="4" width="6" height="16" fill="{COLOR_EMERALD}" />
          <rect x="284" y="2" width="6" height="18" fill="{COLOR_EMERALD}" />
          <path d="M 18 24 Q 108 20, 198 14 T 288 6" fill="none" stroke="{COLOR_BLUE}" stroke-width="1.3" />
          <path d="M 18 23 Q 108 21, 198 16 T 288 10" fill="none" stroke="{COLOR_AMBER}" stroke-width="1.1" stroke-dasharray="2 1" />
        </g>

        <!-- Divider 3 -->
        <line x1="8" y1="194" x2="408" y2="194" stroke="#1b253b" stroke-width="1" />

        <!-- PANE 4: RSI WITH 30/70 BANDS -->
        <g transform="translate(8, 196)">
          <rect width="365" height="36" fill="#080c16" />
          <line x1="0" y1="8" x2="365" y2="8" stroke="{COLOR_ROSE}" stroke-width="0.8" stroke-dasharray="2 2" opacity="0.6" />
          <line x1="0" y1="26" x2="365" y2="26" stroke="{COLOR_EMERALD}" stroke-width="0.8" stroke-dasharray="2 2" opacity="0.6" />
          <text x="6" y="8" fill="{TEXT_DIM}" font-family="var(--font-mono)" font-size="7">PANE 4: RSI (14)</text>
          <text x="372" y="10" fill="{COLOR_ROSE}" font-family="var(--font-mono)" font-size="6.5">70</text>
          <text x="372" y="28" fill="{COLOR_EMERALD}" font-family="var(--font-mono)" font-size="6.5">30</text>
          <path d="M 18 24 Q 78 20, 138 18 T 228 14 T 258 8 T 288 6" fill="none" stroke="{COLOR_PURPLE}" stroke-width="1.5" />
        </g>
      </g>
    """
