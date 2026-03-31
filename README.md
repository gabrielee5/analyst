# Fabietti.xyz — Adaptive Research Analyst

An adaptive research analyst workstation that produces expert-grade research reports as beautifully typeset PDFs. The system **automatically detects the domain** of any topic and adapts its entire pipeline — persona, research strategy, report structure, review criteria, and PDF template — to act as the best analyst for that field.

Built for use with [Claude Code](https://claude.ai/code).

## Quick Start

The primary way to use this repo:

```
/report <topic>
```

That's it. One command produces a complete PDF research report. The `/report` orchestrator handles everything: domain detection, scaffolding, research planning, parallel deep dives with web search, synthesis, review, PDF rendering, and email delivery.

Optional flags:
- `--template default|academic|financial|briefing` — override auto-selected template
- `--depth shallow|standard|deep` — controls research depth (default: standard)
- `--no-email` — skip email delivery

## Prerequisites

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** — Python package manager
- **System dependencies for WeasyPrint:**
  - macOS: `brew install pango cairo gdk-pixbuf libffi`
  - Ubuntu/Debian: `apt install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libcairo2 libffi-dev`
  - See [WeasyPrint docs](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) for other platforms

## Setup

```bash
git clone <repo-url> && cd analyst
uv sync
cp .env.example .env   # then fill in your email credentials
```

## How It Works

The adaptive pipeline classifies your topic into a domain and tailors everything accordingly:

| Domain | Persona | Template |
|--------|---------|----------|
| Financial Analysis | Equity research analyst | financial |
| Market / Industry Analysis | Strategy consultant | financial |
| Geopolitical Analysis | Intelligence analyst | briefing |
| Scientific / Technical Review | Research scientist | academic |
| Historical Analysis | Academic historian | academic |
| Policy Analysis | Policy analyst | briefing |
| Technology Assessment | Technology analyst | default |
| Legal / Regulatory | Legal researcher | default |
| Biomedical / Health | Biomedical researcher | academic |
| Competitive Intelligence | CI analyst | financial |

Each project gets a `domain-profile.md` file (auto-generated) that controls the pipeline: analyst persona, report structure, source priorities, review criteria, and PDF template.

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

1. **Scaffold**: `/new-research "Topic Name"`
2. **Brief**: Edit `research/<project>/brief.md` with your research question and scope
3. **Plan**: `/plan` — generates domain profile + research plan
4. **Research**: `/deep-dive <subtopic>` — repeat for each area (uses web search)
5. **Write**: `/synthesize` — turns notes into a cohesive report draft
6. **Review**: `/review` — critical review with suggested fixes
7. **Render**: `/render` — produces the final PDF and emails it

### Direct Script Usage

```bash
# Scaffold a new project
uv run python scripts/new_research.py "Nuclear Fusion Energy"

# Render to PDF
uv run python scripts/render.py research/nuclear-fusion-energy/report.md

# Render with specific template
uv run python scripts/render.py research/nuclear-fusion-energy/report.md --template academic
```

## Project Structure

```
analyst/
├── CLAUDE.md                  # Instructions for Claude Code
├── .env.example               # Email configuration template
├── research/                  # Each research project gets a subfolder
│   └── <project>/
│       ├── domain-profile.md  # Domain classification & pipeline config (auto-generated)
│       ├── brief.md           # Research question & scope
│       ├── notes/             # Raw notes, one file per subtopic
│       ├── report.md          # Final markdown report (rendered to PDF)
│       └── output/            # Generated PDFs
├── templates/                 # HTML + CSS templates for PDF rendering
│   ├── default.html           # Clean, professional report
│   ├── academic.html          # Academic paper style
│   ├── financial.html         # Equity research / industry analysis
│   ├── briefing.html          # Intelligence / policy briefing
│   └── assets/
│       ├── style.css          # Shared stylesheet
│       └── logo.png           # Header logo
├── scripts/
│   ├── render.py              # Markdown → PDF renderer
│   ├── email_pdf.py           # SMTP email delivery
│   ├── new_research.py        # Project scaffolder
│   └── utils/md_extensions.py # Custom markdown extensions (admonitions, etc.)
└── .claude/skills/            # Claude Code skills
    ├── report/                # /report — full adaptive pipeline
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
| `/report <topic>` | **The main entry point.** Full adaptive pipeline: topic → domain detection → PDF. |
| `/plan` | Generate a domain-aware research plan from a brief |
| `/deep-dive <subtopic>` | Investigate a subtopic in depth with web research |
| `/synthesize` | Turn notes into a domain-structured report draft |
| `/review` | Domain-specific critical review and improvement |
| `/render` | Render report.md to PDF via WeasyPrint |
| `/new-research <topic>` | Scaffold a new research project folder |

## PDF Templates

| Template | Best For | Key Features |
|----------|----------|--------------|
| `default` | Technology, legal, general research | Cover page, clean sections |
| `academic` | Scientific, historical, biomedical | Numbered sections, abstract, bibliography |
| `financial` | Earnings, M&A, industry, competitive intel | Report type label, tight tables, disclaimer footer |
| `briefing` | Geopolitical, policy, intelligence | Key judgments box, confidence badges |

Templates are auto-selected by domain profile. Override with `--template <name>`.

## Email Delivery

After rendering, reports are automatically emailed via SMTP.

- **Configuration:** Copy `.env.example` to `.env` and fill in `EMAIL_RECIPIENT`, `SMTP_USER`, `SMTP_PASSWORD`.
- **Subject format:** `[Fabietti.xyz] <report title>`
- Pass `--no-email` to skip. If sending fails, the render still succeeds — email is best-effort.

## Dependencies

Managed with `uv`. Key packages: weasyprint, markdown, Jinja2, Pygments, pyyaml.
