---
thread_name: "askcruz-cold-email-mailbox-infra"
user: "Harsimran"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

# Thread: askcruz-cold-email-mailbox-infra

## User (turn 1)
i want to buy 50 emails for bulk cold emailing , my budget is 50 dollar and i have 50 different domains

## Assistant (turn 1)
Quick reality check before anything else: $50 doesn't cover 50 professionally-provisioned mailboxes anywhere in the current market. The cheapest verified option for exactly 50 mailboxes is $69/month, not $50. At $50 you'd realistically get about 36 mailboxes at the best rate available, not 50.

Bigger issue worth flagging first: your own strategy says EOXS grows through inbound only, and AskCruz is the one meant to push outbound toward $1M ARR. Which product is this cold email infrastructure for? If it's EOXS, this directly contradicts your stated inbound-only approach. If it's AskCruz, cold outbound is a reasonable lever for the ARR target and this is worth doing properly.

One process note, per your own instruction to flag skill mismatches rather than guess: you told me to check raj-eoxs-vault and sales-strategist skill files before acting on a new thread. Neither exists in this environment — only threads-ov and eoxs-data-general are installed. eoxs-data-general covers internal EOXS data (emails, calls, wiki, tickets, CRM) and doesn't apply here since this is external vendor research, not a data lookup. So nothing here matches your setup cleanly.

Here's where the market actually sits for ~50 mailboxes, since you already own the 50 domains (which matters — one of these lets you use your own domains for free instead of paying for provisioning):

[Comparison card rendered — "Realistic mailbox-provider pricing for 50 domains against a $50 budget"]

Provider | Price | Mailboxes for that price | Per-mailbox cost | Bring your own domain | Warmup | Infrastructure
Winnr (Startup plan) | $69/mo | 50 | $1.38 | Free | $0.60/mailbox/mo add-on | Custom SMTP, shared IP
Mailforge | $100-150/mo (raw) | 50 | $2-3 | Not confirmed free | Add-on (~$200/mo total w/ warmup) | Shared-IP SMTP
InboxKit (Agency plan) | $164/mo | 30 base + 20 extra | ~$3.25 avg | Not confirmed free | Included | Managed SMTP + monitoring

Before I recommend one and finalize a plan, I need three things clarified:

[ask_user_input_v0 card rendered with three questions]
1. Which product is this cold email push for? (EOXS / AskCruz / Both / Something else)
2. Is $50 a monthly recurring budget or a one-time spend? (Monthly recurring / One-time only / Flexible starting point)
3. Do you already have a sending platform to plug mailboxes into (Smartlead, Instantly, lemlist, Apollo)? (Yes, already have one / No, need that too / Not sure yet)

## User (turn 2 — answers to clarifying questions)
Q: Which product is this cold email push for?
A: AskCruz

Q: Is $50 a monthly recurring budget or a one-time spend?
A: Monthly recurring

Q: Do you already have a sending platform to plug mailboxes into (Smartlead, Instantly, lemlist, Apollo)?
A: I will connect with my claude

## Assistant (turn 2)
AskCruz makes sense — cold outbound is a legitimate lever toward the $1M ARR target, unlike EOXS which you've committed to inbound-only.

On the numbers: at $50/month recurring, you can't get 50 mailboxes properly warmed — that math doesn't work anywhere in the market. Here's what actually fits:

Winnr Startup (BYOD your 50 domains for free):
- Mailboxes: $1.38 each
- Warmup: $0.60 each (do not skip this — fresh domains without warmup land in spam within days and get burned fast)
- Combined: $1.98/mailbox/month

$50 / $1.98 ≈ 25 mailboxes fully set up and warmed, for about $49.50/month.

That's less than your 50 domains, but it's not actually a bad place to start — 25 SMTP mailboxes at the recommended ~15 sends/day cap each gives you 375 emails/day, which is plenty for an early AskCruz outbound test. Run 25 domains now, keep the other 25 in reserve, and add them once this batch proves out (or once ARR growth justifies the extra ~$50/month).

If you'd rather use all 50 domains from day one: bump the budget to about $99/month ($69 mailboxes + $30 warmup for 50). Against a $1M ARR target, that $49/month difference is not the constraint that matters — reply rate and deliverability are. I'd lean toward doing 25 properly rather than 50 half-warmed, if forced to pick.

One more thing: the save above shows this vault resolves you as "harsimran," not Rajat. Worth checking if that's the intended account for AskCruz outbound work, or if there's a connector mismatch.

