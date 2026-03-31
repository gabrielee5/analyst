# Fabietti.xyz — Research Workstation

## What This Repo Is

The Fabietti.xyz research workstation for producing deep, high-quality research reports as beautifully typeset PDFs. All reports are branded as Fabietti.xyz publications. Pick any subject, do rigorous research, and get a polished PDF report.

## Primary Workflow

**One command does everything:**

```
/report <topic>
```

This runs the full pipeline: scaffolds the project → generates a brief → creates a research plan → spawns parallel sub-agents for deep dives → synthesizes everything into a report → reviews and polishes → renders the final PDF. You sit back and get a finished report.

## Manual Workflow (More Control)

For when you want to drive each step yourself:

1. `/new-research "Topic Name"` — scaffold the project folder
2. Edit `brief.md` — define the research question and scope
3. `/plan` — generate a research plan from the brief
4. `/deep-dive <subtopic>` — investigate each subtopic (repeat as needed)
5. `/synthesize` — turn notes into a structured report draft
6. `/review` — critically review and improve the draft
7. `/render` — render report.md to PDF

## Key Commands

```bash
# Scaffold a new research folder
uv run python scripts/new_research.py "Topic Name"

# Render a report to PDF (default template)
uv run python scripts/render.py research/<project>/report.md

# Render with academic template
uv run python scripts/render.py research/<project>/report.md --template academic

# Render with custom output path
uv run python scripts/render.py research/<project>/report.md --output ~/Desktop/report.pdf
```

## Skills Reference

This repo ships with custom Claude Code skills in `.claude/skills/`:

| Skill | Description |
|---|---|
| `/report <topic>` | **THE MAIN SKILL.** Full pipeline: topic → PDF. Spawns parallel sub-agents. |
| `/plan` | Generate a research plan from a brief |
| `/deep-dive <subtopic>` | Investigate a specific subtopic with thorough web research |
| `/synthesize` | Turn accumulated notes into a structured report draft |
| `/review` | Critically review and improve a draft |
| `/render` | Render report.md to PDF via WeasyPrint |
| `/new-research <topic>` | Scaffold a new research project folder |

## Research Conventions

### Project Structure
Each research project lives in `research/<slug>/` with:
- `brief.md` — research question, scope, objectives (fill this first)
- `notes/` — one file per source or subtopic (raw research)
- `report.md` — the final report (single source of truth, gets rendered to PDF)
- `output/` — generated PDFs

### Working with Research
- Always start by reading `brief.md` to understand scope.
- Keep notes organized: one file per subtopic or source in `notes/`.
- `report.md` is the single source of truth — it's what gets rendered.
- Use markdown features well: tables, footnotes, admonitions, blockquotes for citations.
- Every significant claim needs a source. Use footnotes (`[^1]`) or inline links.

## Writing Style Guidelines

- **Clear, precise, analytical prose.** Not academic jargon, not blog-style fluff.
- **Lead with insight, not summary.** Every section should have a "so what."
- **Use concrete data.** Replace "significant growth" with the actual number. Replace "recently" with the date.
- **Acknowledge uncertainty.** Present conflicting evidence fairly. Don't paper over debates.
- **Structure matters:** Executive Summary → Context → Deep Analysis (multiple sections) → Implications → Open Questions → Sources.
- **Every paragraph earns its place.** If you can't say why a paragraph exists, cut it.

## Report Markdown Features

Use these in `report.md`:

- **Tables**: for data comparisons (rendered with clean styling)
- **Footnotes**: `[^1]` for source citations
- **Admonitions**: `!!! insight "Key Insight"` with indented body for callout boxes
- **Blockquotes**: for important citations (styled with accent border)
- **Code blocks**: fenced with language identifier for syntax highlighting
- **Horizontal rules**: `---` for section breaks

## Email Delivery

After rendering a PDF, it is automatically emailed via Gmail SMTP.

- **Default:** ON. Pass `--no-email` to `/render` or `/report` to skip.
- **Configuration:** set `EMAIL_RECIPIENT`, `SMTP_USER`, and `SMTP_PASSWORD` in `.env` (see `.env.example`).
- **Default sender:** `gabriele@fabietti.xyz` via Namecheap Private Email (SMTP: `mail.privateemail.com`).
- **Backup sender:** Gmail SMTP (commented out in `.env`, swap to use).
- **Subject format:** `[Fabietti.xyz] <report title>`
- **Script:** `uv run python scripts/email_pdf.py <pdf-path> [--subject "..."] [--to "..."]`
- If sending fails, the render still succeeds — email is best-effort.

## PDF Rendering

The renderer (`scripts/render.py`) converts markdown → HTML → PDF:
1. Extracts YAML frontmatter (title, subtitle, date, author, template)
2. Converts markdown to HTML via Python-Markdown with extensions
3. Feeds HTML into a Jinja2 template (default.html or academic.html)
4. Renders to PDF via WeasyPrint

Templates live in `templates/`. The CSS is in `templates/assets/style.css`.

## Dependencies

Managed with `uv`. Key packages: weasyprint, markdown, Jinja2, Pygments, pyyaml.

System deps for WeasyPrint (macOS): `brew install pango cairo gdk-pixbuf libffi`
