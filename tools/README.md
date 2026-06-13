# tools/

Shared deterministic scripts — the reusable execution layer. Tools function like
APIs: structured I/O (JSON in, JSON out), idempotent where possible, no hidden
state, no domain-specific assumptions. Domains do NOT keep their own tools —
generalize and share here.

Rules (see [dev-workflow.md](../dev-workflow.md) and `docs/architecture/`):
- Preserve generality — no hardcoded domain assumptions.
- Structured JSON inputs and outputs.
- Every shared tool has a matching test in `/tests/`. **No tool change is complete
  unless tests pass.**
- Refactor instead of duplicating.

See `example_tool.py` for the shape. Delete it once you have real tools.
