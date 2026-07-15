# HTML Diagram Patterns

Use this reference when generating polished HTML diagrams, code-derived diagrams, or multi-view architecture artifacts.

## Default Document Shape

Create a single self-contained HTML document:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Diagram title</title>
  <style>
    /* Inline CSS only. */
  </style>
</head>
<body>
  <main class="diagram-page">
    <header>...</header>
    <section class="diagram-shell" aria-label="...">...</section>
    <aside class="notes">...</aside>
  </main>
</body>
</html>
```

Use English or the user's language for labels. If the user writes in Chinese, prefer Chinese labels.

## Visual Grammar

- Actor/user: rounded pill or avatar-like card.
- Service/module: rounded rectangle.
- Data store: cylinder-like SVG shape or card with database icon text.
- Queue/event bus: hexagon, capsule, or card labeled as async.
- Decision: diamond.
- External system: dashed border.
- Trust/security boundary: translucent group box with dashed border.
- Critical path: stronger stroke and primary color.
- Optional/error path: dashed stroke and muted color.

Keep labels short. Put details in side notes rather than stuffing nodes.

## Layout Patterns

### Flowchart

- Arrange left-to-right for product/user flows.
- Arrange top-to-bottom for operational pipelines.
- Give each decision two clearly labeled exits.
- Show loops explicitly and label retry/rollback paths.

### Architecture

- Group by boundary: client, edge/API, application services, data, external dependencies, observability.
- Show direction of data or control flow with arrows.
- Avoid more than three visual hierarchy levels in one diagram.
- If deployment and logical architecture differ, produce two sections instead of merging them.

### Sequence

- Use vertical lifelines or horizontal lanes.
- Number important messages.
- Mark async/evented handoffs distinctly.
- Keep only the main success path in the diagram; put failure paths in notes unless requested.

### Dependency Graph

- Group by package, layer, or owner.
- Draw dependency arrows from consumer to dependency unless the user specifies the opposite.
- Highlight cycles, heavy fan-in/fan-out, or forbidden dependencies when visible.

## Styling

Use a calm default palette:

- Background: `#f8fafc`
- Surface: `#ffffff`
- Text: `#0f172a`
- Muted text: `#64748b`
- Primary: `#2563eb`
- Success/data: `#059669`
- Warning/async: `#d97706`
- Risk/error: `#dc2626`
- Border: `#cbd5e1`

Use system fonts. Do not use web fonts unless requested.

## Accessibility And Editing

- Include `aria-label` on major SVGs or diagram sections.
- Use readable font sizes: 13px minimum for SVG labels, 14px minimum for explanatory text.
- Keep CSS class names semantic so the user can edit them later.
- Do not rely only on color; pair color with shape, line style, or label.

## Assumptions Panel

Add an assumptions panel when:

- The input omits a relationship needed to make the diagram coherent.
- Static code analysis cannot prove runtime behavior.
- The diagram intentionally abstracts several objects into one node.
- The user asked for a target-state architecture rather than an as-is architecture.

Keep assumptions short and falsifiable.
