# tests/

Verification for shared tools, critical workflows, and runner logic. Tests are the
guardrail that lets the system change fast without breaking.

Standards (see [dev-workflow.md](../dev-workflow.md)):
- Deterministic — no flakiness.
- **No paid API calls** without explicit approval — use mocks and fixtures.
- Validate structured JSON output.
- Runner tests verify successful execution, proper tool invocation, and controlled
  failure handling.

Run the suite from the repo root:

```
pytest
```

See `test_example_tool.py` for the pattern. Delete it once you have real tests.
