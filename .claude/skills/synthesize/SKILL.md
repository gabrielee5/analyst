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

4. **If `notes/research-plan.md` exists**, use its expected report structure as a guide.

5. **Produce a complete report draft** in `report.md` with:

### YAML Frontmatter
```yaml
---
title: "<Report Title>"
subtitle: "<Descriptive subtitle>"
date: "<today's date>"
author: "Deep Research"
template: "default"
---
```

### Required Sections

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

- **Sources**: All references used, formatted as markdown footnotes (`[^1]`).

### Writing Standards

- **Every paragraph must earn its place.** If you can't articulate why a paragraph exists, cut it.
- **Lead with insight, not summary.** Don't describe what something is — explain what it means.
- **Use concrete language.** Replace "significant" with the actual number. Replace "recently" with the actual date.
- **Vary sentence length.** Short sentences for impact. Longer ones for nuance. Not everything needs to be a list.
- **Prefer prose over bullet points** in the report body. Lists are for quick reference; prose is for analysis.
- **Use markdown features well**: tables, footnotes, admonitions, blockquotes. But don't overdo it — these are accents, not the main course.
- **Target 3,000–5,000 words** for standard-depth reports.

6. **Self-review pass**: Before saving, read through the draft once for flow and coherence. Fix awkward transitions, redundant passages, and weak openings.

7. **Save** as `report.md` in the project folder, overwriting the starter template.
