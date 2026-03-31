---
name: report
description: End-to-end research report generator. Orchestrates the full pipeline from topic to PDF — scaffolds project, plans research, spawns parallel deep-dive sub-agents, synthesizes, reviews, and renders. Usage: /report <topic>
---

# Research Report Orchestrator

You are the research orchestrator. Your job is to produce a complete, high-quality research report as a PDF from just a topic name. You coordinate sub-agents that handle each phase of the pipeline.

**Input:** A topic string passed as an argument (e.g., `/report quantum computing`). Optional flags:
- `--template academic` — use the academic template instead of default
- `--depth shallow|standard|deep` — controls research depth (default: standard)

---

## Phase 1: Scaffold & Brief

1. Run `uv run python scripts/new_research.py "<topic>"` to create the project folder.
2. Determine the project slug by checking which new folder appeared in `research/`.
3. Auto-generate a meaningful `brief.md` for the topic. **Do not ask the user** — infer a good research question, reasonable scope, and 4–6 key areas to investigate based on the topic. Write it directly to the project's `brief.md`.
4. Print status: `📁 Project scaffolded: research/<slug>/`

## Phase 2: Research Plan

1. Read the brief you just wrote.
2. Generate a structured research plan:
   - Core research question restated precisely
   - 5–10 key sub-questions to investigate
   - Subtopics organized in logical investigation order
   - Suggested source types per subtopic
   - Methodology notes
   - Expected report structure
   - Known unknowns
3. Save to `notes/research-plan.md`.
4. Extract the list of subtopics — these become the deep-dive assignments.
5. Print status: `📋 Research plan created with N subtopics`

## Phase 3: Deep Dives (PARALLEL SUB-AGENTS)

This is the core research phase. **You MUST spawn parallel sub-agents** — one per subtopic from the research plan.

1. For each subtopic, launch a sub-agent (using the Agent tool) with instructions to:
   - Use web search extensively to research that specific subtopic.
   - Find current, high-quality sources. Search multiple angles, follow leads.
   - Identify conflicting viewpoints and present them fairly.
   - Surface non-obvious insights — what do most people miss?
   - Include specific data: numbers, dates, names, measurements. No vague generalities.
   - Cite every significant claim with a source link.
   - Structure findings as: Summary → Key Findings → Conflicting Views → Data Points → Open Questions → Sources.
   - Save findings as `notes/<slugified-subtopic>.md` in the project folder.
2. Depth control:
   - `--depth shallow`: 3–4 subtopics, shorter notes, faster.
   - `--depth standard` (default): 5–7 subtopics, thorough notes.
   - `--depth deep`: 8–12 subtopics, exhaustive notes, follow-up dives on anything surprising.
3. **Launch ALL sub-agents in a single message** so they run in parallel. Do not run them sequentially.
4. Wait for all sub-agents to complete.
5. Print status: `🔍 Deep dives complete. N notes collected.`

## Phase 4: Synthesis

1. Read ALL notes in the `notes/` directory.
2. Read `brief.md` to re-anchor on the original question.
3. Produce a complete `report.md` with:
   - **YAML frontmatter**: title, subtitle, date (today), author ("Deep Research"), template.
   - **Executive Summary**: the single most important page — what did we find and why does it matter? Write this LAST but place it first.
   - **Context / Background**: set the scene.
   - **Deep Analysis sections**: multiple H2 sections, each covering a major aspect. Lead with insight, not description. Use data, examples, comparisons. Acknowledge uncertainty.
   - **Implications**: so what?
   - **Open Questions**: what remains unresolved?
   - **Sources**: all references used, formatted as footnotes.
4. **Writing quality is paramount**:
   - Every paragraph must earn its place. Cut filler ruthlessly.
   - Use tables for data comparisons. Use blockquotes sparingly for key citations.
   - Use admonitions (`!!! insight "Key Insight"`) for standout findings.
   - Vary sentence length. Prefer prose over lists where it reads better.
   - Aim for 3,000–5,000 words for standard depth.
5. Print status: `✍️ Report draft complete.`

## Phase 5: Review & Polish

1. Critically review the draft. Check for:
   - Unsupported claims, logical gaps, redundancy
   - Weak sections, missing data, unclear passages
   - Executive summary accuracy
   - Proper markdown formatting
2. **Apply all fixes directly** to `report.md` — do not just list them.
3. Do a second pass for prose quality: tighten sentences, improve transitions, ensure every paragraph earns its place.
4. Print status: `✅ Review complete, fixes applied.`

## Phase 6: Render

1. Run `uv run python scripts/render.py research/<project>/report.md` with the appropriate template flag if specified.
2. If render fails, diagnose and fix the issue (usually malformed markdown or missing frontmatter), then retry.
3. Report the output PDF path and file size.
4. Print final status: `📄 Report complete: research/<slug>/output/report.pdf`

## Error Handling

- If any phase fails, diagnose the error, fix it, and retry before moving on.
- If web search returns thin results for a subtopic, note it as a gap and move on — don't block the pipeline.
- If the render fails, check common issues (frontmatter, broken markdown tables, encoding) and fix.

## Final Output

Print a summary card at the end:

```
══════════════════════════════════════════
  Research Report Complete
  Topic:    <topic>
  Sections: <N sections>
  Sources:  <N sources cited>
  Output:   research/<slug>/output/report.pdf
══════════════════════════════════════════
```
