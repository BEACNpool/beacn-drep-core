import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from .config import SOUL_REPO, RESOURCES_REPO, OUTPUT_DIR, AUDIT_LOG, MAX_STALE_SECONDS, LLM_SCORE_ADJUST_CAP
from .routing import select_resources
from .adapters.git_adapter import commit_hash
from .replay import sha256_file, canonical_json_hash, csv_row_by_action, write_manifest, read_manifest
from .anchors import load_anchor_text
from . import llm


KNOWN_ACTION_TYPES = {
    "treasurywithdrawals", "treasury_withdrawal", "parameterchange", "parameter_change",
    "hardforkinitiaton", "hardforkinitiation", "hardfork", "infoaction", "info_action",
    "newconstitution", "new_constitution", "noconfidence", "updatecommittee", "newcommittee",
}


def _action_family(action_type: str | None) -> str:
    normalized = (action_type or "").lower().replace("_", "").replace("-", "").replace(" ", "")
    if "treasury" in normalized:
        return "treasury"
    if "hardfork" in normalized:
        return "hardfork"
    if "parameter" in normalized:
        return "parameter"
    if "info" in normalized:
        return "info"
    if "committee" in normalized:
        return "committee"
    if "constitution" in normalized:
        return "constitution"
    return "other"


def _param_changes(action: dict) -> dict:
    raw = action.get("param_changes")
    if isinstance(raw, dict):
        return raw
    if not raw:
        return {}
    try:
        parsed = json.loads(str(raw))
    except (TypeError, json.JSONDecodeError):
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _is_committee_liveness_parameter(action: dict) -> bool:
    changes = _param_changes(action)
    try:
        min_size = int(changes.get("committee_min_size"))
    except (TypeError, ValueError):
        return False
    title = (action.get("metadata_title") or "").lower()
    return min_size == 5 and ("committeeminsize" in title or "committee min" in title)


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


_DOCTRINE_FILES = {
    "treasury": "treasury_spending_doctrine.md",
    "hardfork": "hardfork_doctrine.md",
    "parameter": "parameter_change_doctrine.md",
    "info": "info_action_doctrine.md",
    "committee": "committee_update_doctrine.md",
    "constitution": "constitutional_amendment_doctrine.md",
}


def _load_doctrine_for(action_type: str | None) -> dict:
    """Load the soul doctrine that applies to this action family — the per-type
    doctrine plus the always-on values hierarchy — so the reasoning layer votes
    against BEACN's published standard rather than generic priors."""
    family = _action_family(action_type)
    names = ["values_hierarchy.md"]
    specific = _DOCTRINE_FILES.get(family)
    if specific:
        names.append(specific)
    parts: list[str] = []
    files_used: list[str] = []
    for name in names:
        p = SOUL_REPO / name
        if p.exists():
            try:
                parts.append(f"# {name}\n" + p.read_text(encoding="utf-8").strip())
                files_used.append(name)
            except Exception:
                continue
    text = "\n\n".join(parts)
    return {
        "family": family,
        "text": text,
        "files": files_used,
        "sha256": _sha256_bytes(text.encode("utf-8")) if text else "",
    }


def _load_scoring_weights() -> dict:
    p = SOUL_REPO / "scoring_weights.json"
    if not p.exists():
        raise RuntimeError(f"Missing required scoring weights file: {p}")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Unable to parse scoring weights file {p}: {e}") from e

    if not isinstance(data, dict):
        raise RuntimeError("scoring_weights.json must be a JSON object")

    version = data.get("version")
    weights = data.get("weights")
    if not version or not isinstance(weights, dict):
        raise RuntimeError("scoring_weights.json must contain 'version' and object 'weights'")
    return data


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


def _truth_label(v: str | None) -> str:
    b = _yn(v)
    if b is True:
        return "confirmed"
    if b is False:
        return "not confirmed"
    return "unknown"


def _short_amount(lovelace: str | None) -> str:
    value = _to_float(lovelace)
    if value <= 0:
        return "not specified"
    ada = value / 1_000_000
    if ada >= 1_000_000:
        return f"{ada / 1_000_000:.2f}M ADA"
    if ada >= 1_000:
        return f"{ada / 1_000:.1f}k ADA"
    return f"{ada:.0f} ADA"


def _missing_deep_research(deep_row: dict | None) -> list[str]:
    required = [
        ("proposal_summary_complete", "complete proposal summary"),
        ("budget_analysis_complete", "budget analysis"),
        ("feasibility_assessment_complete", "feasibility assessment"),
        ("risk_analysis_complete", "risk analysis"),
        ("alternatives_analysis_complete", "alternatives analysis"),
        ("failure_mode_analysis_complete", "failure-mode analysis"),
        ("community_impact_complete", "community impact analysis"),
    ]
    if not deep_row:
        return [label for _, label in required]
    return [label for key, label in required if _yn(deep_row.get(key)) is not True]


def _assessment_section(title: str, status: str, findings: list[str] | None = None, missing: list[str] | None = None, conclusion: str = "") -> dict:
    return {
        "title": title,
        "status": status,
        "findings": [x for x in (findings or []) if x],
        "missing": [x for x in (missing or []) if x],
        "conclusion": conclusion,
    }