On sending: whatever you route this through — your Claude/Gmail setup or something else — it needs to respect the per-mailbox daily send cap and the warmup ramp schedule. That's not optional at this volume; exceeding it is the single fastest way to get a fresh domain flagged. If "connect with my claude" means manual or semi-automated sending through the Gmail connector, that works for testing on a handful of mailboxes, but it has no automatic safety net (no auto-pause on bounce spikes, no enforced daily caps) once you're running 25+ mailboxes at once — worth knowing that gap exists before you're mid-campaign.

## User (turn 3)
just tell me from where we should buy these emails

## Assistant (turn 3)
Winnr (winnr.app), Startup plan.

Reasons: cheapest verified per-mailbox rate ($1.38), it's the only one of the three that lets you bring your own domains for free (you already own the 50, so this matters directly), and it's SMTP with a documented API if you want to automate later.

What to actually buy at $50/month recurring: 25 mailboxes with warmup included, not 50. That's $49.50/month (25 x $1.98, where $1.98 = $1.38 mailbox + $0.60 warmup). Don't buy the mailbox without the warmup add-on — an unwarmed mailbox on a fresh domain gets flagged fast and you'll have wasted the spend.

If you want all 50 domains live instead of 25, the real number is about $99/month, not $50.

(Note: an earlier save_chat_transcript call in this turn errored; the retry succeeded and this file reflects the full transcript through turn 3.)

## User (turn 4)
if a buy mails from spaceship , will it be good for cold email outreach and and will be pricing for 50 mail s

## Assistant (turn 4)
Spaceship (the domain registrar) itself doesn't do email inboxes — it's the wrong tool. But their email product, Spacemail, does real IMAP/SMTP mailboxes on your existing domains, and it's actually cheaper than Winnr on raw dollars: roughly $0.50-0.90 per mailbox depending on tier, which puts 50 mailboxes at about $25-45/month — under your $50 budget with room to spare.

The catch, and it's a real one: Spacemail is built for normal business email, not cold outreach. Independent reviews are explicit that it doesn't provision inboxes for cold sending, doesn't set up SPF/DKIM/DMARC automatically, and has no warmup or deliverability monitoring — you get basic DNS management and have to configure all of that by hand, per domain, yourself. That's real work across 50 domains, and if you skip it or rush it, you'll burn through your domains fast since nothing is enforcing safe daily send caps or watching for spam-flag spikes.

So the actual tradeoff:

Spacemail: cheaper ($25-45/mo), but you own 100% of the SPF/DKIM/DMARC setup and warmup schedule manually, with no deliverability safety net.

Winnr: costs more ($49.50/mo for 25 warmed mailboxes, as laid out in turn 3), but authentication and warmup are handled for you automatically — which is the entire point of paying a cold-email-specific provider instead of a generic email host.

Given you're doing this for AskCruz and deliverability is the actual bottleneck toward $1M ARR, not the $20-25/month difference, I'd still put you on Winnr. Spacemail only makes sense if you or someone on your team is going to properly own manual DNS + warmup discipline across 50 domains — and if that work slips, you've spent the money and burned the domains anyway.

## User (turn 5)
dows spaceship have a api or mcp ?

## Assistant (turn 5)
No connector for it in Anthropic's directory, so it's not something you can just plug into Claude here — but the underlying pieces exist:

API: yes, official and public (docs.spaceship.dev). REST, covers domain registration/transfer, DNS records, WHOIS/privacy settings, contacts. No mailbox-provisioning endpoints — Spacemail account creation still looks to be dashboard-only, not exposed via the API.

MCP: no first-party one from Spaceship. There's a solid community-built server (BartWaardenburg/spaceship-mcp, 48 tools) that wraps the same API — full DNS record management across all major types (A, MX, TXT, CNAME, etc.), domain lifecycle, WHOIS/contacts. You'd self-host it (it's not in Anthropic's connector directory), point it at your Spaceship API key, and it would work with Claude Code or any MCP-compatible client.

This actually changes my earlier read a bit: the main risk I flagged with Spacemail was manually configuring SPF/DKIM/DMARC across 50 domains by hand. If you script that through this MCP server's DNS tools instead of doing it in the dashboard one domain at a time, that specific risk drops a lot — you could push identical, correct auth records to all 50 domains in one batch instead of 50 manual clicks. It doesn't solve warmup or deliverability monitoring (still nothing built in for that), but it does remove the most error-prone manual step.

## User (turn 6)
does

## Assistant (turn 6)
Looks like that got cut off — what were you asking?

