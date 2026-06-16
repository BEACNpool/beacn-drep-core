#!/usr/bin/env python3
"""Append HONEST per-proposal decision-support rows for the 9 active actions.

Replaces the absence (and, for older actions, the uniform fabricated rows) with
assessments grounded in each proposal's anchor document. Principles:
  * independent_assurance_present = no unless a third-party audit/assurance is shown
    (the old rows lied with a blanket 'yes').
  * No treasury dossier is marked complete: BEACN has not done full independent
    diligence this session, so treasury actions correctly stay NEEDS_MORE_INFO with
    SPECIFIC outstanding items, rather than being rubber-stamped.
Existing rows are preserved; the 9 active rows are appended (or replaced if present).
"""
import csv
from pathlib import Path

DS = Path("/home/ubuntudesktop/.openclaw/workspace/beacn-drep-resources/data/input/governance/decision_support")

INFO = "gov_action1t5ap7etluvct2x69nj5mfqhurgakuvekyflcsrv2qkrhrs378n3qq3z2c22"
IKIGAI = "gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq"
HYDRA = "gov_action1fah9m7dxu99af8jqdc4mkrgs3va790nyh9tfhycq2wsvrm47p4rsqtcm6ry"
CMINSIZE = "gov_action1cadmygtqv6r64pvwezw859wg36wpwp209cz94cc7ej9fdp7dyphqq58n5ur"
TWEAG = "gov_action1zljrlljt9cxlz7ra2nep43nxg0r54wcnrgexyuhuam9ah0ws607qq2vcg4x"
RAREEVO = "gov_action18a9sytyez02jl8ee4ryz5xu7heg587m5tu6nr7fkd3ex30umnnjqq27e7ey"
CCI = "gov_action1cp0w6zwgwpj98jtu3r2q838lgwmhs6j49l58zx4q05lx220lmzaqqztnljz"
FIVEAM = "gov_action142ndnn9hycuuwld5ddemash2l709ln06qjgfeudq77z45nf3fpdqqn7pwux"
ETERNL = "gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z"

TREASURY = "TreasuryWithdrawals"
OWNER = "drep-ops"


def upsert(filename, header, rows_by_id):
    path = DS / filename
    existing = []
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            existing = list(csv.DictReader(f))
    keep = [r for r in existing if r.get("action_id") not in rows_by_id]
    out = keep + [rows_by_id[a] for a in rows_by_id]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        for r in out:
            w.writerow({k: r.get(k, "") for k in header})
    print(f"{filename}: {len(keep)} kept + {len(rows_by_id)} active = {len(out)} rows")


# ---------------- financial_sustainability_profiles (treasury only) -------------
# NOTE: includes `sustainability_path_clear` — the engine reads this key from the financial
# row (readiness bonus + treasury-analysis "sustainability path" check), but the column was
# absent from the original CSV, so it always evaluated to None. Adding it fixes that mismatch.
FIN_H = ["action_id", "action_type", "requested_ada", "budget_granularity", "milestone_payment_gates",
         "clawback_refund_path", "fee_recovery_dependency", "fee_recovery_clarity", "recurring_funding_dependency",
         "runway_clarity", "sustainability_path_clear", "cost_benefit_clarity", "financial_confidence",
         "financial_blocker", "notes", "owner", "status"]


def fin(aid, ada, bg, mpg, claw, recdep, runway, sustain, cbc, conf, notes):
    return {"action_id": aid, "action_type": TREASURY, "requested_ada": ada, "budget_granularity": bg,
            "milestone_payment_gates": mpg, "clawback_refund_path": claw, "fee_recovery_dependency": "no",
            "fee_recovery_clarity": "unknown", "recurring_funding_dependency": recdep, "runway_clarity": runway,
            "sustainability_path_clear": sustain, "cost_benefit_clarity": cbc, "financial_confidence": conf,
            "financial_blocker": "no", "notes": notes, "owner": OWNER, "status": "needs_independent_diligence"}


fin_rows = {
    IKIGAI: fin(IKIGAI, "103000", "yes", "no", "no", "no", "yes", "yes", "yes", "0.70",
                "One-time reimbursement; 100k deposit loss is on-chain verifiable, +3k staking comp; no recurring cost."),
    HYDRA: fin(HYDRA, "5100781", "unknown", "unknown", "no", "no", "unknown", "no", "unknown", "0.40",
               "Four workstreams described; needs independent line-item budget and milestone gates; production-usage claims need on-chain verification."),
    TWEAG: fin(TWEAG, "18263496", "yes", "no", "no", "no", "unknown", "no", "unknown", "0.40",
               "Budget basis stated ($176/hr, 0.25 ADA/USD) but framed as single non-milestone pipeline; rate/hours need independent validation at this scale."),
    RAREEVO: fin(RAREEVO, "2750000", "unknown", "no", "no", "no", "no", "no", "no", "0.35",
                 "Event sponsorship; deliverables are soft/marketing; 20% VIP rebate is a partial return mechanism but value uncertain; outcomes hard to verify."),
    CCI: fin(CCI, "23000000", "unknown", "unknown", "no", "yes", "no", "no", "unknown", "0.40",
             "Explicit recurring annual licensing dependency (Circle/LayerZero/Pyth/Dune) plus new Fireblocks; needs line-item fees and a plan to reduce dependence."),
    FIVEAM: fin(FIVEAM, "10000000", "unknown", "yes", "no", "no", "unknown", "no", "unknown", "0.40",
                "Hard-capped and milestone-structured (M1/M2/M3) — positive controls; execution risk across India/Cambodia/Kenya; reach figures unverified."),
    ETERNL: fin(ETERNL, "1680000", "yes", "no", "no", "yes", "yes", "yes", "yes", "0.55",
                "Clear ~$420k/yr cost; recurring but with a stated Pro-plan sustainability path (~5,500 subs to break even) that needs validation."),
}