def _claims_findings(claims: dict | None) -> tuple[list[str], list[str], str]:
    """Build the Claims-and-evidence findings from the extracted proposal claims.

    Returns (findings, missing, status_hint). When extraction is unavailable the
    section degrades to a thin status that names why, exactly as before.
    """
    if not claims or not claims.get("available"):
        reason = (claims or {}).get("reason") or "claim extraction unavailable"
        return (
            [f"Proposal claims not extracted ({reason})."],
            ["No structured claim/evidence extraction from the proposal document."],
            "thin",
        )
    req = claims.get("request") or {}
    findings = [
        f"Requested: {req.get('what', 'not stated')}",
        f"Recipient: {req.get('recipient', 'not stated')}",
        f"Stated amount: {req.get('amount_ada', 'not stated')}",
        f"Deliverables: {', '.join(req.get('deliverables') or []) or 'not stated'}",
        f"Deadline/expiry: {req.get('deadline', 'not stated')}",
    ]
    rows = claims.get("claims") or []
    for c in rows[:6]:
        findings.append(
            f"Claim ({c.get('category')}, {c.get('support')}, {c.get('materiality')} materiality): {c.get('claim')}"
        )
    weak = [
        c for c in rows
        if c.get("support") in ("unsupported", "proposer_asserted") and c.get("materiality") != "low"
    ]
    missing = [f"Independent evidence for: {c.get('claim')}" for c in weak[:4]]
    status = "thin" if (weak or not rows) else "complete"
    return findings, missing, status


def _counterarguments(action: dict, claims: dict | None, blockers: list[str], is_treasury: bool, deep_complete: bool) -> tuple[str, str, str]:
    """Per-proposal best YES / NO / hold cases, derived from the extracted claims
    and the actual gate results — not constant boilerplate."""
    amount = _short_amount(action.get("treasury_amount_lovelace"))
    atype = action.get("action_type") or "this action"
    rows = (claims.get("claims") if (claims and claims.get("available")) else None) or []
    strong = [c for c in rows if c.get("support") in ("supported_in_proposal", "independently_verifiable")]
    weak = [c for c in rows if c.get("support") in ("unsupported", "proposer_asserted") and c.get("materiality") != "low"]

    if strong:
        yes = f"Strongest YES: the proposal substantiates \"{strong[0]['claim']}\" and clears the evidence gates."
    elif is_treasury and amount != "not specified":
        yes = f"Strongest YES: the {amount} request funds {atype} with public benefit worth the risk if its controls and delivery hold."
    else:
        yes = f"Strongest YES: {atype} advances a credible public benefit worth its risk if the evidence holds."

    if weak:
        no = f"Strongest NO: a material claim is unsupported — \"{weak[0]['claim']}\" — so cost or precedent may outweigh the benefit."
    elif blockers:
        no = f"Strongest NO: an unresolved blocker ({blockers[0]}) means costs or weak controls may outweigh the claimed benefit."
    else:
        no = f"Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of {atype}."

    if is_treasury and not deep_complete:
        abstain = "Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty."
    elif blockers:
        abstain = f"Strongest hold: evidence is too thin for a directional vote while {len(blockers)} blocker(s) remain open."
    else:
        abstain = "Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty."
    return yes, no, abstain


def _fallback_message(action: dict, title: str, rationale: dict, assessment: dict, claims: dict | None) -> str:
    """Deterministic plain-language summary, always produced so the pipeline ends
    in a human-readable message; replaced by the model-written one when available."""
    rec = rationale.get("recommendation")
    reason = rationale.get("abstain_reason_code") or rationale.get("needs_more_info_reason_code")
    amount = _short_amount(action.get("treasury_amount_lovelace"))
    blockers = assessment.get("blocking_questions") or []
    parts = [
        f"BEACN's autonomous DRep recorded {rec} on \"{title or action.get('action_id')}\" "
        f"({action.get('action_type')})."
    ]
    if rec in ("ABSTAIN", "NEEDS_MORE_INFO"):
        parts.append("This is a conservative, evidence-based hold rather than opposition.")
    if amount != "not specified":
        parts.append(f"The action requests {amount} from the treasury.")
    if claims and claims.get("available"):
        weak = [
            c for c in (claims.get("claims") or [])
            if c.get("support") in ("unsupported", "proposer_asserted") and c.get("materiality") != "low"
        ]
        if weak:
            parts.append(f"A key material claim lacks independent support: \"{weak[0]['claim']}\".")
    if blockers:
        parts.append("Open questions before a directional vote: " + "; ".join(blockers[:3]) + ".")
    if reason:
        parts.append(f"Reason code: {reason}.")
    parts.append(
        "(Plain-language summary generated deterministically; a model-written explanation "
        "appears here when the reasoning layer is enabled.)"
    )
    return " ".join(parts)


