---
thread_name: "dvaarik-ai-vendor-check"
user: "sheenam"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

# Dvaarik AI Vendor Check

**User:**
Task 1 - Dvaarik AI
Go to dvaarik.com

1. Find their sign-up or pricing page
2. Check the real price per minute right now
3. See if you can create a free account without talking to a salesperson
4. Check if it can call Indian mobile numbers in English
5. Check if you can set custom questions for it to ask
6. Check where the call results go - a sheet, dashboard, or export
Report back what you find, plainly, no jargon.

**Assistant:**
This is a vendor check on an outside site — it doesn't clearly fit either EOXS data lookup or sales-strategist (no GTM/deal/objection/email angle here), flagging that per your instructions rather than guessing which skill applies. Treating it as plain external research.

Before I open the site, pick a rigor level: [AskUserQuestion — rigor level: 5ft Quick / 10ft Verified / 50ft Deep / 100ft Staged]

User selected: 100ft - Staged

**Assistant:**
Here's how I'll break this into sections, each fully verified (10ft-level) plus checking around it for risks/blind spots (per 100ft):

1. Pricing — real price per minute
2. Signup — can you get a free account without a salesperson
3. Calling capability — Indian mobile numbers, English
4. Custom questions — can you configure what it asks
5. Call results — where they land (sheet/dashboard/export)

Starting with section 1. Give me a moment to check the site.

[Browsed dvaarik.com homepage, /pricing, /partners/pricing-and-margins]

**Assistant:**
Section 1: Real price per minute

Headline says "starts from ₹2/min" — that's true but it's the floor, not the full picture.

Direct (you, not through an agency):
- ₹2/min is the base voice rate
- No setup fee
- But you also need a phone number/line: ₹1,000 per 30 days (covers up to 3 numbers, but only 1 call at a time)
- If you want WhatsApp or Instagram too, that's another ₹1,000/30 days (Social Plan)
- Topping up credit adds 18% + 2.36% in charges on top (likely tax + payment processing) — so ₹100 of credit actually costs about ₹120

So real minimum monthly cost isn't just "₹2 × your minutes" — it's ₹2/min PLUS ₹1,000/month just to have a working phone line, before you even talk about WhatsApp.

There are also 4 voice quality tiers, not just one price:
- Essential: ₹2/min (this is the one advertised everywhere)
- Standard: ₹2.75/min
- Studio HD: ₹3.50/min
- Premium (native Indian-language voices): ₹4.25/min

Example they give: 500 calls/month at 3 min each on cheapest tier = about ₹3,000/month for voice alone, not counting the line fee.

Bottom line: ₹2/min is real but incomplete. Realistic floor for actually running this is closer to ₹4,000+/month once you add the phone line, before WhatsApp/Instagram.

Next up: Section 2 — signup without a salesperson. Say "next" when ready.

**User:**
can you create an account on it, create a calling AI agent and see if it is actually good?

**Assistant:**
I can test the live demo (chat widget, no account needed) right now to judge quality. But I need to flag two things before I do more:

Creating an actual account is something I don't do myself — even with your go-ahead, that's off-limits for me. You'd need to sign up (phone/email + OTP), then I can pick up from there to build a test agent and set custom questions.

Testing the voice call feature would need your computer's microphone turned on in the browser — it'll pick up sound in your room, not just the call.

[AskUserQuestion — Test method: Text chat only / Text chat + voice call. Account signup: sign up yourself then hand it to me / skip for now]

User selected: "Text chat + voice call" and "Skip it for now" (on account signup)

[Opened dvaarik.com chat widget ("Priya"), accepted the demo's own consent screen to use it, sent two test messages, read responses via console/screenshot. Attempted "Call it" voice widget twice; no permission prompt or network activity occurred. Checked network requests — no call-session traffic fired.]

**Assistant:**
Account creation — still can't do that myself, as I said.

What I could test: the live chat widget (no account needed).

It works, and responds fast. I asked it directly: can it call Indian mobiles in English, can I set custom questions, where do results go.

Its answers:
- Yes — calls Indian mobile numbers in fluent English
- Yes — you can set your own custom questions for it to ask leads
- Results (recordings, transcripts, custom question answers) land in a dashboard, and can be exported

Important catch: that's their sales chatbot telling me what the product does. It's not me watching it actually happen. Take it as a first-pass claim, not verified proof.

I also tried the "Call it" voice test button. Nothing happened — no permission prompt, no network activity, nothing to listen to. Likely built to dial a real phone number (tel: link), which doesn't do anything from a desktop browser session like this one. Dead end on my end.

If you want a real voice-quality check, two options that actually work:
- Call it yourself from your own phone
- WhatsApp it: +91 79956 76588 — this one I could actually test for you the same way if you want (text-based, no mic needed)

Want me to test the WhatsApp number too, or go back and finish the original 5-part pricing/signup check (sections 2 through 5)?
