import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_adapters as generator


def agent(agent_id="sample-agent"):
    return {
        "id": agent_id,
        "name": "Sample Agent",
        "version": "1.0.0",
        "mission": "Perform a bounded sample task.",
        "responsibilities": ["inspect"],
        "inputs": {"required": ["task"]},
        "outputs": {"required": ["report"]},
        "skills": [],
        "constraints": ["Stay in scope."],
        "quality": {"criteria": ["Evidence is present."]},
    }


def profiles(subagents="unverified", verified=False):
    result = {}
    for provider in sorted(generator.PROVIDERS):
        result[provider] = {
            "verification_status": "verified" if verified else "pending",
            "last_verified": "2026-11-04" if verified else None,
            "capabilities": {
                "subagents": subagents if provider in {"cursor", "claude-code"} else "unverified",
                "skills": "shared",
            },
            "documentation": ["https://example.org/docs"],
        }
    return result


class GeneratorRenderTests(unittest.TestCase):
    def test_render_is_deterministic(self):
        first = generator.render(profiles(), [agent()])
        second = generator.render(profiles(), [agent()])
        self.assertEqual(first, second)

    def test_pending_profiles_do_not_emit_native_subagents(self):
        output = generator.render(profiles(), [agent()])
        self.assertIn(".cursor/capability-report.md", output)
        self.assertIn(".claude-code/capability-report.md", output) if ".claude-code/capability-report.md" in output else self.assertIn(".claude/capability-report.md", output)
        self.assertNotIn(".cursor/agents/sample-agent.md", output)
        self.assertNotIn(".claude/agents/sample-agent.md", output)

    def test_native_capability_requires_verified_profile_in_cli(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            (root / ".ai/adapters/providers.yaml").write_text(
                "version: '1.0'\nproviders:\n" +
                "\n".join(
                    f"  {name}:\n    verification_status: pending\n    last_verified: null\n    capabilities:\n      subagents: native\n"
                    for name in sorted(generator.PROVIDERS)
                ),
                encoding="utf-8",
            )
            (root / ".ai/agents/sample.yaml").write_text(
                "agent:\n  id: sample-agent\n  name: Sample\n  version: '1.0'\n  mission: Test\n",
                encoding="utf-8",
            )
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", root / ".ai/adapters/generated-manifest.json"), patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(generator.main(), 2)

    def test_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(generator, "ROOT", Path(temp)):
                with self.assertRaises(ValueError):
                    generator.safe_path("../outside.txt")

    def test_manifest_write_then_check_is_clean(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            import yaml
            cfg = {"version": "1.0", "providers": profiles()}
            (root / ".ai/adapters/providers.yaml").write_text(yaml.safe_dump(cfg), encoding="utf-8")
            (root / ".ai/agents/sample.yaml").write_text(yaml.safe_dump({"agent": agent()}), encoding="utf-8")
            manifest = root / ".ai/adapters/generated-manifest.json"
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", manifest):
                with patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(generator.main(), 0)
                with patch.object(sys, "argv", ["generate_adapters.py", "--check"]), contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(generator.main(), 0)

    def test_non_generated_file_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            import yaml
            (root / ".ai/adapters/providers.yaml").write_text(yaml.safe_dump({"version": "1.0", "providers": profiles()}), encoding="utf-8")
            (root / ".ai/agents/sample.yaml").write_text(yaml.safe_dump({"agent": agent()}), encoding="utf-8")
            target = root / ".cursor/rules/ai-core.mdc"
            target.parent.mkdir(parents=True)
            target.write_text("hand maintained content\n", encoding="utf-8")
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", root / ".ai/adapters/generated-manifest.json"), patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(generator.main(), 2)
            self.assertEqual(target.read_text(encoding="utf-8"), "hand maintained content\n")

    def test_stale_generated_file_is_removed_only_if_marked(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            import yaml
            (root / ".ai/adapters/providers.yaml").write_text(yaml.safe_dump({"version": "1.0", "providers": profiles()}), encoding="utf-8")
            (root / ".ai/agents/sample.yaml").write_text(yaml.safe_dump({"agent": agent()}), encoding="utf-8")
            manifest = root / ".ai/adapters/generated-manifest.json"
            stale = root / ".cursor/agents/retired-agent.md"
            stale.parent.mkdir(parents=True)
            stale.write_text(generator.MARKER + "\nretired\n", encoding="utf-8")
            manifest.write_text(json.dumps({"version": 1, "files": {".cursor/agents/retired-agent.md": "a" * 64}}), encoding="utf-8")
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", manifest), patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(generator.main(), 0)
            self.assertFalse(stale.exists())

    def test_unmarked_stale_file_is_preserved_and_fails_safely(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            import yaml
            (root / ".ai/adapters/providers.yaml").write_text(yaml.safe_dump({"version": "1.0", "providers": profiles()}), encoding="utf-8")
            (root / ".ai/agents/sample.yaml").write_text(yaml.safe_dump({"agent": agent()}), encoding="utf-8")
            manifest = root / ".ai/adapters/generated-manifest.json"
            stale = root / ".cursor/agents/retired-agent.md"
            stale.parent.mkdir(parents=True)
            stale.write_text("manual content\n", encoding="utf-8")
            manifest.write_text(json.dumps({"version": 1, "files": {".cursor/agents/retired-agent.md": "oldhash"}}), encoding="utf-8")
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", manifest), patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(generator.main(), 2)
            self.assertEqual(stale.read_text(encoding="utf-8"), "manual content\n")


    def test_non_output_manifest_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(generator, "ROOT", Path(temp)):
                with self.assertRaises(ValueError):
                    generator.safe_path(".cursor/README.md")

    def test_symlink_output_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".cursor/rules").mkdir(parents=True)
            outside = root / "AGENTS.md"
            outside.write_text("hand maintained\n", encoding="utf-8")
            (root / ".cursor/rules/ai-core.mdc").symlink_to(outside)
            with patch.object(generator, "ROOT", root):
                with self.assertRaises(ValueError):
                    generator.safe_path(".cursor/rules/ai-core.mdc")

    def test_manifest_cannot_delete_hand_maintained_provider_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            import yaml
            (root / ".ai/adapters/providers.yaml").write_text(yaml.safe_dump({"version": "1.0", "providers": profiles()}), encoding="utf-8")
            (root / ".ai/agents/sample.yaml").write_text(yaml.safe_dump({"agent": agent()}), encoding="utf-8")
            manifest = root / ".ai/adapters/generated-manifest.json"
            manual = root / ".cursor/README.md"
            manual.parent.mkdir(parents=True)
            manual.write_text(generator.MARKER + "\nmanual readme\n", encoding="utf-8")
            manifest.write_text(json.dumps({"version": 1, "files": {".cursor/README.md": "oldhash"}}), encoding="utf-8")
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", manifest), patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(generator.main(), 2)
            self.assertTrue(manual.exists())


    def test_verified_profiles_emit_native_agent_files_for_all_providers(self):
        output = generator.render(profiles(subagents="native", verified=True), [agent()])
        self.assertIn(".cursor/agents/sample-agent.md", output)
        self.assertIn(".claude/agents/sample-agent.md", output)
        self.assertIn(".codex/agents/sample-agent.toml", output)
        self.assertIn('developer_instructions = "', output[".codex/agents/sample-agent.toml"])
        self.assertIn(".codex/capability-report.md", output)

    def test_codex_generated_path_is_allowed(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(generator, "ROOT", Path(temp)):
                path = generator.safe_path(".codex/agents/research-agent.toml")
                self.assertEqual(path, Path(temp) / ".codex/agents/research-agent.toml")

    def test_invalid_calendar_verification_date_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            import yaml
            cfg = {"version": "1.0", "providers": profiles(subagents="native", verified=True)}
            cfg["providers"]["cursor"]["last_verified"] = "2026-99-45"
            (root / ".ai/adapters/providers.yaml").write_text(yaml.safe_dump(cfg), encoding="utf-8")
            (root / ".ai/agents/sample.yaml").write_text(yaml.safe_dump({"agent": agent()}), encoding="utf-8")
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", root / ".ai/adapters/generated-manifest.json"), patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(generator.main(), 2)

    def test_manifest_rejects_unapproved_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".ai/adapters").mkdir(parents=True)
            (root / ".ai/agents").mkdir(parents=True)
            import yaml
            (root / ".ai/adapters/providers.yaml").write_text(yaml.safe_dump({"version": "1.0", "providers": profiles()}), encoding="utf-8")
            (root / ".ai/agents/sample.yaml").write_text(yaml.safe_dump({"agent": agent()}), encoding="utf-8")
            manifest = root / ".ai/adapters/generated-manifest.json"
            manifest.write_text(json.dumps({"version": 1, "files": {"AGENTS.md": "a" * 64}}), encoding="utf-8")
            with patch.object(generator, "ROOT", root), patch.object(generator, "MANIFEST", manifest), patch.object(sys, "argv", ["generate_adapters.py", "--write"]), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(generator.main(), 2)



if __name__ == "__main__":
    unittest.main()
