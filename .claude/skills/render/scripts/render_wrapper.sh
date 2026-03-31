#!/bin/bash
# Wrapper for render.py — called by the render skill
PROJECT_PATH="${1:?Usage: render_wrapper.sh <project-path> [--template <name>]}"
shift
uv run python scripts/render.py "$PROJECT_PATH/report.md" "$@"
