---
thread_name: "3gm-entra-admin-consent-fix"
user: "ron"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: Ron
Context: 3GM Steel AskCruz implementation. Admin at 3GM granted access to allow sending users a link to extract their email via Microsoft Entra, but a user (travis@3gmsteel.com) hit a "Need admin approval" error for the app "Cruz - 3GM Outlook Ingestion" (unverified). Ron asked what needs to be done on the admin side to get access to read the users' emails.

Assistant response: Explained that approving one user's consent prompt is not the same as tenant-wide admin consent. Provided step-by-step fix via step_card_display_v0:
1. Open the app in Enterprise Applications (Entra admin center > Identity > Applications > Enterprise applications > "Cruz - 3GM Outlook Ingestion")
2. Grant admin consent at the tenant level (Permissions tab > "Grant admin consent for 3GM Steel") - this is the actual fix
3. Verify permissions list shows all as "Granted" (Mail.Read, Mail.ReadWrite, offline_access, User.Read)
4. Check if "Assignment required?" is Yes on Properties page; if so, add travis@3gmsteel.com under Users and groups
5. Check publisher/consent restriction policies (app is unverified) under Consent and permissions > User consent settings
6. Have Travis retry the sign-in link once permissions show Granted
