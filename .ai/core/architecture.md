# AI-Native Architecture Specification

Version: 0.1.0  
Status: Proposed baseline

## 1. Purpose
Create a portable multi-agent engineering system for building a multi-purpose
WordPress Block Theme. The system must preserve its knowledge, contracts, workflows,
and durable state when the runtime changes between Cursor, Claude Code, and Codex.

## 2. Logical layers

1. **Governance core** — principles, contracts, approval rules, and quality gates.
2. **Agent intelligence** — canonical agent roles, capabilities, and instructions.
3. **Skills and knowledge** — reusable procedures and durable project knowledge.
4. **Workflow and state** — task lifecycle, dependencies, handoffs, and project status.
5. **Runtime adapters** — provider-specific files, tool bindings, and capability mapping.

## 3. Source of truth
Git-tracked files are authoritative. Conversations are transient working context only.
The canonical definitions are stored in `.ai/`; portable skills are stored in
`.agents/skills/`. Provider-specific files must remain thin adapters.

## 4. Architecture constraints
- Provider-independent intent must not be encoded only in provider-specific files.
- Every task has one accountable owner at a time.
- Every task declares inputs, outputs, acceptance criteria, and permitted file scope.
- Important decisions are recorded as ADRs.
- State changes must follow the task lifecycle.
- Human approval is required at configured gates.
- Permissions follow least privilege.
- Runtime capability gaps must be reported, never silently ignored.

## 5. Initial execution model
The first iteration is file-based and human-supervised. It does not require a separate
orchestration server or framework. A future runtime may automate scheduling, locking,
and delegation without changing the canonical contracts.

## 6. Portability boundary
Portability means preserving definitions, artifacts, state, and governance. It does
not promise identical model reasoning, tool availability, or execution behavior.
Each adapter must document unsupported or differently implemented capabilities.

## 7. Non-goals for v0.1
- Autonomous deployment or release.
- Unattended modification of product scope or ADRs.
- Distributed multi-agent concurrency.
- Provider-specific model tuning.
- A custom agent execution framework.
