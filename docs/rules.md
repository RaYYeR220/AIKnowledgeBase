# Core Rules

## 1. Canonical-source rule
Indexes are not the source of truth.
The canonical knowledge store is the durable human-readable layer.

## 2. Retrieval-before-answer rule
If user context could change the answer, retrieve first.

## 3. Generic-vs-personal rule
Do not confuse topic requests with facts about the user.

## 4. Save-the-fact rule
Save reusable facts, plans, constraints, and preferences — not full transcript dumps.

## 5. Update-existing-first rule
When possible, update an existing note/record instead of creating duplicates.

## 6. Daily/staging rule
Use a temporary layer for fresh capture, then promote durable facts into canonical storage.

## 7. Compression rule
Operational memory should stay compact and instruction-heavy.

## 8. Drift rule
If a fact changes, update the current canonical note and treat the older statement as superseded.

## 9. Stale-index rule
If retrieval returns deleted or moved content, inspect stale index entries before assuming canonical data is wrong.
