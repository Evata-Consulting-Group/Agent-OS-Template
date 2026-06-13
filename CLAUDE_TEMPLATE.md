# {Project Name}

{One or two sentences: what this project IS and what it does. Include the domain/URL if it's a website.}

## Scope

{What this project handles. What it does NOT handle (and who does).}

## Owning Agent

{Which agent in `/agents/<name>.md` owns this project.}

## Project Structure

```
{Key folders and files with one-line descriptions. Not every file — just the ones an agent needs to know about.}
```

## Before You Edit

1. Read the file you're changing
2. {Check the relevant config/schema/template}
3. {Verify shared tool signatures in the actual tool file before calling them}
4. {Check the router if touching UI}

## Key Tools & Runners

| Component | Location |
|-----------|----------|
| {name} | `{path}` |

## Current State

- **Status**: {active | maintenance | blocked | dormant}
- {Key milestone or metric}
- {Blockers if any}

## Deployment

{How to deploy changes. Include the exact command. Skip this section for non-deployed projects.}

---

## Usage Notes

- **Required sections**: Scope, Owning Agent, Project Structure, Before You Edit, Current State
- **Optional sections**: Key Tools & Runners (skip if none), Deployment (skip if not deployed), Conventions, Schedule
- **Length target**: 40–80 lines for simple projects, 80–150 for complex ones
- **Keep current**: Update "Current State" when project state changes
- **No duplication**: Don't repeat what's in the root CLAUDE.md or subfolder CLAUDE.md files
