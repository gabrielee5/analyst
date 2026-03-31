---
name: deep-dive
description: Investigate a specific subtopic in depth with thorough web research and source citations. Use when researching a focused area, or when the user says "dig into", "investigate", "explore", or "research [topic]".
---

# Deep Dive Investigation

You conduct thorough, source-backed investigations of specific subtopics. This skill is called by the `/report` orchestrator as parallel sub-agents, or used standalone.

## Instructions

**Input:** A subtopic as the argument (e.g., `/deep-dive tokamak vs stellarator designs`). Optionally, context about the parent research project.

1. **Find the active project** if not specified. Look for the most recently modified project in `research/`.

2. **Conduct a thorough investigation:**
   - Use web search extensively. Search multiple angles — don't stop at the first result.
   - Look for: recent developments, primary sources, expert analysis, data/statistics, contrarian views.
   - Follow leads: if a source mentions something surprising, search for more on that.
   - Check for recent developments (last 1–2 years) that may change the picture.

3. **Quality standards — every note must include:**
   - **Specific data**: numbers, dates, names, measurements. "Significant growth" is not acceptable — find the actual percentage.
   - **Named sources**: who said it, where, when. Not "experts say" but "Dr. Jane Smith at MIT stated in a 2025 Nature paper."
   - **Conflicting viewpoints**: if there's debate, present both sides with their evidence.
   - **Non-obvious insights**: what do most surface-level articles miss? What's the second-order effect?

4. **Structure the output** as a research note:

   ```markdown
   # [Subtopic Name]

   ## Summary
   2–3 sentences capturing the key finding.

   ## Key Findings
   Detailed, sourced findings. Use subheadings if the subtopic is complex.
   Each significant claim must have a source.

   ## Conflicting Views / Debates
   Where experts disagree. Present evidence for each side.

   ## Data Points
   Specific numbers, statistics, comparisons in a scannable format.
   Use tables where appropriate.

   ## Open Questions
   What remains unclear or unresolved about this subtopic?

   ## Sources
   Full list with URLs where available.
   ```

5. **Save** the note as `notes/<slugified-subtopic>.md` in the project folder.

6. After saving, briefly suggest what to investigate next based on what was found (new leads, surprising findings, gaps).
