# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#2
Recommendation: **YES**
Score: `0.275` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7887` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe maintenance of an existing security-critical access layer, include a clear budget split, external references for Hydra voting and NCL compliance, disclosed prior funding, and a structured smart-contract oversight process. The nudge remains small because several core need and non-duplication statements are proposer assertions rather than independently verified evidence within the supplied claims.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Withdraw 1,310,960 ada for Hardware Wallet Maintenance 2026. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, interoperability libraries, cardano-hw-cli, developer support, integration-path support, and vendor-required audits. It asks the treasury for 1310960 ADA. The strongest grounded claim is: The proposal requests 1,310,960 ADA for Hardware Wallet Maintenance 2026.

A residual watch item: this claim remains proposer-asserted rather than independently shown: The proposal asserts that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer.

## Review Tree
- overall_status: `incomplete`

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, interoperability libraries, cardano-hw-cli, developer support, integration-path support, and vendor-required audits.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1310960
- finding: Deliverables: 12 months of production maintenance for Cardano hardware-wallet support, Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting with milestones and evidence
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ADA for Hardware Wallet Maintenance 2026.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget consists of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and a 38,183 ADA Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): The requested work covers 12 months of production maintenance for Ledger and Trezor compatibility, supporting libraries, cardano-hw-cli, developer support, integration support, and vendor-required audits.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal asserts that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal states that the scope is limited to compatibility, security, supporting libraries/tooling, release support, and vendor-required audit work and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting results, documentation, and audit materials.
- missing: Independent evidence for: The proposal asserts that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer.
- missing: Independent evidence for: The proposal states that the scope is limited to compatibility, security, supporting libraries/tooling, release support, and vendor-required audit work and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.66
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: medium
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA for Hardware Wallet Maintenance 2026." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer." — so cost or precedent may outweigh the benefit.
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
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA for Hardware Wallet Maintenance 2026." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe maintenance of an existing security-critical access layer, include a clear budget split, external references for Hydra voting and NCL compliance, disclosed prior funding, and a structured smart-contract oversight process. The nudge remains small because several core need and non-duplication statements are proposer assertions rather than independently verified evidence within the supplied claims.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal asserts that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk at the hardware-wallet access layer.
- Claims and evidence missing: Independent evidence for: The proposal states that the scope is limited to compatibility, security, supporting libraries/tooling, release support, and vendor-required audit work and does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `f06b765a1bc2d9abdfa15f54f0c93618bde49fdb5495935fba6e4951e036e4bf`
- snapshot_bundle_hash: `f4ebe160cf276b7f74902765c031c82f0cfbe854247efe6e1bb424a72b6eb9f1`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2043, "NO": 0.0461, "YES": 0.7495}`

