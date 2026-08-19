---
thread_name: "dps-change-documents"
user: "humaira"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

## User (turn 1)
[Attached: DPS_Change_Document_v2026.06.01.pdf, DPS_Change_Document_Task_433_1.pdf]

You know we have a client named "Discount Pipe and Steel". They told us their requirements and we created tasks for their requirements and completed task, Now we'll send them a change document, I attached 2 change documents for your reference. We have to replicate these change document. I'll provide you all the information. Please review and let me know if you understood everything?

## Assistant (turn 1)
I've reviewed both documents. Here's what I understood:

Structure and purpose — this is a standard EOXS "Production Change Document" template used to formally hand a release scope to a client (DPS) before pushing to production. Both samples follow the same skeleton:

1. Header table — prepared date, client, release version, task(s) included
2. Purpose statement
3. Release Summary table — previous state vs. new state, per task, plus a client/QA status callout
4. Controlled Release Validation Process — explains sandbox-first deployment, that only approved tasks are bundled, no unrelated changes
5. Per-task sections — business reason, previous production code (what already existed), release code changes (with file paths and sometimes code snippets), functional result, QA evidence table, DPS validation table, impact mapping
6. Previous Code vs. Release Code summary table (recap across all tasks)
7. Production Approval, Implementation, and Cutover Monitoring — DPS review requirement, validation readout, deployment process, monitoring plan
8. Rollback Plan — triggers, decision owner, rollback action, data review
9. Sign-Off table — roles (Release Owner, Lead Developer, QA Owner, DPS Approver, Deployment Executor, Rollback Owner, DPS Production Approval status)

