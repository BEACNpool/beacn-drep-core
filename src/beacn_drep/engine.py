import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from .config import SOUL_REPO, RESOURCES_REPO, OUTPUT_DIR, AUDIT_LOG, MAX_STALE_SECONDS
from .routing import select_resources
from .adapters.git_adapter import commit_hash
from .replay import sha256_file, canonical_json_hash, csv_row_by_action, write_manifest, read_manifest


KNOWN_ACTION_TYPES = {
    "treasurywithdrawals", "treasury_withdrawal", "parameterchange", "parameter_change",
    "hardforkinitiaton", "hardforkinitiation", "hardfork", "infoaction", "info_action",
    "newconstitution", "new_constitution", "noconfidence", "updatecommittee", "newcommittee",
}


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


def _load_anchor_index() -> dict[str, dict]:
    path = RESOURCES_REPO / "data" / "input" / "governance" / "anchor_documents_index.csv"
    if not path.exists():
        return {}
    out = {}
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            aid = r.get("action_id", "")
            if aid:
                out[aid] = r
    return out


def _load_decision_support_csv(name: str) -> dict[str, dict]:
    path = RESOURCES_REPO / "data" / "input" / "governance" / "decision_support" / name
    if not path.exists():
        return {}
    out: dict[str, dict] = {}
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            aid = r.get("action_id", "")
            if aid:
                out[aid] = r
    return out


def _yn(v: str | None) -> bool | None:
    s = (v or "").strip().lower()
    if s in ("yes", "true", "1"):
        return True
    if s in ("no", "false", "0"):
        return False
    return None


def _load_treasury_flow() -> dict:
    p = RESOURCES_REPO / "data" / "history" / "governance_metrics" / "latest" / "treasury_flow_6m.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _load_treasury_doctrine() -> dict:
    p = SOUL_REPO / "treasury_spending_doctrine.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _doctrine_penalty(doctrine: dict, bucket: str, rule_id: str, default: float = 0.0) -> float:
    try:
        rows = doctrine.get("scoring_adjustments", {}).get(bucket, [])
        for r in rows:
            if r.get("id") == rule_id:
                if "penalty" in r:
                    return float(r["penalty"])
                if "bonus" in r:
                    return float(r["bonus"])
    except Exception:
        pass
    return default