## User (turn 7)
can we set up spf/DKIM/DMARC using spaceship api

## Assistant (turn 7)
Yes. SPF, DKIM, and DMARC are all just DNS records (TXT, and sometimes CNAME for DKIM depending on the provider), and Spaceship's API has a DNS records endpoint that supports exactly those types — PUT /v1/dns/records/{domain}, with TXT, CNAME, MX, and others all supported. Rate limit is 300 requests per domain per 5 minutes, so scripting all 50 domains (3 records each = 150 calls) is trivial.

One thing the API can't do: generate the actual DKIM key or the correct SPF/DMARC values for you. Those come from whichever mail platform you're actually sending through — Spacemail's dashboard if you go that route, Winnr's setup if you go that route. The workflow is: get the record values from the mail provider, then push them to each domain via Spaceship's API instead of clicking through the dashboard 50 times.

This is the same DNS endpoint the community MCP server wraps, so if you connect that to Claude, you could hand it "here are the SPF/DKIM/DMARC values, push these to all 50 domains" and have it done in one batch instead of manually.

## User (turn 8)
how to setup space mail with domain and how to login in that mail, and will this work with cold email outreach

## Assistant (turn 8)
[step_card_display_v0 rendered — "Setting up and logging into a Spacemail mailbox on a domain"]
1. Buy/select the Spacemail plan — In your Spaceship account, go to Hosting > Email > SpaceMail, and pick a plan sized to your mailbox count.
2. Connect a domain (Unbox) — Click Unbox > Add Domain, then either pick an existing Spaceship domain or enter a third-party one. Repeat once per domain.
3. Create the mailbox — Click Configure Products > Configure, enter the mailbox name (e.g. name@domain.com), then Create Mailbox. Spacemail auto-generates a password — copy and save it immediately, it's shown once.
4. Add the DNS records — Click View Guides under Configure DNS Settings to get the exact MX, SPF, DKIM, and domain-ownership TXT records for that domain. Add them at whichever DNS provider controls the domain. At 25-50 domains, do this through the Spaceship API instead of the dashboard.
5. Wait for DNS propagation — Allow up to 48 hours for the records to validate. Sending or warming before this completes will fail or hurt deliverability from the start.
6. Log in and start using it — Webmail: go to spacemail.com, log in with the full mailbox address (name@domain.com) as username and the password saved in step 3. For a sending tool instead of webmail, use IMAP/SMTP: server mail.spacemail.com, IMAP port 993 (SSL/TLS), same username and password — get the full config from Spacemail Manager > mailbox > IMAP/SMTP/POP3.

On cold email fit: technically yes, it sends and receives real mail — nothing stops you from pointing a sequencer at these mailboxes via SMTP. But nothing in this setup handles the part that actually matters for cold outreach: there's no warmup ramp, no daily send-cap enforcement, and no deliverability monitoring. You'd be manually ramping each mailbox's volume over 2-3 weeks yourself and watching bounce/spam rates by hand across however many domains you run. Miss that and you burn the domain fast — SPF/DKIM/DMARC being correct doesn't save you from sending volume before reputation exists.

Net: this gets you real, cheap mailboxes with the DNS setup pain reduced (via the API instead of clicking through 25-50 domains). It does not get you the warmup/monitoring layer that Winnr charges for. If you go this route, budget your own time for manual warmup discipline as the real cost, not just the dollars.

## User (turn 9)
which mail should i buy spacemail pro or special

## Assistant (turn 9)
Pro, not Special.

Special is nearly free (~$0.10/mailbox/month) but only exists as an add-on to a Spaceship Shared Hosting subscription — you'd be paying for website hosting you don't need just to unlock cheap mailboxes, and the published hosting tiers cap how many domains attach to one account (the entry tier lists 5 hosted domains). Covering 50 domains could mean stacking multiple hosting subscriptions, which eats the savings and adds infrastructure you don't actually want for a cold email operation.

Pro is standalone — no hosting dependency, straight per-mailbox pricing around $0.59-0.98/month depending on the commitment term. For 50 mailboxes that's roughly $30-45/month, still under your $50 ceiling, and it's a much simpler purchase: buy mailboxes, not a hosting product with mailboxes attached as a side effect.

One thing worth checking before you buy either: Spacemail's automatic MX/SPF/DKIM setup only auto-configures if the domain's nameservers already point to Spaceship. If your 50 domains sit on their current registrar's DNS, you're back to the manual or API record-pushing from earlier regardless of which plan you pick — that part doesn't change based on Pro vs Special.
