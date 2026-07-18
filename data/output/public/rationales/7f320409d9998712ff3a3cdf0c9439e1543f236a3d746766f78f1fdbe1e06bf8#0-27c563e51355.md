# Rationale: 7f320409d9998712ff3a3cdf0c9439e1543f236a3d746766f78f1fdbe1e06bf8#0
Recommendation: **ABSTAIN**
Score: `0.11` (base + flags + capped margin; LLM lean `+0.005` recorded, not added) | Confidence: `0.4475` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 7 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Set 2025 Net Change Limit of 300M ADA, 2026 Net Change Limit of 250M ADA. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Set 2025 Net Change Limit of 300M ADA, 2026 Net Change Limit of 250M ADA. The strongest grounded claim is: As part of the budget approval process, it is necessary to establish a Net Change Limit.

A material claim remains proposer-asserted or thinly supported: The Net Change Limit will be used when reviewing both budget actions and treasury withdrawal actions to ensure constitutionality as required by Article IV of the Constitution and the Treasury Withdrawal Guardrails outlined in Appendix I. Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 546
- finding: Expires after epoch: 553
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Set 2025 Net Change Limit of 300M ADA, 2026 Net Change Limit of 250M ADA
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: As part of the budget approval process, it is necessary to establish a Net Change Limit., This serves as an opportunity for all governance stakeholders to formally express their positions regarding the proposed Net Change Limit, ensuring transparency, accountability, and alignment with organizational objectives., 2025 Net Change Limit of 300,000,000,000,000 lovelace (300M ada) 2026 Net Change Limit of 250,000,000,000,000 lovelace (250M ada) The Net Change Limit beyond 2027 is not defined in this governance action., The Net Change Limit will be used when reviewing both budget actions and treasury withdrawal actions to ensure constitutionality as required by Article IV of the Constitution and the Treasury Withdrawal Guardrails outlined in Appendix I.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): As part of the budget approval process, it is necessary to establish a Net Change Limit.
- finding: Claim (governance, supported_in_proposal, medium materiality): This serves as an opportunity for all governance stakeholders to formally express their positions regarding the proposed Net Change Limit, ensuring transparency, accountability, and alignment with organizational objectives.
- finding: Claim (economic, supported_in_proposal, medium materiality): 2025 Net Change Limit of 300,000,000,000,000 lovelace (300M ada) 2026 Net Change Limit of 250,000,000,000,000 lovelace (250M ada) The Net Change Limit beyond 2027 is not defined in this governance action.
- finding: Claim (economic, proposer_asserted, high materiality): The Net Change Limit will be used when reviewing both budget actions and treasury withdrawal actions to ensure constitutionality as required by Article IV of the Constitution and the Treasury Withdrawal Guardrails outlined in Appendix I.
- finding: Claim (economic, supported_in_proposal, high materiality): Prior to the submission of any budget request, a Net Change Limit must be formally agreed upon.
- finding: Claim (economic, supported_in_proposal, high materiality): Failure to establish a Net Change Limit shall render any such budget request unconstitutional and, therefore, inapplicable.
- missing: Independent evidence for: The Net Change Limit will be used when reviewing both budget actions and treasury withdrawal actions to ensure constitutionality as required by Article IV of the Constitution and the Treasury Withdrawal Guardrails outlined in Appendix I.
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
- finding: Strongest YES: the proposal substantiates "As part of the budget approval process, it is necessary to establish a Net Change Limit." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The Net Change Limit will be used when reviewing both budget actions and treasury withdrawal actions to ensure constitutionality as required by Article IV of the Constitution and the Treasury Withdrawal Guardrails outlined in Appendix I." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Intake: Action type: InfoAction
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "As part of the budget approval process, it is necessary to establish a Net Change Limit." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was +0.005 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a info action: 7 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: The Net Change Limit will be used when reviewing both budget actions and treasury withdrawal actions to ensure constitutionality as required by Article IV of the Constitution and the Treasury Withdrawal Guardrails outlined in Appendix I.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `27c563e51355ff021817d31296977ef2a880a5203bdc879c7fcd69b659c13221`
- snapshot_bundle_hash: `aa3d8bfe9476269ece0cb37206627742ec58deb2f343a74b0708cd82edfef322`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `71c55fc4938e0c692e52f6c0b4a1c4d9d8926c12`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `5`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4319, "NO": 0.1741, "YES": 0.3941}`

