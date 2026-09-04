---
thread_name: "ai-calling-agent-recruiting-screening"
user: "kriti-jain"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: basically, we had a job posting, and we got two thousand applications. So what we are thinking is that, like, do we need an AI agent that can help us at, like, okay, we'll text them all that, okay, call on this number, and they'll call. It's... it would be an AI call. And this AI will ask those questions. We'll train that calling agent. Okay? And that that agent will properly feed the name and answers of it so that we can analyze later. Like, is there something prebuilt like this, a calling agent or something that we can train accordingly?

Assistant: This is a research/product question, not something any of the EOXS-specific skills cover — flagging that per your instruction rather than guessing.

Before I go dig into this, pick a depth:
[AskUserQuestion: rigor level 5ft/10ft/50ft/100ft — user selected 50ft - Deep]

Assistant (final response, turn 1): Yes — this exists as a mature product category, and there are two distinct approaches, not one.

Recruiting-specific screening platforms — built for exactly this: candidate calls in (or gets called), AI asks your questions, transcribes, scores, and pushes structured name+answer data out for you to review. No engineering needed.

| Tool | Pricing | Fit |
|---|---|---|
| Classet (Joy) | ~$190/week per job or $700/mo flat | Purpose-built for high-volume frontline/bulk hiring, 100+ ATS integrations, voice interview within minutes of applying |
| Ribbon | $499–1,999/mo | Video+voice AI interviews, ATS field mapping, auto follow-up via SMS/email |
| Alex AI (formerly Apriora) | Quote-based | Adds identity verification/fraud detection |
| HeyMilo | Quote-based (undisclosed) | Voice/video/SMS screening, 20+ ATS integrations, scorecard write-back |
| Paradox (Olivia) | $10,000+/yr | Mostly chat-first, enterprise, now under Workday |
| HireVue | $35,000+/yr | Overkill for a single job posting |

General-purpose voice-agent platforms — you build and train the conversation yourself.

| Tool | Loaded cost | Setup |
|---|---|---|
| Retell AI | ~$0.10–0.20/min, no platform fee | No-code + SDK, hours to launch, native batch calling |
| Bland AI | ~$0.13–0.18/min + $0–499/mo | API/developer-led, days to weeks |
| Synthflow | ~$0.11–0.24/min (or $30k+/yr enterprise tier) | No-code visual builder, ~1 hour to first agent |
| Vapi | ~$0.30–0.33/min | Fully custom, developer infra required |

At 2,000 candidates, ~5-min calls, ~10,000 minutes total: raw calling cost on Retell/Bland ~₹85,000–170,000 ($1,000–2,000), Vapi ~₹250,000+ ($3,000+) — excludes 1-3 weeks of dev time to build the flow, retry/no-answer handling, and analysis dashboard.

Flagged: the text-in/call-in flow is candidate-initiated, which mostly sidesteps TRAI DND (that restricts businesses calling consumers, not the reverse), but the SMS blast itself needs DLT template registration as a Principal Entity — penalties up to ₹1.5 lakh per violation plus number blocking if not registered.

Also flagged: for a one-off single job posting, buy (Classet/Ribbon) beats build on time and cost — build only pays off if this becomes recurring infrastructure. Also questioned whether dev time here is better spent on AskCruz given this is operational, not growth-leverage, work.

Sources: cloudtalk.io best-ai-voice-agents-for-hr-and-recruiting, retellai.com retell-vs-bland-vs-synthflow-vs-vapi, hirevire.com best-ribbon-ai-alternatives, hiretruffle.com paradox-ai-pricing, rootle.ai trai-regulation-voice-ai-compliance, classet.ai heymilo-ai-reviews-pricing-alternatives

User (turn 2): It's not necessary that we'll keep it just for one job posting. We maybe, like, you know, force... keep it for future also if we like the scenario. So I want a comparison between the, like, premade things and also the thing that we make, the agent that we will make because just tell me how much time it will be taking, how much cost it will take. Just tell me everything about that also.

Assistant (final response, turn 2): Since you might keep this running, the calculus changes — laid out all three paths: buy prebuilt, build on a voice-agent platform, or build fully custom in-house.

Fully custom in-house (own STT/TTS/telephony/LLM stack) — ruled out: $50,000–300,000+ to build, 12–24 months to production, up to $2M for enterprise-grade. Not worth considering at this scale.

Build on a voice-agent platform (Retell AI, Bland AI, Vapi, Synthflow):
- Setup time: 3–7 working days for an engineer familiar with the platform for a working screening flow with structured answer capture; 2–3 weeks if it's their first time, accounting for edge cases (interruptions, unclear audio, off-topic answers, voicemail/no-answer/retry handling).
- Per-call cost: blended $0.10–0.30/min (telephony+STT+TTS+LLM+platform markup stacked); at 5 min/call that's $0.50–1.50/candidate.
- Recurring cost at 2,000/month: $1,000–3,000/month call cost + $0–500/mo platform fee + 3–8 hrs engineering time per new job posting to rebuild/tune the flow.
- Benefit: full data ownership, reusable infra, per-role customization, no per-job vendor markup, and the TRAI/DLT compliance setup becomes a one-time sunk cost that pays off on every future use.

Buy prebuilt (Classet, Ribbon, HeyMilo):
- Setup time: hours — define questions, connect/skip ATS, publish same day.
- Cost: Classet ~$190/week per job or $700/month flat; Ribbon $499–1,999/month — flagged that these are largely priced per active job req, not flat annual seats, so confirm with vendor whether multi-req/annual plans exist since per-job pricing compounds with frequent hiring.
- Benefit: scorecards, transcripts, ATS write-back, candidate-experience polish out of the box; locked into their UI and their (largely US-centric) compliance posture — TRAI/DLT still needs separate verification either way.

Breakeven: at 2,000-candidate volume, hiring at this scale more than roughly once a quarter tips the build option cheaper within the first year (usage-based cost vs flat per-job/month premade pricing). Sporadic use (once or twice a year) favors buying prebuilt each time.

Asked user to confirm expected hiring frequency at this volume over the next 12 months, since that number decides build vs buy.

Sources: agxntsix.ai ai-voice-agent-pricing-guide-per-minute-costs-telephony-overhead-setup-fees, ainora.lt retell-ai-vs-bland-ai-vs-vapi-comparison-2026, cloudtalk.io best-ai-voice-agents-for-hr-and-recruiting, rootle.ai trai-regulation-voice-ai-compliance
