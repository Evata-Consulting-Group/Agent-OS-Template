#!/usr/bin/env python3
"""
build_map.py — generate a Build Map table for a domain (or a set of paths).

The "Show Your Work" convention (see CLAUDE.md): after a non-trivial build, show what
was built at every layer, with the deterministic-vs-judgment split made visible, plus
how the pieces relate. This tool does the *discovery* deterministically so the inventory
and the relationships aren't hand-maintained — the agent then annotates Status (done/
partial/planned) and adds the one-paragraph build note when presenting a specific build.

Discovers, under each given domain dir: workflows (`**/workflows/*.md`), runners
(`**/runners/*.py`), skills (`**/.claude/skills/*/SKILL.md`), reference docs (`**/*.md`),
and any shared `tools/<x>.py` those files reference. Classifies each by layer → type tag,
then links components that name each other.

Usage:
  python tools/build_map.py example_domain
  python tools/build_map.py <dir-or-file> [more...]
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# layer, default type tag (⚙️ deterministic / 🧠 judgment / 📐 decision-contract / 📋 ref / 🔁 mixed)
def classify(p: Path):
    s = str(p).replace("\\", "/")
    if "/workflows/" in s and p.suffix == ".md":
        return "workflow", "🔁"
    if "/runners/" in s and p.suffix == ".py":
        return "runner", "⚙️"
    if p.name == "SKILL.md" or "/.claude/skills/" in s:
        return "skill", "🧠"
    if "/agents/" in s and p.suffix == ".md":
        return "agent", "🧠"
    if s.startswith(str(REPO / "tools").replace("\\", "/")) and p.suffix == ".py":
        return "tool", "⚙️"
    if p.suffix == ".py":
        return "tool", "⚙️"
    if p.suffix == ".md":
        return "reference", "📋"
    return "reference", "📋"


def display_name(p: Path, layer: str):
    if layer == "skill":               # .claude/skills/<name>/SKILL.md -> <name>
        return p.parent.name
    return p.name


def discover(root: Path):
    """Return {key: {path, layer, type, name, text}} for a domain dir (or a single file)."""
    found = {}

    def add(p: Path):
        if not p.is_file():
            return
        layer, tag = classify(p)
        name = display_name(p, layer)
        key = str(p.relative_to(REPO)) if REPO in p.parents else str(p)
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            text = ""
        found[key] = {"path": p, "layer": layer, "type": tag, "name": name, "text": text}

    if root.is_file():
        add(root)
        return found

    for pat in ("**/workflows/*.md", "**/runners/*.py", "**/.claude/skills/*/SKILL.md"):
        for p in root.glob(pat):
            add(p)
    # reference docs: domain .md files that aren't workflows/skills
    for p in root.rglob("*.md"):
        s = str(p).replace("\\", "/")
        if "/workflows/" in s or p.name == "SKILL.md" or "/output" in s:
            continue
        add(p)
    # shared tools referenced by anything discovered so far
    refs = set()
    for c in list(found.values()):
        refs |= set(re.findall(r"tools/([A-Za-z0-9_]+)\.py", c["text"]))
    for t in refs:
        add(REPO / "tools" / f"{t}.py")
    return found


def relations(found):
    """A relates-to B if A's text names B (by display name or filename stem)."""
    names = {k: (v["name"], v["path"].stem) for k, v in found.items()}
    rels = {}
    for k, v in found.items():
        hits = []
        for k2, (disp, stem) in names.items():
            if k2 == k:
                continue
            needle = disp if v["layer"] != "tool" else stem
            for cand in {disp, stem}:
                if len(cand) >= 4 and re.search(r"\b" + re.escape(cand) + r"\b", v["text"]):
                    hits.append(found[k2]["name"])
                    break
        rels[k] = sorted(set(hits))
    return rels


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: build_map.py <domain-dir-or-paths>...")
    found = {}
    for arg in sys.argv[1:]:
        found.update(discover(Path(arg).resolve()))
    if not found:
        sys.exit("No components found.")
    rels = relations(found)

    order = {"workflow": 0, "runner": 1, "tool": 2, "skill": 3, "agent": 4, "reference": 5}
    rows = sorted(found.items(), key=lambda kv: (order.get(kv[1]["layer"], 9), kv[1]["name"]))

    print("## Build Map\n")
    print("| Component | Layer | Type | Status | Relates to |")
    print("|---|---|---|---|---|")
    for k, v in rows:
        rel = ", ".join(rels[k][:6]) or "—"
        print(f"| `{v['name']}` | {v['layer']} | {v['type']} | — | {rel} |")
    print("\n> Type: ⚙️ deterministic · 🧠 judgment · 📐 decision-contract · 📋 reference · 🔁 mixed-steps")
    print("> Status (—) and the build note are filled in by the agent for a specific build.")


if __name__ == "__main__":
    main()
