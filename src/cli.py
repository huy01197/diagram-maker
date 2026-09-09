"""
diagram-maker: Command Line Interface & Unified Dispatcher
Provides commands to compile individual JSON specs, batch process entire specification suites,
and execute deterministic AST validation gates.
"""

import sys
import json
import argparse
from pathlib import Path
from .compiler import GraphCompiler
from .slide_compiler import SlideCompiler
from .engine import DiagramEngine
from .validator import validate_file, validate_all, SpecValidator

def detect_spec_type(spec_data):
    """Xác định loại spec: 'topology' (Topology 2.0 đa dạng), 'diagram' (Cột 4/5-tier), hoặc 'slide'"""
    return SpecValidator.detect_type(spec_data)

def compile_spec(spec_data, theme="dark"):
    """Biên dịch đối tượng dictionary spec thành mã HTML với theme chỉ định"""
    spec_type = detect_spec_type(spec_data)
    if spec_type == "topology":
        engine = DiagramEngine(spec_data)
        topo_name = engine.detect_topology()
        # Pass theme to compiler if supported
        return f"topology:{topo_name}", engine.compile()
    elif spec_type == "diagram":
        compiler = GraphCompiler(spec_data)
        return "diagram", compiler.compile_to_html(default_theme=theme)
    else:
        compiler = SlideCompiler(spec_data)
        return "slide", compiler.compile_to_html()

def compile_file(input_path, output_path=None, theme="dark", skip_validate=False):
    """Biên dịch tệp JSON spec sang tệp HTML đích"""
    input_path = Path(input_path).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Khong tim thay tep dac ta: {input_path}")

    if not skip_validate:
        val_res = validate_file(input_path)
        if not val_res.valid:
            err_msg = "; ".join(val_res.errors)
            raise ValueError(f"Kiem dinh AST that bai cho {input_path.name}: {err_msg}")

    with open(input_path, "r", encoding="utf-8") as f:
        spec_data = json.load(f)

    spec_type, html_content = compile_spec(spec_data, theme=theme)

    if output_path is None:
        base_name = input_path.stem
        if spec_type.startswith("topology"):
            out_name = f"{base_name}.html"
        elif spec_type == "diagram" and not base_name.startswith("diagram_"):
            out_name = f"diagram_{base_name}.html"
        else:
            out_name = f"{base_name}.html"
        output_path = input_path.parent / out_name
    else:
        output_path = Path(output_path).resolve()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return spec_type, output_path

def compile_all(repo_root=None, theme="dark"):
    """Tự động tìm kiếm và biên dịch toàn bộ các file spec trong thư mục specs/"""
    if repo_root is None:
        repo_root = Path(__file__).resolve().parent.parent
    else:
        repo_root = Path(repo_root).resolve()

    specs_dir = repo_root / "specs"
    output_dir = repo_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not specs_dir.exists():
        print(f"[Canh bao] Thu muc specs khong ton tai tai: {specs_dir}")
        return []

    results = []
    spec_files = sorted(specs_dir.rglob("*.json"))

    print(f"=== diagram-maker: Bat dau bien dich {len(spec_files)} dac ta (Theme: {theme.upper()}) ===")
    for spec_file in spec_files:
        rel_spec = spec_file.relative_to(specs_dir)
        spec_stem = spec_file.stem
        
        # Đặt tên file xuất chuẩn mực trong output/
        if spec_stem.startswith("sample_"):
            out_filename = f"{spec_stem}.html"
        elif any(spec_stem == x for x in ["vietnam_stock_heatmap", "telegram_stock_bot", "vietnamese_stock_analysis"]):
            out_filename = f"{spec_stem}.html"
        else:
            out_filename = f"diagram_{spec_stem}.html"

        is_en = "en" in spec_file.parts
        target_dir = (output_dir / "en") if is_en else output_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        out_path = target_dir / out_filename
        try:
            spec_type, final_path = compile_file(spec_file, out_path, theme=theme)
            rel_out = out_path.relative_to(output_dir)
            print(f"  [OK] [{spec_type.upper()}] {rel_spec} -> output/{rel_out}")
            results.append((spec_file, final_path, True, ""))
        except Exception as e:
            print(f"  [ERROR] {rel_spec}: {str(e)}")
            results.append((spec_file, out_path, False, str(e)))

    success_count = sum(1 for r in results if r[2])
    print(f"=== Hoan tat: {success_count}/{len(results)} tep bien dich thanh cong ===")
    return results

