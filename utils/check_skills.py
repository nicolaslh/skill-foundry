#!/usr/bin/env python3
"""Lightweight repository checks for local skill folders."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening YAML frontmatter fence"]

    try:
        _, raw_frontmatter, _ = text.split("---\n", 2)
    except ValueError:
        return {}, ["missing closing YAML frontmatter fence"]

    data: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, errors


def check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    frontmatter, parse_errors = parse_frontmatter(skill_md)
    errors.extend(f"{skill_dir.name}: {error}" for error in parse_errors)

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not name:
        errors.append(f"{skill_dir.name}: missing frontmatter name")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{skill_dir.name}: invalid skill name {name!r}")
    elif name != skill_dir.name:
        errors.append(f"{skill_dir.name}: name does not match directory ({name!r})")

    if not description:
        errors.append(f"{skill_dir.name}: missing frontmatter description")
    elif "TODO" in description:
        errors.append(f"{skill_dir.name}: description still contains TODO")

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if not agent_yaml.exists():
        errors.append(f"{skill_dir.name}: missing agents/openai.yaml")
    else:
        agent_text = agent_yaml.read_text(encoding="utf-8")
        for required in ("display_name:", "short_description:", "default_prompt:"):
            if required not in agent_text:
                errors.append(f"{skill_dir.name}: agents/openai.yaml missing {required}")
        if "TODO" in agent_text:
            errors.append(f"{skill_dir.name}: agents/openai.yaml still contains TODO")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills directory does not exist", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    errors = [error for skill_dir in skill_dirs for error in check_skill(skill_dir)]

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: checked {len(skill_dirs)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
