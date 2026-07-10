#!/usr/bin/env python3
"""Fetch public evidence snapshots and bind their hashes into a packet."""
from __future__ import annotations

import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT.parent / "beacn-drep-resources"
PACKETS = RES / "data/input/governance/decision_support/value_evidence"


def main() -> int:
    for packet_path in sorted(PACKETS.glob("*.json")):
        packet = json.loads(packet_path.read_text())
        changed = False
        for item in (packet.get("fields") or {}).values():
            for source in item.get("sources") or []:
                target = RES / source["snapshot_path"]
                if not target.exists():
                    req = urllib.request.Request(source["url"], headers={"User-Agent": "BEACN-DRep-evidence/1.0"})
                    with urllib.request.urlopen(req, timeout=45) as response:
                        data = response.read()
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                    changed = True
                source["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
        if changed or any(not s.get("sha256") for i in packet["fields"].values() for s in i.get("sources", [])):
            packet["pinned_at_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        packet_path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        print(f"pinned {packet_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
