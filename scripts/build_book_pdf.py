#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ENGINE_CANDIDATES = ("tectonic", "xelatex", "lualatex")

FONT_CANDIDATES = {
    "mainfont": (
        "PT Serif",
        "Charter",
        "Athelas",
        "Georgia",
        "Times New Roman",
        "Liberation Serif",
        "DejaVu Serif",
        "Noto Serif",
    ),
    "sansfont": (
        "PT Sans",
        "Helvetica Neue",
        "Arial Unicode MS",
        "Arial",
        "Helvetica",
        "Liberation Sans",
        "DejaVu Sans",
        "Noto Sans",
    ),
    "monofont": (
        "Menlo",
        "Monaco",
        "Courier New",
        "Liberation Mono",
        "DejaVu Sans Mono",
        "Noto Sans Mono",
    ),
}

SYMBOL_REPLACEMENTS = {
    "✅": "[+]",
    "❌": "[-]",
    "⚠️": "[!]",
    "⚠": "[!]",
    "🔄": "[R]",
    "↺": "[R]",
    "↻": "[R]",
    "✓": "[+]",
    "✗": "[-]",
    "❗": "[!]",
    "⭐": "[*]",
    "▶": "->",
    "→": "->",
    "←": "<-",
    "↔": "<->",
    "Σ": "sum",
    "∈": " in ",
    "ℝ": "R",
    " ": " ",
    "₁": "_1",
    "₂": "_2",
    "₃": "_3",
    "₄": "_4",
    "₅": "_5",
    "ₙ": "_n",
}

TABLE_SCALE_WORDS = {
    "$": "низкая",
    "$$": "средняя",
    "$$$": "высокая",
    "$$$$": "очень высокая",
}

TABLE_SCALE_PATTERN = re.compile(r"(?<=\|\s)(\${1,4})(?=\s*\|)")
CURRENCY_PATTERN = re.compile(r"(?<!\\)\$(?=\d)")
LATEX_COMMAND_PATTERN = re.compile(r"[A-Za-z@]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a PDF from a Markdown book without touching the source files.",
    )
    parser.add_argument(
        "--source",
        default="book",
        help="Directory or Markdown file to convert. Default: %(default)s",
    )
    parser.add_argument(
        "--output",
        default=f"{Path.cwd().name}.pdf",
        help="Output PDF path. Default: %(default)s",
    )
    parser.add_argument(
        "--engine",
        default="auto",
        help="PDF engine: auto, tectonic, xelatex, or lualatex. Default: %(default)s",
    )
    parser.add_argument(
        "--no-toc",
        action="store_true",
        help="Disable the generated table of contents.",
    )
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep the temporary sanitized copy after a successful build.",
    )
    parser.add_argument(
        "--margin",
        default="1in",
        help="Page margin passed to LaTeX geometry. Default: %(default)s",
    )
    parser.add_argument(
        "--page-width",
        help="Custom page width (for example: 6in). Use together with --page-height.",
    )
    parser.add_argument(
        "--page-height",
        help="Custom page height (for example: 8in). Use together with --page-width.",
    )
    parser.add_argument(
        "--wrap-code-blocks",
        action="store_true",
        help="Wrap long lines inside code blocks in the generated PDF.",
    )
    parser.add_argument(
        "--code-font-size",
        help="LaTeX font size command for code blocks, for example: footnotesize.",
    )
    return parser.parse_args()


def resolve_engine(requested: str) -> str:
    if requested != "auto":
        if shutil.which(requested):
            return requested
        raise SystemExit(f"PDF engine '{requested}' was not found in PATH.")

    for candidate in ENGINE_CANDIDATES:
        if shutil.which(candidate):
            return candidate

    raise SystemExit(
        "No supported PDF engine found. Install one of: tectonic, xelatex, lualatex."
    )


def ensure_pandoc() -> None:
    if not shutil.which("pandoc"):
        raise SystemExit("pandoc was not found in PATH.")


def resolve_page_geometry(args: argparse.Namespace) -> tuple[str | None, str]:
    has_width = bool(args.page_width)
    has_height = bool(args.page_height)

    if has_width != has_height:
        raise SystemExit("Both --page-width and --page-height must be provided together.")

    if has_width and has_height:
        return None, f"paperwidth={args.page_width},paperheight={args.page_height},margin={args.margin}"

    return "a4", f"margin={args.margin}"


def normalize_latex_command(value: str, *, option_name: str) -> str:
    command = value.lstrip("\\")
    if not command or not LATEX_COMMAND_PATTERN.fullmatch(command):
        raise SystemExit(f"Invalid {option_name} value: {value}")
    return f"\\{command}"


