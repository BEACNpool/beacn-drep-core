# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.3533` (raw `-0.3533` + doctrine-LLM nudge `+0.0`) | Confidence: `0.6583` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show meaningful public-benefit alignment through technical governance, independent review, and smart-contract oversight, but the deterministic tree already marks treasury analysis incomplete and the doctrine directs caution for treasury stewardship when diligence is incomplete. The anchor provides checkable process and contract references, yet several key spending-control and delivery assurances remain mostly asserted, so no additional nudge beyond the engine's existing treasury and dossier treatment is justified.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request did not clear the higher evidence bar for spending shared ADA: a material financial accountability claim was not independently supported.

The action requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support. The proposal split the budget into 256,000 ada for community-facing technical coordination, 832,000 ada for protocol governance and evolution work, and 105,000 ada for a pilot independent technical review programme launching in 2027. It claimed the funds would support activities such as expert event attendance, technical reports, the Parameter Committee, CIP editors, the Hard Fork Working Group, technical review, milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and use of Intersect treasury management smart contracts.

Several core claims were well supported by the proposal or independently verifiable: the amount requested, the work-package budget split, the role of WP2 in protocol governance, the planned WP3 review programme, the Intersect budget-process support threshold, the Net Change Limit statement, and use of the Sundae Labs treasury management framework with published addresses and auditability features. But important claims remained thin or unsupported, especially that all spending would be fully accounted for and any unspent funds returned to the treasury, and that Appold would provide independent audits and assurance.

The review found a pinned, replayable anchor document and acknowledged the strongest YES case: the proposal substantiated the basic request and cleared some evidence gates. However, treasury withdrawals require elevated scrutiny because they consume shared ada and set precedent. The review also found medium execution risk, incomplete treasury analysis, missing sustainability and cost-benefit clarity, missing independent assurance and dependency mapping, and an unsustainable treasury-flow signal. On balance, those gaps outweighed the supported benefits, so BEACN voted NO.

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
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee support activities for 12 months, including community engagement, protocol governance, and independent technical review.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination for 256,000 ADA, including expert event attendance and technical reports, WP 2: Protocol Governance and Evolution for 832,000 ADA, funding the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3: Technical Review for 105,000 ADA, establishing a pilot independent technical review programme launching in 2027, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold, Use of Intersect treasury management smart contracts with specified reserve and project-specific addresses
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is split into WP 1 at 256,000 ADA, WP 2 at 832,000 ADA, and WP 3 at 105,000 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): WP 2 funds the Parameter Committee, CIP editors, and Hard Fork Working Group to support protocol governance and evolution.
- finding: Claim (governance, supported_in_proposal, high materiality): WP 3 will establish a pilot independent technical review programme launching in 2027, with conflict-of-interest provisions, published recusals, and open reviewer selection against documented criteria.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1193000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.76
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1193000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `1353b155d684d3bb5be7f90b2dc14212b34a7bdbdbccbdcb1f88c06ddc0f5a56`
- snapshot_bundle_hash: `3db75c3286980e62e7fb623238c511a02fef7ea0ffebfd48d699393cd53a90c2`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `31`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2075, "NO": 0.7489, "YES": 0.0436}`

