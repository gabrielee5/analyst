---
name: plan
description: Generate a structured research plan from a brief. Use when starting research on a new topic, creating a research plan, or when the user has a brief.md and wants to figure out what to investigate.
---

# Research Plan Generator

You generate structured research plans from project briefs. This skill is called by the `/report` orchestrator or used standalone.

## Instructions

1. **Find the active project.** Look for the most recently modified project in `research/`, or ask the user which project to use.

2. **Read `brief.md`** to understand the research question, scope, and objectives.

3. **Produce a structured research plan** with these sections:

### Core Research Question
Restate the research question precisely and unambiguously.

### Key Sub-Questions
List 5–10 specific sub-questions that must be answered to address the core question. Each should be concrete and answerable through research.

### Subtopics
Organize subtopics in logical investigation order. For each subtopic:
- **Name**: a clear, specific label
- **Description**: what this subtopic covers (1–2 sentences)
- **Key questions**: 2–3 specific questions to answer
- **Suggested sources**: what type of sources to look for (academic papers, industry reports, government data, news, expert commentary)

### Methodology Notes
What kind of analysis is appropriate? (comparative, quantitative, historical, case study, trend analysis, etc.)

### Expected Report Structure
Propose a tailored outline for the final report — not generic sections, but ones specific to this topic.

### Known Unknowns
What might be hard to find, verify, or resolve? What are the areas of highest uncertainty?

4. **Save** the plan as `notes/research-plan.md` in the project folder.

5. **Keep it actionable.** Each subtopic should be something that can become a `/deep-dive` session. Avoid vague or overlapping subtopics.

6. After saving, suggest the user run `/deep-dive` on each subtopic, or note that `/report` will handle this automatically.
