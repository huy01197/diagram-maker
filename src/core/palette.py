"""
diagram-maker: Core Institutional Color Palette
Bảng màu chuẩn hóa phong cách Institutional Financial Terminal (Bloomberg / TradingView / TCBS).
Tuyệt đối không sử dụng icon hoạt họa, emoji, hoặc phong cách sặc sỡ.
"""

# Base Dark Theme Colors
BG_DARK = "#070a12"
CARD_BG = "#0b101b"
SUBCARD_BG = "#0e1524"
BORDER_BASE = "#1b253b"
BORDER_HIGHLIGHT = "#2962ff"

# Functional Data Colors
COLOR_BLUE = "#2962ff"      # Navigation / Links / Highlight
COLOR_CYAN = "#06b6d4"      # Ingress / Real-time / In-memory
COLOR_EMERALD = "#089981"   # Growth / Bullish / Verified / Live Stream
COLOR_AMBER = "#f59e0b"     # Warning / Failover / Gold / Volume
COLOR_PURPLE = "#a855f7"    # Ceiling / Quant / Session / Logic
COLOR_ROSE = "#f23645"      # Floor / Decline / Error / Overbought
COLOR_SLATE = "#94a3b8"     # Neutral / Metadata / Secondary

# Typography Colors
TEXT_MAIN = "#f1f5f9"
TEXT_MUTED = "#8b9bb4"
TEXT_DIM = "#64748b"

# Color Palette Config by Token Name
THEME_PALETTE = {
    "blue": {
        "primary": COLOR_BLUE,
        "border": "#1d4ed8",
        "badge_bg": "#1e1b4b",
        "badge_border": "#4338ca",
        "text": "#93c5fd"
    },
    "cyan": {
        "primary": COLOR_CYAN,
        "border": "#0e7490",
        "badge_bg": "#082f49",
        "badge_border": "#0284c7",
        "text": "#38bdf8"
    },
    "emerald": {
        "primary": COLOR_EMERALD,
        "border": "#059669",
        "badge_bg": "#064e3b",
        "badge_border": "#059669",
        "text": "#34d399"
    },
    "amber": {
        "primary": COLOR_AMBER,
        "border": "#b45309",
        "badge_bg": "#451a03",
        "badge_border": "#b45309",
        "text": "#fbbf24"
    },
    "purple": {
        "primary": COLOR_PURPLE,
        "border": "#7c3aed",
        "badge_bg": "#2e1065",
        "badge_border": "#6d28d9",
        "text": "#c084fc"
    },
    "rose": {
        "primary": COLOR_ROSE,
        "border": "#be123c",
        "badge_bg": "#4c0519",
        "badge_border": "#be123c",
        "text": "#fb7185"
    },
    "slate": {
        "primary": COLOR_SLATE,
        "border": "#475569",
        "badge_bg": "#1e293b",
        "badge_border": "#334155",
        "text": "#cbd5e1"
    }
}

# Standard Virtual Port Coupling Palette (A, B, C, D, E, F, G, H...)
PORT_PALETTE = {
    "A": COLOR_PURPLE,   # 01. High-frequency Logic / Quant Engine / Primary Bus
    "B": COLOR_EMERALD,  # 02. Real-time Stream / Lakehouse Sync / Verified Output
    "C": COLOR_CYAN,     # 03. Fast Ingestion / In-Memory Store / Direct Stream
    "D": COLOR_AMBER,    # 04. Failover Fallback / Polling Drawer / Cold Cache
    "E": COLOR_BLUE,     # 05. Gateway Router / Dispatcher / User Control
    "F": COLOR_ROSE,     # 06. Circuit Breaker / Anomaly / Risk Engine
    "G": "#ec4899",      # 07. Analytics Extension Bus (Pink)
    "H": "#6366f1",      # 08. Cross-Region Bridge Bus (Indigo)
}

def get_port_color(port_id: str, default: str = COLOR_CYAN) -> str:
    """Tra cứu màu sắc chuẩn hóa cho Virtual Port Junction theo mã định danh (A, B, C, D, E, F...)."""
    return PORT_PALETTE.get(str(port_id).strip().upper(), default)

