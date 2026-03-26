#!/usr/bin/env python3
"""Mock processor for queued reindex tasks.
Replace the inner steps with your actual indexing pipeline.
"""

from pathlib import Path
import json

QUEUE_FILE = Path("./reindex-queue.jsonl")

if not QUEUE_FILE.exists():
    print("no queue file")
    raise SystemExit(0)

for line in QUEUE_FILE.read_text(encoding="utf-8").splitlines():
    rec = json.loads(line)
    print(f"would reindex: {rec['path']} ({rec.get('reason', 'update')})")

print("done")
