#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


CLAUDE_ROOT = Path.home() / ".claude" / "projects"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["preview", "purge"], required=True)
    return parser.parse_args()


def project_dir_name(project_root: Path) -> str:
    # Claude Code encodes the project path by replacing / with -
    return str(project_root).replace("/", "-")


def find_session_files(project_root: Path) -> list[Path]:
    dir_name = project_dir_name(project_root)
    project_sessions = CLAUDE_ROOT / dir_name
    if not project_sessions.exists():
        return []
    files = [f for f in project_sessions.glob("*.jsonl")]
    return sorted(files, key=lambda f: f.stat().st_mtime)


def main() -> None:
    args = parse_args()
    project_root = Path.cwd().resolve()
    session_files = find_session_files(project_root)

    if not session_files:
        print("No project sessions found.")
        return

    keep_file = session_files[-1]
    purge_files = session_files[:-1]

    print(f"Keep:  {keep_file}")
    print("Purge:")
    for path in purge_files:
        print(f"  {path}")

    if args.mode == "preview":
        return

    for path in purge_files:
        path.unlink(missing_ok=True)

    print(f"\nRemoved sessions: {len(purge_files)}")


if __name__ == "__main__":
    main()
