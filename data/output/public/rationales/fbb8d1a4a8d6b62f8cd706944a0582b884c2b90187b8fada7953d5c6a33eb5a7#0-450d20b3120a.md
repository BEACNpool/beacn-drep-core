# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.78` (raw `-0.78` + doctrine-LLM nudge `+0.0`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal includes concrete budget, custody, audit, and repayment mechanics, but several high-materiality adoption and impact claims remain proposer-asserted, and the deterministic assessment already marks claims and evidence as thin; no additional discretionary nudge is justified beyond the engine's treatment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and the applicable Net Change Limit was not pinned and independently verified from public chain evidence. That makes a directional vote premature, even though parts of the proposal were reviewable and some claims were well supported.

The proposal asks for ₳2,350,000 for 12 months of Eternl operations, maintenance, and improvements from August 2026 through July 2027. The proposer says this covers about $420,000 in annual operating cost, spread across frontend work, backend infrastructure, support, administration, audits, and product improvements such as Eternl Pro, governance tooling, a Core rewrite, Eternl Hub, hardware wallet support, and data export improvements. The review found support in the proposal for the requested amount, budget split, staffing model, stablecoin conversion plan, return of excess Ada, voting-abstaining treasury account, planned independent audits, and the fact that Eternl is a non-custodial Cardano light wallet across web, extension, Android, and iOS.

The main unsupported areas were adoption and impact claims. The review did not find independent evidence for the claim that Eternl has about 100,000 browser extension installs and about 30,000 mobile installs, or for the claim that 10-18% of Cardano mainnet transactions are conducted through Eternl. The review also noted thin claims-and-evidence status, unknown execution risk, no documented milestone-gated disbursement, missing cost-benefit clarity, missing independent assurance, and no dependency map.

This is a conservative, evidence-based hold. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable public evidence for the adoption and transaction-share claims, clearer milestone-gated disbursement, clearer cost-benefit justification, and stronger independent assurance around execution risk.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 2.35M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements from August 2026 to July 2027.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Administrative operations, Periodic independent audits of treasury fund use and oversight metrics, Eternl Pro plan rollout, Governance tooling enhancements, Eternl Core rewrite, Eternl Hub, enhanced hardware wallet support, and wallet data export improvements
- finding: Deadline/expiry: July 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover an annual operating cost of about $420,000.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget allocates 55% to frontend, 25% to backend, 5% to support, 13% to admin, and 2% to audits.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs.
- finding: Claim (economic, supported_in_proposal, high materiality): If roughly 5,500 users, or about 4.2% of the install base, buy the Pro plan, Pro income would fully cover the annual $420,000 cost.
- missing: Independent evidence for: Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs.
- missing: Independent evidence for: The proposer states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs." — so cost or precedent may outweigh the benefit.
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
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Proposal clears individual quality floors but is not currently portfolio-eligible: insufficient remaining NCL capacity after higher-ranked proposals.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs.
- Claims and evidence missing: Independent evidence for: The proposer states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `450d20b3120accd8ed66905c9e670facbf714770b362d7d82b0e155bb3c197ec`
- snapshot_bundle_hash: `4271b4e8a8c80ba9f9dd48286490817ef9ae6e5e7ac1037e119a4cd08fd36e6b`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