def _check_freshness() -> dict:
    """Freshness check using best available snapshot timestamp.

    Preference order: manifest generated_at_utc, then governance CSV mtime, then
    decision-support dossier mtime. This prevents false staleness when datasets
    are intentionally updated without re-exporting the manifest.
    """
    candidates: list[tuple[str, datetime]] = []

    manifest_path = RESOURCES_REPO / "data" / "input" / "governance" / "governance_export_manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            gen_str = manifest.get("generated_at_utc", "")
            if gen_str:
                normalized = gen_str.replace("Z", "+00:00") if gen_str.endswith("Z") else gen_str
                gen_time = datetime.fromisoformat(normalized)
                if gen_time.tzinfo is None:
                    gen_time = gen_time.replace(tzinfo=timezone.utc)
                candidates.append(("manifest", gen_time))
        except Exception:
            pass

    for name, p in [
        ("governance_actions_all.csv", RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_all.csv"),
        ("deep_research_dossiers.csv", RESOURCES_REPO / "data" / "input" / "governance" / "decision_support" / "deep_research_dossiers.csv"),
    ]:
        if p.exists():
            try:
                mt = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
                candidates.append((name, mt))
            except Exception:
                pass

    if not candidates:
        return {"snapshot_age_seconds": -1, "max_allowed_seconds": MAX_STALE_SECONDS, "is_stale": True, "reason": "no freshness sources found"}

    source, snap_time = max(candidates, key=lambda x: x[1])
    now = datetime.now(timezone.utc)
    age_seconds = int((now - snap_time).total_seconds())
    return {
        "snapshot_age_seconds": age_seconds,
        "max_allowed_seconds": MAX_STALE_SECONDS,
        "is_stale": age_seconds > MAX_STALE_SECONDS,
        "snapshot_time": snap_time.isoformat().replace("+00:00", "Z"),
        "freshness_source": source,
    }


def _check_missing_evidence(action: dict) -> list[str]:
    missing = []
    action_type = (action.get("action_type") or "").lower()

    if not action.get("anchor_url"):
        missing.append("anchor_url is empty — no proposal metadata link available")
    if not action.get("anchor_hash"):
        missing.append("anchor_hash is empty — proposal integrity cannot be verified")

    if "treasury" in action_type:
        amt = action.get("treasury_amount_lovelace", "")
        if not amt or amt == "0" or amt == "":
            missing.append("treasury_amount_lovelace is missing for a treasury withdrawal")

    # proposer_address can be unavailable in current upstream snapshots; treat as non-critical.
    return missing


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

    if path.is_dir():
        # deterministic directory digest for pinned snapshot folders
        file_entries = []
        for p in sorted(path.rglob("*")):
            if p.is_file():
                file_entries.append({
                    "rel": str(p.relative_to(path)),
                    "sha256": sha256_file(p),
                })
        return {
            "resource_id": resource_row["resource_id"],
            "kind": "directory",
            "path": source_url,
            "files_count": len(file_entries),
            "dir_hash": canonical_json_hash(file_entries),
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


def _score_action(
    action: dict,
    flags: list[dict],
    freshness: dict,
    missing_evidence: list[str],
    anchor_ok: bool,
    readiness_row: dict | None = None,
    financial_row: dict | None = None,
    risk_row: dict | None = None,
    deep_row: dict | None = None,
    treasury_flow: dict | None = None,
    treasury_doctrine: dict | None = None,
) -> dict:
    action_type = (action.get("action_type") or "").lower()
    flag_score = _to_float(action.get("flag_score"))
    drep_yes = _to_float(action.get("drep_yes_pct"))
    drep_no = _to_float(action.get("drep_no_pct"))
    drep_abstain = _to_float(action.get("drep_abstain_pct"))

    facts = []
    inf = []
    unc = []

    # Freshness gate: stale data → forced ABSTAIN
    if freshness.get("is_stale"):
        age = freshness.get("snapshot_age_seconds", -1)
        reason = freshness.get("reason", f"data is {age}s old, max allowed is {freshness.get('max_allowed_seconds')}s")
        return {
            "recommendation": "ABSTAIN",
            "abstain_reason_code": "STALE_DATA",
            "score": 0.0,
            "confidence": 0.0,
            "facts": [f"Data freshness check failed: {reason}"],
            "inferences": ["Cannot produce reliable recommendation with stale data."],
            "uncertainty": ["All scoring suspended until fresh data is available."],
            "missing_evidence": [],
        }

    # Unknown action type → ABSTAIN
    action_type_normalized = action_type.replace("_", "").replace("-", "").replace(" ", "")
    if action_type_normalized and action_type_normalized not in KNOWN_ACTION_TYPES:
        return {
            "recommendation": "ABSTAIN",
            "abstain_reason_code": "UNKNOWN_ACTION_TYPE",
            "score": 0.0,
            "confidence": 0.1,
            "facts": [f"Action type '{action.get('action_type')}' is not in the known classification set."],
            "inferences": ["Cannot score an action type with no established rubric."],
            "uncertainty": ["This may be a new governance action type requiring doctrine update."],
            "missing_evidence": [f"No scoring rubric exists for action type: {action.get('action_type')}"],
        }

    # Missing evidence gate → NEEDS_MORE_INFO
    if missing_evidence:
        return {
            "recommendation": "NEEDS_MORE_INFO",
            "score": 0.0,
            "confidence": 0.1,
            "facts": ["Critical evidence fields are missing for this action."],
            "inferences": ["Cannot produce a responsible recommendation without baseline evidence."],
            "uncertainty": [f"Missing: {item}" for item in missing_evidence],
            "missing_evidence": missing_evidence,
        }

    # Deep-research gate for treasury proposals.
    if "treasury" in action_type:
        deep_ok = _yn((deep_row or {}).get("dossier_complete")) is True
        if not deep_ok:
            need = [
                "Deep research dossier is required for treasury actions before directional voting.",
                "Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.",
            ]
            return {
                "recommendation": "NEEDS_MORE_INFO",
                "needs_more_info_reason_code": "DEEP_RESEARCH_REQUIRED",
                "score": 0.0,
                "confidence": 0.2,
                "facts": ["Treasury actions are high-impact and require a completed deep research dossier."],
                "inferences": ["Directional voting is blocked until dossier quality gates pass."],
                "uncertainty": ["Dossier completeness not confirmed for this treasury proposal."],
                "missing_evidence": need,
            }

    score = 0.0

    if anchor_ok:
        score += 0.05
        facts.append("Pinned anchor document is available for this action.")
    else:
        unc.append("Anchor document is not yet pinned locally for this action.")

    # Conservative doctrine-aligned rule set
    if "treasury" in action_type:
        score -= 0.10
        facts.append("Treasury withdrawal actions require elevated scrutiny.")

        inflow = _to_float((treasury_flow or {}).get("treasury_fee_inflow_6m_lovelace"))
        outflow = _to_float((treasury_flow or {}).get("treasury_withdrawals_6m_lovelace"))
        if inflow > 0:
            ratio = outflow / inflow
            if ratio > 1.0:
                score += _doctrine_penalty(treasury_doctrine or {}, "treasury_withdrawals", "low_capacity_regime", -0.12)
                unc.append("Treasury outflow exceeded 6m treasury-fee inflow.")
            elif ratio > 0.8:
                score -= 0.06
                unc.append("Treasury outflow is close to 6m treasury-fee inflow.")
            else:
                score += 0.03
                inf.append("Treasury outflow remains below 6m treasury-fee inflow.")

        # Rolling-window concentration checks if NCL annual is provided.
        ncl_annual = _to_float(os.environ.get("BEACN_NCL_ANNUAL_LOVELACE"))
        if ncl_annual > 0:
            w73 = _to_float((treasury_flow or {}).get("withdrawals_73e_lovelace"))
            available = max(0.0, ncl_annual - w73)
            req = _to_float(action.get("treasury_amount_lovelace"))
            if available > 0 and req > 0:
                share = req / available
                if share > 0.50:
                    score += _doctrine_penalty(treasury_doctrine or {}, "treasury_withdrawals", "concentration_severe", -0.45)
                    unc.append("Proposal requests over 50% of rolling available capacity.")
                elif share > 0.30:
                    score += _doctrine_penalty(treasury_doctrine or {}, "treasury_withdrawals", "concentration_high", -0.25)
                    unc.append("Proposal requests over 30% of rolling available capacity.")

        # Milestone signal from decision-support financial profile.
        if financial_row and _yn(financial_row.get("milestone_payment_gates")) is False:
            score += _doctrine_penalty(treasury_doctrine or {}, "treasury_withdrawals", "no_milestones", -0.15)
            unc.append("No milestone-gated disbursement documented.")
    if "parameter" in action_type:
        score -= 0.05
        facts.append("Protocol parameter changes carry system-wide risk.")
    if "hardfork" in action_type:
        score -= 0.12
        facts.append("Hard fork actions require strongest evidence quality.")

    score -= min(flag_score / 30.0, 0.35)
    if flag_score > 0:
        facts.append(f"Flag score present ({int(flag_score)}), reducing confidence.")

    if drep_yes + drep_no + drep_abstain > 0:
        margin = (drep_yes - drep_no) / 100.0
        score += max(min(margin, 0.45), -0.45)
        inf.append("Network DRep distribution used as one signal, not authority.")
    else:
        unc.append("No DRep distribution available.")

    # Decision-support readiness enrichment (resources-side structured context)
    readiness_score = 0.0
    hard_blocker = False
    if readiness_row:
        if _yn(readiness_row.get("hard_blocker")) is True:
            hard_blocker = True
        if _yn(readiness_row.get("anchor_pinned")) is True or _yn(readiness_row.get("anchor_fallback_packet")) is True or anchor_ok:
            readiness_score += 0.15
        if _yn(readiness_row.get("action_metadata_complete")) is True and not missing_evidence:
            readiness_score += 0.15
        if _yn(readiness_row.get("timeline_defined")) is True:
            readiness_score += 0.10
        if _yn(readiness_row.get("governance_rules_clear")) is True:
            readiness_score += 0.10
        if _yn(readiness_row.get("risk_profile_complete")) is True:
            readiness_score += 0.15
        if _yn(readiness_row.get("drep_distribution_available")) is True or (drep_yes + drep_no + drep_abstain > 0):
            readiness_score += 0.10
        if financial_row:
            if _yn(financial_row.get("budget_granularity")) is True:
                readiness_score += 0.10
            if _yn(financial_row.get("milestone_payment_gates")) is True:
                readiness_score += 0.10
            if _yn(financial_row.get("sustainability_path_clear")) is True:
                readiness_score += 0.05
        if risk_row:
            if _yn(risk_row.get("mitigation_evidence_present")) is True:
                readiness_score += 0.05
            if _yn(risk_row.get("independent_assurance_present")) is True:
                readiness_score += 0.05

    readiness_score = max(0.0, min(1.0, readiness_score))

    # Recommendation thresholds
    treasury_doctrine_ready = ("treasury" in action_type) and (_yn((deep_row or {}).get("dossier_complete")) is True)
    treasury_ratio = None
    inflow = _to_float((treasury_flow or {}).get("treasury_fee_inflow_6m_lovelace"))
    outflow = _to_float((treasury_flow or {}).get("treasury_withdrawals_6m_lovelace"))
    if inflow > 0:
        treasury_ratio = outflow / inflow

    if hard_blocker:
        rec = "ABSTAIN"
        unc.append("Hard blocker present in vote-readiness matrix.")
    elif flag_score >= 9 and not (risk_row and _yn(risk_row.get("mitigation_evidence_present")) is True):
        rec = "ABSTAIN"
        unc.append("High risk flags triggered conservative abstain.")
    elif treasury_doctrine_ready and treasury_ratio is not None and treasury_ratio > 1.0:
        rec = "NO"
        inf.append("Directional NO forced: treasury outflow/inflow sustainability exceeded 1.0 with completed dossier.")
    elif score >= (0.06 if treasury_doctrine_ready else 0.12):
        rec = "YES"
    elif score <= (-0.06 if treasury_doctrine_ready else -0.12):
        rec = "NO"
    elif readiness_score >= 0.70 or treasury_doctrine_ready:
        # Force directional decision when structured evidence packet is sufficiently complete.
        rec = "YES" if score >= 0 else "NO"
        inf.append("Directional vote forced by completed readiness packet (treasury-aware).")
    else:
        rec = "ABSTAIN"

    confidence = max(0.0, min(1.0, 0.55 + abs(score) - (0.03 * len(flags))))
    reason_code = None
    if rec == "ABSTAIN":
        if hard_blocker:
            reason_code = "HARD_BLOCKER_PRESENT"
        elif flag_score >= 9 and not (risk_row and _yn(risk_row.get("mitigation_evidence_present")) is True):
            reason_code = "RISK_HIGH"
        elif not anchor_ok:
            reason_code = "CONTEXT_THIN_ANCHOR_UNPINNED"
        elif drep_yes + drep_no + drep_abstain == 0:
            reason_code = "DREP_DISTRIBUTION_MISSING"
        else:
            reason_code = "RULE_THRESHOLD_UNMET"
    return {
        "recommendation": rec,
        "abstain_reason_code": reason_code,
        "readiness_score": round(readiness_score, 4),
        "score": round(score, 4),
        "confidence": round(confidence, 4),
        "facts": facts or ["Deterministic rule set applied."],
        "inferences": inf or ["No additional inference."],
        "uncertainty": unc or ["Rule-based system; does not infer unstated intent."],
        "missing_evidence": [],
    }


def _enrich_decision_metadata(action: dict, score_obj: dict, resources_used: list[str], freshness: dict, missing_evidence: list[str]) -> dict:
    rec = (score_obj.get("recommendation") or "ABSTAIN").upper()
    score = float(score_obj.get("score", 0.0) or 0.0)
    confidence = float(score_obj.get("confidence", 0.0) or 0.0)

    # bounded probability-like distribution (deterministic, calibrated to avoid 0/1 overclaims)
    eps = 0.05
    lean = max(-0.45, min(0.45, score))
    p_yes = 0.34 + lean
    p_no = 0.34 - lean
    p_abstain = 0.32

    boost = max(0.0, min(0.25, confidence * 0.25))
    if rec == "YES":
        p_yes += boost
        p_no -= boost / 2
        p_abstain -= boost / 2
    elif rec == "NO":
        p_no += boost
        p_yes -= boost / 2
        p_abstain -= boost / 2
    elif rec in ("ABSTAIN", "NEEDS_MORE_INFO"):
        p_abstain += boost
        p_yes -= boost / 2
        p_no -= boost / 2

    p_yes = max(eps, p_yes)
    p_no = max(eps, p_no)
    p_abstain = max(eps, p_abstain)

    total = p_yes + p_no + p_abstain
    probs = {
        "YES": round(p_yes / total, 4),
        "NO": round(p_no / total, 4),
        "ABSTAIN": round(p_abstain / total, 4),
    }

    if confidence >= 0.80:
        band = "HIGH"
    elif confidence >= 0.55:
        band = "MEDIUM"
    else:
        band = "LOW"

    # simple evidence-depth heuristic for action-specific readiness
    depth = 0
    if action.get("anchor_url"):
        depth += 1
    if action.get("anchor_hash"):
        depth += 1
    if action.get("proposer_address"):
        depth += 1
    if action.get("treasury_amount_lovelace") not in (None, "", "0"):
        depth += 1
    depth += 1 if len(resources_used) >= 3 else 0
    if freshness.get("is_stale"):
        depth = max(0, depth - 2)
    depth = max(0, min(6, depth))

    return {
        "decision_probs": probs,
        "uncertainty_band": band,
        "evidence_depth_score": depth,
        "intelligence_profile": "deterministic-v1",
        "missing_evidence_count": len(missing_evidence),
    }


def run_once(action_id: str | None = None) -> dict:
    actions = _load_actions()
    action = next((a for a in actions if a["action_id"] == action_id), actions[0]) if action_id else actions[0]
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

    anchor_index = _load_anchor_index()
    anchor_ok = (anchor_index.get(action["action_id"], {}).get("fetch_status") == "ok")

    readiness_map = _load_decision_support_csv("vote_readiness_matrix.csv")
    financial_map = _load_decision_support_csv("financial_sustainability_profiles.csv")
    risk_map = _load_decision_support_csv("risk_mitigation_registry.csv")
    deep_map = _load_decision_support_csv("deep_research_dossiers.csv")
    treasury_flow = _load_treasury_flow()
    treasury_doctrine = _load_treasury_doctrine()

    freshness = _check_freshness()
    missing_evidence = _check_missing_evidence(action)
    score_obj = _score_action(
        action,
        flags_by_action.get(action["action_id"], []),
        freshness,
        missing_evidence,
        anchor_ok,
        readiness_map.get(action["action_id"]),
        financial_map.get(action["action_id"]),
        risk_map.get(action["action_id"]),
        deep_map.get(action["action_id"]),
        treasury_flow,
        treasury_doctrine,
    )
    intelligence = _enrich_decision_metadata(action, score_obj, resources_used, freshness, missing_evidence)

    rationale = {
        "action_id": action["action_id"],
        "action_type": action_type,
        "recommendation": score_obj["recommendation"],
        "abstain_reason_code": score_obj.get("abstain_reason_code"),
        "needs_more_info_reason_code": score_obj.get("needs_more_info_reason_code"),
        "score": score_obj["score"],
        "confidence": score_obj["confidence"],
        "readiness_score": score_obj.get("readiness_score"),
        "facts": score_obj["facts"],
        "inferences": score_obj["inferences"],
        "uncertainty": score_obj["uncertainty"],
        "missing_evidence": score_obj.get("missing_evidence", []),
        "input_hash": input_hash,
        "snapshot_bundle_hash": snapshot_bundle_hash,
        "soul_commit": soul_commit,
        "soul_text_hash": soul_text_hash,
        "resource_registry_commit": resources_commit,
        "resources_used": resources_used,
        "freshness": freshness,
        "decision_probs": intelligence["decision_probs"],
        "uncertainty_band": intelligence["uncertainty_band"],
        "evidence_depth_score": intelligence["evidence_depth_score"],
        "intelligence_profile": intelligence["intelligence_profile"],
        "missing_evidence_count": intelligence["missing_evidence_count"],
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

    missing_section = ""
    if score_obj.get("missing_evidence"):
        missing_section = "\n## Missing Evidence\n" + "\n".join(f"- {x}" for x in score_obj["missing_evidence"]) + "\n"

    freshness_note = ""
    if freshness.get("is_stale"):
        freshness_note = f"\n- **DATA STALE**: {freshness.get('reason', 'age exceeded threshold')}\n"

    (out_dir / "rationale.md").write_text(
        "\n".join([
            f"# Rationale: {action['action_id']}",
            f"Recommendation: **{score_obj['recommendation']}**",
            f"Score: `{score_obj['score']}` | Confidence: `{score_obj['confidence']}` | Readiness: `{score_obj.get('readiness_score', 0)}`",
            "",
            "## Facts",
            *[f"- {x}" for x in score_obj["facts"]],
            "",
            "## Inferences",
            *[f"- {x}" for x in score_obj["inferences"]],
            "",
            "## Uncertainty",
            *[f"- {x}" for x in score_obj["uncertainty"]],
            missing_section,
            "## Reproducibility",
            f"- input_hash: `{input_hash}`",
            f"- snapshot_bundle_hash: `{snapshot_bundle_hash}`",
            f"- soul_commit: `{soul_commit}`",
            f"- soul_text_hash: `{soul_text_hash}`",
            f"- resource_registry_commit: `{resources_commit}`",
            f"- resources_used: `{', '.join(resources_used)}`",
            f"- snapshot_age_seconds: `{freshness.get('snapshot_age_seconds', 'unknown')}`",
            f"- uncertainty_band: `{intelligence['uncertainty_band']}`",
            f"- evidence_depth_score: `{intelligence['evidence_depth_score']}`",
            f"- decision_probs: `{json.dumps(intelligence['decision_probs'], sort_keys=True)}`",
            freshness_note,
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
        "readiness_score": score_obj.get("readiness_score"),
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
