---
name: review
description: Critically review a research report draft and suggest improvements. Use when the user asks to review, check, proofread, improve, or strengthen a report or draft.
---

# Report Review & Critique

You critically review research report drafts and either suggest or directly apply improvements. This skill is called by the `/report` orchestrator or used standalone.

## Instructions

1. **Find the active project.** Look for the most recently modified project in `research/`, or ask.

2. **Read `report.md`** (the current draft).

3. **Read `brief.md`** to check alignment with original objectives.

4. **Perform a critical review** checking each of these dimensions:

### Logic & Argumentation
- Do the arguments follow logically?
- Are there internal contradictions?
- Are causal claims justified or merely correlational?
- Does the executive summary accurately reflect the findings?

### Evidence & Sources
- Are there unsupported claims? (Flag any statement that needs a source but doesn't have one.)
- Are sources credible and current?
- Is evidence presented fairly, or is it cherry-picked?
- Are data points specific (numbers, dates) or vague ("significant", "many")?

### Completeness
- What important angles were missed?
- Are there obvious counter-arguments not addressed?
- Does the report answer the original research question from the brief?
- Are the open questions genuine (not things that should have been answered)?

### Writing Quality
- Is there redundancy? (Anything said twice should be said once.)
- Are there confusing passages, undefined jargon, or ambiguous language?
- Do transitions between sections flow naturally?
- Does every paragraph earn its place?
- Is sentence variety adequate (not all the same length/structure)?

### Formatting & Structure
- Proper markdown: consistent heading levels, working footnotes, clean tables.
- Appropriate use of admonitions, blockquotes, and tables.
- YAML frontmatter present and correct.

5. **Produce a structured review** with:
   - **Overall Assessment** (1 paragraph)
   - **Critical Issues** (must fix — with specific locations and rewrites)
   - **Suggested Improvements** (should fix)
   - **Minor Notes** (nice to fix)
   - For weak passages: show **before → after** rewrites.

6. **Save the review** as `notes/review-feedback.md`.

7. **When called by `/report`**: Apply all fixes directly to `report.md` without asking.
   **When called standalone**: Ask the user if they want fixes applied, then apply them.
