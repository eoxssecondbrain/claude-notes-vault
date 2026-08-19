---
thread_name: "linkedin-outreach-customers"
user: "yashvir"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: Are you aware, how many EOXS customers did we found through the LinkedIn outreach, just give me the names and dates of the outreach.

Assistant: I don't have a clean answer for this — here's what the data actually supports and where it breaks down.

**What's confirmed:**
- None of EOXS's 8 current paying clients (Sabre Alloys, 3GM Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, Ohio Strip Steel/Greer, RW Conklin Steel, Brannon Steel) have a wiki-documented origin story that traces to LinkedIn outreach. 3GM Steel's origin traces to a Travis Lane/Scott Begin referral, not LinkedIn.
- **Pacesetter Steel Service** — Technology Director Thomas Sulkowski contacted Rajat directly via LinkedIn on **2023-05-16**. This is the one clean "LinkedIn-sourced lead" record I found. But it's tagged as a *prospect* in the wiki, not a client, and it isn't in the client registry — so it doesn't look like it closed.
- **Bryan Lord** — cold LinkedIn contact on **2022-12-22**, converted to a call within a day. He became a signed *advisor* (Dec 2022), not a customer.
- A 2021 email archive references aggregate LinkedIn outreach numbers — **1,688 approached, 20 responses, 6 demos** — and a separate broader BOF pipeline (May–Sept 2021, 30 demos, 2 won) — but no names are attached to the "2 won" in what I pulled, and this predates EOXS's ERP pivot (still "The Steel Store" marketplace at that point), so it's unclear those 2 wins are even ERP customers.

Straight answer: I can't give you a verified names+dates list of customers won via LinkedIn outreach. The record either shows LinkedIn leads that didn't convert to customers, or aggregate outreach stats with no names attached. This needs a proper pass — cross-referencing LinkedIn-origin leads in eoxs-db against actual won deals in eoxs-teams (CRM), rather than wiki snippets.

Want me to run that properly? Pick a level:
- **10ft** — pull every LinkedIn-tagged lead from eoxs-db, cross-check each against eoxs-teams CRM for won/customer status
- **50ft** — same, plus check if the 2021 "2 won" and any other unnamed outreach-era wins map to any client in the current registry, and flag data gaps
