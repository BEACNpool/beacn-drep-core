# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence needed to responsibly vote yes or no on a treasury withdrawal. This is a conservative, evidence-based hold, not a rejection of Eternl or its work.

The proposal requested ₳2,350,000 for 12 months of Eternl operations, maintenance, support, infrastructure, governance tooling, audits, and product improvements from August 2026 through July 2027. The proposer supported several basic budget and operating claims inside the proposal, including the stated $420,000 annual cost, 6.0 FTE across 10 contributors, planned paid Pro plans, stablecoin conversion plans, repayment commitments, and semiannual fund-use audits. The review also accepted that Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.

The hold came from what was not yet reviewable. For a treasury withdrawal, the structured review was missing the required `treasury_amount_lovelace` field, a complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. Several major adoption claims also lacked independent evidence, including the claimed 100,000 browser extension installs, 30,000 mobile installs, and 10-18% share of Cardano mainnet transactions.

A directional vote would be unblocked by a complete treasury withdrawal record, especially the missing lovelace amount, plus a line-item budget, milestone-gated disbursement plan, independent evidence for the adoption and transaction-share claims, and clearer mitigation and assurance evidence for execution and governance risks. Until that baseline evidence is present, BEACN abstained rather than pretend certainty.

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
- finding: Requested: 12 months of Eternl operations, maintenance, and improvements, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, audits of fund use, and oversight metrics.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: ₳2,350,000 at about $0.1787 per Ada
- finding: Deliverables: Maintain and develop Eternl frontend across web, browser extension, iOS, Android, and beta channels, Maintain backend infrastructure including multi-region servers, Cardano nodes, DBSync indexers, application servers, metadata aggregation, Hub services, monitoring, alerting, and incident response, Provide user support through Discord, Telegram, public channels, project support, wiki updates, and educational videos, Enhance governance tooling including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Develop upcoming features including Eternl Core rewrite, Eternl Hub, enhanced hardware wallet support, Bluetooth mobile support, and wallet data export, Perform independent audits of treasury fund use in February 2027 and August 2027, Publish oversight metrics including balances, conversion rates, transaction hashes, and repayment hashes
- finding: Deadline/expiry: Delivery period is August 2026 to July 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000 to cover approximately $420,000 in annual operating costs for a 12-month period.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposed budget funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce paid Pro plans at $96 per year for personal users and $360 per year for company users.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposer states that about 5,500 Pro users, roughly 4.2% of its stated install base, would fully cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs.
- missing: Independent evidence for: The proposer states Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs.
- missing: Independent evidence for: The proposer states 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposer states Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposer states Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs.
- Claims and evidence missing: Independent evidence for: The proposer states 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- input_hash: `9a39441a395fb0136175f9de742e849bd719f63c0ca677f5cc2d02b38430d52a`
- snapshot_bundle_hash: `0cf7be90640f132eac23b1c03ed2afee7620b2c85b9b890d013f34d4e2d861a1`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

