"""
diagram-maker: Institutional Vector Flowchart & Architecture Diagram Engine
Auto-layouts declarative JSON specs into 100% vector SVG/HTML canvases with dynamic Bezier wiring.
"""

from .compiler import GraphCompiler, COLOR_PALETTE
from .slide_compiler import SlideCompiler
from .cli import compile_spec, compile_file

__version__ = "1.0.0"
__all__ = ["GraphCompiler", "SlideCompiler", "compile_spec", "compile_file", "COLOR_PALETTE"]
