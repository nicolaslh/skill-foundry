#!/usr/bin/env python3
"""Install local skills into the Codex skills directory."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCAL_SKILLS = ROOT / "skills"
DEFAULT_DEST = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills"


class SkipInstall(Exception):
    """Destination already exists and should be left untouched."""


def skill_dirs(names: list[str], install_all: bool) -> list[Path]:
    if install_all:
        return sorted(path for path in LOCAL_SKILLS.iterdir() if path.is_dir())
    if not names:
        raise SystemExit("Provide at least one skill name or use --all")
    result = []
    missing = []
    for name in names:
        path = LOCAL_SKILLS / name
        if not path.is_dir():
            missing.append(name)
            continue
        result.append(path)
    if missing:
        raise SystemExit(f"Skill(s) not found: {', '.join(missing)}")
    return result


def backup_path(dest: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return dest.with_name(f"{dest.name}.backup.{timestamp}")


def prepare_dest(dest: Path, overwrite: bool, backup_existing: bool) -> None:
    if not dest.exists() and not dest.is_symlink():
        return
    if backup_existing:
        backup = backup_path(dest)
        dest.rename(backup)
        print(f"Backed up {dest} -> {backup}")
        return
    if overwrite:
        if dest.is_symlink() or dest.is_file():
            dest.unlink()
        else:
            shutil.rmtree(dest)
        print(f"Removed existing {dest}")
        return
    raise SkipInstall(f"already exists at {dest}")


def install_skill(
    source: Path, dest_root: Path, method: str, overwrite: bool, backup_existing: bool
) -> str:
    dest = dest_root / source.name
    try:
        dest_root.mkdir(parents=True, exist_ok=True)
        prepare_dest(dest, overwrite, backup_existing)
        if method == "copy":
            shutil.copytree(source, dest)
        elif method == "symlink":
            dest.symlink_to(source, target_is_directory=True)
        else:
            raise SystemExit(f"Unknown method: {method}")
    except SkipInstall as skip:
        print(f"Skipped {source.name}: {skip} (use --overwrite or --backup-existing to replace)")
        return "skipped"
    except OSError as error:
        print(f"Failed {source.name} -> {dest}: {error}", file=sys.stderr)
        return "failed"
    print(f"Installed {source.name} -> {dest} ({method})")
    return "installed"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=f"{__doc__} Skills that already exist at the destination are skipped.",
    )
    parser.add_argument("skills", nargs="*", help="Skill names to install")
    parser.add_argument("--all", action="store_true", help="Install all local skills")
    parser.add_argument("--dest", default=str(DEFAULT_DEST), help="Destination skills directory")
    parser.add_argument("--method", choices=("copy", "symlink"), default="copy")
    parser.add_argument("--overwrite", action="store_true", help="Remove existing destination first")
    parser.add_argument("--backup-existing", action="store_true", help="Backup existing destination first")
    args = parser.parse_args()

    if args.overwrite and args.backup_existing:
        raise SystemExit("Choose only one of --overwrite or --backup-existing")

    dest_root = Path(args.dest).expanduser()
    tally = {"installed": 0, "skipped": 0, "failed": 0}
    for source in skill_dirs(args.skills, args.all):
        status = install_skill(
            source, dest_root, args.method, args.overwrite, args.backup_existing
        )
        tally[status] += 1

    print(
        f"Summary: {tally['installed']} installed, "
        f"{tally['skipped']} skipped, {tally['failed']} failed"
    )
    return 1 if tally["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
