"""
Diagram Maker Engine - Graph Compiler
Chuyển đổi khai báo đồ thị (JSON AST) thành SVG Vector với thuật toán Auto-Layout & Bezier Routing.
Tuân thủ chuẩn Institutional Dark Terminal.
"""

import html

COLOR_PALETTE = {
    "sky": {
        "primary": "#38bdf8",
        "border": "#0284c7",
        "badge_bg": "#082f49",
        "badge_border": "#0284c7",
        "glow": "blueGlow"
    },
    "emerald": {
        "primary": "#34d399",
        "border": "#059669",
        "badge_bg": "#064e3b",
        "badge_border": "#059669",
        "glow": "emeraldGlow"
    },
    "amber": {
        "primary": "#fbbf24",
        "border": "#d97706",
        "badge_bg": "#451a03",
        "badge_border": "#b45309",
        "glow": "amberGlow"
    },
    "rose": {
        "primary": "#fb7185",
        "border": "#e11d48",
        "badge_bg": "#4c0519",
        "badge_border": "#be123c",
        "glow": "roseGlow"
    },
    "indigo": {
        "primary": "#818cf8",
        "border": "#4f46e5",
        "badge_bg": "#1e1b4b",
        "badge_border": "#4338ca",
        "glow": "indigoGlow"
    },
    "purple": {
        "primary": "#c084fc",
        "border": "#7c3aed",
        "badge_bg": "#2e1065",
        "badge_border": "#6d28d9",
        "glow": "purpleGlow"
    },
    "slate": {
        "primary": "#94a3b8",
        "border": "#475569",
        "badge_bg": "#1e293b",
        "badge_border": "#334155",
        "glow": "slateGlow"
    }
}

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
PADDING_X = 60
BODY_TOP = 145
BODY_BOTTOM = 645
MID_Y = (BODY_TOP + BODY_BOTTOM) / 2  # 395

