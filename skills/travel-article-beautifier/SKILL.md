---
name: travel-article-beautifier
description: Beautify travel notes, diaries, itineraries, photo captions, route logs, or rough drafts into polished travel articles with narrative structure, visual layout direction, Markdown or HTML presentation, and publication-ready finishing. Use when the user asks to 美化游记, polish a travel article, turn trip notes into an illustrated article, create a travelogue layout, or produce a share-ready destination story.
---

# Travel Article Beautifier

## Overview

Transform raw travel material into a polished travelogue. Preserve the user's actual experience, elevate structure and prose, and produce a visually guided article that can be delivered as Markdown or a self-contained HTML page.

This skill is inspired by article-beautification workflows that separate source intake, planning, staged composition, visual design, review, and final delivery. For travel writing, add special attention to route logic, sensory detail, local context, photo placement, maps/timelines, and fact-sensitive travel claims.

## Workflow

1. Create a per-article workspace before large edits:
   `python3 skills/travel-article-beautifier/scripts/scaffold_workspace.py --title "<title>"`
2. Gather source material: notes, dates, route, places, photos, audience, destination, tone, platform, and required format.
3. Normalize the source into a brief before writing. See `references/source-intake.md`.
4. Route the style with `references/style-router.md`, then read the selected prompt template from `references/style-templates/`.
5. Choose article type and structure. See `references/article-types.md`.
6. Choose visual direction, section rhythm, and optional HTML treatment. See `references/visual-design.md`.
7. Draft the first screen or opening section first when producing an HTML or visually rich article. Confirm the tone and layout direction when the user is available.
8. Build the full article in sections: hook, route or story arc, scenes, practical notes, reflections, and close.
9. Run the travel-specific review checklist. See `references/review-checklist.md`.
10. Deliver the final artifact and mention any assumptions, unverified facts, or suggested assets.

## Output Modes

- Markdown article: best for blogs, newsletters, notes, or later CMS import.
- Self-contained HTML article: best when the user asks for article beautification, a visual travelogue, a shareable page, or design-heavy presentation.
- Social derivative: optional title variants, excerpt, cover copy, tags, and platform captions.

## Style Templates

When the user asks for a visual style, select one of the harness-managed templates registered in `harness/templates/travel-article-beautifier.yaml`.

- `field-journal`: reflective, slow, textured travel diary.
- `city-magazine`: editorial city guide with strong grid and captions.
- `route-map`: chronology-first route and timeline article.
- `minimal-gallery`: image-led visual essay.
- `practical-guide`: scan-friendly itinerary and planning guide.

Read the selected prompt template from `references/style-templates/<template-id>.md`, apply its recognition signals and prompt instructions, and keep the template's intended article rhythm unless the user asks for a different style.

Use `workflows/travel-article-beautifier.yaml` as the full execution path when the user asks for a complete transformation from raw material to final article.

## Travel Writing Rules

- Do not invent visited places, personal feelings, prices, opening hours, safety conditions, visa rules, or transport schedules.
- Mark uncertain live facts for verification.
- Preserve route order when the user's experience depends on chronology.
- Use concrete travel detail: weather, light, sounds, smells, textures, food, movement, waiting, and transitions.
- Keep practical information separate from reflective prose when the article needs both.
- Prefer a distinctive but readable article over decorative excess.

## HTML Build Guidance

When creating HTML, produce a single `index.html` with embedded CSS unless the user asks for a project. Include responsive layout, stable typography, image placeholders or real user-provided images, and sections that work without external build tools.

Use visual devices that fit travel content:

- Route timeline
- Destination cards
- Pull quotes
- Photo strips
- Practical tip boxes
- Map placeholder or route summary
- Closing itinerary summary

## Delivery Checklist

- Article has a clear travel promise and target reader.
- Structure supports either chronology, destination discovery, or thematic reflection.
- Visual hierarchy is intentional and mobile-friendly.
- User-provided facts are preserved.
- Unverified current facts are flagged.
- Final output includes file paths when artifacts are written locally.
