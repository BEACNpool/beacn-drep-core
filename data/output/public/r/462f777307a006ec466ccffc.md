# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8syhyg4hw
Recommendation: **NO**
Score: `-0.2733` (raw `-0.2533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7883` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has useful governance and administration evidence, including budget breakdown, voting references, NCL assertion, prior funding disclosure, and smart-contract oversight details, but the core value-for-money case for a high treasury ask rests mostly on asserted compatibility risk and a broad work package rather than detailed vendor identity, milestones, rates, or reproducible maintenance workload evidence in the supplied claims. A small cautionary nudge is justified because treasury stewardship and evidence quality are not fully satisfied by process controls alone.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks for a large treasury withdrawal, but the core value-for-money case is not supported strongly enough by independent evidence. The review found useful process and administration evidence, but the main justification for spending 1,310,960 ada still depends too much on proposer assertions about scope, compatibility risk, workload, and delivery details.

The action requested 1,310,960 ada for Hardware Wallet Maintenance 2026, with 1,272,777 ada for maintenance and compatibility assurance and 38,183 ada for Intersect budget administration. The proposal says the work would cover Ledger and Trezor compatibility updates, supporting libraries and cardano-hw-cli, developer support, integration support, vendor-required audits, capped time-and-materials reporting, and milestone-based disbursements over 12 months. It also states that this would not create a new wallet product or duplicate other infrastructure budgets.

Several governance and administration claims were well supported: the anchor document was available and replayable, the budget split was clear, oversight and administration controls were described, six external Oversight Committee entities were named, and smart-contract addresses, thresholds, a dashboard URL, repository references, and audit references were provided for treasury administration checks. The proposal also cited Intersect budget process support, a Net Change Limit assertion, and prior funding references.

The review gates were stricter because this is a treasury withdrawal. The proposal passed enough intake and administration checks to be reviewable, and the strongest YES case was that the amount and budget split were substantiated. But BEACN’s evidence review remained thin on the substance of the spend: independent support was missing for the limited scope claim and for the claimed ongoing compatibility risk, and the treasury review lacked a sustainability path and cost-benefit clarity. Risk review also lacked independent assurance and a rollback or remedy path. Given those gaps, BEACN concluded that the cost and precedent risk outweighed the supported benefit, so the evidence-based vote was NO.

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
- finding: Requested: Funding for Hardware Wallet Maintenance 2026 covering production maintenance of Cardano hardware-wallet support.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,310,960
- finding: Deliverables: Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting and milestone-based disbursement controls
- finding: Deadline/expiry: 12 months of funding in 2026
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ada, split into 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The funded scope is limited to hardware-wallet compatibility, tooling, supporting libraries, release support, and vendor-required assurance, and is not intended to build a new wallet product or duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk for Ledger and Trezor users and integrators.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, independently_verifiable, high materiality): The proposer claims the requested withdrawal does not breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 at the time of submission, either alone or in aggregate.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal says audit and oversight costs are included in the overhead and administration fee, with independent oversight by Intersect and technically capable third parties plus milestone-based disbursement controls.
- missing: Independent evidence for: The funded scope is limited to hardware-wallet compatibility, tooling, supporting libraries, release support, and vendor-required assurance, and is not intended to build a new wallet product or duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- missing: Independent evidence for: The proposer states that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk for Ledger and Trezor users and integrators.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1310960
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, split into 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The funded scope is limited to hardware-wallet compatibility, tooling, supporting libraries, release support, and vendor-required assurance, and is not intended to build a new wallet product or duplicate broader core-node, ledger, or general infrastructure maintenance budgets." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1310960
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, split into 1,272,777 ada for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has useful governance and administration evidence, including budget breakdown, voting references, NCL assertion, prior funding disclosure, and smart-contract oversight details, but the core value-for-money case for a high treasury ask rests mostly on asserted compatibility risk and a broad work package rather than detailed vendor identity, milestones, rates, or reproducible maintenance workload evidence in the supplied claims. A small cautionary nudge is justified because treasury stewardship and evidence quality are not fully satisfied by process controls alone.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The funded scope is limited to hardware-wallet compatibility, tooling, supporting libraries, release support, and vendor-required assurance, and is not intended to build a new wallet product or duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- Claims and evidence missing: Independent evidence for: The proposer states that continuous maintenance is needed because Cardano protocol evolution, vendor firmware and app release cycles, and wallet and dApp integration demand create compatibility risk for Ledger and Trezor users and integrators.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `490e102e09724620dece1c1c765d389b5ea15874acb635fa0cb0568f3c51c469`
- snapshot_bundle_hash: `8194e69b3ec43621303dae15c807f993bb9a910cd9040944a3c8de897ee5d88a`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2047, "NO": 0.7491, "YES": 0.0462}`

