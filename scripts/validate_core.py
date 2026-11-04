#!/usr/bin/env python3
"""Validate canonical YAML agent/task records against JSON Schemas."""
from pathlib import Path
import json
import sys
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def validate_yaml(path: Path, schema_path: Path, data_key=None):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if data_key:
        data = data[data_key]
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data),
        key=lambda e: list(e.path)
    )
    if errors:
        print(f"FAIL {path.relative_to(ROOT)}")
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"  - {location}: {error.message}")
        return False
    print(f"PASS {path.relative_to(ROOT)}")
    return True

def main():
    checks = [
        (ROOT / ".ai/agents/orchestrator.yaml", ROOT / ".ai/contracts/agent.schema.json", None),
        (ROOT / ".ai/agents/research-agent.yaml", ROOT / ".ai/contracts/agent.schema.json", None),
    ]
    ok = all(validate_yaml(*check) for check in checks)
    tasks_path = ROOT / ".ai/state/active-tasks.yaml"
    task_schema = json.loads((ROOT / ".ai/contracts/task.schema.json").read_text(encoding="utf-8"))
    tasks = yaml.safe_load(tasks_path.read_text(encoding="utf-8"))["tasks"]
    validator = Draft202012Validator(task_schema)
    for task in tasks:
        errors = list(validator.iter_errors(task))
        if errors:
            ok = False
            print(f"FAIL task {task.get('id', '<unknown>')}")
            for error in errors:
                print(f"  - {error.message}")
        else:
            print(f"PASS task {task['id']}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
