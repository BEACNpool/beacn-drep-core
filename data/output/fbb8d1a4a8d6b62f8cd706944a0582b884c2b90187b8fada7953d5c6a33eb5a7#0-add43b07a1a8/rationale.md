# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.78` (binding treasury composite; advisory raw signal `-0.78`; LLM lean `-0.02` recorded, not added) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure value and some concrete treasury-handling commitments, but the assessment says evidence is thin and several high-materiality adoption, continuity, uptime, and sustainability claims are proposer-asserted rather than verified. The non-milestone structure and large up-front treasury request justify only a small cautionary nudge because the deterministic engine already handles hard gates and treasury analysis.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027. It says the funds would cover maintenance, infrastructure, support, administration, audits of treasury fund use, Pro plan rollout, governance tooling, the Eternl Core rewrite, Eternl Hub, hardware wallet improvements, and wallet data export work. The proposer also says the request is worth about $420,000 at $0.1787 per Ada, that up to $420,000 worth of Ada would be converted into stablecoins, and that any Ada above that amount would be returned to the treasury.

Several important claims were supported in the proposal itself, including the amount requested, the 12-month delivery window, the proposed treasury-handling approach, the commitment not to delegate treasury-held Ada to an SPO before conversion or return, and the planned February 2027 and August 2027 audits of fund use. But other material claims remained proposer-asserted rather than independently verified, including the 6.0 FTE cost basis, install counts, the number of Pro users needed for sustainability, the share of Cardano mainnet transactions attributed to Eternl, and the claim of basically zero downtime over more than five years.

This is therefore a conservative, evidence-based hold, not a rejection of Eternl’s usefulness. The review gates found a pinned and replayable proposal anchor, but treasury scrutiny remains elevated, claims evidence is thin, execution risk is unknown, there is no milestone-gated disbursement documented, and cost-benefit clarity, independent assurance, and a dependency map are missing. A directional vote would be unblocked by the verified Net Change Limit from public chain evidence, plus stronger independent evidence for the material cost, adoption, continuity, and sustainability claims.

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
- finding: Requested: Treasury withdrawal for 12 months of Eternl operations, maintenance, infrastructure, support, audits/oversight, and continued development while introducing paid Pro plans.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Administrative operations, Periodic independent audits of treasury fund use and oversight metrics, Eternl Pro plan rollout, Governance tooling enhancements, Eternl Core rewrite, Eternl Hub, enhanced hardware wallet support, and wallet data export improvements
- finding: Deadline/expiry: Delivery period August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $420,000 using $0.1787 per Ada, to fund a 12-month delivery period from August 2026 to July 2027.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE, and states this is a lower-bound rate compared with other proposals exceeding $200,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, supported_in_proposal, medium materiality): The proposer commits that treasury-held Ada before conversion or return will be held in an auditable account, not delegated to an SPO, and delegated to the predefined abstain voting option.
- finding: Claim (economic, supported_in_proposal, high materiality): The audits allocation is for independent audits of treasury fund use in February 2027 and August 2027, covering custody, conversion, spending, balances, Pro plan income relevant to repayment, and refunds or repayments, rather than technical security audits.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl says it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs, and that roughly 5,500 Pro users would cover its $420,000 annual cost.
- missing: Independent evidence for: The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE, and states this is a lower-bound rate compared with other proposals exceeding $200,000 per FTE.
- missing: Independent evidence for: Eternl says it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs, and that roughly 5,500 Pro users would cover its $420,000 annual cost.
- missing: Independent evidence for: The proposal states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: The proposer states that Eternl has provided multi-platform Cardano access with basically zero downtime for over five years.
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using $0.1787 per Ada, to fund a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE, and states this is a lower-bound rate compared with other proposals exceeding $200,000 per FTE." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using $0.1787 per Ada, to fund a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show plausible public-benefit infrastructure value and some concrete treasury-handling commitments, but the assessment says evidence is thin and several high-materiality adoption, continuity, uptime, and sustainability claims are proposer-asserted rather than verified. The non-milestone structure and large up-front treasury request justify only a small cautionary nudge because the deterministic engine already handles hard gates and treasury analysis.
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
- Claims and evidence missing: Independent evidence for: The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE, and states this is a lower-bound rate compared with other proposals exceeding $200,000 per FTE.
- Claims and evidence missing: Independent evidence for: Eternl says it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs, and that roughly 5,500 Pro users would cover its $420,000 annual cost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `add43b07a1a8367a484ca1036a0f258f16f0e3e07c9226d261f261b7596a2596`
- snapshot_bundle_hash: `973bc6a219721797c7ecf450d46167bd6bd6a85994b3b43cbcfb0141ac6ada8f`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

