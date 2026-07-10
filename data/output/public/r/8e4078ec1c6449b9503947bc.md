# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the treasury withdrawal could not be responsibly reviewed without a complete baseline amount field: `treasury_amount_lovelace` was missing for a treasury action. This is a conservative, evidence-based hold, not a judgment that the Eternl funding request is good or bad.

The proposal requested 12 months of operations, maintenance, support, infrastructure, governance tooling work, administration, and oversight for the Eternl wallet. The anchor document stated a request of ₳2,350,000, described as about $420,000 of annual costs at about $0.1787 per Ada, with a budget split across frontend, backend, support, admin, and audits. It also described planned paid Personal and Company Pro plans, stablecoin conversion up to $420,000, possible return of excess Ada, semiannual repayment checks, and audits of treasury fund use in February 2027 and August 2027.

Several financial claims were supported inside the proposal, including the requested amount, budget allocation, paid plan assumptions, conversion plan, and repayment approach. But key adoption claims remained proposer assertions without independent evidence in the review, including the description of Eternl’s wallet role, its stated install counts, and the claim that 10-18% of Cardano mainnet transactions are conducted via Eternl. The treasury review was also incomplete because milestone-gated disbursement and cost-benefit clarity were missing, while the risk review lacked independent assurance and a dependency map.

The evidence that would unblock a directional vote is specific: the missing on-chain treasury amount in lovelace for the withdrawal, independent evidence for the major adoption and usage claims, clearer treasury cost-benefit support, milestone or disbursement safeguards, independent assurance, and a dependency map. Until that baseline evidence is present, BEACN abstained rather than pretending confidence it did not have.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: 12 months of operations, maintenance, and improvements for the Eternl non-custodial Cardano light wallet, including frontend and backend work, infrastructure, support, administration, and audits/oversight.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: ₳2,350,000 stated in anchor document; action metadata amount not stated in document context
- finding: Deliverables: Frontend maintenance and cross-platform development for browser extension, web/PWA, iOS, Android, and beta channels, Backend infrastructure and operations including multi-region servers, Cardano nodes, DBSync, application servers, metadata aggregation, and monitoring, User support through Discord ticketing, Telegram, public channels, ecosystem support, wiki updates, and educational videos, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Independent audits of treasury fund use and oversight metrics in February 2027 and August 2027
- finding: Deadline/expiry: 12-month delivery period, August 2026 to July 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 of annual costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 55% frontend, 25% backend, 5% support, 13% admin, and 2% audits.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce Personal and Company Pro plans priced at $96/year and $360/year, and says about 5,500 paying users would cover the $420,000 annual cost.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer says Eternl has about 100,000 browser extension installs and about 30,000 Android/iOS installs.
- finding: Claim (economic, supported_in_proposal, high materiality): After withdrawal, the proposer says it will convert up to $420,000 worth of Ada into stablecoins in a public company wallet and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- missing: Independent evidence for: The proposer says Eternl has about 100,000 browser extension installs and about 30,000 Android/iOS installs.
- missing: Independent evidence for: The proposer says 10-18% of Cardano mainnet transactions are conducted via Eternl and that Eternl has provided access across several platforms with basically zero downtime for over 5 years.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.78
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
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal asks for ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 of annual costs for 12 months." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal asks for ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 of annual costs for 12 months." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- Claims and evidence missing: Independent evidence for: The proposer says Eternl has about 100,000 browser extension installs and about 30,000 Android/iOS installs.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `4b6574d3a53c5bb48799a93a411a809cd9a43b82c8be3de5c9a97929bd0e6467`
- snapshot_bundle_hash: `277cf59215a73e64ee082e562ba7889a9acabfc1f08956b6b58c6ff2ebb79b4e`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

