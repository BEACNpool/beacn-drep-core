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
    path = RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_sample.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


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


def run_once(action_id: str | None = None) -> dict:
    actions = _load_actions()
    action = next((a for a in actions if a["action_id"] == action_id), actions[0])

    raw_bytes = json.dumps(action, sort_keys=True).encode("utf-8")
    input_hash = _sha256_bytes(raw_bytes)
    action_type = action["action_type"]

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
        "resource_registry_commit": resources_commit,
    })

    recommendation = "ABSTAIN"
    rationale = {
        "action_id": action["action_id"],
        "action_type": action_type,
        "recommendation": recommendation,
        "facts": ["Deterministic scaffold with snapshot manifest."],
        "inferences": ["Scoring model pending; conservative default applied."],
        "uncertainty": ["Remote sources require pinned snapshots for strict replay."],
        "input_hash": input_hash,
        "snapshot_bundle_hash": snapshot_bundle_hash,
        "soul_commit": soul_commit,
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
        "resource_registry_commit": resources_commit,
        "resources_used": resources_used,
        "resource_snapshots": resource_snapshots,
        "snapshot_bundle_hash": snapshot_bundle_hash,
    }

    (out_dir / "rationale.json").write_text(json.dumps(rationale, indent=2) + "\n", encoding="utf-8")
    (out_dir / "rationale.md").write_text(
        "\n".join([
            f"# Rationale: {action['action_id']}",
            f"Recommendation: **{recommendation}**",
            "",
            "## Facts",
            "- Deterministic scaffold with snapshot manifest.",
            "",
            "## Inferences",
            "- Scoring model pending; conservative default applied.",
            "",
            "## Uncertainty",
            "- Remote sources require pinned snapshots for strict replay.",
            "",
            "## Reproducibility",
            f"- input_hash: `{input_hash}`",
            f"- snapshot_bundle_hash: `{snapshot_bundle_hash}`",
            f"- soul_commit: `{soul_commit}`",
            f"- resource_registry_commit: `{resources_commit}`",
            f"- resources_used: `{', '.join(resources_used)}`",
        ]) + "\n",
        encoding="utf-8",
    )
    write_manifest(out_dir / "input_manifest.json", manifest)

    log_row = {
        "run_id": run_id,
        "action_id": action["action_id"],
        "input_hash": input_hash,
        "snapshot_bundle_hash": snapshot_bundle_hash,
        "soul_commit": soul_commit,
        "resource_registry_commit": resources_commit,
    }
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_row) + "\n")

    return {"run_id": run_id, "output_dir": str(out_dir)}


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
        "resource_registry_commit": manifest["resource_registry_commit"],
    })
    checks["snapshot_bundle_hash_match"] = recomputed_bundle_hash == manifest["snapshot_bundle_hash"]

    checks["ok"] = all(checks.values())
    checks["run_id"] = run_id
    return checks
