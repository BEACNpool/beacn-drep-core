# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.33` (binding treasury composite; advisory raw signal `-0.33`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7725` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims show a plausible public-benefit case for maintaining established wallet infrastructure, but several high-materiality adoption and dependency claims are asserted rather than evidenced in the document, and the deterministic assessment already marks claims and evidence as thin. A small cautionary nudge is justified because treasury stewardship and evidence quality remain weaker than the proposal's ecosystem-growth narrative.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Eternl or its usefulness.

The proposal requests ₳2,350,000 for 12 months of Eternl operations, maintenance, support, infrastructure, audits, governance tooling, Pro plan rollout, Core rewrite, Hub work, hardware wallet support, and export improvements from August 2026 through July 2027. The proposer says this equals about $420,000 in annual costs, with the budget split across frontend, backend, support, administration, and audits. The proposal also says up to $420,000 worth of Ada would be converted to stablecoins, placed in a public company wallet, and any Ada above that amount returned to the treasury.

Several important claims were supported in the proposal, including that Eternl is a non-custodial Cardano light wallet across web, browser extension, Android, and iOS; the requested amount and budget allocation; the Pro plan break-even claim; and the planned independent audits of treasury fund use. Other material claims were still only proposer-asserted, especially the claimed 100,000 browser extension installs, 30,000 combined mobile installs, and 10-18% share of Cardano mainnet transactions. Because this is a treasury withdrawal, BEACN applies elevated scrutiny: proposer assertions alone are not enough when shared ADA is being spent.

The review found a pinned and replayable proposal anchor, but the claims-and-evidence status remained thin, execution risk was unknown, and missing items included milestone-gated disbursement, cost-benefit clarity, independent assurance, and a dependency map. A directional YES or NO would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus stronger independent evidence for the high-materiality adoption and usage claims and clearer treasury-risk controls such as milestone gating and assurance.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
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
- finding: Requested: Treasury withdrawal for 12 months of Eternl operations, maintenance, and improvements from August 2026 to July 2027.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend and backend maintenance and development, Backend infrastructure and operations, User support, Day-to-day operations, Independent audits of treasury fund use and oversight metrics, Eternl Pro plan rollout for personal and company users, Governance tooling enhancements, Eternl Core rewrite, Eternl Hub, enhanced hardware wallet support, and wallet data export improvements
- finding: Deadline/expiry: July 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is allocated as 55% frontend, 25% backend, 5% support, 13% admin, and 2% audits.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl says it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl claims that about 5,500 Pro plan users, or 4.2% of its stated install base, would fully cover the annual $420,000 cost.
- finding: Claim (economic, supported_in_proposal, high materiality): After withdrawal, Eternl says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl says it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined.
- missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl states that if it does not receive treasury funds and paid licenses are insufficient beyond August, it may let developers go, reduce to essential maintenance, shift focus outside Cardano, or remove the free option.
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
- finding: Strongest NO: a material claim is unsupported — "Eternl says it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show a plausible public-benefit case for maintaining established wallet infrastructure, but several high-materiality adoption and dependency claims are asserted rather than evidenced in the document, and the deterministic assessment already marks claims and evidence as thin. A small cautionary nudge is justified because treasury stewardship and evidence quality remain weaker than the proposal's ecosystem-growth narrative.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl says it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined.
- Claims and evidence missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `857436f9e4346db22d5978f02fe8c59fcd924e50493bbf99012cdfb2f02cbebe`
- snapshot_bundle_hash: `17f8ec5e75ec4d55ece7496f45e8e33fff055ea90a822c4e572d5bde81b7929e`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `2d4ca1500b8dba4c613121f0e0daabae335dbd3a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4515, "NO": 0.5045, "YES": 0.044}`

