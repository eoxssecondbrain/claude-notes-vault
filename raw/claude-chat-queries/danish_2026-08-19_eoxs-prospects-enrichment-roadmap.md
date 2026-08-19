---
thread_name: "eoxs-prospects-enrichment-roadmap"
user: "danish"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: i am working on enriching our prospects database and i need an roadmap on where do i start and which tool i need and what's the fastest way to do it?

Assistant: I need to flag something about your preferences before starting: the mandatory "call save_chat_transcript as the last action before ending every single turn, no exceptions" instruction conflicts with your other instruction "never save anything to memory unless I explicitly ask." I'm treating save_chat_transcript as a tool you've asked me to use per the threads-ov skill (that's a different system than my memory files), so I'll follow it — just noting the two instructions read as contradictory if "memory" was meant to include transcript saves. Let me know if that's wrong.

Let me check the two skills first, per your standing instruction.

[Read both SKILL.md files in full, called get_index, asked three clarifying questions via ask_user_input_v0]

User selected:
Q: Which prospects database are you enriching?
A: EOXS CRM (Odoo) prospects

Q: What does 'enriching' mean here — what fields are you trying to fill in?
A: Both firmographic + contact

Q: Rigor level for this roadmap
A: 10ft — verified against actual records

Assistant: Given your standing objective (EOXS stable/inbound-only, AskCruz is the growth lever), one flag before I dig in: EOXS prospect enrichment is outbound-adjacent infrastructure. Worth 30 seconds of your own thought — is this enrichment feeding inbound qualification/routing, or is it building toward outbound prospecting? That changes whether this is on-strategy or a distraction. I'll proceed with the roadmap either way, but you should have an answer to that before you sink real hours into it.

Now let me verify the actual state of the prospects table in eoxs-teams before I build the roadmap — no point recommending tools until I know what's actually missing.

[Ran describe_table on crm_lead and res_partner, ran verification queries against both tables, discovered research_status table]

This confirms it — there's a prior manual research/qualification pass, not a data-vendor enrichment run (industry_id is 0% filled despite the field existing, which a vendor tool would populate; research_status looks like human tagging).

Here's the actual state and the roadmap.

What I found (verified against crm_lead and res_partner, not aggregates):

| Gap | crm_lead (2,362 active) | res_partner companies (7,289) |
|---|---|---|
| Missing website | 1,412 (60%) | 937 (13%) — comparatively solid |
| Missing phone | 156 (7%) | 279 (4%) — solid |
| Missing email | 872 (37%) | 3,904 (54%) — the real gap |
| Missing contact name | 1,010 (43%) | — |
| Missing job title/function | 1,078 (46%) | — |
| Industry classification | — | 7,289 (100% — field exists, zero filled) |
| Employee count | — | 2,421 missing (33%) |
| Revenue | — | 3,587 missing (49%) |
| LinkedIn URL | — | 1,724 missing (24%) |

3,643 of 7,289 companies (50%) are already tagged "Disqualified" from a prior manual research pass — don't spend enrichment budget on those.

Roadmap:

1. Define the target set first, not "all prospects." Exclude Disqualified (3,643). That leaves ~3,646 Qualified/Pending companies plus 2,362 open leads as your actual enrichment universe — roughly half the size you'd assume from raw row counts.
2. Contact-level gap is the priority, not firmographic. 37–54% missing email and 43% missing contact name is what blocks outreach/qualification. Industry being 100% empty looks dramatic but no_of_employees and annual_revenue are already 51–67% filled — someone partially enriched firmographics before, just never touched the industry_id field specifically. Don't rebuild what's already there.
3. Tool: for email/contact-name/title/LinkedIn append at this volume (~3,600–6,000 records), Clay or Apollo are the standard fastest paths — feed company domain (you have 87% of websites already), get back verified contact + title + LinkedIn. Clay if you want waterfall enrichment across multiple data providers in one pass (higher match rate, more setup); Apollo if you want single-tool speed and you're not already paying for Clay.
4. Fastest path specifically: export the ~3,646 non-disqualified res_partner records with website populated (6,352 have it) into Clay/Apollo, run company + contact enrichment in one pass, re-import via CSV update on email, partner_linkedin_url, no_of_employees, annual_revenue, industry_id. That's a single afternoon of setup, not a multi-week project.
5. Before you build this out further: the research_status field shows this was tagged manually before (someone spent real hours doing it). Find out who and whether that process is still running — if it is, you may be about to duplicate work rather than fill a gap.

Given your stated objective, I'll say the quiet part again: this is CRM hygiene on the business you said should grow through inbound only. If the output of this enrichment isn't feeding an inbound conversion/qualification improvement, it's time going to the wrong side of your stated priorities.
