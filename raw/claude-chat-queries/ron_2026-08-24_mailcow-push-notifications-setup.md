---
thread_name: "mailcow-push-notifications-setup"
user: "ron"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

User: At AskCruz we use Mailcow as our mailing server. how can I have this installed on my phone where I can get push notifications whenever I get an email?

Assistant: This question doesn't clearly match any of the account-strategist or email-drafting skills — it's a general infra/product question, not an EOXS client matter, so I'm just answering it directly.

Mailcow has no dedicated mobile app. Push depends on how you connect your phone's mail client to it. Two real paths:

1. IMAP IDLE (native Apple Mail, iOS only)
Dovecot in Mailcow supports IMAP IDLE, so the stock iOS Mail app gets near-instant push over plain IMAP. Add the account in Settings > Mail > Accounts > Add Account > Other, using your Mailcow hostname for IMAP/SMTP. Mailcow also serves a ready-made config profile: visit https://{your-mailcow-hostname}/mobileconfig.php on the phone and install the profile it generates — sets IMAP/SMTP/SSL correctly without manual entry.

2. Exchange ActiveSync via SOGo (true push, iOS and Android)
Mailcow bundles SOGo, and SOGo supports ActiveSync. Configuring the phone's mail account as "Exchange" instead of IMAP hits SOGo's ActiveSync endpoint and gets you real push plus calendar/contacts sync.
- iOS: Settings > Mail > Add Account > Exchange, server = your Mailcow hostname, username = full mailbox address.
- Android: the stock Gmail/mail app doesn't handle third-party ActiveSync well — use Outlook for Android (supports ActiveSync properly) or a third-party IMAP client that holds a persistent IDLE connection (e.g. FairEmail) if you'd rather stay on plain IMAP.

One caveat worth knowing: Mailcow's community forum has recurring reports of SOGo's ActiveSync being flaky specifically for contacts/calendar sync on Android (truncated names, duplicate phone numbers) — mail push itself is generally fine, it's the groupware sync that's shakier. If you only care about mail notifications and not calendar/contacts, plain IMAP IDLE on iOS or Outlook-for-Android is the more reliable route; ActiveSync is worth it mainly if you also want calendar/contacts synced.
