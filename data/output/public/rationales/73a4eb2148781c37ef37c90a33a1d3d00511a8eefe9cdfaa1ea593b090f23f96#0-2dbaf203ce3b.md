# Rationale: 73a4eb2148781c37ef37c90a33a1d3d00511a8eefe9cdfaa1ea593b090f23f96#0
Recommendation: **ABSTAIN**
Score: `0.01` (raw `0.01` + doctrine-LLM nudge `+0.005`) | Confidence: `0.4225` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 5 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Net Change Limit of 300 Million ADA for Epochs 613–713. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Net Change Limit of 300 Million ADA for Epochs 613–713. The strongest grounded claim is: This governance action proposes a Net Change Limit of 300,000,000,000,000 lovelace (300 million ADA) for the period from the start of Epoch 613 (13 February 2026) to the end of Epoch 713 (3 July 2027).

A material claim remains proposer-asserted or thinly supported: Total treasury inflows for 2025 are defined as the sum of inflows from Epoch 532 through Epoch 604. Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 611
- finding: Expires after epoch: 618
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Net Change Limit of 300 Million ADA for Epochs 613–713
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: This governance action proposes a Net Change Limit of 300,000,000,000,000 lovelace (300 million ADA) for the period from the start of Epoch 613 (13 February 2026) to the end of Epoch 713 (3 July 2027)., Upon approval in accordance with the Constitution, this NCL shall apply to Epochs 613–713 and supersede any previously agreed NCL for the same period., This governance action is required to establish a Net Change Limit for a defined period in accordance with the Constitution., 1) Why Epochs 613–713 This Net Change Limit (NCL) period is proposed to align the NCL cycle with the mid-year budget season and ensure that a complete prior year of treasury inflow data is available when setting the subsequent NCL.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, medium materiality): This governance action proposes a Net Change Limit of 300,000,000,000,000 lovelace (300 million ADA) for the period from the start of Epoch 613 (13 February 2026) to the end of Epoch 713 (3 July 2027).
- finding: Claim (governance, supported_in_proposal, high materiality): Upon approval in accordance with the Constitution, this NCL shall apply to Epochs 613–713 and supersede any previously agreed NCL for the same period.
- finding: Claim (governance, supported_in_proposal, high materiality): This governance action is required to establish a Net Change Limit for a defined period in accordance with the Constitution.
- finding: Claim (economic, supported_in_proposal, high materiality): 1) Why Epochs 613–713 This Net Change Limit (NCL) period is proposed to align the NCL cycle with the mid-year budget season and ensure that a complete prior year of treasury inflow data is available when setting the subsequent NCL.
- finding: Claim (economic, supported_in_proposal, high materiality): 2) Why 300 Million ADA For the purpose of maintaining fiscal discipline, the proposed NCL is set with reference to the previous year’s total treasury inflows.
- finding: Claim (other, proposer_asserted, high materiality): Total treasury inflows for 2025 are defined as the sum of inflows from Epoch 532 through Epoch 604.
- missing: Independent evidence for: Total treasury inflows for 2025 are defined as the sum of inflows from Epoch 532 through Epoch 604.
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
- finding: Strongest YES: the proposal substantiates "This governance action proposes a Net Change Limit of 300,000,000,000,000 lovelace (300 million ADA) for the period from the start of Epoch 613 (13 February 2026) to the end of Epoch 713 (3 July 2027)." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Total treasury inflows for 2025 are defined as the sum of inflows from Epoch 532 through Epoch 604." — so cost or precedent may outweigh the benefit.
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
- Intake: Action type: InfoAction
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This governance action proposes a Net Change Limit of 300,000,000,000,000 lovelace (300 million ADA) for the period from the start of Epoch 613 (13 February 2026) to the end of Epoch 713 (3 July 2027)." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was +0.005 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a info action: 5 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: Total treasury inflows for 2025 are defined as the sum of inflows from Epoch 532 through Epoch 604.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `2dbaf203ce3b0c7c189d48342312b05bb50575fc9002d26eef9fa4dd6e943d90`
- snapshot_bundle_hash: `3a4e3184ae3356e1305f5e03ec124a6331c17e2366cbb04f5749dfb96edbfed1`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4256, "NO": 0.2772, "YES": 0.2972}`

