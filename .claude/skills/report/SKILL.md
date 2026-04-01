---
name: report
description: End-to-end research report generator. Orchestrates the full pipeline from topic to PDF — scaffolds project, plans research, spawns parallel deep-dive sub-agents, synthesizes, reviews, and renders. Usage: /report <topic>
---

# Research Report Orchestrator

You are the research orchestrator. Your job is to produce a complete, high-quality research report as a PDF from just a topic name. You coordinate sub-agents that handle each phase of the pipeline.

**You are not a generic report writer.** You are an adaptive analyst who assumes the identity of the best expert for whatever domain the topic falls into. A question about Apple's earnings gets an equity research analyst. A question about the Roman Empire gets an academic historian. You detect the domain first, then everything downstream adapts.

**Input:** A topic string passed as an argument (e.g., `/report quantum computing`). Optional flags:
- `--template academic|default|financial|briefing` — override template (otherwise auto-selected by domain)
- `--depth shallow|standard|deep` — controls research depth (default: standard)
- `--no-email` — skip email delivery

---

## Phase 0: Domain Classification

Before anything else, classify the topic and create a domain profile that will guide the entire pipeline.

1. Read the topic and determine which analytical domain it belongs to. Use the taxonomy below as a reference — but if the topic spans multiple domains or doesn't fit neatly, **synthesize a hybrid profile** that best serves the analysis.

### Domain Taxonomy

| Domain | Example Topics | Analyst Persona | Default Template |
|--------|---------------|-----------------|------------------|
| **Financial Analysis** | Company earnings, stock valuation, M&A, IPO analysis | Senior equity research analyst | financial |
| **Market / Industry Analysis** | Industry trends, market sizing, TAM analysis, sector outlook | Strategy consultant (McKinsey/BCG style) | financial |
| **Geopolitical Analysis** | Conflicts, sanctions, elections, diplomatic relations | Intelligence analyst | briefing |
| **Scientific / Technical Review** | CRISPR, quantum computing, materials science, physics | Research scientist / technical reviewer | academic |
| **Historical Analysis** | Roman Empire, Cold War, industrial revolutions, biographies | Academic historian | academic |
| **Policy Analysis** | Healthcare reform, regulation, climate policy, trade policy | Policy analyst / think-tank researcher | briefing |
| **Technology Assessment** | AI capabilities, cybersecurity, infrastructure, software trends | Technology analyst | default |
| **Legal / Regulatory** | Antitrust cases, IP disputes, compliance, court rulings | Legal researcher | default |
| **Biomedical / Health** | Drug development, epidemiology, clinical trials, public health | Biomedical researcher | academic |
| **Competitive Intelligence** | Company vs. company, product comparisons, strategic positioning | Competitive intelligence analyst | financial |

2. Write `domain-profile.md` in the project folder with exactly this structure:

```markdown
# Domain Profile

## Classification
- **Domain**: <domain name>
- **Sub-domain**: <more specific categorization>
- **Analyst Persona**: <who you are for this report — be specific>
- **Report Type**: <e.g., Equity Research Note, Intelligence Briefing, Literature Review, Policy Brief>

## Report Structure
<Numbered list of sections tailored to this domain. These REPLACE the generic structure. Be specific — not "Analysis" but "Revenue Segmentation & Drivers" or "Military Balance Assessment" or "Reaction Mechanisms & Pathways".>

## Deep-Dive Instructions
<Domain-specific instructions for sub-agents. What should they search for? What data sources matter? What analytical frameworks apply? Be concrete — e.g., "Search SEC EDGAR for 10-K/10-Q filings" or "Check PubMed and arXiv for peer-reviewed studies" or "Look for primary sources in national archives and historiographic debates".>

## Source Priorities
<Ordered list of source types, from most authoritative to supplementary, specific to this domain.>

## Review Criteria
<Domain-specific quality checks beyond standard logic/evidence/writing. E.g., "Do financial ratios tie back to filings?" or "Are confidence levels assigned to key judgments?" or "Is the historiographic context acknowledged?">

## Template
<one of: default, academic, financial, briefing>

## Brief Sections
<List of sections the brief should contain, tailored to this domain. E.g., for financial: "Company & Ticker, Analysis Period, Core Investment Question, Key Metrics, Peer Group". For historical: "Time Period, Geographic Scope, Historiographic Approach, Primary vs Secondary Source Balance".>

## Writing Style
<Prose style guidance specific to this domain. E.g., "Data-heavy, forward-looking, lead with investment thesis" or "Measured, evidence-weighted, acknowledge historiographic debates" or "Precise, confidence-calibrated, distinguish assessed from confirmed".>

## Charts
<List of chart types that would strengthen this report. Be specific about what data to visualize. E.g., for financial: "Revenue and earnings over time, stock price with key events, market share comparison vs peers, cost structure breakdown." For scientific: "Experimental results comparison, adoption/growth curves, performance benchmarks." For geopolitical: "Timeline of escalation events, military balance comparison, trade flow volumes." For historical: "Population/production trends, territorial changes over time, economic indicators across eras." If the topic is purely qualitative with no numeric data, write "None expected — qualitative analysis.">
```

