#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CODEX_ROOT = Path.home() / ".codex"
SESSION_ROOT = CODEX_ROOT / "sessions"
HISTORY_FILE = CODEX_ROOT / "history.jsonl"
LOG_FILE = CODEX_ROOT / "log" / "codex-tui.log"
SNAPSHOT_ROOT = CODEX_ROOT / "shell_snapshots"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["preview", "purge"], required=True)
    return parser.parse_args()


def load_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def session_id_from_path(path: Path) -> str | None:
    match = re.search(r"([0-9a-f]{8,}-[0-9a-f-]+)\.jsonl$", path.name)
    return match.group(1) if match else None


def session_sort_key(path: Path) -> str:
    match = re.search(r"rollout-(\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2})-", path.name)
    return match.group(1) if match else path.name


def collect_project_session_files(project_root: Path) -> list[Path]:
    if not SESSION_ROOT.exists():
        return []

    project_root_str = str(project_root)
    matched: list[Path] = []
    for path in sorted(SESSION_ROOT.rglob("*.jsonl")):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if f'"cwd":"{project_root_str}"' in text:
            matched.append(path)
    return sorted(matched, key=session_sort_key)


def rewrite_jsonl_excluding_session_ids(path: Path, session_ids: set[str]) -> bool:
    if not path.exists():
        return False

    kept_lines: list[str] = []
    changed = False

    with path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.rstrip("\n")
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                kept_lines.append(raw_line)
                continue

            if entry.get("session_id") in session_ids:
                changed = True
                continue

            kept_lines.append(raw_line if raw_line.endswith("\n") else raw_line + "\n")

    if changed:
        path.write_text("".join(kept_lines), encoding="utf-8")
    return changed


def rewrite_text_excluding_tokens(path: Path, tokens: set[str]) -> bool:
    if not path.exists():
        return False

    original = path.read_text(encoding="utf-8")
    filtered_lines = [line for line in original.splitlines(True) if not any(token in line for token in tokens)]
    updated = "".join(filtered_lines)

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def delete_snapshot_files(session_ids: set[str]) -> list[Path]:
    deleted: list[Path] = []
    if not SNAPSHOT_ROOT.exists():
        return deleted

    for path in SNAPSHOT_ROOT.glob("*.sh"):
        if any(session_id in path.name for session_id in session_ids):
            path.unlink(missing_ok=True)
            deleted.append(path)
    return deleted


def main() -> None:
    args = parse_args()
    project_root = Path.cwd().resolve()
    session_files = collect_project_session_files(project_root)

    if not session_files:
        print("No project sessions found.")
        return

    keep_file = session_files[-1]
    purge_files = session_files[:-1]
    purge_session_ids = {sid for sid in (session_id_from_path(path) for path in purge_files) if sid}

    print(f"Keep: {keep_file}")
    print("Purge:")
    for path in purge_files:
        print(path)

    if args.mode == "preview":
        return

    for path in purge_files:
        path.unlink(missing_ok=True)

    rewrite_jsonl_excluding_session_ids(HISTORY_FILE, purge_session_ids)
    rewrite_text_excluding_tokens(LOG_FILE, purge_session_ids | {str(project_root)})
    deleted_snapshots = delete_snapshot_files(purge_session_ids)

    print(f"Removed sessions: {len(purge_files)}")
    print(f"Removed snapshots: {len(deleted_snapshots)}")


if __name__ == "__main__":
    main()
