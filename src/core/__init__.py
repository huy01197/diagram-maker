"""
diagram-maker: Core Package
Base components, color palette, geometry calculations, and visual mockups.
"""

from .palette import (
    BG_DARK, CARD_BG, SUBCARD_BG, BORDER_BASE, BORDER_HIGHLIGHT,
    COLOR_BLUE, COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_PURPLE, COLOR_ROSE, COLOR_SLATE,
    TEXT_MAIN, TEXT_MUTED, TEXT_DIM, THEME_PALETTE
)
from .base import render_svg_defs, render_html_document, render_port_junction
from .geometry import render_pill_badge, compute_bezier_path
from .mockups import render_mini_treemap, render_mini_candlestick_chart, render_mini_multipane_chart

__all__ = [
    "BG_DARK", "CARD_BG", "SUBCARD_BG", "BORDER_BASE", "BORDER_HIGHLIGHT",
    "COLOR_BLUE", "COLOR_CYAN", "COLOR_EMERALD", "COLOR_AMBER", "COLOR_PURPLE", "COLOR_ROSE", "COLOR_SLATE",
    "TEXT_MAIN", "TEXT_MUTED", "TEXT_DIM", "THEME_PALETTE",
    "render_svg_defs", "render_html_document", "render_port_junction",
    "render_pill_badge", "compute_bezier_path",
    "render_mini_treemap", "render_mini_candlestick_chart", "render_mini_multipane_chart"
]
