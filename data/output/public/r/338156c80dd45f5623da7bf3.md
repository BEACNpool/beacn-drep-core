# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8syhyg4hw
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show a plausible public-benefit maintenance need for a security-critical access layer and some independently checkable governance and smart-contract references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under treasury stewardship and evidence-quality doctrine, that evidence gap justifies a small cautionary negative nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and the review found too many unresolved evidence gaps for shared ADA to be released responsibly.

The action requested 1,310,960 ada for 12 months of 2026 hardware-wallet maintenance, covering Ledger and Trezor compatibility updates, supporting libraries and cardano-hw-cli, developer support, integration support, vendor-required audits, and capped time-and-materials reporting. The proposal did support the total budget figure: 1,272,777 ada for maintenance and compatibility assurance, plus 38,183 ada for Intersect budget administration. It also had a pinned, replayable anchor document, passed the required 67% Intersect Budget Process Hydra Voting threshold, and did not breach the applicable 350M Net Change Limit at submission.

However, several important claims remained unsupported or thinly evidenced. The review did not find independent evidence for the claim that continuous hardware-wallet maintenance is necessary to prevent users or integrators from losing secure access when Cardano, Ledger, or Trezor introduce breaking changes. It also did not find independent evidence that the scope avoids duplication with broader core-node, ledger, or infrastructure maintenance budgets. The risk review was thin, with execution risk marked unknown and missing mitigation evidence and independent assurance.

The treasury gate required elevated scrutiny, and key review areas failed or remained blocked: complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. The strongest YES case was that the requested amount and top-level budget split were substantiated, but seven blockers remained open. For BEACN, that was not enough to justify a directional YES on a treasury withdrawal, so the evidence-based outcome was NO.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.31M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Hardware Wallet Maintenance 2026 for 12 months of Cardano hardware-wallet production maintenance.
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,310,960
- finding: Deliverables: Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting with milestones and evidence
- finding: Deadline/expiry: 12 months during 2026
- finding: Claim (technical, proposer_asserted, high materiality): Cardano hardware-wallet support must be maintained continuously or users and integrators may lose secure access when Cardano, Ledger, or Trezor introduce breaking changes.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal scope is limited to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget totals 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance and Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The requested amount does not, at the time of submission, breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 either alone or in aggregate.
- finding: Claim (governance, proposer_asserted, high materiality): Independent oversight will be provided through Intersect and technically capable third parties, with reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: Cardano hardware-wallet support must be maintained continuously or users and integrators may lose secure access when Cardano, Ledger, or Trezor introduce breaking changes.
- missing: Independent evidence for: The proposal scope is limited to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- missing: Independent evidence for: Independent oversight will be provided through Intersect and technically capable third parties, with reporting obligations and milestone-based disbursement controls.
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
- finding: Requested ADA: 1.31M ADA
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
- finding: Strongest YES: the proposal substantiates "The requested budget totals 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance and Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Cardano hardware-wallet support must be maintained continuously or users and integrators may lose secure access when Cardano, Ledger, or Trezor introduce breaking changes." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1.31M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The requested budget totals 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance and Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show a plausible public-benefit maintenance need for a security-critical access layer and some independently checkable governance and smart-contract references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under treasury stewardship and evidence-quality doctrine, that evidence gap justifies a small cautionary negative nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Cardano hardware-wallet support must be maintained continuously or users and integrators may lose secure access when Cardano, Ledger, or Trezor introduce breaking changes.
- Claims and evidence missing: Independent evidence for: The proposal scope is limited to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
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
- input_hash: `61befb8da183eca7fb308a836809c3013b419e13ffedb6b8e5f24d9b0cdce98e`
- snapshot_bundle_hash: `1294b13862112d48e22b54f6c3d6ef9fd98d3d670b1331303f004d16b7de68a2`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

