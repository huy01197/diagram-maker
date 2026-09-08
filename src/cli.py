"""
diagram-maker: Command Line Interface & Unified Dispatcher
Provides commands to compile individual JSON specs or batch process entire specification suites.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from .compiler import GraphCompiler
from .slide_compiler import SlideCompiler

def detect_spec_type(spec_data):
    """Xác định loại spec: 'diagram' nếu có columns/connections, ngược lại là 'slide'"""
    if "columns" in spec_data or "connections" in spec_data:
        return "diagram"
    return "slide"

def compile_spec(spec_data):
    """Biên dịch đối tượng dictionary spec thành mã HTML"""
    spec_type = detect_spec_type(spec_data)
    if spec_type == "diagram":
        compiler = GraphCompiler(spec_data)
        return "diagram", compiler.compile_to_html()
    else:
        compiler = SlideCompiler(spec_data)
        return "slide", compiler.compile_to_html()

def compile_file(input_path, output_path=None):
    """Biên dịch tệp JSON spec sang tệp HTML đích"""
    input_path = Path(input_path).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Khong tim thay tep dac ta: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        spec_data = json.load(f)

    spec_type, html_content = compile_spec(spec_data)

    if output_path is None:
        base_name = input_path.stem
        # Nếu là diagram, gán tiền tố diagram_ nếu chưa có
        if spec_type == "diagram" and not base_name.startswith("diagram_"):
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

def compile_all(repo_root=None):
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

    print(f"=== diagram-maker: Bat dau bien dich {len(spec_files)} dac ta ===")
    for spec_file in spec_files:
        rel_spec = spec_file.relative_to(specs_dir)
        spec_stem = spec_file.stem
        
        # Đặt tên file xuất chuẩn mực trong output/
        if spec_stem.startswith("sample_"):
            out_filename = f"{spec_stem}.html"
        else:
            out_filename = f"diagram_{spec_stem}.html"

        out_path = output_dir / out_filename
        try:
            spec_type, final_path = compile_file(spec_file, out_path)
            print(f"  [OK] [{spec_type.upper()}] {rel_spec} -> output/{out_filename}")
            results.append((spec_file, final_path, True, ""))
        except Exception as e:
            print(f"  [ERROR] {rel_spec}: {str(e)}")
            results.append((spec_file, out_path, False, str(e)))

    success_count = sum(1 for r in results if r[2])
    print(f"=== Hoan tat: {success_count}/{len(results)} tep bien dich thanh cong ===")
    return results

def main():
    parser = argparse.ArgumentParser(
        prog="diagram-maker",
        description="Institutional Vector Flowchart & Architecture Diagram Engine"
    )
    parser.add_argument(
        "spec_file",
        nargs="?",
        help="Duong dan toi tep dac ta JSON can bien dich (tuy chon)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Duong dan tep HTML dau ra (mac dinh: tu dong sinh trong output/)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Bien dich toan bo cac tep dac ta trong thu muc specs/"
    )

    args = parser.parse_args()

    # Trường hợp 1: Chạy biên dịch toàn bộ (--all hoặc không truyền tham số)
    if args.all or args.spec_file is None:
        compile_all()
        return 0

    # Trường hợp 2: Chạy file cụ thể
    input_file = Path(args.spec_file)
    if not input_file.exists():
        print(f"[Loi] Khong tim thay tep: {args.spec_file}", file=sys.stderr)
        return 1

    try:
        spec_type, out_path = compile_file(input_file, args.output)
        print(f"[Thanh cong] [{spec_type.upper()}] Da bien dich: {out_path}")
        return 0
    except Exception as e:
        print(f"[Loi] Bien dich that bai: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
