#!/usr/bin/env python3
"""Build a local evaluation task package for a harness case.

This runner intentionally does not call a model. It gathers the case input,
expected checks, selected style prompt template, rubric, quality gates, and
artifact schema into a reproducible package an agent or evaluator can run.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "harness" / "cases"
TEMPLATES_DIR = ROOT / "harness" / "templates"
RUBRICS_DIR = ROOT / "harness" / "rubrics"
GATES_DIR = ROOT / "harness" / "quality-gates"
SCHEMAS_DIR = ROOT / "harness" / "schemas"


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_case(case_id: str) -> tuple[dict[str, object], Path]:
    for path in sorted(CASES_DIR.glob("*.yaml")):
        lines = path.read_text(encoding="utf-8").splitlines()
        index = 0
        while index < len(lines):
            line = lines[index]
            if not re.match(r"\s*-\s+id:\s*", line):
                index += 1
                continue

            current: dict[str, object] = {}
            current["id"] = unquote(line.split("id:", 1)[1])
            index += 1
            while index < len(lines) and not re.match(r"\s*-\s+id:\s*", lines[index]):
                nested = lines[index]
                stripped = nested.strip()
                if stripped.startswith("skill:"):
                    current["skill"] = unquote(stripped.split(":", 1)[1])
                elif stripped.startswith("template:"):
                    current["template"] = unquote(stripped.split(":", 1)[1])
                elif stripped.startswith("input:"):
                    current["input"] = unquote(stripped.split(":", 1)[1])
                elif stripped.startswith("- ") and "expect" in current:
                    current.setdefault("expect", []).append(unquote(stripped[2:]))
                elif stripped.startswith("expect:"):
                    current["expect"] = []
                index += 1

            if current.get("id") == case_id:
                return current, path
    raise SystemExit(f"Case not found: {case_id}")


def find_template_path(skill: str, template: str | None) -> Path | None:
    if not template:
        return None

    registry = TEMPLATES_DIR / f"{skill}.yaml"
    if not registry.exists():
        raise SystemExit(f"Template registry not found: {registry.relative_to(ROOT)}")

    active = False
    for line in registry.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- id:"):
            active = unquote(stripped.split(":", 1)[1]) == template
        elif active and stripped.startswith("path:"):
            return ROOT / unquote(stripped.split(":", 1)[1])
    raise SystemExit(f"Template {template!r} not found in {registry.relative_to(ROOT)}")


def copy_if_exists(path: Path, dest: Path, target_name: str | None = None) -> str | None:
    if not path.exists():
        return None
    target = dest / (target_name or path.name)
    shutil.copy2(path, target)
    return target.name


def write_task_readme(output: Path, manifest: dict[str, object]) -> None:
    expected = "\n".join(f"- {item}" for item in manifest.get("expect", []))
    readme = f"""# Harness Task Package: {manifest["case_id"]}

## Source

- Case file: `{manifest["case_file"]}`
- Skill: `{manifest["skill"]}`
- Template: `{manifest.get("template") or "none"}`

## User Input

{manifest["input"]}

## Expected Checks

{expected}

## How To Use

1. Read `input.md`.
2. Read `manifest.json`.
3. Load the style prompt template when `template_file` is present.
4. Produce artifacts according to `travel-article-artifacts.yaml`.
5. Review with `travel-article-beautifier.yaml` rubric and quality gates.
"""
    (output / "README.md").write_text(readme, encoding="utf-8")


def write_codex_task(output: Path, manifest: dict[str, object]) -> None:
    template_file = manifest.get("template_file") or "none"
    task = f"""# Codex Harness Task

You are running a local harness case for `{manifest["skill"]}`.

## Case

- Case id: `{manifest["case_id"]}`
- Template: `{manifest.get("template") or "none"}`
- Template file: `{template_file}`

## Instructions

1. Read `input.md`.
2. Read `expected.md`.
3. Read `manifest.json`.
4. If a template file is present, follow that prompt template.
5. Produce all required artifacts from `travel-article-artifacts.yaml`.
6. Review the output with `rubric.{manifest["skill"]}.yaml`.
7. Apply `quality-gates.{manifest["skill"]}.yaml`; fix any fail-severity issue before final delivery.
8. Write final artifacts into an `output/` directory beside this task file.

## Required Final Response

After completing the case, report:

- Output directory path
- Selected style and rationale
- Quality gate pass/fail summary
- Any facts that still need verification
"""
    (output / "codex_task.md").write_text(task, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, help="Harness case id")
    parser.add_argument(
        "--out",
        default="/tmp/agent-foundry-harness",
        help="Directory where task packages are written",
    )
    args = parser.parse_args()

    case, case_file = load_case(args.case)
    skill = str(case.get("skill") or "")
    if not skill:
        raise SystemExit(f"Case {args.case} does not declare skill")

    template = case.get("template")
    template_name = str(template) if template else None
    template_path = find_template_path(skill, template_name)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output = Path(args.out).expanduser() / f"{timestamp}-{args.case}"
    output.mkdir(parents=True, exist_ok=False)

    (output / "input.md").write_text(str(case.get("input") or ""), encoding="utf-8")
    (output / "expected.md").write_text(
        "\n".join(f"- {item}" for item in case.get("expect", [])) + "\n",
        encoding="utf-8",
    )

    copied: dict[str, str | None] = {
        "case_file": copy_if_exists(case_file, output),
        "template_file": copy_if_exists(template_path, output) if template_path else None,
        "rubric_file": copy_if_exists(
            RUBRICS_DIR / f"{skill}.yaml",
            output,
            f"rubric.{skill}.yaml",
        ),
        "quality_gates_file": copy_if_exists(
            GATES_DIR / f"{skill}.yaml",
            output,
            f"quality-gates.{skill}.yaml",
        ),
        "schema_file": copy_if_exists(SCHEMAS_DIR / "travel-article-artifacts.yaml", output),
    }

    manifest: dict[str, object] = {
        "case_id": args.case,
        "skill": skill,
        "template": template_name,
        "input": case.get("input") or "",
        "expect": case.get("expect", []),
        "case_file": str(case_file.relative_to(ROOT)),
        **copied,
    }

    (output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_task_readme(output, manifest)
    write_codex_task(output, manifest)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
