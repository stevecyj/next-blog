---
name: extract-project-prompts
description: Extract all prompts used so far for the current project from local Claude Code session files, then write them to a chapter prompts markdown file. Use when the user asks to collect, recover, export, or update prompts for a chapter like 2-2, 10-3, or 26-12 into docs/Chapter/chX/X-Y-prompts.md.
---

# Extract Project Prompts

Use this skill when the user wants all prompts used so far for the current project, saved into a chapter prompts file.

## Input format

Expect a chapter id in the form `X-Y`.

Examples:

- `2-2`
- `2-10`
- `10-3`
- `26-12`

## Behavior

1. Treat the current working directory as the project root.
2. Parse local Claude Code session files from `~/.claude/projects/<project-dir>/`.
3. Keep only project-related user prompts.
4. Remove noise such as local command caveats, meta messages, and empty turns.
5. Deduplicate prompts while preserving first-seen order.
6. Write the result to `docs/Chapter/chX/X-Y-prompts.md`.

## Command

Run:

```bash
python3 .claude/skills/extract-project-prompts/scripts/extract_project_prompts.py --chapter X-Y
```

Replace `X-Y` with the requested chapter id.

## Output path rule

- Chapter `2-2` -> `docs/Chapter/ch2/2-2-prompts.md`
- Chapter `10-3` -> `docs/Chapter/ch10/10-3-prompts.md`

## Notes

- The skill always deduplicates.
- The skill overwrites the target prompts file.
- If the target chapter directory does not exist, the script creates it.