class GraphCompiler:
    def __init__(self, spec):
        self.spec = spec
        self.nodes = {}
        self.columns = []
        self.connections = spec.get("connections", [])
        self.title = spec.get("title", "Architecture Diagram")
        self.category = spec.get("category", "SYSTEM ARCHITECTURE")
        self.subtitle = spec.get("subtitle", "Autonomous Pipeline Architecture")

    def _calculate_node_dimensions(self, node):
        """Tự động tính toán kích thước chiều rộng và chiều cao tối ưu, thích ứng số lượng cột"""
        num_cols = len(self.spec.get("columns", []))
        title_len = len(node.get("title", ""))
        badge_len = len(node.get("badge", ""))
        has_items = bool(node.get("items"))
        has_badges = bool(node.get("custom_badges"))
        
        # 1. Chiều rộng: Thích ứng linh hoạt theo số cột (4 cột: trần 280px, 5 cột: trần 212px)
        if num_cols >= 5:
            max_limit = 212
            default_w = 205
            char_w = 6.6
            badge_char_w = 5.8
        else:
            max_limit = 280
            default_w = 260
            char_w = 7.5
            badge_char_w = 6.8

        req_w = node.get("width", default_w)
        if has_items and badge_len > 0:
            min_text_w = title_len * char_w + badge_len * badge_char_w + 26
            w = min(max(req_w, min_text_w), max_limit)
        elif has_badges:
            w = min(max(req_w, title_len * 7.5 + 26), max_limit)
        else:
            w = min(max(req_w, 195), max_limit if num_cols >= 5 else 230)

        # 2. Chiều cao: Thiết kế theo tỷ lệ cô đọng (compact layout)
        if "height" in node and node["height"] is not None:
            h = node["height"]
        else:
            items_count = len(node.get("items", []))
            badges_count = len(node.get("custom_badges", []))
            has_bottom_box = bool(node.get("bottom_box"))
            
            if items_count > 0:
                h = 46 + items_count * 32 + 8
            elif badges_count > 0:
                h = 56 + ((badges_count + 1) // 2) * 26 + 8
            elif node.get("subtitle") or node.get("meta"):
                h = 108
            else:
                h = 88
            
            if has_bottom_box:
                h += 38

        return int(w), int(h)

    def calculate_layout(self):
        raw_cols = self.spec.get("columns", [])
        num_cols = len(raw_cols)
        if num_cols == 0:
            return

        self.padding_x = 40 if num_cols >= 5 else PADDING_X

        # 1. Đo lường kích thước các cột
        col_widths = []
        col_node_dims = []
        for c in raw_cols:
            nodes_in_col = c.get("nodes", [])
            max_w = 0
            dims_for_col = []
            for n in nodes_in_col:
                nw, nh = self._calculate_node_dimensions(n)
                dims_for_col.append((nw, nh))
                if nw > max_w:
                    max_w = nw
            col_widths.append(max_w)
            col_node_dims.append(dims_for_col)

        # 2. Phân bổ khoảng cách trục X cân đối
        total_col_width = sum(col_widths)
        available_width = CANVAS_WIDTH - (self.padding_x * 2)
        
        if num_cols > 1:
            gap_x = max(18, (available_width - total_col_width) / (num_cols - 1))
        else:
            gap_x = 0

        cur_x = self.padding_x
        # 3. Tính toán vị trí từng Node theo trục Y
        for col_idx, col_data in enumerate(raw_cols):
            nodes_in_col = col_data.get("nodes", [])
            w = col_widths[col_idx]
            m = len(nodes_in_col)

            # Khoảng cách giữa các Node trong cùng cột: 16px nếu 5 cột, 18px nếu 4 cột
            node_heights = [dim[1] for dim in col_node_dims[col_idx]]
            gap_y = 16 if num_cols >= 5 else 18
            if m <= 1:
                gap_y = 0
            total_col_h = sum(node_heights) + (m - 1) * gap_y

            # Căn giữa theo MID_Y
            start_y = MID_Y - (total_col_h / 2)
            cur_y = start_y

            for n_idx, n in enumerate(nodes_in_col):
                node_id = n["id"]
                node_h = node_heights[n_idx]
                self.nodes[node_id] = {
                    "data": n,
                    "x": cur_x,
                    "y": cur_y,
                    "width": w,
                    "height": node_h
                }
                cur_y += node_h + gap_y

            cur_x += w + gap_x

    def render_node(self, node_id, node_layout):
        n = node_layout["data"]
        x = node_layout["x"]
        y = node_layout["y"]
        w = node_layout["width"]
        h = node_layout["height"]
        
        color_name = n.get("color", "sky")
        theme = COLOR_PALETTE.get(color_name, COLOR_PALETTE["sky"])
        
        title = html.escape(n.get("title", ""))
        badge = html.escape(n.get("badge", ""))
        subtitle = html.escape(n.get("subtitle", ""))
        meta = html.escape(n.get("meta", ""))
        items = n.get("items", [])
        custom_badges = n.get("custom_badges", [])
        bottom_box = n.get("bottom_box")

        svg = []
        svg.append(f'<!-- Node: {node_id} -->')
        svg.append(f'<g class="diagram-node" data-node-id="{node_id}" data-title="{title}" transform="translate({x:.1f}, {y:.1f})" filter="url(#nodeShadow)">')
        
        # 1. Khung nền thẻ bo tròn hoàn hảo rx=16
        svg.append(f'  <rect width="{w}" height="{h}" rx="16" fill="#111827" stroke="{theme["border"]}" stroke-width="1.5"/>')

        # 2. Phân loại cấu trúc hiển thị
        is_endpoint_node = (subtitle or meta) and not items and not custom_badges

        if is_endpoint_node:
            # Dạng Node Ingestion / Dispatcher
            svg.append(f'  <rect x="1" y="1" width="{w - 2}" height="28" rx="14" fill="#1f2937" fill-opacity="0.5"/>')
            if badge:
                svg.append(f'  <circle cx="16" cy="15" r="3" fill="{theme["primary"]}"/>')
                svg.append(f'  <text x="24" y="18.5" fill="{theme["primary"]}" font-size="9.5" font-weight="700" font-family="monospace">{badge}</text>')
            
            svg.append(f'  <text x="16" y="52" fill="#ffffff" font-size="14.5" font-weight="700" font-family="system-ui">{title}</text>')
            if subtitle:
                svg.append(f'  <text x="16" y="73" fill="#9ca3af" font-size="11.5" font-family="system-ui">{subtitle}</text>')
            if meta:
                svg.append(f'  <text x="16" y="92" fill="{theme["primary"]}" font-size="10.5" font-weight="600" font-family="monospace">{meta}</text>')

        elif items:
            # Dạng Node Quy tắc / Xử lý
            title_fsize = "12.5" if w < 230 else "13.5"
            svg.append(f'  <text x="14" y="31" fill="{theme["primary"]}" font-size="{title_fsize}" font-weight="700" font-family="system-ui">{title}</text>')
            
            if badge:
                badge_char_w = 5.6 if w < 230 else 6.8
                badge_w = len(badge) * badge_char_w + 12
                badge_x = w - badge_w - 12
                svg.append(f'  <rect x="{badge_x:.1f}" y="16" width="{badge_w:.1f}" height="20" rx="6" fill="{theme["badge_bg"]}" stroke="{theme["badge_border"]}" stroke-width="0.8"/>')
                svg.append(f'  <text x="{badge_x + badge_w / 2:.1f}" y="30" fill="{theme["primary"]}" font-size="9" font-weight="700" font-family="monospace" text-anchor="middle">{badge}</text>')

            item_y = 46
            it_fsize = "9.5" if w < 230 else "10.5"
            for it in items:
                it_escaped = html.escape(it)
                svg.append(f'  <g transform="translate(12, {item_y})">')
                svg.append(f'    <rect width="{w - 24}" height="26" rx="6" fill="#1f2937" fill-opacity="0.6"/>')
                svg.append(f'    <text x="8" y="17" fill="#e5e7eb" font-size="{it_fsize}" font-weight="600" font-family="system-ui">{it_escaped}</text>')
                svg.append(f'  </g>')
                item_y += 32

        elif custom_badges:
            # Dạng Node Ma trận Quyết định
            svg.append(f'  <text x="16" y="32" fill="{theme["primary"]}" font-size="14" font-weight="700" font-family="system-ui">{title}</text>')
            if badge:
                svg.append(f'  <text x="16" y="49" fill="#9ca3af" font-size="10" font-family="monospace">{badge}</text>')

            badge_group_y = 58
            btn_w = (w - 38) / 2
            for b_idx, cb in enumerate(custom_badges):
                col_i = b_idx % 2
                row_i = b_idx // 2
                bx = 14 + col_i * (btn_w + 10)
                by = badge_group_y + row_i * 28
                c_theme = COLOR_PALETTE.get(cb.get("color", "slate"), COLOR_PALETTE["slate"])
                cb_label = html.escape(cb.get("label", ""))
                
                svg.append(f'  <g transform="translate({bx:.1f}, {by})">')
                svg.append(f'    <rect width="{btn_w:.1f}" height="22" rx="6" fill="{c_theme["badge_bg"]}" stroke="{c_theme["badge_border"]}" stroke-width="0.8"/>')
                svg.append(f'    <text x="{btn_w / 2:.1f}" y="15" fill="{c_theme["primary"]}" font-size="9.5" font-weight="700" font-family="system-ui" text-anchor="middle">{cb_label}</text>')
                svg.append(f'  </g>')

        # Hộp thông tin phụ dưới đáy (Bottom Box)
        if bottom_box:
            bb_escaped = html.escape(bottom_box)
            bb_y = h - 34
            svg.append(f'  <g transform="translate(14, {bb_y})">')
            svg.append(f'    <rect width="{w - 28}" height="26" rx="7" fill="#1f2937" stroke="#374151" stroke-width="1"/>')
            svg.append(f'    <text x="10" y="17" fill="#fbbf24" font-size="9.5" font-weight="700" font-family="monospace">{bb_escaped}</text>')
            svg.append(f'  </g>')

        svg.append('</g>')
        return "\n".join(svg)

    def render_connections(self):
        svg = []
        svg.append('<!-- BEZIER DYNAMIC WIRES (WITH AUTOMATIC PORT SPREAD) -->')
        
        # Đếm số lượng kết nối vào/ra từng node để dàn đều cổng kết nối (Port Spread)
        out_counts = {}
        in_counts = {}
        out_indices = {}
        in_indices = {}
        for conn in self.connections:
            s, d = conn.get("from"), conn.get("to")
            if s in self.nodes and d in self.nodes:
                out_counts[s] = out_counts.get(s, 0) + 1
                in_counts[d] = in_counts.get(d, 0) + 1

        for conn in self.connections:
            src_id = conn.get("from")
            dst_id = conn.get("to")
            
            if src_id not in self.nodes or dst_id not in self.nodes:
                continue

            src = self.nodes[src_id]
            dst = self.nodes[dst_id]

            out_idx = out_indices.get(src_id, 0)
            out_indices[src_id] = out_idx + 1
            in_idx = in_indices.get(dst_id, 0)
            in_indices[dst_id] = in_idx + 1

            # Dàn đều vị trí cổng vào/ra theo trục Y nếu có nhiều đường kết nối
            spread_out = 0
            if out_counts.get(src_id, 0) > 1:
                spread_out = (out_idx - (out_counts[src_id] - 1) / 2.0) * 10.0

            spread_in = 0
            if in_counts.get(dst_id, 0) > 1:
                spread_in = (in_idx - (in_counts[dst_id] - 1) / 2.0) * 10.0

            # Cổng ra (Right side of source with spread)
            x1 = src["x"] + src["width"]
            y1 = src["y"] + src["height"] / 2 + spread_out

            # Cổng vào (Left side of destination with spread - lùi 2.5px để mũi tên tiếp xúc viền chuẩn xác)
            x2 = dst["x"] - 2.5
            y2 = dst["y"] + dst["height"] / 2 + spread_in

            color_name = conn.get("color", "sky")
            theme = COLOR_PALETTE.get(color_name, COLOR_PALETTE["sky"])
            stroke_color = theme["primary"]

            is_animated = conn.get("animated", False)
            is_glow = conn.get("glow", False)

            dx = x2 - x1
            if dx <= 0:
                c1_x = x1 + 25
                c1_y = y1
                c2_x = x2 - 25
                c2_y = y2
            else:
                c1_x = x1 + dx * 0.5
                c1_y = y1
                c2_x = x2 - dx * 0.5
                c2_y = y2

            path_d = f"M {x1:.1f} {y1:.1f} C {c1_x:.1f} {c1_y:.1f}, {c2_x:.1f} {c2_y:.1f}, {x2:.1f} {y2:.1f}"

            classes = ["diagram-wire"]
            if is_animated:
                classes.append("glow-line")
            class_attr = f'class="{" ".join(classes)}"'
            data_attr = f'data-from="{src_id}" data-to="{dst_id}"'
            filter_attr = 'filter="url(#glowEffect)"' if is_glow else ''
            width_attr = 'stroke-width="2.2"' if is_animated or is_glow else 'stroke-width="1.6"'
            opacity_attr = 'stroke-opacity="0.9"' if is_animated or is_glow else 'stroke-opacity="0.7"'
            marker_attr = f'marker-end="url(#arrow-{color_name})"'

            svg.append(f'<path d="{path_d}" stroke="{stroke_color}" {width_attr} {opacity_attr} fill="none" {class_attr} {data_attr} {filter_attr} {marker_attr}/>')

        return "\n".join(svg)

    def compile_to_html(self, default_theme="dark"):
        self.calculate_layout()

        # Render tất cả Wires
        wires_svg = self.render_connections()

        # Render tất cả Nodes
        nodes_svg = []
        for n_id, n_layout in self.nodes.items():
            nodes_svg.append(self.render_node(n_id, n_layout))
        nodes_rendered = "\n".join(nodes_svg)

        # Header Category Badge
        cat_badge_w = len(self.category) * 8.2 + 48
        cat_esc = html.escape(self.category)
        title_esc = html.escape(self.title)
        sub_esc = html.escape(self.subtitle)

        is_en = self.spec.get("locale") == "en" or self.spec.get("lang") == "en" or not any(c in (str(self.title) + str(self.category) + str(self.subtitle)).lower() for c in ['kiến trúc', 'hệ thống', 'dữ liệu', 'sơ đồ', 'tầng', 'khung', 'phân tích'])
        html_lang = "en" if is_en else "vi"

        search_ph = "Search components... (/)" if is_en else "Tìm kiếm... (/)"
        theme_tt = "Toggle Theme (T)" if is_en else "Đổi giao diện (T)"
        svg_tt = "Export SVG Source" if is_en else "Xuất mã nguồn SVG"
        png_tt = "Export 2x Retina PNG" if is_en else "Xuất ảnh PNG Retina 2x"
        help_tt = "Keyboard Shortcuts (?)" if is_en else "Phím tắt (?)"

        modal_title = "VIEWER KEYBOARD SHORTCUTS" if is_en else "PHÍM TẮT ĐIỀU KHIỂN (VIEWER SHORTCUTS)"
        sc_search = "Search components" if is_en else "Tìm kiếm thành phần"
        sc_theme = "Toggle Light / Dark theme" if is_en else "Chuyển đổi giao diện Sáng / Tối"
        sc_reset = "Deselect / Reset active filters" if is_en else "Hủy chọn / Đặt lại bộ lọc"
        sc_svg = "Export Vector SVG" if is_en else "Xuất ảnh Vector SVG"
        sc_png = "Export Raster PNG 2x" if is_en else "Xuất ảnh Raster PNG 2x"
        sc_help = "Open this shortcut modal" if is_en else "Mở bảng trợ giúp này"

        html_output = f"""<!DOCTYPE html>
<html lang="{html_lang}" data-theme="{default_theme}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_esc}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root, [data-theme="dark"] {{
      --bg: #070a12;
      --card-bg: #0c121e;
      --border-base: #1b253b;
      --text-main: #e2e8f0;
      --text-muted: #8b9bb4;
      --canvas-bg: #080c16;
      --canvas-border: #1b253b;
      --toolbar-bg: #0d1424;
      --btn-bg: #131b2e;
      --btn-border: #23314f;
      --btn-hover: #1e2a47;
      --accent-cyan: #06b6d4;
      --accent-emerald: #089981;
      --accent-amber: #f59e0b;
      --accent-purple: #a855f7;
      --accent-rose: #f23645;
      --accent-blue: #2962ff;
      --dot-grid-color: #ffffff;
      --font-sans: 'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'Geist Mono', Menlo, Consolas, monospace;
    }}
    [data-theme="light"] {{
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border-base: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --canvas-bg: #ffffff;
      --canvas-border: #cbd5e1;
      --toolbar-bg: #f1f5f9;
      --btn-bg: #ffffff;
      --btn-border: #cbd5e1;
      --btn-hover: #e2e8f0;
      --accent-cyan: #0284c7;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-purple: #7c3aed;
      --accent-rose: #e11d48;
      --accent-blue: #1d4ed8;
      --dot-grid-color: #000000;
    }}
    body {{
      background-color: var(--bg);
      color: var(--text-main);
      font-family: var(--font-sans);
      margin: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      padding: 16px;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}
    .top-bar {{
      width: 100%;
      max-width: 1280px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-base);
      gap: 12px;
      flex-wrap: wrap;
    }}
    .eyebrow-title {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}
    .top-eyebrow {{
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--accent-cyan);
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }}
    .top-title {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
    }}
    .controls-bar {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .search-box input {{
      background: var(--toolbar-bg);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      color: var(--text-main);
      font-family: var(--font-mono);
      font-size: 11px;
      padding: 6px 10px;
      width: 140px;
      outline: none;
      transition: width 0.2s ease, border-color 0.2s ease;
    }}
    .search-box input:focus {{
      width: 190px;
      border-color: var(--accent-cyan);
    }}
    .btn {{
      background: var(--btn-bg);
      border: 1px solid var(--btn-border);
      border-radius: 6px;
      color: var(--text-main);
      font-family: var(--font-mono);
      font-size: 10.5px;
      font-weight: 600;
      padding: 6px 11px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: background 0.15s ease, border-color 0.15s ease;
    }}
    .btn:hover {{
      background: var(--btn-hover);
      border-color: var(--accent-cyan);
    }}
    .diagram-container {{
      width: 100%;
      max-width: 1280px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}
    svg {{
      width: 100%;
      height: auto;
      max-width: 1280px;
      background: var(--canvas-bg);
      border: 1px solid var(--canvas-border);
      border-radius: 12px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
      transition: background 0.2s ease, border-color 0.2s ease;
    }}
    .diagram-node {{
      cursor: pointer;
      transition: opacity 0.2s ease, filter 0.2s ease;
    }}
    .diagram-wire {{
      transition: opacity 0.2s ease, stroke-width 0.2s ease;
    }}
    .dimmed {{
      opacity: 0.15 !important;
    }}
    .highlighted {{
      opacity: 1 !important;
      filter: drop-shadow(0 0 10px rgba(6, 182, 212, 0.7));
    }}
    .highlighted-wire {{
      opacity: 1 !important;
      stroke-width: 3.5px !important;
    }}
    .glow-line {{
      stroke-dasharray: 8 4;
      animation: dash 30s linear infinite;
    }}
    @keyframes dash {{
      to {{
        stroke-dashoffset: -1000;
      }}
    }}
    #scale-indicator {{
      margin-top: 10px;
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-size: 11px;
    }}
    /* Modal Shortcuts Dialog */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(4px);
      z-index: 1000;
      justify-content: center;
      align-items: center;
    }}
    .modal-overlay.active {{
      display: flex;
    }}
    .modal-card {{
      background: var(--card-bg);
      border: 1px solid var(--border-base);
      border-radius: 10px;
      padding: 24px;
      max-width: 440px;
      width: 90%;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }}
    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-base);
      padding-bottom: 10px;
    }}
    .modal-title {{
      font-size: 14px;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--text-main);
    }}
    .modal-close {{
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-family: var(--font-mono);
      font-size: 14px;
    }}
    .shortcuts-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .shortcut-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      color: var(--text-muted);
    }}
    kbd {{
      background: var(--toolbar-bg);
      border: 1px solid var(--border-base);
      border-radius: 4px;
      padding: 3px 8px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--accent-cyan);
      font-weight: 700;
    }}
  </style>
</head>
<body>

  <div class="top-bar">
    <div class="eyebrow-title">
      <div class="top-eyebrow">{cat_esc}</div>
      <div class="top-title">{title_esc}</div>
    </div>
    <div class="controls-bar">
      <div class="search-box">
        <input type="text" id="nodeSearch" placeholder="{search_ph}" />
      </div>
      <button class="btn" id="themeToggleBtn" title="{theme_tt}">THEME: DARK</button>
      <button class="btn" id="exportSvgBtn" title="{svg_tt}">SVG</button>
      <button class="btn" id="exportPngBtn" title="{png_tt}">PNG</button>
      <button class="btn" id="helpBtn" title="{help_tt}">?</button>
    </div>
  </div>

  <div class="diagram-container">
    <svg id="diagramSvg" viewBox="0 0 1280 720" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Gradients -->
        <linearGradient id="bgGrad" x1="0" y1="0" x2="1280" y2="720" gradientUnits="userSpaceOnUse">
          <stop stop-color="var(--card-bg)"/>
          <stop offset="1" stop-color="var(--canvas-bg)"/>
        </linearGradient>
        <linearGradient id="blueGlow" x1="0" y1="0" x2="1" y2="0">
          <stop stop-color="#38bdf8"/>
          <stop offset="1" stop-color="#818cf8"/>
        </linearGradient>
        <linearGradient id="emeraldGlow" x1="0" y1="0" x2="1" y2="0">
          <stop stop-color="#10b981"/>
          <stop offset="1" stop-color="#34d399"/>
        </linearGradient>
        <linearGradient id="amberGlow" x1="0" y1="0" x2="1" y2="0">
          <stop stop-color="#f59e0b"/>
          <stop offset="1" stop-color="#fbbf24"/>
        </linearGradient>
        <linearGradient id="roseGlow" x1="0" y1="0" x2="1" y2="0">
          <stop stop-color="#f43f5e"/>
          <stop offset="1" stop-color="#fb7185"/>
        </linearGradient>
        <linearGradient id="indigoGlow" x1="0" y1="0" x2="1" y2="0">
          <stop stop-color="#6366f1"/>
          <stop offset="1" stop-color="#818cf8"/>
        </linearGradient>
        <linearGradient id="purpleGlow" x1="0" y1="0" x2="1" y2="0">
          <stop stop-color="#a855f7"/>
          <stop offset="1" stop-color="#c084fc"/>
        </linearGradient>
        <linearGradient id="slateGlow" x1="0" y1="0" x2="1" y2="0">
          <stop stop-color="#64748b"/>
          <stop offset="1" stop-color="#94a3b8"/>
        </linearGradient>

        <!-- Drop Shadow Filters -->
        <filter id="nodeShadow" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.6"/>
        </filter>
        <!-- Directional Arrowhead Markers -->
        <marker id="arrow-sky" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8"/>
        </marker>
        <marker id="arrow-emerald" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#34d399"/>
        </marker>
        <marker id="arrow-amber" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#fbbf24"/>
        </marker>
        <marker id="arrow-rose" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#fb7185"/>
        </marker>
        <marker id="arrow-purple" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#c084fc"/>
        </marker>
        <marker id="arrow-indigo" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#818cf8"/>
        </marker>
        <marker id="arrow-slate" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- Canvas Frame -->
      <rect x="2" y="2" width="1276" height="716" rx="24" fill="url(#bgGrad)" stroke="var(--border-base)" stroke-width="1.5"/>

      <!-- Header -->
      <g transform="translate({self.padding_x}, 48)">
        <rect width="{cat_badge_w:.1f}" height="24" rx="12" fill="#064e3b" fill-opacity="0.6" stroke="#059669" stroke-width="1"/>
        <text x="{cat_badge_w / 2:.1f}" y="16" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui" letter-spacing="1" text-anchor="middle">{cat_esc}</text>
        <text x="0" y="52" fill="var(--text-main)" font-size="26" font-weight="800" font-family="system-ui">{title_esc}</text>
        <text x="0" y="74" fill="var(--text-muted)" font-size="13" font-family="system-ui">{sub_esc}</text>
      </g>

      {wires_svg}

      {nodes_rendered}

      <!-- Footer Branding -->
      <text x="{self.padding_x}" y="682" fill="var(--text-muted)" font-size="11" font-family="monospace">Diagram Maker Engine • Dynamic Bezier Graph Routing • Zero-Wrap Vector Canvas</text>
    </svg>
  </div>

  <div id="scale-indicator">Auto-Scaling Vector Canvas</div>

  <!-- Modal Trợ Giúp Phím Tắt -->
  <div class="modal-overlay" id="helpModal">
    <div class="modal-card">
      <div class="modal-header">
        <span class="modal-title">{modal_title}</span>
        <button class="modal-close" id="closeModalBtn">ESC</button>
      </div>
      <div class="shortcuts-list">
        <div class="shortcut-row"><span>{sc_search}</span> <kbd>/</kbd></div>
        <div class="shortcut-row"><span>{sc_theme}</span> <kbd>T</kbd></div>
        <div class="shortcut-row"><span>{sc_reset}</span> <kbd>ESC</kbd></div>
        <div class="shortcut-row"><span>{sc_svg}</span> <kbd>Alt + S</kbd></div>
        <div class="shortcut-row"><span>{sc_png}</span> <kbd>Alt + P</kbd></div>
        <div class="shortcut-row"><span>{sc_help}</span> <kbd>?</kbd></div>
      </div>
    </div>
  </div>

  <script>
    (function() {{
      const htmlEl = document.documentElement;
      const svgEl = document.getElementById('diagramSvg');
      const searchInput = document.getElementById('nodeSearch');
      const themeBtn = document.getElementById('themeToggleBtn');
      const exportSvgBtn = document.getElementById('exportSvgBtn');
      const exportPngBtn = document.getElementById('exportPngBtn');
      const helpBtn = document.getElementById('helpBtn');
      const helpModal = document.getElementById('helpModal');
      const closeModalBtn = document.getElementById('closeModalBtn');
      const scaleInd = document.getElementById('scale-indicator');

      // 1. Theme Toggle
      function setTheme(theme) {{
        htmlEl.setAttribute('data-theme', theme);
        themeBtn.textContent = 'THEME: ' + theme.toUpperCase();
        try {{ localStorage.setItem('dm_theme', theme); }} catch(e) {{}}
      }}
      const savedTheme = (function() {{
        try {{ return localStorage.getItem('dm_theme') || '{default_theme}'; }} catch(e) {{ return '{default_theme}'; }}
      }})();
      setTheme(savedTheme);

      themeBtn.addEventListener('click', () => {{
        const cur = htmlEl.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
        setTheme(cur);
      }});

      // 2. Search & Filter
      searchInput.addEventListener('input', (e) => {{
        const q = e.target.value.trim().toLowerCase();
        const nodes = svgEl.querySelectorAll('.diagram-node');
        const wires = svgEl.querySelectorAll('.diagram-wire');

        if (!q) {{
          nodes.forEach(n => n.classList.remove('dimmed', 'highlighted'));
          wires.forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
          return;
        }}

        nodes.forEach(n => {{
          const title = (n.getAttribute('data-title') || '').toLowerCase();
          const text = n.textContent.toLowerCase();
          if (title.includes(q) || text.includes(q)) {{
            n.classList.remove('dimmed');
            n.classList.add('highlighted');
          }} else {{
            n.classList.add('dimmed');
            n.classList.remove('highlighted');
          }}
        }});
        wires.forEach(w => w.classList.add('dimmed'));
      }});

      // 3. Upstream & Downstream Reach Tracing
      let selectedNodeId = null;
      svgEl.addEventListener('click', (e) => {{
        const nodeG = e.target.closest('.diagram-node');
        if (!nodeG) {{
          selectedNodeId = null;
          svgEl.querySelectorAll('.diagram-node').forEach(n => n.classList.remove('dimmed', 'highlighted'));
          svgEl.querySelectorAll('.diagram-wire').forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
          return;
        }}

        const nodeId = nodeG.getAttribute('data-node-id');
        if (selectedNodeId === nodeId) {{
          selectedNodeId = null;
          svgEl.querySelectorAll('.diagram-node').forEach(n => n.classList.remove('dimmed', 'highlighted'));
          svgEl.querySelectorAll('.diagram-wire').forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
          return;
        }}

        selectedNodeId = nodeId;
        const allNodes = svgEl.querySelectorAll('.diagram-node');
        const allWires = svgEl.querySelectorAll('.diagram-wire');

        const connectedNodes = new Set([nodeId]);
        allWires.forEach(w => {{
          const fromId = w.getAttribute('data-from');
          const toId = w.getAttribute('data-to');
          if (fromId === nodeId || toId === nodeId) {{
            w.classList.remove('dimmed');
            w.classList.add('highlighted-wire');
            if (fromId) connectedNodes.add(fromId);
            if (toId) connectedNodes.add(toId);
          }} else {{
            w.classList.add('dimmed');
            w.classList.remove('highlighted-wire');
          }}
        }});

        allNodes.forEach(n => {{
          const nid = n.getAttribute('data-node-id');
          if (connectedNodes.has(nid)) {{
            n.classList.remove('dimmed');
            n.classList.add('highlighted');
          }} else {{
            n.classList.add('dimmed');
            n.classList.remove('highlighted');
          }}
        }});
      }});

      // 4. Client-side SVG & PNG Export
      function exportSvg() {{
        const serializer = new XMLSerializer();
        let source = serializer.serializeToString(svgEl);
        if (!source.includes('xmlns="http://www.w3.org/2000/svg"')) {{
          source = source.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
        }}
        const blob = new Blob(['<?xml version="1.0" standalone="no"?>
', source], {{ type: 'image/svg+xml;charset=utf-8' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = '{title_esc}'.replace(/[^a-zA-Z0-9_-]/g, '_') + '.svg';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      }}

      function exportPng() {{
        const serializer = new XMLSerializer();
        let source = serializer.serializeToString(svgEl);
        const canvas = document.createElement('canvas');
        const scale = 2;
        canvas.width = 1280 * scale;
        canvas.height = 720 * scale;
        const ctx = canvas.getContext('2d');
        ctx.scale(scale, scale);

        const img = new Image();
        const svgBlob = new Blob([source], {{ type: 'image/svg+xml;charset=utf-8' }});
        const url = URL.createObjectURL(svgBlob);

        img.onload = function() {{
          ctx.fillStyle = htmlEl.getAttribute('data-theme') === 'light' ? '#ffffff' : '#070a12';
          ctx.fillRect(0, 0, 1280, 720);
          ctx.drawImage(img, 0, 0);
          URL.revokeObjectURL(url);

          canvas.toBlob(function(blob) {{
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = '{title_esc}'.replace(/[^a-zA-Z0-9_-]/g, '_') + '_retina.png';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
          }}, 'image/png');
        }};
        img.src = url;
      }}

      exportSvgBtn.addEventListener('click', exportSvg);
      exportPngBtn.addEventListener('click', exportPng);

      // 5. Modal & Keyboard Shortcuts
      function toggleHelp(show) {{
        if (show === undefined) helpModal.classList.toggle('active');
        else if (show) helpModal.classList.add('active');
        else helpModal.classList.remove('active');
      }}

      helpBtn.addEventListener('click', () => toggleHelp(true));
      closeModalBtn.addEventListener('click', () => toggleHelp(false));
      helpModal.addEventListener('click', (e) => {{ if (e.target === helpModal) toggleHelp(false); }});

      window.addEventListener('keydown', (e) => {{
        const isInput = e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA';
        if (e.key === 'Escape') {{
          toggleHelp(false);
          searchInput.value = '';
          searchInput.blur();
          searchInput.dispatchEvent(new Event('input'));
          selectedNodeId = null;
          svgEl.querySelectorAll('.diagram-node').forEach(n => n.classList.remove('dimmed', 'highlighted'));
          svgEl.querySelectorAll('.diagram-wire').forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
        }} else if (!isInput) {{
          if (e.key === '/') {{
            e.preventDefault();
            searchInput.focus();
          }} else if (e.key === 't' || e.key === 'T') {{
            e.preventDefault();
            themeBtn.click();
          }} else if (e.key === '?') {{
            e.preventDefault();
            toggleHelp();
          }}
        }}
      }});

      // 6. Scale Indicator
      function updateScale() {{
        const rect = svgEl.getBoundingClientRect();
        const scale = Math.round((rect.width / 1280) * 100);
        if (scaleInd) scaleInd.textContent = ;
      }}
      window.addEventListener('resize', updateScale);
      window.addEventListener('DOMContentLoaded', updateScale);
      updateScale();
    }})();
  </script>
</body>
</html>"""
        return html_output
