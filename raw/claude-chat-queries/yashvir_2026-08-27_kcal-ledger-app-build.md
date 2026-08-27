---
thread_name: "kcal-ledger-app-build"
user: "yashvir"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

## Continued

**User:** [screenshot of Android app Voice tab] — text showing mojibake ("â€œ", "ðŸŽ¤ Voice" instead of 🎤) and all 3 parsed voice items showing "No match — tap to pick a food" for a long rambling dictated sentence. Asked "why is it showing this?"

**Assistant:** Diagnosed two separate issues:
1. Mojibake — real bug: Android WebView sometimes ignores `<meta charset="UTF-8">` for Capacitor-packaged local content and defaults to ISO-8859-1, corrupting all multi-byte UTF-8 chars (emoji, curly quotes, em dashes). Fixed via `MainActivity.java` override forcing `getSettings().setDefaultTextEncodingName("utf-8")`, plus added a redundant `<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">` tag in both the Android and Mac build-www.py wrapper scripts. Regenerated www/index.html for both projects and also copied the corrected file into `android/app/src/main/assets/public/index.html` (the actual file the compiled APK loads — the www/ copy alone wasn't enough). Re-zipped and delivered both `kcal-ledger-android.zip` and `kcal-ledger-mac.zip` with the fix.
2. "No match" on all 3 voice items — not a bug: the transcript was a rambling, self-questioning run-on sentence, not clean "quantity + food" phrasing; the rule-based parser correctly declined to guess rather than mismatch. Explained the parser splits on commas/and/with/plus and needs tighter phrasing to work reliably; suggested re-testing with cleaner phrasing after reinstalling the fixed build.
