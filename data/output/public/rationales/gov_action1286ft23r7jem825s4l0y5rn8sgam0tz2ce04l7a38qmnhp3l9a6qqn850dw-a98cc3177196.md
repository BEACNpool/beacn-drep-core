# Rationale: gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw
Recommendation: **NO**
Score: `-0.4033` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.57` | Readiness: `1.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a parameter action: parameter doctrine demands elevated scrutiny. Net bounded adjustment -0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a ParameterChange. The cached anchor describes the request as: not stated.

Residual uncertainty remains limited to the replayed evidence and the public resources cited by the run manifest.

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
- finding: Snapshot freshness source: manifest
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
- Claims and evidence missing: No structured claim/evidence extraction from the proposal document.
- Claims and evidence status is thin.

## Reproducibility
- input_hash: `a98cc31771965e898952bb2b0559391734a4cad4dfd367ca57ba38aed6b796fd`
- snapshot_bundle_hash: `4c10b215c5f94fb13be821a0ea65f7937418d959a720957d9116bf1e900a1744`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1227`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.21, "NO": 0.7478, "YES": 0.0422}`

