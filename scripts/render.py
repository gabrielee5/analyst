#!/usr/bin/env python3
"""Render a markdown research report to PDF via WeasyPrint."""

import argparse
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.utils.md_extensions import make_extensions, extension_configs

TEMPLATES_DIR = PROJECT_ROOT / "templates"


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown text. Returns (metadata, body)."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return meta, body
    return {}, text


def render_markdown(md_text: str) -> tuple[str, str]:
    """Convert markdown to HTML. Returns (content_html, toc_html)."""
    md = markdown.Markdown(
        extensions=make_extensions(),
        extension_configs=extension_configs(),
    )
    content = md.convert(md_text)
    toc = getattr(md, "toc", "")
    return content, toc


def render_pdf(md_path: str, template_name: str = "default", output_path: str | None = None):
    """Render a markdown file to PDF."""
    md_file = Path(md_path).resolve()
    if not md_file.exists():
        print(f"Error: {md_file} not found", file=sys.stderr)
        sys.exit(1)

    raw = md_file.read_text(encoding="utf-8")
    meta, body = extract_frontmatter(raw)

    # Metadata with defaults
    title = meta.get("title", md_file.stem.replace("-", " ").replace("_", " ").title())
    subtitle = meta.get("subtitle", "")
    date = meta.get("date", "")
    author = meta.get("author", "Fabietti.xyz")
    report_type = meta.get("report_type", "Research Report")
    template_name = meta.get("template", template_name)

    content_html, toc_html = render_markdown(body)

    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template_file = f"{template_name}.html"
    try:
        template = env.get_template(template_file)
    except Exception:
        print(f"Error: template '{template_file}' not found in {TEMPLATES_DIR}", file=sys.stderr)
        sys.exit(1)

    full_html = template.render(
        content=content_html,
        title=title,
        subtitle=subtitle,
        date=date,
        author=author,
        report_type=report_type,
        toc=toc_html,
    )

    # Determine output path
    if output_path:
        out = Path(output_path).resolve()
    else:
        out_dir = md_file.parent / "output"
        out_dir.mkdir(exist_ok=True)
        slug = md_file.parent.name
        out = out_dir / f"{slug}.pdf"

    # Render PDF
    base_url = str(TEMPLATES_DIR) + "/"
    HTML(string=full_html, base_url=base_url).write_pdf(str(out))

    size_kb = out.stat().st_size / 1024
    print(f"PDF rendered: {out} ({size_kb:.1f} KB)")
    return str(out)


def main():
    parser = argparse.ArgumentParser(description="Render a research report to PDF")
    parser.add_argument("markdown_file", help="Path to the markdown report file")
    available = [p.stem for p in (Path(__file__).resolve().parent.parent / "templates").glob("*.html")]
    parser.add_argument(
        "--template",
        default="default",
        choices=available,
        help=f"Template to use (available: {', '.join(sorted(available))})",
    )
    parser.add_argument("--output", default=None, help="Custom output PDF path")
    args = parser.parse_args()
    render_pdf(args.markdown_file, args.template, args.output)


if __name__ == "__main__":
    main()
