# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.78` (binding treasury composite; advisory raw signal `-0.78`; LLM lean `-0.02` recorded, not added) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The assessment says claims and evidence are thin, and several high-materiality claims central to treasury stewardship, including adoption scale, transaction share, future repayment, and audit execution, are mostly proposer-asserted rather than independently evidenced. Because the deterministic engine already treated the case as incomplete, only a small cautionary nudge is justified rather than a directional merits judgment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Eternl or its work.

The action asks for ₳2,350,000 for 12 months of Eternl operations, maintenance, infrastructure, support, governance tooling, administration, and audits from August 2026 through July 2027. The proposal supports several basic budget and scope claims: Eternl is described as a non-custodial Cardano light wallet across web, browser extension, Android, and iOS; the request is tied to about $420,000 in annual operating costs; and the budget is framed as 6.0 FTE across 10 contributors at $70,000 per FTE. It also describes future paid Pro plans and says about 5,500 paying users would cover those annual costs.

The review found that several high-materiality treasury stewardship claims were still mostly proposer-asserted rather than independently evidenced. These include the plan to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return excess Ada to the treasury; the proposed independent audits in February 2027 and August 2027; the claimed install counts; and the claim that 10-18% of Cardano mainnet transactions are conducted via Eternl. The review also noted no documented milestone-gated disbursement, missing cost-benefit clarity, missing independent assurance, and an unknown execution-risk picture.

The gates that passed were the presence of a pinned, replayable proposal anchor and a defensible strongest-YES case around Eternl’s basic wallet availability. The gates that did not clear were the higher treasury evidence bar, independent assurance for key fund-handling claims, and the required verified Net Change Limit. A directional vote would be unblocked by public chain evidence verifying the applicable Net Change Limit, plus independent evidence for the treasury flow, audit execution, repayment or refund mechanics, milestone-gated disbursement, and the other material claims now relying mainly on proposer assertion.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements, including frontend and backend work, infrastructure, support, administration, and audits/oversight.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: 12 months of frontend maintenance and cross-platform development, 12 months of backend infrastructure and operations, User support through Discord ticketing, Telegram, public channels, ecosystem project support, wiki updates, and educational videos, Day-to-day operations including release management, vendor and ecosystem coordination, code review, and security practices, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and governance proposal creation, Periodic independent audits of treasury fund use and implementation of oversight metrics
- finding: Deadline/expiry: August 2026 to July 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 of annual operating costs.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce paid Pro plans priced at $96 per year for personal users and $360 per year for companies, and says about 5,500 paying users would fully cover the annual $420,000 cost.
- finding: Claim (economic, proposer_asserted, high materiality): The team says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that independent audits by a party unaffiliated with Tastenkunst GmbH or the Eternl team will occur in February 2027 and August 2027 and will review custody, conversion, spending, balances, Pro plan income relevant to repayment, and treasury refunds or repayments.
- missing: Independent evidence for: The team says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: The proposal states that independent audits by a party unaffiliated with Tastenkunst GmbH or the Eternl team will occur in February 2027 and August 2027 and will review custody, conversion, spending, balances, Pro plan income relevant to repayment, and treasury refunds or repayments.
- missing: Independent evidence for: The proposal claims Eternl has about 100,000 browser extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: The proposal claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Strongest NO: a material claim is unsupported — "The team says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, and return any Ada above that amount to the treasury." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The assessment says claims and evidence are thin, and several high-materiality claims central to treasury stewardship, including adoption scale, transaction share, future repayment, and audit execution, are mostly proposer-asserted rather than independently evidenced. Because the deterministic engine already treated the case as incomplete, only a small cautionary nudge is justified rather than a directional merits judgment.
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
- Claims and evidence missing: Independent evidence for: The team says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, and return any Ada above that amount to the treasury.
- Claims and evidence missing: Independent evidence for: The proposal states that independent audits by a party unaffiliated with Tastenkunst GmbH or the Eternl team will occur in February 2027 and August 2027 and will review custody, conversion, spending, balances, Pro plan income relevant to repayment, and treasury refunds or repayments.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `297ec8f29b4b3842d3f6a32730f8fc10b5306bd9e67aa05dd2c1e168b77da01b`
- snapshot_bundle_hash: `91682770baf340117476e3f3735d7ecf04af96246658e481e6a8022268cb0111`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

