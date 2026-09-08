"""
diagram-maker: Unified Architecture Engine
Bộ điều phối trung tâm tự động phân loại Topology từ tệp JSON AST Spec
và biên dịch thành tài liệu SVG/HTML độc lập chuẩn Institutional Terminal.
"""

import json
import os

from .topologies.streaming_topology import StreamingTopologyCompiler
from .topologies.interactive_loop import InteractiveLoopCompiler
from .topologies.medallion_lakehouse import MedallionLakehouseCompiler

TOPOLOGY_REGISTRY = {
    "streaming": StreamingTopologyCompiler,
    "streaming_topology": StreamingTopologyCompiler,
    "fan_in": StreamingTopologyCompiler,
    
    "interactive_loop": InteractiveLoopCompiler,
    "interactive_closed_loop": InteractiveLoopCompiler,
    "bot_pipeline": InteractiveLoopCompiler,
    
    "medallion": MedallionLakehouseCompiler,
    "medallion_lakehouse": MedallionLakehouseCompiler,
    "columnar_lakehouse": MedallionLakehouseCompiler,
}

class DiagramEngine:
    def __init__(self, spec_data):
        if isinstance(spec_data, str):
            if os.path.exists(spec_data):
                with open(spec_data, "r", encoding="utf-8") as f:
                    self.spec = json.load(f)
            else:
                self.spec = json.loads(spec_data)
        else:
            self.spec = spec_data

    def detect_topology(self):
        """Tự động phát hiện topology từ metadata hoặc từ cấu trúc dữ liệu"""
        explicit = self.spec.get("topology") or self.spec.get("type")
        if explicit and explicit.lower() in TOPOLOGY_REGISTRY:
            return explicit.lower()

        # Suy luận từ tiêu đề hoặc nội dung
        title = self.spec.get("title", "").lower()
        if "heatmap" in title or "streaming" in title:
            return "streaming"
        elif "bot" in title or "telegram" in title or "interactive" in title:
            return "interactive_loop"
        elif "analysis" in title or "parquet" in title or "lakehouse" in title or "medallion" in title:
            return "medallion_lakehouse"

        return "streaming"

    def compile(self, output_path=None):
        """Biên dịch spec thành mã HTML"""
        topo_type = self.detect_topology()
        compiler_cls = TOPOLOGY_REGISTRY.get(topo_type, StreamingTopologyCompiler)
        
        compiler = compiler_cls(self.spec)
        html_output = compiler.compile()

        if output_path:
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_output)

        return html_output
