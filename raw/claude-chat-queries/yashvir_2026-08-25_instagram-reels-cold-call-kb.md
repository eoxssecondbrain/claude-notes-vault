---
thread_name: "instagram-reels-cold-call-kb"
user: "yashvir"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

User: is there a way you can watch the reels faster, use your powers and make me a roadmap which requires my min intervention and i can just share the reels link with you and you can watch transcribe and add it to the KB?

Assistant: Straight answer: no, I can't fetch or watch a video from an Instagram link. My network access doesn't include instagram.com or its CDN, and even a browser session wouldn't hand me a file I can process — that's a hard limitation, not something a smarter workflow works around. So "just share the link" isn't achievable here. Downloading and uploading the file stays the required step on your end.

What I can actually speed up:

1. Batch uploads. Send 5-10 videos in one message instead of one at a time — I process the batch and give you one updated KB file, not five round trips.

2. Automate the caption reading. What I did manually just now (extract frames, build contact sheets, read them visually) can be replaced with an OCR script — extract frames, run text recognition on the caption region, dedupe repeated frames, reconstruct the line automatically. Faster and more consistent than me eyeballing grids, for any reel where the script is burned in as on-screen text (like this one was).

3. Standing workflow. Once set up, you stop specifying format — you just drop files and say "add these," I auto-detect, append to the same KB file, and give you a one-line summary of what got added.

One real limitation to flag: reels that rely purely on spoken audio with no on-screen captions. I have no speech-to-text available in this sandbox — the models aren't reachable on the allowed network. For those I'd either need you to jot the line manually, or you stick to reels with burned-in captions, which seems to be the format you're already pulling from.

Want me to build and test the OCR script now against this same video, so we confirm it matches what I read manually before relying on it for future ones?

---

User: So basically i had to download the videos first.?

Assistant: Yes. That step doesn't go away — link-sharing isn't an option here, so download-then-upload is the workflow.

---

User: Can we build an agent that would reduce my work from minimal to 0?

Assistant: No — not to zero, and worth being direct about why before we design anything:

The download step is tied to a judgment call you're making — scrolling your feed, recognizing "this opener is good," saving it. That's not a mechanical task an agent can replicate; it's the actual value you're adding. An agent that auto-downloads reels based on some rule (hashtag, account, keyword) would need a proxy for "good," and you'd end up reviewing its picks anyway — which is the same work relocated, not removed.

Separately, a background agent that logs into Instagram and scrapes/downloads content on a schedule is against Instagram's Terms of Service. That's not a technical limitation I can engineer around — it's a real risk (account flags/bans) if you want to seriously consider it, so I'd flag it rather than build it quietly.

What's actually achievable, ordered by effort saved:

1. One-click download tool (e.g. a browser extension or yt-dlp) so "download" becomes a single click instead of screen-recording or hunting for a save option. Doesn't touch your curation step.

2. Batch instead of one-at-a-time. You save reels to a folder all week, upload the folder once. Reduces round trips, not decisions.

3. A watched-folder script — if you're on Claude Code or similar, a script watches a local folder and auto-runs the frame-extraction + OCR + KB-append pipeline the moment a file lands, no upload step needed on your end. This gets you close to zero for steps 2 onward (transcribe, tag, append) — but step 1 (you deciding what's worth saving and clicking download) stays yours.

Realistic floor: you click "download" on reels you already decided were good. Everything after that can be near-automatic.

Want me to build the watched-folder pipeline (step 3), or the OCR script from earlier first so we validate accuracy before wiring it into anything automatic?

---

User: lets build this agent

Assistant: [asked clarifying question via options: where should this run — local Claude Code, manual batch mode in chat, or explain tradeoff first]

---

User: Q: Where should this run?
A: upto you

Assistant: [Built reel_to_kb.py — a script combining ffmpeg frame extraction, pytesseract OCR on a cropped caption region, and markdown KB appending, with --once and --watch modes. Tested it end-to-end against the previously-shared reel.]

Ran the script against the known reel. Result was garbage — full OCR output was unreadable noise mixed with a few recognizable fragments, not usable.

Reported this plainly: "That test just failed — worth showing you, not just telling you," showed the raw garbled OCR output, then attempted a fix (tighter crop + image thresholding on a known frame reading "Give me"). The cleaned/thresholded crop was visually perfect and human-readable, but tesseract still returned garbage across every psm mode tried (6,7,8,11,12).

Concluded: "This isn't a crop-calibration problem, it's the font: stylized italic serif captions with drop shadows are a known weak spot for tesseract, and no amount of preprocessing fixed it here." Stated I would not ship an agent that silently produces garbage KB entries. Revised the realistic ceiling: unattended OCR isn't reliable for this caption style; the actual reading step still requires vision (me), which means a chat turn per batch, not a silent background job. Proposed the honest floor: you download → you batch-upload → I read and log — and offered to at least build the frame-sampling/dedup/formatting automation around that, since that mechanical part doesn't need visual judgment.

---

User: i didn't say make it 0 eentirely, i just said reduce it to the minimum you can

Assistant: Built reel_prep.py — a script that automates frame extraction (ffmpeg) and assembles frames into contact sheets for fast visual review, replacing the multiple manual ffmpeg+montage tool calls previously needed per video. Explicitly did NOT include OCR (already proven unreliable) or a naive full-frame dedup step.

First test run showed dedup wasn't dropping any frames (99 raw -> 99 kept) because full-frame pixel diff was dominated by handheld camera/background movement rather than caption changes. Fixed the diff function to compare only the caption-band crop instead of the full frame, re-tested — still barely reduced frame count (132 -> 125).

Diagnosed directly by comparing known same-caption frame pairs vs a genuine caption-change pair using actual reel footage: same-caption pairs scored 26.75 and 40.45 (mean pixel diff), while a genuine caption-change pair scored only 19.19 — proving the diff signal could not reliably distinguish "same caption, camera/hand moved" from "caption actually changed." Concluded the dedup heuristic was unreliable and explicitly disabled it in the script rather than shipping a threshold known to risk dropping real captions, with an inline comment documenting why and the measured scores.

Re-ran with dedup disabled and fps=2 (66 frames, 6 contact sheets) and viewed sheet_01.png to confirm output quality — it was clean and fully readable, and in fact resolved a previously-uncertain caption ("Hey Alex, what's your call opener?" — the full narrator line, not previously fully captured).

Gave a final honest breakdown:
- Works and packaged: frame extraction + contact-sheet building (one script call vs ~15 manual tool calls per video previously).
- Tested and dropped: OCR-based caption reading (fails on this stylized italic font even on a clean crop), and frame deduping (hand/camera movement produces diff scores indistinguishable from real caption changes).
- Final workflow: user downloads and batch-uploads reels -> Claude runs reel_prep.py once per batch -> Claude reads the resulting contact sheets and writes KB entries -> Claude appends to the KB and shares it. User's step did not shrink further than "download and batch-upload." Claude's per-video tool-call overhead dropped from ~15 to ~2.

[Created and shared file: /mnt/user-data/outputs/reel_prep.py — the validated frame-extraction + contact-sheet automation script, with dedup left present in code but disabled and documented as unreliable.]

Closed by inviting the user to send the next batch of reels, multiple videos in one message, for Claude to run reel_prep.py on all of them before reading and updating the KB.
