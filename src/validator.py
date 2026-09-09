"""
diagram-maker: Deterministic AST & Specification Validator
Validates JSON specifications for structural correctness, schema conformance,
node ID uniqueness, and connection integrity (eliminating dangling pointers).
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Tuple

class ValidationResult:
    def __init__(self, spec_path: str = ""):
        self.spec_path = spec_path
        self.valid = True
        self.spec_type = "unknown"
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.stats: Dict[str, Any] = {}

    def add_error(self, message: str):
        self.valid = False
        self.errors.append(message)

    def add_warning(self, message: str):
        self.warnings.append(message)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "spec_path": str(self.spec_path),
            "valid": self.valid,
            "spec_type": self.spec_type,
            "errors": self.errors,
            "warnings": self.warnings,
            "stats": self.stats
        }

    def __repr__(self) -> str:
        status = "PASS" if self.valid else "FAIL"
        return f"<ValidationResult {status} type={self.spec_type} errors={len(self.errors)} warnings={len(self.warnings)}>"


class SpecValidator:
    @staticmethod
    def detect_type(spec: Dict[str, Any]) -> str:
        if "topology" in spec:
            return "topology"
        if "columns" in spec or "connections" in spec:
            return "diagram"
        if "branches" in spec or "sections" in spec or "rules" in spec:
            return "slide"
        return "unknown"

    @classmethod
    def validate(cls, spec_data: Dict[str, Any], spec_path: str = "") -> ValidationResult:
        result = ValidationResult(spec_path)
        
        if not isinstance(spec_data, dict):
            result.add_error("Root element must be a JSON object.")
            return result

        spec_type = cls.detect_type(spec_data)
        result.spec_type = spec_type

        if not spec_data.get("title"):
            result.add_warning("Specification missing 'title' field.")

        if spec_type == "diagram":
            cls._validate_diagram(spec_data, result)
        elif spec_type == "topology":
            cls._validate_topology(spec_data, result)
        elif spec_type == "slide":
            cls._validate_slide(spec_data, result)
        else:
            result.add_error("Unrecognized specification schema: neither columns, topology, nor slide structures found.")

        return result

    @classmethod
    def _validate_diagram(cls, spec: Dict[str, Any], result: ValidationResult):
        columns = spec.get("columns", [])
        connections = spec.get("connections", [])
        
        if not columns:
            result.add_error("Diagram specification requires at least one column in 'columns'.")

        node_ids = set()
        duplicate_ids = set()
        total_nodes = 0

        for col_idx, col in enumerate(columns):
            if not isinstance(col, dict):
                result.add_error(f"Column at index {col_idx} is not an object.")
                continue
            
            nodes = col.get("nodes", [])
            for node in nodes:
                total_nodes += 1
                node_id = node.get("id")
                if not node_id:
                    result.add_error(f"Node in column '{col.get('title', col_idx)}' missing 'id' field.")
                else:
                    if node_id in node_ids:
                        duplicate_ids.add(node_id)
                    node_ids.add(node_id)

                if not node.get("title"):
                    result.add_warning(f"Node '{node_id}' missing 'title' field.")

        if duplicate_ids:
            result.add_error(f"Duplicate node IDs detected: {', '.join(sorted(duplicate_ids))}")

        # Connection integrity check (eliminate dangling pointers)
        valid_connections = 0
        for conn_idx, conn in enumerate(connections):
            from_node = conn.get("from") or conn.get("from_node")
            to_node = conn.get("to") or conn.get("to_node")

            if not from_node:
                result.add_error(f"Connection at index {conn_idx} missing source 'from' node.")
            elif from_node not in node_ids:
                result.add_error(f"Dangling connection: source node '{from_node}' does not exist.")

            if not to_node:
                result.add_error(f"Connection at index {conn_idx} missing target 'to' node.")
            elif to_node not in node_ids:
                result.add_error(f"Dangling connection: target node '{to_node}' does not exist.")

            if from_node and to_node and from_node in node_ids and to_node in node_ids:
                valid_connections += 1

        result.stats = {
            "columns_count": len(columns),
            "nodes_count": total_nodes,
            "connections_count": len(connections),
            "valid_connections": valid_connections
        }

    @classmethod
    def _validate_topology(cls, spec: Dict[str, Any], result: ValidationResult):
        topology_name = spec.get("topology")
        valid_topologies = {"streaming", "streaming_topology", "fan_in", "interactive_loop", 
                            "interactive_closed_loop", "bot_pipeline", "medallion", 
                            "medallion_lakehouse", "columnar_lakehouse"}
        
        if topology_name and topology_name.lower() not in valid_topologies:
            result.add_warning(f"Unknown topology '{topology_name}'. Engine will fallback to heuristic detection.")

        metrics = spec.get("metrics", [])
        if not isinstance(metrics, list):
            result.add_error("'metrics' must be an array of objects.")
        
        footer_notes = spec.get("footer_notes", [])
        if not isinstance(footer_notes, list):
            result.add_error("'footer_notes' must be an array of objects.")

        result.stats = {
            "topology": topology_name or "inferred",
            "metrics_count": len(metrics) if isinstance(metrics, list) else 0,
            "footer_notes_count": len(footer_notes) if isinstance(footer_notes, list) else 0
        }

    @classmethod
    def _validate_slide(cls, spec: Dict[str, Any], result: ValidationResult):
        branches = spec.get("branches", [])
        rules = spec.get("rules", [])
        
        result.stats = {
            "branches_count": len(branches) if isinstance(branches, list) else 0,
            "rules_count": len(rules) if isinstance(rules, list) else 0
        }


def validate_file(file_path: Path) -> ValidationResult:
    path = Path(file_path).resolve()
    if not path.exists():
        res = ValidationResult(str(path))
        res.add_error(f"File not found: {path}")
        return res

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        res = ValidationResult(str(path))
        res.add_error(f"JSON Syntax Error: {str(e)}")
        return res
    except Exception as e:
        res = ValidationResult(str(path))
        res.add_error(f"Read error: {str(e)}")
        return res

    return SpecValidator.validate(data, str(path))


def validate_all(repo_root: Path = None) -> List[ValidationResult]:
    if repo_root is None:
        repo_root = Path(__file__).resolve().parent.parent
    specs_dir = repo_root / "specs"
    if not specs_dir.exists():
        return []

    results = []
    for p in sorted(specs_dir.rglob("*.json")):
        results.append(validate_file(p))
    return results
