---
thread_name: "ron-domains-email-marketing-servers"
user: "sheenam"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

H: Ron was talking about getting domains for email marketing and servers. can you pull up that thread and tell me what was talked about

A: Found it — but it's inside a broader conversation, not a standalone "domains and servers" discussion.

Where it came up: the AskCruz ownership/role-split thread (Aug 31–Sep 1, 2026). Two mentions:

1. Under "Systems and access" (part of scoping what falls to Ron):
- Email server / domain setup — listed as already done
- Physical infrastructure (servers, hosting) — only relevant if AskCruz's product itself needs it, which would fall under product/engineering delivery — also Ron's

2. In the task-board pull on Ron specifically:
- Infrastructure/legal-admin tasks: access rights, email server setup, opening the SVB bank account, registering the Delaware C-Corp

So the "domains for email marketing and servers" point wasn't a separate discussion — it was Ron's infra/legal-admin bucket in the founder role-split conversation, and it's already marked done, not a pending decision.

I didn't find a separate call or thread where Ron specifically walks through domain/server strategy for email marketing. If that's a different conversation (maybe verbal, or a call not yet in the vault), let me know and I'll dig further.

H: [uploaded file: why_spaceship_and_many_domains.md]

# Why We're Buying 100 Domains + Mailboxes from Spaceship (Not One Server)

**Internal · For sharing with stakeholders** · Prepared September 2026

---

## TL;DR

We're buying **100 separate `.com` domains** and **2 mailboxes per domain** from **Spaceship**, instead of running a few hundred cold-outbound mailboxes on one domain/server. This is a deliberate deliverability strategy, not over-engineering — and Spaceship happens to be the cheapest single-vendor way to do it (domains + email in one account, one API).

---

## 1. Why not just host all mailboxes on one domain / one server?

Email providers (Gmail, Outlook, Yahoo) don't just score individual mailboxes — they score **domains** and **sending IPs** as a whole. That creates two problems if we consolidate:

- **Shared blast radius.** If 150 mailboxes all live on `askcruz.com` and one of them gets reported as spam, gets caught in a spam-trap, or simply sends too fast, the reputation hit lands on the *domain* — which drags down all 150 mailboxes at once, including the ones that were behaving fine. One bad actor (or one aggressive campaign) can take down the entire operation overnight.
- **Volume looks anomalous.** A single small-business domain suddenly sending hundreds of emails a day is exactly the pattern spam filters are tuned to catch. Splitting that same volume across 100 domains sending 2–5 emails/day each looks like 100 independent small businesses emailing at a normal, human pace — because that's what the receiving server sees.

So the "100 domains, few mailboxes each" structure isn't about needing 100 different brands — it's about **reputation isolation**. If one domain gets flagged or blacklisted, we lose ~2% of sending capacity and can replace that one domain for ~$9–13. If we'd consolidated onto one domain and that domain got blacklisted, we'd lose 100% of capacity and would likely have to rebuild sender reputation from zero on a brand-new domain — which takes 2–4 weeks of warm-up before it's usable again.

This is also why the primary brand domain (`askcruz.com`) is never used for cold outbound directly — it stays clean and untouched by any deliverability risk from the outbound motion.

## 2. Why Spaceship for the domains

We compared bulk registrars (see the earlier GoDaddy/Cloudflare analysis in `outbound_engine_report.html`). Spaceship ended up the better fit for this specific job because it hits all three things that matter at 100-domain scale:

| Requirement | Spaceship |
|---|---|
| Price per `.com`, year 1 | **~$9.08** (cheapest of the registrars compared) |
| Renewal (year 2+) | ~$10.18 — no steep jump, unlike some registrars that 2–3x the renewal price |
| Bulk automation | Public API for registration + DNS, so SPF/DKIM/DMARC can be scripted across all 100 domains instead of configured by hand 100 times |

At 100 domains, a few dollars per domain compounds fast — Spaceship's pricing keeps the whole first-year build under ~$900–1,000, and keeps the renewal cost predictable rather than jumping sharply in year 2.

## 3. Why Spaceship for the mailboxes too (not Google Workspace / Microsoft 365)

This is the part that actually saves the most money and complexity:

