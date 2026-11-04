# Provider Adapter Specification

## Purpose
Translate canonical agent, skill, and instruction definitions into the conventions
of a runtime without changing their meaning.

## Adapter responsibilities
- expose shared repository instructions;
- register or render canonical agent roles in the provider's native format;
- make skills discoverable using supported paths;
- map tools and permissions where possible;
- identify unsupported capabilities;
- preserve canonical IDs and versions;
- validate generated files for drift.

## Adapter rules
1. `.ai/` and `.agents/skills/` remain canonical.
2. Generated provider files must be marked as generated.
3. Do not hand-edit generated files; edit canonical sources and regenerate.
4. If a provider requires a different schema, transform explicitly and validate.
5. Never claim capability parity without a tested compatibility check.
6. Human approval requirements must survive every mapping.

## Initial targets
- Cursor
- Claude Code
- OpenAI Codex

## Capability matrix
Maintain a versioned matrix covering project instructions, subagents, skills,
MCP/tool configuration, permission controls, and delegation behavior. Recheck it
against current official documentation before each adapter implementation.

## Migration acceptance
A migration passes when the new runtime can:
- discover shared instructions and relevant skills;
- load the active task and project state;
- read prior artifacts and ADRs;
- continue a task without losing its acceptance criteria or approval status;
- report any unavailable tools or behavior differences.