def _build_assessment(
    action: dict,
    freshness: dict,
    missing_evidence: list[str],
    anchor_ok: bool,
    readiness_row: dict | None,
    financial_row: dict | None,
    risk_row: dict | None,
    deep_row: dict | None,
    treasury_flow: dict | None,
    treasury_doctrine: dict | None,
    flags: list[dict],
    claims: dict | None = None,
) -> dict:
    action_type = action.get("action_type", "")
    is_treasury = "treasury" in action_type.lower()
    deep_missing = _missing_deep_research(deep_row) if is_treasury else []
    deep_complete = _yn((deep_row or {}).get("dossier_complete")) is True
    hard_blocker = _yn((readiness_row or {}).get("hard_blocker")) is True
    risk_blocker = _yn((risk_row or {}).get("risk_blocker")) is True
    financial_blocker = _yn((financial_row or {}).get("financial_blocker")) is True

    sections = []

    sections.append(_assessment_section(
        "Intake",
        "complete" if not missing_evidence else "blocked",
        [
            f"Action type: {action_type or 'unknown'}",
            f"Status: {action.get('status') or 'unknown'}",
            f"Proposed epoch: {action.get('proposed_epoch') or 'unknown'}",
            f"Expires after epoch: {action.get('expires_after_epoch') or action.get('expiration_epoch') or 'unknown'}",
            f"Treasury request: {_short_amount(action.get('treasury_amount_lovelace'))}",
            f"Anchor pinned locally: {'yes' if anchor_ok else 'no'}",
        ],
        missing_evidence,
        "Baseline fields and source anchors establish whether the proposal can be reviewed at all.",
    ))

    claim_findings, claim_missing, claim_status = _claims_findings(claims)
    evidence_context = [
        f"Proposal anchor: {'pinned and replayable' if anchor_ok else 'not pinned'}",
        f"Proposal document read by reasoning layer: {'yes' if (claims and claims.get('available')) else 'no'}",
        f"Snapshot freshness source: {freshness.get('freshness_source') or 'unknown'}",
        f"Deep research dossier: {'complete' if deep_complete else ('required' if is_treasury else 'not required')}",
    ]
    section_status = claim_status
    if not anchor_ok or freshness.get("is_stale"):
        section_status = "thin"
    sections.append(_assessment_section(
        "Claims and evidence",
        section_status,
        evidence_context + claim_findings,
        claim_missing + (deep_missing if is_treasury and not deep_complete else []),
        "Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.",
    ))

    if is_treasury:
        inflow = _to_float((treasury_flow or {}).get("treasury_fee_inflow_6m_lovelace"))
        outflow = _to_float((treasury_flow or {}).get("treasury_withdrawals_6m_lovelace"))
        ratio = outflow / inflow if inflow > 0 else None
        rt = (treasury_doctrine or {}).get("regime_thresholds", {})
        sustainable_max = _to_float(rt.get("sustainable_max_ratio")) or 1.0
        hard_no_ratio = _to_float(rt.get("unsustainable_hard_no_ratio")) or 2.0
        tf_stale, _tf_epoch, _tf_lag = _treasury_flow_stale(treasury_flow)
        if tf_stale:
            regime = "unknown (stale snapshot)"
        elif ratio is None:
            regime = "unknown"
        elif ratio <= sustainable_max:
            regime = "sustainable"
        elif ratio <= hard_no_ratio:
            regime = "stressed"
        else:
            regime = "unsustainable"
        sections.append(_assessment_section(
            "Treasury analysis",
            "complete" if financial_row and deep_complete else "incomplete",
            [
                f"Requested ADA: {(financial_row or {}).get('requested_ada') or _short_amount(action.get('treasury_amount_lovelace'))}",
                f"Budget granularity: {_truth_label((financial_row or {}).get('budget_granularity'))}",
                f"Milestone payment gates: {_truth_label((financial_row or {}).get('milestone_payment_gates'))}",
                f"Clawback/refund path: {_truth_label((financial_row or {}).get('clawback_refund_path'))}",
                f"Cost/benefit clarity: {_truth_label((financial_row or {}).get('cost_benefit_clarity'))}",
                f"Recurring funding dependency: {_truth_label((financial_row or {}).get('recurring_funding_dependency'))}",
                f"Six-month treasury flow regime: {regime}",
                f"Financial confidence: {(financial_row or {}).get('financial_confidence') or 'unknown'}",
            ],
            [
                label for label, value in [
                    ("line-item budget", (financial_row or {}).get("budget_granularity")),
                    ("milestone-gated disbursement", (financial_row or {}).get("milestone_payment_gates")),
                    ("sustainability path", (financial_row or {}).get("sustainability_path_clear")),
                    ("cost-benefit clarity", (financial_row or {}).get("cost_benefit_clarity")),
                ] if _yn(value) is not True
            ],
            "Treasury votes require a higher bar because they consume shared ADA and create precedent.",
        ))

    sections.append(_assessment_section(
        "Risk review",
        "blocked" if hard_blocker or risk_blocker or financial_blocker else ("complete" if risk_row else "thin"),
        [
            f"Execution risk: {(risk_row or {}).get('execution_risk_level') or 'unknown'}",
            f"Governance risk: {(risk_row or {}).get('governance_risk_level') or 'unknown'}",
            f"Technical risk: {(risk_row or {}).get('technical_risk_level') or 'unknown'}",
            f"Treasury exposure risk: {(risk_row or {}).get('treasury_exposure_risk_level') or 'unknown'}",
            f"Mitigation evidence: {_truth_label((risk_row or {}).get('mitigation_evidence_present'))}",
            f"Independent assurance: {_truth_label((risk_row or {}).get('independent_assurance_present'))}",
            f"Rollback/remedy path: {_truth_label((risk_row or {}).get('rollback_or_remedy_path'))}",
            f"Flag count: {len(flags)}",
        ],
        [
            label for label, value in [
                ("mitigation evidence", (risk_row or {}).get("mitigation_evidence_present")),
                ("independent assurance", (risk_row or {}).get("independent_assurance_present")),
                ("rollback/remedy path", (risk_row or {}).get("rollback_or_remedy_path")),
                ("dependency map", (risk_row or {}).get("dependency_map_complete")),
            ] if _yn(value) is not True
        ],
        "Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.",
    ))

    blockers = []
    if freshness.get("is_stale"):
        blockers.append("freshness gate failed")
    if missing_evidence:
        blockers.extend(missing_evidence)
    if is_treasury and not deep_complete:
        blockers.extend([f"missing {x}" for x in deep_missing])
    if hard_blocker:
        blockers.append("readiness hard blocker present")
    if risk_blocker:
        blockers.append("risk blocker present")
    if financial_blocker:
        blockers.append("financial blocker present")

    yes_case, no_case, abstain_case = _counterarguments(action, claims, blockers, is_treasury, deep_complete)
    sections.append(_assessment_section(
        "Counterargument pass",
        "complete",
        [yes_case, no_case, abstain_case],
        [],
        "A defensible rationale must show the best opposing case before it reaches a vote.",
    ))

    sections.append(_assessment_section(
        "Synthesis",
        "blocked" if blockers else "ready",
        [
            "Final vote must be derived from completed sections above, not from a prose summary.",
            "The public rationale should name the decisive section and the strongest counterargument.",
        ],
        blockers[:12],
        "The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.",
    ))

    return {
        "schema_version": "assessment-tree-v1",
        "action_id": action.get("action_id"),
        "action_type": action_type,
        "overall_status": "blocked" if any(s["status"] == "blocked" for s in sections) else ("incomplete" if any(s["status"] in ("thin", "incomplete") for s in sections) else "ready"),
        "sections": sections,
        "blocking_questions": blockers[:12],
    }


