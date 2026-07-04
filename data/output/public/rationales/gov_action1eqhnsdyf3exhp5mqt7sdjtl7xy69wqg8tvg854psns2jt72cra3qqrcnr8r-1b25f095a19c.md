# Rationale: gov_action1eqhnsdyf3exhp5mqt7sdjtl7xy69wqg8tvg854psns2jt72cra3qqrcnr8r
Recommendation: **ABSTAIN**
Score: `0.03` (raw `0.06` + doctrine-LLM nudge `-0.03`) | Confidence: `0.4575` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a parameter action: 4 well-supported claim(s), 2 unsupported high-materiality claim(s), parameter doctrine demands elevated scrutiny. Net bounded adjustment -0.030 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Update Plutus Cost Models. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a ParameterChange. The cached anchor describes the request as: Update Plutus Cost Models. The strongest grounded claim is: This governance action is motivated by three objectives: First, following the hard fork to Protocol Version 11, new Plutus primitives become available.

A material claim remains proposer-asserted or thinly supported: Intersect's Parameter Committee proposes to update the Plutus V3 Cost Model via a Parameter Update governance action to enable the new Plutus primitives that will be available following the van Rossem hard fork (to Protocol Version 11), to enable all Plutus. Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: ParameterChange
- finding: Status: enacted
- finding: Proposed epoch: 633
- finding: Expires after epoch: 640
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Update Plutus Cost Models
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Intersect's Parameter Committee proposes to update the Plutus V3 Cost Model via a Parameter Update governance action to enable the new Plutus primitives that will be available following the van Rossem hard fork (to Protocol Version 11), to enable all Plutus..., Note that the new primitives will not be enabled in Protocol version 10, but only following the enactment of the hard fork to Protocol Version 11., However, the changes for existing primitives will happen immediately on enactment of this governance action., This governance action is motivated by three objectives: First, following the hard fork to Protocol Version 11, new Plutus primitives become available.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, proposer_asserted, high materiality): Intersect's Parameter Committee proposes to update the Plutus V3 Cost Model via a Parameter Update governance action to enable the new Plutus primitives that will be available following the van Rossem hard fork (to Protocol Version 11), to enable all Plutus...
- finding: Claim (technical, proposer_asserted, high materiality): Note that the new primitives will not be enabled in Protocol version 10, but only following the enactment of the hard fork to Protocol Version 11.
- finding: Claim (technical, proposer_asserted, medium materiality): However, the changes for existing primitives will happen immediately on enactment of this governance action.
- finding: Claim (technical, supported_in_proposal, high materiality): This governance action is motivated by three objectives: First, following the hard fork to Protocol Version 11, new Plutus primitives become available.
- finding: Claim (technical, supported_in_proposal, high materiality): This proposal provides the necessary cost model settings so that these primitives can be used following the van Rossem hard fork.
- finding: Claim (technical, supported_in_proposal, low materiality): Second, the action also ensures that Plutus primitives previously limited to Plutus V3 are available in Plutus V1 and Plutus V2.
- missing: Independent evidence for: Intersect's Parameter Committee proposes to update the Plutus V3 Cost Model via a Parameter Update governance action to enable the new Plutus primitives that will be available following the van Rossem hard fork (to Protocol Version 11), to enable all Plutus...
- missing: Independent evidence for: Note that the new primitives will not be enabled in Protocol version 10, but only following the enactment of the hard fork to Protocol Version 11.
- missing: Independent evidence for: However, the changes for existing primitives will happen immediately on enactment of this governance action.
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
- finding: Flag count: 0
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "This governance action is motivated by three objectives: First, following the hard fork to Protocol Version 11, new Plutus primitives become available." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Intersect's Parameter Committee proposes to update the Plutus V3 Cost Model via a Parameter Update governance action to enable the new Plutus primitives that will be available following the van Rossem hard fork (to Protocol Version 11), to enable all Plutus..." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Protocol parameter changes carry system-wide risk.
- Intake: Action type: ParameterChange
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This governance action is motivated by three objectives: First, following the hard fork to Protocol Version 11, new Plutus primitives become available." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): Doctrine-aware offline lean for a parameter action: 4 well-supported claim(s), 2 unsupported high-materiality claim(s), parameter doctrine demands elevated scrutiny. Net bounded adjustment -0.030 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: Intersect's Parameter Committee proposes to update the Plutus V3 Cost Model via a Parameter Update governance action to enable the new Plutus primitives that will be available following the van Rossem hard fork (to Protocol Version 11), to enable all Plutus...
- Claims and evidence missing: Independent evidence for: Note that the new primitives will not be enabled in Protocol version 10, but only following the enactment of the hard fork to Protocol Version 11.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `1b25f095a19c6582ab99e757ad8651b35c0e571fda97093b0ca01abd7c641638`
- snapshot_bundle_hash: `b2240b492eab4b4fcbc48bab9b320193f2c0989130a75e1da1c55ab32c97d4c1`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4344, "NO": 0.2528, "YES": 0.3128}`