# ---------------- risk_mitigation_registry (all 9) -----------------------------
RISK_H = ["action_id", "action_type", "execution_risk_level", "governance_risk_level", "technical_risk_level",
          "treasury_exposure_risk_level", "mitigation_evidence_present", "independent_assurance_present",
          "rollback_or_remedy_path", "dependency_map_complete", "risk_profile_confidence", "risk_blocker",
          "notes", "owner", "status"]


def risk(aid, atype, ex, gov, tech, texp, mit, rollback, depmap, conf, notes):
    # independent_assurance_present is honestly 'no' across the board — none provide third-party assurance.
    return {"action_id": aid, "action_type": atype, "execution_risk_level": ex, "governance_risk_level": gov,
            "technical_risk_level": tech, "treasury_exposure_risk_level": texp, "mitigation_evidence_present": mit,
            "independent_assurance_present": "no", "rollback_or_remedy_path": rollback,
            "dependency_map_complete": depmap, "risk_profile_confidence": conf, "risk_blocker": "no",
            "notes": notes, "owner": OWNER, "status": "first_pass_review"}


risk_rows = {
    INFO: risk(INFO, "InfoAction", "low", "medium", "low", "none", "no", "no", "no", "0.6",
               "Non-binding discussion; no funds. Network DReps ~99% NO."),
    IKIGAI: risk(IKIGAI, TREASURY, "low", "low", "low", "low", "yes", "yes", "no", "0.65",
                 "Low risk: one-time payment, verifiable cause; remedy n/a (one-off)."),
    HYDRA: risk(HYDRA, TREASURY, "medium", "low", "high", "high", "partial", "no", "no", "0.45",
                "High technical/treasury exposure (5.1M ADA); delivery risk on a feature-complete v2; mitigations not independently assured."),
    CMINSIZE: risk(CMINSIZE, "ParameterChange", "low", "medium", "medium", "none", "partial", "no", "yes", "0.6",
                   "Governance-resilience parameter; tied to a separate cost-model change; network DReps ~72% NO."),
    TWEAG: risk(TWEAG, TREASURY, "medium", "low", "high", "high", "partial", "no", "no", "0.45",
                "18.26M ADA, protocol-level crypto (Peras); single-pipeline framing raises delivery-risk concentration; no milestone gates."),
    RAREEVO: risk(RAREEVO, TREASURY, "medium", "low", "low", "medium", "no", "no", "no", "0.4",
                  "Event outcomes hard to measure; benefit realization risk; no enforceable success metrics."),
    CCI: risk(CCI, TREASURY, "medium", "low", "medium", "high", "partial", "no", "no", "0.45",
              "Recurring third-party dependency is the dominant risk; declining future funding could strand paid-for integrations."),
    FIVEAM: risk(FIVEAM, TREASURY, "high", "low", "medium", "medium", "yes", "no", "no", "0.45",
                 "Execution risk across three developing-market geographies; milestone structure is a partial mitigation."),
    ETERNL: risk(ETERNL, TREASURY, "low", "low", "low", "low", "yes", "no", "yes", "0.55",
                 "Mature, widely-used wallet; main risk is whether the sustainability plan materializes."),
}

# ---------------- deep_research_dossiers (all 9) -------------------------------
DOS_H = ["action_id", "action_type", "proposal_summary_complete", "budget_analysis_complete",
         "feasibility_assessment_complete", "risk_analysis_complete", "alternatives_analysis_complete",
         "failure_mode_analysis_complete", "community_impact_complete", "dossier_complete", "analyst_notes",
         "owner", "status"]


def dossier(aid, atype, notes):
    # Honest first pass: BEACN has summarized and done a risk pass; budget/feasibility/alternatives/
    # failure-mode require independent verification -> dossier NOT complete.
    return {"action_id": aid, "action_type": atype, "proposal_summary_complete": "yes",
            "budget_analysis_complete": "no", "feasibility_assessment_complete": "no",
            "risk_analysis_complete": "yes", "alternatives_analysis_complete": "no",
            "failure_mode_analysis_complete": "no", "community_impact_complete": "no",
            "dossier_complete": "no", "analyst_notes": notes, "owner": OWNER, "status": "diligence_in_progress"}


