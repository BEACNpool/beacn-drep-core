#!/usr/bin/env python3
"""Verify pinned protocol-readiness packets before directional protocol votes."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT.parent / "beacn-drep-resources"
DS = RES / "data" / "input" / "governance" / "decision_support"
CSV = DS / "protocol_readiness_profiles.csv"
PACKETS = DS / "protocol_evidence"
FIELDS = {
    "version_guardrails_pass", "testnet_results_pass", "spo_readiness_pass",
    "exchange_readiness_pass", "dapp_readiness_pass", "security_review_pass",
    "constitutional_alignment_pass", "impact_analysis_complete",
    "rollback_or_containment_plan", "safety_margin_clear", "affirmative_blocker",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    with CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); header = list(reader.fieldnames or []); rows = list(reader)
    by_id = {r.get("action_id"): r for r in rows}
    failed = 0
    for packet_path in sorted(PACKETS.glob("*.json")):
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        aid = packet.get("action_id"); row = by_id.get(aid); errors = []
        if row is None:
            errors.append("profile row missing")
        domains = set(); refs = []
        for field in FIELDS:
            item = (packet.get("fields") or {}).get(field) or {"value": "unknown", "sources": []}
            value = str(item.get("value") or "unknown").lower()
            if value not in {"yes", "no", "unknown"}: errors.append(f"{field}: invalid value")
            sources = item.get("sources") or []
            if value != "unknown" and not sources: errors.append(f"{field}: sources required")
            for source in sources:
                url = str(source.get("url") or ""); rel = str(source.get("snapshot_path") or "")
                snap = (RES / rel).resolve(); domain = (urlparse(url).hostname or "").lower()
                if not url.startswith("https://") or not domain: errors.append(f"{field}: public HTTPS URL required")
                if not str(snap).startswith(str(RES.resolve())) or not snap.is_file():
                    errors.append(f"{field}: snapshot missing"); continue
                got = digest(snap)
                if got != source.get("sha256"): errors.append(f"{field}: hash mismatch")
                if "/anchors/" in rel or "decision_support/dossiers" in rel:
                    errors.append(f"{field}: proposal material is not independent readiness evidence")
                domains.add(domain); refs.append(f"{url}#{got}")
            if row is not None: row[field] = value
        if len(domains) < 2: errors.append("at least two independent source domains required")
        if packet.get("material_discrepancies"): errors.append("material discrepancies unresolved")
        if errors:
            failed += 1
            if row is not None: row.update(evidence_status="verification_failed", status="; ".join(errors)[:500])
            print(f"HELD {aid}: {'; '.join(errors)}")
        else:
            row.update(evidence_status="independently_verified", evidence_refs=json.dumps(refs),
                       owner=str(packet.get("independent_verifier") or "independent-verifier"),
                       status="verified_pinned_public_sources")
            print(f"VERIFIED {aid}: {len(refs)} source references")
    with CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header); writer.writeheader()
        writer.writerows({k: r.get(k, "") for k in header} for r in rows)
    return 1 if failed else 0


if __name__ == "__main__": raise SystemExit(main())
