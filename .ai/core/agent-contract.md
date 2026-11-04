# Agent Contract Specification

Version: 0.3.0

## Required identity
Each canonical agent definition must include a stable `id`, human-readable `name`,
semantic `version`, `type`, `role`, and concise `mission`.

## Required operating contract
Each agent declares:
- responsibilities and capabilities;
- required and optional inputs;
- expected outputs and artifact locations;
- permissions and permitted file scope;
- constraints and escalation conditions;
- quality criteria;
- handoff target or completion destination;
- approval requirements.

## Mandatory Git branch and commit policy

**No agent, orchestrator, generated provider adapter, automation, script, or delegated
sub-agent may create a commit directly on `master` or push changes to `master`.**

1. All work that changes repository content MUST start on a dedicated, descriptive
   branch created from the latest appropriate base.
2. Every commit MUST target that working branch. Before committing, verify the checked
   out branch; if the branch is `master`, empty, detached, or cannot be verified, STOP.
3. Agents MUST NOT use GitHub Contents API or any other write API with `master` as
   the target ref. All file writes must explicitly name the approved working branch.
4. Changes reach `master` only through a Pull Request, required validation, review,
   and an authorized merge. An agent may merge only when a separate explicit task
   grants that permission and all configured gates are satisfied.
5. If branch creation, branch verification, or branch-targeted writes cannot be
   guaranteed by the active provider, the agent MUST NOT write. It must report the
   limitation and request a safe execution path.
6. Read-only inspection of `master` is allowed. Creating a branch from `master` is
   allowed. Direct mutation of `master` is never allowed.
7. This rule is provider-independent and applies equally to Cursor, Claude Code,
   Codex, future providers, humans acting through agents, and all generated adapters.

This is a mandatory governance constraint, not a suggestion. Prompt text alone may
not technically prevent a provider from writing to a protected branch. Where possible,
repository branch protection/rulesets MUST also disallow direct pushes and require PRs.
The agent must distinguish configured technical enforcement from instruction-only policy.

## Execution protocol
1. Read repository instructions and the assigned task.
2. Validate required inputs and dependencies.
3. Identify the current branch and verify it is not `master` before any write.
4. State material assumptions and missing information.
5. Work only within declared permissions and scope.
6. Create the required artifacts on the approved working branch.
7. Evaluate every acceptance criterion and attach evidence.
8. Report risks, unresolved questions, and deviations.
9. Request review or approval when required.
10. Propose a state transition; do not self-approve a human gate.

## Agent types
- `coordinator`: plans and routes work; does not silently take ownership of specialist output.
- `specialist`: creates a domain-specific deliverable.
- `reviewer`: evaluates work against independent criteria.

An agent may have multiple capabilities, but each task has one accountable owner.

## Permission semantics
Canonical permissions describe intended boundaries. The adapter must classify each
mapping as enforceable, instruction-only, unsupported, or unverified. A generated
prompt saying "do not write outside this scope" is not a filesystem sandbox.
If the runtime cannot enforce a required boundary, the agent must escalate before
performing the action rather than claim that the boundary is technically enforced.

## Completion rule
A task is complete only when required artifacts exist, acceptance criteria are checked,
required review is passed, and required human approval is recorded.
