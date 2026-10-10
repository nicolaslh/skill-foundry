---
name: h3-prompt-writer
description: Generate structured MiniMax-H3 / ComfyUI video prompts from character, reference image, scene, plot, dialogue, camera, and voice requirements. Use when the user asks for 视频提示词, 分镜提示词, MiniMax-H3 prompt, ComfyUI video prompt, or any prompt using the Subject / S / Shot / says syntax.
---

# H3 Prompt Writer

## Overview

Turn loose character, scene, plot, dialogue, camera, and voice notes into a prompt that can be pasted straight into a MiniMax-H3 / ComfyUI video workflow. The deliverable is not a prose video description; it is a structured prompt with stable bindings.

Default output language is Chinese, because the fixed syntax and dialogue tags are Chinese. Structural tokens stay in their original form regardless of the user's language.

## Core Rule

Never change the fixed syntax. Only replace character, scene, plot, dialogue, camera action, and voice content.

```text
<Subject> / <Picture> / S / [Shot] / says / <d>
```

Token priority, highest first:

```text
<SubjectX>
<Picture X>
S X
[Shot X]
<Subject X> (SX) says:
<d>[Chinese]...</d>
```

## Reference Image Binding

`<Picture X>` anchors a character to a supplied reference image and is what keeps appearance from drifting. It is part of the fixed syntax, not optional decoration.

- Number pictures in the order the user supplied them, and keep that mapping stable.
- Say where the character sits inside that image, such as 画面左侧 or 画面右侧, so a multi-character reference image resolves correctly.
- Two characters from the same image share the picture number and differ by position.
- When no reference image exists, drop the `<Picture X>` clause and describe appearance directly. Never invent a picture number.

## Input Intake

Collect what the user actually gave, per character and per scene:

- character: name, number, reference image, position in the image, face, hair, clothing, body proportion, props, overall look
- voice: gender, age feel, register, timbre, default pace, volume, sentence endings, emotion variants, forbidden voice styles
- scene: place, time, weather, light, background, environment objects, ambient sound
- relations: left/right position, distance, body facing, eyeline, hand state, prop state
- plot: synopsis, behavior, emotional turns, dialogue, closing action
- shots: user-supplied shot list, shot count, or target duration

When shots are not supplied, split the plot into shots yourself. When the user fixes a shot count or duration, follow it exactly.

## Workflow

1. Parse characters and assign `<SubjectX>` numbers.
2. Assign one `S` number per speaking character, matching its Subject number.
3. Bind each character to its `<Picture X>` reference image and position, then lock visual features from that image instead of inventing them.
4. Lock voice features: fixed attributes, emotion variants, forbidden styles.
5. Build the scene block and the spatial relationship block.
6. Read the plot as a timeline, then split it into shots.
7. Give each shot a shot size, camera position, action chain, micro-actions, expression, and prop state.
8. Bind dialogue to the correct speaker with `says` and `<d>[Chinese]...</d>`.
9. Audit continuity across characters, voices, props, and space.
10. Append the forbidden list and the forced declaration.
11. Run the quality check, then output the full prompt.

## Fixed Structure

The prompt is always assembled in this order:

```text
Subject -> Voice / S -> Scene -> Spatial Continuity -> Shot Timeline -> Dialogue Binding -> Global Constraints
```

Use `references/prompt-template.md` for the exact block templates, the full output template, and worked examples. Copy those templates verbatim and swap only the bracketed content.

Use `references/craft-guide.md` for voice attribute lists, shot selection, action chains, the micro-action library, continuity rules, and the full quality checklist.

## Non-Negotiables

- Keep `<Subject>` tokens; never downgrade them to plain character descriptions.
- Keep S bindings; S1 speaks only Subject1's lines, S2 only Subject2's.
- Never introduce an undefined speaker, and never put two characters' lines in one `says`.
- Keep dialogue inside `<d>[Chinese]...</d>`; plain quotes are not acceptable.
- Do not merge shots into one prose paragraph, and do not trade action clarity for literary flourish.
- Do not add background music, subtitles, UI, logos, or on-screen text unless the user explicitly asks.
- Preserve user-supplied lines as written. Polish only when asked, and stay inside the character's voice setting.
- Prefer continuity of character, prop, space, and action over variety.
- Do not swap character numbers or left/right positions between shots.

## Missing Information

If a detail is missing but reasonably inferable, take the most conservative, context-consistent option and keep generating. Ask the user only when the gap would break character identity, plot logic, or shot execution.

## Quality Check

Before returning the prompt, verify:

- Subject numbers are unique, and appearance, clothing, and props stay consistent
- every character with a reference image carries `<Picture X>` plus a position, and picture numbers match the supplied images
- every speaking character has a unique S number that matches its Subject
- each voice block has fixed attributes, emotion variants, and forbidden styles
- each shot has a shot size, a readable action order, and needed micro-actions
- shots are continuous, with no unexplained prop, position, or wardrobe jumps
- dialogue uses `says` and `<d>[Chinese]...</d>`, bound to the right speaker
- the forbidden list and forced declaration are present, with no music unless requested

`references/craft-guide.md` holds the expanded checklist.

## Response Pattern

Lead with the complete prompt. Then list only material assumptions, inferred details, or shot-split decisions the user may want to change. Skip explanation of the syntax itself unless asked.
