---
name: publish
description: Build the static research website from published reports and optionally serve locally. Use when the user says "publish", "build the site", "update the website", or wants to deploy reports to the web.
disable-model-invocation: true
---

# Web Publisher

You build the static research website from all reports marked `published: true`.

## Instructions

1. Run the build:
   ```bash
   uv run python scripts/publish.py build
   ```
   To include all reports (even those without `published: true`):
   ```bash
   uv run python scripts/publish.py build --all
   ```

2. Report the number of reports built and the output path (`_site/`).

3. If the user wants to preview locally:
   ```bash
   uv run python scripts/publish.py serve
   ```
   This builds the site and starts a local server at http://localhost:8000.

4. **Deploy:** After a successful build, commit any new or changed reports and push to trigger Vercel auto-deploy:
   ```bash
   git add research/ && git commit -m "publish reports" && git push origin main
   ```
   Vercel auto-deploys from main — no manual `vercel deploy` needed.

5. Print status: `🌐 Published & deployed — site will update automatically.`

## Notes

- Reports need `published: true` in their YAML frontmatter to be included (unless `--all` is used).
- PDFs are automatically included if they exist in the report's `output/` directory.
- The site is output to `_site/` at the project root.
- Templates are in `templates/web/` and match the PDF template variants (default, academic, financial, briefing).
- Vercel is connected to the GitHub repo and auto-deploys on every push to main.
