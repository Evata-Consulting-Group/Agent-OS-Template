# config/

System-wide configuration that isn't a secret (secrets go in `.env` /
`.claude/settings.local.json`). Examples: app manifests for the Control UI,
allowlists for automation, shared constants.

Keep config declarative and discoverable. Anything machine-specific or sensitive
stays out of git.
