"""
Super AI Layout & Diagram Engine - Graph Compiler
Chuyển đổi khai báo đồ thị (JSON AST) thành SVG Vector với thuật toán Auto-Layout & Bezier Routing.
Tuân thủ chuẩn Institutional Dark Terminal.
"""

import json
import os
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
        svg.append(f'<g transform="translate({x:.1f}, {y:.1f})" filter="url(#nodeShadow)">')
        
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
        svg.append('<!-- BEZIER DYNAMIC WIRES -->')
        for conn in self.connections:
            src_id = conn.get("from")
            dst_id = conn.get("to")
            
            if src_id not in self.nodes or dst_id not in self.nodes:
                continue

            src = self.nodes[src_id]
            dst = self.nodes[dst_id]

            # Cổng ra (Right side of source)
            x1 = src["x"] + src["width"]
            y1 = src["y"] + src["height"] / 2

            # Cổng vào (Left side of destination - lùi 2.5px để mũi tên tiếp xúc viền chuẩn xác)
            x2 = dst["x"] - 2.5
            y2 = dst["y"] + dst["height"] / 2

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

            classes = ["glow-line"] if is_animated else []
            class_attr = f'class="{" ".join(classes)}"' if classes else ''
            filter_attr = 'filter="url(#glowEffect)"' if is_glow else ''
            width_attr = 'stroke-width="2.2"' if is_animated or is_glow else 'stroke-width="1.6"'
            opacity_attr = 'stroke-opacity="0.9"' if is_animated or is_glow else 'stroke-opacity="0.65"'
            marker_attr = f'marker-end="url(#arrow-{color_name})"'

            svg.append(f'<path d="{path_d}" stroke="{stroke_color}" {width_attr} {opacity_attr} fill="none" {class_attr} {filter_attr} {marker_attr}/>')

        return "\n".join(svg)

    def compile_to_html(self):
        self.calculate_layout()

        # Render tất cả Wires
        wires_svg = self.render_connections()

        # Render tất cả Nodes
        nodes_svg = []
        for n_id, n_layout in self.nodes.items():
            nodes_svg.append(self.render_node(n_id, n_layout))
        nodes_rendered = "\n".join(nodes_svg)

        # Header Category Badge: Thiết kế theo chuẩn Illustrator Extra Width (bán kính rx=12 + 11px padding đối xứng mỗi bên = +46)
        cat_badge_w = len(self.category) * 7.6 + 46
        cat_esc = html.escape(self.category)
        title_esc = html.escape(self.title)
        sub_esc = html.escape(self.subtitle)

        html_output = f"""<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_esc}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{
      background-color: #0a0e17;
      color: #f3f4f6;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      overflow: hidden;
    }}
    .diagram-container {{
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      box-sizing: border-box;
      background: radial-gradient(circle at 50% 40%, #111a2e 0%, #0a0e17 100%);
    }}
    svg {{
      width: 100%;
      height: 100%;
      max-width: 1280px;
      max-height: 720px;
      filter: drop-shadow(0 20px 50px rgba(0, 0, 0, 0.8));
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
      position: fixed;
      bottom: 14px;
      right: 16px;
      background: rgba(0, 0, 0, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #38bdf8;
      font-family: monospace;
      font-size: 12px;
      padding: 6px 12px;
      border-radius: 9999px;
      pointer-events: none;
      z-index: 100;
    }}
  </style>
</head>
<body>

  <div class="diagram-container">
    <svg viewBox="0 0 1280 720" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Gradients -->
        <linearGradient id="bgGrad" x1="0" y1="0" x2="1280" y2="720" gradientUnits="userSpaceOnUse">
          <stop stop-color="#111827"/>
          <stop offset="1" stop-color="#0b1120"/>
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
      <rect x="2" y="2" width="1276" height="716" rx="24" fill="url(#bgGrad)" stroke="#1f2937" stroke-width="1.5"/>

      <!-- Header -->
      <g transform="translate({self.padding_x}, 48)">
        <rect width="{cat_badge_w:.1f}" height="24" rx="12" fill="#064e3b" fill-opacity="0.6" stroke="#059669" stroke-width="1"/>
        <text x="{cat_badge_w / 2:.1f}" y="16" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui" letter-spacing="1" text-anchor="middle">{cat_esc}</text>
        <text x="0" y="52" fill="#ffffff" font-size="26" font-weight="800" font-family="system-ui">{title_esc}</text>
        <text x="0" y="74" fill="#9ca3af" font-size="13" font-family="system-ui">{sub_esc}</text>
      </g>

      {wires_svg}

      {nodes_rendered}

      <!-- Footer Branding -->
      <text x="{self.padding_x}" y="682" fill="#4b5563" font-size="11" font-family="monospace">Super AI Layout Engine • Dynamic Bezier Graph Routing • Zero-Wrap Vector Canvas</text>
    </svg>
  </div>

  <div id="scale-indicator">Auto-Scaling Vector Canvas</div>
  <script>
    function updateScale() {{
      const svg = document.querySelector('svg');
      if (!svg) return;
      const rect = svg.getBoundingClientRect();
      const scale = Math.round((rect.width / 1280) * 100);
      const ind = document.getElementById('scale-indicator');
      if (ind) ind.textContent = `Scale: ${{scale}}% (${{Math.round(rect.width)}}x${{Math.round(rect.height)}})`;
    }}
    window.addEventListener('resize', updateScale);
    window.addEventListener('DOMContentLoaded', updateScale);
    updateScale();
  </script>
</body>
</html>"""
        return html_output

if __name__ == "__main__":
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    spec_path = os.path.join(cur_dir, "sample_diagram_spec.json")
    
    if os.path.exists(spec_path):
        with open(spec_path, "r", encoding="utf-8") as f:
            spec = json.load(f)
    else:
        raise FileNotFoundError(f"Spec file not found: {spec_path}")

    compiler = GraphCompiler(spec)
    out_html = compiler.compile_to_html()
    
    out_path = os.path.join(cur_dir, "generated_diagram.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_html)
        
    print(f"-> Đã biên dịch thành công sơ đồ động: {out_path}")
