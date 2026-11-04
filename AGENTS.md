# Repository-wide AI instructions

## Source of truth
The Git repository is the source of truth. Do not treat chat history, model memory,
or provider-specific configuration as authoritative project state.

## Before working
1. Read this file and the relevant `.ai/core/` documents.
2. Read `.ai/state/project-status.yaml` and identify the active task.
3. Read only the requirements, decisions, skills, and artifacts relevant to that task.
4. Confirm task ownership, dependencies, expected outputs, and file scope.

## While working
- Follow the canonical agent contract in `.ai/core/agent-contract.md`.
- Follow the workflow and state rules in `.ai/core/workflow-state.md`.
- Do not silently change product scope, architecture decisions, permissions, or acceptance criteria.
- Distinguish verified facts, assumptions, and recommendations.
- Prefer official WordPress and Gutenberg documentation for platform behavior.
- Do not invent test results, citations, compatibility claims, or completed actions.
- Keep changes within the task's declared file scope.
- Ask for human approval when a gate or escalation condition requires it.

## Before handing off
- Produce every required artifact.
- Check each acceptance criterion and report evidence.
- Record unresolved questions, risks, and assumptions.
- Update task state only when the transition is valid.
- Do not mark work `COMPLETED` merely because implementation or drafting has stopped.

## Provider portability
Canonical definitions live in `.ai/` and `.agents/skills/`. Provider-specific files
are adapters only. Never make a provider-specific file the sole home of important
instructions or project knowledge.
