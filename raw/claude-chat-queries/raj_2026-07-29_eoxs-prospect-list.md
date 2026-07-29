---
thread_name: "eoxs-prospect-list"
user: "raj"
type: claude-chat
created: 2026-07-29
updated: 2026-07-29
---

User: prospect list of eoxs

A: 252 total opportunities in the CRM (EOXS Teams Live, live query, not OV2's deprecated prospect tools). Breaking down by stage:

**Closed — not live prospects**
- WON (clients): 7 — 3GM Steel, Sabre Alloys, Discount Pipe & Steel, RW Conklin Steel, David Brannon, PPC Speciality Metals, plus Monarch's earlier WON entries don't appear here (Monarch shows as Unsure/Parked, worth checking separately)
- LOST: ~34
- Disqualified: ~15

**Live pipeline (the actual "prospect list")** — roughly 196 open opportunities, by stage:

| Stage | Count (approx) |
|---|---|
| Leads | ~55 |
| Unsure | ~40 |
| Intent | ~35 |
| Actions Pending | ~20 |
| Parked Accounts | ~20 |
| Discovery Call (Done) | ~12 |
| Client Proposal | ~7 |
| Rescheduled | 1 |

Notable open ones with real expected_revenue attached (most records show $0 expected_revenue, meaning it's not filled in — not a reliable pipeline-value indicator):
- Titanium Industries Inc — $61,632, Actions Pending, Scott Begin
- North Shore Steel — $328,800, Intent, Ron
- Three D Metals Canada — $277,107, Parked, Raj
- Superior Steel Supply — $119,017, Parked, Lew Dennen
- Coilplus — $308,400, Intent, RJ
- Farmers Copper — $73,152, Intent, RJ
- Varsteel/Varsteel Company — $484,400 / $207,600, Parked/Intent, RJ/Lew
- Worthington Industries — $4,154,400, Leads, Raj (very old, 2022, likely stale)
- Excelsior Metals — $394,320, Disqualified (dead)

Raj — this full 252-row list has a data-quality problem: 60-70% of open opportunities have $0 expected_revenue filled in and haven't had a stage update since 2025 or earlier despite "active=true" — that's not a real pipeline, that's a stale CRM. If you want, I can pull the ones stalled >90 days for cleanup, or filter to just this year's genuinely active motion.

Want the full 196-row list as a file (CSV/xlsx) instead of a truncated table, or a filtered cut (e.g. only 2026 activity, or only >$0 expected revenue)?

---

User: gather me the list of our employees

A: Before I pull the employee list, I need to clarify scope:

**5 ft deep** — just names, titles, and roles from EOXS Teams Live HR/employee module if available, plus any team roster pages in the vault. Quick scan, minimal enrichment.

**10 ft deep** — verified against multiple sources: HR records, email senders across raj_gmail/ron_gmail, current Odoo user accounts, team wiki pages. Cross-check to catch inactive vs. active, spot duplicates, and confirm current roles.

**50 ft deep** — full picture including: all current staff with roles/departments, start dates, contract status (employee vs. contractor vs. intern), compensation level if available, reporting lines, and any active projects/assignments from the Odoo Implementation Kanban. Plus flag any departures or transitions in motion.

You also have 50 MBA interns incoming — do you want them included in this pull, or just permanent/core staff?

Which depth?

---

A: 60 active users in EOXS Teams Live. Quick scan shows a mix of real staff, test accounts, bots, and what looks like third-party integrations. Here's the core staff (filtering out obvious test/bot/partner logins):

**Leadership & Core**
- Rajat Jain (rajat@eoxs.com)
- Ron (ronn@eoxs.com)
- Ayan Dutta (ayanduttaeoxs@gmail.com) — co-founder, engineering/AI
- Aryan Bakshi (aryan@eoxsteam.com) — implementation

**Sales & Account Management**
- Scott Begin (scott@scottbegin.com)
- Yashvir Singh Thakur (yash@eoxsteam.com)
- Lew Dennen (lewis@lewdersteel.com)
- Timothy Quinn (Timothy@eoxs.com)
- RJ (rajat@prata.ca)

**Development & Tech**
- Dhrup Kumar Singh (dhrup@eoxsteam.com)
- G. Nijamuddin (nijam.eoxs@gmail.com)
- Kartikey Tripathi (kartikeyeoxs@gmail.com)
- Hashir Saleem (hashir@eoxsteam.com)
- Humaira Zainab (humaira@eoxsteam.com)

**Other Staff**
- Isha Bisht (isha@eoxsteam.com)
- Sheenam Rawat (sheenam@eoxsteam.com)
- Sakshi (sakshi@eoxsteam.com)
- Anvitha Shetty (anvitha.eoxs@gmail.com)
- Azra Saleem (azrasaleemeoxs@gmail.com)
- Mahesh Mudiraj (mudirajmahesh4eoxs@gmail.com)

Plus ~20 recent adds (Jan-Jul 2026) with inbox-style logins — likely interns or newer hires from the 50-person MBA internship program (names: Aaryan Mehra, Anjali Singh, Ankit Pachauri, Arshad Malik, Harsimran Singh, Jaskeerat Singh, Kriti Jain, Mahnoor Saeed, Maria Naeem, Misbah, Nidhi Rana, Prashant, Priyanshu Sinha, Rohit Chand, Talal, Vaibhav Jain, Vithal, etc.).

Want this exported as CSV/xlsx, or just the core team subset?
