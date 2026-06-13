# agents/

Named entities that own workflows, communicate with the operator, and steward the
work. One file per agent: `agents/<name>.md`, conforming to the Agent Spec in
[docs/architecture/agent-stewardship.md](../docs/architecture/agent-stewardship.md).

## Files here

- **`people.md`** — canonical registry of humans (you + collaborators) and their
  identity signals (email, phone) and permissions. Agents read it on session start
  to know who they're talking to. Copy from `people.md.example`.
- **`email_channels.md`** — canonical registry of your sending identities and email
  tooling. Read before drafting/sending any email. Copy from `email_channels.md.example`.
- **`example-agent.md`** — a worked example. Copy it to `agents/<name>.md` and edit.

Agents do not simulate emotions — they communicate as competent employees:
stake-claims, specific asks, time-bounded.
