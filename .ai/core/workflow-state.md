# Workflow and State Management Specification

## Task lifecycle
`BACKLOG -> READY -> IN_PROGRESS -> REVIEW -> APPROVED -> COMPLETED`

Additional states:
- `BLOCKED`: a dependency or required input prevents progress.
- `REJECTED`: review failed; return to `IN_PROGRESS` with actionable feedback.
- `ON_HOLD`: explicitly paused by a human.
- `FAILED`: execution ended unsuccessfully.
- `CANCELLED`: explicitly cancelled.

## State transition rules
- Only tasks whose dependencies are satisfied may become `READY`.
- An assigned owner moves a task to `IN_PROGRESS`.
- Work moves to `REVIEW` only when required artifacts are present.
- A reviewer records findings and either rejects or recommends approval.
- Human-required approvals must be performed by the human.
- `COMPLETED` requires passed criteria and all required approvals.

## State storage
The initial implementation stores state in `.ai/state/`. Keep edits small and serialized.
Do not have multiple agents concurrently write the same state file. Use one state owner
(the orchestrator or human) to apply transitions.

## Handoff
A handoff must identify the source task, receiving role, artifact paths, open questions,
risks, and the next expected action.

## Context restoration
At session start, read `AGENTS.md`, project status, active tasks, relevant ADRs,
and the artifacts explicitly referenced by the active task. Do not load the entire
repository by default.

## Concurrency limitation
The file-based v0.1 model is single-writer. If parallel execution is introduced,
add locking or transactional state management before allowing concurrent state writes.
