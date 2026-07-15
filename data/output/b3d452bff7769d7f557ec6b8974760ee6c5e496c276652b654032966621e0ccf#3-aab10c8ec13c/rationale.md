# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **YES**
Score: `0.189` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7672` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a governance-infrastructure proposal with a detailed budget split, on-chain/smart-contract administration details, external references for voting and NCL checks, and stated oversight mechanisms; the deterministic assessment is already ready, and no additional doctrine-based nudge is warranted beyond what those rules should capture.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Withdraw 1,193,000 ada for Intersect Technical Steering Committee Support. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw treasury funds for Intersect Technical Steering Committee support covering 12 months of community engagement, protocol governance, and independent technical review activities. It asks the treasury for 1,193,000 ADA. The strongest grounded claim is: Intersect requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support activities.

A residual watch item: this claim remains proposer-asserted rather than independently shown: All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.19M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw treasury funds for Intersect Technical Steering Committee support covering 12 months of community engagement, protocol governance, and independent technical review activities.
- finding: Recipient: Intersect 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination for 256,000 ADA, including technical expert attendance at major ecosystem events and commissioned technical reports., WP 2: Protocol Governance and Evolution for 832,000 ADA, including support for the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review for 105,000 ADA, including a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support activities.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is divided into 256,000 ADA for community-facing technical coordination, 832,000 ADA for protocol governance and evolution, and 105,000 ADA for technical review.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, independently_verifiable, high materiality): The requested amount does not at submission, alone or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, potentially including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- missing: Independent evidence for: The TSC's activities are described as foundational technical governance infrastructure supporting protocol settings, CIPs, hard fork coordination, DRep decision-making, and treasury scrutiny.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1193000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.55
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support activities." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1193000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support activities." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, potentially including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `aab10c8ec13cf4d2e4dab2c523b8feb6d7cb936db25fc563fe6da5f409f07f9f`
- snapshot_bundle_hash: `3af6450eee29f611019f8afdc053282dfef10962b4bee47c23c6bcfea99d9946`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2241, "NO": 0.0551, "YES": 0.7208}`

