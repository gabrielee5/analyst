---
name: render
description: Render a research report to PDF. Use when the user wants to generate, export, or create a PDF from the report, or says "render", "make the PDF", "export PDF", or "generate PDF".
---

# PDF Renderer

You render research reports from markdown to PDF using WeasyPrint.

## Instructions

1. **Determine the active project.** Check for the most recently modified project in `research/`, or ask the user.

2. **Verify `report.md` exists** in the project folder and has valid YAML frontmatter (title, date, template).

3. **Run the render script:**
   ```bash
   uv run python scripts/render.py research/<project>/report.md
   ```

   Optional flags:
   - `--template academic` — use the academic template
   - `--output <path>` — custom output path

   Or use the bundled wrapper:
   ```bash
   bash .claude/skills/render/scripts/render_wrapper.sh research/<project>
   ```

4. **If the render succeeds**: report the output file path and size.

5. **If the render fails**, diagnose the issue. Common problems:
   - **Missing WeasyPrint system deps** (pango, cairo, gdk-pixbuf): suggest `brew install pango cairo gdk-pixbuf libffi` on macOS or the equivalent on Linux.
   - **Malformed markdown**: broken tables, unclosed code blocks, bad frontmatter YAML.
   - **Missing frontmatter**: the script expects `---` delimited YAML at the top of the file.
   - **Encoding issues**: ensure the file is UTF-8.
   Fix the issue and retry.

6. **Email delivery** (default: ON, skip with `--no-email`):
   - After a successful render, email the PDF by running:
     ```bash
     uv run python scripts/email_pdf.py <pdf-path> --subject "[Fabietti.xyz] <report title>"
     ```
   - Recipient and SMTP credentials are configured in `.env`.
   - If sending fails (missing credentials, network error), warn the user but do NOT fail the render — the PDF is still on disk.
   - Print status after success: `📧 PDF emailed to <address>`

7. After successful render, tell the user the output path and offer to re-render with a different template.
