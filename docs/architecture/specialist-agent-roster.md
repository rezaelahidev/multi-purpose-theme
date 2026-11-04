# Initial WordPress Block Theme Agent Roster

Version: 0.1.0
Status: Proposed baseline

## Purpose

Define the first domain-facing agent group after the portable core and provider migration smoke test. These contracts are canonical in `.ai/agents/*.yaml`; provider-specific files are generated and must not be edited manually.

## Agent roster

| Agent | Type | Primary responsibility | Output boundary |
|---|---|---|---|
| Master Orchestrator | Coordinator | Owns task routing, dependencies, state proposals, and approval gates | Task plans, handoffs, state proposals |
| Research Agent | Specialist | Produces evidence-backed ecosystem and platform research | Research reports |
| Product Architect | Specialist | Defines approved product scope, requirements, and MVP | Product brief, requirements, MVP scope |
| Theme Architect | Specialist | Converts approved requirements into a Block Theme architecture | Theme architecture, file structure, compatibility matrix |
| QA Agent | Reviewer | Independently reviews artifacts and validates acceptance evidence | QA review and test strategy |

## Responsibility boundaries

### Product Architect
- Owns product definition, not technical architecture.
- Converts research and approved goals into testable requirements.
- Labels evidence, assumptions, proposals, and approved decisions separately.
- Cannot expand MVP scope or approve the Product Scope gate.

### Theme Architect
- Owns technical architecture for the WordPress Block Theme.
- Must use native Block Theme capabilities where appropriate and justify custom code.
- Documents WordPress/PHP compatibility and core-vs-plugin feature dependencies.
- Does not implement theme files during architecture tasks and cannot approve the Architecture gate.

### QA Agent
- Is an independent reviewer, not an implementation owner.
- Reviews artifacts against explicit acceptance criteria and recorded evidence.
- Must distinguish passed, failed, and not-verifiable checks.
- Does not modify the artifact under review or approve a human gate.

## Default handoff sequence

`Research Agent -> Product Architect -> Human Product Scope Approval -> Theme Architect -> Human Architecture Approval -> QA Agent -> Master Orchestrator`

The sequence is a default routing path, not permission to skip dependencies or approval gates. QA may be invoked continuously on incremental artifacts; it is not restricted to the end of the project.

## Human approval gates

1. Product Scope: human approval required before product scope is treated as fixed.
2. Architecture: human approval required before implementation begins.
3. Design System baseline: human approval required before the system is treated as canonical.
4. Release: human approval required before release.

Agents may prepare proposals and evidence for a gate, but cannot approve it.

## Next specialist expansion

After the initial contracts and generated adapters pass CI, add the implementation-facing specialists in bounded increments:
- UX/UI Architect
- Design System Agent
- Block Development Agent
- Template Engineer
- Pattern Engineer
- Performance Agent
- Security Agent
- Documentation Agent

Do not activate these agents until their inputs, outputs, file scopes, skills, and independent QA expectations are defined.
