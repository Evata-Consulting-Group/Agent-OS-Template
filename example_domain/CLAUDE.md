# Example Domain

A worked example of a top-level **domain** folder. Domains hold your actual
business/work areas (e.g. a consulting practice, a product, a content brand). Copy
this pattern to create your own domains at the repo root, then delete this folder.

## Scope

What this domain handles, and what it does NOT (and which other domain/agent does).

## Owning Agent

`agents/sam.md` (example). Each domain names an owning agent.

## Project Structure

```
example_domain/
├── CLAUDE.md              # this brief
└── widget_tracker/        # a sub-project within the domain
    ├── workflows/         # project-specific workflow specs (resolve before global)
    ├── docs/              # human inputs (read-only for the agent)
    ├── outputs/           # AI-generated deliverables (committed)
    └── .tmp/              # disposable intermediates
```

## Before You Edit

1. Read the file you're changing and this CLAUDE.md.
2. Check the relevant sub-project's `workflows/` for the governing spec.
3. Verify any shared tool's signature in `/tools/<tool>.py` before calling it.

## Current State

- **Status**: example / template — replace with a real domain.

---

> Remember: domains do not keep their own tools — shared tools live in `/tools/`.
> Domain-specific *workflows* live here and resolve before the global `/workflows/`.
