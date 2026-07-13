#!/usr/bin/env python3
"""Fetch public evidence snapshots and bind their hashes into a packet.

This fetch IS the integrity backstop for the whole ecosystem-value evidence base. Every cited URL
is retrieved and SHA-256 hashed here, so an invented, dead, moved or auth-walled citation cannot
survive into evidence — it simply fails to pin. Nothing downstream has to trust whoever wrote the
packet.

A URL that will not fetch is not evidence, so we DROP that source rather than abort. If dropping
leaves a directional field with no sources at all, the field is demoted to "unknown" — honest, and
it keeps the rest of the packet usable. Under BEACN doctrine missing evidence can never become a
NO, so an "unknown" is always safe; a fabricated "yes" is not.

Previously a single 404 raised out of the loop and killed the pinning of EVERY packet.
"""
from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT.parent / "beacn-drep-resources"
PACKETS = RES / "data/input/governance/decision_support/value_evidence"

UA = "BEACN-DRep-evidence/1.0 (+https://beacnpool.github.io/beacn-drep-web/)"

# Snapshots are arbitrary third-party pages committed to a PUBLIC repo, and any page may contain a
# credential-shaped string: a presigned S3 URL carrying an AWS access-key id, a site's public Google
# browser key, even a content-hashed image filename that happens to look like a Mailgun key (all
# three showed up in the 2026-07-12 backfill and GitHub push protection rightly blocked the push).
#
# None of that is evidence — it is incidental page furniture — and none of it should be republished
# from BEACN's repo. Redact on write so the problem cannot recur on the next backfill. The
# evidential PROSE is untouched, and the sha256 is taken AFTER redaction, so the packet stays
# internally consistent and verifiable.
SECRET_PATTERNS = [
    re.compile(rb"key-[0-9a-f]{32}"),                     # Mailgun-shaped (and Docusaurus asset hashes)
    re.compile(rb"AKIA[0-9A-Z]{16}"),                     # AWS access-key id
    re.compile(rb"ASIA[0-9A-Z]{16}"),                     # AWS temporary access-key id
    re.compile(rb"AIza[0-9A-Za-z_\-]{35}"),               # Google API key
    re.compile(rb"gh[pousr]_[A-Za-z0-9]{36,}"),           # GitHub token
    re.compile(rb"xox[baprs]-[A-Za-z0-9\-]{10,}"),        # Slack token
    re.compile(rb"sk-[A-Za-z0-9]{32,}"),                  # OpenAI-style key
    re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),   # any private key block
]
REDACTION = b"[REDACTED-CREDENTIAL-SHAPED-STRING]"


def sanitize(data: bytes) -> tuple[bytes, int]:
    """Strip credential-shaped strings from a fetched page. Returns (clean_bytes, n_redacted)."""
    n = 0
    for pat in SECRET_PATTERNS:
        data, hits = pat.subn(REDACTION, data)
        n += hits
    return data, n


def fetch(url: str) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=45) as response:
            if getattr(response, "status", 200) >= 400:
                return None
            return response.read()
    except Exception:
        return None


def main() -> int:
    total_kept = total_dropped = total_demoted = 0
    total_redacted = 0
    redacted_now = [0]      # redactions applied to newly fetched pages

    # Re-sanitise anything already on disk from an earlier run (pre-redaction snapshots).
    for snap in sorted((PACKETS / "snapshots").glob("*")):
        if not snap.is_file():
            continue
        raw = snap.read_bytes()
        clean, n = sanitize(raw)
        if n:
            snap.write_bytes(clean)
            total_redacted += n
            print(f"  REDACT {snap.name[:44]:46} {n} credential-shaped string(s)")

    for packet_path in sorted(PACKETS.glob("*.json")):
        packet = json.loads(packet_path.read_text())
        changed = False
        kept = dropped = demoted = 0

        for field_name, item in (packet.get("fields") or {}).items():
            live_sources = []
            for source in item.get("sources") or []:
                url = source.get("url") or ""
                rel_path = source.get("snapshot_path") or ""
                # Without a snapshot_path this resolved to the resources repo ROOT, and hashing it
                # blew up with IsADirectoryError. A source we cannot pin is not evidence — drop it
                # rather than let it ride along unhashed.
                if not rel_path or not url:
                    dropped += 1
                    print(f"  DROP  {packet_path.stem[:20]:22} {field_name:30} malformed source (no url/snapshot_path)")
                    continue
                target = RES / rel_path
                if not target.exists():
                    data = fetch(url)
                    if data is None:
                        dropped += 1
                        print(f"  DROP  {packet_path.stem[:20]:22} {field_name:30} unfetchable: {url[:60]}")
                        continue
                    data, n_red = sanitize(data)   # never republish a credential-shaped string
                    redacted_now[0] += n_red
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                    changed = True
                source["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
                live_sources.append(source)
                kept += 1

            item["sources"] = live_sources
            # A directional claim with no surviving source is unverifiable — say "unknown".
            if str(item.get("value", "unknown")).lower() != "unknown" and not live_sources:
                item["value"] = "unknown"
                demoted += 1
                changed = True

        if changed or any(not s.get("sha256")
                          for i in (packet.get("fields") or {}).values()
                          for s in i.get("sources", [])):
            packet["pinned_at_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")

        packet_path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        print(f"pinned {packet_path.name[:34]:36} kept={kept:2} dropped={dropped:2} demoted={demoted:2}")
        total_kept += kept
        total_dropped += dropped
        total_demoted += demoted

    print(f"\nsources pinned={total_kept} dropped(unfetchable)={total_dropped} "
          f"fields demoted to unknown={total_demoted} "
          f"credential-shaped strings redacted={total_redacted + redacted_now[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
