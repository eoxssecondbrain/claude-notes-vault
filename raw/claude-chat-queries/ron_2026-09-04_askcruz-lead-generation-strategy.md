---
thread_name: "askcruz-lead-generation-strategy"
user: "ron"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: We need to get more leads for AskCruz. If you had to get more leads for AskCruz, where would you go about finding that? What would your step be? I need data which is good data. I do not want shitty data. Good high quality data convert to high quality leads.

Assistant: Quick note before I dig in: your preferences reference a "sales-strategist" skill to stack with raj-eoxs-vault for GTM/sales-strategy queries, but I don't see that skill installed — only sales-advisor (the Cardone/Miner lens, normally routed through ceo-advisor) exists in this environment. I'm proceeding with raj-eoxs-vault only, flagging this per your own rule rather than guessing which persona you meant.

This is a strategic research question (lead-gen channel strategy for AskCruz), not a quick lookup, so pick a rigor level:

5ft — Quick: fastest path — direct data sources (Apollo/ZoomInfo-type platforms, LinkedIn Sales Nav, industry associations), a shortlist of channels, no verification.

10ft — Verified: same scope, but I check claims about each source (accuracy rates, pricing, coverage of steel/manufacturing/industrial verticals) against more than one reference before reporting.

50ft — Deep: full investigation — verified sources, plus adjacent angles you didn't ask (e.g. whether your existing EOXS client base and steel-industry relationships are a cheaper/higher-converting lead source than cold data, trade show/association data, referral mechanics, data enrichment/verification workflow), risks and blind spots flagged.

50ft is probably the right call here since "good vs shitty data" is fundamentally a source-quality and vertical-fit question, not just a list of platforms — but your choice.

User: I want you to look for sources and tell me which one would be best for good quality data.

Assistant: Straight answer first: for AskCruz specifically, the single best source isn't a generic B2B database — it's layering three things, because "quality" here means two different problems (right company vs. real contact) that no one source solves alone.

Top pick, ranked

1. Industry association directories (steel/metals-specific) — highest company-level quality, essentially free
Metals Service Center Institute (MSCI) — ~400 member companies, 1,500+ locations, purchase 55-75M tons/yr, primarily steel/aluminum service centers and distributors. This is close to your exact ICP.
AMPD (Association of Metal Processors and Distributors) and FMA (Fabricators & Manufacturers Association) — both publish searchable member directories of real, operating steel/metal companies.
Why this beats a purchased list: membership is self-verifying. Every company on it is a confirmed, active steel/metals operator — zero "ghost company" risk, which is the main way generic databases go bad. Weakness: these give you the company, sometimes a GM, rarely a verified email — you still need step 2.

2. Apollo.io (filtered + verified) — for the actual decision-maker contact
You already have Apollo integration and a job-title classifier built (per your GitLab/Teams MCP work). Apollo's raw accuracy runs 65-89% depending on the source you check, so don't trust it unverified — that's exactly how "shitty data" happens.
Fix: run Apollo output through ZeroBounce or NeverBounce (95-99.6% claimed accuracy) before it ever hits a sequence. That single step is what converts a mediocre database into a clean list — verification technique matters more than which base provider you pick.
Use it narrowed to steel/metals NAICS + the VP/Director/Controller/GM title set you already defined, cross-referenced against the MSCI/AMPD/FMA company lists from step 1 so you're not prospecting blind into companies outside your ICP.

3. ZoomInfo or Cognism — only if you want to go up-market
ZoomInfo has the strongest US enterprise coverage and intent data (Bombora) but starts around 15k/yr — worth it only if you're chasing larger steel/manufacturing accounts than your current DPS/Sabre/Greer/PPC tier. Cognism is the better pick if any target ever has EU operations. Skip both if budget or account size doesn't justify the spend yet.

What I'd deliberately not lead with: ThomasNet. It's the most obvious "industrial directory" but it's built for procurement discovery (buyers finding suppliers), not outbound contact data — company/product listings only, minimal verified individual contacts. Useful for company discovery, weak as a lead source on its own.

One thing worth naming even though it's outside "external data sources": your existing EOXS relationships (Sabre, Greer, DPS, PPC, 3GM, Eastern States) and the steel-industry referral network around them are a higher-converting source than anything above — 100% ICP fit, warm intro, zero data-quality risk. If lead volume is the actual bottleneck and this network isn't yet being mined for AskCruz referrals systematically, that's worth fixing before spending on new data sources. Want me to build that out as a specific play, or size up the MSCI/AMPD/FMA + Apollo + verification pipeline first?
