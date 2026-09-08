"""
diagram-maker: Slide Presentation Compiler
Renders declarative JSON slide specs into high-contrast glassmorphic presentation canvases.
Compliant with Institutional Financial Terminal aesthetics and zero-emoji design rules.
"""


HTML_SLIDE_TEMPLATE = """<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
  <meta charset="UTF-8">
  <title>__TITLE__</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body, html { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background: #0a0e17; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    #viewport { width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center; position: relative; background: radial-gradient(circle at 50% 50%, #111827 0%, #0a0e17 100%); }
    #canvas { width: 1280px; height: 720px; position: absolute; transform-origin: center center; box-shadow: 0 25px 60px -15px rgba(0,0,0,0.9); border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.08); background: linear-gradient(145deg, #111827 0%, #0b1120 100%); padding: 2.5rem 3rem; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box; }
    .glass-card { background: rgba(17, 24, 39, 0.75); backdrop-filter: blur(14px); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 1rem; }
    #scale-indicator { position: fixed; bottom: 14px; right: 16px; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.15); color: #38bdf8; font-family: monospace; font-size: 12px; padding: 6px 12px; border-radius: 9999px; pointer-events: none; z-index: 100; }
  </style>
</head>
<body>
  <div id="viewport">
    <div id="canvas">
      <div class="flex items-center justify-between">
        <div>
          <span class="text-xs font-bold text-emerald-400 uppercase tracking-widest">__CATEGORY__</span>
          <h2 class="text-3xl font-extrabold text-white mt-1 tracking-tight">__TITLE__</h2>
        </div>
        <span class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-emerald-950/80 text-emerald-300 border border-emerald-700/60">__BADGE__</span>
      </div>
      <div class="grid grid-cols-2 gap-6 my-auto">
        __BRANCHES__
      </div>
      <div class="p-3 bg-gray-900/80 rounded-xl border border-gray-800 flex items-center justify-between text-xs text-gray-300">
        <span class="text-emerald-400 font-semibold">diagram-maker • Vector Slide Engine</span>
        <span class="text-sky-400 font-mono text-[11px]">Zero-Wrap Presentation Canvas</span>
      </div>
    </div>
  </div>
  <div id="scale-indicator">Scale: 100%</div>
  <script>
    const DESIGN_WIDTH = 1280;
    const DESIGN_HEIGHT = 720;
    const canvas = document.getElementById('canvas');
    const indicator = document.getElementById('scale-indicator');
    function resizeCanvas() {
      const scale = Math.min((window.innerWidth - 32) / DESIGN_WIDTH, (window.innerHeight - 32) / DESIGN_HEIGHT);
      const finalScale = Math.max(0.15, Math.min(scale, 1.4));
      canvas.style.transform = `scale(${finalScale})`;
      indicator.textContent = `AutoScale: ${Math.round(finalScale * 100)}% (${window.innerWidth}x${window.innerHeight})`;
    }
    window.addEventListener('resize', resizeCanvas);
    window.addEventListener('DOMContentLoaded', resizeCanvas);
    resizeCanvas();
  </script>
</body>
</html>"""


class SlideCompiler:
    def __init__(self, spec):
        self.spec = spec

    def compile_to_html(self):
        spec = self.spec
        branches_html = ""
        for b in spec.get("branches", []):
            color = b.get("color", "sky")
            border_col = f"border-l-{color}-500"
            text_col = f"text-{color}-400"
            bg_tag = f"bg-{color}-950 text-{color}-300 border-{color}-800/50"

            rules_html = ""
            for r in b.get("rules", []):
                rules_html += f'''
            <div class="p-2.5 rounded-lg bg-gray-900/80 border border-gray-800">
              <div class="font-semibold text-white">{r['title']}</div>
              <div class="text-gray-400 text-[11px] mt-0.5 leading-relaxed">{r['desc']}</div>
            </div>'''

            branches_html += f'''
        <div class="glass-card p-4 space-y-3 border-l-4 {border_col} shadow-lg">
          <div class="{text_col} font-bold text-base flex items-center justify-between pb-1 border-b border-gray-800/80">
            <span>{b['name']}</span>
            <span class="text-[11px] {bg_tag} px-2.5 py-0.5 rounded-md font-mono border">{b['weight']}</span>
          </div>
          <div class="space-y-2 text-xs text-gray-300">
            {rules_html}
          </div>
        </div>'''

        html_out = HTML_SLIDE_TEMPLATE.replace("__TITLE__", spec.get('title', ''))
        html_out = html_out.replace("__CATEGORY__", spec.get('category', ''))
        html_out = html_out.replace("__BADGE__", spec.get('badge', ''))
        html_out = html_out.replace("__BRANCHES__", branches_html)
        return html_out
