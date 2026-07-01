# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8syhyg4hw
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8333` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit alignment around security-critical wallet access and include some independently checkable governance and custody references, but the deterministic assessment is blocked for missing budget, feasibility, risk, alternatives, failure-mode, and complete summary analysis. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than rewarding a large withdrawal with incomplete diligence.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 1,310,960 ada for Hardware Wallet Maintenance 2026. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, supporting interoperability libraries and cardano-hw-cli maintenance, developer support, integration-path support, and vendor-required audits.. The recorded treasury amount is 1,310,960. The strongest grounded claim is: The proposal requests 1,310,960 ADA, consisting of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee.

A material weak point is that this claim remains proposer-asserted or thinly supported: The requested funding covers 12 months of production maintenance for Cardano hardware-wallet support rather than building a new wallet product. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, supporting interoperability libraries and cardano-hw-cli maintenance, developer support, integration-path support, and vendor-required audits.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,310,960
- finding: Deliverables: 12 months of production maintenance for Cardano hardware-wallet support, Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting, Milestone-based disbursement controls
- finding: Deadline/expiry: 2026 funding period; exact deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ADA, consisting of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The requested funding covers 12 months of production maintenance for Cardano hardware-wallet support rather than building a new wallet product.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer says continuous maintenance is necessary because Cardano protocol evolution, Ledger and Trezor release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer claims funding continuity in 2026 is less costly and less disruptive than waiting for breakage to accumulate and reacting after users or integrators lose access.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The proposer claims the withdrawal does not, at the time of submission, breach the applicable 350M ADA Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: The requested funding covers 12 months of production maintenance for Cardano hardware-wallet support rather than building a new wallet product.
- missing: Independent evidence for: The proposer says continuous maintenance is necessary because Cardano protocol evolution, Ledger and Trezor release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer.
- missing: Independent evidence for: The proposer claims funding continuity in 2026 is less costly and less disruptive than waiting for breakage to accumulate and reacting after users or integrators lose access.
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
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA, consisting of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The requested funding covers 12 months of production maintenance for Cardano hardware-wallet support rather than building a new wallet product." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA, consisting of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show plausible public-benefit alignment around security-critical wallet access and include some independently checkable governance and custody references, but the deterministic assessment is blocked for missing budget, feasibility, risk, alternatives, failure-mode, and complete summary analysis. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than rewarding a large withdrawal with incomplete diligence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~19 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The requested funding covers 12 months of production maintenance for Cardano hardware-wallet support rather than building a new wallet product.
- Claims and evidence missing: Independent evidence for: The proposer says continuous maintenance is necessary because Cardano protocol evolution, Ledger and Trezor release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer.
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
- input_hash: `f6145516a515e20d704c50bfbec37d36c6be82cc0c6efc77713230510b9e4b3e`
- snapshot_bundle_hash: `40cea9204fd82a7ae7b1f2088500652f1a30a9c30f507c6b80fbbf42a9e2ecf7`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `643`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1914, "NO": 0.7642, "YES": 0.0443}`

