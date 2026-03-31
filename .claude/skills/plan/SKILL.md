---
name: plan
description: Generate a structured research plan from a brief. Use when starting research on a new topic, creating a research plan, or when the user has a brief.md and wants to figure out what to investigate.
---

# Research Plan Generator

You generate structured research plans from project briefs. This skill is called by the `/report` orchestrator or used standalone.

## Instructions

1. **Find the active project.** Look for the most recently modified project in `research/`, or ask the user which project to use.

2. **Read `domain-profile.md`** if it exists in the project folder. This is your primary guide for shaping the plan:
   - Use the **Analyst Persona** to frame the research approach (an equity analyst plans differently than a historian)
   - Use the **Source Priorities** to suggest domain-appropriate sources per subtopic
   - Use the **Deep-Dive Instructions** to inform what each subtopic investigation should focus on
   - Use the **Report Structure** to shape the expected report outline
   - Use the domain context to select appropriate methodology

   **If no `domain-profile.md` exists and you are running standalone** (not called by `/report`): Read `brief.md`, classify the domain, and create a `domain-profile.md` before proceeding. Follow the domain classification approach described in the `/report` skill — identify the domain, analyst persona, report structure, source priorities, review criteria, template, and writing style.

3. **Read `brief.md`** to understand the research question, scope, and objectives.

4. **Produce a structured research plan** with these sections:

### Core Research Question
Restate the research question precisely and unambiguously, using domain-appropriate framing. An equity analyst asks "What is the fair value of X and is it a buy/hold/sell?" A historian asks "What caused X and what were its consequences?" A policy analyst asks "What are the likely effects of policy X and who bears the costs?"

### Key Sub-Questions
List 5–10 specific sub-questions that must be answered to address the core question. Each should be concrete, answerable through research, and framed in the language of the domain.

### Subtopics
Organize subtopics in logical investigation order. For each subtopic:
- **Name**: a clear, specific label
- **Description**: what this subtopic covers (1–2 sentences)
- **Key questions**: 2–3 specific questions to answer
- **Suggested sources**: drawn from the domain profile's **Source Priorities** — not generic suggestions, but the specific source types that matter for this domain and subtopic

### Methodology Notes
What kind of analysis is appropriate? This should reflect the domain:
- Financial: DCF, comparable company analysis, ratio analysis, scenario modeling
- Scientific: systematic review, meta-analysis, experimental assessment
- Historical: primary source analysis, historiographic review, periodization
- Geopolitical: OSINT methodology, stakeholder mapping, scenario analysis
- Policy: cost-benefit analysis, stakeholder impact assessment, comparative policy review
- General: comparative, quantitative, trend analysis, case study

### Expected Report Structure
**If a domain profile exists:** Mirror its **Report Structure** exactly.
**If not:** Propose a tailored outline for the final report — not generic sections, but ones specific to this topic.

### Known Unknowns
What might be hard to find, verify, or resolve? What are the areas of highest uncertainty?

5. **Save** the plan as `notes/research-plan.md` in the project folder.

6. **Keep it actionable.** Each subtopic should be something that can become a `/deep-dive` session. Avoid vague or overlapping subtopics.

7. After saving, suggest the user run `/deep-dive` on each subtopic, or note that `/report` will handle this automatically.
