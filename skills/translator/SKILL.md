---
name: translator
description: Translate text between languages while preserving meaning, tone, formatting, terminology, and domain context. Use when the user asks for translation, bilingual polishing, localization, glossary-aware rendering, or naturalization of literal machine translation.
---

# Translator

## Overview

Translate faithfully and naturally. Preserve formatting and intent, adapt idioms when needed, and call out ambiguous source text instead of silently guessing.

## Workflow

1. Identify source language, target language, audience, tone, locale, and domain.
2. Preserve headings, lists, tables, links, code, placeholders, and proper nouns unless asked to adapt them.
3. Translate meaning rather than word order; keep terminology consistent.
4. Flag ambiguities, culturally specific phrases, or terms that may need a glossary.
5. Provide alternatives only when the user asks or when a phrase has meaningful tradeoffs.

## Style Guidance

- Prefer natural target-language phrasing over literal syntax.
- Keep brand names, API names, file paths, and code identifiers unchanged unless instructed.
- For professional writing, use a calm and precise tone by default.
- For marketing or social content, preserve persuasion without adding unsupported claims.

## Output Checklist

- Faithful meaning
- Natural target-language style
- Formatting preserved
- Ambiguities or glossary needs noted
