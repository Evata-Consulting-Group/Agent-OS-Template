# shared/ — Control UI (documented, not shipped)

In a full AOS, `shared/` holds the **Control UI**: a single web app (e.g. Flask)
that **auto-discovers** runners, workflows, tools, agents, and pending items by
reading the filesystem and the metadata each component declares. It never hardcodes
component registration and contains no business logic — it *reflects* system
structure.

This template **documents the contract but does not ship a UI**, so you can start
lean and add one when you actually need a window into the system.

## The discovery contract (what a UI relies on)

- **Workflows** declare YAML frontmatter (Name, Owner, Maturity, Trigger,
  Cost_Profile) — see `docs/architecture/workflow-and-component-specs.md`.
- **Runners** start with a metadata header docstring (Runner / Description /
  Schedule / Cost_Profile).
- **Tools** declare structured JSON I/O and side effects.
- **Agents** live at `agents/<name>.md` with the Agent Spec frontmatter.

If you build a UI, put it here (`shared/ai_control_center/` is a good name),
register its port in `PORTS.md` first, and keep it a pure reflection of structure.

## Apps (optional)

Domain-specific interfaces a user would "live in" for a focused session (a content
calendar, a pipeline board) can be added as Apps under the UI. Use the main UI for
system-wide concerns (inventory, governance) and Apps for one-domain deep work.
