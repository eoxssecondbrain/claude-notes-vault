---
thread_name: "ess-sam-stroman-access-issue"
user: "humaira"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

**User:**
[Uploaded image: /mnt/user-data/uploads/1788369502922_image.png]
Image content (Slack/support message screenshot):
"Sam User Access issues
Ryan Capinski • [search icon]
10:47 PM • [flag icon]
Support, Sam Stroman
One of our users Sam Stroman is having some trouble with his EOXS account

Sam had been using the system with no trouble earlier in the day. At one point, perhaps connected, he was using the old version of Microsoft Outlook and decided to start using the new version of Outlook. After that when opening up a new link in EOXS, it prompted him to re sign into his EOXS account which I thouhgt was odd because it had never prompted me to do so. Possibly this is connected to him using the newest version of Mircrosoft Outlook?"

Our client ESS sent this can you please review and tell how can we help them in this ?

**Assistant:**
Reviewed. Client is Eastern States Steel (ESS). Here's what's relevant.

**What's likely happening**

EOXS logins are typically browser-session based, not tied to Outlook itself. When Sam switched from classic Outlook to New Outlook, that switch commonly resets the browser/webview context Outlook uses to open links (New Outlook runs as a separate app with its own embedded browser session, separate cookie store from classic Outlook or the desktop browser). That's the most probable reason a link that used to open straight into EOXS now prompts a fresh login — his old cached EOXS session simply isn't available in the new Outlook's link-handling context. This isn't a bug in EOXS; it's a client-side session change.

**One complication specific to Sam that's worth checking first**

On 2026-08-17, Support issued two separate EOXS login credential sets for Sam, a few minutes apart, because Ryan corrected his email mid-request: first to SamS@EasternStatesSteel.com, then to SStroman@EasternStatesSteel.com. Both got a welcome email with a username and password. If Sam or his browser has the old SamS@ credentials saved/autofilled, that's a second plausible cause: he's being prompted because he's entering (or autofill is entering) the wrong username, not because of an Outlook-related session issue at all. Worth confirming with him which address he's actually signing in with before treating this as a New Outlook problem.

**What to tell the client / next step**

1. Ask Sam to sign in explicitly with SStroman@EasternStatesSteel.com (the address Support confirmed credentials were sent to) rather than relying on saved autofill.
2. If that resolves it, the earlier prompt was the stale/wrong saved credential, not New Outlook.
3. If it still prompts repeatedly even with the right login, that's a session-persistence issue tied to New Outlook's link handling — worth a support ticket so it can be checked on the backend, but there's no indication yet this is an EOXS-side account or access problem.

One unrelated open item on this account: as of 2026-08-28 there's still an unresolved internal question on whether ESS gets billed for a 7th active user now that Sam's been added (Ryan hasn't decided who to remove, Chip was supposed to make the call). Not connected to this access issue, but flagging since it's the same new user and still pending.
