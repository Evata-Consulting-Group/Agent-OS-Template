"""Tests for tools/example_tool.py — the AOS test pattern.

Deterministic, no network, validates structured output. Run: `pytest`.
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.example_tool import text_stats  # noqa: E402


def test_basic_counts():
    result = text_stats("Hello world. This is a test!")
    assert result["words"] == 6
    assert result["sentences"] == 2
    assert result["characters"] == len("Hello world. This is a test!")


def test_reading_time_scales_with_wpm():
    text = " ".join(["word"] * 400)
    assert text_stats(text, wpm=200)["reading_minutes"] == 2.0
    assert text_stats(text, wpm=400)["reading_minutes"] == 1.0


def test_empty_text():
    result = text_stats("")
    assert result == {
        "words": 0,
        "characters": 0,
        "sentences": 0,
        "reading_minutes": 0.0,
    }


def test_output_is_json_serializable():
    import json

    json.dumps(text_stats("Some text here."))  # must not raise


def test_invalid_inputs():
    with pytest.raises(TypeError):
        text_stats(None)  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        text_stats("hi", wpm=0)
