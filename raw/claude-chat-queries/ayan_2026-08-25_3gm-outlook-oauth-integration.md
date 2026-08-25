---
thread_name: "3gm-outlook-oauth-integration"
user: "ayan"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

**User:**
lets do 50ft deep.

**Assistant:**
Auth flow: this part is a close port, not a redesign

Microsoft's shape matches Google's almost exactly. Authorization code flow, and the one thing that used to be Gmail-specific hardening — PKCE — is now something Microsoft recommends for every app type including confidential web clients, not just public/native ones, so nothing changes there between the two providers (PKCE is now recommended for all application types, both public and confidential clients, though the Microsoft identity platform only requires it for single-page apps). A confidential web app still needs a client_secret at the token-exchange step, same as the Gmail flow's GMAIL_OAUTH_WEB_CLIENT_SECRET (a client_secret is required for confidential web apps redeeming an authorization code, since it can be stored securely on the server side, unlike in a native app or SPA).

The refresh-token mechanics map too: you have to explicitly ask for offline_access in the scope list to get a refresh token back at all (only if the offline_access scope was requested does the token response include a refresh_token), and once issued, refresh tokens for a web app don't have a fixed expiry — they're long-lived, same as Google's (refresh tokens for web apps and native apps don't have specified lifetimes and are typically long-lived, though they can be revoked or expire in some cases).

Scope for read-only mail is https://graph.microsoft.com/Mail.Read. Worth knowing: this is a low-impact, self-consentable delegated permission by default — it's not in the same bucket as Mail.ReadWrite, which Microsoft explicitly blocks from end-user consent under its recommended tenant policy and requires an admin to approve (Mail.ReadWrite is considered a high-impact permission and is blocked from end-user consent in the Microsoft-recommended user consent policy, requiring an administrator to grant consent). Since we only need read access, that's the easier tier — plain Mail.Read is available for individual consent, including on personal accounts (The Mail.Read delegated permission is available for consent in personal Microsoft accounts).

App registration: register it multitenant — "Accounts in any organizational directory and personal Microsoft accounts" (Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant) and personal Microsoft accounts, for example Skype or Xbox) — Web platform type, redirect URI https://<domain>/oauth/outlook/callback, and use common as the tenant segment in the authorize/token URLs so any org's user (or a personal outlook.com account) can complete it (the sign-on URL for multi-tenant and personal accounts is https://login.microsoftonline.com/common). This is the direct structural sibling of the Google Cloud "Web application" client requirement in section 4 of your doc — same one-time setup shape, different portal.

One thing I checked for and couldn't confirm either way: Google's flow needs prompt=consent forced on every request, because Google silently skips the consent screen on repeat sign-in and withholds the refresh token if you don't — that's the load-bearing line in section 3 of your doc. I didn't find a documented Microsoft equivalent of that specific footgun; the docs just tie refresh-token issuance to requesting offline_access, with no mention of a silent-skip case. A few community threads describe refresh tokens not coming back, but those trace to missing admin consent on other scopes, not a Google-style silent reauth (the refresh token won't be issued if the overall permission set isn't valid or lacks admin consent for other required permissions) — different root cause. I'm flagging this as unverified rather than claiming it's fine either way. Costs nothing to keep passing prompt=consent defensively and treat a missing refresh_token as a hard error, exactly like oauth_gmail.py already does — so this piece needs zero new design regardless of which way it turns out.

Real-time delivery: this is the actually new part, not a port

Your doc is explicit that Pub/Sub push is a separate mechanism layered on top of the OAuth flow, documented in a different onboarding playbook I don't have in front of me. That matters here: I can tell you precisely how Microsoft's side works, but I can't give you a clean line-by-line diff against Gmail's Pub/Sub implementation, because I haven't seen it. Some of what I'm about to call "new" below may already have a solved analogue on the Gmail side — worth pulling that playbook before locking the build plan.

Microsoft's mechanism is Graph "change notifications" — webhooks, not a pub/sub topic. You POST /subscriptions with the mailbox folder as the resource, and Graph pushes to your endpoint when something changes:

Setup handshake — when you create the subscription, Graph immediately POSTs a validation token to your notification URL, and you must echo it back as plain text within 10 seconds or the subscription never gets created (when a subscription is requested, Microsoft Graph sends a validation token to the notification URL, and the client must respond with a 200 OK, content type text/plain, and the URL-decoded plain text validation token within 10 seconds).

Delivery contract is stricter than anything in the polling-based sweep — you need a 2xx response within 3 seconds or Graph starts retrying, and if your endpoint is slow on more than 10% of responses in a 10-minute window it gets marked "slow" and notifications get delayed 10 minutes; past 15%, they start getting dropped outright (once Microsoft Graph receives a 2xx response within 3 seconds the notification is considered delivered; an endpoint is marked slow once more than 10% of responses exceed that window, and marked drop once more than 15% exceed the 10-second retry timeout). Practical implication: the webhook handler has to be a thin validate-and-enqueue layer, never doing the actual mail fetch inline.

Payload is a reference, not content — by default the notification just tells you a message id changed, not what's in it. The natural design: webhook validates clientState (a shared secret Graph echoes back on every call, your fraud check — the clientState property allows your service to confirm that a change notification originated from Microsoft Graph, since the value is known only to your application and the service), enqueues the message id, returns 200 immediately, and a worker calls the same GET /messages/{id} your fetcher already needs for the scheduled sweep. That reuses gmail_fetcher.py's shape almost exactly — triggered by a queue instead of a timer, same downstream code.