def run_validation(target_path=None, repo_root=None):
    """Chạy cổng kiểm định AST và in kết quả bảng chuyên nghiệp"""
    if repo_root is None:
        repo_root = Path(__file__).resolve().parent.parent
    else:
        repo_root = Path(repo_root).resolve()

    if target_path and Path(target_path).is_file():
        results = [validate_file(Path(target_path))]
    else:
        results = validate_all(repo_root)

    print("\n=== diagram-maker: AST & Schema Validation Gate ===")
    print(f"{'SPECIFICATION':<36} {'TYPE':<12} {'NODES/METRICS':<16} {'STATUS'}")
    print("-" * 74)

    all_pass = True
    for r in results:
        file_name = Path(r.spec_path).name
        if len(file_name) > 34:
            file_name = file_name[:31] + "..."
        
        count_str = "-"
        if "nodes_count" in r.stats:
            count_str = f"{r.stats.get('nodes_count', 0)}n / {r.stats.get('connections_count', 0)}e"
        elif "metrics_count" in r.stats:
            count_str = f"{r.stats.get('metrics_count', 0)} metrics"
        elif "branches_count" in r.stats:
            count_str = f"{r.stats.get('branches_count', 0)} branches"

        status_str = "PASS" if r.valid else "FAIL"
        if not r.valid:
            all_pass = False

        print(f"{file_name:<36} {r.spec_type:<12} {count_str:<16} [{status_str}]")
        for err in r.errors:
            print(f"    x ERROR: {err}")
        for warn in r.warnings:
            print(f"    ! WARN:  {warn}")

    print("-" * 74)
    pass_count = sum(1 for r in results if r.valid)
    print(f"Ket qua: {pass_count}/{len(results)} specifications hop le.\n")
    return 0 if all_pass else 1

def main():
    # Kiểm tra lệnh phụ đặc biệt
    if len(sys.argv) > 1 and sys.argv[1] in ["validate", "--validate"]:
        val_parser = argparse.ArgumentParser(
            prog="diagram-maker validate",
            description="Kiem tra tinh toan ven cua tep dac ta JSON AST"
        )
        val_parser.add_argument("spec_file", nargs="?", help="Duong dan tep JSON can kiem tra (bo trong de kiem tra toan bo)")
        val_parser.add_argument("--all", action="store_true", help="Kiem tra toan bo specs")
        args = val_parser.parse_args(sys.argv[2:])
        target = None if args.all else args.spec_file
        return run_validation(target)

    # Parser chuẩn cho biên dịch
    parser = argparse.ArgumentParser(
        prog="diagram-maker",
        description="Institutional Vector Flowchart & Architecture Diagram Engine"
    )
    # Bỏ qua từ khóa 'compile' nếu người dùng gõ: python3 main.py compile <file>
    parse_args_list = sys.argv[1:]
    if parse_args_list and parse_args_list[0] == "compile":
        parse_args_list = parse_args_list[1:]

    parser.add_argument("spec_file", nargs="?", help="Duong dan tep dac ta JSON can bien dich")
    parser.add_argument("-o", "--output", help="Duong dan tep HTML dau ra")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Giao dien mac dinh (dark hoac light)")
    parser.add_argument("--all", action="store_true", help="Bien dich toan bo cac tep dac ta trong thu muc specs/")
    parser.add_argument("--validate", action="store_true", help="Chay kiem tra AST thay vi bien dich")

    args = parser.parse_args(parse_args_list)

    if args.validate:
        return run_validation(args.spec_file)

    if args.all or args.spec_file is None:
        compile_all(theme=args.theme)
        return 0

    input_file = Path(args.spec_file)
    if not input_file.exists():
        print(f"[Loi] Khong tim thay tep: {args.spec_file}", file=sys.stderr)
        return 1

    try:
        spec_type, out_path = compile_file(input_file, args.output, theme=args.theme)
        print(f"[Thanh cong] [{spec_type.upper()}] Da bien dich: {out_path}")
        return 0
    except Exception as e:
        print(f"[Loi] Bien dich that bai: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
