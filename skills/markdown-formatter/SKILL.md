---
name: markdown-formatter
description: Format, clean, restructure, and normalize Markdown while preserving source meaning. Use when the user asks to convert rough notes, outlines, drafts, meeting notes, reports, or plain text into readable Markdown with headings, lists, tables, links, code fences, or consistent style.
---

# Markdown Formatter

## Overview

Convert messy source material into clear Markdown without changing its meaning. Preserve important wording, code, links, numbers, and hierarchy unless the user asks for rewriting.

## Workflow

1. Detect the desired output shape: article, notes, README, checklist, changelog, table, or report.
2. Preserve facts, ordering, and quoted material unless the user asks for editorial changes.
3. Normalize headings, bullets, numbering, tables, links, and code fences.
4. Use concise labels for sections and avoid decorative formatting.
5. Return only the formatted artifact when the user asks for direct formatting.

## Formatting Rules

- Use ATX headings (`#`, `##`, `###`).
- Use fenced code blocks with language info when known.
- Prefer tables only when comparison is clearer than bullets.
- Keep nested bullets shallow.
- Do not invent links or citations.

## Output Checklist

- Valid Markdown
- Stable hierarchy
- Original meaning preserved
- No unexplained omissions
