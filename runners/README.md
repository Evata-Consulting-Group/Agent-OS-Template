# runners/

Thin orchestration entry points. Runners coordinate tools, may invoke workflows,
and may call LLM APIs — but they hold **no heavy business logic** (that lives in
tools and workflows). Scheduling is **external** (cron / GitHub Actions); never
schedule from inside a runner, tool, or workflow.

Every runner starts with the metadata header docstring (see `example_runner.py`)
so the Control UI can discover it.

Rules:
- Keep logic thin — orchestration, not business rules.
- Respect cost boundaries (caps, batching, caching).
- Don't duplicate tool functionality.

Delete `example_runner.py` once you have real runners.
