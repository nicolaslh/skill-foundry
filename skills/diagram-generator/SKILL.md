---
name: diagram-generator
description: Generate rich, self-contained HTML diagrams from natural-language descriptions, pasted code, or repository code. Use when the user asks for flowcharts, architecture diagrams, component maps, dependency graphs, data-flow diagrams, sequence diagrams, state diagrams, or visual explanations of a system, process, API, workflow, module, or codebase.
---

# Diagram Generator

## Overview

Turn vague system descriptions or source code into diagrams that are easy to inspect, share, and revise. Default to a complete single-file HTML artifact because it supports richer layout, styling, legends, notes, and optional interactivity than plain diagram DSLs.

## Output Decision

1. Produce HTML by default.
2. Produce Mermaid, PlantUML, Graphviz DOT, Markdown, SVG, or PNG only when the user explicitly requests that format or the surrounding task requires it.
3. If the user asks for a file, create a `.html` file with inline CSS and no external dependencies unless they approve external libraries.
4. If the user asks in chat without requesting a file, return a complete HTML code block first, then a short note explaining the diagram assumptions.
5. If the user asks for a quick sketch, return a compact HTML diagram rather than a polished dashboard.

## Workflow

1. Identify the source:
   - Natural-language process or system description.
   - Pasted code, logs, config, API snippets, or database schema.
   - Repository files that need inspection.
2. Extract the entities, steps, states, and relationships. Separate confirmed facts from inferred relationships.
3. Choose the diagram type:
   - Flowchart for ordered decisions, business processes, pipelines, and user journeys.
   - Architecture diagram for systems, services, deployment boundaries, queues, stores, APIs, and external actors.
   - Production architecture blueprint for polished cloud/platform diagrams with regions, numbered nodes, role colors, legends, and sync/async edges. Use `references/production-architecture-blueprint.md`.
   - Component/dependency graph for modules, packages, classes, functions, imports, ownership, or build dependencies.
   - Sequence diagram for request/response behavior, async events, handoffs, and cross-service interactions.
   - Data-flow diagram for ingestion, transformation, storage, lineage, and privacy boundaries.
   - State diagram for lifecycle, workflow state, retry, cancellation, or error paths.
4. Pick the right altitude:
   - Use one overview diagram for the whole system.
   - Split into multiple diagrams when there are more than 12 major nodes or when mixing architecture, sequence, and data-flow views.
5. Generate the HTML using the rules in `references/html-diagram-patterns.md`.
6. Add a concise assumptions section when relationships are inferred or the source is incomplete.

## Code-To-Diagram Rules

- Inspect code before drawing when repository files are in scope.
- Prefer actual imports, call sites, routes, handlers, config, schemas, and package boundaries over guessed architecture.
- Name nodes using the codebase's own identifiers when they are readable; otherwise use clear human labels.
- Keep uncertain links visually distinct or list them under assumptions.
- Avoid claiming runtime behavior from static code alone unless it is directly visible from tests, config, handlers, or call chains.
- For large codebases, start with a file/module map, then zoom into the requested path or subsystem.

## HTML Requirements

Read `references/html-diagram-patterns.md` before generating non-trivial HTML diagrams, multi-section diagrams, or repository/code-derived diagrams.

Read `references/production-architecture-blueprint.md` when the user asks for a diagram like a production platform architecture map, cloud architecture blueprint, AI service platform, SaaS architecture, or the reference image with R/N labels and role-colored nodes.

For all HTML output:

- Use a self-contained document with `<!doctype html>`, semantic structure, inline CSS, and accessible labels.
- Prefer SVG inside HTML for precise diagram geometry; use HTML/CSS cards for explanatory panels, legends, and notes.
- Include a title, legend, and optional assumptions panel when helpful.
- Use restrained colors and consistent visual language for actors, services, data stores, decisions, queues, and external systems.
- Make the layout responsive enough to read in a browser at common laptop widths.
- Do not load CDN scripts, fonts, or styles unless the user asks for them.

## Response Pattern

When delivering a diagram:

1. Lead with the artifact or file path.
2. State the selected diagram type and why, in one sentence.
3. List only material assumptions or unknowns.
4. Offer one useful next refinement, such as adding sequence detail, grouping by deployment boundary, or generating a Mermaid version.
