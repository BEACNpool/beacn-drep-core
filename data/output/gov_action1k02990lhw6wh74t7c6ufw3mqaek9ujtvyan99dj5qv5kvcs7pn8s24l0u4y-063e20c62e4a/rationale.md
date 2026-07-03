# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9033` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims include some checkable governance and custody mechanisms, but the deterministic assessment identifies missing treasury, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under the doctrine, treasury stewardship and evidence quality justify a cautious negative nudge rather than rewarding plausible ecosystem value that is not fully supported in the anchor.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 3,810,423 ada for Mithril Protocol. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw treasury funds for Mithril Protocol continuous development through Intersect on behalf of the vendor.. The recorded treasury amount is 3,810,423. The strongest grounded claim is: The requested budget is 3,699,440 ada for Mithril Protocol Continuous Development plus a 110,983 ada Intersect Budget Administration fee, totaling 3,810,423 ada.

A material weak point is that this claim remains proposer-asserted or thinly supported: Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify state in a trustless way. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Withdraw treasury funds for Mithril Protocol continuous development through Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with project funds later transferred to a Project-Specific Smart Contract; vendor named Teragone in prior funding disclosure.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect budget administration and oversight, Milestone-based disbursement controls through TRSC/PSSC smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, proposer_asserted, high materiality): Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify state in a trustless way.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is 3,699,440 ada for Mithril Protocol Continuous Development plus a 110,983 ada Intersect Budget Administration fee, totaling 3,810,423 ada.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The requested withdrawal does not, at time of submission alone or in aggregate, breach the 350M Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (governance, proposer_asserted, high materiality): Audit, administrative oversight, reporting obligations, and milestone-based disbursement controls are included through Intersect overhead and administration fees.
- finding: Claim (technical, independently_verifiable, high materiality): Treasury funds will be administered through Sundae Labs treasury management smart contracts, including one Treasury Reserve Smart Contract and one Project-Specific Smart Contract.
- missing: Independent evidence for: Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify state in a trustless way.
- missing: Independent evidence for: Audit, administrative oversight, reporting obligations, and milestone-based disbursement controls are included through Intersect overhead and administration fees.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs, but has worked on Mithril for several years through IOG-funded collaboration.
- missing: Independent evidence for: Faster Mithril sync times lower onboarding friction and enable tooling for exchanges, wallets, monitoring, bridges, full wallets, light clients, and community-built tools.
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
- finding: Six-month treasury flow regime: unsustainable
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
- finding: Strongest YES: the proposal substantiates "The requested budget is 3,699,440 ada for Mithril Protocol Continuous Development plus a 110,983 ada Intersect Budget Administration fee, totaling 3,810,423 ada." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify state in a trustless way." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The requested budget is 3,699,440 ada for Mithril Protocol Continuous Development plus a 110,983 ada Intersect Budget Administration fee, totaling 3,810,423 ada." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims include some checkable governance and custody mechanisms, but the deterministic assessment identifies missing treasury, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under the doctrine, treasury stewardship and evidence quality justify a cautious negative nudge rather than rewarding plausible ecosystem value that is not fully supported in the anchor.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- Claims and evidence missing: Independent evidence for: Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify state in a trustless way.
- Claims and evidence missing: Independent evidence for: Audit, administrative oversight, reporting obligations, and milestone-based disbursement controls are included through Intersect overhead and administration fees.
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
- input_hash: `063e20c62e4a7d8c101f6d9f18dbb899096a104ad6384d6749f2dc13ca8b8870`
- snapshot_bundle_hash: `9737f726a3fe11ee0bb0d2df04e1ecadc0bb4d38a5b2ebf60ec56ff34161a6c5`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `b97265e867768077aac16ceb31ccfe1be639d187`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `800`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1717, "NO": 0.7869, "YES": 0.0415}`

