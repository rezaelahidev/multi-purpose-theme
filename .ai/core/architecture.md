# AI-Native Architecture Specification

Version: 0.2.0
Status: Proposed baseline — generated adapter strategy

## 1. Purpose
Create a portable multi-agent engineering system for building a multi-purpose
WordPress Block Theme. The system must preserve its knowledge, contracts, workflows,
and durable state when the runtime changes between Cursor, Claude Code, and Codex.

## 2. Logical layers
1. **Governance core** — principles, contracts, approval rules, and quality gates.
2. **Agent intelligence** — canonical agent roles, capabilities, and instructions.
3. **Skills and knowledge** — reusable procedures and durable project knowledge.
4. **Workflow and state** — task lifecycle, dependencies, handoffs, and project status.
5. **Adapter generation** — deterministic transformation of canonical definitions.
6. **Runtime adapters** — provider-specific files, tool bindings, and capability mapping.

## 3. Source of truth
Git-tracked files are authoritative. Conversations are transient working context only.
Canonical definitions live in `.ai/`; portable skills live in `.agents/skills/`.
Generated provider files are disposable build artifacts and MUST NOT become the
authoritative home of agent intent, permissions, workflow logic, or project knowledge.

## 4. Generated adapter architecture
- Canonical agent definitions, provider capability profiles, and generation policy
  live under `.ai/`.
- `scripts/generate_adapters.py` transforms canonical records into provider files.
- Generation is deterministic: identical canonical inputs and generator version produce
  byte-identical outputs.
- Every generated file contains a machine-readable ownership marker.
- A generated manifest records each output path and SHA-256 digest.
- Check mode detects missing, modified, and stale generated files without changing
  the working tree.
- Write mode may replace or remove only files previously declared as generator-owned.
- Hand-edited generated output is drift, not a source of truth. Edit canonical inputs
  and regenerate.
- Provider-specific unsupported capabilities must be reported explicitly.

## 5. Architecture constraints
- Provider-independent intent must not be encoded only in provider-specific files.
- Every task has one accountable owner at a time.
- Every task declares inputs, outputs, acceptance criteria, and permitted file scope.
- Important decisions are recorded as ADRs.
- State changes must follow the task lifecycle.
- Human approval is required at configured gates.
- Permissions follow least privilege.
- A prompt-level permission description is not equivalent to an enforceable runtime
  permission boundary. The adapter must distinguish the two.
- Runtime capability gaps must be reported, never silently ignored.

## 6. Initial execution model
The first iteration is file-based and human-supervised. It does not require a separate
orchestration server or framework. Generation and validation are local deterministic
commands. A future runtime may automate scheduling, locking, and delegation without
changing canonical contracts.

## 7. Portability boundary
Portability means preserving definitions, artifacts, state, and governance. It does
not promise identical model reasoning, tool availability, permission enforcement, or
execution behavior. Each adapter must document unsupported or differently implemented
capabilities. Native provider configuration is an integration surface, not the core.

## 8. Non-goals for v0.2
- Autonomous deployment or release.
- Unattended modification of product scope or ADRs.
- Distributed multi-agent concurrency.
- Provider-specific model tuning.
- A custom agent execution framework.
- Automatic translation of arbitrary tool permissions into provider-native security
  policies without a verified mapping.
