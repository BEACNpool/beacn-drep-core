# Rationale: gov_action19uhuy5uame2s60yrh6n8cyds8ps5q7tkh05dqlzmpcfy429p9w4qq5ll3g0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2833` (raw `-0.2833` + doctrine-LLM nudge `-0.005`) | Confidence: `0.6108` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a treasury action: 3 well-supported claim(s), 1 unsupported high-materiality claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.005 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Amaru Treasury Withdrawal 2026. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Amaru Treasury Withdrawal 2026. It asks the treasury for 10.14M ADA. The strongest grounded claim is: Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security.

A material claim remains proposer-asserted or thinly supported: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025. Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 614
- finding: Expires after epoch: 621
- finding: Treasury request: 10.14M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Amaru Treasury Withdrawal 2026
- finding: Recipient: not stated in document
- finding: Stated amount: 10.14M ADA
- finding: Deliverables: Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security., Amaru provides another perspective and solution for stake pool operators and developers alike, prioritizing low hardware requirements and a seamless user experience., The project is implemented primarily in Rust and aims to attract new contributors to the ecosystem's core maintenance., This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security.
- finding: Claim (economic, supported_in_proposal, low materiality): Amaru provides another perspective and solution for stake pool operators and developers alike, prioritizing low hardware requirements and a seamless user experience.
- finding: Claim (economic, proposer_asserted, low materiality): The project is implemented primarily in Rust and aims to attract new contributors to the ecosystem's core maintenance.
- finding: Claim (economic, proposer_asserted, high materiality): This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- finding: Claim (economic, supported_in_proposal, low materiality): Before we dive further into the details and cost breakdown, here is a high-level view of the ask, some assumptions we are making, and the general direction of this withdrawal request.
- finding: Claim (economic, proposer_asserted, low materiality): 2025 Retrospective We provide a full retrospective of our 2025 roadmap in annex of this document.
- missing: Independent evidence for: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- missing: Independent evidence for: Duration & Milestones This proposal spans over 12 months , from January to December 2026, throughout which there will be several deliveries, demos, and workshops.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 10.14M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 10.14M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was -0.005 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a treasury action: 3 well-supported claim(s), 1 unsupported high-materiality claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.005 (clamped to ±0.05).
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- Claims and evidence missing: Independent evidence for: Duration & Milestones This proposal spans over 12 months , from January to December 2026, throughout which there will be several deliveries, demos, and workshops.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence
- delivery controls, milestones, assurance, or remedy path

## Reproducibility
- input_hash: `275170fd92d0b86d90851c23a1f6f067aad413615e03b608509d3335214ff191`
- snapshot_bundle_hash: `18d109e3a7e0eb4ea785d6153bcb5742b9696784c0bb240ca928ac1396ee9c2a`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `11`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4419, "NO": 0.5113, "YES": 0.0467}`

