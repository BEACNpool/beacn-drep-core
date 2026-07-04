# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.3933` (raw `-0.3533` + doctrine-LLM nudge `-0.04`) | Confidence: `0.5183` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure value and some checkable governance and smart-contract process evidence, but the assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, those evidence gaps warrant a small cautionary nudge against spending beyond the deterministic blockers already applied.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and the review found major evidence gaps in the budget, feasibility, risk, alternatives, failure modes, and community impact analysis.

The action requested 3,810,423 ada for Mithril Protocol continuous development through Intersect: 3,699,440 ada for development and 110,983 ada for Intersect budget administration. The funds would first go to the 2026 Treasury Reserve Smart Contract stake address, then later move to a project-specific smart contract once legal contract and vendor readiness conditions are met. The proposal described milestone-based disbursement controls, Intersect oversight, and third-party reporting, but no deadline was stated.

Several important claims were supported or checkable. The review accepted that Mithril uses stake-based threshold multi-signatures to help certify Cardano state, and it treated the pinned anchor document as available and replayable. It also noted checkable governance context, including Hydra Voting support and that the withdrawal did not breach the applicable 350M Net Change Limit at submission. However, other material claims were only proposer-asserted or lacked independent evidence, including whether audit and oversight costs were fully covered by the overhead and administration fee, and whether Teragone had not previously received direct Cardano treasury or community governance funding.

The decisive issue was not that Mithril lacked value. The strongest YES case was that the proposal substantiated Mithril’s public-benefit technical role. But for a 3.81M ada treasury withdrawal, BEACN applies elevated scrutiny, and the review gates were not complete: treasury analysis was missing a line-item budget and full milestone-gated disbursement evidence, risk review lacked mitigation evidence and independent assurance, and synthesis was blocked by missing proposal, budget, feasibility, risk, alternatives, failure-mode, and community-impact analysis. On the available evidence, BEACN judged that the open blockers and unsupported cost-oversight claim outweighed the case for approving the withdrawal.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 3.81M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continuous development through Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with later transfer to a Project-Specific Smart Contract when legal contract and vendor readiness conditions are met.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect budget administration and oversight, Milestone-based disbursement controls through Intersect smart contract process
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is 3,699,440 ada for Mithril Protocol Continuous Development plus a 110,983 ada Intersect Budget Administration fee, totaling 3,810,423 ada.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The requested withdrawal does not, at the time of submission, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (economic, proposer_asserted, medium materiality): Audit and oversight costs are included within the overhead applied to this proposal, and Intersect's administration fee covers administrative oversight.
- finding: Claim (governance, supported_in_proposal, high materiality): Independent oversight will be provided through Intersect and technically capable third parties, including reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: Audit and oversight costs are included within the overhead applied to this proposal, and Intersect's administration fee covers administrative oversight.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs.
- missing: Independent evidence for: Teragone has worked on Mithril for several years through collaboration with IOG, which has funded the project to date.
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
- finding: Requested ADA: 3.81M ADA
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
- finding: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Audit and oversight costs are included within the overhead applied to this proposal, and Intersect's administration fee covers administrative oversight." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 3.81M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.040 (clamped to ±0.05): The extracted claims show plausible public-benefit infrastructure value and some checkable governance and smart-contract process evidence, but the assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, those evidence gaps warrant a small cautionary nudge against spending beyond the deterministic blockers already applied.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Audit and oversight costs are included within the overhead applied to this proposal, and Intersect's administration fee covers administrative oversight.
- Claims and evidence missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs.
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
- input_hash: `7b4aeb4507545b9975d266f0422305cc03c57b3bd287abb2987912c97e728dc7`
- snapshot_bundle_hash: `06616c82bf18047b6df04bdd85f95e9c47b40d12384cacba5b1ba82af4a4e12e`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `961`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2185, "NO": 0.7387, "YES": 0.0428}`

