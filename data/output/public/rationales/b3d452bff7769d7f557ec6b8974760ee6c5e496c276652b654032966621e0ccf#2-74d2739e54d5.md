# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#2
Recommendation: **YES**
Score: `0.275` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7887` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal aligns with protocol safety and counterfactual-risk concerns because it frames hardware-wallet compatibility as established security-critical infrastructure and includes concrete administration, oversight, prior-funding disclosure, NCL, and audit-reference mechanisms. The positive nudge is small because several core benefit and non-funding-risk claims remain proposer-asserted rather than evidenced within the document itself.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Withdraw 1,310,960 ada for Hardware Wallet Maintenance 2026. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund 12 months of Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, interoperability libraries, cardano-hw-cli, developer support, integration-path support, and vendor-required audits. It asks the treasury for 1,310,960 ADA. The strongest grounded claim is: The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee.

A residual watch item: this claim remains proposer-asserted rather than independently shown: The work is described as continuity maintenance for an already-proven Cardano access layer rather than creation of a new wallet product.

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
- finding: Requested: Fund 12 months of Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, interoperability libraries, cardano-hw-cli, developer support, integration-path support, and vendor-required audits.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1,310,960
- finding: Deliverables: WP1 - Cardano Hardware Wallet Maintenance & Compatibility Assurance, Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting, Milestone-based disbursement controls
- finding: Deadline/expiry: 12 months of funding for 2026
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The work is described as continuity maintenance for an already-proven Cardano access layer rather than creation of a new wallet product.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer says continuous hardware-wallet maintenance is needed because Cardano protocol evolution, Ledger and Trezor release cycles, and wallet and dApp integration demand create compatibility risk.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer claims non-funding would risk users and integrators losing secure access when Cardano, Ledger, or Trezor introduce breaking changes.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal says its scope is limited to hardware-wallet compatibility, tooling, release support, supporting libraries, security, and vendor-required assurance, and does not duplicate core-node, ledger, or general infrastructure maintenance budgets.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: The work is described as continuity maintenance for an already-proven Cardano access layer rather than creation of a new wallet product.
- missing: Independent evidence for: The proposer says continuous hardware-wallet maintenance is needed because Cardano protocol evolution, Ledger and Trezor release cycles, and wallet and dApp integration demand create compatibility risk.
- missing: Independent evidence for: The proposer claims non-funding would risk users and integrators losing secure access when Cardano, Ledger, or Trezor introduce breaking changes.
- missing: Independent evidence for: The proposal says its scope is limited to hardware-wallet compatibility, tooling, release support, supporting libraries, security, and vendor-required assurance, and does not duplicate core-node, ledger, or general infrastructure maintenance budgets.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The work is described as continuity maintenance for an already-proven Cardano access layer rather than creation of a new wallet product." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal aligns with protocol safety and counterfactual-risk concerns because it frames hardware-wallet compatibility as established security-critical infrastructure and includes concrete administration, oversight, prior-funding disclosure, NCL, and audit-reference mechanisms. The positive nudge is small because several core benefit and non-funding-risk claims remain proposer-asserted rather than evidenced within the document itself.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The work is described as continuity maintenance for an already-proven Cardano access layer rather than creation of a new wallet product.
- Claims and evidence missing: Independent evidence for: The proposer says continuous hardware-wallet maintenance is needed because Cardano protocol evolution, Ledger and Trezor release cycles, and wallet and dApp integration demand create compatibility risk.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `74d2739e54d526ac277163e5ee9078658c927001ac18e17f60fed57e064a8112`
- snapshot_bundle_hash: `4c4cf9a3fa68b709be040930a91a422af4fe90d637a4bd99974fb2d1cf902f83`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2043, "NO": 0.0461, "YES": 0.7495}`

