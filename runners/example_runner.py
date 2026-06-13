#!/usr/bin/env python3
"""
Runner: Example Daily Digest
Description: Reads input text, calls the shared text-stats tool, and prints a
             one-line digest. Demonstrates the thin-runner pattern: it orchestrates
             a tool and formats output — no business logic of its own.
Schedule: manual (wire scheduling externally via cron / GitHub Actions)
Cost_Profile: Low
"""
from __future__ import annotations

import sys
from pathlib import Path

# Make shared tools importable regardless of where the runner is launched.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.example_tool import text_stats  # noqa: E402


def run(text: str) -> str:
    """Orchestrate the tool and return a human-readable digest line."""
    stats = text_stats(text)
    return (
        f"{stats['words']} words · {stats['sentences']} sentences · "
        f"~{stats['reading_minutes']} min read"
    )


def main() -> int:
    text = sys.stdin.read() or "No input provided."
    print(run(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
