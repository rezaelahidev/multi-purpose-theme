# Scripts

## validate_core.py
Validates canonical agent YAML and task records against the JSON Schemas.
Run from any directory with:

```bash
python scripts/validate_core.py
```

## Adapter generation
Provider adapter generation is intentionally not enabled in v0.1. Before implementing
it, verify the current official schemas for Cursor, Claude Code, and Codex. Generation
must be deterministic, mark generated files, preserve canonical IDs, and fail when a
required capability cannot be represented safely.
