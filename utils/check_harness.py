#!/usr/bin/env python3
"""Lightweight checks for harness-managed template registries."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_REGISTRY_DIR = ROOT / "harness" / "templates"
PATH_RE = re.compile(r"^\s*path:\s*(.+?)\s*$")
REFERENCE_RE = re.compile(r"^\s*-\s*((?:skills|harness|workflows|prompts)/.+\.(?:md|yaml))\s*$")


def main() -> int:
    errors: list[str] = []
    registries = sorted(TEMPLATE_REGISTRY_DIR.glob("*.yaml"))

    if not registries:
        print("No harness template registries found")
        return 0

    for registry in registries:
        for line_number, line in enumerate(registry.read_text(encoding="utf-8").splitlines(), 1):
            match = PATH_RE.match(line) or REFERENCE_RE.match(line)
            if not match:
                continue
            raw_path = match.group(1).strip().strip('"').strip("'")
            target = ROOT / raw_path
            if not target.exists():
                errors.append(f"{registry.relative_to(ROOT)}:{line_number}: missing {raw_path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: checked {len(registries)} template registry file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
