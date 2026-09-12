"""Create deterministic feature-store snapshots and fingerprints."""
from __future__ import annotations

import hashlib
import json
from typing import Any


def snapshot(rows: list[dict[str, Any]], key: str = "id") -> dict[str, Any]:
    """Sort records by key and hash their canonical JSON representation."""
    records = sorted(rows, key=lambda row: str(row[key]))
    payload = json.dumps(records, sort_keys=True, separators=(",", ":"), default=str)
    return {"records": records, "sha256": hashlib.sha256(payload.encode()).hexdigest()}
