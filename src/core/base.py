"""
diagram-maker: Base Template & SVG Definitions Engine
Cung cấp khung chứa SVG, hệ thống lưới dotGrid, bộ lọc phát sáng,
và các mẫu thẻ chuẩn Institutional Financial Terminal.
"""

from .palette import (
    BG_DARK, COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_PURPLE, COLOR_BLUE
)

def render_svg_defs():
    """Tạo khối <defs> chứa toàn bộ pattern lưới điểm, marker mũi tên và filter"""
    return f"""
      <defs>
        <!-- Background Dot Grid Pattern -->
        <pattern id="dotGrid" width="24" height="24" patternUnits="userSpaceOnUse">
          <circle cx="12" cy="12" r="1.1" fill="rgba(255, 255, 255, 0.07)" />
        </pattern>

        <!-- Arrow Markers -->
        <marker id="arrow-cyan" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{COLOR_CYAN}" />
        </marker>
        <marker id="arrow-emerald" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{COLOR_EMERALD}" />
        </marker>
        <marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{COLOR_AMBER}" />
        </marker>
        <marker id="arrow-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{COLOR_PURPLE}" />
        </marker>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{COLOR_BLUE}" />
        </marker>
        
        <!-- Glow Filters -->
        <filter id="blueGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="emeraldGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="2.5" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>
    """

def render_html_document(title, eyebrow, metrics, svg_body, footer_notes, width=1320, height=915):
    """Bao bọc toàn bộ SVG trong khung HTML độc lập với phong cách Terminal tối cao cấp"""
    
    metrics_html = ""
    for m in metrics:
        color = m.get("color", "#38bdf8")
        metrics_html += f"""
      <div class="metric-pill">
        <div class="metric-label">{m.get('label', '')}</div>
        <div class="metric-value" style="color: {color};">{m.get('value', '')}</div>
      </div>"""

    footer_html = ""
    for note in footer_notes:
        color = note.get("color", "#06b6d4")
        footer_html += f"""
    <div class="note-card">
      <div class="note-title"><span style="color: {color};">&bull;</span> {note.get('title', '')}</div>
      <div class="note-desc">{note.get('desc', '')}</div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: #070a12;
      --card-bg: #0c121e;
      --border-base: #1b253b;
      --text-main: #e2e8f0;
      --text-muted: #8b9bb4;
      --accent-cyan: #06b6d4;
      --accent-emerald: #089981;
      --accent-amber: #f59e0b;
      --accent-purple: #a855f7;
      --accent-rose: #f23645;
      --accent-blue: #2962ff;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --font-mono: "Geist Mono", "SF Mono", Menlo, Consolas, monospace;
    }}
    body {{
      background-color: var(--bg);
      color: var(--text-main);
      font-family: var(--font-sans);
      display: flex;
      justify-content: center;
      align-items: flex-start;
      min-height: 100vh;
      padding: 24px 16px;
    }}
    .container {{
      width: 100%;
      max-width: 1360px;
    }}
    .header {{
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      border-bottom: 1px solid var(--border-base);
      padding-bottom: 14px;
    }}
    .eyebrow {{
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent-cyan);
      margin-bottom: 4px;
      font-weight: 600;
    }}
    .title {{
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
    }}
    .metrics-bar {{
      display: flex;
      gap: 12px;
    }}
    .metric-pill {{
      background: #0d1424;
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 6px 14px;
      text-align: right;
    }}
    .metric-label {{
      font-family: var(--font-mono);
      font-size: 9.5px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .metric-value {{
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      margin-top: 2px;
    }}
    .svg-wrapper {{
      background: #080c16;
      border: 1px solid var(--border-base);
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    }}
    svg {{
      display: block;
      width: 100%;
      height: auto;
    }}
    .footer-notes {{
      margin-top: 18px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }}
    .note-card {{
      background: #0a0e1a;
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 12px 14px;
    }}
    .note-title {{
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .note-desc {{
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.45;
    }}
  </style>
</head>
<body>

<div class="container">
  <div class="header">
    <div>
      <div class="eyebrow">{eyebrow}</div>
      <h1 class="title">{title}</h1>
    </div>
    <div class="metrics-bar">
      {metrics_html}
    </div>
  </div>

  <div class="svg-wrapper">
    <svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
      {render_svg_defs()}
      
      <!-- Background with Dot Grid -->
      <rect width="{width}" height="{height}" fill="{BG_DARK}" />
      <rect width="{width}" height="{height}" fill="url(#dotGrid)" />

      {svg_body}
    </svg>
  </div>

  <div class="footer-notes">
    {footer_html}
  </div>
</div>

</body>
</html>
"""
