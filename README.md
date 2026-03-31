# Deep Research

A personal research workstation for producing deep, high-quality research reports as beautifully typeset PDFs. Built for use with [Claude Code](https://claude.ai/code).

## Quick Start

The primary way to use this repo:

```
/report <topic>
```

That's it. One command produces a complete PDF research report. The `/report` orchestrator handles everything: scaffolding, research planning, parallel deep dives with web search, synthesis, review, and PDF rendering.

## Prerequisites

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** — Python package manager
- **System dependencies for WeasyPrint:**
  - macOS: `brew install pango cairo gdk-pixbuf libffi`
  - Ubuntu/Debian: `apt install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libcairo2 libffi-dev`
  - See [WeasyPrint docs](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) for other platforms

## Setup

```bash
cd deep-research
uv sync
```

## Usage

### Automated (Recommended)

Run in Claude Code:

```
/report quantum computing
/report "The Economics of Space Mining"
/report climate adaptation strategies --template academic
/report neural interfaces --depth deep
```

### Manual Workflow

For more control over each step:

1. **Scaffold**: `/new-research "Topic Name"` or `uv run python scripts/new_research.py "Topic Name"`
2. **Brief**: Edit `research/<project>/brief.md` with your research question and scope
3. **Plan**: `/plan` — generates a structured research plan
4. **Research**: `/deep-dive <subtopic>` — repeat for each area (uses web search)
5. **Write**: `/synthesize` — turns notes into a cohesive report draft
6. **Review**: `/review` — critical review with suggested fixes
7. **Render**: `/render` — produces the final PDF

### Direct Script Usage

```bash
# Scaffold a new project
uv run python scripts/new_research.py "Nuclear Fusion Energy"

# Render to PDF
uv run python scripts/render.py research/nuclear-fusion-energy/report.md

# Render with academic template
uv run python scripts/render.py research/nuclear-fusion-energy/report.md --template academic
```

## Project Structure

```
deep-research/
├── CLAUDE.md                  # Instructions for Claude Code
├── research/                  # Each research project gets a subfolder
│   └── <project>/
│       ├── brief.md           # Research question & scope
│       ├── notes/             # Raw notes, one file per subtopic
│       ├── report.md          # Final markdown report (rendered to PDF)
│       └── output/            # Generated PDFs
├── templates/                 # HTML + CSS templates for PDF rendering
│   ├── default.html           # Clean, professional report template
│   ├── academic.html          # Academic paper style
│   └── assets/style.css       # Shared stylesheet
├── scripts/
│   ├── render.py              # Markdown → PDF renderer
│   ├── new_research.py        # Project scaffolder
│   └── utils/md_extensions.py # Custom markdown extensions
└── .claude/skills/            # Claude Code skills
    ├── report/                # /report — full pipeline orchestrator
    ├── plan/                  # /plan — research planning
    ├── deep-dive/             # /deep-dive — subtopic investigation
    ├── synthesize/            # /synthesize — report drafting
    ├── review/                # /review — critical review
    ├── render/                # /render — PDF generation
    └── new-research/          # /new-research — project scaffolding
```

## Skills

| Skill | Description |
|---|---|
| `/report <topic>` | Full pipeline: topic → PDF. The main entry point. |
| `/plan` | Generate a research plan from a brief |
| `/deep-dive <subtopic>` | Investigate a specific subtopic in depth |
| `/synthesize` | Turn notes into a structured report draft |
| `/review` | Critically review and improve a draft |
| `/render` | Render report.md to PDF |
| `/new-research <topic>` | Scaffold a new research project |

## Templates

- **default** — Clean, professional report with cover page, table of contents, and polished typography
- **academic** — Academic paper style with numbered sections and abstract
