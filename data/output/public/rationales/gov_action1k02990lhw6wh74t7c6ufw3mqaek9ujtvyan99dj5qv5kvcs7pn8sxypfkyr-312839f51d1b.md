# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show some governance and custody structure, but the deterministic assessment identifies missing proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Under BEACN's hierarchy, treasury stewardship and evidence quality outweigh public-benefit assertions, so the bounded nudge should be cautious and negative rather than rewarding the high-level alignment claims.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the evidence bar for spending 1,193,000 ada from shared Cardano funds. The proposal described useful Technical Steering Committee support, but the review found too many open blockers around budget detail, risk, feasibility, alternatives, failure modes, and community impact.

The action requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support. The work was split into three packages: 256,000 ada for community-facing technical coordination, 832,000 ada for protocol governance and evolution, and 105,000 ada for a technical review pilot launching in 2027. The proposer also stated that spending would be fully accounted for, unspent funds would be returned, and Appold would provide independent audits or assurance.

Some claims were supported. The amount, duration, work package structure, dependency on the IntersectMBO budget proposal, Hydra Voting support threshold, net-change-limit compliance, custody structure using Sundae Labs smart contracts, and the treasury dashboard were supported or independently verifiable to varying degrees. But key claims remained unsupported or thin, especially the claim that all spending would be fully accounted for and unused funds returned, and the claim about independent audit and assurance by Appold.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The review passed enough intake checks to make a directional vote possible, including a pinned and replayable proposal anchor, but several review gates failed or remained incomplete: treasury analysis lacked a line-item budget and milestone-gated disbursement, risk review lacked mitigation evidence and independent assurance, and synthesis was blocked by missing budget and proposal analysis. BEACN therefore voted NO because treasury stewardship and evidence quality outweighed the proposal’s high-level public-benefit case.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Withdraw treasury funds for Intersect Technical Steering Committee support over 12 months covering community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination for 256,000 ADA, including expert attendance at ecosystem events and commissioning technical reports., WP 2: Protocol Governance and Evolution for 832,000 ADA, including support for the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review for 105,000 ADA, including a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The work is divided into three work packages totaling 1,193,000 ADA: WP1 at 256,000 ADA, WP2 at 832,000 ADA, and WP3 at 105,000 ADA.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The requested amount does not, at time of submission, breach the applicable 350M ADA Net Change Limit for Epoch 613 to Epoch 713.
- missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, including possible deliverable verification, control testing, spend validation, and milestone evidence assessment.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1.19M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

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
- finding: Strongest YES: the proposal substantiates "The proposal requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1.19M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show some governance and custody structure, but the deterministic assessment identifies missing proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Under BEACN's hierarchy, treasury stewardship and evidence quality outweigh public-benefit assertions, so the bounded nudge should be cautious and negative rather than rewarding the high-level alignment claims.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, including possible deliverable verification, control testing, spend validation, and milestone evidence assessment.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `312839f51d1b9abd7e0591a640c46dfdb6d2a1e6825da6565cf8c521deaf4427`
- snapshot_bundle_hash: `2556fe3438254aff969e5145eabe7909648fe1f08176f2b2af76cb4305a743b4`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

