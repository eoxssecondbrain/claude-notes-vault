---
thread_name: "askcruz-customer-count"
user: "muskan-sharma"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

User: how many customers does askcruz currently have?

Assistant: No AskCruz-specific data connector is available in this session. Available connectors (eoxs-data-general, Team_EOXS_live) are scoped to EOXS data only, not AskCruz. Flagged that the user's referenced skills "raj-eoxs-vault" and "Muskan-eoxs-vault" are not among the actually-enabled skills (only threads-ov and eoxs-data-general exist). Asked user where AskCruz customer data lives (CRM, spreadsheet, billing system) rather than guessing.

User: in eoxs data general

Assistant: Investigated via eoxs-data-general skill (eoxs-db connector). Found that AskCruz is EOXS's own internal AI product ("Company Brain"), with EOXS as its internal pilot. Confirmed via wiki pages and assets:
- 3GM Steel: confirmed external paying customer. Travis (CCO) confirmed the deal Aug 19, 2026 at reduced 2-user scope, shortened initial term. Currently mid-implementation; Sep 2, 2026 internal task board shows active dev/QA work (task #294).
- Sabre Alloys: NOT yet confirmed as a signed customer. Ron provisioned Claude AI (Company Brain) login credentials to two Sabre contacts (Juan, Tye Webb/COO) on Sep 1, 2026, following the same mid-August proposal push. Deal/payment status unconfirmed in records.
- Three D Metals and a legal-firm prospect (Sarah/virtualilegal.com) are still at pitch/demo stage, not customers.
- The canonical "AskCruz — Product-Market Fit & Product Knowledge Guide" asset (revised Aug 25, 2026) explicitly states 3GM is the only external client as of that date; Sabre's Sep 1 access grant postdates that document and hasn't been reconciled into it.

Answer given: 1 confirmed customer (3GM Steel), 1 likely-imminent-but-unconfirmed (Sabre Alloys). Cited sources: 3GM Steel AskCruz proposal call wiki page, Sabre Alloys Claude AI access wiki page, AskCruz PMF asset, AskCruz Internal Task Board (Sep 2, 2026).
