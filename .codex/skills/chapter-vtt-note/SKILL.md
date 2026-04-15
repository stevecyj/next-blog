---
name: chapter-vtt-note
description: Turn a course subtitle transcript file such as a VTT markdown file into a chapter learning note. Use when the user provides a subtitle file and wants the core ideas, practical development actions, and a note written to a target markdown path like docs/Chapter/ch2/2-3-note.md.
---

# Chapter VTT Note

Use this skill when the user gives a course subtitle file and wants a structured study note extracted from it.

## Expected inputs

- A subtitle transcript path, typically like `docs/Chapter/ch2/2-3-vtt.md`
- Optionally a target note path, typically like `docs/Chapter/ch2/2-3-note.md`

If the user does not provide a note path, infer it by replacing `-vtt.md` with `-note.md`.

## Required outputs

Produce a note in Traditional Chinese with these sections:

1. `# X-Y 標題`
2. `## 核心內容`
3. `## 開發上可採取的行動步驟`
4. `## 我可以立刻採取的實作清單`
5. `## 總結`

## Workflow

1. Read the subtitle file first.
2. Identify the real learning objective of the chapter, not just a transcript summary.
3. Separate:
   - concepts the learner should understand
   - concrete actions the learner can take in development work
4. Check local project context when needed:
   - existing note files in the same chapter
   - the actual project structure if the transcript talks about files or tooling
   - local framework docs if the chapter may contain version-sensitive claims
5. Write or update the target note file.

## Quality bar

- Do not copy the subtitle line by line.
- Compress repetitive teaching filler into concise conclusions.
- Prefer practical, reusable guidance over passive summary.
- State the main learning objective directly. Avoid padded contrast patterns like `不是…而是…` unless the contrast is genuinely necessary for technical accuracy.
- If the transcript contains outdated or version-sensitive claims, correct them against the local project and local docs before writing.
- Keep the note actionable: the learner should be able to do something immediately after reading it.

## Output style

- Write in Traditional Chinese.
- Prefer concise headings and high-signal bullets.
- Prefer direct statements over rhetorical framing. Do not use `不是…而是…` as a default explanatory template.
- When the chapter is about a concrete codebase, anchor the note to real file paths and current project structure.
- When a specific path is provided, write the result directly to that file instead of only replying in chat.

## Invocation examples

Example 1:

```text
使用 $chapter-vtt-note，根據 docs/Chapter/ch2/2-3-vtt.md 整理這一節的核心內容與開發上的行動步驟，並寫入 docs/Chapter/ch2/2-3-note.md
```

Example 2:

```text
用 $chapter-vtt-note 處理 docs/Chapter/ch5/5-1-vtt.md。請先整理核心內容與可執行步驟，再把筆記寫到對應的 -note.md 檔案。
```
