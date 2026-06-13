# PORT REGISTRY

Single source of truth for every TCP port this AOS instance uses.

**Before recommending or binding any port:** read this file AND run `ss -tlnp` to
confirm the port is actually free. Update this file whenever you add a service.

## Reserved range

Pick a private range for your AOS services and keep everything inside it, e.g.
**8760–8799**. Document each assignment below.

| Port | Service | Notes |
|------|---------|-------|
| 8765 | (example) Control UI | If you stand up the Control UI, register it here. |
|      |         |       |

## Why a registry

Port collisions are silent and maddening to debug. A registry plus a quick
`ss -tlnp` check before binding prevents two services from fighting over the same
port and documents what's listening for the next person (or agent).
