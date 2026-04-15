#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SESSION_ROOT = Path.home() / ".codex" / "sessions"
HISTORY_FILE = Path.home() / ".codex" / "history.jsonl"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", required=True, help="Chapter id like 2-2 or 10-3")
    return parser.parse_args()


def validate_chapter(chapter: str) -> str:
    if not re.fullmatch(r"\d+-\d+", chapter):
        raise SystemExit("chapter must match X-Y, for example 2-2 or 10-3")
    return chapter


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


def is_noise(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    if stripped.startswith(
        (
            "<environment_context>",
            "<turn_aborted>",
            "# AGENTS.md instructions",
            "# CLAUDE.md instructions",
        )
    ):
        return True
    if stripped in {"/clear", "/help", "/bug", "/mpdel"}:
        return True
    return False


def session_id_from_path(path: Path) -> str | None:
    match = re.search(r"([0-9a-f]{8,}-[0-9a-f-]+)\.jsonl$", path.name)
    return match.group(1) if match else None


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
    return matched


def collect_session_prompts(session_files: list[Path]) -> tuple[list[str], set[str]]:
    prompts: list[str] = []
    session_ids: set[str] = set()

    for path in session_files:
        session_id = session_id_from_path(path)
        if session_id:
            session_ids.add(session_id)

        for entry in load_jsonl(path):
            payload = entry.get("payload", {})
            if payload.get("type") != "user_message":
                continue
            text = payload.get("message", "")
            if is_noise(text):
                continue
            prompts.append(text.strip())

    return prompts, session_ids


def collect_history_prompts(session_ids: set[str]) -> list[str]:
    if not HISTORY_FILE.exists() or not session_ids:
        return []

    prompts: list[str] = []
    for entry in load_jsonl(HISTORY_FILE):
        if entry.get("session_id") not in session_ids:
            continue
        text = entry.get("text", "")
        if is_noise(text):
            continue
        prompts.append(text.strip())
    return prompts


def dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def render_markdown(chapter: str, prompts: list[str]) -> str:
    lines = [f"# {chapter} prompts", "", "## Prompts", ""]
    if not prompts:
        lines.extend(["目前沒有找到 prompts。", ""])
        return "\n".join(lines)

    for index, prompt in enumerate(prompts, start=1):
        lines.extend(
            [
                f"### {index}",
                "",
                "```text",
                prompt,
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> None:
    chapter = validate_chapter(parse_args().chapter)
    project_root = Path.cwd().resolve()
    major = chapter.split("-", 1)[0]

    session_files = collect_project_session_files(project_root)
    session_prompts, session_ids = collect_session_prompts(session_files)
    history_prompts = collect_history_prompts(session_ids)
    prompts = dedupe_preserve_order(session_prompts + history_prompts)

    output_dir = project_root / "docs" / "Chapter" / f"ch{major}"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{chapter}-prompts.md"
    output_path.write_text(render_markdown(chapter, prompts), encoding="utf-8")

    print(output_path)


if __name__ == "__main__":
    main()