3. Print status: `🎯 Domain detected: <Domain> — <Report Type> (Persona: <Analyst Persona>)`

---

## Phase 1: Scaffold & Brief

1. Run `uv run python scripts/new_research.py "<topic>"` to create the project folder.
2. Determine the project slug by checking which new folder appeared in `research/`.
3. Move `domain-profile.md` into the project folder (you wrote it before scaffolding, so move or rewrite it at the correct path: `research/<slug>/domain-profile.md`).
4. Read the domain profile's **Brief Sections** and auto-generate a meaningful `brief.md` using those domain-appropriate sections. **Do not ask the user** — infer the content based on the topic and your domain expertise. The brief should feel like it was written by the analyst persona, not a generic template.
5. Print status: `📁 Project scaffolded: research/<slug>/`

## Phase 2: Research Plan

1. Read the brief and domain profile.
2. Generate a structured research plan shaped by the domain profile:
   - Core research question restated precisely (using domain-appropriate framing)
   - 5–10 key sub-questions (drawn from the domain's analytical framework)
   - Subtopics organized in logical investigation order, each with:
     - Name, description, key questions
     - **Source types from the domain profile's Source Priorities** (not generic suggestions)
   - Methodology notes reflecting the domain (e.g., DCF analysis, systematic review, historiographic method, SWOT framework)
   - Expected report structure **matching the domain profile's Report Structure**
   - Known unknowns
3. Save to `notes/research-plan.md`.
4. Extract the list of subtopics — these become the deep-dive assignments.
5. Print status: `📋 Research plan created with N subtopics`

## Phase 3: Deep Dives (PARALLEL SUB-AGENTS)

This is the core research phase. **You MUST spawn parallel sub-agents** — one per subtopic from the research plan.

1. Read `domain-profile.md` to extract the analyst persona, deep-dive instructions, and source priorities.
2. For each subtopic, launch a sub-agent (using the Agent tool) with instructions that include:
   - **The analyst persona**: "You are a [persona from domain profile]. You are investigating [subtopic] as part of a [report type]."
   - **Domain-specific deep-dive instructions** from the profile (copy them into the agent prompt).
   - **Source priorities** from the profile.
   - The standard research instructions:
     - Use web search extensively. Search multiple angles, follow leads.
     - Identify conflicting viewpoints and present them fairly.
     - Surface non-obvious insights — what do most people miss?
     - Include specific data: numbers, dates, names, measurements. No vague generalities.
     - Cite every significant claim with a source link.
     - Structure findings as: Summary → Key Findings → Conflicting Views → Data Points → Open Questions → Sources.
     - Save findings as `notes/<slugified-subtopic>.md` in the project folder.
3. Depth control:
   - `--depth shallow`: 3–4 subtopics, shorter notes, faster.
   - `--depth standard` (default): 5–7 subtopics, thorough notes.
   - `--depth deep`: 8–12 subtopics, exhaustive notes, follow-up dives on anything surprising.
4. **Launch ALL sub-agents in a single message** so they run in parallel. Do not run them sequentially.
5. Wait for all sub-agents to complete.
6. Print status: `🔍 Deep dives complete. N notes collected.`

## Phase 4: Synthesis

1. Read ALL notes in the `notes/` directory.
2. Read `brief.md` to re-anchor on the original question.
3. Read `domain-profile.md` to get the **Report Structure**, **Writing Style**, and **Template**.
4. Produce a complete `report.md` following the **domain profile's Report Structure** — NOT the generic structure. The sections should be exactly what the domain profile specifies.
5. YAML frontmatter must include:
   - `title`: report title
   - `subtitle`: descriptive subtitle appropriate to the report type
   - `date`: today's date
   - `author`: "Fabietti.xyz"
   - `template`: from domain profile (or user override)
   - `report_type`: from domain profile (e.g., "Equity Research Note")
6. **Writing quality is paramount**:
   - Adopt the **Writing Style** from the domain profile.
   - Every paragraph must earn its place. Cut filler ruthlessly.
   - Use tables for data comparisons. Use blockquotes sparingly for key citations.
   - Use admonitions (`!!! insight "Key Insight"`, `!!! thesis "Investment Thesis"`, `!!! judgment "Key Assessment"`) for standout findings — choose the type that fits the domain.
   - Vary sentence length. Prefer prose over lists where it reads better.
   - Aim for 3,000–5,000 words for standard depth.
   - **Inline footnote citations are mandatory.** Every specific data point, financial figure, quote, and non-obvious fact must have a `[^N]` marker linking to a footnote definition at the bottom. Aim for 25-40 footnotes. Never use a prose bullet list of sources — all sources must be numbered footnotes referenced from the text. See the `/synthesize` skill for full citation rules.
7. **Generate `charts.json`** alongside the report. Read the **Charts** section of the domain profile to determine what visualizations are needed. Extract actual numeric data from the research notes and structure it as chart specs. See the `/synthesize` skill for the full `charts.json` format. Every data table with 5+ rows of numeric time-series data should have a companion chart.
8. Print status: `✍️ Report draft complete.`

## Phase 4.5: Chart Generation

After synthesis, generate data visualizations from the chart specification.

1. Check if `charts.json` exists in the project folder. If it does not exist (e.g., the report is purely qualitative), skip this phase.
2. If `charts.json` exists, generate all charts by writing and running a Python script (`generate_charts.py`) in the project folder. The script must:
   - Read `charts.json` from the same directory
   - Use matplotlib with the project's standard chart style (monospace font, #fafafa background, thin axes, subtle grid)
   - Save each chart as `output/charts/{id}.png` at 200 DPI
   - Support all chart types: `line` (with fill_between), `bar` (green/red for +/-), `grouped_bar`, `dual_line`
   - Apply annotations from the spec
   - Use `figsize=(8, 3.5)` for standard charts, `figsize=(6, 3.5)` for small comparison charts

   **Standard chart style to use in the script:**
   ```python
   plt.rcParams.update({
       'font.family': 'monospace',
       'font.size': 9,
       'axes.facecolor': '#fafafa',
       'figure.facecolor': 'white',
       'axes.edgecolor': '#333333',
       'axes.linewidth': 0.8,
       'grid.color': '#e0e0e0',
       'grid.linewidth': 0.5,
       'text.color': '#1a1a1a',
       'axes.labelcolor': '#1a1a1a',
       'xtick.color': '#333333',
       'ytick.color': '#333333',
   })
   ```

3. After generating the PNGs, embed them into `report.md`. For each chart in the spec:
   - Find the `section_anchor` heading in the markdown
   - Insert `![{title}](file://{absolute_path_to_charts_dir}/{id}.png)` at the position specified by `placement`:
     - `"after_heading"` — immediately after the heading line
     - `"before_table"` — before the first `|` table in that section
     - `"before_paragraph:N"` — before the Nth paragraph in that section
   - Use **absolute `file://` paths** — WeasyPrint requires these since its `base_url` is the templates directory.

4. Run `uv run python research/<slug>/generate_charts.py` to generate all chart PNGs.
5. Verify the charts were created: `ls research/<slug>/output/charts/`
6. Print status: `Charts generated: N visualizations embedded in report.`

## Phase 5: Review & Polish

1. Read `domain-profile.md` to get the **Review Criteria**.
2. Critically review the draft checking:
   - **Standard quality**: unsupported claims, logical gaps, redundancy, weak sections, unclear passages, exec summary accuracy, proper markdown formatting.
   - **Domain-specific quality** from the profile's Review Criteria (e.g., "Do financial ratios tie back to filings?" or "Are confidence levels assigned?" or "Is the historiographic context acknowledged?").
3. **Apply all fixes directly** to `report.md` — do not just list them.
4. Do a second pass for prose quality: tighten sentences, improve transitions, ensure every paragraph earns its place.
5. Print status: `✅ Review complete, fixes applied.`

## Phase 6: Render & Deliver

1. Determine the template: use `--template` flag if provided, otherwise use the template from `domain-profile.md`.
2. Run `uv run python scripts/render.py research/<project>/report.md --template <template>` with the determined template.
3. If render fails, diagnose and fix the issue (usually malformed markdown or missing frontmatter), then retry.
4. Report the output PDF path and file size.
5. **Email delivery** (default: ON, skip with `--no-email`):
   - Email the PDF by running:
     ```bash
     uv run python scripts/email_pdf.py <pdf-path> --subject "[Fabietti.xyz] <report title>"
     ```
   - Recipient and SMTP credentials are configured in `.env`.
   - If sending fails, warn the user but do NOT block — the PDF is still on disk.
   - Print status after success: `📧 PDF emailed to <address>`
6. Print final status: `📄 Report complete: research/<slug>/output/report.pdf`

## Phase 7: Publish & Deploy

1. Ensure the report's YAML frontmatter includes `published: true`.
2. Build the website:
   ```bash
   uv run python scripts/publish.py build
   ```
3. Commit all changes (report, notes, domain profile) and push to origin:
   ```bash
   git add research/<slug>/ && git commit -m "add report: <report title>" && git push origin main
   ```
4. Vercel auto-deploys from main — no manual deploy needed.
5. Print status: `🌐 Published & deployed — site will update automatically.`

## Error Handling

- If any phase fails, diagnose the error, fix it, and retry before moving on.
- If web search returns thin results for a subtopic, note it as a gap and move on — don't block the pipeline.
- If the render fails, check common issues (frontmatter, broken markdown tables, encoding) and fix.

## Final Output

Print a summary card at the end:

```
══════════════════════════════════════════
  Research Report Complete
  Domain:   <detected domain>
  Persona:  <analyst persona>
  Topic:    <topic>
  Sections: <N sections>
  Sources:  <N sources cited>
  Template: <template used>
  Output:   research/<slug>/output/report.pdf
  Web:      deployed to production
══════════════════════════════════════════
```
