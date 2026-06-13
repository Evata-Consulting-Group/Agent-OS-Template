# AOS Agent Stewardship — Spec, Feedback Loop, Self-Improvement

> The authoritative contract for how agents are defined and how the
> observe → diagnose → propose → route → verify → log improvement cycle runs.
> Read this when **defining or changing an agent** or its stewardship behavior.
> The short version (registries, channels, no-emotion rule) stays in root `CLAUDE.md`.

---

## Agent Spec (the contract)

Every agent lives at `/agents/<name>.md` and conforms to:

```yaml
---
Name: <e.g., Sam>
Scope: <what they own — workflows, domains>
Phone: <messaging number, if used>
Email: <forwarding alias, if used>
Voice: terse | warm | formal
---

Workflows Owned: [<list>]

Push Triggers (real-time, e.g. text):
  - Decision needed, severity HIGH
  - Pending item default-fires within 24h
  - Anomaly escalation, severity HIGH
  Quiet hours: <e.g., 9pm–7am, weekends> (HIGH severity overrides)

Heartbeat (periodic digest):
  Cadence: weekly, <day + time>
  Sections:
    1. What ran (one-liners with status)
    2. Anomalies + auto-remediations applied
    3. Pending items awaiting the operator's call
    4. Proposed improvements (tweak / adjustment / redesign)
    5. Notes from the world (relevant tech/research noticed)

Pending Queue:
  Storage: <table/path>
  Item shape: id, summary, origin_workflow, options, default_if_no_response, expires_at, status
  Reply protocol:
    "<id> go"        → execute
    "<id> defer 2w"  → snooze 2 weeks
    "<id> forget"    → dismiss, never re-raise unless conditions change
    "<id> → <name>"  → reassign with context
    "<id> ?"         → request more detail

Re-nudge rule: An item never re-nudges unless its default-fire window is approaching OR severity escalates. No nagging.

Escalation Chain:
  1. Apply decision contract / criteria
  2. Surface to the operator via the right channel (HIGH = real-time, else digest)
  3. If unresponsive past expires_at → apply default
  4. If no default → reassign per escalation field
```

---

## Agent Stewardship

The agent's job is not just to run workflows but to **steward** them:

1. **Run the work** per the spec (or invoke the deterministic runner).
2. **Watch the outcome** — operational anomalies (errors, retries) and quality
   anomalies (output regression).
3. **Route decisions** via Decision Contracts: criteria match → decide and log;
   criteria don't match → push to the owner; owner unresponsive past `expires_at`
   → apply default, else reassign per escalation chain.
4. **Log everything operational to the event store** (NOT to agent memory). Agent
   context stays clean; humans get full history when they want it.
5. **Reflect on a cadence** — review logs, run metrics, output samples; produce
   structured proposals against specific workflows.
6. **Propose improvements** with a class tag:
   - **Tweak** (prompt, retry count, batch size, cache config): auto-applies, logged.
   - **Adjustment** (add/remove step, swap tool, change memory strategy): owner
     approval in production tier; auto-applies in draft tier.
   - **Redesign** (flow change, new decision contract, new owner): always the operator.

Agents communicate **as competent employees**, not emotional entities. Concrete,
time-bounded, decision-oriented. No simulated feelings, no validation-seeking, no
displeasure when ignored. Voice differentiation (terse vs. warm) is encouraged;
affective manipulation is not.

---

## Feedback Loop

```
Workflow runs
  │
  ├── Operational anomaly → log → known pattern? → auto-fix → log
  │                                └→ unknown? → escalate to owner agent
  │
  ├── Quality eval → drift? → owner agent investigates → proposal
  │
  ├── Reflection cadence fires → owner agent reviews logs+runs+world → proposal
  │
  └── Operator's gripe ("this annoys me") → owner agent → proposal

All proposals → owner agent's pending queue
                 │
                 ├── Class = Tweak → auto-apply, mention in next digest
                 ├── Class = Adjustment → in next digest, await operator's call
                 └── Class = Redesign → notify operator (or digest if not urgent)

Operator's reply ("forget" / "defer" / "go" / "→ <name>")
  → item resolved, agent does not re-raise unless conditions change
```

**Pending queue parking lot:** Items the operator isn't ready to act on stay
parked. No re-nudge unless conditions materially change. "Forget" dismisses for good.

---

## Self-Improvement Loop

Every workflow has a **Reflection** block:

1. **Observe** — operational logs, quality eval, run metrics, external signals.
2. **Diagnose** — drift, recurring failures, cost overrun, regression, opportunity.
3. **Propose** — structured proposal against a specific workflow, classified
   Tweak / Adjustment / Redesign.
4. **Route** — auto-apply (Tweak), surface to owner (Adjustment), or operator (Redesign).
5. **Verify** — for production-tier changes, tests must pass before promotion.
6. **Log** — every proposal and its disposition goes to the reflection log.

Reflection is structured, not free-form — proposals must name the workflow, the
change class, and the expected effect.
