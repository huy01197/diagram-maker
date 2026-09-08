"""
diagram-maker: Geometry & Routing Calculations
Cung cấp thuật toán định tuyến đường cong Bézier mềm mại, tính toán tiếp điểm,
và tạo các huy hiệu nhãn (pill badges) không che lấp dây nối và mũi tên.
"""

from .palette import THEME_PALETTE

def render_pill_badge(x, y, text, color="cyan", width=None, height=20):
    """
    Kết xuất huy hiệu nhãn kỹ thuật (pill badge) với nền bảo vệ đặc để không che đường nét.
    """
    theme = THEME_PALETTE.get(color, THEME_PALETTE["cyan"])
    badge_bg = theme["badge_bg"]
    badge_border = theme["badge_border"]
    text_color = theme["text"]
    
    calc_width = width if width else max(60, len(text) * 7.2 + 24)

    return f"""
      <g transform="translate({x}, {y})">
        <rect x="0" y="0" width="{calc_width}" height="{height}" rx="4" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1" />
        <text x="{calc_width / 2}" y="{height / 2 + 4}" fill="{text_color}" font-family="var(--font-mono)" font-size="9" font-weight="700" text-anchor="middle">{text}</text>
      </g>
    """

def compute_bezier_path(start, end, style="horizontal_s"):
    """
    Tính toán đường cong Cubic Bézier mượt mà giữa 2 điểm (x1, y1) và (x2, y2).
    """
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    if style == "horizontal_s":
        # Uốn lượn hình chữ S theo chiều ngang
        cx1 = x1 + dx * 0.5
        cy1 = y1
        cx2 = x2 - dx * 0.5
        cy2 = y2
        return f"M {x1} {y1} C {cx1} {cy1}, {cx2} {cy2}, {x2} {y2}"
    elif style == "vertical_s":
        # Uốn lượn hình chữ S theo chiều dọc
        cx1 = x1
        cy1 = y1 + dy * 0.5
        cx2 = x2
        cy2 = y2 - dy * 0.5
        return f"M {x1} {y1} C {cx1} {cy1}, {cx2} {cy2}, {x2} {y2}"
    elif style == "straight":
        return f"M {x1} {y1} L {x2} {y2}"
    else:
        return f"M {x1} {y1} L {x2} {y2}"
