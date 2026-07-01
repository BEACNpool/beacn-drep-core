# Rationale: gov_action1f9da8n2yaf4updxzmwc7fnw8ug2gwnpvqays5n3yw6nz0mu3z2qqq6ggge9
Recommendation: **ABSTAIN**
Score: `-0.01` (raw `0.01` + doctrine-LLM nudge `-0.02`) | Confidence: `0.53` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a info action: 3 well-supported claim(s), 2 unsupported high-materiality claim(s). Net bounded adjustment -0.020 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records ABSTAIN on Tempo for Cardono Governance - Maintenance & Development Budget for 2025. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Tempo for Cardono Governance - Maintenance & Development Budget for 2025. The strongest grounded claim is: We aim to make Cardano governance easily accessible, especially on mobile phone & wallet to ADA holder can vote on-chain anytime, anywhere.

A material weak point is that this claim remains proposer-asserted or thinly supported: In order to ensure Tempo.Vote will continue running smoothly to service Cardano community, we are seeking to withdraw from Treasury 380k ADA for the 6 month period (1 Aug 2025 - 31 Jan 2026) with the following breakdown: - Infrastructure Cost: 200k ADA - De... Reason code: RULE_THRESHOLD_UNMET.

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
- finding: Snapshot freshness source: manifest
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
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): Doctrine-aware offline lean for a info action: 3 well-supported claim(s), 2 unsupported high-materiality claim(s). Net bounded adjustment -0.020 (clamped to ±0.05).
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
- input_hash: `4ee941229d2ea3669006753a6db8331236d9601eb02aa0b8dde77a590e9c8c41`
- snapshot_bundle_hash: `46db432758258e56d8ab102586f78a34270f1800de82a1bb42add4b502aa0ec6`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `256`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4525, "NO": 0.2838, "YES": 0.2638}`

