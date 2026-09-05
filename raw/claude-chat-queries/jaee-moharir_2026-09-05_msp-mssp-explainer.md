---
thread_name: "msp-mssp-explainer"
user: "jaee-moharir"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

User: tell me about MSP (MSSP)

Assistant: This query doesn't match either skill's content domain — it's not EOXS-internal data (eoxs-data-general) and it's just a factual lookup, not something requiring an analysis save (threads-ov's save_analysis). I'll answer directly; the mandatory transcript save still applies at the end of the turn.

**MSP (Managed Service Provider)**
A company that remotely manages a client's IT infrastructure — networks, servers, endpoints, backups, cloud, helpdesk — usually under a flat-fee subscription (per-device or per-user/month) rather than break-fix billing. Core value prop: outsourced IT department for companies too small to run one in-house, plus proactive monitoring (RMM tools) instead of reactive fixes.

**MSSP (Managed Security Service Provider)**
A subset/specialization of MSP focused specifically on security operations: SIEM/log monitoring, threat detection and response, vulnerability management, firewall/IDS management, compliance support (SOC2, HIPAA, PCI-DSS), and often a 24/7 SOC (Security Operations Center). Some MSSPs are standalone security shops; some MSPs bolt on an MSSP tier as they mature.

Key distinction: MSP = "keep the lights on and IT running." MSSP = "keep it running securely and defensible against attackers/audits." Many vendors blur the line and market themselves as "MSP/MSSP" to cover both.

Revenue model for both: typically tiered contracts (Bronze/Silver/Gold or per-seat pricing), high retention/low churn once embedded, growth via cross-sell (add security, backup, compliance add-ons to existing IT contracts).

If there's an EOXS or AskCruz angle to this (e.g., considering MSP/MSSP as a customer segment, competitor, or vendor), say so and I'll go pull the relevant data instead of guessing at relevance.

User: i want in general, how qualys and druva work with mssp/msp what is the working model and how do they generate revenue and what services they provide

Assistant: This is external research (Qualys and Druva partner/channel programs) — not a one-line lookup — so per your rigor-level preference, pick a depth before I start. Doesn't touch EOXS/eoxs-data-general data.

5ft — Quick: pull each company's published MSP/MSSP partner program page + one or two overview articles, summarize working model, revenue mechanics, and service scope as stated.

10ft — Verified: same as above, but cross-check partner program terms (margin/revenue-share structure, licensing model) against at least 2 sources each (official partner portal page + industry writeups/press), flag any discrepancies.

50ft — Deep: verified scope, plus competitive context (how their MSP models compare to each other and to category norms), pricing/margin mechanics where disclosed, deal structures (white-label vs referral vs reseller), and blind spots (e.g., what's not publicly disclosed).

Which level?

User: 50 ft and explain to a beginner with easy examples

Assistant: Structure: Qualys model, Druva model, how MSPs/MSSPs actually make money off either, comparison, blind spots. No bold, plain text throughout as instructed.

The core concept first, in one sentence: Qualys and Druva don't run their own MSP/MSSP business — they sell their software to independent IT companies (the MSPs/MSSPs), who then wrap it into a service and resell it to end customers at a markup. Think of Qualys/Druva as wholesalers, and the MSP as the retailer/manager.

QUALYS — vulnerability management / security scanning

What it is, in plain terms: Qualys builds software that scans a company's computers, servers, and cloud accounts for security holes (missing patches, misconfigurations, exposed ports) and tells you what to fix first. An MSSP buys access to this scanning engine and offers "we monitor your security posture 24/7" as a service to its own clients, instead of each small business having to buy and run Qualys itself.

Working model:
- Qualys runs a dedicated MSSP partner track, separate from selling direct to enterprises. Partners get onboarded into an MSSP Portal that gives them a single dashboard to manage all their end-client accounts, provision licenses, and single-sign-on into each client's environment instead of juggling separate logins per client. The portal gives partners a unified platform that streamlines client, subscription, and security services management, aimed at increasing revenue opportunities and improving operating margins.
- Partners choose which "lane" fits them — MSSP, MSP, VAR (reseller), or distributor — and get different program benefits per lane, including deal registration (protection from another partner undercutting them on a deal they found) and access to technical certifications so they can charge for their own consulting on top. Partners can identify new customer opportunities and gain deal protection, pursue certifications to deliver value through professional and consulting services, and align with whichever market segment fits their business model — MSSP, MSP, VAR, or distributor.
- Underlying pricing to the partner is the same subscription logic Qualys uses everywhere: modular, priced per asset scanned per year (each module — vulnerability management, web app scanning, compliance, etc. — priced separately), so an MSSP's cost scales with how many client machines/apps it's protecting. Core pricing is module-based: each Qualys module is priced separately, typically per asset or per application, with the number of assets scanned driving the base cost.

Beginner example: Imagine Qualys is like a car-diagnostics machine manufacturer. An independent garage (the MSSP) buys/leases the diagnostics machine, plugs in each customer's car (client's network), and sells "monthly car health checkups" as its own branded service. The garage pays Qualys per car scanned; it charges the car owner a higher flat monthly fee that includes the scan plus its own labor (interpreting results, fixing what's found, writing a report).

How the MSSP actually makes money on Qualys: the margin is the spread between what Qualys charges per asset/module and what the MSSP bills the end client for the bundled "managed security service" (scan + human analysis + remediation + reporting + SLA). Qualys itself profits from partner-driven volume — more assets under scan across all of a partner's clients, on renewing annual subscriptions.

DRUVA — cloud backup / data resilience (ransomware recovery)

What it is, in plain terms: Druva backs up a company's servers, laptops, cloud workloads (AWS, Microsoft 365, etc.) to Druva's own cloud, so if ransomware hits or someone deletes something, the data can be restored. Unlike Qualys, Druva actually built a specific MSP console from day one — it's arguably more "MSP-native" than Qualys.

Working model:
- Druva's MSP program, launched 2021, is built entirely on AWS with zero on-prem infrastructure for the partner to manage — an MSP can spin up a new client's backup protection in minutes rather than shipping and racking hardware. The MSP program offers a SaaS-based delivery model with zero-touch onboarding and no infrastructure to maintain, letting MSPs onboard new customers in as little as 15 minutes while maintaining high, recurring margins.
- Partners get a dedicated "Managed Services Center" console — this is the key differentiator — where one MSP admin can see and manage all their clients' backup jobs, storage usage, and account health from a single pane, and it plugs directly into common MSP billing tools. The Managed Services Center integrates with the Druva platform so MSPs can centrally manage multi-tenant data protection across any client workload, and it connects to ConnectWise PSA to automate billing, tickets, and service workflows across clients.
- Billing to the partner is consumption/credit-based, not per-seat: one Druva credit = 1 TB of deduplicated (compressed) data stored per month. One Druva credit allows storing 1 TB of deduplicated data in the cloud for one month, expressed as a TB-Month, and organizations pre-purchase credits based on expected storage volume — e.g., needing to store 10 TB/month for a year means buying 120 credits. Actual billing tracks daily usage and converts it to that monthly credit figure. Credits are consumed based on actual deduplicated storage used to protect backup data, calculated daily and converted into credits — so a server with 10 TB of data that dedupes down to 8 TB unique data consumes 8 credits, not 10.
- Druva now also gives MSPs a chargeback/telemetry reporting layer specifically so the MSP can automate billing its own clients based on their actual consumption (storage, user count, server count) instead of manually pulling numbers from each client's console. These reports consolidate detailed telemetry across all tenants directly in the MSP console, letting partners charge back clients based on consumption factors like storage used, number of users, or server counts, and automate monthly invoicing instead of manually compiling spreadsheets.

Beginner example: Druva is like a public self-storage warehouse company. The MSP is a local moving-and-storage business that rents a big block of warehouse space wholesale (in TB-months), then re-rents smaller storage units to its own individual customers, handling the packing, pickup, and "call us if you need your stuff back" service. The MSP's bill from Druva scales with how much stuff (data) is actually stored; the MSP's bill to its customer is usually a flatter, simpler monthly number that bakes in a margin plus the MSP's own service work.

How the MSP actually makes money on Druva: same spread logic as Qualys — buy storage wholesale on a usage-based credit meter, resell it to end clients bundled with monitoring/recovery service, usually at a simpler flat or tiered price so the client doesn't have to think about deduplication math. Druva itself reported that this MSP channel became a fast-growing slice of its business. Druva's MSP program, launched in 2021, grew nearly 300% annually, and by August 2023 Druva had surpassed $200 million in ARR with 300% year-over-year growth specifically in MSP customers.

Side-by-side, beginner framing

Qualys: sells "the ability to find security problems." Priced per asset/module scanned. MSSP wraps it with human analysis and remediation, charges a security-monitoring retainer.

Druva: sells "the ability to store and recover data safely." Priced per TB stored (consumption/credit model). MSP wraps it with backup management and disaster-recovery response, charges a data-protection retainer.

In both cases the vendor's own revenue comes from the underlying consumption (assets scanned, or TB stored) scaling up across every client the partner signs — the partner is a distribution and service layer, not just a reseller of a static license count. Both vendors explicitly optimize their partner tooling (single console, multi-tenant management, billing automation) specifically because a partner managing 50 clients through 50 separate logins doesn't scale, and vendor growth depends on removing that friction.

Blind spots / what's not publicly disclosed, since this is the 50ft ask

Neither company publishes actual partner margin percentages, rebate tiers, or deal-registration discount depth — that's negotiated per partner and typically NDA'd. Industry analyst commentary generally pegs MSSP/MSP software margins in a "modest but recurring" range rather than huge one-time markups; the real profit for the MSP is the service labor stacked on top, not the software arbitrage itself. Take that as a general channel-economics pattern, not a sourced figure for either company specifically. Also worth flagging: Qualys's page for the MSSP program itself is JavaScript-rendered and doesn't publish structured pricing publicly — its numbers above come from third-party pricing-benchmark sites (Vendr, UnderDefense), not Qualys's own price list, so treat exact per-asset dollar figures as directional, not authoritative.

If there's a reason you're looking at this — e.g., evaluating a vendor relationship model as a template for how AskCruz could structure a partner/reseller channel — say so and I'll reframe the comparison around that specifically rather than leaving it as general background.