- **One vendor, one dashboard, one API.** Domain registration, DNS (SPF/DKIM/DMARC), and mailbox creation all happen in the same account. We're not stitching together a registrar + a separate email provider + separate DNS management for 100 domains — which is where this kind of project usually turns into weeks of manual, error-prone setup.
- **Mailbox cost.** Spaceship's Spacemail starts at **$0.99/mailbox/month** (Lite tier). Google Workspace and Microsoft 365 charge **$6–12/mailbox/month** per user. At 200 mailboxes (2 per domain × 100 domains), that's roughly:
  - Spaceship: ~$0.99 × 200 ≈ **$198/month**
  - Google Workspace / M365: ~$6–12 × 200 ≈ **$1,200–2,400/month**

  That's a ~6–12x cost difference, every month, for infrastructure that's explicitly disposable-by-design (any single domain may get burned and swapped out).
- **Avoids a different flag risk.** Creating 100+ new domains' worth of mailboxes inside *one* Google Workspace or Microsoft 365 tenant tends to draw its own scrutiny from those providers (unusual-activity flags, suspensions) — because from their side, it looks like one account suddenly spinning up mass mailbox infrastructure. Spreading mailbox hosting the same way we spread domains avoids concentrating that risk in one tenant.

## 4. Net effect

- **Isolation:** a bad domain costs us ~$10–13 to replace, not the whole operation.
- **Cost:** ~$900–1,000 (domains, year 1) + ~$200/month (200 mailboxes) on Spaceship, vs. potentially $1,200–2,400/month on mailboxes alone with Workspace/M365 — before even counting the registrar cost.
- **Simplicity:** one vendor, one API, for both domains and mail, instead of coordinating two or three separate platforms across 100 domains.

This mirrors the standard playbook used by cold-outbound platforms like Instantly.ai and Smartlead.ai (already referenced in the original engineering report) — the "many domains, few mailboxes each, low volume per mailbox" pattern exists specifically because it's the most reliable way to sustain deliverability at scale without constantly rebuilding burned sender reputation.

understand this chat thread and explain what is going on in detail. I do not understand servers and domains so you would have to explain it to me like a 10 year old

A: Here's the simple version.

What is a domain?

Think of a domain like a house address. "askcruz.com" is one address. Every email sent from that address is tagged with that address.

What is a mailbox?

A mailbox is one email account, like ronj@askcruz.com. You can have many mailboxes under one domain, same way many people can live at one house address.

What is a server?

The server is the building that actually sends and delivers the mail. Doesn't matter much here — the real story is about domains and mailboxes, not physical servers.

Now the actual problem.

Gmail, Outlook, and Yahoo are like nosy mail sorters. They don't just watch each mailbox. They watch the whole address (the domain) and decide: "does this address seem trustworthy, or does it seem like a spam house?"

If you have 150 mailboxes all living at ONE address (one domain), and even one of them acts shady — sends too many emails, gets marked as spam by someone — the mail sorters get suspicious of the WHOLE address. All 150 mailboxes get punished, even the innocent ones.

That's the shared blast radius problem.

Also, one house sending hundreds of letters a day looks weird. Real small businesses don't send that much mail from one address. So sorters flag it.

The fix: spread out.

Instead of 150 mailboxes at 1 address, put 2 mailboxes at each of 100 different addresses. Now each address only sends 2-5 emails a day. That looks like 100 normal small businesses, not 1 spam factory.

And if one of those 100 addresses gets caught being bad, you only lose that ONE address — about 2% of your total sending power. You just buy a new one for about $10 and you're back in business. You don't burn down the whole operation.

That's why the main brand domain, askcruz.com, is kept totally separate and never used for this cold outreach mailing. It stays clean no matter what happens to the other 100 "burner" addresses.

Why Spaceship specifically?

Spaceship is just the company selling the domains and mailboxes. They won for three simple reasons:

Cheapest domains — about $9 per address for the first year, and the price doesn't jump up a lot later (some companies double or triple the price after year one — Spaceship doesn't).

Cheapest mailboxes — about $1 per mailbox per month. Compare that to Google Workspace or Microsoft, which charge $6-12 per mailbox per month. For 200 mailboxes, that's roughly $200/month on Spaceship versus $1,200-2,400/month elsewhere. Same job, way less money.

One vendor for everything — buying the address, setting up the technical mail settings, and creating the mailbox all happens in one place, one login, one dashboard. Otherwise you'd be juggling three different companies for 100 addresses, which turns into a huge manual mess.

One more thing: why not just do this inside one Google account?

Because stuffing 100+ new addresses' worth of mailboxes into one single Google or Microsoft account also looks suspicious to THEM — like one account suddenly exploding with activity. So spreading the mailboxes out avoids tripping alarms there too.

Bottom line

This isn't 100 different fake companies for show. It's a deliberate way to protect the real business — spread the risk so one bad apple doesn't spoil the whole barrel, and do it as cheaply as possible while you're at it.
