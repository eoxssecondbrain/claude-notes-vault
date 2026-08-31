---
thread_name: "steel-ops-console-artifact"
user: "mba_interns"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

# Thread: steel-ops-console-artifact

## User
I want to make an artifact: a web page published with the Artifact tool. Ask me a few questions about what it should show, then build it and publish it.

## Assistant
[Loaded threads-ov and eoxs-data-general skills per standing instructions, then asked clarifying questions via AskUserQuestion tool:]

**Question 1: What should this artifact show or do?**
Options: Dashboard / tracker; Interactive tool; Reference page; Something else.
User selected: **Dashboard / tracker**

**Question 2: What data or content should it be built from?**
Options: Numbers I'll give you now; EOXS or AskCruz business data; Made-up / placeholder data; General knowledge.
User selected: **Made-up / placeholder data**

## User (sent mid-turn, before I could respond further)
Create an interactive sales operations dashboard for a steel service center. The dashboard should include:

1. Total customer orders
2. Pending orders
3. Delayed orders
4. Completed orders
5. Sales pipeline
6. Top 5 customers
7. Order status distribution
8. A section showing possible reasons for order delays Use realistic sample data. Make the dashboard professional and business-oriented, with filters for order status and customer. Make it an interactive Artifact that I can actually click and explore.

## Assistant
[Per standing user preference, asked for a craft level before building a deliverable:]

**What craft level for this dashboard?**
Options: Draft; Painting; Commissioned; Sketch.
User selected: **Sketch**

[Loaded artifact-design and dataviz skills, read the dataviz reference palette, then built the dashboard as a self-contained HTML file (steel-ops-console.html): IBM Plex Sans/Mono typefaces, light+dark theme tokens from the validated dataviz reference palette, seeded-random realistic sample data (56 orders across 10 steel-industry customers, 8 products, 3 statuses, 7 delay reasons; a 4-stage sales pipeline with ~16 deals). Built: 4 clickable KPI tiles (total/pending/delayed/completed orders), an order-status-distribution bar chart, a top-5-customers-by-value bar chart, a sales pipeline funnel with stage-to-stage conversion, a delay-reasons bar chart, and a sortable orders table — all cross-filtered by two dropdown filters (order status, customer) plus click-to-filter on KPI tiles and chart bars. Verified with a headless Chromium render (light mode, a filtered state, and dark mode) — no console errors, filtering logic confirmed correct in screenshots.

Published the artifact via the Artifact tool at https://claude.ai/code/artifact/bea4b8b0-c118-413e-a75a-f153679a73ee (favicon: 🏭, description: "Interactive sales operations dashboard for a steel service center — order status, pipeline, top customers, and delay drivers, filterable by status and customer.").

Final reply to user: Published — the Steel Ops Console dashboard is live. It covers all eight sections you asked for: the four KPI tiles (total, pending, delayed, completed orders), order status distribution, top 5 customers by order value, a sales pipeline funnel with stage-to-stage conversion, and a delay-reasons breakdown, plus a sortable table of all 56 sample orders underneath. Everything cross-filters — use the status/customer dropdowns, or just click a KPI tile or a chart bar directly to filter by it. Built at Sketch craft level as you picked; light and dark themes are both wired up and I checked it headlessly (light, filtered, and dark states) before shipping, no console errors. Sample data is illustrative only, generated for the demo.