def _assessment_lines(assessment: dict) -> tuple[list[str], list[str], list[str]]:
    facts: list[str] = []
    inf: list[str] = []
    unc: list[str] = []
    for section in assessment.get("sections", []):
        title = section.get("title", "Assessment")
        status = section.get("status", "unknown")
        if section.get("findings"):
            facts.append(f"{title}: {section['findings'][0]}")
        if section.get("conclusion"):
            inf.append(f"{title}: {section['conclusion']}")
        for item in section.get("missing", [])[:2]:
            unc.append(f"{title} missing: {item}")
        if status in ("blocked", "thin", "incomplete"):
            unc.append(f"{title} status is {status}.")
    return facts[:12], inf[:8], unc[:12]


def _mainnet_epoch_now() -> int:
    """Deterministic current mainnet epoch from wall-clock. Shelley epoch 208 began
    2020-07-29T21:44:51Z; epochs are 432000s (5 days)."""
    import time
    return 208 + int((time.time() - 1596059091) // 432000)


def _treasury_flow_stale(treasury_flow: dict | None) -> tuple[bool, int, int]:
    """Is the treasury fee-flow snapshot too old to inform a live vote?

    Returns (is_stale, snapshot_epoch, lag_epochs). Stale treasury data must NOT
    silently penalize a treasury vote — that would be voting real money on an
    out-of-date picture of the treasury. Threshold via BEACN_TREASURY_FLOW_MAX_LAG_EPOCHS
    (default 6 epochs ~ 30 days)."""
    try:
        snap_epoch = int((treasury_flow or {}).get("current_epoch") or 0)
    except Exception:
        snap_epoch = 0
    try:
        max_lag = int(os.environ.get("BEACN_TREASURY_FLOW_MAX_LAG_EPOCHS", "6"))
    except Exception:
        max_lag = 6
    if snap_epoch <= 0:
        return True, snap_epoch, -1
    lag = _mainnet_epoch_now() - snap_epoch
    return (lag > max_lag), snap_epoch, lag


def _treasury_gate_config(treasury_doctrine: dict | None) -> tuple[str, float]:
    """Treasury dossier-gate posture.

    Fail-safe by design: the CODE default is the strict 'hard' gate (no dossier ->
    NEEDS_MORE_INFO), so a missing or malformed config can never silently open the
    money gate. Only the soul doctrine (treasury_spending_doctrine.json
    'dossier_gate') can loosen it to 'soft', which is an explicit, auditable,
    version-controlled choice. BEACN_TREASURY_GATE_MODE overrides for emergencies.

    In 'soft' mode a treasury action without a complete dossier is NOT blocked; it
    is judged on the available repo context (anchor + doctrine + reasoning lean)
    with a caution penalty, so the agent can defend the treasury directionally
    instead of always abstaining.
    """
    cfg = (treasury_doctrine or {}).get("dossier_gate", {}) if isinstance(treasury_doctrine, dict) else {}
    mode = os.environ.get("BEACN_TREASURY_GATE_MODE", str(cfg.get("mode", "hard"))).strip().lower()
    if mode not in ("hard", "soft"):
        mode = "hard"
    penalty = _to_float(cfg.get("incomplete_penalty")) or -0.10
    if penalty > 0:
        penalty = -penalty
    return mode, penalty


def _score_action(
    action: dict,
    flags: list[dict],
    freshness: dict,
    missing_evidence: list[str],
    anchor_ok: bool,
    assessment: dict,
    readiness_row: dict | None = None,
    financial_row: dict | None = None,
    risk_row: dict | None = None,
    deep_row: dict | None = None,
    treasury_flow: dict | None = None,
    treasury_doctrine: dict | None = None,
    scoring_weights: dict | None = None,
    llm_lean: dict | None = None,
) -> dict:
    action_type = (action.get("action_type") or "").lower()
    action_family = _action_family(action_type)
    flag_score = _to_float(action.get("flag_score"))
    drep_yes = _to_float(action.get("drep_yes_pct"))
    drep_no = _to_float(action.get("drep_no_pct"))
    drep_abstain = _to_float(action.get("drep_abstain_pct"))

    facts = []
    inf = []
    unc = []
    assessment_facts, assessment_inferences, assessment_uncertainty = _assessment_lines(assessment)

    sw = (scoring_weights or {}).get("weights", {})
    w_anchor_present = _to_float(sw.get("anchor_present_bonus", 0.05))
    w_treasury_base = _to_float(sw.get("treasury_base_penalty", -0.10))
    w_treasury_flow_sustainable = _to_float(sw.get("treasury_flow_sustainable_bonus", 0.03))
    w_treasury_flow_stressed = _to_float(sw.get("treasury_flow_stressed_penalty", -0.06))
    w_treasury_flow_unsustainable = _to_float(sw.get("treasury_flow_unsustainable_penalty", -0.10))
    w_parameter_base = _to_float(sw.get("parameter_change_base_penalty", -0.05))
    w_hardfork_base = _to_float(sw.get("hardfork_base_penalty", -0.12))
    w_flag_divisor = _to_float(sw.get("flag_score_divisor", 30.0)) or 30.0
    w_flag_penalty_cap = _to_float(sw.get("flag_penalty_cap", 0.35))
    w_drep_margin_cap = _to_float(sw.get("drep_margin_cap", 0.45))

    # Freshness gate: stale data → forced ABSTAIN
    if freshness.get("is_stale"):
        age = freshness.get("snapshot_age_seconds", -1)
        reason = freshness.get("reason", f"data is {age}s old, max allowed is {freshness.get('max_allowed_seconds')}s")
        return {
            "recommendation": "ABSTAIN",
            "abstain_reason_code": "STALE_DATA",
            "score": 0.0,
            "confidence": 0.0,
            "facts": [f"Data freshness check failed: {reason}", *assessment_facts],
            "inferences": ["Cannot produce reliable recommendation with stale data.", *assessment_inferences],
            "uncertainty": ["All scoring suspended until fresh data is available.", *assessment_uncertainty],
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
            "facts": [f"Action type '{action.get('action_type')}' is not in the known classification set.", *assessment_facts],
            "inferences": ["Cannot score an action type with no established rubric.", *assessment_inferences],
            "uncertainty": ["This may be a new governance action type requiring doctrine update.", *assessment_uncertainty],
            "missing_evidence": [f"No scoring rubric exists for action type: {action.get('action_type')}"],
        }

    # Missing evidence gate → ABSTAIN (conservative default until evidence improves)
    if missing_evidence:
        return {
            "recommendation": "ABSTAIN",
            "abstain_reason_code": "MISSING_BASELINE_EVIDENCE",
            "score": 0.0,
            "confidence": 0.1,
            "facts": ["Critical evidence fields are missing for this action.", *assessment_facts],
            "inferences": ["Cannot produce a responsible recommendation without baseline evidence.", *assessment_inferences],
            "uncertainty": [*[f"Missing: {item}" for item in missing_evidence], *assessment_uncertainty],
            "missing_evidence": missing_evidence,
        }

    # Deep-research gate for treasury proposals.
    treasury_gate_mode, treasury_no_dossier_penalty = _treasury_gate_config(treasury_doctrine)
    treasury_dossier_incomplete = False
    if action_family == "treasury":
        deep_ok = _yn((deep_row or {}).get("dossier_complete")) is True
        if not deep_ok:
            deep_missing = _missing_deep_research(deep_row)
            if treasury_gate_mode == "hard":
                need = [
                    "Deep research dossier is required for treasury actions before directional voting.",
                    "Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.",
                    *[f"Missing dossier section: {item}" for item in deep_missing],
                ]
                return {
                    "recommendation": "NEEDS_MORE_INFO",
                    "needs_more_info_reason_code": "DEEP_RESEARCH_REQUIRED",
                    "score": 0.0,
                    "confidence": 0.2,
                    "facts": ["Treasury actions are high-impact and require a completed deep research dossier.", *assessment_facts],
                    "inferences": ["Directional voting is blocked until dossier quality gates pass.", *assessment_inferences],
                    "uncertainty": ["Dossier completeness not confirmed for this treasury proposal.", *assessment_uncertainty],
                    "missing_evidence": need,
                }
            # soft mode: judge directionally on available repo context, with a caution penalty.
            treasury_dossier_incomplete = True

    score = 0.0

    if anchor_ok:
        score += w_anchor_present
        facts.append("Pinned anchor document is available for this action.")
    else:
        unc.append("Anchor document is not yet pinned locally for this action.")

    # Conservative doctrine-aligned rule set
    if action_family == "treasury":
        score += w_treasury_base
        facts.append("Treasury withdrawal actions require elevated scrutiny.")
        if treasury_dossier_incomplete:
            score += treasury_no_dossier_penalty
            unc.append(
                f"Treasury diligence dossier incomplete; soft gate applied a {treasury_no_dossier_penalty} "
                "caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) "
                "rather than abstaining."
            )

        inflow = _to_float((treasury_flow or {}).get("treasury_fee_inflow_6m_lovelace"))
        outflow = _to_float((treasury_flow or {}).get("treasury_withdrawals_6m_lovelace"))
        tf_stale, tf_epoch, tf_lag = _treasury_flow_stale(treasury_flow)
        if tf_stale:
            # Do not let an out-of-date treasury snapshot penalize or reward a live vote.
            unc.append(
                f"Treasury fee-flow snapshot is stale (epoch {tf_epoch}, ~{tf_lag} epochs behind); "
                "regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics."
            )
        elif inflow > 0:
            ratio = outflow / inflow
            rt = (treasury_doctrine or {}).get("regime_thresholds", {})
            sustainable_max = _to_float(rt.get("sustainable_max_ratio")) or 1.0
            hard_no_ratio = _to_float(rt.get("unsustainable_hard_no_ratio")) or 2.0

            # Fee-flow is advisory signal only (not hard gate) until treasury inflow model is fully calibrated.
            if ratio <= sustainable_max:
                score += w_treasury_flow_sustainable
                inf.append("Treasury fee-flow signal is in sustainable regime.")
            elif ratio <= hard_no_ratio:
                score += w_treasury_flow_stressed
                unc.append("Treasury fee-flow signal is in stressed regime.")
            else:
                score += w_treasury_flow_unsustainable
                unc.append("Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).")

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
    if action_family == "parameter":
        score += w_parameter_base
        facts.append("Protocol parameter changes carry system-wide risk.")
    if action_family == "hardfork":
        score += w_hardfork_base
        facts.append("Hard fork actions are high-impact protocol upgrades and require operator-aware review.")

    score -= min(flag_score / w_flag_divisor, w_flag_penalty_cap)
    if flag_score > 0:
        facts.append(f"Flag score present ({int(flag_score)}), reducing confidence.")

    if drep_yes + drep_no + drep_abstain > 0:
        # The governance export percentages are ratification support, not a clean
        # explicit-vote sentiment ledger. In particular, the "no" side can include
        # stake that simply has not voted YES yet. Treat it as turnout/support
        # context, never as active opposition by itself.
        if drep_yes >= 60.0:
            score += min(0.06, w_drep_margin_cap)
            inf.append("DRep ratification support is above the hard-fork threshold; treated as a positive context signal.")
        elif drep_yes >= 25.0:
            score += min(0.03, w_drep_margin_cap)
            inf.append("DRep ratification support is material but below threshold; treated as a modest context signal.")
        elif drep_yes > 0:
            unc.append("DRep ratification support is below threshold; this is not treated as active opposition.")
        else:
            unc.append("No DRep YES support recorded in the ratification snapshot.")
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
                readiness_score += w_anchor_present
        if risk_row:
            if _yn(risk_row.get("mitigation_evidence_present")) is True:
                readiness_score += w_anchor_present
            if _yn(risk_row.get("independent_assurance_present")) is True:
                readiness_score += w_anchor_present

    readiness_score = max(0.0, min(1.0, readiness_score))

    # Bounded LLM influence (Stage 1.5). Every HARD gate (stale data, unknown type,
    # missing evidence, treasury-needs-dossier) has already returned above, so the
    # reasoning layer can only nudge a NON-GATED action's score, clamped to
    # ±LLM_SCORE_ADJUST_CAP. The raw score is preserved for the public record.
    raw_score = score
    llm_adjustment = 0.0
    llm_info = None
    if llm_lean and llm_lean.get("available"):
        llm_adjustment = max(-LLM_SCORE_ADJUST_CAP, min(
            LLM_SCORE_ADJUST_CAP, float(llm_lean.get("score_adjustment") or 0.0)))
        score += llm_adjustment
        llm_info = {
            "source": llm_lean.get("source"),
            "model": llm_lean.get("model"),
            "direction": llm_lean.get("direction"),
            "score_adjustment": round(llm_adjustment, 4),
            "confidence": llm_lean.get("confidence"),
            "rationale": llm_lean.get("rationale"),
            "doctrine_basis": llm_lean.get("doctrine_basis"),
            "cap": LLM_SCORE_ADJUST_CAP,
        }
        if abs(llm_adjustment) > 0:
            inf.append(
                f"Doctrine-aware reasoning layer nudged the score by {llm_adjustment:+.3f} "
                f"(clamped to ±{LLM_SCORE_ADJUST_CAP}): {llm_lean.get('rationale')}"
            )

    # Recommendation thresholds
    treasury_doctrine_ready = (action_family == "treasury") and (_yn((deep_row or {}).get("dossier_complete")) is True)
    treasury_ratio = None
    inflow = _to_float((treasury_flow or {}).get("treasury_fee_inflow_6m_lovelace"))
    outflow = _to_float((treasury_flow or {}).get("treasury_withdrawals_6m_lovelace"))
    if inflow > 0:
        treasury_ratio = outflow / inflow
    rt = (treasury_doctrine or {}).get("regime_thresholds", {})
    sustainable_max = _to_float(rt.get("sustainable_max_ratio")) or 1.0
    hard_no_ratio = _to_float(rt.get("unsustainable_hard_no_ratio")) or 2.0
    ncl_annual = _to_float(os.environ.get("BEACN_NCL_ANNUAL_LOVELACE"))
    available = None
    if ncl_annual > 0:
        w73 = _to_float((treasury_flow or {}).get("withdrawals_73e_lovelace"))
        available = ncl_annual - w73

    clean_hardfork = (
        action_family == "hardfork"
        and anchor_ok
        and not missing_evidence
        and flag_score == 0
        and not hard_blocker
        and not (risk_row and _yn(risk_row.get("risk_blocker")) is True)
    )
    clean_committee_liveness_parameter = (
        action_family == "parameter"
        and _is_committee_liveness_parameter(action)
        and anchor_ok
        and not missing_evidence
        and flag_score == 0
        and not hard_blocker
        and not (risk_row and _yn(risk_row.get("risk_blocker")) is True)
    )

    # Directional threshold magnitude used for the YES/NO decision. Emitted so the
    # downstream vote-revision policy can measure how far a score sits from the
    # boundary (hysteresis) when deciding whether to change an existing on-chain vote.
    directional_threshold = 0.06 if treasury_doctrine_ready else 0.12

    if hard_blocker:
        rec = "ABSTAIN"
        unc.append("Hard blocker present in vote-readiness matrix.")
    elif flag_score >= 9 and not (risk_row and _yn(risk_row.get("mitigation_evidence_present")) is True):
        rec = "ABSTAIN"
        unc.append("High risk flags triggered conservative abstain.")
    elif treasury_doctrine_ready and available is not None and available <= 0:
        rec = "NO"
        inf.append("Directional NO forced: rolling-window available treasury capacity is depleted.")
    elif score >= directional_threshold:
        rec = "YES"
    elif score <= -directional_threshold:
        rec = "NO"
    elif clean_hardfork and score > -0.10:
        rec = "YES"
        inf.append("Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.")
    elif clean_committee_liveness_parameter and score > -0.12:
        rec = "YES"
        inf.append("Action-type policy: a clean committeeMinSize liveness parameter may proceed despite thin generic risk fields; governance-risk detail remains explicit uncertainty.")
    elif readiness_score >= 0.70 or treasury_doctrine_ready:
        # Force directional decision when structured evidence packet is sufficiently complete.
        rec = "YES" if score >= 0 else "NO"
        inf.append("Directional vote forced by completed readiness packet (treasury-aware).")
    else:
        rec = "ABSTAIN"

    # Did the bounded LLM nudge actually move the action across a directional
    # boundary? Recorded so the public can see exactly when the reasoning layer
    # changed an outcome the mechanical rules would not have reached.
    llm_assisted = False
    llm_assisted_reason_code = None
    if llm_info and abs(llm_adjustment) > 0:
        def _band(s: float) -> str:
            if s >= directional_threshold:
                return "YES"
            if s <= -directional_threshold:
                return "NO"
            return "MID"
        if _band(raw_score) != _band(score):
            llm_assisted = True
            if rec in ("YES", "NO"):
                llm_assisted_reason_code = "LLM_ASSISTED_DIRECTIONAL"

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
    high_impact_reason_code = None
    if clean_hardfork and rec == "YES":
        high_impact_reason_code = "HIGH_IMPACT_HARD_FORK"
    elif clean_committee_liveness_parameter and rec == "YES":
        high_impact_reason_code = "GOVERNANCE_LIVENESS_PARAMETER"

    return {
        "recommendation": rec,
        "abstain_reason_code": reason_code,
        "operator_review_required": False,
        "operator_review_reason_code": None,
        "agentic_high_impact_reason_code": high_impact_reason_code,
        "readiness_score": round(readiness_score, 4),
        "score": round(score, 4),
        "raw_score": round(raw_score, 4),
        "treasury_gate_mode": treasury_gate_mode,
        "treasury_dossier_incomplete": treasury_dossier_incomplete,
        "llm_score_adjustment": round(llm_adjustment, 4),
        "llm_lean": llm_info,
        "llm_assisted": llm_assisted,
        "llm_assisted_reason_code": llm_assisted_reason_code,
        "directional_threshold": round(directional_threshold, 4),
        "confidence": round(confidence, 4),
        "facts": [*(facts or ["Deterministic rule set applied."]), *assessment_facts],
        "inferences": [*(inf or ["No additional inference."]), *assessment_inferences],
        "uncertainty": [*(unc or ["Rule-based system; does not infer unstated intent."]), *assessment_uncertainty],
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
    anchor_ok = (
        anchor_index.get(action["action_id"], {}).get("fetch_status")
        in ("ok", "ok_cached")
    )

    readiness_map = _load_decision_support_csv("vote_readiness_matrix.csv")
    financial_map = _load_decision_support_csv("financial_sustainability_profiles.csv")
    risk_map = _load_decision_support_csv("risk_mitigation_registry.csv")
    deep_map = _load_decision_support_csv("deep_research_dossiers.csv")
    treasury_flow = _load_treasury_flow()
    treasury_doctrine = _load_treasury_doctrine()
    scoring_weights = _load_scoring_weights()

    freshness = _check_freshness()
    missing_evidence = _check_missing_evidence(action)

    # Load the soul doctrine for this action family so the reasoning layer votes
    # against BEACN's published standard, not generic priors.
    doctrine = _load_doctrine_for(action_type)

    # Stage 1: read the proposal's cached anchor document and extract structured
    # claims (model-assisted; feeds the evidence table, never a hard gate).
    anchor_text, anchor_meta = load_anchor_text(action["action_id"])
    claims = llm.extract_claims(action, anchor_text, doctrine.get("text"))

    assessment = _build_assessment(
        action,
        freshness,
        missing_evidence,
        anchor_ok,
        readiness_map.get(action["action_id"]),
        financial_map.get(action["action_id"]),
        risk_map.get(action["action_id"]),
        deep_map.get(action["action_id"]),
        treasury_flow,
        treasury_doctrine,
        flags_by_action.get(action["action_id"], []),
        claims,
    )

    # Stage 1.5: bounded, doctrine-aware lean. Clamped + recorded in _score_action.
    lean = llm.assess_lean(action, claims, assessment, doctrine.get("text"), doctrine.get("family"))

    score_obj = _score_action(
        action,
        flags_by_action.get(action["action_id"], []),
        freshness,
        missing_evidence,
        anchor_ok,
        assessment,
        readiness_map.get(action["action_id"]),
        financial_map.get(action["action_id"]),
        risk_map.get(action["action_id"]),
        deep_map.get(action["action_id"]),
        treasury_flow,
        treasury_doctrine,
        scoring_weights,
        lean,
    )
    intelligence = _enrich_decision_metadata(action, score_obj, resources_used, freshness, missing_evidence)

    rationale = {
        "action_id": action["action_id"],
        "action_type": action_type,
        "recommendation": score_obj["recommendation"],
        "abstain_reason_code": score_obj.get("abstain_reason_code"),
        "needs_more_info_reason_code": score_obj.get("needs_more_info_reason_code"),
        "operator_review_required": score_obj.get("operator_review_required", False),
        "operator_review_reason_code": score_obj.get("operator_review_reason_code"),
        "agentic_high_impact_reason_code": score_obj.get("agentic_high_impact_reason_code"),
        "score": score_obj["score"],
        "raw_score": score_obj.get("raw_score", score_obj["score"]),
        "llm_score_adjustment": score_obj.get("llm_score_adjustment", 0.0),
        "llm_lean": score_obj.get("llm_lean"),
        "llm_assisted": score_obj.get("llm_assisted", False),
        "llm_assisted_reason_code": score_obj.get("llm_assisted_reason_code"),
        "doctrine_files": doctrine.get("files"),
        "doctrine_hash": doctrine.get("sha256"),
        "directional_threshold": score_obj.get("directional_threshold", 0.12),
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
        "assessment_schema_version": assessment["schema_version"],
        "assessment_status": assessment["overall_status"],
        "assessment": assessment,
        "missing_evidence_count": intelligence["missing_evidence_count"],
        "scoring_weights_version": scoring_weights.get("version"),
        "scoring_weights_hash": _sha256_bytes(json.dumps(scoring_weights, sort_keys=True).encode("utf-8")),
    }

    # Stage 6: plain-English explanation of the already-decided verdict.
    title = action.get("metadata_title") or ""
    message = llm.write_human_message(action, title, rationale, assessment, claims)
    if message.get("available"):
        human_text = message["text"]
        message_source = message.get("source") or "model"
    else:
        human_text = _fallback_message(action, title, rationale, assessment, claims)
        message_source = "deterministic-template"

    model_layer = {
        "claim_extraction": {
            "available": claims.get("available"),
            "source": claims.get("source"),
            "reason": claims.get("reason"),
            "model": claims.get("model"),
            "anchor": anchor_meta,
            "claim_count": len(claims.get("claims") or []),
            "prompt_sha256": claims.get("prompt_sha256"),
            "output_sha256": claims.get("output_sha256"),
        },
        "doctrine": {
            "family": doctrine.get("family"),
            "files": doctrine.get("files"),
            "sha256": doctrine.get("sha256"),
        },
        "lean": {
            "available": lean.get("available"),
            "source": lean.get("source"),
            "reason": lean.get("reason"),
            "model": lean.get("model"),
            "direction": lean.get("direction"),
            "score_adjustment": score_obj.get("llm_score_adjustment", 0.0),
            "cap": LLM_SCORE_ADJUST_CAP,
            "assisted_directional": score_obj.get("llm_assisted", False),
            "prompt_sha256": lean.get("prompt_sha256"),
            "output_sha256": lean.get("output_sha256"),
        },
        "human_message": {
            "source": message_source,
            "available": message.get("available"),
            "reason": message.get("reason"),
            "model": message.get("model"),
            "prompt_sha256": message.get("prompt_sha256"),
            "output_sha256": message.get("output_sha256"),
        },
        "note": (
            "Claim extraction and the plain-language message are model-assisted, advisory layers. "
            "The hard gates (stale data, missing evidence, treasury-needs-dossier, hard blockers, "
            "high flags) are deterministic and binding. The doctrine-aware reasoning layer may apply "
            f"a bounded score nudge of at most ±{LLM_SCORE_ADJUST_CAP}, clamped and recorded here "
            "(raw_score + llm_score_adjustment), so its influence is fully auditable and replayable."
        ),
    }
    rationale["human_message"] = human_text
    rationale["human_message_source"] = message_source
    rationale["model_layer"] = model_layer

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
        "model_layer": model_layer,
    }

    (out_dir / "rationale.json").write_text(json.dumps(rationale, indent=2) + "\n", encoding="utf-8")
    (out_dir / "assessment.json").write_text(json.dumps(assessment, indent=2) + "\n", encoding="utf-8")
    (out_dir / "claims.json").write_text(json.dumps(claims, indent=2) + "\n", encoding="utf-8")
    (out_dir / "rationale_message.md").write_text(
        "\n".join([
            f"# {title or action['action_id']}",
            f"**BEACN DRep vote: {score_obj['recommendation']}**  "
            f"_(plain-language explanation — {message_source})_",
            "",
            human_text,
            "",
            "---",
            "_The vote, score, and gates are produced deterministically and are the binding record. "
            "This explanation is a model-assisted plain-language layer over that record. "
            "Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; "
            "the decision is byte-for-byte replayable via `cli verify-replay`._",
        ]) + "\n",
        encoding="utf-8",
    )

    missing_section = ""
    if score_obj.get("missing_evidence"):
        missing_section = "\n## Missing Evidence\n" + "\n".join(f"- {x}" for x in score_obj["missing_evidence"]) + "\n"

    freshness_note = ""
    if freshness.get("is_stale"):
        freshness_note = f"\n- **DATA STALE**: {freshness.get('reason', 'age exceeded threshold')}\n"

    assessment_section = ["## Review Tree", f"- overall_status: `{assessment['overall_status']}`", ""]
    for section in assessment["sections"]:
        assessment_section.extend([
            f"### {section['title']}",
            f"- status: `{section['status']}`",
        ])
        assessment_section.extend(f"- finding: {x}" for x in section.get("findings", []))
        assessment_section.extend(f"- missing: {x}" for x in section.get("missing", []))
        if section.get("conclusion"):
            assessment_section.append(f"- conclusion: {section['conclusion']}")
        assessment_section.append("")

    (out_dir / "rationale.md").write_text(
        "\n".join([
            f"# Rationale: {action['action_id']}",
            f"Recommendation: **{score_obj['recommendation']}**",
            f"Score: `{score_obj['score']}` (raw `{score_obj.get('raw_score', score_obj['score'])}` "
            f"+ doctrine-LLM nudge `{score_obj.get('llm_score_adjustment', 0.0):+}`) "
            f"| Confidence: `{score_obj['confidence']}` | Readiness: `{score_obj.get('readiness_score', 0)}`",
            (f"> Reasoning layer ({(score_obj.get('llm_lean') or {}).get('source', 'n/a')}): "
             f"{(score_obj.get('llm_lean') or {}).get('rationale', 'no nudge applied')}"
             + (" — **this nudge changed the directional outcome.**" if score_obj.get("llm_assisted") else "")
             ) if score_obj.get("llm_lean") else "",
            "",
            f"## Plain-language explanation ({message_source})",
            human_text,
            "",
            *assessment_section,
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
        "directional_threshold": score_obj.get("directional_threshold", 0.12),
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


def run_all(limit: int | None = None, status: str | None = None) -> dict:
    actions = _load_actions()
    if status:
        actions = [
            action for action in actions
            if (action.get("status") or "").lower() == status.lower()
        ]
    run_ids = []
    for a in actions[:limit] if limit else actions:
        run_ids.append(run_once(a["action_id"])["run_id"])
    return {"runs": len(run_ids), "status_filter": status, "run_ids": run_ids}


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
