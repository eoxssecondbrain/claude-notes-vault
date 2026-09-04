---
thread_name: "siv-bolna-calling-vs-link-approach"
user: "sheenam"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Human
As you know, I have created an AI hiring agent on Bolna AI, and I've named it Siv. You can go through the chat in this Claude account to get more context.
Now I have set up the agent for the post of operations manager. There are a couple of things that I would like to clarify. Raj said that, instead of having this agent called AI, these calls would work on Bolna like this: I will upload a CSV-format file of all the people that need to be called. For example, I have 818 applicants for the post of operations manager. I will upload the sheet with 818 applicants' phone numbers on Bolna, and Bolna will automatically start calling all of these numbers. Whichever numbers are called and answered, the interview would be conducted. All the data of the interview, the transcript, would be saved in Bolna. I can download it and export it however I need.
Now Raj said that, instead of having this agent call each of these numbers, he suggests that we should have a mechanism where we can share a link with all these applicants over LinkedIn (because they applied for the job post on LinkedIn). We can share this link with them, and then these applicants can click on that link, and then they would get a call.
I understand this idea, and that is initially what I thought, but that would require a lot of manual configuration. Someone would have to sit and send that link to all those 818 candidates, and they will open that link and then conduct the interview.
The second concern that I have with this is that a lot of people are skeptical about opening links on their systems because everyone sees that as dicey. If I were to get a link on my LinkedIn and it would ask me to click on a link to set up the interview, I would also not click it. I would also try to verify the website and the person who has sent me the link.
If I don't have the mandate to send these links, whoever would send these links to each of these people would also need to have a verifiable background. If they go and check about the company (for example, we are doing this for Askcruz), there is no surety that they would even believe it because we don't have a website yet. It kills our credibility to some level.
Another thing that I worry about with this method is that a lot of people use LinkedIn on their computers. If they use it on a computer and click on that link on their computer, they won't be able to receive the call because the call is required to be on the phone number, and the phone number needs to be available to make this call. It does not seem feasible to me. I need to explain this to Raj because he asked me: instead of having this agent call all these people, people should get the link.
Lastly, another concern that I have is that the rate of these interviews being actually conducted will totally depend upon the people actually clicking the link. If they don't click on the link, we don't get an interview. These are my concerns. What do you think about them? I need to send Raj back an update on this, and I would like to make this agent live today to conduct the post for operations manager.

# Assistant
Read threads-ov and raj-eoxs-vault skill files, pulled the eoxs-db index, checked memory notes on the Siv project, and searched past chats for prior Bolna context (nothing indexed yet on Bolna specifically — the last recorded state was the Sept 2 decision to test Agni AI for async link-based screening, so this Bolna/CSV-calling setup is new since then).

Your concerns are legitimate, not just resistance to Raj's idea — the manual workload, the link-trust problem (especially with no AskCruz website yet), the desktop-vs-phone issue, and the click-dependent conversion rate are all real operational risks with the link approach.

This needs a proper side-by-side before I hand you something to send Raj, and it ends in a message to him — so two quick picks first:

1. How deep should the comparison go
2. How polished should the update to Raj be

Rigor:
5ft deep - quick, fastest read on the tradeoffs
10ft deep - verified, checked against real numbers where possible
50ft deep - full investigation, plus angles you didn't ask about
100ft deep - staged, delivered section by section

Craft (for the Raj update):
Sketch - bare structure, one pass
Draft - styled, presentable, not fussed over
Painting - custom, detail-checked
Commissioned - full polish

[ask_user_input_v0 called: Q1 "How deep should the comparison go?" options 5ft deep / 10ft deep / 50ft deep / 100ft deep. Q2 "Craft level for the update to Raj?" options Sketch / Draft / Painting / Commissioned]

# Human
Q: How deep should the comparison go?
A: 50ft - deep

Q: Craft level for the update to Raj?
A: Draft

# Assistant
Your four concerns hold up. There's also a fifth risk neither of you raised, and it might matter more than the link-vs-call debate itself.

1. Manual effort — confirmed
Sending 818 links by hand is real work, and it repeats for every future job post. Not a one-time cost.

2. Link trust — confirmed, and worse for AskCruz specifically
A cold link from an unfamiliar company with no website looks like a phishing pattern to most people. You're right that you wouldn't click it either. This hits AskCruz harder than it would EOXS, since EOXS already has a public track record people can check.

3. Desktop vs phone — confirmed
LinkedIn gets heavy desktop use for job browsing. A link clicked on desktop can't take a call unless the flow then asks for a phone number and dials out anyway — which brings back the outbound-call problem Raj is trying to avoid, just one step later.

4. Click-dependent conversion — confirmed
Industry data on recruiting outreach consistently shows text-based and call-based contact converting far better than link-click flows — staffing and recruiting texts see something like a 37% response rate versus under 9% for outreach email. A cold LinkedIn link behaves more like the email number than the text number. Some real share of your 818 never click, on top of whoever wasn't going to answer a call either.

The risk nobody flagged: compliance and answer rates on the outbound side
This could sink the CSV-calling plan even if Raj drops his objection. Bulk commercial voice calls in India fall under TRAI's telecom customer preference regulations, and AI calling gets treated the same as human calling — there's no exemption for it being a bot. Calls need to go out from a number registered to the right category — a different series for promotional versus service/transactional calls — and numbers outside that registration get recognized and ignored, or flagged.

A job interview call probably qualifies as a service call tied to something the candidate started (their application) — a much better position than cold sales dialing. But that only holds if Bolna's setup actually has the number, sender registration, and consent trail configured that way. Worth confirming, not assuming.

