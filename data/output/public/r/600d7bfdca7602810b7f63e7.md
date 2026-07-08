# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.2433` (raw `-0.2533` + doctrine-LLM nudge `+0.01`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): A very small positive nudge is justified because the proposal includes a clear budget breakdown, named work packages, prior-funding disclosure, NCL and Hydra voting references, smart-contract custody details, and external assurance commitments. The nudge remains small because several central benefit claims about ecosystem impact and necessity are still proposer-asserted, and treasury stewardship requires caution for a seven-figure ADA withdrawal.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a seven-figure treasury withdrawal and a material accountability claim was not independently supported: the proposal said all spending would be fully accounted for and unspent funds returned to the Cardano treasury, but the review did not find enough replayable evidence for that claim.

The action requested 1,193,000 ada to fund Intersect Technical Steering Committee support for 12 months. The proposal broke this into 256,000 ada for community-facing technical coordination, 832,000 ada for protocol governance and evolution, and 105,000 ada for a pilot independent technical review programme launching in 2027. It also claimed milestone-based drawdowns, evidence-backed reporting, transparent disclosures, external assurance, and return of unspent funds.

Several parts were well supported or independently checkable: the pinned anchor document was available, the budget breakdown was clear, the proposal referenced Hydra voting support, stated that the withdrawal did not breach the 350M Net Change Limit at submission, disclosed prior treasury funding context, and described smart-contract custody and oversight arrangements. But key benefit and stewardship claims remained thin or proposer-asserted, including the return-of-unspent-funds commitment and the broader claim that the work would support Cardano technical governance, DRep decision-making, protocol evolution, ecosystem resilience, and 2030 strategy goals.

The treasury review also found missing cost-benefit clarity, no sustainability path, missing independent assurance detail, and no dependency map. Because treasury withdrawals require elevated scrutiny and the treasury flow signal was in an unsustainable regime, BEACN treated these gaps as enough to outweigh the proposal’s stronger points and voted NO.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee support activities for 12 months across community-facing technical coordination, protocol governance and evolution, and technical review.
- finding: Recipient: Intersect on behalf of the vendor, with funds directed to the 2026 Treasury Reserve Smart Contract stake address stated in the proposal.
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including expert attendance at major ecosystem events and commissioning technical reports, budgeted at 256,000 ADA., WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group, budgeted at 832,000 ADA., WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027, budgeted at 105,000 ADA., Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, external assurance, and return of any unspent funds to the Cardano treasury.
- finding: Deadline/expiry: 12 months; WP3 pilot independent technical review programme launching in 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The TSC requests $298,250, equivalent to 1,193,000 ADA, to support activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is divided into 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The proposer states the withdrawal does not breach the applicable 350M Net Change Limit at the moment of submission.
- missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: The proposer asserts the TSC work supports Cardano technical governance, DRep decision-making, protocol evolution, ecosystem resilience, and 2030 strategy pillars.
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
- finding: Strongest YES: the proposal substantiates "The TSC requests $298,250, equivalent to 1,193,000 ADA, to support activities for 12 months." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1193000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The TSC requests $298,250, equivalent to 1,193,000 ADA, to support activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by +0.010 (clamped to ±0.05): A very small positive nudge is justified because the proposal includes a clear budget breakdown, named work packages, prior-funding disclosure, NCL and Hydra voting references, smart-contract custody details, and external assurance commitments. The nudge remains small because several central benefit claims about ecosystem impact and necessity are still proposer-asserted, and treasury stewardship requires caution for a seven-figure ADA withdrawal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: The proposer asserts the TSC work supports Cardano technical governance, DRep decision-making, protocol evolution, ecosystem resilience, and 2030 strategy pillars.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a1a0e7b8ee5f6b277cc25b92a0f4ff804b66463cac60b4b96ad4897e7a523048`
- snapshot_bundle_hash: `4654ca6c0cede99e046992569ede9d5c95c3d5a71a60759e0bbc8aa27c4e1c7e`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2116, "NO": 0.7408, "YES": 0.0476}`

