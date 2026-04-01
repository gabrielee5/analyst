---
name: synthesize
description: Synthesize research notes into a cohesive, well-structured report draft. Use when the user has accumulated notes and wants to write the report, or says "write the report", "draft it", "put it together", or "synthesize".
---

# Report Synthesis

You turn accumulated research notes into a polished, cohesive report. This skill is called by the `/report` orchestrator or used standalone.

## Instructions

1. **Find the active project.** Look for the most recently modified project in `research/`, or ask.

2. **Read ALL files in `notes/`** to understand the full scope of research.

3. **Read `brief.md`** to re-anchor on the original research question and scope.

4. **Read `domain-profile.md`** if it exists. This is your primary structural guide — it determines report structure, writing style, and template. If it does not exist, use the default structure below.

5. **Produce a complete report draft** in `report.md`:

### YAML Frontmatter
```yaml
---
title: "<Report Title>"
subtitle: "<Descriptive subtitle appropriate to the report type>"
date: "<today's date>"
author: "Fabietti.xyz"
template: "<from domain-profile.md, or 'default'>"
report_type: "<from domain-profile.md, e.g. 'Equity Research Note', 'Intelligence Briefing'>"
---
```

### Report Structure

**If `domain-profile.md` exists:** Use its **Report Structure** as your outline. The sections listed there replace the default structure entirely. Follow them in order. Each numbered item becomes an H2 section.

**If no domain profile exists (fallback):** Use this default structure:

- **Executive Summary**: The single most important page. What did we find and why does it matter? Write this LAST but place it first. It should stand alone — a busy reader who reads only this section should get the core message.

- **Context / Background**: Set the scene. Why does this topic matter now? What's the current state of affairs? Keep it concise — don't over-explain things the target reader already knows.

- **Deep Analysis** (multiple H2 sections): The meat of the report. Each section covers a major aspect. Guidelines:
  - Lead with the insight, not the description. "X is happening" is weak; "X is happening, which means Y" is strong.
  - Use data, examples, and comparisons generously.
  - Acknowledge uncertainty and conflicting evidence — don't paper over debates.
  - Flow logically from one section to the next. Use transitions.
  - Use tables where data comparisons are clearer in tabular form.
  - Use blockquotes sparingly for particularly important citations.
  - Use admonitions (`!!! insight "Key Insight"`) for standout findings.

- **Implications**: So what? What does this mean for the reader, the field, or the future?

- **Open Questions**: What remains unresolved or worth watching? These should be genuine unknowns, not rhetorical questions.

- **Sources**: All references as numbered markdown footnotes (`[^1]`, `[^2]`, etc.). See citation rules below.

### Citation Rules (Mandatory)

Every report must use **inline numbered footnotes** for all significant factual claims. This is non-negotiable — it is the house style.

1. **Add `[^N]` markers inline** at every specific data point, financial figure, date, quote, production number, or sourced claim throughout the body text. Aim for 25-40 footnotes in a standard report.
2. **Create matching `[^N]:` definitions** in a `## Sources and References` section at the very end of the report.
3. **Footnote definitions must be concise**: Author/Publication, "Article Title" (Year) or brief description. No URLs in the footnote text — keep them clean.
4. **Number sequentially** from `[^1]` onwards. Every `[^N]` in the body must have exactly one matching definition, and vice versa.
5. **Never use a prose bullet list of sources.** No "### Sources Consulted" sections with dashes. Every source must be a numbered footnote referenced from the text.
6. **Use the research notes** in `notes/` to find the correct source for each claim — the notes have detailed citations with URLs.
7. **Do not over-cite**: obvious context and common knowledge don't need footnotes. But every specific number, quote, or non-obvious fact does.

**Example of correct style in body text:**
```
Bethlehem produced over 60% of Allied finished artillery and guns.[^5] Revenue surged from $135 million to $1.33 billion.[^6]
```

**Example of correct footnote definitions:**
```
[^5]: Lehigh University Environmental Initiative, "Bethlehem Steel."
[^6]: FundingUniverse, "History of Bethlehem Steel Corporation."
```

### Writing Standards

