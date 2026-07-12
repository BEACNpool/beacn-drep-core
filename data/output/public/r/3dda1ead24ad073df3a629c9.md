# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2384` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7796` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show direct alignment with protocol safety and governance infrastructure, a clear work-package budget, public smart-contract custody details, prior-funding disclosure, and independently checkable process and NCL references. The adjustment remains small because several benefit claims and the Appold assurance arrangement are stated prospectively, and execution depends on the separate IntersectMBO budget approval.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests 1,193,000 ada for 12 months of Intersect Technical Steering Committee support, delivered through three work packages: community-facing technical coordination, protocol governance and evolution, and a pilot independent technical review programme launching in 2027. The proposal gives a clear budget split of 256,000 ada for WP1, 832,000 ada for WP2, and 105,000 ada for WP3, and it describes custody through treasury management smart contracts with public auditability features. It also says execution depends on approval of the IntersectMBO budget proposal.

Several core facts were supported well enough for review: the pinned anchor document was available and replayable, the amount and work packages were stated, prior treasury funding was disclosed, and the proposal provided voting, audit, custody, and NCL references. But some important claims still relied on proposer assertion rather than independent evidence, including that all spending will be fully accounted for, unspent funds will be returned to the treasury, and Appold assurance will cover deliverables, controls, spending, or milestones.

This is a conservative, evidence-based hold, not a rejection of the work itself. To unblock a YES or NO vote, BEACN needs the applicable Net Change Limit pinned and independently verified from public chain evidence. Stronger independent evidence for the spending return commitment, assurance arrangement, sustainability path, cost-benefit clarity, and rollback or remedy path would also reduce the remaining uncertainty around this treasury request.

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
- finding: Requested: Withdraw treasury funds for Intersect Technical Steering Committee Support over 12 months.
- finding: Recipient: Intersect Technical Steering Committee support via Intersect treasury management smart contracts
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including technical expert attendance at major ecosystem events and commissioning technical reports, WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 1,193,000 ADA, stated as $298,250, to support Technical Steering Committee activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal allocates 256,000 ADA to WP 1, 832,000 ADA to WP 2, and 105,000 ADA to WP 3, totaling 1,193,000 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): The work packages cover community-facing technical coordination, protocol governance and evolution, and a pilot independent technical review programme launching in 2027.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides related voting and audit references.
- missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews of deliverables, controls, spending, and milestone evidence.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ADA, stated as $298,250, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ADA, stated as $298,250, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show direct alignment with protocol safety and governance infrastructure, a clear work-package budget, public smart-contract custody details, prior-funding disclosure, and independently checkable process and NCL references. The adjustment remains small because several benefit claims and the Appold assurance arrangement are stated prospectively, and execution depends on the separate IntersectMBO budget approval.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews of deliverables, controls, spending, and milestone evidence.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `1a688d8d12933602d2f53f09c3d355df9ed1b72cebc97779cd4aa373a565bea4`
- snapshot_bundle_hash: `b9857933e34ada91a24bddca9b15765e25bd03a162db94d9bc448cdec6039364`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4923, "NO": 0.0478, "YES": 0.4599}`

