# SETUP — Personalize Your AOS

This template is written in generic prose ("the operator," "your company") so it
reads cleanly to Claude Code. There are only a handful of things to personalize
before you start. Work top to bottom — most of it is 5–10 minutes.

## 1. Identity & naming
- [ ] In `CLAUDE.md`, replace **"the operator"** references with how you want the
      agent to address you, and set your name/role in the opening lines.
- [ ] In `agents/people.md` (copy from `people.md.example`), add yourself and any
      collaborators: name, email, phone, permissions.
- [ ] In `agents/email_channels.md` (copy from `email_channels.md.example`), list
      your real sending identities and which is the default.

## 2. Secrets & config (never commit these)
- [ ] Copy `.env.template` → `.env` and fill in your API keys. `.env` is gitignored.
- [ ] Copy `.claude/settings.local.json.example` → `.claude/settings.local.json`
      and put any MCP/server secrets in its `env` block. Also gitignored.
- [ ] `.mcp.json` references secrets as `${VAR}` — it stays committed and
      secret-free. The values come from the `env` block above (or your shell).
- [ ] **Never put a secret directly in a committed file** (`.mcp.json`,
      `settings.json`, code, docs). If you do, rotate it.

## 3. Your work
- [ ] Decide your first **agent** — copy `agents/example-agent.md` to
      `agents/<name>.md` and define its scope, voice, and channels.
- [ ] Start a domain or a venture: a mature/revenue effort becomes a **top-level
      folder** (see `example_domain/`); an early idea goes under `ventures/`.
- [ ] Each substantial project gets its own `CLAUDE.md` — copy `CLAUDE_TEMPLATE.md`.

## 4. Infrastructure (optional, when you need it)
- [ ] If you run scheduled automation, wire it externally (cron / GitHub Actions) —
      never inside tools or workflows.
- [ ] If you stand up a Control UI or any service, register its port in `PORTS.md`
      first and confirm it's free (`ss -tlnp`).
- [ ] Private material (finances, personal docs) → put it in `personal/` and track
      it in a **separate private repo**, not this one. See `personal/README.md`.

## 5. Remote
- [ ] Point `origin` at your own repo and push:
      `git remote set-url origin <your-repo-url>` then `git push -u origin main`.

## 6. Clean up the examples
- [ ] Once the pattern is clear, delete the `example_*` files
      (`tools/example_tool.py`, `runners/example_runner.py`,
      `workflows/example_workflow.md`, `tests/test_example_tool.py`,
      `agents/example-agent.md`, `example_domain/`). They exist only to teach.

That's it. The architecture does the rest.