You can skip the alternative — Graph supports pushing the encrypted message body inline (includeResourceData: true), which would avoid the follow-up GET. I'd pass on that for v1: it needs a certificate you generate and rotate, and it cuts the subscription's maximum lifetime from 7 days to 1 day (for Outlook message, event, and contact resources the maximum subscription lifetime is 10,080 minutes, under seven days, but for subscriptions with resource data included that lifetime drops to 1,440 minutes, under one day) — 7x more renewal traffic for a convenience you don't need.

The hard new constraint: subscriptions expire and don't auto-renew, full stop — a renewal request past the resource's ceiling is rejected outright (apps need to renew their subscriptions before the expiration time; otherwise they need to create a new subscription). For mail that ceiling is under 7 days, so you need a scheduled job that PATCHes expirationDateTime forward for every connected mailbox, indefinitely, for as long as the account stays connected. Nothing in oauth_gmail.py's structure has an existing slot for this — it's a genuinely new recurring job, separate from any token-refresh logic.

One place Microsoft is arguably ahead of what your doc describes for Gmail: register a lifecycleNotificationUrl alongside the notification URL, and Graph proactively pushes you a subscriptionRemoved event if a tenant admin revokes the app's access, plus advance warnings before the access token or subscription itself expires (when you subscribe to lifecycle notifications, Microsoft Graph alerts you when the access token is about to expire, when a subscription is about to expire, and when a tenant administrator revokes your app's permissions). Your Gmail doc doesn't describe an active signal for "client revoked access" — worth checking whether Pub/Sub already handles that or whether Gmail just discovers it on the next failed fetch. Genuine open question, not a claim either way.

Expected latency for a new-mail notification: Microsoft's own numbers put it under a minute on average, 3 minutes worst case (for the message resource, average latency is less than 1 minute and maximum latency is 3 minutes) — real-time in the sense you mean it, not instant, and very likely the same ballpark Pub/Sub already delivers.

Mapped onto the 4-file/2-table pattern

Direct ports, same shape, new provider:
oauth_outlook.py — link generation, /oauth/outlook/connect, /oauth/outlook/callback, token storage. Structurally identical to oauth_gmail.py.
outlook_fetcher.py — reads oauth_accounts, refreshes the access token, calls the Graph mail endpoint. Same job as gmail_fetcher.py, different HTTP calls.
oauth_accounts / oauth_connect_tokens — no schema change needed. source_type is already a column, not hardcoded — 'outlook' is a new value, not a new table.

Genuinely new, no existing slot:
A webhook route (/webhooks/outlook/notifications), separate from the OAuth callback route — thin, ack-and-queue only.
A subscription manager: creates the Graph subscription right after the OAuth callback completes (chains onto the existing "mailbox connected" moment), plus a renewal job running comfortably inside the 7-day window — daily is safe.
A small new table or columns tracking subscription id, expiry, and clientState per mailbox.
New one-time setup: multitenant Entra app registration, Web platform, redirect URI on the app itself, new .env values OUTLOOK_OAUTH_CLIENT_ID / OUTLOOK_OAUTH_CLIENT_SECRET, reusing the existing OAUTH_REDIRECT_BASE_URL.

Risks, ranked by how much they could derail the 6pm call

1. Tenant consent policy — the actual equivalent of the Google Workspace admin block. Microsoft tenants commonly run one of three postures: open self-consent, "verified publishers only + low-impact permissions," or "no user consent at all, admin required for everything" (Do not allow user consent requires administrator approval for all consent requests; Allow user consent for apps from verified publishers, for selected permissions lets users consent only when the permission is low-impact and the app is from a verified publisher or the org's own tenant). Mail.Read isn't on Microsoft's current default blocked list — that list currently covers four unrelated SharePoint/OneDrive-scale permissions (the recommended policy blocks user consent to just four high-impact permissions covering OneDrive and SharePoint access at scale; all other permissions behave as they did under the legacy policy) — so on a default-configured tenant this should self-serve. But we don't know 3GM's actual policy, and if it's locked down, the invite link fails exactly like the Workspace case did. Same mitigation as your doc already recommends for Workspace: ask, and get an admin contact ready before sending the link, not after it fails.

2. Whether 3GM is actually on Microsoft 365 / Exchange Online at all. Custom-domain mail (@3gmsteel.com) accessed via Outlook strongly suggests it, but that's an assumption — the whole admin-consent and subscription story only applies if there's a real Entra tenant behind their mailboxes.

3. I don't have the Gmail-side Pub/Sub playbook, so I can't confirm which pieces above are genuinely new versus already-solved-once-for-Gmail. Worth pulling before the build plan is final.

4. Refresh-token silent-skip behavior on Microsoft's side is unverified, not confirmed safe — see above. Free to defend against either way.

5. Scale is not a risk at 3GM's size. Mail reads allow roughly 10,000 requests per 10 minutes per app per mailbox (Outlook calendar and mail APIs are typically limited to a threshold on the order of 10,000 requests every 10 minutes per app per mailbox), subscription writes are capped at 500 per 20 seconds per app per tenant (for the subscription resource, write operations are limited to 500 requests per 20 seconds per app per tenant) — a 2-user account, per the accepted proposal's reduced scope, won't come close to either ceiling.

For the 6pm call: two questions worth bringing — are Jessica, Leslie, and Travis on Microsoft 365, and who's the IT/admin contact if so. Same discovery question your doc already recommends for Workspace clients, aimed at Microsoft's version of the same problem.

Build order I'd propose: port oauth_outlook.py and outlook_fetcher.py first — low-risk, well-documented, no open design questions — so one-click-consent-to-scheduled-fetch works end to end. Layer the webhook subscription and renewal job on second, since that's the genuinely new engineering and it benefits from the fetch path already existing to call into.
