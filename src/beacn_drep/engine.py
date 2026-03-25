import csv
import hashlib
import json
from pathlib import Path
from .config import SOUL_REPO, RESOURCES_REPO, OUTPUT_DIR, AUDIT_LOG
from .routing import select_resources
from .adapters.git_adapter import commit_hash
from .replay import sha256_file, canonical_json_hash, csv_row_by_action, write_manifest, read_manifest


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_registry() -> list[dict]:
    path = RESOURCES_REPO / "registries" / "resource_registry.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _load_actions() -> list[dict]:
    path = RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_all.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _load_flags() -> dict[str, list[dict]]:
    path = RESOURCES_REPO / "data" / "input" / "governance" / "governance_action_flags.csv"
    if not path.exists():
        return {}
    out: dict[str, list[dict]] = {}
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out.setdefault(r.get("action_id", ""), []).append(r)
    return out


def _load_soul() -> tuple[str, str]:
    path = SOUL_REPO / "README.md"
    text = path.read_text(encoding="utf-8")
    return text, _sha256_bytes(text.encode("utf-8"))


def _resource_snapshot_entry(resource_row: dict, action_id: str) -> dict | None:
    source_url = resource_row["source_url"]
    if source_url.startswith("http://") or source_url.startswith("https://"):
        return {
            "resource_id": resource_row["resource_id"],
            "kind": "remote",
            "source_url": source_url,
            "note": "remote resources must be pinned to local snapshot for strict replay",
        }

    path = RESOURCES_REPO / source_url
    if not path.exists():
        return {
            "resource_id": resource_row["resource_id"],
            "kind": "missing",
            "source_url": source_url,
            "exists": False,
        }

    entry = {
        "resource_id": resource_row["resource_id"],
        "kind": "file",
        "path": source_url,
        "file_hash": sha256_file(path),
    }

    if path.suffix.lower() == ".csv":
        row = csv_row_by_action(path, action_id)
        if row is not None:
            entry["selected_row"] = row
            entry["selected_row_hash"] = canonical_json_hash(row)

    return entry


def _to_float(v: str | None) -> float:
    try:
        return float(v) if v not in (None, "") else 0.0
    except Exception:
        return 0.0


def _score_action(action: dict, flags: list[dict]) -> dict:
    action_type = (action.get("action_type") or "").lower()
    flag_score = _to_float(action.get("flag_score"))
    drep_yes = _to_float(action.get("drep_yes_pct"))
    drep_no = _to_float(action.get("drep_no_pct"))
    drep_abstain = _to_float(action.get("drep_abstain_pct"))

    score = 0.0
    facts = []
    inf = []
    unc = []

    # conservative doctrine-aligned rule set
    if "treasury" in action_type:
        score -= 0.20
        facts.append("Treasury withdrawal actions require elevated scrutiny.")
    if "parameter" in action_type:
        score -= 0.10
        facts.append("Protocol parameter changes carry system-wide risk.")
    if "hardfork" in action_type:
        score -= 0.25
        facts.append("Hard fork actions require strongest evidence quality.")

    score -= min(flag_score / 20.0, 0.5)
    if flag_score > 0:
        facts.append(f"Flag score present ({int(flag_score)}), reducing confidence.")

    if drep_yes + drep_no + drep_abstain > 0:
        margin = (drep_yes - drep_no) / 100.0
        score += max(min(margin, 0.25), -0.25)
        inf.append("Network DRep distribution used as one signal, not authority.")
    else:
        unc.append("No DRep distribution available.")

    # recommendation thresholds
    if flag_score >= 8:
        rec = "ABSTAIN"
        unc.append("High risk flags triggered conservative abstain.")
    elif score >= 0.15:
        rec = "YES"
    elif score <= -0.20:
        rec = "NO"
    else:
        rec = "ABSTAIN"

    confidence = max(0.0, min(1.0, 0.55 + abs(score) - (0.03 * len(flags))))
    return {
        "recommendation": rec,
        "score": round(score, 4),
        "confidence": round(confidence, 4),
        "facts": facts or ["Deterministic rule set applied."],
        "inferences": inf or ["No additional inference."],
        "uncertainty": unc or ["Rule-based system; does not infer unstated intent."],
    }


