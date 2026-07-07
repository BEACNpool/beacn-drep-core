# Rationale: gov_action1k5vwlfrxtyusd2ec37tckd54gjvqn2kd72xj4t6wkkapdv7zfg0qq468n2r
Recommendation: **ABSTAIN**
Score: `0.015` (raw `0.01` + doctrine-LLM nudge `+0.005`) | Confidence: `0.4237` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 6 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Approve Cardano Foundation as New Managing Entity of Project Catalyst. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Approve Cardano Foundation as New Managing Entity of Project Catalyst. The strongest grounded claim is: The Cardano Foundation (CF), supported by Input Output Group (IOG), is requesting community approval to be appointed as the new managing entity for Project Catalyst.

A material claim remains proposer-asserted or thinly supported: This transition will ensure continuity of operations and minimise delays on milestone reviews and eligible payouts for teams delivering against projects in Funds 10-14. Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 619
- finding: Expires after epoch: 626
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Approve Cardano Foundation as New Managing Entity of Project Catalyst
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: The Cardano Foundation (CF), supported by Input Output Group (IOG), is requesting community approval to be appointed as the new managing entity for Project Catalyst., This will allow for full and effective transition of Catalyst operations and responsibilities from IOG to CF in accordance with the statutes of the Catalyst Foundation Company (CFC)., This transition will ensure continuity of operations and minimise delays on milestone reviews and eligible payouts for teams delivering against projects in Funds 10-14., This approval request and Info Action is unrelated to Intersect’s role as the constitutionally mandated budget administrator for funds 14 to 16.
- finding: Deadline/expiry: not stated in document
- finding: Claim (adoption, supported_in_proposal, medium materiality): The Cardano Foundation (CF), supported by Input Output Group (IOG), is requesting community approval to be appointed as the new managing entity for Project Catalyst.
- finding: Claim (other, proposer_asserted, low materiality): This will allow for full and effective transition of Catalyst operations and responsibilities from IOG to CF in accordance with the statutes of the Catalyst Foundation Company (CFC).
- finding: Claim (economic, proposer_asserted, high materiality): This transition will ensure continuity of operations and minimise delays on milestone reviews and eligible payouts for teams delivering against projects in Funds 10-14.
- finding: Claim (economic, supported_in_proposal, high materiality): This approval request and Info Action is unrelated to Intersect’s role as the constitutionally mandated budget administrator for funds 14 to 16.
- finding: Claim (other, supported_in_proposal, low materiality): In February CF agreed to assume stewardship of Catalyst from IOG, with the primary goal of ensuring continuity for existing grant recipients.
- finding: Claim (adoption, supported_in_proposal, medium materiality): CF is submitting this Info Action to request the Community’s approval for the transition of the Catalyst management role from IOG to CF, in accordance with CFC’s statutes.
- missing: Independent evidence for: This transition will ensure continuity of operations and minimise delays on milestone reviews and eligible payouts for teams delivering against projects in Funds 10-14.
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
- finding: Strongest YES: the proposal substantiates "The Cardano Foundation (CF), supported by Input Output Group (IOG), is requesting community approval to be appointed as the new managing entity for Project Catalyst." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "This transition will ensure continuity of operations and minimise delays on milestone reviews and eligible payouts for teams delivering against projects in Funds 10-14." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The Cardano Foundation (CF), supported by Input Output Group (IOG), is requesting community approval to be appointed as the new managing entity for Project Catalyst." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by +0.005 (clamped to ±0.05): Doctrine-aware offline lean for a info action: 6 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: This transition will ensure continuity of operations and minimise delays on milestone reviews and eligible payouts for teams delivering against projects in Funds 10-14.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `a83b8b18cceb0b2aab375318019d9293c4e3bd40061c2164132846713efbe18a`
- snapshot_bundle_hash: `b2379a67ad799268c4b296fe9aa5b2df3614e2a157a6b1adb6aabc7093d4720c`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4259, "NO": 0.272, "YES": 0.302}`

