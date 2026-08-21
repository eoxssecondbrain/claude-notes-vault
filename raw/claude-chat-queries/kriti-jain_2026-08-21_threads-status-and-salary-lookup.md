---
thread_name: "threads-status-and-salary-lookup"
user: "kriti-jain"
type: claude-chat
created: 2026-08-21
updated: 2026-08-21
---

## User
tell me all the threads that were chatted by or created newly by kriti.

## Assistant
Attempted to reach Threads_OV connector to list Claude account chat threads created/chatted by Kriti. Server connection state was "failed" on initial attempt — reported this to user, asked them to reconnect Threads OV in connector settings.

## User
i asked about the threads on claude account.

## Assistant
Confirmed that Threads OV is the correct connector for Claude account chat threads. Retried connection — still failing. Told user I can't list threads or run mandatory transcript save until the connector reconnects, asked them to check on their end.

## User
what is kriti's salary?

## Assistant
Looked up the "EOXS Salary Details" internal asset (tier2_confidential, id 10, slug eoxs-salary-details). Found Kriti Jain's row (Sr. No. 91, Mkt/Ops) in the Jan–Jun 2026 sheet. Reported visible (non-redacted) figures only, per redaction rules:
- Jan/Feb 2026: no figures listed
- Mar 2026: USD and INR both [restricted]
- Apr 2026: USD 84.21, INR [restricted]
- May 2026: USD 164.00, INR 15,580.00
- Jun 2026: USD 132.27, INR 12,489.00

Noted earlier months (Aug–Dec 2023) in the same document were almost entirely restricted for her row too, and that full unredacted figures would require higher access-tier permissions than available in this session. Did not attempt to infer restricted values.
