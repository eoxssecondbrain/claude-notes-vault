---
thread_name: "askcruz-overview-steel"
user: "sebastian"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

**User:**
Give me a two-minute plain-English overview of what AskCruz does and the problem it solves for steel service centers.

**Assistant:**
AskCruz is EOXS's own AI product — an internal knowledge and work-assistant tool that's now being sold externally, and its current deployments are all steel and metals service centers. First external client is 3GM Steel (mid-implementation on a six-week rollout), and the sales push has extended to Sabre Alloys and Three D Metals. Worth flagging up front: EOXS's own documentation formally positions AskCruz as industry-agnostic long-term, not steel-specific — but every real customer today is a steel service center, so the "problem it solves for steel service centers" framing you asked about is accurate to what it's actually doing right now, even if it's not the official permanent scope.

The core problem: at a steel service center, the knowledge needed to run the business well is scattered. A customer's actual delivery promise lives in an email thread, a pricing exception got agreed on a call, true inventory availability sits in the ERP, and the reason a customer's margin moved might only live in one salesperson's head. When that person is out, or nobody remembers where to look, the business stalls or makes a worse decision. AskCruz pulls that scattered information together so anyone can ask an ordinary question and get a grounded answer instead of hunting across systems and people.

It's built around four pieces. Company Brain answers questions using the company's own history — what was promised to a customer, why a margin changed, how quotes are normally priced. Company Hands does practical work with that knowledge — drafting a quote using your actual pricing logic, flagging an order at risk of missing its promise date, summarizing a call against the right account. Digital Workforce is standing responsibilities — watching an order queue or exception and flagging it without being asked. Company Personalization means it reflects how your specific company actually operates — your vocabulary, your pricing exceptions, your tolerances — not generic steel-industry assumptions.

For a steel service center specifically, this maps onto real operational pain: knowing what's genuinely "free to sell" once commitments are netted out, catching orders drifting toward a missed promise date, understanding "true margin" after freight and processing, and not losing a customer's history when the one rep who knew the account leaves.

Boundaries worth knowing: it explicitly does not replace your ERP, isn't guaranteed real-time (there's a sync lag), and doesn't make commercial decisions on its own — it's an assistant layer on top of what you already run.

Want me to go deeper on any one piece — the four-pillar model, the current 3GM/Sabre Alloys deal terms, or that industry-agnostic-vs-steel positioning tension?

Sources: AskCruz — Product Feature File; AskCruz — Comprehensive Client-Facing Product Understanding; AskCruz — Market Positioning, ICP & Product-Market Fit Status (internal EOXS knowledge base, confidential)
