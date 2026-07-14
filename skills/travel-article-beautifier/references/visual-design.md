# Visual Design

Use this reference when the output should be visually polished, especially for HTML.

## Design Principles

- Let destination and route become the design system.
- Keep the first screen strong: title, subtitle, route/date cue, and one clear visual anchor.
- Use section rhythm: immersive scene, practical block, image or quote, next scene.
- Avoid generic decorative gradients when a route, map, photograph, texture, or timeline can carry the article.
- Keep mobile layout readable with comfortable line length and stable spacing.

## Theme Directions

### Field Journal

- Paper-like background
- Serif title, readable body type
- Timestamp, coordinates, route notes
- Good for slow travel and reflective essays

### City Magazine

- Strong grid, large title, editorial captions
- Photo strips and neighborhood blocks
- Good for city guides and stylish weekend trips

### Route Map

- Timeline spine, leg cards, transport notes
- Good for road trips, train routes, and multi-city journeys

### Minimal Gallery

- Big images, short captions, sparse prose
- Good for photography-led travelogues

### Practical Guide

- Dense but clean sections, tables, checklists, tips
- Good for itinerary and planning content

## Template Registry

Use the harness registry at `harness/templates/travel-article-beautifier.yaml` to select and audit AI-readable style prompt templates. The actual prompt templates live under `skills/travel-article-beautifier/references/style-templates/`.

## HTML Components

- Hero section
- Route overview
- Timeline
- Scene section
- Pull quote
- Practical tips
- Photo grid
- Cost or time note, only if supplied or verified
- Closing card with route summary
