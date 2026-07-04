# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal contains useful budget totals, work-package descriptions, external references, audit/assurance intent, and smart-contract control details, but the deterministic assessment identifies missing budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis for a treasury withdrawal. Under a treasury stewardship and evidence-quality lens, those omissions justify a small cautionary negative nudge without trying to override the engine's blocked status.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not clear the evidence bar expected for spending shared ADA. The request is significant, 1,193,000 ada for 12 months of Intersect Technical Steering Committee support, but the review found the treasury diligence record incomplete and several core analyses missing.

The proposal asked for funding across three work packages: community-facing technical coordination, protocol governance and evolution, and a pilot independent technical review program launching in 2027. It provided clear top-level budget figures: 256,000 ada for WP1, 832,000 ada for WP2, and 105,000 ada for WP3. It also described smart-contract treasury management, external oversight, audit or assurance intent, and prior Intersect budget-process support.

However, several important claims were not independently supported in the review record, including the claim that execution depends on approval of the IntersectMBO budget proposal and the claim that all spending would be fully accounted for with unused funds returned. The review also found missing or incomplete budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. Treasury analysis lacked a line-item budget and milestone-gated disbursement, while the risk review lacked mitigation evidence and independent assurance.

The strongest case for YES was that the proposal did substantiate the basic request and purpose of the funding. But for a treasury withdrawal, BEACN applies elevated scrutiny because the action consumes shared ADA and sets precedent. With seven review blockers still open, thin evidence status, unknown execution risk, and an incomplete synthesis, the evidence supported a NO vote rather than approving the withdrawal.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee Support for 12 months across community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including expert attendance at ecosystem events and commissioned technical reports, WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support activities.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is split into 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3.
- finding: Claim (governance, proposer_asserted, high materiality): Execution of the described work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says independent audits and assurance will be provided by Appold, potentially including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Execution of the described work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: The proposal claims the TSC work supports Cardano strategy pillars including infrastructure reliability, governance participation, ecosystem growth, and treasury stewardship.
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
- finding: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support activities." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Execution of the described work packages is contingent on approval of the IntersectMBO budget proposal." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support activities." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal contains useful budget totals, work-package descriptions, external references, audit/assurance intent, and smart-contract control details, but the deterministic assessment identifies missing budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis for a treasury withdrawal. Under a treasury stewardship and evidence-quality lens, those omissions justify a small cautionary negative nudge without trying to override the engine's blocked status.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Execution of the described work packages is contingent on approval of the IntersectMBO budget proposal.
- Claims and evidence missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
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
- input_hash: `4a211680b0414f81c21e2420015138d090355e02873b6f88f9d51814d1186cf0`
- snapshot_bundle_hash: `4fc832c86729bd518f29128ffd3baaf301a92269f4279e0507ec116314f6b845`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1218`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

