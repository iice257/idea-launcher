#!/usr/bin/env python3
"""Find unresolved Idea Launcher template placeholders."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PLACEHOLDER = re.compile(r"\{\{[A-Z0-9_]+\}\}")
DEFAULT_EXCLUDES = {".git", "node_modules", ".next", "dist", "build", "__pycache__"}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in DEFAULT_EXCLUDES for part in path.parts):
            continue
        yield path


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate that generated project docs have no unresolved placeholders.")
    parser.add_argument("path", nargs="?", default=".", help="Project path to scan.")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    findings = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            matches = PLACEHOLDER.findall(line)
            if matches:
                findings.append((path, line_number, ", ".join(sorted(set(matches)))))

    if findings:
        print("Unresolved placeholders found:")
        for path, line_number, matches in findings:
            print(f"{path}:{line_number}: {matches}")
        raise SystemExit(1)

    print(f"No unresolved placeholders found under {root}")


if __name__ == "__main__":
    main()
