---
Name: example_workflow
Owner: Sam
Maturity: draft
Trigger: manual
Cost_Profile: Low
---

> Example workflow demonstrating the full spec. Copy it, rename, and adapt.
> Delete this file once you have real workflows.

Purpose: Produce a readability digest for a piece of text and route it for review.

Requires:
  Infrastructure: []
  Tools: [tools/example_tool.py]
  Skills/MCP: []
  Humans: [operator — approval before publishing]

Inputs:
  - name: draft text
    location: passed in / a file under the project's docs/

Outputs:
  - name: digest line + recommendation
    destination: the owning agent's heartbeat digest

Memory Strategy: event-log
Memory Location: <event store table/path — separate from agent context>

Steps:
  - id: 1
    description: Compute text statistics for the draft.
    executor: script:tools/example_tool.py
  - id: 2
    description: Decide whether the draft is ready to publish.
    executor: agent
    decision_contract:
      criteria: "reading_minutes <= 7 AND sentences >= 3 → mark READY; else NEEDS WORK"
      default: NEEDS WORK
      escalation: operator, within 24h
  - id: 3
    description: If READY, queue for the operator's approval; if NEEDS WORK, return notes.
    executor: agent

Evaluation:
  Per-step checks: tool returns valid JSON; decision criteria evaluated against it.
  Anomaly handling:
    - pattern: tool returns an error object
      action: escalate:Sam
  Event log: <path — NOT in agent memory>

Reflection:
  Cadence: monthly
  Triggers: 3 anomalies in a week, cost +20%, output drift
  Approval rules:
    Tweak: auto-apply, log
    Adjustment: owner approval if production tier
    Redesign: operator only
