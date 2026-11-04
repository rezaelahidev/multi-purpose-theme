# Core tooling

Validate canonical records with `python scripts/validate_core.py`.

Generate provider adapters with `python scripts/generate_adapters.py --write`.

Check generated-file drift without modifying files with `python scripts/generate_adapters.py --check`.

The generator refuses to overwrite non-generated files and removes stale files only when recorded in the previous generated manifest.
