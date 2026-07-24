# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.21` (binding treasury composite; advisory raw signal `-0.21`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7425` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth and includes explicit custody, reporting, return, and risk terms, but the extracted claims show many high-materiality adoption and assurance points are proposer-asserted or internally presented without references in the anchor document. Given the large treasury deployment and conversion into USDM, BEACN's hierarchy supports a small cautionary nudge for treasury stewardship and independently reproducible evidence quality, without treating missing information as a directional hard rejection.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal asks for 9,000,000 ADA for a 12-month treasury-owned liquidity deployment into Strike Finance V2. The ADA would be sold for USDM, modeled at ADA = 0.15 USD, to provide about 1,350,000 USDM of liquidity. The proposal says realized yield from the first six months would return to the Cardano Treasury at month 6, and all treasury-owned deployed assets, including remaining principal and realized yield, would return at month 12. It also commits to monthly public transparency reports and third-party assurance reports at deployment, month 6, and month 12.

Several core terms were supported in the proposal: the amount requested, the liquidity-deployment structure rather than grant funding, the USDM conversion model, the modeled 10% USD-denominated annual return with no guarantee, the independent multisig custody arrangement, and the listed risks. But important high-materiality claims were not independently evidenced in the review, including Strike’s reported cumulative volume, trades, users, protocol revenue, liquidity provider profit, and the expected audit and assurance process. The review also found missing treasury and risk details, including milestone-gated disbursement, independent assurance, and a dependency map.

Because this is a large TreasuryWithdrawal action that converts shared ADA into USDM and carries medium execution risk, BEACN applies a higher evidence bar. The pinned proposal anchor made the action reviewable, and the best YES case was that the basic request and structure were substantiated. The best hold case prevailed: BEACN needs the applicable Net Change Limit pinned and independently verified from public chain evidence, plus stronger replayable evidence for the unsupported material claims, before casting a YES or NO vote.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 9.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity.
- finding: Recipient: Independent multisig council administering deployment for Strike Finance V2 liquidity infrastructure
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital as USDM liquidity for Strike Finance V2, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, Provide monthly public transparency reports covering deployment, utilization, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and risks, Publish third-party assurance reports at deployment confirmation, month 6, and month 12
- finding: Deadline/expiry: 12 months from deployment; month-6 yield distribution
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual percentage return, or about 135,000 USD / 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports over 1.13 billion USD in cumulative volume, roughly one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as showing 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, 30,105 USD total V2 revenue, and peak open interest of 1,246,007 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The Strike Liquidity Provider vault is described as having 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 69,537.24 USD all-time P&L, 1.15% maximum drawdown, and 208 depositors after two months.
- missing: Independent evidence for: Strike reports over 1.13 billion USD in cumulative volume, roughly one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposal states that an official audit by Christian Schmitz is expected to be finalized by July 1, 2026 and that assurance reports will verify deployment, balances, P&L, drawdown, and distributions against on-chain data.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9000000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.66
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike reports over 1.13 billion USD in cumulative volume, roughly one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 9000000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal is aligned with public-benefit ecosystem growth and includes explicit custody, reporting, return, and risk terms, but the extracted claims show many high-materiality adoption and assurance points are proposer-asserted or internally presented without references in the anchor document. Given the large treasury deployment and conversion into USDM, BEACN's hierarchy supports a small cautionary nudge for treasury stewardship and independently reproducible evidence quality, without treating missing information as a directional hard rejection.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike reports over 1.13 billion USD in cumulative volume, roughly one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The proposal states that an official audit by Christian Schmitz is expected to be finalized by July 1, 2026 and that assurance reports will verify deployment, balances, P&L, drawdown, and distributions against on-chain data.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `f6d1991ed73475bc66221ebb197e42ec970100641a37413e71a245899d9cae2f`
- snapshot_bundle_hash: `ddfa1217a3ec1639efbce4b49fd6b831aef22f55571ba31c5793ac4c574c8eec`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `2d4ca1500b8dba4c613121f0e0daabae335dbd3a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4992, "NO": 0.4514, "YES": 0.0494}`

