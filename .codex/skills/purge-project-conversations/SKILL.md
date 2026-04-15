---
name: purge-project-conversations
description: Remove all local Codex conversation records related to the current project except the current latest project conversation. Use when the user wants to clear past project conversations after extracting prompts, so the next chapter starts from a clean state.
---

# Purge Project Conversations

Use this skill when the user wants to keep the current conversation and delete every other local Codex conversation record related to the current project.

## Behavior

1. Treat the current working directory as the project root.
2. Find all local Codex session files for this project from `~/.codex/sessions`.
3. Keep the latest matching session as the current conversation.
4. Delete every other matching project session.
5. Remove matching entries from:
   - `~/.codex/history.jsonl`
   - `~/.codex/log/codex-tui.log`
   - `~/.codex/shell_snapshots/`
6. Leave the latest matching session untouched.

## Modes

- `preview`: show what would be removed and what would be kept
- `purge`: perform the cleanup

## Command

```bash
python3 .codex/skills/purge-project-conversations/scripts/purge_project_conversations.py --mode preview
python3 .codex/skills/purge-project-conversations/scripts/purge_project_conversations.py --mode purge
```

## Notes

- The kept session is the latest matching project session by timestamp in its filename.
- This skill is destructive in `purge` mode.
