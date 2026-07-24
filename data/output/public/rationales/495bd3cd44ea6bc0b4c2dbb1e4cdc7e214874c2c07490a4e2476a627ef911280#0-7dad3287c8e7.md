# Rationale: 495bd3cd44ea6bc0b4c2dbb1e4cdc7e214874c2c07490a4e2476a627ef911280#0
Recommendation: **ABSTAIN**
Score: `0.01` (base + flags + capped margin; LLM lean `-0.02` recorded, not added) | Confidence: `0.4225` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 3 well-supported claim(s), 2 unsupported high-materiality claim(s). Net bounded adjustment -0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Tempo for Cardono Governance - Maintenance & Development Budget for 2025. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Tempo for Cardono Governance - Maintenance & Development Budget for 2025. The strongest grounded claim is: We aim to make Cardano governance easily accessible, especially on mobile phone & wallet to ADA holder can vote on-chain anytime, anywhere.

A material claim remains proposer-asserted or thinly supported: In order to ensure Tempo.Vote will continue running smoothly to service Cardano community, we are seeking to withdraw from Treasury 380k ADA for the 6 month period (1 Aug 2025 - 31 Jan 2026) with the following breakdown: - Infrastructure Cost: 200k ADA - De. Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 569
- finding: Expires after epoch: 576
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Tempo for Cardono Governance - Maintenance & Development Budget for 2025
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: Tempo.Vote was developed out of passion to support Cardano decentralized mission., We aim to make Cardano governance easily accessible, especially on mobile phone & wallet to ADA holder can vote on-chain anytime, anywhere., Tempo.Vote runs our own Cardano node, backend indexer independently to ensure we have the most accurate governance voting data so that we are not reliant on any 3rd party centralized provider., However this independent infrastructure comes at significant running cost.
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, proposer_asserted, low materiality): Tempo.Vote was developed out of passion to support Cardano decentralized mission.
- finding: Claim (economic, independently_verifiable, medium materiality): We aim to make Cardano governance easily accessible, especially on mobile phone & wallet to ADA holder can vote on-chain anytime, anywhere.
- finding: Claim (technical, supported_in_proposal, medium materiality): Tempo.Vote runs our own Cardano node, backend indexer independently to ensure we have the most accurate governance voting data so that we are not reliant on any 3rd party centralized provider.
- finding: Claim (technical, proposer_asserted, low materiality): However this independent infrastructure comes at significant running cost.
- finding: Claim (technical, proposer_asserted, high materiality): In order to ensure Tempo.Vote will continue running smoothly to service Cardano community, we are seeking to withdraw from Treasury 380k ADA for the 6 month period (1 Aug 2025 - 31 Jan 2026) with the following breakdown: - Infrastructure Cost: 200k ADA - De...
- finding: Claim (governance, supported_in_proposal, medium materiality): In the next 6 months, Tempo aim to deliver the following features to support Cardano Governance: - Optimize Governance Action Voting & Display - Improve UX for submitting Governance Action - Support Lending Pool to allow anyone to pay a small fee and borrow...
- missing: Independent evidence for: In order to ensure Tempo.Vote will continue running smoothly to service Cardano community, we are seeking to withdraw from Treasury 380k ADA for the 6 month period (1 Aug 2025 - 31 Jan 2026) with the following breakdown: - Infrastructure Cost: 200k ADA - De...
- missing: Independent evidence for: If Approved, this budget and associated Treasury Withdrawal will be administered by Selfdriven (https://selfdriven.fyi/services)
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
- finding: Strongest YES: the proposal substantiates "We aim to make Cardano governance easily accessible, especially on mobile phone & wallet to ADA holder can vote on-chain anytime, anywhere." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "In order to ensure Tempo.Vote will continue running smoothly to service Cardano community, we are seeking to withdraw from Treasury 380k ADA for the 6 month period (1 Aug 2025 - 31 Jan 2026) with the following breakdown: - Infrastructure Cost: 200k ADA - De..." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "We aim to make Cardano governance easily accessible, especially on mobile phone & wallet to ADA holder can vote on-chain anytime, anywhere." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a info action: 3 well-supported claim(s), 2 unsupported high-materiality claim(s). Net bounded adjustment -0.020 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: In order to ensure Tempo.Vote will continue running smoothly to service Cardano community, we are seeking to withdraw from Treasury 380k ADA for the 6 month period (1 Aug 2025 - 31 Jan 2026) with the following breakdown: - Infrastructure Cost: 200k ADA - De...
- Claims and evidence missing: Independent evidence for: If Approved, this budget and associated Treasury Withdrawal will be administered by Selfdriven (https://selfdriven.fyi/services)
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `7dad3287c8e7368df9f15fa402f6a96700668645258b94b2e51c7bdc6ff1dc37`
- snapshot_bundle_hash: `ca8bb7cf3d08d126d405d829be01da9d56d5d3c63380bde8a6c42c5b8dbe93dc`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `2d4ca1500b8dba4c613121f0e0daabae335dbd3a`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `5`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4256, "NO": 0.2772, "YES": 0.2972}`

