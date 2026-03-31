---
name: new-research
description: Scaffold a new research project with the standard folder structure. Use when the user wants to start, create, or begin a new research project or investigation on a topic.
---

# New Research Project Scaffolder

You create new research projects with the standard folder structure.

## Instructions

1. **Accept a topic name** as the argument (e.g., `/new-research Quantum Computing in Drug Discovery`).

2. **Run the scaffold script:**
   ```bash
   uv run python scripts/new_research.py "<topic name>"
   ```

3. **After scaffolding**, read the generated `brief.md` and tell the user to fill in:
   - The core research question — what specifically are they trying to answer?
   - Scope boundaries — what's in scope, what's explicitly out?
   - Key areas to investigate (4–6 suggested)
   - Any constraints (timeline, depth, specific focus)

4. **Once the brief is ready**, suggest next steps:
   - Run `/plan` to generate a research plan
   - Or run `/report <topic>` to do everything automatically

5. **Provide a quick workflow overview:**
   - `brief.md` → `/plan` → `/deep-dive` (repeat per subtopic) → `/synthesize` → `/review` → `/render`
   - Or just: `/report <topic>` for the fully automated pipeline
