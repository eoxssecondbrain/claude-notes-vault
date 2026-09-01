---
thread_name: "askcruz-customer-count"
user: "ron"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: How many customers are there in AskCruz.

Assistant: 2 customer accounts show up on the AskCruz Odoo project board:

- Customer 1 - EOXS
- Customer 2 - 3GM

Caveat: the sale/purchase apps aren't installed in this instance, so there's no billing-based customer count — this is project-tracking labeling, not a CRM or sales record. res_partner.customer_rank exists as a field but isn't meaningfully populated here for the same reason.

Of these two, EOXS itself is internal usage, not a paying account. So going by paying customers specifically, that's 1 external customer (3GM Steel) tracked so far — consistent with 3GM being the first paying AskCruz customer.
