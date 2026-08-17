---
thread_name: "gfc-us-bank-account-nonresident"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

User: We have to open a new bank account for GFC. We were originally doing banking with SVB for EOXs, and we reached out to them. However, they said they can't open a bank account. So stupid.
Now I need a bank which is flexible to one of my biggest needs. That is that I am not physically present in the US. I remember ten years ago I opened a bank account with a bank in the US, and they wanted me to physically be there to open the bank account.

I want to deal with a bank which will not tell me to come to the branch for every little thing.

Assistant: No skill here matches cleanly — this is a banking/entity-setup question, not a sales-strategy or EOXS-data query, so I'm proceeding without one.

Before I dig into bank options, pick a rigor level:

**5ft — Quick:** List of 3-5 banks known for accepting non-resident/foreign-founder US entities remotely (e.g. Mercury, Relay, Wise Business, Brex), based on general knowledge and quick verification.

**10ft — Verified:** Same, but I check each bank's actual current published requirements (remote KYC process, whether they require SSN/ITIN, whether they support Delaware/Wyoming LLCs with a non-resident founder) against their own docs, not just reputation.

**50ft — Deep:** Verified, plus I look into adjacent angles — how each handles ongoing account maintenance without branch visits (wire limits, support model, whether they'll freeze/request docs later), what entity structure requirements they have (LLC vs C-corp, EIN turnaround), any complaints about them suddenly de-banking remote founders, and how this interacts with your existing GFC entity plan (Delaware/Wyoming LLC, IRIS IP transfer) and SVB relationship for EOXS.

Which one?

User: 50

Assistant: Bottom line: Mercury is the right primary pick. Relay is out unless you get an ITIN. Wise Business is a good secondary account, not a bank replacement.

Why SVB said no
SVB (now a division of First Citizens Bank) has tightened non-resident onboarding significantly since its 2023 collapse and FDIC receivership — it's no longer the founder-friendly SVB of a decade ago, and its current book leans toward VC-backed entities with US operating presence. SVB is still marketed as accepting non-resident founders with Delaware LLCs or C-Corps, but in practice this is inconsistent and skews toward larger, VC-backed accounts — a new small entity like GFC without institutional backing is exactly the profile that gets declined now. This isn't really about you; it's about SVB's risk appetite post-collapse.

The three real options for a non-resident (India-based) founder

Mercury — best fit for your stated need
Mercury requires valid government ID for anyone owning 25%+ of the company, and non-residents typically submit a passport. The onboarding is fully remote — no branch visit, no in-person meeting. Indian founders qualify by forming a US LLC first, then opening a Mercury account remotely with no US visit required, and Mercury explicitly accepts international founders without requiring US residency or citizenship, with the only exclusion being founders from countries on Mercury's own prohibited list — India isn't on it. Requirements are EIN, formation docs, and passport — no SSN, no ITIN.

Relay — ruled out unless you get an ITIN
Relay accepts an SSN or ITIN; non-residents without either face a practical barrier and should contact support before applying. Since you don't have either, skip Relay for now.

Wise Business — useful add-on, not a real bank
Wise is not a US-chartered bank — it's an Electronic Money Institution that gives you US bank details for receiving payments, useful mainly for multi-currency work. It's not a substitute for a real operating account.

The catch you need to know before committing to Mercury

This is the important part given what you actually said you want — a bank that won't make you jump through hoops for every little thing. Mercury's account-opening is frictionless, but its ongoing account stability has a real, documented problem: sudden freezes and closures during compliance reviews, sometimes with no stated reason and no appeal.

A Product Hunt reviewer's account was closed with no warning after a routine document request, before they'd even had the chance to upload the ID. Support response times ran two to three business days during an active dispute. The most repeated complaint across reviews is reliability — sudden account restrictions or closures during compliance reviews, weak explanations, and real operational disruption. A BBB complaint from June 2026 describes an account closed twelve days after opening, funds held for sixty days with no electronic transfer option, and no specific violation ever named. Another BBB complaint describes Mercury refusing to release historical statements after closure, blocking the company's own tax compliance. And a third-party recovery-service guide notes bluntly that founders can be closed with no violation history and no reason given.

So the tradeoff is real: Mercury never asks you to visit a branch, but it can unilaterally freeze your operating cash with less due process than a branch visit would've given you. For a company gunning for $1M ARR in 12 months, a surprise 60-day fund freeze is a worse outcome than an occasional branch inconvenience.

What actually reduces that risk, based on the closure-trigger patterns reported: use a real business address, not a bare registered-agent or PO box address (flagged automatically); keep the account activity boringly consistent with what you declared at signup (industry, volume, countries); respond to any document request same-day rather than letting it sit; and never run third-party pass-through payments through it.

What I'd actually do

Open Mercury as the primary GFC operating account — it's the only one of the three that matches "no branch, no SSN, works from India" without qualification. In parallel, open a Wise Business account and keep it lightly funded and active, purely as a fallback rail so a Mercury freeze doesn't stop you from paying anyone. Don't wait until a freeze happens to set up the second option — set it up now, in the same week, so it's already live if you ever need it.

One open item: your entity is still listed as "considering Delaware/Wyoming LLC" — not yet finalized. Lock that before applying anywhere, since the bank application needs the actual formation docs and EIN, and switching entity type after applying resets the clock.
