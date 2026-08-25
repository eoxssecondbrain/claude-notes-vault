---
thread_name: "3gm-outlook-oauth-integration"
user: "ayan"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

**User:**
I'd flagged the 7-day subscription renewal as a genuinely new burden Gmail doesn't have. That's wrong — I checked, and Gmail's own watch() call expires on the same 7-day ceiling and also needs a proactive renewal job before then, with no auto-renew either. So that piece isn't new engineering, it's the same problem you've already solved once, just against a different endpoint.

We cant have 7days window for renewal, doesnt make sense. It has to be a one time thing.

Account label convention for Outlook mailboxes — proposing the same shape as Gmail's, e.g. 3gm_owner_outlook.

Expand on this point

Migration file numbering — the Gmail schema stops at 028_oauth_pkce_verifier.sql, so new ones presumably start at 029, but that assumes nothing else has landed since; Claude Code should check the actual migrations folder rather than assume.

Expand on this as well

**Assistant:**
Fair pushback, but worth being precise about why: neither Microsoft nor Google actually sell a "set once, never renew" push subscription. It isn't a gap in this design — it's how both platforms work, on purpose. A webhook subscription that never expired would mean an app could keep getting live mail data forever with no periodic proof it's still authorized, still running, still has a live endpoint. Both vendors deliberately force a renewal heartbeat instead of offering a permanent option. There's no setting on either side that buys "one-time."

So "no renewal, ever" and "push notifications" can't both be true on these platforms. But there's a real way to get the outcome you actually want — no subscription lifecycle to babysit — without giving up much on speed.

Microsoft Graph has a separate, pull-based mechanism called delta query, built for exactly this. No subscription object, no /subscriptions call, no expiration clock, no webhook route, no validation handshake, no clientState. You call GET /me/mailFolders('inbox')/messages/delta on a schedule you control, and each response hands you a cursor (@odata.deltaLink) to replay next time — Graph returns only what changed since then (save and use the @odata.deltaLink URL to synchronize the same folder in the next round). There's no calendar-based expiry the way a subscription has — the cursor only goes stale if you stop polling for an extended stretch (delta cursors are not permanent; if a folder sits unsynced too long, the server discards the tracking state, and the required recovery is to discard the stored deltaLink and start a fresh delta cycle). If you're the one polling on a fixed interval for your own reasons, that staleness case never comes up.

What that buys you: poll every 60 seconds and mail shows up within a minute, with nothing to ever renew. Compare that to Microsoft's own published latency for the webhook route — under a minute average, up to 3 minutes worst case. A 60-second poll isn't meaningfully slower than push in practice; it just trades a small amount of polling overhead for zero subscription-lifecycle engineering.

And it turns out Gmail has the identical fork already built into its own docs — Google explicitly documents a pure poll-based alternative to watch()/Pub/Sub, using history.list on a timer with no watch() call at all (for notifications to user-owned devices, the poll-based Synchronize clients with Gmail API guide is still the recommended approach to retrieve updates). So this isn't a Microsoft-only fallback — both platforms offer the same trade: push (fast, but needs a renewal heartbeat forever) versus poll-with-a-cursor (slightly less instant, but genuinely one-time to set up and forget).

My recommendation: build the "real-time" half on delta-query polling instead of Graph subscriptions and webhooks. That removes the webhook route, the subscription table, the renewal job, and the lifecycle-notification handling from the build entirely — what's left is a timed GET call with a saved cursor, architecturally close to the existing scheduled sweep, just running every 60 seconds instead of on a longer interval. Want me to rewrite Part 2 of the build prompt around that instead of the subscription/webhook design?

Account label convention, expanded

account_label is the unique key in oauth_accounts — it's what shows up in the CLI invite command, in logs, in the confirmation page copy ("<name>'s Outlook is connected"), and in any audit trail. It isn't part of the URL the client clicks (that's a random opaque token), so it doesn't need to be URL-safe, but it does need to be globally unique across the whole table — not just unique per client — since the column has a single UNIQUE constraint with no client-scoping.

The Gmail doc's own example, 3gm_owner_gmail, works for a single shared inbox. But the accepted AskCruz proposal for 3GM is explicitly a reduced 2-user scope, which means two separate mailboxes get connected, not one generic "owner" inbox — so a single 3gm_owner_outlook label would be wrong for this client specifically. Better shape: <client_slug>_<person>_<provider> — so, using the two of Jessica Worley, Leslie Countryman, and Travis Lane who end up in scope, something like 3gm_travis_outlook and 3gm_jessica_outlook. The provider suffix mirrors Gmail's own pattern of naming after the protocol (_gmail, presumably _zoho), not the vendor (_google) — so _outlook, not _microsoft365 or _m365. That also keeps the door open cleanly if the same person ever gets a second mailbox on a different provider later — 3gm_travis_outlook and 3gm_travis_gmail wouldn't collide.

Migration numbering, expanded

The concern isn't cosmetic. If a migration runner applies files in strict numeric order and two people each pick "029" for unrelated changes, you get either a silent collision (one file gets skipped or overwritten depending on the tool) or a hard failure at deploy time. The 028 ceiling I can see comes from a snapshot doc, not a live view of the repo — and this is clearly an actively developed codebase (task 309 itself was opened yesterday), so there's a real chance something has landed at 029 or beyond since that doc was written, from a completely unrelated piece of work.

There's a second wrinkle beyond "check the folder": some migration tools track applied migrations in a database table (commonly something like schema_migrations) rather than relying purely on filenames on disk. If that's how this repo works, a number could look free in the directory listing while actually being reserved or mid-flight on another branch — checking only the filesystem wouldn't catch that. So the instruction to Claude Code should be: inspect the actual migrations directory and, if the repo uses a migration-tracking table, check that too, and take the next number confirmed free by both — never hardcode a specific number into the prompt itself, since by the time this prompt gets executed the true next-free number may have moved.
