# workflows/

**Global** workflow specs. Project-specific workflows live under
`/<domain>/.../workflows/` and resolve first; these are the global fallback.

A workflow is a defined, orchestrated sequence (not autonomous). Each one conforms
to the Workflow Spec in
[docs/architecture/workflow-and-component-specs.md](../docs/architecture/workflow-and-component-specs.md):
YAML frontmatter (Name, Owner, Maturity, Trigger, Cost_Profile) plus Purpose,
Requires, Inputs, Outputs, Steps (with Decision Contracts on judgment steps),
Evaluation, and Reflection.

**Protection rule:** creating a new workflow is fine when it's part of directed
work; **overwriting or deleting** an existing one requires the operator's explicit
approval.

See `example_workflow.md` for a complete, minimal spec. Delete it once you have
real workflows.
