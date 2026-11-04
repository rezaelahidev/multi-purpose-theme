# Provider Adapter Generation

Canonical agent YAML and provider capability profiles are transformed by `scripts/generate_adapters.py` into Cursor, Claude Code, and Codex adapter files. Root `AGENTS.md` and portable skills remain shared canonical inputs.

## Procedure
1. Edit canonical YAML under `.ai/`.
2. Run `python scripts/validate_core.py`.
3. Run `python scripts/generate_adapters.py --write`.
4. Review generated diffs.
5. Run `python scripts/generate_adapters.py --check`.

The manifest records output hashes and ownership. It is not a security boundary. The generator refuses to overwrite non-generated files, constrains output paths, and only removes stale files recorded in the previous manifest. Prompt-level constraints do not sandbox filesystem or tool access.
