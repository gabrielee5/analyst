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

4. **Read `domain-profile.md`** if it exists. This provides domain-specific review criteria that supplement the standard checks. The analyst persona tells you what lens to apply — an equity analyst reviews differently than a historian.

5. **Perform a critical review** checking each of these dimensions:

### Logic & Argumentation
- Do the arguments follow logically?
- Are there internal contradictions?
- Are causal claims justified or merely correlational?
- Does the executive summary / lead section accurately reflect the findings?

### Evidence & Sources
- Are there unsupported claims? (Flag any statement that needs a source but doesn't have one.)
- Are sources credible and current?
- Is evidence presented fairly, or is it cherry-picked?
- Are data points specific (numbers, dates) or vague ("significant", "many")?
- **Footnote citation check (critical):** Every specific data point, financial figure, quote, and non-obvious fact MUST have a `[^N]` inline footnote marker. The report should have 25-40 footnotes minimum. Sources must ONLY appear as numbered `[^N]:` definitions at the bottom — never as a prose bullet list. If the report uses a "Sources Consulted" list instead of inline footnotes, flag this as a critical issue and fix it.

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
- Every `[^N]` in the body has a matching `[^N]:` definition, and vice versa — no orphaned references or unused definitions.

### Domain-Specific Quality
**If `domain-profile.md` exists**, apply its **Review Criteria** as an additional review dimension. Examples of what this checks:

- **Financial reports**: Do ratios and financial data tie back to filings? Is the valuation methodology appropriate and consistent? Are projections clearly distinguished from facts? Is the peer comparison valid?
- **Intelligence/geopolitical briefings**: Are confidence levels assigned to key judgments? Are sources properly weighted? Is assessed vs. confirmed information clearly distinguished?
- **Scientific/technical reviews**: Is the methodology sound? Are limitations acknowledged? Is prior work properly cited? Are statistical claims valid?
- **Historical analysis**: Is historiographic context acknowledged? Are primary and secondary sources distinguished? Are anachronistic framings avoided?
- **Policy analysis**: Are costs and benefits quantified where possible? Are stakeholder impacts identified? Are political feasibility constraints acknowledged?

If no domain profile exists, skip this section.

6. **Produce a structured review** with:
   - **Overall Assessment** (1 paragraph)
   - **Critical Issues** (must fix — with specific locations and rewrites)
   - **Suggested Improvements** (should fix)
   - **Minor Notes** (nice to fix)
   - For weak passages: show **before -> after** rewrites.

7. **Save the review** as `notes/review-feedback.md`.

8. **When called by `/report`**: Apply all fixes directly to `report.md` without asking.
   **When called standalone**: Ask the user if they want fixes applied, then apply them.
