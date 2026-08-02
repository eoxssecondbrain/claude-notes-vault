---
thread_name: "askcruz-vs-palantir-positioning"
user: "raj"
type: claude-chat
created: 2026-08-02
updated: 2026-08-02
---

User: So what we are doing with the ask Cruz. Is it similar to what palantir does. The only difference is they work with companies with 1000+ employees and we are in the 30-200 employees

Assistant: Similar model, different economics — not just company size.

Similarities:
- Both build a unified layer over messy, siloed internal data (Palantir's ontology, Cruz's OV) and let users query/act on it through an AI/analyst interface rather than hunting through source systems.
- Both require heavy bespoke integration per client, not self-serve setup. Palantir calls this forward-deployed engineering; Krinox's "30 client integrations in 90 days" delivery problem is the same animal.

Real differences beyond employee count:

1. Palantir built the ontology/integration engine first (Foundry/Gotham), over a decade, then layered AI on top (AIP). Cruz is AI-first — the OV is comparatively lightweight, leaning on Claude as the reasoning layer instead of a purpose-built data-integration platform.

2. Unit economics, not just target size. Palantir can burn months of engineer time per client because contracts run $1M+. At $30K ACV, that same bespoke-integration motion doesn't scale unless delivery cost per client drops by an order of magnitude. That's the actual hard problem — "smaller companies" is a symptom, not the constraint.

3. Palantir's counterpart is usually a client IT/data team. A 30-200 employee company mostly has none — so Cruz has to do more of the plumbing itself, with less structured data and no internal partner to lean on.

4. Palantir is, in practice, still a services-heavy business per client — which is exactly what the GFC charter says AskCruz explicitly is not. If the delivery model ends up looking like Palantir's forward-deployed teams, that's a direct contradiction worth naming now, not after 10 client builds.

The delivery-capacity gap already flagged for the 30-client target is really this same tension surfacing early.