def run_once(action_id: str | None = None) -> dict:
    actions = _load_actions()
    action = next((a for a in actions if a["action_id"] == action_id), actions[0])
    flags_by_action = _load_flags()

    raw_bytes = json.dumps(action, sort_keys=True).encode("utf-8")
    input_hash = _sha256_bytes(raw_bytes)
    action_type = action["action_type"]

    soul_text, soul_text_hash = _load_soul()
    soul_commit = commit_hash(SOUL_REPO)
    resources_commit = commit_hash(RESOURCES_REPO)

    registry = _load_registry()
    resources = select_resources(registry, action_type)
    resources_used = [r["resource_id"] for r in resources]

    resource_snapshots = []
    for r in resources:
        snap = _resource_snapshot_entry(r, action["action_id"])
        if snap:
            resource_snapshots.append(snap)

    snapshot_bundle_hash = canonical_json_hash({
        "action": action,
        "resource_snapshots": resource_snapshots,
        "soul_commit": soul_commit,
        "soul_text_hash": soul_text_hash,
        "resource_registry_commit": resources_commit,
    })

    score_obj = _score_action(action, flags_by_action.get(action["action_id"], []))

    rationale = {
        "action_id": action["action_id"],
        "action_type": action_type,
        "recommendation": score_obj["recommendation"],
        "score": score_obj["score"],
        "confidence": score_obj["confidence"],
        "facts": score_obj["facts"],
        "inferences": score_obj["inferences"],
        "uncertainty": score_obj["uncertainty"],
        "input_hash": input_hash,
        "snapshot_bundle_hash": snapshot_bundle_hash,
        "soul_commit": soul_commit,
        "soul_text_hash": soul_text_hash,
        "resource_registry_commit": resources_commit,
        "resources_used": resources_used,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    run_id = f"{action['action_id']}-{input_hash[:12]}"
    out_dir = OUTPUT_DIR / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "run_id": run_id,
        "action": action,
        "input_hash": input_hash,
        "action_type": action_type,
        "soul_commit": soul_commit,
        "soul_text_hash": soul_text_hash,
        "resource_registry_commit": resources_commit,
        "resources_used": resources_used,
        "resource_snapshots": resource_snapshots,
        "snapshot_bundle_hash": snapshot_bundle_hash,
    }

    (out_dir / "rationale.json").write_text(json.dumps(rationale, indent=2) + "\n", encoding="utf-8")
    (out_dir / "rationale.md").write_text(
        "\n".join([
            f"# Rationale: {action['action_id']}",
            f"Recommendation: **{score_obj['recommendation']}**",
            f"Score: `{score_obj['score']}` | Confidence: `{score_obj['confidence']}`",
            "",
            "## Facts",
            *[f"- {x}" for x in score_obj["facts"]],
            "",
            "## Inferences",
            *[f"- {x}" for x in score_obj["inferences"]],
            "",
            "## Uncertainty",
            *[f"- {x}" for x in score_obj["uncertainty"]],
            "",
            "## Reproducibility",
            f"- input_hash: `{input_hash}`",
            f"- snapshot_bundle_hash: `{snapshot_bundle_hash}`",
            f"- soul_commit: `{soul_commit}`",
            f"- soul_text_hash: `{soul_text_hash}`",
            f"- resource_registry_commit: `{resources_commit}`",
            f"- resources_used: `{', '.join(resources_used)}`",
        ]) + "\n",
        encoding="utf-8",
    )
    write_manifest(out_dir / "input_manifest.json", manifest)

    log_row = {
        "run_id": run_id,
        "action_id": action["action_id"],
        "recommendation": score_obj["recommendation"],
        "score": score_obj["score"],
        "confidence": score_obj["confidence"],
        "input_hash": input_hash,
        "snapshot_bundle_hash": snapshot_bundle_hash,
        "soul_commit": soul_commit,
        "resource_registry_commit": resources_commit,
    }
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_row) + "\n")

    return {"run_id": run_id, "output_dir": str(out_dir)}


def run_all(limit: int | None = None) -> dict:
    actions = _load_actions()
    run_ids = []
    for a in actions[:limit] if limit else actions:
        run_ids.append(run_once(a["action_id"])["run_id"])
    return {"runs": len(run_ids), "run_ids": run_ids}


def verify_replay(run_id: str) -> dict:
    out_dir = OUTPUT_DIR / run_id
    manifest_path = out_dir / "input_manifest.json"
    manifest = read_manifest(manifest_path)

    expected_input_hash = manifest["input_hash"]
    action = manifest["action"]
    observed_input_hash = _sha256_bytes(json.dumps(action, sort_keys=True).encode("utf-8"))

    checks = {
        "input_hash_match": expected_input_hash == observed_input_hash,
        "resource_hashes_match": True,
        "row_hashes_match": True,
    }

    for snap in manifest.get("resource_snapshots", []):
        if snap.get("kind") != "file":
            continue
        path = RESOURCES_REPO / snap["path"]
        if not path.exists() or sha256_file(path) != snap.get("file_hash"):
            checks["resource_hashes_match"] = False
        if "selected_row_hash" in snap and "selected_row" in snap:
            current_row = csv_row_by_action(path, action.get("action_id"))
            if current_row is None or canonical_json_hash(current_row) != snap["selected_row_hash"]:
                checks["row_hashes_match"] = False

    recomputed_bundle_hash = canonical_json_hash({
        "action": manifest["action"],
        "resource_snapshots": manifest["resource_snapshots"],
        "soul_commit": manifest["soul_commit"],
        "soul_text_hash": manifest.get("soul_text_hash", ""),
        "resource_registry_commit": manifest["resource_registry_commit"],
    })
    checks["snapshot_bundle_hash_match"] = recomputed_bundle_hash == manifest["snapshot_bundle_hash"]

    checks["ok"] = all(checks.values())
    checks["run_id"] = run_id
    return checks
