# DEVELOPMENT WORKFLOW

How code changes occur inside the AOS — branching, testing, merging, rollback.
For architectural rules, layer definitions, and metadata contracts, see `CLAUDE.md`
and `docs/architecture/`. This document builds on those; it doesn't duplicate them.

Follow this process for every code change. No shortcuts.

---

# Core Rule

No changes are made directly to `main`. All development occurs in branches.

---

# Branching Model

```
main
├── feature/*    # New capabilities or enhancements
├── tool/*       # Changes to /tools/
├── domain/*     # Domain-specific work (maps to /<domain>/)
├── runner/*     # Changes to /runners/
├── ui/*         # Changes to the Control UI
└── fix/*        # Bug fixes and regressions
```

Domain branches scope changes to that domain's directory and its workflows.
Cross-cutting changes belong in `feature/*` or `tool/*` branches.

---

# Standard Process

1. `git checkout -b feature/description`
2. Draft changes.
3. Review: `git diff`
4. Test: `pytest`
5. Confirm: tests pass · no regressions · metadata standards satisfied · no
   architectural rules violated.
6. Commit with a structured message: `[layer] brief description`
   - `[tool] add batch endpoint support for rate-limited API`
   - `[runner] add daily digest runner with cost cap`
   - `[workflow] update scraping workflow with retry guidance`
   - `[fix] resolve JSON output regression in parser tool`
7. Merge only when stable.

---

# Rollback Protocol

When a merge introduces a regression:
1. Revert the merge commit immediately: `git revert <merge-commit-hash>`
2. Reopen the branch or create a `fix/*` branch.
3. Diagnose, fix, retest before re-merging.
4. Never patch `main` directly. If unsure whether it's a regression, escalate
   before reverting.

---

# Remote Sync

- Push branches after meaningful commits — don't let local work accumulate without
  a remote backup.
- `main` is merged locally, then pushed. `main` on the remote must always reflect a
  stable state.
- Never force-push to `main`.

```
git remote add origin <your-repo-url>
git push -u origin main
```

Check sync with `git status` and `git log --oneline origin/main..main`.

---

# Modification Protocols

## Tools (`/tools/`)
Preserve generality (no hardcoded domain assumptions) · structured JSON I/O ·
include test updates in `/tests/` · respect metadata standards · pass all tests
before merge.

## Runners (`/runners/`)
Keep logic thin (orchestration, not business rules) · respect cost boundaries ·
include the metadata header docstring · don't duplicate tool functionality.

## Workflows (`/workflows/`, `/<domain>/.../workflows/`)
Include the metadata header (see specs doc) · preserve human readability · don't
embed execution logic. **Do not overwrite or delete an existing workflow without
the operator's explicit approval** — propose the update and wait. Workflows are
operating instructions: they get refined, not discarded.

## UI
The Control UI must not require manual wiring. New runners/workflows/tools conform
to metadata standards so the UI discovers them automatically. The UI reflects
filesystem structure — it does not define it.

---

# Build Artifacts

Test outputs, build artifacts, and intermediate files go in `.tmp/` (global or a
project's `.tmp/`). Everything in `.tmp/` is disposable and regenerable. Final
deliverables go to `outputs/` (committed) or the appropriate destination.

---

# Testing Protocol

All shared tools must have tests in `/tests/`. Tests must be deterministic, avoid
paid API calls (use mocks/fixtures), and validate structured JSON output. Runner
tests verify successful execution, proper tool invocation, and controlled failure.

UI test automation comes only after core flows stabilize — premature UI tests are
brittle.

---

# Architectural Escalation

Pause and escalate when changes would: alter folder structure · increase scheduled
cost exposure · break metadata standards · collapse layer separation · create,
overwrite, or delete workflows · affect multiple domains. When in doubt, ask.

---

# Goal

The system must scale and stay productizable, reproducible, defensible, and
maintainable. Short-term speed must not destroy long-term integrity. Every commit
should leave the system stronger than you found it.
