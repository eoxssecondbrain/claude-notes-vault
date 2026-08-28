---
thread_name: "books-mcp-vault-index"
user: "ayan"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

USER:
Use the books MCP and list me down the entire index present in the vault

ASSISTANT:
Books MCP isn't covered by either existing skill (threads-ov = chat transcripts, raj-eoxs-vault = EOXS data) — no skill file governs this connector, flagging per your standing rule.

Tier server status: this server is tier 1, allowed tiers [1,2,3]. Row counts: T1 = 48, T2 = 152, T3 = 2. Total = 202 notes.

list_recent_tiered_notes caps at 50 regardless of the limit passed (confirmed: limit=250 and limit=5 both returned exactly the requested count up to a 50 ceiling, and there's no offset/pagination parameter in the tool schema). So this is the most recent 50 of 202, not the entire index — 152 older notes aren't retrievable through this tool.

Most recent 50 notes (id, tier, title):

1326 (T2) The Wisdom of Father Brown
1325 (T2) The Moon and Sixpence
1324 (T2) The Return of Sherlock Holmes
1323 (T2) The Secret Sharer
1322 (T2) Heart of Darkness
1321 (T2) C. Iuli Caesaris De Bello Gallico, I-IV
1320 (T2) Sons and Lovers
1319 (T1) The Tao Teh King, or the Tao and its Characteristics
1318 (T2) The Call of the Wild
1317 (T2) In the Days When the World Was Wide, and Other Verses
1316 (T2) The Man from Snowy River
1315 (T2) A List of Factorial Math Constants
1314 (T2) The Aspern Papers
1313 (T2) An International Episode
1312 (T2) The Turn of the Screw
1311 (T2) Daisy Miller: A Study
1310 (T2) The Spell of the Yukon and Other Verses
1309 (T2) The Martin Luther King, Jr. Day, 1995, Memorial Issue
1308 (T2) Walden, and On The Duty Of Civil Disobedience
1307 (T2) The Innocence of Father Brown
1306 (T2) Uncle Tom's Cabin
1305 (T2) My Bondage and My Freedom
1304 (T2) Flatland: A Romance of Many Dimensions
1303 (T2) The Project Gutenberg Encyclopedia, Volume 1 of 28
1302 (T2) The Project Gutenberg RST Manual
1301 (T2) The 1994 CIA World Factbook
1300 (T2) The Europeans
1299 (T2) Confidence
1298 (T2) The American
1297 (T2) Roderick Hudson
1296 (T2) The Phantom of the Opera
1295 (T2) The Picture of Dorian Gray
1294 (T2) The Insidious Dr. Fu Manchu
1293 (T2) The Haunted Bookshop
1292 (T2) Charlotte Temple
1291 (T2) The Haunted Hotel: A Mystery of Modern Venice
1290 (T2) The Well at the World's End: A Tale
1289 (T2) The History and Practice of the Art of Photography
1288 (T2) American Hand Book of the Daguerreotype
1287 (T2) Summer
1286 (T2) McTeague: A Story of San Francisco
1285 (T2) Twenty Thousand Leagues under the Sea
1284 (T2) Flower Fables
1283 (T2) Take Me for a Ride: Coming of Age in a Destructive Cult
1282 (T2) Sense and Sensibility
1281 (T2) The Awakening, and Selected Short Stories
1280 (T2) The Island of Doctor Moreau
1279 (T2) Emma
1278 (T2) Daddy-Long-Legs
1277 (T2) Symphony No. 5 in C minor, Opus 67

To get the remaining 152 older entries, the only path with the current toolset is search_tiered_wiki with targeted queries (it does full-text search, not indexing, so it's not a clean substitute) or read_tiered_note by guessing IDs below 1277 — neither actually enumerates them. If a full inventory matters, that's a gap worth raising with whoever built this connector: a paginated list or an offset param would fix it.
