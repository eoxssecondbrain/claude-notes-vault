---
thread_name: "odoo-tab-title-askcruz-rename"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: [uploaded screenshot: Odoo Settings > Employees page, browser tab reading "New - Odoo"] In the bar above, you will see a new - Odoo written. I'm trying to understand: how can I get rid of it and instead it say new - AskCruz?

Assistant: The "- Odoo" suffix comes from the company name field (`res.company.name`) in this Odoo instance, not from the app or database name.

To change it:

1. Go to Settings > Users & Companies > Companies
2. Open the company record (probably still named "Odoo" or default demo name)
3. Rename it to "AskCruz"
4. Save

The tab title format is "{page/action} - {company name}", so once the company record's name is "AskCruz", every tab will read "New - AskCruz" instead of "New - Odoo" going forward, across the whole instance, not just this page.

If you also want the favicon or browser tab icon changed, that's a separate setting (Settings > General Settings > favicon upload), but that's not what's causing this text.
