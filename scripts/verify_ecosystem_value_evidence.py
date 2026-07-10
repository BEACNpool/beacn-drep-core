#!/usr/bin/env python3
"""Deterministically verify independently researched ecosystem-value packets.

This script does not decide whether a claim is true. It verifies that every
directional value field is backed by pinned public snapshots, that high-risk
claims use multiple independent domains, and that the verifier is distinct from
the dossier drafter. Only then may a profile become `independently_verified`.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT.parent / "beacn-drep-resources"
DS = RES / "data" / "input" / "governance" / "decision_support"
PROFILES = DS / "ecosystem_value_profiles.csv"
PACKETS = DS / "value_evidence"
DOSSIERS = DS / "dossiers"

FIELDS = {
    "critical_infrastructure", "open_source_public_good", "measurable_existing_adoption",
    "ecosystem_leverage", "strategic_necessity", "credible_prior_delivery",
    "cost_compared_to_market", "output_priced", "material_duplication", "private_capture_risk",
    "established_service", "builder_workflow_dependency", "low_functional_substitutability",
    "non_funding_disruption_risk",
}
MULTI_SOURCE = {"measurable_existing_adoption", "cost_compared_to_market", "material_duplication",
                "low_functional_substitutability", "non_funding_disruption_risk"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_packet(path: Path) -> tuple[bool, list[str], dict]:
    packet = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    aid = packet.get("action_id")
    if not aid:
        errors.append("action_id missing")
    receipt_path = DOSSIERS / f"{aid}.receipt.json"
    drafter = ""
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        drafter = str(receipt.get("model") or receipt.get("backend") or "")
    verifier = str(packet.get("independent_verifier") or "")
    if not verifier:
        errors.append("independent_verifier missing")
    if drafter and verifier.lower() == drafter.lower():
        errors.append("independent verifier must differ from dossier drafter")
    if packet.get("material_discrepancies"):
        errors.append("material discrepancies must be resolved")

    fields = packet.get("fields") or {}
    domains: set[str] = set()
    flattened_refs: list[str] = []
    values: dict[str, str] = {}
    for field in FIELDS:
        item = fields.get(field) or {"value": "unknown", "sources": []}
        value = str(item.get("value") or "unknown").lower()
        if value not in {"yes", "no", "unknown"}:
            errors.append(f"{field}: invalid value {value}")
            value = "unknown"
        values[field] = value
        sources = item.get("sources") or []
        field_domains: set[str] = set()
        if value != "unknown" and not sources:
            errors.append(f"{field}: directional value has no sources")
        for source in sources:
            url = str(source.get("url") or "")
            domain = (urlparse(url).hostname or "").lower()
            rel = str(source.get("snapshot_path") or "")
            want = str(source.get("sha256") or "")
            snap = (RES / rel).resolve()
            if not url.startswith("https://") or not domain:
                errors.append(f"{field}: source URL must be public HTTPS")
            if not str(snap).startswith(str(RES.resolve())) or not snap.exists() or not snap.is_file():
                errors.append(f"{field}: pinned snapshot missing: {rel}")
                continue
            if "decision_support/dossiers" in rel or "/anchors/" in rel:
                errors.append(f"{field}: proposal/dossier material is not independent evidence")
            observed = sha256(snap)
            if observed != want:
                errors.append(f"{field}: snapshot hash mismatch: {rel}")
            domains.add(domain)
            field_domains.add(domain)
            flattened_refs.append(f"{url}#{observed}")
        if value != "unknown" and field in MULTI_SOURCE and len(field_domains) < 2:
            errors.append(f"{field}: requires two independent source domains")

    if any(v != "unknown" for v in values.values()) and len(domains) < 2:
        errors.append("packet requires at least two independent source domains")
    return not errors, errors, {
        "action_id": aid,
        "values": values,
        "evidence_refs": flattened_refs,
        "confidence": packet.get("confidence", 0),
        "verifier": verifier,
    }


def main() -> int:
    with PROFILES.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = list(reader.fieldnames or [])
        rows = list(reader)
    by_id = {r.get("action_id"): r for r in rows}
    failed = 0
    for path in sorted(PACKETS.glob("*.json")):
        ok, errors, result = verify_packet(path)
        aid = result.get("action_id")
        row = by_id.get(aid)
        if row is None:
            failed += 1
            print(f"HELD {path.name}: profile row missing")
            continue
        if not ok:
            failed += 1
            row["evidence_status"] = "verification_failed"
            row["status"] = "; ".join(errors)[:500]
            print(f"HELD {aid}: {'; '.join(errors)}")
            continue
        row.update(result["values"])
        row["evidence_status"] = "independently_verified"
        row["evidence_refs"] = json.dumps(result["evidence_refs"], separators=(",", ":"))
        row["confidence"] = str(result["confidence"])
        row["owner"] = result["verifier"]
        row["status"] = "verified_pinned_public_sources"
        print(f"VERIFIED {aid}: {len(result['evidence_refs'])} pinned source references")
    with PROFILES.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows({k: r.get(k, "") for k in header} for r in rows)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