Difference between the two samples: the v2026.06.01 doc (Task #336 + #386) is a fully closed-out release — both tasks tested by client and DPS-validated, ready to sign off. The Task #433 doc is a mid-process version — EOXS QA is done (including a very detailed test-case execution log broken out by tester and category), but DPS sandbox validation is "pending," so several fields say "not yet performed" and the deployment version/date are marked TBD. It also adds a "Testing Process and Dependencies" section and a "Short Client Summary" at the end that #336/#386 doesn't have.

So to replicate this format for a new task, I'll need from you: the task number/title, business reason, previous production behavior, what changed (file paths + code changes if available), QA scope/coverage/outcome and who ran it, DPS validation status (done or pending, by whom), rollback triggers specific to that task, and the release version/target date.

What task(s) are we building the next change document for, and do you have the equivalent details (dev notes, QA summary, file changes) to feed me, or should I pull them from the implementation task record in our system?

## User (turn 2)
[Attached 6 screenshots of Odoo project task records: task id=364 "Scanned Tags Create Incorrect SO Line on Packing Slip", task id=384 "Bug - Scan Control Tag Field in create Transfer Screen Not Working", task id=357 "Reservation Function", task id=383 "Reservation Not Auto Reserving Correctly", plus a second screenshot of 364 and 384 again]
[Attached: DPS_Production_Change_Document.docx.pdf — a partially completed change document covering tasks #384 and #364]

we need to create change documents for four tasks. The Task ID for each task is highlighted in blue in the URL. Two of the four tasks are related to the Reservation functionality. Although these are separate tasks, they cover one functionality, so the QA should not be documented separately for each task. A single QA section should cover both Reservation tasks, including all the test scenarios that will be provided. The Control Tag task already has a partially completed change document attached, so that existing document should be reviewed and completed rather than creating a new document from scratch. Based on the screenshots, task details, existing change document, and Reservation test scenarios provided, we need to prepare the change documentation for all four tasks in a clear and consistent format.

Reservation Functionality QA
Reservation Creation
Confirm one SO with auto reserve. Expected: matching tag reserves immediately.
Confirm one SO with manual reserve. Expected: selected tag reserves exactly the entered pieces.
Confirm SO with no manual tag selected. Expected: blocked unless user has reservation override.
Confirm SO with manual reserved pieces greater than tag available_qty. Expected: blocked.
Confirm SO where auto reserve does not have enough available pieces. Expected: blocked for normal user; override user can proceed only according to override rules.
Confirm SO without freight line after freight warning is handled. Expected: reservation still gets created. Reservation should not depend on freight.
Confirm SO with multiple stock lines. Expected: each line reserves independently.
Confirm SO with service/buyout/routed line. Expected: no unnecessary material reservation.
Auto Reserve Matching
Same product, same grade, same warehouse, same size. Expected: tag can be reserved.
Same product but wrong grade. Expected: tag cannot be auto-reserved.
Same product/grade but wrong warehouse. Expected: tag cannot be auto-reserved.
Same product/grade/warehouse but wrong length/cut specs. Expected: tag cannot be auto-reserved.
Matching tag has available_qty = 0. Expected: tag is ignored.
Required quantity is split across multiple matching tags. Expected: reservation splits correctly and total reserved equals required pieces.
Manual Reserve
User manually selects a valid tag from same product/warehouse. Expected: reservation succeeds.
User manually selects oversized/different grade material intentionally. Expected: allowed on original manual reservation if product and warehouse rules allow it.
Manually selected tag later gets displaced by another delivery. Expected: replacement follows the original tag's actual specs, not the sale order line specs.
Manual replacement needs multiple identical tags to fulfill pieces. Expected: allowed to split across multiple matching replacement tags.
Manual replacement has only wrong warehouse/wrong product/wrong specs available. Expected: blocked unless delivery override is used.
Delivery Reshuffle
SO1 reserves Tag A. SO2 reserves Tag B. Deliver Tag B on SO1. Expected: SO2 reservation moves from Tag B to Tag A or another identical available tag.
SO1/SO2/SO3/SO4 all reserve identical tags. Deliver SO3's tag on SO1. Expected: reshuffle works no matter how many orders exist.
Delivery uses a tag already reserved for the same sale order. Expected: no reshuffle.
Delivery uses an unreserved tag. Expected: no reshuffle.
Delivery tag is changed and saved, but the tag does not affect another reservation. Expected: no chatter, no reservation movement.
Delivery tag is changed to a tag reserved for another confirmed SO and saved. Expected: reshuffle happens on save, before validation.
Delivery is validated without save or after another user changed reservations. Expected: validation checks again and blocks/reshuffles if needed.
Partial delivery uses part of a tag reserved for another SO. Expected: only the correct remaining reservation should stay protected; no negative availability.
Delivery uses tag reserved for an expired unpaid/cancelled/invoiced order. Expected: no reshuffle if that reservation is no longer active or has zero pieces.
Replacement Not Found
Normal user delivers a tag reserved for another SO and no replacement exists. Expected: popup blocks the save/validation.
Popup message should show useful details. Expected: displaced tag, original SO, original line, missing pieces, and why user is blocked.
Manager with Reservation Delivery Override repeats same test. Expected: allowed, but reservation is zeroed/marked short and chatter note is posted.
Override should not silently hide the issue. Expected: affected SO/control tag/picking clearly show what happened.
Lifecycle
Cancel confirmed SO with reservations. Expected: reservation rows remain, but reserved pieces become zero.
Expired unpaid SO cleanup runs. Expected: reserved pieces become zero, not deleted.
Expired paid SO. Expected: reservation stays.
Fully invoiced SO. Expected: reservation no longer counts against available quantity.
Partially delivered SO. Expected: remaining undelivered pieces stay reserved.
Backorder/second delivery. Expected: reservation remains correct until remaining pieces are delivered/invoiced.
Data Integrity / Stress
Two users confirm orders for the same available tag at the same time. Expected: no double reservation.
Two users save deliveries using the same reserved tag at the same time. Expected: one clean result, no negative availability.
User clicks confirm twice or refreshes during confirmation. Expected: no duplicate reservation rows.
Change confirmed SO line quantity/specs after reservation. Expected: either blocked or reservation is corrected. This is a very important edge case.
Change reserve mode from manual to auto after confirmation. Expected: no duplicate or stale reservations.
Delete/edit manual reserve rows after confirmation. Expected: actual reserved quantity should not become inconsistent.
Existing bad data where a tag already has negative available quantity. Expected: system should not make it worse; ideally it should warn or require correction.

All the Above scenarios passed the QA

## Assistant (turn 2)
A few things I need pinned down before drafting, since the reservation tasks need info I don't have yet.

[Asked AskUserQuestion with 3 questions: (1) one combined document vs. two separate documents — user chose "One combined document"; (2) release version/date — keep v2026.07.01 vs new version — user chose "New version number"; (3) QA Owner/DPS Validator pattern for reservation tasks — user chose "Same pattern as other tasks" i.e. Aryan Bakshi / Zana Williams]

Good — one combined document, QA/validator pattern consistent with the other tasks (Aryan Bakshi / Zana Williams). Two more things I still need before I can build this correctly:

[Asked AskUserQuestion with 2 more questions: (1) exact version string — options v2026.08.01 or user-provided — user did not directly answer this one; (2) whether to include file paths/code for reservation tasks or leave functional-only — user responded outside the option list]

## User (turn 3, in response to clarifying questions)
Leave code part empty, We'll send the document to developer and he'll fill the code part

## Assistant (turn 3)
[Proceeded with v2026.08.01 as the release version (no objection raised), read the docx skill, then built a combined 4-task Production Change Document as a .docx file covering:
- Task #384 - Bug - Scan Control Tag Field in Create Transfer Screen Not Working (reused content from the existing partial docx: business reason, previous production code, release code changes with representative code excerpt, functional result, QA evidence by Prashant, DPS validation by Zana Williams dated 2026-07-01, impact mapping)
- Task #364 - Scanned Tags Create Incorrect SO Line on Packing Slip (reused content from the existing partial docx: business reason, previous production code, release code changes with representative code excerpt, functional result, two-round QA evidence by Hashir Saleem and Prashant, DPS validation by Zana Williams dated 2026-07-01, impact mapping)
- Task #357 (Reservation Function) and Task #383 (Reservation Not Auto Reserving Correctly) combined into one section: business reason drawn from task #383's description (no location selection, no intelligence in reservation, negative quantity creation) and task #357's thin "Reference other Reservation Item" description; Release Code Changes section explicitly left as a placeholder ("[Pending - to be completed by Developer/Engineering]") per the user's instruction; Functional Result summarizing validated behavior; a single combined QA Evidence section (6.5) with all 44 user-provided test scenarios grouped into 7 category tables (Reservation Creation, Auto Reserve Matching, Manual Reserve, Delivery Reshuffle, Replacement Not Found, Lifecycle, Data Integrity/Stress), QA Owner Aryan Bakshi, all scenarios marked Pass; DPS Validation originally marked "Not yet performed" / Task Stage "DPS Sandbox Review" (matching the screenshots, which showed both reservation tasks still sitting in DPS Sandbox Review while the control-tag tasks were already at "Can be moved to live")
- Section 7: Previous Code vs Release Code summary table across all 4 areas plus 3 reservation-specific rows noting code detail is pending developer completion
- Section 8: Production Approval, Implementation, and Cutover Monitoring, updated to include reservation-specific monitoring areas
- Section 9: Rollback Plan with added reservation-specific rollback triggers (no double reservation, no negative availability, reshuffle correctness, override not hiding issues)
- Section 10: Sign-Off, listing EOXS Release Owner Ron, EOXS Lead Developer Dhrup, Assigned Developer Hashir Saleem (#384, #364) / Dhrup (#357, #383), EOXS QA Owner Prashant/Hashir Saleem/Aryan Bakshi, DPS/Client Approver Zana Williams (validation pending for #357, #383), Deployment Executor Talal, Rollback Decision Owner Ron, DPS Production Approval pending

Generated the .docx with docx-js (US Letter, navy/light-blue table styling matching the existing template), rendered it to PDF and reviewed page images to verify formatting, then delivered the file to the user via SendUserFile as DPS_Production_Change_Document_v2026.08.01.docx with the caption "Combined 4-task change document — matches the existing template format."

I also gave a text summary flagging two open items: Section 6.3 (Reservation Release Code Changes) left as a placeholder for the developer to fill in, and that Tasks #357/#383 showed DPS validation as "not yet performed" per the screenshots. Noted the release version v2026.08.01 was a default pending confirmation.

## User (turn 4)
I want to make one change. Uh, DPS already approved the changes. Uh, we gave them, uh, sandbox access, and they reviewed it, and they passed that everything is working fine. We can go to go live.

## Assistant (turn 4)
[Asked one AskUserQuestion: who validated the Reservation tasks and when, and whether there's a confirmation quote — user chose "Zana Williams, today's date, generic confirmation"]

[Updated the .docx via the build script:
- Section 2 Client Status bullet: changed from "DPS-side validation for Tasks #357 and #383 has not yet been performed..." to "DPS-side validation for Tasks #357 and #383 was completed by Zana Williams on 2026-08-19. DPS was given sandbox access, reviewed the Reservation functionality, and confirmed everything is working fine; both tasks are approved to move to live."
- Section 6.5 DPS Validation block for the Reservation tasks: updated Validator (Zana Williams), added Date (2026-08-19), Confirmation ("Confirmed working in sandbox, ready to move to live."), Task Stage changed to "DPS Sandbox Review -> Can be moved to live (both Task #357 and Task #383)", Status updated to reflect approval.
- Section 8 "DPS Review Before Production Push": reworded from a forward-looking "EOXS will not proceed..." to a completed-tense statement that DPS reviewed all four tasks and confirmed everything working, all four approved to move to live.
- Section 10 Known Validation / DPS Validator paragraph: updated to state Zana Williams validated all four items (Tasks #384/#364 on 2026-07-01, Tasks #357/#383 on 2026-08-19), all four moved to Can be moved to live.
- Sign-Off table: DPS/Client Approver changed to "Zana Williams (all four tasks approved)"; DPS Production Approval changed to "DPS has reviewed this change document and validated all four tasks in sandbox; all four tasks approved to move to live. Production deployment scheduling to follow."
- Also fixed a cosmetic docx-js rendering bug: added `cantSplit: true` to all TableRow constructors (header rows, data rows, and field-table rows) to stop LibreOffice from rendering a stray blank row when a table split across a page boundary — confirmed fixed by re-rendering to PDF and inspecting the page images.

Regenerated the .docx, converted to PDF, reviewed page images (pages 1, 9, 11, 12) to confirm the changes and the page-break fix, then delivered the updated file via SendUserFile as DPS_Production_Change_Document_v2026.08.01.docx with caption "Updated — all four tasks now show DPS sandbox approval and are marked ready to move to live."]
