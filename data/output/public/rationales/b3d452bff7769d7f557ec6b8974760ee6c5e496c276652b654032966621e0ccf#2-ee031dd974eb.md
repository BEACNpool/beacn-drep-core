# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#2
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.08` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.74` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a security-critical continuity proposal with concrete budget totals, governance-process references, and oversight mechanics, but several core benefit claims about breakage risk, adoption value, and scope necessity remain proposer asserted in the anchor text. Because the deterministic assessment is already ready and hard gates are binding, the evidence mix does not justify an additional directional nudge beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 1,310,960 ada for 2026 hardware wallet maintenance: 1,272,777 ada for Cardano hardware wallet maintenance and compatibility assurance, plus a 38,183 ada Intersect administration fee. The stated work covers 12 months of Ledger and Trezor compatibility updates, interoperability libraries, cardano-hw-cli maintenance, integrator support, externally maintained component integration where relevant, vendor-required audits, capped time-and-materials reporting, and milestone-based disbursement controls.

Several governance and process claims were supported: the proposal anchor was pinned and replayable, the action came through the 2026 Intersect Budget Process Hydra Voting phase with the required 67% support threshold, and the proposal describes Intersect oversight, reporting obligations, milestone controls, and a Sundae Labs treasury smart contract framework. The amount requested was clearly stated, and the proposal disclosed related prior funding links.

The hold is conservative and evidence-based. The review found thin claim evidence, unknown execution risk, no pinned independent Net Change Limit verification, no clear sustainability path, no clear cost-benefit analysis, no independent assurance, and no rollback or remedy path. A directional vote would be unblocked by public, replayable evidence verifying the Net Change Limit position and stronger independent evidence for the continuity-maintenance claims, execution assurances, cost-benefit case, sustainability path, and remedy controls.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: ratified
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
- finding: Requested: Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, interoperability libraries and cardano-hw-cli maintenance, developer support for integrators, externally maintained component integration support where relevant, and vendor-required product or security audits.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1,310,960
- finding: Deliverables: 12 months of production maintenance of Cardano hardware-wallet support, Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting, Milestone-based disbursement controls
- finding: Deadline/expiry: 2026 funding period; exact delivery deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance and Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The funded work is described as a 12-month continuity scope for existing Cardano hardware-wallet support rather than a new wallet product.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that without continuous maintenance, Cardano, Ledger, or Trezor changes can cause users and integrators to lose secure hardware-wallet access.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal claims the work supports Cardano strategy Pillar 1 by preserving a secure, reliable, interoperable signing layer and Pillar 2 by supporting secure UX, developer experience, and compatibility.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, independently_verifiable, high materiality): The requested amount is claimed not to breach the 350M ada Net Change Limit covering Epoch 613 to Epoch 713 at the time of submission, either alone or in aggregate.
- missing: Independent evidence for: The funded work is described as a 12-month continuity scope for existing Cardano hardware-wallet support rather than a new wallet product.
- missing: Independent evidence for: The proposal states that without continuous maintenance, Cardano, Ledger, or Trezor changes can cause users and integrators to lose secure hardware-wallet access.
- missing: Independent evidence for: The proposal claims the work supports Cardano strategy Pillar 1 by preserving a secure, reliable, interoperable signing layer and Pillar 2 by supporting secure UX, developer experience, and compatibility.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance and Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The funded work is described as a 12-month continuity scope for existing Cardano hardware-wallet support rather than a new wallet product." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for Cardano Hardware Wallet Maintenance and Compatibility Assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The funded work is described as a 12-month continuity scope for existing Cardano hardware-wallet support rather than a new wallet product.
- Claims and evidence missing: Independent evidence for: The proposal states that without continuous maintenance, Cardano, Ledger, or Trezor changes can cause users and integrators to lose secure hardware-wallet access.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `ee031dd974eba472d3ff01202325fa22b374a087e4f455cc27a1094c4f11d0a7`
- snapshot_bundle_hash: `3800b01fcc33c5a219b68dee339f1792a1a1e04a1f0e57ecf37937f9bb325285`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `2d4ca1500b8dba4c613121f0e0daabae335dbd3a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.505, "NO": 0.3275, "YES": 0.1675}`

