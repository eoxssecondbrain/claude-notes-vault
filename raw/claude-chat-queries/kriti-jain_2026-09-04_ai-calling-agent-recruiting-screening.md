---
thread_name: "ai-calling-agent-recruiting-screening"
user: "kriti-jain"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: basically, we had a job posting, and we got two thousand applications. So what we are thinking is that, like, do we need an AI agent that can help us at, like, okay, we'll text them all that, okay, call on this number, and they'll call. It's... it would be an AI call. And this AI will ask those questions. We'll train that calling agent. Okay? And that that agent will properly feed the name and answers of it so that we can analyze later. Like, is there something prebuilt like this, a calling agent or something that we can train accordingly?

Assistant: Flagged this as a research/product question outside EOXS-specific skills. Asked for rigor level via AskUserQuestion — user picked 50ft (Deep).

Assistant (turn 1 summary): Two approaches exist — prebuilt recruiting screening platforms (Classet/Joy ~$190/wk per job or $700/mo; Ribbon $499-1,999/mo; Alex AI/Apriora quote-based; HeyMilo quote-based; Paradox $10k+/yr; HireVue $35k+/yr — overkill) vs general voice-agent platforms to build on (Retell ~$0.10-0.20/min; Bland ~$0.13-0.18/min + $0-499/mo; Synthflow ~$0.11-0.24/min or $30k+/yr enterprise; Vapi ~$0.30-0.33/min). At 2,000 candidates/~10,000 min, build-option raw cost ~$1,000-3,000 excluding 1-3 weeks dev time. Flagged TRAI DLT/DND compliance: candidate-initiated call-in flow mostly sidesteps DND, but bulk SMS invite needs DLT Principal Entity registration, penalties up to ₹1.5 lakh/violation. For a one-off job posting, buy beats build. Questioned whether dev time is better spent on AskCruz.

User (turn 2): Said this may become recurring, not just one posting — asked for full build-vs-buy comparison including time and cost for building the custom agent.

Assistant (turn 2 summary): Added three-tier comparison. Fully custom in-house stack (own STT/TTS/telephony/LLM): $50k-300k+, 12-24 months to production, up to $2M enterprise — ruled out as overkill. Build on a voice-agent platform (Retell/Bland/Vapi/Synthflow): setup 3-7 days (experienced) to 2-3 weeks (first time); per-call blended $0.10-0.30/min (~$0.50-1.50/candidate at 5 min); recurring at 2,000/month ~$1,000-3,000/mo call cost + $0-500/mo platform fee + 3-8 hrs engineering per new job posting; benefit: data ownership, reusable infra, one-time compliance setup pays off long-term. Buy prebuilt (Classet/Ribbon/HeyMilo): setup hours, cost as above but largely priced per active job req not flat annual — flagged to confirm multi-req/annual plans with vendor. Breakeven: hiring at 2,000-candidate scale more than ~quarterly tips build cheaper within a year; sporadic (1-2x/yr) favors buy. Asked user to confirm expected hiring frequency at this volume over next 12 months to decide.

User (turn 3): Asked to put all the data into a table so it's easy to understand.

Assistant (turn 3): Consolidated everything into one master comparison table covering all options (5 prebuilt platforms + 4 build platforms + fully-custom tier) with columns for setup time, cost structure (one-time build cost estimate where applicable, recurring/per-unit cost), and key notes (compliance, ownership, lock-in). Reiterated the breakeven framing (>quarterly hiring at this volume favors build; sporadic favors buy) and repeated the open question on expected hiring frequency, which the user has not yet answered.
