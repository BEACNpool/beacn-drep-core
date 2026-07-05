# Rationale: gov_action133jnaewfsq8x6v08ndd87l2yqryp63r30t2dkceacxx5cply5n7sqzlcyqf
Recommendation: **ABSTAIN**
Score: `0.03` (raw `0.01` + doctrine-LLM nudge `+0.02`) | Confidence: `0.5775` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a constitution action: 8 well-supported claim(s), constitution doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Cardano Constitution to Replace the Interim Constitution. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a NewConstitution. The cached anchor describes the request as: Cardano Constitution to Replace the Interim Constitution. The strongest grounded claim is: This Cardano Constitution is proposed to replace the Interim Constitution.

Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: NewConstitution
- finding: Status: enacted
- finding: Proposed epoch: 537
- finding: Expires after epoch: 544
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Cardano Constitution to Replace the Interim Constitution
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: This Cardano Constitution is proposed to replace the Interim Constitution., The Cardano Constitution is the result of extensive Cardano community consultation throughout 2024., The Interim Constitution was intended to be temporary, and its Appendix II: Ratification of Final Constitution required its replacement to be submitted on-chain no later than January 31, 2025., CIP-1694 The age of Voltaire for the Cardano Blockchain laid out the foundations for decentralized decision-making.
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, independently_verifiable, high materiality): This Cardano Constitution is proposed to replace the Interim Constitution.
- finding: Claim (governance, independently_verifiable, high materiality): The Cardano Constitution is the result of extensive Cardano community consultation throughout 2024.
- finding: Claim (governance, independently_verifiable, high materiality): The Interim Constitution was intended to be temporary, and its Appendix II: Ratification of Final Constitution required its replacement to be submitted on-chain no later than January 31, 2025.
- finding: Claim (other, independently_verifiable, low materiality): CIP-1694 The age of Voltaire for the Cardano Blockchain laid out the foundations for decentralized decision-making.
- finding: Claim (economic, independently_verifiable, medium materiality): To give effect to true governance by all ada owners, including on-chain voting, members of the Cardano Community worked together for more than a year, holding global workshops, to ultimately approve a Cardano Improvement Proposal, CIP-1694, that provides a...
- finding: Claim (governance, independently_verifiable, medium materiality): CIP-1694 was first published November 18, 2022, as a minimum viable on-chain governance framework.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "This Cardano Constitution is proposed to replace the Interim Constitution." and clears the evidence gates.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of NewConstitution.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Flag score present (3), reducing confidence.
- Intake: Action type: NewConstitution
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This Cardano Constitution is proposed to replace the Interim Constitution." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): Doctrine-aware offline lean for a constitution action: 8 well-supported claim(s), constitution doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `5cd506b065f71d420aa1f4e9f4c65208c742b83dfd2a40ff53914d11dee6a7af`
- snapshot_bundle_hash: `957edd8cdc3028ec90d84125fedcac680e20d40d9508e38e517a4c7c0c38b1c6`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `10`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4644, "NO": 0.2378, "YES": 0.2978}`

