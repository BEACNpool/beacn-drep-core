# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#2
Recommendation: **YES**
Score: `0.275` (raw `-0.08` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7887` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a security-critical continuity rationale, defined budget, milestone and oversight structure, and multiple independently checkable governance and custody references. The deterministic assessment is already ready and appears to have captured the material treasury, evidence, and risk factors, so no additional bounded nudge is justified.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Withdraw 1,310,960 ada for Hardware Wallet Maintenance 2026. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, including Ledger and Trezor compatibility updates, interoperability libraries, cardano-hw-cli, developer support, integration-path support, and vendor-required audits. It asks the treasury for 1,310,960 ADA. The strongest grounded claim is: The proposal requests 1,310,960 ADA to fund 12 months of Hardware Wallet Maintenance 2026.

A residual watch item: this claim remains proposer-asserted rather than independently shown: The requested work is scoped to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and is not intended to build a new wallet product.

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
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1,310,960
- finding: Deliverables: 12 months of production maintenance for Cardano hardware-wallet support, Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Milestone-based disbursement controls and transparent capped T&M reporting
- finding: Deadline/expiry: 2026 / 12 months, exact start and end dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ADA to fund 12 months of Hardware Wallet Maintenance 2026.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget consists of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The requested work is scoped to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and is not intended to build a new wallet product.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise cause users and integrators to lose secure hardware-wallet access.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The proposer states that the requested amount does not breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 at the time of submission.
- missing: Independent evidence for: The requested work is scoped to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and is not intended to build a new wallet product.
- missing: Independent evidence for: The proposer states that continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise cause users and integrators to lose secure hardware-wallet access.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA to fund 12 months of Hardware Wallet Maintenance 2026." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The requested work is scoped to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and is not intended to build a new wallet product." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA to fund 12 months of Hardware Wallet Maintenance 2026." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The requested work is scoped to compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and is not intended to build a new wallet product.
- Claims and evidence missing: Independent evidence for: The proposer states that continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise cause users and integrators to lose secure hardware-wallet access.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `f4498b9a39f61be45bb5ef97482144630a5661679ab760e6e1497bce6e034156`
- snapshot_bundle_hash: `9b570b04f5812c6f20d8206f44a3ecd02eb9c7024dfb1ee8020441397807e3a6`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `afd630a34be9d7440e2fac020ac552cde501098f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2043, "NO": 0.0461, "YES": 0.7495}`

