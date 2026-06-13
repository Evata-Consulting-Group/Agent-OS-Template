# Agent Operating System (AOS) — Starter Template

A disciplined, scalable structure for AI-assisted work. AOS separates **reasoning**
from **execution** where reliability matters, keeps domain knowledge in
human-readable **workflows**, hardens repeated work into deterministic **tools**,
and puts a named **agent** in charge of stewarding each piece.

This repo is a **clean template**. It ships the architecture, the operating
contract (`CLAUDE.md`), and one worked example of every component — then you fill
it with your own ventures, tools, and agents.

> Originally built by Jared Clark as a personal AI System; generalized here for the
> Evata Consulting Group team. Nothing personal to the original author is included.

---

## What's in here

| Path | What it is |
|------|------------|
| `CLAUDE.md` | The operating contract Claude Code reads every session. **Start here.** |
| `SETUP.md` | The short checklist of things *you* personalize before using it. |
| `dev-workflow.md` | Branching, testing, merging, rollback rules. |
| `docs/architecture/` | Deep reference: the Workflow/Tool/Runner specs and the agent stewardship model. |
| `CLAUDE_TEMPLATE.md` | Copy this to create a per-project/domain `CLAUDE.md`. |
| `agents/` | Named agents + the people/email registries (examples). |
| `tools/` | Shared deterministic scripts (one example). |
| `runners/` | Thin orchestration entry points (one example). |
| `workflows/` | Global workflow specs (one example). |
| `tests/` | Verification for shared tools (one example). |
| `shared/` | Where a Control UI would live (documented, not shipped). |
| `config/` | System-wide configuration. |
| `ventures/` | Early-stage / pre-revenue projects you start. |
| `example_domain/` | A worked example of a top-level domain folder. |
| `personal/` | Your private space — gitignored, meant for a separate private repo. |

## Quickstart

1. **Clone**, then work through [SETUP.md](SETUP.md) (5–10 min).
2. Open the repo in your editor with the Claude Code extension. It auto-loads
   `CLAUDE.md` and any per-directory `CLAUDE.md`.
3. Read [CLAUDE.md](CLAUDE.md) yourself once — it's the whole mental model.
4. Delete the `example_*` files once you understand the pattern, and start adding
   your own domains under the repo root and early ideas under `ventures/`.

## The core idea (one paragraph)

Mature, repeated, high-stakes work should harden into deterministic code; one-off
exploratory work can stay agent-led. AI handles judgment and edge cases; code
handles repeatable mechanics. Tools are shared infrastructure. Workflows encode
domain intelligence in a readable spec. A named agent owns each workflow, runs it,
watches it, and proposes improvements — protecting *your* attention, which is the
scarce resource. See `CLAUDE.md` for the full philosophy and the six-term vocabulary.
