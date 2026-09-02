---
thread_name: "ppc-manual-refresh-investigation"
user: "nizamuddin"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

User:
"Investigate Manual Refresh Issue
Project	Build Team
Customer	PPC Speciality Metals.
Associated Customers	
Ownership	Dev Team
Assigned To	
Planned Hours	00:00
Progress	
0%
  
Deadline	
Tags	
Priority	P4
Billable	No
Developer Incentive	0.00
QA Incentive	0.00
Dev State	Developing
QA State	QA
 
Description
Timesheets
Extra Info
Training Information
Users are experiencing situations where they need to manually refresh the system before they can proceed with certain actions. This is happening in multiple areas.
Please investigate why manual refresh is required and check if this behavior can be resolved.
One of the main screens where we have seen this happen is the packing list screen, where whenever a packing list is created, there are some tags which are not visible there. When we refresh that screen or that sale order, there are situations where user A is not able to see that tag, but user B is able to see that tag and add that tag on the packing list. Need to investigate why this is happening, and this happens with a couple of customers. "

See, the above context I pasted is my task . I need to know is this task can be done or not ?  I need to know is this fix possible on odoo13 or is this core behavior can't fix it??

Assistant:
This ticket bundles two different problems — one is core Odoo behavior, one isn't.

1. "Need to manually refresh to see changes made by another user" — this is core Odoo behavior on v13, not a bug. The Odoo web client doesn't push live updates to other open sessions for ordinary business records (sale orders, packing lists, tags, etc.). Only Discuss/chatter uses the longpolling bus for real-time push. When user B changes something, it's in the database immediately, but user A's browser is still holding the snapshot it loaded when the page opened — it needs a refresh, a reopen, or some UI action that forces a re-read to see it. That's how the client has behaved since early versions, including v13. It's technically possible to build live-refresh onto a specific screen using the bus (v13 has bus.bus), but that's a real feature build — instrument that view to listen for a notification and trigger a re-fetch — not a small patch, and it only covers the screens you build it for.

2. User A genuinely can't see a tag that user B can see and use — inconsistently, across a couple of customers. This is not normal "stale view" behavior; it's a difference in what data each user is being served, not just timing. That points to one of:
- a record rule / access rule / domain difference between the two users on whatever tag model this is (permissions, company, team, warehouse scoping)
- a caching or field-invalidation bug in the custom code that relates the tag onto the packing list (e.g. a related/computed field missing correct @api.depends, or a server-side cache not invalidated on write)
- a widget that only fetches a filtered subset for one user

That is a real bug, and it's fixable. I can't tell you which of the three it is from here — I don't have access to the actual module code or the two users' role/group config through what I can query, so this needs a developer to compare: the tag field's definition and dependency chain, the two users' access rights on that tag model, and ideally the actual network responses each user's browser received for the same record, side by side.

One thing worth flagging: this doesn't look isolated to PPC. In EOXS's own history I found a "cache workaround offered, fix in QA" logged against PPC in the Dec 2025 post-launch window, a similar "refresh and check, let us know if visible" pattern at Discount Pipe & Steel, and 3GM Steel had a recurring case escalated to DevOps for session-level cache review. If the same shape keeps showing up across separate client deployments, that suggests a shared root cause in EOXS's own custom code or session handling rather than something specific to PPC's data — worth investigating once at the source instead of per-ticket.

Also: I checked for an existing task/ticket matching this exact "Investigate Manual Refresh Issue" item and didn't find one logged in what I can query — this looks like a new Build Team item not yet reflected there, so there's no prior EOXS diagnosis to build on for this specific ticket.

User:
explain you the exact scenario what has happened.when a client opened our application in two desktops, and in one desktop, he opened the inventory and seeing the tags. In another desktop, he entered the new tag to the inventory he added. And his concern is the tag is isn't visible in the desktop which is opened before to see the control tags.

Assistant:
That scenario clears something up: it's the same client (likely same user or at least same account/permissions) in two separate browser sessions, not two different users with different access. That rules out the record-rule/permission-difference explanation from before. What's left is simpler and points squarely at core Odoo client behavior.

What's actually happening

Desktop 1 opens the inventory screen. At that moment, the browser loads the current state of the "control tags" field/list into its own in-memory session — that's a one-time snapshot, not a live connection to the database.

Desktop 2 creates a new tag. That write goes straight into the database and is real immediately — any fresh query would see it.

Desktop 1's browser tab has no idea anything changed. Odoo's v13 web client doesn't maintain a live connection to the database for ordinary business data — it isn't watching for changes made elsewhere. The only thing in Odoo that works that way is the Discuss/chatter bus (used for things like instant notifications and chat), and only because that specific feature was built to subscribe to it. A regular field like a tag list on an inventory record was never wired into that channel, so nothing tells desktop 1 to go re-fetch. It will keep showing what it loaded until something forces a new read — a manual refresh, closing and reopening the record, or (depending on the widget) typing into the tag field to trigger a fresh server search.

Is this core, unfixable behavior?

Not unfixable — but it is core behavior, meaning "it will keep doing this by default" rather than "it's a bug sitting in some function waiting to be patched." To actually make desktop 1 pick up a tag created on desktop 2 without a manual refresh, you'd need to build one of these:

1. Real push refresh: on tag creation, broadcast a message over Odoo's bus.bus (the same longpolling/websocket mechanism chatter uses) on a channel the tag widget subscribes to; the client listens for it and re-fetches that field's data automatically. This is a genuine feature build — server-side broadcast on create, client-side JS listener wired into that specific widget — not a small patch, but it is buildable on v13, since bus.bus has existed since well before v13.
2. Cheaper middle ground: keep the manual-refresh requirement, but make it less confusing — have the tag-creation event push a lightweight bus notification that just pops a "New tag added — refresh to see it" banner on other open sessions, rather than forcing them to guess. Much less work than full live sync, and removes the "why can't I see it and nobody told me" confusion.
3. Minimum check worth doing regardless of which path you pick: confirm whether the tag input widget itself does a fresh server-side name_search every time the user types/reopens it, versus using a list it cached once at initial page load. If it's already re-querying live, then simply clicking into the tag field again (without a full page reload) should already surface the new tag — worth verifying before assuming a full refresh is required, since that changes what you tell the client and how much dev work this actually needs.

So: this specific complaint is core client behavior, not a defect, and a full fix means building real-time refresh for that one field/screen rather than debugging existing code. Given P4 priority, I'd verify point 3 first — cheap to check, and it may turn out users just need to reopen the field rather than reload the whole page, which changes the scope of this ticket substantially.
