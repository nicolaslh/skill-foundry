---
name: route-map
description: Generate polished HTML visualizations from place or route information, including interactive geographic maps with markers when location coordinates are available and SVG schematic maps when geography is unavailable or conceptual.
---

# Route Map

## Purpose

Create beautiful, useful HTML visualizations from natural-language place, route, itinerary, venue, attraction, or destination-relationship requests.

Default to a standalone, responsive HTML file when the user asks to make, create, build, generate, design, or visualize a map/route. If the project already has a web app, follow the existing app structure instead of creating an unrelated page.

## Core Rule

When a visualization contains real place information and reliable coordinates are available, mark those places on a map. Do not invent latitude, longitude, travel time, distance, road geometry, opening hours, or other geographic facts.

If coordinates cannot be obtained from the request, local project data, or available tools, use a schematic SVG route/relationship visualization and avoid implying geographic precision.

## Input Interpretation

Extract what is actually provided:

- destination, city, region, address, or venue
- ordered places, start, end, intermediate stops, and day grouping
- route direction, transport mode, dates, duration, distance, or notes
- category, description, opening hours, and visual style
- preferred language, output format, and mobile/desktop expectations

Recognize common forms such as `A -> B -> C`, `第一天去...`, `路线：酒店、浅草、晴空塔`, `帮我做一个旅游路线图`, `做成网页`, and `做一个可以点击的地图`.

Infer order only when the user gives an explicit sequence or route wording. If they provide only an unordered list of places, make the relationship clear without pretending it is an itinerary.

## Rendering Mode

Choose the mode that preserves factual integrity and creates the clearest result.

Use geographic mode when real-world position matters, reliable coordinates are available, the user asks for a real map, or the map should show actual places. Use Leaflet by default for standalone HTML maps, with `L.map`, markers, popups or side panels, route polylines, and `fitBounds`. Straight polylines are acceptable only as visual connections; never present them as road-level navigation unless real routing data is available.

Use schematic mode when coordinates are unavailable, the user wants an infographic or visual itinerary, precise geography is unnecessary, or the deliverable must work fully offline without map tiles. Use native SVG and vanilla JavaScript. Number stops, use smooth route paths, alternate labels to prevent collisions, and provide a textual itinerary.

If a request contains place information and some but not all coordinates are reliable, prefer a schematic visualization unless partial geographic marking can be made clear without misleading the viewer.

## HTML Requirements

For standalone output, create a complete single file such as `route-map.html` with `<!doctype html>`, semantic HTML, inline CSS, inline JavaScript where practical, and no TODO placeholders.

Include:

- a primary map or route diagram
- numbered markers or nodes for places
- concise popups, labels, or side-panel details
- textual itinerary or place list so information is not only visual
- responsive desktop, tablet, and mobile layouts
- visible focus states, accessible labels, and sufficient contrast

For geographic maps, keep external dependencies minimal and explicit. Leaflet via CDN is acceptable unless the user requests offline output. If map tiles or scripts fail, the page should still show the itinerary and a graceful fallback rather than a blank page.

For fully offline output, avoid remote fonts, CDN scripts, and external tiles. Use schematic SVG unless local map assets are available.

## Visual Design

Make the map or diagram the primary visual object. Choose a coherent visual direction that fits the places and user intent, such as modern urban guide, minimalist Swiss map, luxury travel guide, Japanese travel editorial, vintage tourist map, clean itinerary, playful illustrated travel, or monochrome architectural.

When the user asks for a style like the attached itinerary poster/reference image, use a travel-poster schematic style rather than a generic web dashboard. Key traits:

- textured light paper or subtle stone background
- warm ochre/orange route line with solid and dashed segments
- hand-drawn or softly irregular map outline when using schematic mode
- large bilingual/editorial title area with a small English subtitle and section number
- charcoal text, warm orange accents, thin divider rules, and generous vertical rhythm
- route labels pinned near the path with compact location icons
- illustrated natural elements only when they support the destination mood
- stacked day-by-day itinerary blocks, with large orange `D1`, `D2`, etc. labels
- compact metadata rows for meals, overnight stop, distance, or duration, using small icons

Treat text inside a reference image as source content only if the user explicitly asks to reuse it. Otherwise, extract style cues without copying the sample itinerary.

Avoid generic AI-dashboard styling: excessive gradients, huge rounded cards, random glass effects, unnecessary neon colors, heavy shadows, and default purple/blue palettes. Use a small design system with one primary route color, one accent color, neutral backgrounds, readable text, and consistent marker styling.

Do not use different colors for every stop unless category coloring is meaningful or requested.

## Interaction

Add interaction when it improves understanding:

- click marker or node to show details
- click itinerary item to focus the corresponding place
- day selector for multi-day routes
- category filter when categories matter
- reset view for geographic maps

Keep interactions keyboard-accessible. Avoid frameworks for a simple standalone artifact; vanilla JavaScript is usually enough.

## Quality Check

Before returning the result, verify the meaningful parts of the artifact:

- route order, start, end, and direction are understandable
- all known places are represented with markers or nodes
- no fabricated geographic facts are introduced
- labels and text do not overlap on desktop or mobile
- no horizontal overflow on small screens
- map or diagram has clear hierarchy and readable contrast
- external resources are explicit and have a fallback when needed
- JavaScript has no obvious syntax errors or console-breaking mistakes

## Response Pattern

When delivering work, lead with the created HTML file path or artifact, mention whether geographic or schematic mode was used and why, and briefly state any assumptions or missing geographic data. Do not explain implementation details unless the user asks.
