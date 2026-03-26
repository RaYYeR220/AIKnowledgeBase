#!/usr/bin/env python3
"""Mock script to queue changed notes for reindexing."""

import json
import sys
from pathlib import Path
from datetime import datetime

QUEUE_FILE = Path("./reindex-queue.jsonl")

path = sys.argv[1] if len(sys.argv) > 1 else None
reason = sys.argv[2] if len(sys.argv) > 2 else "update"

if not path:
    raise SystemExit("usage: queue_reindex_example.py <path> [reason]")

record = {
    "path": path,
    "reason": reason,
    "queued_at": datetime.utcnow().isoformat() + "Z"
}

with QUEUE_FILE.open("a", encoding="utf-8") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")

print(f"queued: {path}")
