#!/usr/bin/env python3
"""Create a local workspace for a travel article beautification job."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "untitled-travel-article"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Article title or working title")
    parser.add_argument(
        "--root",
        default="/tmp/travel-article-beautifier",
        help="Workspace root directory",
    )
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    workspace = Path(args.root).expanduser() / f"{timestamp}-{slugify(args.title)}"
    workspace.mkdir(parents=True, exist_ok=False)

    files = {
        "source.md": "# Source Material\n\n",
        "brief.md": "# Article Brief\n\n",
        "article.md": "# Draft Article\n\n",
        "index.html": "<!doctype html>\n<html lang=\"zh-CN\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n  <title></title>\n</head>\n<body>\n</body>\n</html>\n",
        "review.md": "# Review Notes\n\n",
    }

    for name, content in files.items():
        (workspace / name).write_text(content, encoding="utf-8")

    print(workspace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
