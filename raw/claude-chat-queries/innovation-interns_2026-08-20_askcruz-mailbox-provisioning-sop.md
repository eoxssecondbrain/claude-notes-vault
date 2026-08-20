---
thread_name: "askcruz-mailbox-provisioning-sop"
user: "innovation_interns"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

USER: Ayan has given us a task to make sop and we need to report to him in an hour with the sop so list out the basic criteria and requirements and also keep in mind the sop is to be created for askcruz

ASSISTANT: AskCruz shows up across several distinct threads — board scrum reporting, mailbox/IT provisioning, intern onboarding, and the external sales pitch (Company Brain product to clients like 3GM, Sabre Alloys). "SOP for AskCruz" doesn't point to one of these on its own, and I'm not going to guess with an hour on the clock.

What is the SOP actually for — pick one, or tell me if it's something else:

[Asked via ask_user_input_v0: "What is this AskCruz SOP for?" Options: "Mailbox/account provisioning for new hires (IT process)", "Board/scrum reporting process (internal team engagement)", "Sales pitch/demo process (selling AskCruz to clients like 3GM, Sabre)", "Something else — I'll specify"]

USER: Mailbox/account provisioning for new hires (IT process)

ASSISTANT: AskCruz mailbox provisioning is not currently a documented SOP anywhere in the system — it is a repeated ad hoc process run by Isha Bisht. Here is what the actual practice looks like right now, and what the SOP needs to lock down.

Current process, as actually run (from provisioning emails, Aug 11–18)

1. Trigger: new hire or intern needs an askcruz.com mailbox — either a batch cohort (43 people, Aug 11) or a one-off add (e.g. Kriti Jain, Aug 18).
2. Isha creates the mailbox on the mailcow.askcruz.com portal, format firstname@askcruz.com.
3. Credentials sent by email to the person's personal address (Gmail or institutional), with an instruction to log in and change the password immediately.
4. Recipient asked to confirm successful login, sometimes by a deadline (6 PM same day for the batch).
5. No tracking mechanism observed — for the Aug 18 Kriti case, no confirmation of login is logged anywhere.

Gaps the current process has, that a real SOP needs to close

1. Shared/default passwords sent in plaintext over email, reused across many recipients in the same batch. Same pattern already flagged separately for the Cattr rollout — this is a repeat, not a one-off.
2. No pre-send verification of the login ID — the Kriti case shows a typo (kriti@ vs kritij@) caught only after the wrong credentials were already sent.
3. No confirmation tracking — "please confirm you logged in" has no follow-up mechanism if someone doesn't reply.
4. No defined offboarding/deactivation step anywhere in what's captured — only provisioning is documented.
5. Ownership is currently informal (Isha does it on request). As of Aug 18, Ayan was assigned broader ownership of AskCruz access rollout to the functional team, with Rajat noting he already knows a specific gap Ayan is likely to miss on his own — worth clarifying with Ayan directly whether this SOP is meant to also close that specific gap, since it isn't stated anywhere I can see.

Minimum sections the SOP itself should have

1. Trigger and request intake — who can request a mailbox, what info is required (name, personal email for delivery, role/team)
2. Provisioning steps — portal, naming convention, who executes it
3. Credential delivery — this is the piece that needs to change: unique password per person, not a shared one; verify the login ID before sending
4. Confirmation and tracking — a log of requested / sent / confirmed, not email-thread-only tracking
5. Access scope — what askcruz.com mailbox access grants vs. eoxs.com/eoxsteam.com accounts, and how it relates to individual Claude account access (separate but related rollout happening same week)
6. Offboarding — deactivation when someone leaves, currently undocumented anywhere
7. Owner of record — name a single owner (currently Isha executes, Ayan now owns the broader access rollout — SOP should state which)

Given the hour deadline, I'd flag point 4 (ownership) to Ayan directly rather than guess — the SOP will read differently depending on whether it's meant to just document Isha's current mailbox process or formalize the broader access rollout Ayan now owns.
