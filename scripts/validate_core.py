#!/usr/bin/env python3
"""Validate canonical JSON Schemas, YAML records, and cross references."""
import json, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[1]

def read_yaml(path):
    with path.open(encoding="utf-8") as f: return yaml.safe_load(f)

def load_schema(name):
    data=json.loads((ROOT/".ai/contracts"/(name+".schema.json")).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(data)
    print("PASS schema meta-validation: "+name)
    return data

def validate(data,schema,label):
    errors=sorted(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(data),key=lambda e:(list(map(str,e.path)),e.message))
    if errors:
        print("FAIL "+label)
        for e in errors: print("  - "+(".".join(map(str,e.path)) or "<root>")+": "+e.message)
        return False
    print("PASS "+label); return True

def main():
    ok=True; schemas={}
    for name in ("agent","task","decision"):
        try: schemas[name]=load_schema(name)
        except Exception as e: print("FAIL schema "+name+": "+str(e)); ok=False
    agents=set()
    for path in sorted((ROOT/".ai/agents").glob("*.yaml")):
        try:
            doc=read_yaml(path); ok=validate(doc,schemas["agent"],str(path.relative_to(ROOT))) and ok
            agents.add(doc["agent"]["id"])
        except Exception as e: print("FAIL "+str(path)+": "+str(e)); ok=False
    try:
        tasks=read_yaml(ROOT/".ai/state/active-tasks.yaml")["tasks"]
        ids={t.get("id") for t in tasks}
        for task in tasks:
            ok=validate(task,schemas["task"],"task "+str(task.get("id"))) and ok
            if task.get("assigned_agent")!="human" and task.get("assigned_agent") not in agents:
                print("FAIL unknown task owner: "+str(task.get("assigned_agent"))); ok=False
            for dep in task.get("dependencies",[]):
                if dep not in ids: print("FAIL unknown task dependency: "+dep); ok=False
    except Exception as e: print("FAIL task records: "+str(e)); ok=False
    try:
        state=read_yaml(ROOT/".ai/state/project-status.yaml")
        if not isinstance(state,dict) or not isinstance(state.get("project"),dict): raise ValueError("project object missing")
        print("PASS project status structure")
    except Exception as e: print("FAIL project status: "+str(e)); ok=False
    for path in sorted((ROOT/".ai/workflows").glob("*.yaml")):
        try:
            workflow=read_yaml(path)["workflow"]
            if not workflow.get("id") or not isinstance(workflow.get("steps"),list): raise ValueError("workflow id/steps missing")
            for step in workflow["steps"]:
                if step.get("owner") not in agents: raise ValueError("unknown workflow owner "+str(step.get("owner")))
            print("PASS "+str(path.relative_to(ROOT)))
        except Exception as e: print("FAIL "+str(path.relative_to(ROOT))+": "+str(e)); ok=False
    return 0 if ok else 1

if __name__=="__main__": sys.exit(main())
