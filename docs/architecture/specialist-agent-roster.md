# WordPress Block Theme Agent Roster

Version: 0.2.0
Status: Expanded roster proposed for human review

## Purpose

Define a portable, provider-independent team for the WordPress Multi-Purpose Block Theme. Canonical contracts live in `.ai/agents/*.yaml`; provider-specific agent files are generated and must not be edited manually.

## Agent roster

| Agent | Type | Responsibility |
|---|---|---|
| Master Orchestrator | Coordinator | Task routing, dependencies, state proposals, and approval gates |
| Research Agent | Specialist | Evidence-backed platform, ecosystem, and competitor research |
| Product Architect | Specialist | Product definition, requirements, and MVP scope |
| Theme Architect | Specialist | Block Theme architecture, compatibility, and technical decisions |
| UX/UI Architect | Specialist | User journeys, information architecture, responsive interaction specifications |
| Design System Agent | Specialist | Design tokens, theme.json mapping, global styles, and style variations |
| Block Development Agent | Specialist | Approved custom Gutenberg block implementation |
| Template Engineer | Specialist | Block Theme templates and template parts |
| Pattern Engineer | Specialist | Reusable block patterns and pattern categories |
| QA Agent | Reviewer | Independent quality, acceptance, compatibility, and accessibility review |
| Performance Agent | Reviewer | Measurement-led performance assessment and regression review |
| Security Agent | Reviewer | Independent WordPress security and trust-boundary review |
| Documentation Agent | Specialist | User, developer, and contributor documentation |

## Responsibility and file ownership boundaries

- **Product Architect** owns product definition, requirements, and MVP scope; it does not own technical architecture.
- **Theme Architect** owns technical architecture and compatibility decisions; it does not implement theme source during architecture tasks.
- **UX/UI Architect** owns user journeys and interaction specifications; it proposes design tokens but does not approve or unilaterally define the design-system baseline.
- **Design System Agent** owns token definitions and theme.json design-system mapping. Changes to `theme.json` require coordination with Theme Architect and human Design System approval.
- **Block Development Agent** owns custom block source only when native blocks, patterns, variations, and styles cannot satisfy an approved requirement.
- **Template Engineer** owns `templates/` and `parts/` implementation.
- **Pattern Engineer** owns `patterns/` implementation and pattern documentation.
- **QA Agent**, **Performance Agent**, and **Security Agent** are reviewers. They report findings and do not modify the artifact under review or approve human gates.
- **Documentation Agent** owns documentation outputs and must distinguish planned, implemented, and released behavior.
- **Master Orchestrator** owns task coordination and state proposals, not specialist implementation.

## Default workflow

`Research -> Product Architect -> Human Product Scope Approval -> Theme Architect -> Human Architecture Approval -> UX/UI Architect -> Design System Agent -> Human Design System Approval -> Implementation Specialists -> Continuous QA / Performance / Security Review -> Documentation -> Human Release Approval`

This is a dependency-aware default, not a rigid serial pipeline. QA, performance, and security reviews may be invoked incrementally. Independent tasks may proceed in parallel only when file ownership and dependencies do not conflict. State writes remain single-writer in the current workflow.

## Human approval gates

1. **Product Scope**: required before scope is treated as fixed.
2. **Architecture**: required before implementation begins.
3. **Design System baseline**: required before tokens and visual rules are treated as canonical.
4. **Release**: required before a release is published.

Agents may prepare proposals and evidence, but cannot approve gates.

## Implementation safeguards

- Theme implementation is blocked until Product Scope, Architecture, and Design System approvals are recorded.
- Custom blocks require an explicit justification against native WordPress capabilities.
- Every implementation task must declare an exclusive or coordinated file scope.
- Reviewer agents must remain independent of the implementation owner.
- CI evidence is required for automated test claims; manual runtime checks must be identified as manual.
- Provider adapter capability gaps must remain visible and must not be silently emulated.

## Next phase

After this expanded roster passes schema, generated-adapter, and CI validation, review the agent contracts and approve the Design System/UX foundation work. Do not begin broad Theme implementation until the relevant human approval gates are satisfied.
