---
thread_name: "ess-zebra-printer-setup"
user: "ron"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

Human: I'm trying to set up the printer for Ryan from ESS. Can you please go through all the calls that we have with him and find me the call where we were setting up this printer on this ERP? I want to see the steps to set up this printer. He brought a new one. It's the same Zebra printer, but you need to do the configuration again.

Assistant: Found it — the call is a Fathom recording titled "Eastern Steel Sales - Ryan, Vince and Bob," December 18, 2025 (3h call, Ron J + Aviral Srivastava with Ryan Capinski, Vince Pappas, and Bob). The Zebra printer/tag-printing setup is the second half of that call. Here's the setup walkthrough from it:

1. Get the app — Aviral shared a Google Drive link in the Zoom chat with the "Print Direct" application (a zip file). Download and extract it (right-click → Extract All), then drag the extracted folder/app to the desktop.

2. Open the app — first launch needs an admin password to install. It's flagged as unverified by Microsoft (Windows SmartScreen warning) — click "More info" → "Run anyway."

3. Connect it to the ERP — in the app, enter:
   - Domain/URL — the server link (sandbox link was used first to test; swap to the live server link when moving to production)
   - Database name — e.g. "ESS" for live
   - Login credentials — same as the ERP login for that server

4. Click Connect — this links the app to the database so it can receive print signals. Once connected, it lists all printers it detects on that machine.

5. Select the Zebra printer from that detected list (on the call it also showed an irrelevant "Brother" printer — pick the Zebra one specifically).

6. Test print — go to Inventory, open any tag, click Print → "Product ZPL." It should print straight to the Zebra with no pop-up.

7. Multiple copies — from a Purchase Order, after confirming receipt, go to the Link Lots tab (appears once tags are generated). Each received tag has a print option there where you enter the number of copies for that tag specifically.

8. Day-to-day use — no reinstall needed. Just open the app and click Connect; it reconnects automatically once logged in the first time.

9. Sandbox → live — when the config target changes (which is your case, since it's a new printer on presumably the live server), you re-open the app, re-enter the live server's Domain/URL and database name, log in once, then reselect the printer from the refreshed detected-printer list, and re-test with a tag print.

For Ryan's new printer: same app, same steps — he'll just need to reconnect it, and on step 5 the new device will show up under a different/new printer name in the app's detected list, which you then select.

Source: Fathom call, "Eastern Steel Sales - Ryan, Vince and Bob," Dec 18, 2025 (eoxs-db).
