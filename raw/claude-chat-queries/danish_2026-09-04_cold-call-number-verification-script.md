---
thread_name: "cold-call-number-verification-script"
user: "danish"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Cold Call / Number Verification Script

## User

i am going to do cold call, not cold call actually but do the mockup call to see whther this no. is active and person is same or not so i had a script where i would ask them Hey, is it Yash from Wisconsin Steel and then Hi,  i have a partcel to deliver or something like that so i need a script i can follow

## Assistant

Two notes before the answer.

Your preferences reference raj-eoxs-vault and sales-strategist. Neither is available in this session — I only have eoxs-data-general (EOXS data connectors) and threads-ov. Flagging so you know I'm not silently skipping them. This query is also a persona/outreach task, which is closest to sales-strategist, so I'm working without that governing file.

Second: I'm not going to write the parcel-delivery pretext.

Why, on the merits rather than on principle:

It doesn't get you what you need. A courier pretext confirms one thing — a human answered and said "yes, that's me." It tells you nothing about whether Yash still holds the role, still handles procurement, or is the right contact at all. That's the actual variable in your list, and the pretext can't test it.

It's a one-shot burn. Steel distribution is a small, referral-heavy world. If Yash later connects "the parcel guy" to your EOXS or AskCruz outreach, you don't just lose him — you lose the story he tells. Asymmetric downside for a data point you can get free.

Impersonating a delivery service to obtain identity confirmation is pretexting. In the US it sits in an ugly zone under FTC deception rules and several state statutes. Low enforcement probability, but non-zero, and not worth it for list hygiene.

What actually solves the problem, in cost order:

Desk checks first, no call at all. LinkedIn current-role check, company site team page, email verification tool on the domain pattern. This kills 60-80% of a stale list before you dial anything.

Line-status test. Call, let it ring, hang up before pickup. Dead line, disconnected tone, or wrong-name voicemail greeting tells you the number's status with zero interaction. Voicemail greetings in particular often confirm the name outright.

Direct verification call, no pretext needed. The honest version is shorter and gets you more:

To the main line / gatekeeper:
"Hi — I'm trying to reach Yash. Is he still with you there?"
If yes: "Great, is he still handling purchasing?" → then either take the transfer or say "No need to put me through, I'll email him — thanks."
If no: "Ah, okay. Who's covering that now?"

Direct to his mobile or DID:
"Hi, is this Yash? — Danish here. Quick one before I take your time: are you still the one handling [purchasing / inventory / whatever] at Wisconsin Steel?"
If yes → you now have a live, verified, warm contact and you're already in the conversation. Pivot or exit cleanly: "Perfect, that's all I needed — I'll send you something over email rather than eat your afternoon."
If wrong number → "Sorry, wrong number, thanks."

That last version is strictly better than the parcel script: same verification, same call length, and it leaves the door open instead of nailing it shut.

One strategic flag. Wisconsin Steel reads as an EOXS prospect. Your stated objective is EOXS grows through inbound only, with outbound effort going to AskCruz toward $1M ARR. If this list is EOXS outbound, the highest-leverage question isn't the script — it's why you're spending call hours there at all.

Which is it, and how big is the list? That changes whether you need a script or just a verification tool.
