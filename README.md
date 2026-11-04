# WordPress Multi-Purpose Block Theme — Portable AI Core

Version: 0.2.0
Status: Architecture scaffold with deterministic provider adapter generation.

This repository provides a provider-independent foundation for AI-assisted
development. The Git repository is the source of truth for contracts, agent
definitions, workflows, state, decisions, skills, and durable artifacts.

## Principles
- Keep canonical agent intent and project knowledge in `.ai/` and `.agents/skills/`.
- Generate provider-specific files; do not maintain duplicated agent definitions.
- Treat generated files as disposable adapters, never as canonical sources.
- Persist important work as repository artifacts, not chat history.
- Require explicit review and human approval at defined gates.
- Give each task one owner and an explicit file scope.
- Do not claim a task is complete until outputs and acceptance criteria are checked.
- Report capability gaps instead of silently approximating provider behavior.

## Quick start
1. Install development dependencies: `python -m pip install -r requirements-dev.txt`.
2. Validate canonical contracts: `python scripts/validate_core.py`.
3. Generate provider adapters: `python scripts/generate_adapters.py --write`.
4. Check generated-file drift: `python scripts/generate_adapters.py --check`.
5. Customize `.ai/state/project-status.yaml` and `.ai/state/active-tasks.yaml`.
6. Review provider capability reports before relying on native runtime behavior.

## Generated adapter workflow
Edit canonical definitions in `.ai/` and skills in `.agents/skills/`, then run
the generator. Never edit generated files directly. The generator manifest is
`.ai/adapters/generated-manifest.json`. Check mode is read-only.

## Important boundary
This is a portable specification and deterministic file generator, not an active
autonomous orchestration runtime. It does not itself schedule agents, enforce
distributed locking, create provider sessions, or guarantee identical behavior
across models. Runtime permission enforcement depends on each provider.

## Repository map
- `.ai/core/`: provider-neutral governance and contracts.
- `.ai/agents/`: canonical agent definitions.
- `.ai/adapters/`: provider capability profiles and generated manifest.
- `.ai/workflows/`: canonical workflow definitions.
- `.ai/contracts/`: JSON Schemas for durable records.
- `.ai/state/`: current project and task state.
- `.agents/skills/`: portable skills.
- `.cursor/`, `.claude/`, `.codex/`: generated or provider-specific runtime adapters.
- `docs/`: durable project documentation and ADRs.
- `scripts/`: validation and adapter generation tooling.
