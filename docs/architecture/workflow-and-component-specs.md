# AOS Component Specs — Workflows, Tools, Runners, UI Contract

> The authoritative contract for how workflows, tools, and runners self-describe so
> a Control UI can discover them. Read this when **authoring or modifying** a
> workflow/tool/runner. Day-to-day operating rules stay in the root `CLAUDE.md`.

---

## UI Integration Contract

All components self-describe so the Control UI can discover them. The UI reflects
structure; it never hardcodes component registration.

## Workflow Spec (the contract)

Every workflow begins with YAML frontmatter and contains the following sections:

```yaml
---
Name: <workflow name>
Owner: <agent name — must match /agents/<name>.md>
Maturity: draft | piloted | production
Trigger: cron:<expr> | event:<source> | manual | upstream:<workflow>
Cost_Profile: Low | Medium | High
---

Purpose: <one sentence>

Requires:
  Infrastructure: [<e.g., vector store path, message number>]
  Tools: [<e.g., tools/example_tool.py>]
  Skills/MCP: [<e.g., MCP: google-workspace>]
  Humans: [<e.g., operator — approval on X>]

Inputs:
  - name: <what>
    location: <path / table / inbox>

Outputs:
  - name: <what>
    destination: <where it goes>

Memory Strategy: none | event-log | semantic-recall | persistent-state
Memory Location: <path/table — separate from agent context>

Steps:
  - id: 1
    description: <what happens>
    executor: agent | script:<path> | human:<name>
    decision_contract:        # only on judgment steps
      criteria: <pre-decision rule the agent applies without asking>
      default: <fallback if no human response>
      escalation: <who, by when>

Evaluation:
  Per-step checks: <what gets validated each run>
  Anomaly handling:
    - pattern: <description>
      action: auto-remediate:<how> | escalate:<agent>
  Event log: <path — NOT in agent memory>

Reflection:
  Cadence: <weekly | monthly | on-trigger>
  Triggers: <e.g., 3 anomalies in a week, cost +20%, drift detected>
  Approval rules:
    Tweak: auto-apply, log
    Adjustment: owner approval if production tier
    Redesign: operator only
```

The Control UI parses this metadata. A workflow cannot be marked
`Maturity: production` until everything in `Requires:` is verified present.

## Tool Metadata Standard

Tools declare input structure, output structure, and side effects. Predictable
JSON responses. Tools function like APIs: reusable, structured I/O, idempotent
where possible, no hidden state. Refactor instead of duplicating.

## Runner Metadata Standard

```python
"""
Runner: <Display Name>
Description: <What it does>
Schedule: <Intended schedule or "manual">
Cost_Profile: <Low | Medium | High>
"""
```

---

## Maturity Spectrum (why it matters)

When AI tries to handle every step of a multi-step workflow directly, accuracy
compounds downward. Five 90%-accurate steps give ~59% end-to-end success. For work
you run *repeatedly* and *depend on*, hardening into deterministic code is a
reliability requirement. For work you're still exploring, full-agent execution is
faster and the failure cost is low. **Harden as it matures** — not "always
deterministic," not "always agent."
