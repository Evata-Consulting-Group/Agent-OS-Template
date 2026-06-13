#!/usr/bin/env python3
"""
Tool: Text Stats
Description: Deterministic text statistics (word/char/sentence counts, reading
             time). Example of the AOS tool contract: structured JSON in/out,
             pure, idempotent, no domain assumptions, no side effects.
Inputs:  {"text": str, "wpm": int (optional, default 200)}
Outputs: {"words": int, "characters": int, "sentences": int,
          "reading_minutes": float}

Run as a CLI for ad-hoc use:
    echo '{"text": "Hello world."}' | python tools/example_tool.py
"""
from __future__ import annotations

import json
import re
import sys


def text_stats(text: str, wpm: int = 200) -> dict:
    """Return deterministic statistics for a block of text.

    Pure function — same input always yields the same output, no I/O.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if wpm <= 0:
        raise ValueError("wpm must be positive")

    words = re.findall(r"\b\w+\b", text)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    word_count = len(words)

    return {
        "words": word_count,
        "characters": len(text),
        "sentences": len(sentences),
        "reading_minutes": round(word_count / wpm, 2),
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        result = text_stats(payload["text"], int(payload.get("wpm", 200)))
        json.dump(result, sys.stdout)
        sys.stdout.write("\n")
        return 0
    except Exception as exc:  # structured error output
        json.dump({"error": str(exc)}, sys.stdout)
        sys.stdout.write("\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
