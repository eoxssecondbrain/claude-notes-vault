---
thread_name: "mailcow-mobile-push-email-app"
user: "ron"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: We use Mailcow for our internal email system and want a phone app that provides push notifications for incoming emails. Which app should we use? Our Mailcow instance runs on our own server. Let me know if you have any questions.

Assistant: Mailcow itself is just IMAP/SMTP under the hood (Dovecot/Postfix), so the app matters less than which sync protocol you point it at. Two real options:

**If you enable SOGo on your mailcow instance (it's bundled, just needs turning on):**
SOGo gives you ActiveSync support. Point the native Mail app (iOS) or Outlook (iOS/Android) at it via Exchange ActiveSync instead of plain IMAP. That's true push — the server notifies the device the moment mail lands, no polling, no battery drain. This is the only way to get real push on iOS; Apple doesn't support IMAP push in its Mail app.

**If you don't want to enable ActiveSync/SOGo, or you're Android-only:**
FairEmail (Android, open source, F-Droid/Play Store) holds a persistent IMAP IDLE connection and delivers near-instant notifications with good battery behavior. It's the best plain-IMAP option, but it's Android only — there's no iOS equivalent that does real push over plain IMAP, since iOS kills background IMAP IDLE connections.

Two things I need to know to give you a final answer instead of two branches:

1. Is SOGo already running on your mailcow instance, or would this be a new addition?
2. iOS, Android, or both across the team?

User: Is there any other app that I can use for iOS for this? I want to download a separate app for this.

Assistant: Yes, but every one of them works the same way: since iOS doesn't let third-party apps hold a background IMAP connection open, Canary Mail, Spark, Edison Mail, and Blue Mail all route your mail through their own cloud servers, which poll or IDLE your Mailcow account on their end and fire an Apple push notification when something arrives. Your login credentials and mail content pass through a third-party company's infrastructure to make that work.

That's worth pausing on given you're self-hosting Mailcow specifically to keep this internal. Options, roughly in order of how much you're giving up:

Canary Mail — solid iOS client, push relay is opt-in (you can disable it and fall back to on-device fetch every ~15 min instead), has a paid tier.

Spark (Readdle) — same relay model, no opt-out for push specifically, free.

Edison Mail — same model, also does inbox analytics on synced mail, would avoid this one for a company account.

None of these are "point at your own server" apps — they're all relay-based. The two ways to get real push without a third party in the middle stay what I said last message: SOGo/ActiveSync on your own mailcow, or accept fetch-interval delay instead of push.

If a separate downloadable app matters more than avoiding the relay, Canary Mail is the least bad of the three — worth confirming their opt-out actually works before rolling it out to the team.