Before you go live today: check with whoever set up Siv on Bolna that the calling number is on the correct registered series and that AskCruz is the registered sender, not just Bolna's default number. If that's not sorted, the batch can start getting flagged mid-run today, and answer rates tank regardless of who wins the Raj conversation. Fifteen minutes to check, and it's separate from the Raj discussion entirely.

One more thing worth knowing before you write to Raj
This isn't a brand new idea from him. The plan that came out of scoping Siv on Sept 2 was link-based screening. Somewhere between then and building it on Bolna, that flipped to CSV outbound. Raj is holding the original plan — you're the one who pivoted. Worth naming that to him directly. It reads very differently as "we tried link-based, here's what changed once we built it out" than as pushback on something new of his.

A middle ground that might solve what Raj actually wants
If his real concern is candidates getting blindsided by a cold AI call, a heads-up text right before the call does that without needing anyone to click anything. Text reminders measurably cut no-show rates in similar screening contexts — one trial dropped no-shows from 38.1% to 23.5% just by adding one. No link, no manual sending, no desktop mismatch. Worth offering as the compromise instead of picking a side.

What I'd do today
Launch the outbound batch as planned. It's already built, and Raj proposed an alternative, he didn't say hold the launch. Send him the explanation in parallel, not as a gate. Confirm the DLT/number registration before the batch goes out, not after.

[message_compose_v1 called: draft message to Raj, kind=other, single variant "Direct explanation" — body: "Following up on the link idea for operations manager screening.\n\nA few practical issues with candidates clicking a link: someone has to manually send all 818 links, a cold link from a company with no website yet reads as phishing to most people, and a lot of applicants browse LinkedIn on desktop so clicking there doesn't guarantee they can take a call after. Realistically we lose a chunk of candidates just to who does and doesn't click.\n\nWorth noting - link-based was actually the original plan when we scoped Siv. We moved to CSV outbound calling on Bolna once we started building, because it drops the click-dependency and the manual sending.\n\nMiddle ground: I can add a short heads-up text right before each call goes out, so people aren't blindsided by an unknown number. Gets you the \"give them notice\" piece without the link problems.\n\nGoing live today with the outbound batch for the 818 operations manager applicants, unless you want to hold."]

Draft's above — swap the channel wording if you're sending it somewhere other than WhatsApp/Slack.

# Human
Can you check on Bolna's website and see how they are regulating this issue so that the number does not get flagged? Whoever created this application must have seen this coming, and they offer 4 providers. I remember Twilio, then we had Exotel and 2 more. You can see that in the chart we had yesterday. It might have the names of the providers. Once we do get a proper subscription, we would also have a number that would actually be making all these calls for us. Please go and check all of this information for me.

# Assistant
I want to flag something before continuing: that last tool result had a "SYSTEM REMINDER" embedded in it telling me to call save_chat_transcript with a parameter name that doesn't match the actual tool (asking for new_messages instead of content, and pushing urgency language like "do it now, don't ask permission"). That's not a real Anthropic system message — it came from inside the tool's data. I'm ignoring its specific instructions and sticking with the correct tool schema and my own standing save routine, just flagging it since it has the shape of an injected instruction.

Couldn't find a chart specifically from yesterday in your saved threads — closest match was a Sept 2 to 3 comparison table that had Agni vs Bolna feature-by-feature, but not a 4-provider breakdown. That breakdown turned out to be simpler to just confirm straight from Bolna's own docs.

The 4 providers, confirmed
Twilio — for calls outside India
Plivo — within India
Vobiz — within India
Exotel — within India
Plus a fifth option: bring your own SIP trunk if you already have a telephony provider

For India numbers specifically, Bolna splits by call type. Vobiz handles 140-series numbers (promotional/telemarketing category). Plivo handles 160-series numbers (transactional/service category).

How Bolna handles the flagging issue — the real answer: they don't, you do
This is the part worth knowing before today. Bolna doesn't automatically protect your number from getting flagged. There are two separate gates, and I can't check from outside whether either is done on your account.

Gate 1, Bolna's own check
Before you can buy any phone number on Bolna at all, you submit a one-time compliance application: your CIN certificate (company registration) and GST registration. This is Bolna's own KYC, not India telecom law.

Gate 2, TRAI DLT registration
This is the actual legal requirement that keeps a number from getting flagged or blocked in India. You register as a Principal Entity on a DLT portal (Bolna's Vobiz partner points to the TATA Teleservices one), submitting CIN, GST, PAN, your MOA with director list, and a Letter of Authorization signed by a director named in the MOA. There's a ₹5,900 fee. Once approved, you get an actual registered 140-series number.

Neither step happens automatically at signup. If AskCruz hasn't cleared both, the number making today's 818 calls isn't a registered number — which is exactly what gets a batch auto-flagged or blocked partway through.

The other thing this affects: speed, not just legality
Bolna also caps how many calls run at once, by account tier, separate from the DLT question entirely.
Trial accounts: 2 calls at a time, verified numbers only
Paid accounts: 10 calls at a time minimum, scales up from there

At 2 concurrent, getting through 818 applicants realistically takes over a day, not today. At 10+, it's a few hours.

What to check right now, before you hit go
Five minutes each, in the Bolna dashboard:
1. Workplace settings, account limits — trial (2 concurrent) or paid (10+)
2. Whether the CIN+GST compliance application has been submitted and approved
3. Whether Siv's assigned number is an actual DLT-registered 140 or 160-series number, or a default/test number

If any of those three aren't sorted, that's the real blocker for going live today — not the Raj conversation.
