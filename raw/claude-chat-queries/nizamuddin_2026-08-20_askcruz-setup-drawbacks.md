---
thread_name: "askcruz-setup-drawbacks"
user: "nizamuddin"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

USER: what are the drawbacks are their withe this eoxs setup

CLAUDE: [Called AskUserQuestion to clarify ambiguity] Your question is ambiguous and this is a fresh thread with no prior context — I don't know what "this EOXS setup" refers to.
Question asked: "Which EOXS setup are you asking about the drawbacks of?" Options: A specific client's implementation / EOXS product/platform in general / EOXS internal business setup / Something else.

USER (via AskUserQuestion): whit this AI set-up mean askcruz

CLAUDE: [Called AskUserQuestion to determine rigor level per user preference]
Question asked: "How deep should I go on drawbacks of the AskCruz AI setup?" Options: 5ft — Quick / 10ft — Verified / 50ft — Deep / 100ft — Staged.

USER (via AskUserQuestion): 50ft — Deep

CLAUDE: [Conducted research via mcp__EOXS_data_general tools: get_index, search_wiki, search_assets, get_wiki_page x9 (AskCruz API Cost Pause; AskCruz Access Rollout Git/Gmail Governance; AskCruz Board Scrum Reporting; Claude Prompt Catcher; AI Transformation Day; 3GM Steel AskCruz Proposal Call; Ohio Strip Steel Ask Cruz Intro Call; Sabre Alloys Claude AI Agent Request; Second Brain Initiative; EOXS IT Account Provisioning; Legal-Firm AI Diagnostic; EOXS AI Spinout), get_call (id 2389 full transcript, id 2390 attempted but exceeded token limit), get_email (id 66158, id 66466 full threads), search_emails x5, search_wiki x2 for Sabre Alloys and EOXS AI Spinout]

Final response delivered to user:

Answer, verified against primary sources (calls, emails, internal wiki), not just summaries. All Aug 2026, current.

1. The architecture burns money it doesn't need to. The Sabre Alloys internal cost review (Fathom call, 2026-07-31) found the Claude integration has no native thread/session context — every single prompt resends the entire conversation history, so cost scales far faster than it should. That's not a minor inefficiency; it's the direct cause of what happened next.

2. The internal team got pulled off the paid AskCruz API entirely on cost grounds. On the "Claude vs AskCruz" call (2026-08-13, Fireflies), Raj killed individual AskCruz API access company-wide and moved everyone to one shared Claude account, saying the run-rate wasn't justified "at this early stage" — even while calling the underlying product "good." Real spend cited on the call in a five-to-seven-day window: $74, then $400, then $200 more. Small in absolute terms, but the point is EOXS's own team stopped dogfooding the paid product it's trying to sell.

3. AskCruz isn't actually the product being sold to the first real paying client. In the corrected 3GM Steel proposal (email, 2026-08-17), Raj tells the client EOXS has "moved forward with Claude as the sole front-end rather than offering Ask Cruz as an alternative," because Claude "is more secure and currently has more built-out functionality," while AskCruz keeps developing in the background. So the flagship brand isn't yet good enough to be the interface on a live deal — the client is buying a personal Claude subscription plus an EOXS data/training layer, not "AskCruz."

4. Commercial execution nearly tanked that live deal. The first proposal sent to 3GM's CCO Travis Lane (copying their CFO) had line items that didn't add up to the stated total, the wrong Claude subscription tier assumed, an ambiguous one-time-vs-recurring fee, and a copy-paste artifact referring to "your salespeople and your four partners" — not 3GM's team at all. Travis caught all of it himself and refused to take it to his CEO until reconciled. Raj's own reply: "This version doesn't match what we discussed, and it shouldn't have gone out that way. That's on me." This is a QC gap on the exact motion you need to repeat at scale to hit $1M ARR.

5. Even after the fix, the customer signed smaller and more cautious than pitched. 3GM confirmed at 2 users (not the fuller team originally discussed), explicitly deferred Prompt History and Historical Data "for now," and pushed back on the standard 12-month-into-3-year lock-in, asking for a shorter initial term or defined pilot "since this is a new platform for us" and they want to "prove out the ROI" first. That's a real, named customer telling you the current pitch/contract structure reads as unproven and high-commitment.

6. Internal governance has visible holes. A board-automation Raj explicitly ordered shut down ("Shut this automation down, please") kept running the next day with expanded scope instead — no explanation on record. A Git repo tied to a personal Gmail account is an open, unanswered security question as of 2026-08-18. A functional-team member (Tanya) said AskCruz couldn't answer a basic question "about EOXS" — and the wiki itself flags that even Raj's on-call explanation doesn't clearly resolve whether that's an access restriction or an actual capability gap. Separately, an internal tool built the same week silently logs every Claude prompt — including edited versions — into a database, and it closely resembles "Prompt History," the same feature being sold to clients partly on a trust/security pitch, with no visible confirmation staff were told their prompts are being captured.

7. Focus is split across verticals before the core one is stable. In the same window the cost and access problems above were unresolved, the team also opened a brand-new, unrelated vertical (a small law firm, via a cold diagnostic) while still firefighting the 3GM steel deal.

One thing I can't verify from here and flag rather than guess at: there's a separate "EOXS AI Spinout" plan — moving the AI product line into a separately-capitalized entity, explicitly timed to avoid triggering someone else's (Scott Begin's) revenue-share right, and already restated live to a Sabre Alloys contact. Whether AskCruz sits inside that spinout or is a distinct initiative isn't settled in the record. If it's the same thing, that's a cap-table/ownership question worth resolving before you push harder on ARR into an entity structure that isn't finalized.

Against your stated goal — AskCruz to $1M ARR in 12 months — the two that matter most are #3/#4 (sales execution nearly cost you a signed deal, and the process that produced that error is the one you'd be repeating at volume) and #1/#2 (the product itself isn't yet what's being delivered; you're selling Claude-plus-EOXS-data, not AskCruz). Those are fixable operationally. The spinout question is the one where I'd want your input before treating it as settled either way.

Sources: internal wiki pages "AskCruz API Cost Pause," "AskCruz Access Rollout... Git/Gmail Governance," "AskCruz Board Scrum Reporting," "Claude Prompt Catcher," "AI Transformation Day," "Sabre Alloys — Claude AI Agent Request," "3GM Steel — AskCruz Proposal Call," "EOXS IT Account Provisioning," "EOXS AI Spinout" (all eoxs-db); call "Claude VS AskCruz" (2026-08-13, Fireflies id 2389); email threads "3GM Steel AI Transformation Investment" and "AI Operating System for 3GM Steel — Update Investment Proposal" (raj_gmail, ids 66158, 66466).
