"""
diagram-maker Package
Thư viện sinh sơ đồ kiến trúc Vector SVG & HTML chuẩn Institutional Financial Terminal.
"""

from .engine import DiagramEngine, TOPOLOGY_REGISTRY
from .topologies.streaming_topology import StreamingTopologyCompiler
from .topologies.interactive_loop import InteractiveLoopCompiler
from .topologies.medallion_lakehouse import MedallionLakehouseCompiler

__version__ = "2.0.0"
__all__ = [
    "DiagramEngine",
    "StreamingTopologyCompiler",
    "InteractiveLoopCompiler",
    "MedallionLakehouseCompiler",
    "TOPOLOGY_REGISTRY"
]
