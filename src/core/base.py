"""
diagram-maker: Base Template & SVG Definitions Engine
Cung cấp khung chứa SVG, hệ thống lưới dotGrid, bộ lọc phát sáng,
bộ điều khiển giao diện đa chế độ (Dark/Light), tìm kiếm thành phần,
truy vết luồng dữ liệu (Reach Tracing) và xuất bản ảnh trực tiếp từ trình duyệt.
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
          <circle cx="12" cy="12" r="1.1" fill="currentColor" opacity="0.08" />
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

def render_html_document(title, eyebrow, metrics, svg_body, footer_notes, width=1320, height=915, default_theme="dark"):
    """Bao bọc toàn bộ SVG trong khung HTML độc lập với bộ điều khiển Institutional Interactive Viewer"""
    
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
      <div class="note-title"><span style="color: {color}; font-size: 14px;">&bull;</span> {note.get('title', '')}</div>
      <div class="note-desc">{note.get('desc', '')}</div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="vi" data-theme="{default_theme}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
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
      display: flex;
      justify-content: center;
      align-items: flex-start;
      min-height: 100vh;
      padding: 24px 16px;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}
    .container {{
      width: 100%;
      max-width: 1360px;
    }}
    .header {{
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      border-bottom: 1px solid var(--border-base);
      padding-bottom: 14px;
      gap: 16px;
      flex-wrap: wrap;
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
      color: var(--text-main);
    }}
    .controls-bar {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .search-box {{
      position: relative;
    }}
    .search-box input {{
      background: var(--toolbar-bg);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      color: var(--text-main);
      font-family: var(--font-mono);
      font-size: 11px;
      padding: 7px 12px;
      width: 160px;
      outline: none;
      transition: width 0.2s ease, border-color 0.2s ease;
    }}
    .search-box input:focus {{
      width: 210px;
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
      padding: 7px 12px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: background 0.15s ease, border-color 0.15s ease;
    }}
    .btn:hover {{
      background: var(--btn-hover);
      border-color: var(--accent-cyan);
    }}
    .metrics-bar {{
      display: flex;
      gap: 10px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}
    .metric-pill {{
      background: var(--toolbar-bg);
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
      background: var(--canvas-bg);
      border: 1px solid var(--canvas-border);
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 20px 40px rgba(0,0,0,0.25);
      position: relative;
      transition: background 0.2s ease, border-color 0.2s ease;
    }}
    svg {{
      display: block;
      width: 100%;
      height: auto;
      color: var(--dot-grid-color);
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
    .footer-notes {{
      margin-top: 18px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }}
    .note-card {{
      background: var(--card-bg);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 12px 14px;
      transition: background 0.2s ease, border-color 0.2s ease;
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

<div class="container">
  <div class="header">
    <div>
      <div class="eyebrow">{eyebrow}</div>
      <h1 class="title">{title}</h1>
    </div>
    <div class="controls-bar">
      <div class="search-box">
        <input type="text" id="nodeSearch" placeholder="Tìm thành phần... (/)" />
      </div>
      <button class="btn" id="themeToggleBtn" title="Chuyển đổi Sáng/Tối (Phím T)">THEME: DARK</button>
      <button class="btn" id="exportSvgBtn" title="Xuất mã nguồn SVG">SVG</button>
      <button class="btn" id="exportPngBtn" title="Xuất ảnh PNG Retina 2x">PNG</button>
      <button class="btn" id="helpBtn" title="Phím tắt (?)">?</button>
    </div>
  </div>

  <div class="metrics-bar">
    {metrics_html}
  </div>

  <div class="svg-wrapper">
    <svg id="diagramSvg" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
      {render_svg_defs()}
      
      <!-- Background with Dot Grid -->
      <rect width="{width}" height="{height}" fill="var(--canvas-bg)" />
      <rect width="{width}" height="{height}" fill="url(#dotGrid)" />

      {svg_body}
    </svg>
  </div>

  <div class="footer-notes">
    {footer_html}
  </div>
</div>

<!-- Modal Trợ Giúp Phím Tắt -->
<div class="modal-overlay" id="helpModal">
  <div class="modal-card">
    <div class="modal-header">
      <span class="modal-title">PHÍM TẮT ĐIỀU KHIỂN (VIEWER SHORTCUTS)</span>
      <button class="modal-close" id="closeModalBtn">ESC</button>
    </div>
    <div class="shortcuts-list">
      <div class="shortcut-row"><span>Tìm kiếm thành phần</span> <kbd>/</kbd></div>
      <div class="shortcut-row"><span>Chuyển đổi giao diện Sáng / Tối</span> <kbd>T</kbd></div>
      <div class="shortcut-row"><span>Hủy chọn / Đặt lại bộ lọc</span> <kbd>ESC</kbd></div>
      <div class="shortcut-row"><span>Xuất ảnh Vector SVG</span> <kbd>Alt + S</kbd></div>
      <div class="shortcut-row"><span>Xuất ảnh Raster PNG 2x</span> <kbd>Alt + P</kbd></div>
      <div class="shortcut-row"><span>Mở bảng trợ giúp này</span> <kbd>?</kbd></div>
    </div>
  </div>
</div>

<script>
  // Institutional Interactive Engine (Zero External Dependencies)
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

    // 1. Theme Management
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
      const nodes = svgEl.querySelectorAll('.diagram-node, g[filter="url(#nodeShadow)"]');
      const wires = svgEl.querySelectorAll('.diagram-wire, path[stroke]');

      if (!q) {{
        nodes.forEach(n => n.classList.remove('dimmed', 'highlighted'));
        wires.forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
        return;
      }}

      nodes.forEach(n => {{
        const text = n.textContent.toLowerCase();
        if (text.includes(q)) {{
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
        // Reset selection when clicking outside
        selectedNodeId = null;
        svgEl.querySelectorAll('.diagram-node, g[filter]').forEach(n => n.classList.remove('dimmed', 'highlighted'));
        svgEl.querySelectorAll('.diagram-wire, path[stroke]').forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
        return;
      }}

      const nodeId = nodeG.getAttribute('data-node-id');
      if (selectedNodeId === nodeId) {{
        selectedNodeId = null;
        svgEl.querySelectorAll('.diagram-node, g[filter]').forEach(n => n.classList.remove('dimmed', 'highlighted'));
        svgEl.querySelectorAll('.diagram-wire, path[stroke]').forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
        return;
      }}

      selectedNodeId = nodeId;
      const allNodes = svgEl.querySelectorAll('.diagram-node');
      const allWires = svgEl.querySelectorAll('.diagram-wire');

      if (allWires.length > 0) {{
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
      }}
    }});

    // 4. Client-side SVG & PNG Export
    function exportSvg() {{
      const serializer = new XMLSerializer();
      let source = serializer.serializeToString(svgEl);
      if (!source.includes('xmlns="http://www.w3.org/2000/svg"')) {{
        source = source.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
      }}
      const blob = new Blob(['<?xml version="1.0" standalone="no"?>\\r\\n', source], {{ type: 'image/svg+xml;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = '{title}'.replace(/[^a-zA-Z0-9_-]/g, '_') + '.svg';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }}

    function exportPng() {{
      const serializer = new XMLSerializer();
      let source = serializer.serializeToString(svgEl);
      const vb = svgEl.viewBox.baseVal;
      const w = (vb && vb.width) ? vb.width : {width};
      const h = (vb && vb.height) ? vb.height : {height};

      const canvas = document.createElement('canvas');
      const scale = 2; // 2x Retina quality
      canvas.width = w * scale;
      canvas.height = h * scale;
      const ctx = canvas.getContext('2d');
      ctx.scale(scale, scale);

      const img = new Image();
      const svgBlob = new Blob([source], {{ type: 'image/svg+xml;charset=utf-8' }});
      const url = URL.createObjectURL(svgBlob);

      img.onload = function() {{
        ctx.fillStyle = htmlEl.getAttribute('data-theme') === 'light' ? '#ffffff' : '#070a12';
        ctx.fillRect(0, 0, w, h);
        ctx.drawImage(img, 0, 0);
        URL.revokeObjectURL(url);

        canvas.toBlob(function(blob) {{
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = '{title}'.replace(/[^a-zA-Z0-9_-]/g, '_') + '_retina.png';
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
        svgEl.querySelectorAll('.diagram-node, g[filter]').forEach(n => n.classList.remove('dimmed', 'highlighted'));
        svgEl.querySelectorAll('.diagram-wire, path[stroke]').forEach(w => w.classList.remove('dimmed', 'highlighted-wire'));
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
  }})();
</script>
</body>
</html>
"""
