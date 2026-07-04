# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.2533` (raw `-0.2533` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7833` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show meaningful governance and protocol-support alignment, some independently verifiable process and smart-contract controls, and a detailed budget split, but the deterministic treasury analysis already captures the main spending and evidence considerations. The document still relies on proposer assertions for key stewardship promises such as full accounting, unspent-fund return, and future assurance, so there is no basis for a positive nudge beyond the engine score.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the higher evidence bar required for spending shared ADA, especially around accountability for spending and the return of unspent funds.

The action requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support. The proposal described three work packages: community-facing technical coordination, protocol governance work for the Parameter Committee, CIP editors, and Hard Fork Working Group, and a pilot independent technical review programme launching in 2027. It also claimed milestone-based drawdowns, evidence-backed reporting, transparent disclosures, external assurance, and return of unspent funds.

Several core facts were supported: the amount, the 12-month scope, the budget split across WP1, WP2, and WP3, the dependency on the IntersectMBO budget proposal, the claimed Intersect budget-process support, the net change limit context, and use of the Sundae Labs treasury management framework. However, important claims were still thin or unsupported by independent evidence, including the claim that all expenditure would be fully accounted for and unspent funds returned to the treasury, and the claim that independent audits and assurance would be provided by Appold.

The review found medium execution risk, missing independent assurance, no clear sustainability path, limited cost-benefit clarity, and no dependency map. Because treasury withdrawals require elevated scrutiny and the broader treasury flow signal was already in an unsustainable regime, BEACN concluded that the cost and precedent risk outweighed the supported benefits, so the vote was NO.

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
- finding: Requested: Withdraw treasury funds to support Intersect Technical Steering Committee activities for 12 months across community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v on behalf of the vendor
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including attendance of technical experts at major ecosystem events and commissioning technical reports, WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, external assurance, and return of unspent funds
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3.
- finding: Claim (technical, supported_in_proposal, high materiality): WP2 funds the Parameter Committee, CIP editors, and Hard Fork Working Group to support protocol governance and evolution.
- finding: Claim (governance, supported_in_proposal, high materiality): WP3 will establish a pilot independent technical review programme launching in 2027 with conflict-of-interest provisions, published recusals, and open reviewer selection against documented criteria.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold and may include deliverable verification, control testing, spend validation, and milestone evidence assessment.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
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
- finding: Strongest YES: the proposal substantiates "The proposal requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1193000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support." and clears the evidence gates.
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
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold and may include deliverable verification, control testing, spend validation, and milestone evidence assessment.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `102e972e99ca7e403f97f2567c0a497f7357ae773f8d602450912ddd56873949`
- snapshot_bundle_hash: `28f442ed37d538aaf5eb6248f99e0192956a735d437f6bd00203668ed314b483`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2093, "NO": 0.7436, "YES": 0.0471}`

