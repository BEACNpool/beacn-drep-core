# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.2333` (raw `-0.2533` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7783` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal gives a concrete work-package budget, custody mechanics, prior-funding disclosure, NCL claim, and several checkable references, which modestly improves evidence quality and treasury-stewardship posture beyond a thin ask. The adjustment remains small because key performance outcomes and some assurance commitments are still mostly proposer-stated, and the work is contingent on another budget approval.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request did not meet the higher evidence bar for spending shared ADA, especially around accountability for funds and return of unspent money.

The proposal requested 1,193,000 ada, stated as $298,250, to fund 12 months of Intersect Technical Steering Committee support. It described three work packages: community-facing technical coordination, protocol governance and evolution support, and a pilot independent technical review programme launching in 2027. The budget split was clearly stated as 256,000 ada for WP 1, 832,000 ada for WP 2, and 105,000 ada for WP 3. The review also found a pinned, replayable proposal anchor, concrete custody mechanics using Sundae Labs treasury management smart contracts, prior-funding disclosure, and a stated claim that the withdrawal did not breach the 350M ada Net Change Limit.

However, some important claims were still too thin for a treasury withdrawal. The proposer stated that all spending would be fully accounted for and that unspent funds would be returned to the Cardano treasury, but the review found missing independent evidence for that claim. The proposer also stated that Appold would provide audits and assurance, but independent evidence for that assurance was also missing. The review flagged missing cost-benefit clarity, no sustainability path, no independent assurance, and no dependency map, with medium execution risk and a treasury-flow signal in an unsustainable regime.

The strongest case for YES was that the proposal clearly substantiated the amount, duration, work packages, and several checkable mechanics. But BEACN’s review concluded that, for a treasury withdrawal, those strengths were outweighed by unsupported accountability and assurance claims. The evidence gates were not strong enough to justify spending 1,193,000 ada, so BEACN voted NO.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee Support for 12 months across community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect on behalf of the vendor, with funds directed to the 2026 Treasury Reserve Smart Contract stake address.
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: community-facing technical coordination, including technical expert attendance at major ecosystem events and commissioned technical reports., WP 2: protocol governance and evolution support for the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: establishment of a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests $298,250, stated as 1,193,000 ADA, to support Technical Steering Committee activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is divided into 256,000 ADA for WP 1, 832,000 ADA for WP 2, and 105,000 ADA for WP 3.
- finding: Claim (technical, supported_in_proposal, high materiality): The work packages cover community-facing technical coordination, protocol governance and evolution, and a pilot independent technical review programme launching in 2027.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for the proposal will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests $298,250, stated as 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests $298,250, stated as 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): The proposal gives a concrete work-package budget, custody mechanics, prior-funding disclosure, NCL claim, and several checkable references, which modestly improves evidence quality and treasury-stewardship posture beyond a thin ask. The adjustment remains small because key performance outcomes and some assurance commitments are still mostly proposer-stated, and the work is contingent on another budget approval.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for the proposal will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `37b3a78817a02444eac08876bcf864fc462b1ebd839aa82f7c5326c560f639e8`
- snapshot_bundle_hash: `99a1518bdaf88936efe682d0e7b66af86f3a063111c349404a26a0ce713dbbfa`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.214, "NO": 0.7379, "YES": 0.048}`

