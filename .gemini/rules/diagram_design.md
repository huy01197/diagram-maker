# Diagram Maker Architecture Design Rules

Whenever generating or modifying diagrams, topologies, specifications, SVG markup, or documents in this codebase:

1. Virtual Port Coupling Pattern:
   - For cross-tier connections in narrow corridors, decouple them into Virtual Port Junctions using `render_port_junction(cx, cy, port_id, label, color=None, is_source=True, text_pos="bottom")`.
   - Supported port IDs: "A", "B", "C", "D", "E", "F", etc.
   - Use `PORT_PALETTE` in `src/core/palette.py` (Purple for logic/quant, Emerald for real-time/lakehouse sync, Cyan for ingestion/memory, Amber for failover/polling, Blue for gateway, Rose for circuit breaker/risk).
   - Maintain staggered label positions (top vs bottom) and at least 30px vertical separation between adjacent ports.

2. Symmetrical Geometry & Tight-Fit Canvas:
   - Never put static text headers on the background. Shift cards up to y=35.
   - Symmetrical margin standard: top margin = 35px, bottom margin = 35px, left/right margin = 45px.
   - Set canvas height tightly: Height = y_max + 35px. Eliminate dead space inside the SVG canvas so footer notes attach cleanly with margin-top: 18px.

3. Micro-Typography:
   - File paths (e.g. `download_history.json`) must be rendered in separate monospace chips with background `#1e293b` and safe margin >= 40px to prevent text clipping.
   - Titles must be concise (<= 50 chars). Eyebrow must be a short uppercase taxonomy tag.

4. Viewport:
   - Keep `.container` at `max-width: 1540px` in `src/core/base.py` for 1:1 unscaled desktop display.
   - Portal `iframe` height in `Product/index.html` should match canvas height (~1080px).

5. Institutional Financial Terminal Standards:
   - Strictly ZERO EMOJIS across all UI, titles, code, logs, and documentation.
   - Use data-driven colors only (Emerald, Rose, Amber, Purple, Cyan, Blue).
