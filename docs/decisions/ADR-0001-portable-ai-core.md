# ADR-0001: Provider-independent AI core

- Status: proposed
- Date: 2026-11-04
- Decision makers: Project owner

## Context
The project may move between Cursor, Claude Code, and OpenAI Codex. Important agent
instructions, skills, workflow state, and project knowledge must not be trapped in
one provider's configuration or conversation history.

## Decision
Maintain canonical agent/workflow definitions and governance in Git-tracked,
provider-neutral files. Use provider-specific adapters only for runtime integration.
Use portable skills and explicit contracts. Keep the initial orchestration model
file-based and human-supervised.

## Alternatives considered
1. Provider-native configuration as the sole source — rejected due to lock-in.
2. A custom orchestration service from day one — deferred due to unnecessary initial
   complexity and additional operational burden.
3. Provider-neutral files plus thin adapters — selected.

## Consequences
- Additional adapter and validation work is required.
- Runtime behavior will not be identical across providers.
- Migration can preserve durable artifacts and state.
- Human review remains necessary for architecture and release decisions.
