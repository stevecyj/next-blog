---
name: purge-project-conversations
description: Remove all local Claude Code conversation records related to the current project except the current latest project conversation. Use when the user wants to clear past project conversations after extracting prompts, so the next chapter starts from a clean state.
---

# Purge Project Conversations

Use this skill when the user wants to keep the current conversation and delete every other local Claude Code conversation record related to the current project.

## Behavior

1. Treat the current working directory as the project root.
2. Find all session files for this project in `~/.claude/projects/<project-dir>/`.
3. Keep the latest matching session as the current conversation.
4. Delete every other matching project session.

## Modes

- `preview`: show what would be removed and what would be kept
- `purge`: perform the cleanup

## Command

```bash
python3 .claude/skills/purge-project-conversations/scripts/purge_project_conversations.py --mode preview
python3 .claude/skills/purge-project-conversations/scripts/purge_project_conversations.py --mode purge
```

## Notes

- The kept session is the latest matching project session by file modification time.
- This skill is destructive in `purge` mode.