def create_header_include(temp_root: Path, args: argparse.Namespace) -> Path | None:
    fv_options: list[str] = []

    if args.wrap_code_blocks:
        fv_options.extend(["breaklines=true", "breakanywhere=true"])

    if args.code_font_size:
        fv_options.append(
            f"fontsize={normalize_latex_command(args.code_font_size, option_name='--code-font-size')}"
        )

    if not fv_options:
        return None

    header_path = temp_root / "pdf-header.tex"
    header_path.write_text(
        "\n".join(
            [
                r"\IfFileExists{fvextra.sty}{",
                r"\usepackage{fvextra}",
                rf"\fvset{{{','.join(fv_options)}}}",
                r"}{",
                r"}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return header_path


def natural_sort_key(path: Path, root: Path) -> list[tuple[int, object]]:
    key: list[tuple[int, object]] = []
    for part in path.relative_to(root).parts:
        for chunk in re.split(r"(\d+)", part.casefold()):
            if not chunk:
                continue
            if chunk.isdigit():
                key.append((0, int(chunk)))
            else:
                key.append((1, chunk))
    return key


def discover_markdown_files(source: Path) -> tuple[Path, list[Path]]:
    if source.is_file():
        if source.suffix.lower() != ".md":
            raise SystemExit(f"Source file must be Markdown: {source}")
        return source.parent, [source]

    if not source.is_dir():
        raise SystemExit(f"Source path does not exist: {source}")

    files = [
        path
        for path in source.rglob("*.md")
        if ".git" not in path.parts
        and not any(part.startswith(".") for part in path.relative_to(source).parts)
    ]
    files.sort(key=lambda path: natural_sort_key(path, source))

    if not files:
        raise SystemExit(f"No Markdown files found under: {source}")

    return source, files


def ignore_copy_items(_: str, names: list[str]) -> list[str]:
    ignored: list[str] = []
    for name in names:
        if name in {".git", "__pycache__", ".DS_Store"}:
            ignored.append(name)
            continue
        if name.startswith("."):
            ignored.append(name)
    return ignored


def pick_fonts() -> dict[str, str]:
    fc_list = shutil.which("fc-list")
    if not fc_list:
        return {}

    proc = subprocess.run([fc_list], capture_output=True, text=True, check=True)
    installed = proc.stdout

    picked: dict[str, str] = {}
    for key, candidates in FONT_CANDIDATES.items():
        for candidate in candidates:
            if candidate in installed:
                picked[key] = candidate
                break
    return picked


def sanitize_markdown(text: str) -> str:
    for old, new in SYMBOL_REPLACEMENTS.items():
        text = text.replace(old, new)

    sanitized_lines: list[str] = []
    for line in text.splitlines():
        if line.strip() != "$$":
            line = TABLE_SCALE_PATTERN.sub(lambda match: TABLE_SCALE_WORDS[match.group(1)], line)
            line = CURRENCY_PATTERN.sub(r"\\$", line)
        sanitized_lines.append(line)

    trailing_newline = "\n" if text.endswith("\n") else ""
    return "\n".join(sanitized_lines) + trailing_newline


def build_temp_tree(root: Path, markdown_files: list[Path], temp_root: Path) -> tuple[Path, list[Path]]:
    temp_source = temp_root / root.name
    shutil.copytree(root, temp_source, ignore=ignore_copy_items, dirs_exist_ok=True)

    temp_markdown_files: list[Path] = []
    for file_path in markdown_files:
        temp_file = temp_source / file_path.relative_to(root)
        temp_file.write_text(sanitize_markdown(temp_file.read_text(encoding="utf-8")), encoding="utf-8")
        temp_markdown_files.append(temp_file)

    return temp_source, temp_markdown_files


def run_pandoc(
    markdown_files: list[Path],
    source_root: Path,
    output: Path,
    engine: str,
    fonts: dict[str, str],
    toc: bool,
    papersize: str | None,
    geometry: str,
    header_include: Path | None,
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    command = ["pandoc", *[str(path) for path in markdown_files]]
    command.extend(["--resource-path", os.pathsep.join([str(source_root), str(source_root.parent)])])
    if toc:
        command.append("--toc")
    if header_include:
        command.extend(["--include-in-header", str(header_include)])
    command.extend(
        [
            f"--pdf-engine={engine}",
            "-V",
            "documentclass=book",
        ]
    )

    if papersize:
        command.extend(["-V", f"papersize={papersize}"])

    command.extend(["-V", f"geometry:{geometry}"])

    for key in ("mainfont", "sansfont", "monofont"):
        value = fonts.get(key)
        if value:
            command.extend(["-V", f"{key}={value}"])

    command.extend(["-o", str(output)])
    subprocess.run(command, check=True)


def main() -> int:
    args = parse_args()
    ensure_pandoc()

    source = Path(args.source).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    engine = resolve_engine(args.engine)
    fonts = pick_fonts()
    papersize, geometry = resolve_page_geometry(args)
    root, markdown_files = discover_markdown_files(source)

    temp_root = Path(tempfile.mkdtemp(prefix="book-pdf-"))
    build_succeeded = False

    try:
        header_include = create_header_include(temp_root, args)
        temp_source, temp_markdown_files = build_temp_tree(root, markdown_files, temp_root)
        print(f"Source root: {root}")
        print(f"Markdown files: {len(markdown_files)}")
        print(f"PDF engine: {engine}")
        if papersize:
            print(f"Paper size: {papersize}")
        else:
            print(f"Page size: {args.page_width} x {args.page_height}")
        print(f"Geometry: {geometry}")
        if header_include:
            print(f"Header include: {header_include}")
        if fonts:
            for key in ("mainfont", "sansfont", "monofont"):
                if key in fonts:
                    print(f"{key}: {fonts[key]}")
        run_pandoc(
            markdown_files=temp_markdown_files,
            source_root=temp_source,
            output=output,
            engine=engine,
            fonts=fonts,
            toc=not args.no_toc,
            papersize=papersize,
            geometry=geometry,
            header_include=header_include,
        )
        build_succeeded = True
    except subprocess.CalledProcessError as error:
        print(f"PDF build failed with exit code {error.returncode}.", file=sys.stderr)
        print(f"Temporary files kept at: {temp_root}", file=sys.stderr)
        return error.returncode
    finally:
        if build_succeeded and not args.keep_temp:
            shutil.rmtree(temp_root, ignore_errors=True)

    print(f"PDF written to: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