**If `domain-profile.md` exists:** Adopt its **Writing Style** guidance. Match the tone, density, and conventions specified. For example:
- Financial reports: data-heavy, forward-looking, lead with the thesis
- Intelligence briefings: confidence-calibrated, distinguish assessed from confirmed
- Academic/scientific: measured, methodical, properly citing prior work
- Historical: narrative-driven where appropriate, acknowledge historiographic debates

**Always apply these universal standards regardless of domain:**
- **Every paragraph must earn its place.** If you can't articulate why a paragraph exists, cut it.
- **Lead with insight, not summary.** Don't describe what something is — explain what it means.
- **Use concrete language.** Replace "significant" with the actual number. Replace "recently" with the actual date.
- **Vary sentence length.** Short sentences for impact. Longer ones for nuance. Not everything needs to be a list.
- **Prefer prose over bullet points** in the report body. Lists are for quick reference; prose is for analysis.
- **Use markdown features well**: tables, footnotes, admonitions, blockquotes. But don't overdo it — these are accents, not the main course.
- **Use domain-appropriate admonitions**: `!!! insight` for general insights, `!!! thesis` for investment theses, `!!! judgment` for intelligence assessments, `!!! finding` for key findings.
- **Target 3,000–5,000 words** for standard-depth reports.

6. **Generate a chart specification** alongside the report. Data-rich reports need visualizations — not just tables. After writing `report.md`, create a file called `charts.json` in the project folder that specifies every chart the report needs.

   **When to include charts:** Any report that contains quantitative data over time, comparisons between entities, or progression/decline narratives should include charts. Most reports will benefit from 3-10 charts. Skip charts only if the report is purely qualitative (e.g., a legal analysis with no numeric data).

   **Chart spec format** (`charts.json`):
   ```json
   [
     {
       "id": "revenue_arc",
       "title": "Company Revenue (1990-2024)",
       "type": "line",
       "section_anchor": "## Financial Performance",
       "placement": "before_table",
       "data": {
         "x": [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024],
         "y": [1.2, 2.3, 4.5, 6.1, 5.8, 7.2, 8.9, 10.1]
       },
       "labels": {"x": "", "y": "Revenue ($B)"},
       "annotations": {"2000": "IPO", "2020": "COVID dip"},
       "color": "#2563eb"
     }
   ]
   ```

   **Supported chart types:**
   - `line` — time series, trends, progressions (fill_between area shading by default)
   - `bar` — comparisons, discrete data points (green for positive, red for negative when data includes both)
   - `grouped_bar` — multi-series comparisons (provide `data.series` as list of `{label, values}`)
   - `dual_line` — two related time series on the same axes (provide `data.y2`, `labels.y2`, `color2`)

   **Rules for chart specs:**
   - Every chart needs an `id` (used for the filename: `{id}.png`)
   - `section_anchor` is the markdown heading where the chart should be inserted (exact match)
   - `placement` is either `"before_table"` (insert before the first table in that section), `"after_heading"` (insert right after the heading), or `"before_paragraph:N"` (before the Nth paragraph)
   - Data must be numeric — extract exact values from the research notes. Do not use placeholder data.
   - `annotations` is optional — use it to label key events on the chart (keys are x-values, values are labels)
   - Keep `title` concise (under 60 chars). The chart title is rendered on the figure itself.
   - Use domain-appropriate colors: blue (`#2563eb`) for primary data, red (`#dc2626`) for negative/losses, green (`#16a34a`) for positive/gains, purple (`#7c3aed`) for stock prices, orange (`#ea580c`) for secondary metrics.

   **What makes a good chart spec:**
   - Revenue/earnings/stock price over time (line)
   - Profit/loss bars showing swings between positive and negative (bar)
   - Market share comparisons (grouped_bar)
   - Employment/production volume trends (line)
   - Competitive comparisons across entities (grouped_bar or dual_line)
   - Any data table in the report with 5+ rows of numeric time-series data is a candidate for a chart

7. **Self-review pass**: Before saving, read through the draft once for flow and coherence. Fix awkward transitions, redundant passages, and weak openings.

8. **Save** `report.md` in the project folder (overwriting the starter template) and `charts.json` alongside it.
