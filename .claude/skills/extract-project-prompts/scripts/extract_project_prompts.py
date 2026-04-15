#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CLAUDE_ROOT = Path.home() / ".claude" / "projects"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", required=True, help="Chapter id like 2-2 or 10-3")
    return parser.parse_args()


def validate_chapter(chapter: str) -> str:
    if not re.fullmatch(r"\d+-\d+", chapter):
        raise SystemExit("chapter must match X-Y, for example 2-2 or 10-3")
    return chapter


def project_dir_name(project_root: Path) -> str:
    # Claude Code encodes the project path by replacing / with -
    return str(project_root).replace("/", "-")


def find_session_files(project_root: Path) -> list[Path]:
    dir_name = project_dir_name(project_root)
    project_sessions = CLAUDE_ROOT / dir_name
    if not project_sessions.exists():
        return []
    return sorted(project_sessions.glob("*.jsonl"))


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
    if stripped.startswith((
        "<local-command-caveat>",
        "<environment_context>",
        "<system-reminder>",
        "<turn_aborted>",
        "# AGENTS.md instructions",
        "# CLAUDE.md instructions",
    )):
        return True
    if stripped in {"/clear", "/help", "/bug", "/model"}:
        return True
    return False


def extract_text(content) -> str | None:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "\n".join(parts) if parts else None
    return None


def collect_prompts(session_files: list[Path]) -> list[str]:
    prompts: list[str] = []
    for path in session_files:
        for entry in load_jsonl(path):
            if entry.get("type") != "user":
                continue
            if entry.get("isMeta"):
                continue
            message = entry.get("message", {})
            if message.get("role") != "user":
                continue
            text = extract_text(message.get("content", ""))
            if not text or is_noise(text):
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
        lines.extend([
            f"### {index}",
            "",
            "```text",
            prompt,
            "```",
            "",
        ])
    return "\n".join(lines)


def main() -> None:
    chapter = validate_chapter(parse_args().chapter)
    project_root = Path.cwd().resolve()
    major = chapter.split("-", 1)[0]

    session_files = find_session_files(project_root)
    if not session_files:
        print(f"No Claude Code sessions found for project: {project_root}")

    prompts = dedupe_preserve_order(collect_prompts(session_files))

    output_dir = project_root / "docs" / "Chapter" / f"ch{major}"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{chapter}-prompts.md"
    output_path.write_text(render_markdown(chapter, prompts), encoding="utf-8")

    print(output_path)


if __name__ == "__main__":
    main()
