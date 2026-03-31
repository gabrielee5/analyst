#!/usr/bin/env python3
"""Scaffold a new research project with the standard folder structure."""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = PROJECT_ROOT / "research"


def slugify(text: str) -> str:
    """Convert a topic name to a filesystem-safe slug."""
    slug = text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug[:80]


def scaffold(topic: str):
    """Create a new research project folder with standard structure."""
    slug = slugify(topic)
    project_dir = RESEARCH_DIR / slug

    if project_dir.exists():
        print(f"Error: project folder already exists: {project_dir}", file=sys.stderr)
        sys.exit(1)

    # Create directories
    (project_dir / "notes").mkdir(parents=True)
    (project_dir / "output").mkdir(parents=True)

    # Write brief.md
    brief = f"""# {topic}

## Research Question

<!-- What specific question(s) are you trying to answer? -->


## Scope

<!-- What's in scope? What's explicitly out of scope? -->


## Key Areas to Investigate

1.
2.
3.
4.
5.

## Constraints

<!-- Any constraints on depth, timeline, or focus? -->

"""
    (project_dir / "brief.md").write_text(brief, encoding="utf-8")

    # Write starter report.md
    today = date.today().isoformat()
    report = f"""---
title: "{topic}"
subtitle: "A Research Report by Fabietti.xyz"
date: "{today}"
author: "Fabietti.xyz"
template: "default"
---

# {topic}

## Executive Summary

<!-- The single most important page — what did you find and why does it matter? -->

## Context & Background

<!-- Why does this topic matter now? What's the state of affairs? -->

## Analysis

<!-- Deep analysis sections go here. Use multiple H2 sections. -->

## Implications

<!-- So what? What does this mean going forward? -->

## Open Questions

<!-- What remains unresolved or worth watching? -->

## Sources

<!-- All references, formatted consistently. -->
"""
    (project_dir / "report.md").write_text(report, encoding="utf-8")

    # Gitkeep for notes
    (project_dir / "notes" / ".gitkeep").touch()

    print(f"Research project scaffolded: {project_dir}")
    print()
    print("Next steps:")
    print(f"  1. Fill in the brief:  {project_dir / 'brief.md'}")
    print("  2. Generate a plan:   /plan")
    print("  3. Research subtopics: /deep-dive <subtopic>")
    print("  4. Write the report:  /synthesize")
    print("  5. Review & improve:  /review")
    print("  6. Render to PDF:     /render")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new research project")
    parser.add_argument("topic", help="The research topic name")
    args = parser.parse_args()
    scaffold(args.topic)


if __name__ == "__main__":
    main()