dossier_rows = {
    IKIGAI: dossier(IKIGAI, TREASURY, "Outstanding: confirm recipient address and exact staking-loss basis on-chain. Low burden; small reimbursement."),
    HYDRA: dossier(HYDRA, TREASURY, "Outstanding: independent line-item budget; on-chain verification of named production users; milestone/acceptance criteria; alternatives to a 5.1M ADA scope."),
    TWEAG: dossier(TWEAG, TREASURY, "Outstanding: independent validation of $176/hr and hours; milestone gating (proposal is single-pipeline); treasury-runway impact of an 18.26M ADA ask; failure-mode if Peras slips."),
    RAREEVO: dossier(RAREEVO, TREASURY, "Outstanding: measurable, enforceable success metrics; basis for the 2.75M ADA valuation; comparison to lower-cost sponsorship tiers."),
    CCI: dossier(CCI, TREASURY, "Outstanding: line-item licensing fees per integration; multi-year recurring-cost projection; plan to reduce treasury dependence; Fireblocks scope justification."),
    FIVEAM: dossier(FIVEAM, TREASURY, "Outstanding: independent feasibility in India/Cambodia/Kenya; basis for the 500k-farmer reach; verification that disbursement is gated on M1/M2/M3."),
    ETERNL: dossier(ETERNL, TREASURY, "Outstanding: evidence for the ~4.2% Pro-plan conversion assumption; verification of install-base figures; staged disbursement against the sustainability plan."),
}

# ---------------- vote_readiness_matrix (all 9) -------------------------------
RDY_H = ["action_id", "action_type", "abstain_reason_code", "anchor_pinned", "anchor_fallback_packet",
         "action_metadata_complete", "timeline_defined", "governance_rules_clear", "budget_envelope_clear",
         "milestones_acceptance_clear", "disbursement_controls_clear", "sustainability_path_clear",
         "risk_profile_complete", "drep_distribution_available", "hard_blocker", "readiness_score",
         "minimum_new_evidence_to_decide", "owner", "status"]


def rdy(aid, atype, timeline, budget_env, milestones, sustain, status, minev):
    return {"action_id": aid, "action_type": atype, "abstain_reason_code": "", "anchor_pinned": "yes",
            "anchor_fallback_packet": "yes", "action_metadata_complete": "yes", "timeline_defined": timeline,
            "governance_rules_clear": "yes", "budget_envelope_clear": budget_env,
            "milestones_acceptance_clear": milestones, "disbursement_controls_clear": "no",
            "sustainability_path_clear": sustain, "risk_profile_complete": "no",
            "drep_distribution_available": "yes", "hard_blocker": "no", "readiness_score": "",
            "minimum_new_evidence_to_decide": minev, "owner": OWNER, "status": status}


rdy_rows = {
    INFO: rdy(INFO, "InfoAction", "no", "no", "no", "no", "directional_from_network",
              "None required for an info action; BEACN follows clear network consensus."),
    IKIGAI: rdy(IKIGAI, TREASURY, "yes", "yes", "no", "no", "needs_independent_diligence",
                "Confirm recipient address + staking-loss basis on-chain."),
    HYDRA: rdy(HYDRA, TREASURY, "yes", "no", "no", "no", "needs_independent_diligence",
               "Independent budget + on-chain usage verification + milestone gates."),
    CMINSIZE: rdy(CMINSIZE, "ParameterChange", "yes", "no", "no", "no", "directional_from_network",
                  "Dependency on the linked cost-model change; otherwise network-driven."),
    TWEAG: rdy(TWEAG, TREASURY, "yes", "yes", "no", "no", "needs_independent_diligence",
               "Independent rate/hours validation + milestone gating + runway impact."),
    RAREEVO: rdy(RAREEVO, TREASURY, "yes", "no", "no", "no", "needs_independent_diligence",
                 "Enforceable success metrics + valuation basis."),
    CCI: rdy(CCI, TREASURY, "yes", "no", "no", "no", "needs_independent_diligence",
             "Line-item recurring fees + dependence-reduction plan."),
    FIVEAM: rdy(FIVEAM, TREASURY, "yes", "no", "yes", "no", "needs_independent_diligence",
                "Independent feasibility + reach basis + milestone-gated disbursement proof."),
    ETERNL: rdy(ETERNL, TREASURY, "yes", "yes", "no", "yes", "needs_independent_diligence",
                "Evidence for Pro-plan conversion + staged disbursement."),
}

upsert("financial_sustainability_profiles.csv", FIN_H, fin_rows)
upsert("risk_mitigation_registry.csv", RISK_H, risk_rows)
upsert("deep_research_dossiers.csv", DOS_H, dossier_rows)
upsert("vote_readiness_matrix.csv", RDY_H, rdy_rows)
print("done.")
