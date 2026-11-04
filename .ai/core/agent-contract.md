# Agent Contract Specification

## Required identity
Each canonical agent definition must include a stable `id`, human-readable `name`,
semantic `version`, `role`, and concise `mission`.

## Required operating contract
Each agent declares:
- responsibilities and capabilities;
- required and optional inputs;
- expected outputs and artifact locations;
- permissions and file scope;
- constraints and escalation conditions;
- quality criteria;
- handoff target or completion destination;
- approval requirements.

## Execution protocol
1. Read repository instructions and the assigned task.
2. Validate required inputs and dependencies.
3. State material assumptions and missing information.
4. Work only within declared permissions and scope.
5. Create the required artifacts.
6. Evaluate every acceptance criterion and attach evidence.
7. Report risks, unresolved questions, and deviations.
8. Request review or approval when required.
9. Propose a state transition; do not self-approve a human gate.

## Agent types
- `coordinator`: plans and routes work; does not silently take ownership of specialist output.
- `specialist`: creates a domain-specific deliverable.
- `reviewer`: evaluates work against independent criteria.

An agent may have multiple capabilities, but each task has one accountable owner.

## Completion rule
A task is complete only when required artifacts exist, acceptance criteria are checked,
required review is passed, and required human approval is recorded.
