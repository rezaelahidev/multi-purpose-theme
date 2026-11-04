# WordPress Multi-Purpose Block Theme — Portable AI Core

Version: 0.1.0  
Status: Architecture scaffold; not an active autonomous orchestration runtime.

This package provides a provider-independent foundation for AI-assisted development.
The canonical source of truth is the Git repository: contracts, agent definitions,
workflow definitions, state, decisions, and durable artifacts.

## Principles

- Keep agent intent and project knowledge outside provider-specific configuration.
- Treat Cursor, Claude Code, and Codex files as runtime adapters.
- Persist important work as repository artifacts, not chat history.
- Require explicit review and human approval at defined gates.
- Give each task one owner and an explicit file scope.
- Do not claim a task is complete until its outputs and acceptance criteria are checked.

## Quick start

1. Copy the contents of this package into the root of the theme repository.
2. Review `AGENTS.md` and `CLAUDE.md`.
3. Install development dependencies: `python -m pip install -r requirements-dev.txt`.
4. Run: `python scripts/validate_core.py`.
5. Customize `.ai/state/project-status.yaml` and `.ai/state/active-tasks.yaml`.
6. Review the adapter notes before enabling provider-specific agents.

## Important boundary

This is a portable specification and scaffold. It does not itself execute agents,
schedule tasks, provide distributed locking, or guarantee identical behavior across
models. Runtime-specific agent files are generated or maintained as thin adapters.
The human remains the authority for product scope, architecture changes, and release.

## Repository map

- `.ai/core/`: provider-neutral governance and contracts.
- `.ai/agents/`: canonical agent definitions.
- `.ai/workflows/`: canonical workflow definitions.
- `.ai/contracts/`: JSON Schemas for durable records.
- `.ai/state/`: current project and task state.
- `.agents/skills/`: portable skills.
- `.cursor/`, `.claude/`, `.codex/`: provider-specific runtime adapters.
- `docs/`: durable project documentation and ADRs.
- `scripts/`: validation and adapter tooling.
