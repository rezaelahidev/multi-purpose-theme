# Provider Adapter Specification

Version: 0.2.0
Status: Proposed — Generated Adapters

## 1. Purpose
Translate canonical agent, skill, and instruction definitions into provider conventions
without changing their meaning or overstating runtime capabilities.

## 2. Canonical inputs
- Agent contracts: `.ai/agents/*.yaml`
- Provider profiles: `.ai/adapters/providers.yaml`
- Shared repository instructions: `AGENTS.md`
- Portable skills: `.agents/skills/*/SKILL.md`
- Governance and workflow rules: `.ai/core/*.md`, `.ai/workflows/*.yaml`
- Generator implementation: `scripts/generate_adapters.py`

The provider profile is declarative metadata. It must not duplicate agent missions,
responsibilities, constraints, or project state.

## 3. Generation contract
Command:
```bash
python scripts/generate_adapters.py --write
python scripts/generate_adapters.py --check
```

- `--write` creates or updates generated outputs and removes stale outputs only when
  they are listed in the previous generated manifest.
- `--check` is read-only and exits non-zero for missing, modified, or stale generated files.
- Running `--write` repeatedly with unchanged inputs must produce no content changes.
- The manifest is written to `.ai/adapters/generated-manifest.json`.
- Every generated artifact starts with a generated-file warning and a stable marker.
- The generator must fail closed on malformed YAML, unsupported schema versions,
  duplicate agent IDs, unsafe paths, or unknown provider targets.
- It must never overwrite a non-generated file.
- It must not delete a file unless the prior manifest proves generator ownership.

## 4. Provider output strategy

### Cursor
Generate:
- `.cursor/agents/{agent-id}.md` using Cursor's project subagent Markdown format, but only after subagent support is verified.
- `.cursor/rules/ai-core.mdc` as an always-applied bridge to repository governance.

If subagent support is unverified, generate a capability report instead of native agent files.

The agent body references the canonical agent YAML, root instructions,
and relevant skills. Only metadata with a verified native mapping is emitted as
frontmatter. Tool permissions are repeated as instructions but are not represented as
enforced controls unless a tested native mapping exists.

### Claude Code
Generate:
- `.claude/agents/{agent-id}.md` using Claude Code subagent Markdown and YAML frontmatter, but only after subagent support is verified.
Existing `.claude/README.md` remains hand-maintained and is not overwritten by the generator.

The agent body references canonical contracts and requires the subagent to inspect
the active task before acting. Native tool allowlists or permission modes are not
inferred from the generic permission object in v0.2.

### OpenAI Codex
Codex uses repository-level `AGENTS.md` instructions and supports project-scoped
custom agents as standalone TOML files under `.codex/agents/`. Generate:
- `.codex/agents/{agent-id}.toml` with required `name`, `description`, and
  `developer_instructions` fields.
- `.codex/capability-report.md` describing supported and unverified mappings.
Existing `.codex/README.md` remains hand-maintained.

The root `AGENTS.md` remains human-maintained and authoritative as shared repository
guidance. It is not overwritten by the generator. Codex discovers project skills from
`.agents/skills/`; the current canonical skill layout is directly discoverable there.

## 5. Capability semantics
Each provider capability is classified as:
- `native`: documented provider feature used by the adapter.
- `shared`: achieved through repository files and instructions, not a native feature.
- `instruction-only`: described to the model but not enforced by the runtime.
- `unsupported`: no verified mapping in this adapter version.
- `unverified`: evidence is insufficient; do not claim support.

At minimum, report instruction discovery, subagent definitions, skills, tool
configuration, permission enforcement, delegation, and generated-file drift checks.

A provider's ability to read an instruction is not proof that it can enforce a
permission. Prompt-level constraints must never be labelled as security controls.

## 6. Adapter rules
1. `.ai/` and `.agents/skills/` remain canonical.
2. Generated provider files must be marked as generated.
3. Do not hand-edit generated files; edit canonical sources and regenerate.
4. If a provider requires a different schema, transform explicitly and validate.
5. Never claim capability parity without a tested compatibility check.
6. Human approval requirements must survive every mapping.
7. Do not silently drop unsupported fields; include them in the capability report.
8. Do not encode secrets, credentials, or user-specific runtime state in generated files.

## 7. Migration acceptance
A migration passes when the target runtime can:
- discover shared instructions and relevant skills;
- load the active task and project state;
- read prior artifacts and ADRs;
- continue a task without losing its acceptance criteria or approval status;
- identify generated files and their canonical sources;
- report unavailable tools, permission-enforcement gaps, and behavior differences.

## 8. Verification policy
Provider formats and capabilities change. Before adding or changing a native mapping,
verify it against current official provider documentation and record the documentation
URL and verification date in the provider profile. Existing provisional classifications must be treated as unverified until checked. An unverified mapping stays
`unverified` or `unsupported`, never `native`.
