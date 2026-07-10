# Rationale: gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.47` | Readiness: `1.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a parameter action: parameter doctrine demands elevated scrutiny. Net bounded adjustment -0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a ParameterChange. The cached anchor describes the request as: not stated.

Reason code: CONTEXT_THIN_ANCHOR_UNPINNED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: ParameterChange
- finding: Status: expired
- finding: Proposed epoch: 518
- finding: Expires after epoch: 525
- finding: Treasury request: not specified
- finding: Anchor pinned locally: no
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: not pinned
- finding: Proposal document read by reasoning layer: no
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Proposal claims not extracted (no cached anchor document text to read).
- missing: No structured claim/evidence extraction from the proposal document.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Risk review
- status: `complete`
- finding: Execution risk: high
- finding: Governance risk: high
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: ParameterChange advances a credible public benefit worth its risk if the evidence holds.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of ParameterChange.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Protocol parameter changes carry system-wide risk.
- Flag score present (10), reducing confidence.
- Intake: Action type: ParameterChange
- Claims and evidence: Proposal anchor: not pinned
- Risk review: Execution risk: high
- Counterargument pass: Strongest YES: ParameterChange advances a credible public benefit worth its risk if the evidence holds.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): Doctrine-aware offline lean for a parameter action: parameter doctrine demands elevated scrutiny. Net bounded adjustment -0.020 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Anchor document is not yet pinned locally for this action.
- No DRep distribution available.
- Protocol action lacks a complete independently pinned readiness packet: constitutional_alignment_pass, impact_analysis_complete, rollback_or_containment_plan, safety_margin_clear
- Claims and evidence missing: No structured claim/evidence extraction from the proposal document.
- Claims and evidence status is thin.

## Reproducibility
- input_hash: `1969ca6977ee1d2f538cc66cf56a2c189c18adf125c6fbdb61f09e2113afed43`
- snapshot_bundle_hash: `ee7e7cf21334047ad66acf87bf35657cb9b2ee776c396e1f841305818f4d5dd6`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `25`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4375, "NO": 0.2812, "YES": 0.2812}`

