# Production Architecture Blueprint

Use this reference when the user asks for a polished production architecture diagram like a cloud/service platform blueprint, especially when the target resembles a dark technical operations map with regions, numbered nodes, role colors, and sync/async edges.

## Recognition Signals

- User asks for "生产架构", "系统架构图", "平台架构", "云架构", "AI 客服平台", "SaaS 架构", "K8s/EKS 架构", "微服务架构", or "类似这张图".
- Diagram needs deployment boundaries such as edge, workload, data plane, external services, observability, or security.
- Input includes services, gateways, databases, queues, vector stores, LLM vendors, billing, voice, auth, CDN, WAF, Kubernetes, Redis, Kafka, PostgreSQL, Qdrant, or OpenAI.
- User cares about visual polish and architecture communication, not just a plain flowchart.

## Diagram Contract

Produce a single self-contained HTML file by default. Use inline CSS and SVG. Do not load external fonts, scripts, or images.

The diagram should include:

- Title line: product/system name plus architecture view.
- Subtitle metadata: version, region/environment, date/quarter, or status when supplied.
- Region boxes labeled `R1`, `R2`, `R3`... with descriptive names.
- Node cards labeled `N1`, `N2`, `N3`... with concise service names.
- Role-based colors and shapes.
- Solid arrows for synchronous calls.
- Dashed arrows for async events, webhooks, queues, or callbacks.
- A legend for roles and edge styles.
- Assumptions or unknowns when relationships are inferred.

## Region Pattern

Use dashed rounded boundary boxes:

- `R1 Public Edge`: clients, portal, CDN, WAF, SSR, public entry points.
- `R2 Workload / Orchestration`: gateways, APIs, auth, business services, orchestration, workers.
- `R3 Data Plane`: SQL stores, cache, event bus, vector DB, object store, logs.
- `R4 External / Third Party`: LLM providers, billing, messaging, voice, email, analytics.

Do not force these exact region names. Adapt to the user's system.

## Role Map

Use both color and label, never color alone:

- User / Client / Edge: cyan
- Gateway / API / BFF: blue
- Business Services: green
- Middleware / Queue: orange
- Infra / Platform: yellow
- Security / Auth: red
- Data / Persistence: purple
- External / Third Party: slate

## Node Rules

- Keep each node label to 1-3 lines.
- Put product names and versions in node body only when supplied.
- Put `N#` in the top-right corner.
- Use simple inline SVG icons only when helpful: cloud, database, shield, queue, browser, service.
- Do not overcrowd nodes with every environment variable, port, or internal class.

## Edge Rules

- Solid line with filled arrow: synchronous request/response, SQL, REST, gRPC, HTTPS, cache read/write.
- Dashed line with hollow arrow: async event, webhook, queue, pub/sub, callback.
- Label edges with protocol or business event: `HTTPS`, `POST /api/*`, `gRPC`, `audit.log`, `webhook: invoice.paid`.
- Route arrows to avoid crossing region titles and legend boxes.
- If a dependency is uncertain, use dashed muted styling and list it under assumptions.

## Visual Style

Default to a dark blueprint look:

- Background: deep navy with subtle grid.
- Text: muted blue-gray.
- Region borders: dashed neon accents.
- Node surfaces: translucent dark cards.
- Edges: light gray with role-color highlights where helpful.
- Legend: bottom-right or right side, framed but not dominant.

Avoid decorative gradients, bokeh, and unrelated illustration. The diagram should feel operational and inspectable.

## Layout Guidance

1. Place title and metadata at the top-left.
2. Use 2-3 horizontal bands:
   - Edge / public entry at upper-left.
   - Workload / service orchestration in upper-middle.
   - Data plane along the bottom.
   - External providers on the right.
3. Keep the primary request path easy to follow from left to right.
4. Put data dependencies below the service that uses them.
5. Place external systems outside internal region boxes.
6. Keep legend outside the critical path.

## Input Normalization

Before drawing, convert the source into this working model:

```yaml
title: ""
meta:
  version: ""
  environment: ""
  region: ""
  date: ""
regions:
  - id: R1
    name: ""
    role: ""
nodes:
  - id: N1
    label: ""
    region: R1
    role: ""
    details: []
edges:
  - from: N1
    to: N2
    kind: sync
    label: ""
legend:
  roles: true
  edge_styles: true
assumptions: []
```

## Output Checklist

- Title and metadata are visible.
- Every region and node has a stable ID.
- Role colors match the legend.
- Sync and async edges are visually distinct.
- External systems are outside internal boundaries.
- The critical path can be read without following tangled crossings.
- Unverified or inferred relationships are called out.
