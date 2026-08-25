---
thread_name: "quotation-s18005-status-error-reply"
user: "hashir"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

User: i need to reply him that we did not got the error while we changed the status of the order, if they could refresh this at there end and let us know if they are experiencing the same, the reply should be polite helpful and professional

[Uploaded image: screenshot of Odoo Quotations S18005 chatter showing a draft message "Hi @James Baker" and log notes by Hashir Saleem showing status changes: Status: Cancelled → Quotation, Status: Sales Order → Cancelled]

Assistant: Here's a draft reply:

Hi James,

Thanks for flagging this. On our end, we did not encounter any error when changing the status of the order. Could you please refresh the page on your end and try again? Let us know if you're still seeing the issue so we can look into it further.

Thanks for your patience.

User: [Uploaded image: screenshot of an Outlook email inbox, email from Eddie Poind... to EOXS, subject "EOXS", body: "Humaira, The system will not allow me to enter an order? Error: Eoxs Server Error Traceback (most recent call last): File \"/opt/odoo/golden-file/odoo/models.py\", line 5101, in ensure_one _id, = self._ids ValueError: not enough values to unpack (expected 1, got 0) During handling of the above exception, another exception occurred: Traceback (most recent call last): File \"/opt/odoo/golden-file/odoo/http.py\", line 624, in _handle_exception return super(JsonRequest, self)._handle_exception(exception) File \"/opt/odoo/golden-file/odoo/http.py\", line 310, in _handle_exception raise pycompat.reraise(type(exception), exception, sys.exc_info()[2]) File \"/opt/odoo/golden-file/odoo/tools/pycompat.py\", line 14, in reraise raise value File \"/opt/odoo/golden-file/odoo/http.py\", line 669, in dispatch result = self._call_function(**self.params)"]

We need to reply eddie on this one where we need to inform him that when we create the quote and if the Unit of Measurement field for unit price is empty while moving through the order to fill in the details we experience this error, where the system asks us to enter the uom value and then the error removes

Assistant: Draft reply to Eddie:

Hi Eddie,

Thanks for sharing the error details. We looked into this and found the cause: when creating the quote, if the Unit of Measurement (UoM) field for the unit price is left empty, the system throws this error while moving through the order. Once the UoM value is entered, the error resolves.

Please try filling in the UoM field before proceeding and let us know if the issue persists.

Thanks,
