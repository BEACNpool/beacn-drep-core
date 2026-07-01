# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8syhyg4hw
Recommendation: **NO**
Score: `-0.3233` (raw `-0.2833` + doctrine-LLM nudge `-0.04`) | Confidence: `0.8433` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal addresses a security-critical access layer and includes some verifiable governance and custody references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than a positive adjustment.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 1,310,960 ada for Hardware Wallet Maintenance 2026. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Hardware Wallet Maintenance 2026 for 12 months of production maintenance of Cardano hardware-wallet support.. The recorded treasury amount is 1,310,960. The strongest grounded claim is: The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee.

A material weak point is that this claim remains proposer-asserted or thinly supported: The requested funding is for continuity of an existing Cardano hardware-wallet access layer rather than building a new wallet product. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Treasury withdrawal to fund Hardware Wallet Maintenance 2026 for 12 months of production maintenance of Cardano hardware-wallet support.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect with project funds later transferred to a Project-Specific Smart Contract.
- finding: Stated amount: 1,310,960
- finding: Deliverables: Ledger and Trezor compatibility updates, maintenance of supporting interoperability libraries and cardano-hw-cli, developer support for ecosystem integrators, support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, vendor-required product or security audits where firmware or app changes trigger them, transparent capped time-and-materials reporting, milestone-based disbursement controls
- finding: Deadline/expiry: 12 months in 2026
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The requested funding is for continuity of an existing Cardano hardware-wallet access layer rather than building a new wallet product.
- finding: Claim (technical, proposer_asserted, high materiality): Without continuous maintenance, Cardano hardware-wallet users and integrators may lose secure access when Cardano, Ledger, or Trezor introduce breaking changes.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal scope is limited to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer says the work aligns primarily with Cardano strategy Pillar 1 and secondarily with Pillar 2 by supporting security, interoperability, developer experience, UX, and adoption.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission.
- missing: Independent evidence for: The requested funding is for continuity of an existing Cardano hardware-wallet access layer rather than building a new wallet product.
- missing: Independent evidence for: Without continuous maintenance, Cardano hardware-wallet users and integrators may lose secure access when Cardano, Ledger, or Trezor introduce breaking changes.
- missing: Independent evidence for: The proposal scope is limited to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- missing: Independent evidence for: The proposer says the work aligns primarily with Cardano strategy Pillar 1 and secondarily with Pillar 2 by supporting security, interoperability, developer experience, UX, and adoption.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The requested funding is for continuity of an existing Cardano hardware-wallet access layer rather than building a new wallet product." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.040 (clamped to ±0.05): The proposal addresses a security-critical access layer and includes some verifiable governance and custody references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than a positive adjustment.
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
- Claims and evidence missing: Independent evidence for: The requested funding is for continuity of an existing Cardano hardware-wallet access layer rather than building a new wallet product.
- Claims and evidence missing: Independent evidence for: Without continuous maintenance, Cardano hardware-wallet users and integrators may lose secure access when Cardano, Ledger, or Trezor introduce breaking changes.
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
- input_hash: `7fa035ec45238cf48ba136a6451dfa359dd09e79dfff16d0f910183c4fd1a6a2`
- snapshot_bundle_hash: `3ee4323de3e4873a763f13fa717710d22ef013b94a1fb9da944f33de02db0db6`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `596`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1884, "NO": 0.7676, "YES": 0.0439}`

