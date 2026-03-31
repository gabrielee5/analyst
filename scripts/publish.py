#!/usr/bin/env python3
"""Build a static website from published research reports."""

import argparse
import http.server
import shutil
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.utils.md_extensions import make_extensions, extension_configs

RESEARCH_DIR = PROJECT_ROOT / "research"
WEB_TEMPLATES_DIR = PROJECT_ROOT / "templates" / "web"
WEB_ASSETS_DIR = WEB_TEMPLATES_DIR / "assets"
PDF_ASSETS_DIR = PROJECT_ROOT / "templates" / "assets"
SITE_DIR = PROJECT_ROOT / "_site"


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown text."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return meta, body
    return {}, text


def render_markdown_web(md_text: str) -> tuple[str, str]:
    """Convert markdown to HTML for web (with permalink anchors)."""
    configs = extension_configs()
    configs["toc"]["permalink"] = True
    md = markdown.Markdown(
        extensions=make_extensions(),
        extension_configs=configs,
    )
    content = md.convert(md_text)
    toc = getattr(md, "toc", "")
    return content, toc


def collect_reports(publish_all: bool = False) -> list[dict]:
    """Scan research/ for publishable reports. Returns list of report metadata dicts."""
    reports = []
    for report_path in sorted(RESEARCH_DIR.glob("*/report.md")):
        slug = report_path.parent.name
        if slug.startswith("_"):
            continue

        raw = report_path.read_text(encoding="utf-8")
        meta, body = extract_frontmatter(raw)

        if not publish_all and not meta.get("published", False):
            continue

        # Check for existing PDF
        pdf_source = report_path.parent / "output" / f"{slug}.pdf"
        pdf_url = f"/pdfs/{slug}.pdf" if pdf_source.exists() else None

        # Estimate reading time (~250 words per minute)
        word_count = len(body.split())
        reading_min = max(1, round(word_count / 250))

        reports.append({
            "slug": slug,
            "title": meta.get("title", slug.replace("-", " ").title()),
            "subtitle": meta.get("subtitle", ""),
            "date": meta.get("date", ""),
            "author": meta.get("author", "Fabietti.xyz"),
            "template": meta.get("template", "default"),
            "report_type": meta.get("report_type", "Research Report"),
            "domain": meta.get("domain", ""),
            "word_count": word_count,
            "reading_min": reading_min,
            "body": body,
            "pdf_source": pdf_source if pdf_source.exists() else None,
            "pdf_url": pdf_url,
        })

    # Sort by date descending
    reports.sort(key=lambda r: r.get("date", ""), reverse=True)
    return reports


def build(publish_all: bool = False):
    """Build the full static site."""
    reports = collect_reports(publish_all)

    if not reports:
        print("No published reports found. Add 'published: true' to report frontmatter.")
        return

    # Clean and create output directory
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()
    (SITE_DIR / "reports").mkdir()
    (SITE_DIR / "assets").mkdir()
    (SITE_DIR / "pdfs").mkdir()

    # Copy assets
    shutil.copy2(WEB_ASSETS_DIR / "style.css", SITE_DIR / "assets" / "style.css")
    logo_src = PDF_ASSETS_DIR / "logo.png"
    if logo_src.exists():
        shutil.copy2(logo_src, SITE_DIR / "assets" / "logo.png")

    # Set up Jinja2
    env = Environment(loader=FileSystemLoader(str(WEB_TEMPLATES_DIR)))

    # Build each report page
    for report in reports:
        content_html, toc_html = render_markdown_web(report["body"])

        template_name = report["template"]
        try:
            template = env.get_template(f"{template_name}.html")
        except Exception:
            print(f"  Warning: template '{template_name}' not found, falling back to default")
            template = env.get_template("default.html")

        html = template.render(
            content=content_html,
            title=report["title"],
            subtitle=report["subtitle"],
            date=report["date"],
            author=report["author"],
            report_type=report["report_type"],
            domain=report["domain"],
            reading_min=report["reading_min"],
            toc=toc_html,
            pdf_url=report["pdf_url"],
        )

        # Write report page
        report_dir = SITE_DIR / "reports" / report["slug"]
        report_dir.mkdir(parents=True, exist_ok=True)
        (report_dir / "index.html").write_text(html, encoding="utf-8")

        # Copy PDF if available
        if report["pdf_source"]:
            shutil.copy2(report["pdf_source"], SITE_DIR / "pdfs" / f"{report['slug']}.pdf")

        print(f"  Built: /reports/{report['slug']}/")

    # Build index page
    index_template = env.get_template("index.html")
    index_html = index_template.render(
        title="Research Archive",
        subtitle="Expert-grade research reports across finance, technology, geopolitics, and more.",
        reports=reports,
    )
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")

    print(f"\nSite built: {SITE_DIR}/ ({len(reports)} report{'s' if len(reports) != 1 else ''})")


def serve(port: int = 8000):
    """Build the site and serve it locally."""
    build(publish_all=True)

    if not SITE_DIR.exists():
        print("Nothing to serve — build produced no output.", file=sys.stderr)
        sys.exit(1)

    import os
    os.chdir(SITE_DIR)
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(("", port), handler) as httpd:
        print(f"\nServing at http://localhost:{port}  (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


def main():
    parser = argparse.ArgumentParser(description="Build the research website")
    sub = parser.add_subparsers(dest="command", required=True)

    build_parser = sub.add_parser("build", help="Build the static site")
    build_parser.add_argument("--all", action="store_true", help="Publish all reports, not just those marked published: true")

    serve_parser = sub.add_parser("serve", help="Build and serve locally")
    serve_parser.add_argument("--port", type=int, default=8000, help="Port to serve on (default: 8000)")

    args = parser.parse_args()

    if args.command == "build":
        build(publish_all=args.all)
    elif args.command == "serve":
        serve(port=args.port)


if __name__ == "__main__":
    main()
