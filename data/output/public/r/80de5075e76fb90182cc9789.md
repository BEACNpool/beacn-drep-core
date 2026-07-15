# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.66`; LLM lean `-0.02` recorded, not added) | Confidence: `0.72` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary nudge is justified because the request is large, principal is converted from ADA into USDM, and several important traction and return assumptions are supplied in the document without references despite the proposal relying heavily on treasury stewardship and evidence quality. The proposal does include risk disclosures, custody structure, reporting, and return mechanics, so the adjustment should remain small rather than substituting for the deterministic assessment.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Strike Finance Liquidity Deployment. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure. It asks the treasury for 9000000 ADA. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment, not grant funding.

A material claim remains proposer-asserted or thinly supported: The document says Strike accounted for more than 50% of Cardano trading activity over the past six months.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure
- finding: Recipient: independent council administrator for Strike Finance liquidity deployment
- finding: Stated amount: 9000000
- finding: Deliverables: Sell deployed ADA for USDM to provide stablecoin-denominated Strike V2 liquidity, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, Provide monthly public transparency reports covering deployment status, utilization, volume, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks, Provide third-party assurance reports at deployment confirmation, month 6, and month 12
- finding: Deadline/expiry: 12 months after deployment
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment, not grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA would be sold for USDM, modeled at ADA = 0.15 USD to produce about 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual return, or about 135,000 USD / 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike claims more than 1.13 billion USD cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity-provider profit.
- finding: Claim (adoption, proposer_asserted, high materiality): The document says Strike accounted for more than 50% of Cardano trading activity over the past six months.
- finding: Claim (adoption, supported_in_proposal, medium materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as 87,288,044 USD total volume, 410,800 total trades, 2,681 users, 30,105 USD revenue, and 1,246,007 USD peak open interest.
- missing: Independent evidence for: The document says Strike accounted for more than 50% of Cardano trading activity over the past six months.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment, not grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document says Strike accounted for more than 50% of Cardano trading activity over the past six months." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment, not grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is justified because the request is large, principal is converted from ADA into USDM, and several important traction and return assumptions are supplied in the document without references despite the proposal relying heavily on treasury stewardship and evidence quality. The proposal does include risk disclosures, custody structure, reporting, and return mechanics, so the adjustment should remain small rather than substituting for the deterministic assessment.
- Directional NO is supported by affirmative independent evidence of waste, duplication, excessive cost, or failed delivery — not by missing information.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The document says Strike accounted for more than 50% of Cardano trading activity over the past six months.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a33c408dc24a622d1eae5e4a27ad479846cec31e4a0e6c1034522d45e839f30d`
- snapshot_bundle_hash: `673411d3990bbf7e6d9ba6bf717481c08236397e6b34a9f73d73a8eea2de00e3`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

