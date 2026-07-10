# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal, especially the missing `treasury_amount_lovelace` field. This is a conservative, evidence-based hold, not a rejection of Eternl or its usefulness.

The proposal requested ₳2,350,000 for 12 months of Eternl operations, maintenance, infrastructure, support, audits, and development from August 2026 through July 2027. The proposer said this would cover about $420,000 in annual costs, fund 6.0 FTE, support paid Pro plans, convert up to $420,000 worth of Ada into stablecoins, return excess Ada to the treasury, and commission independent fund-use audits in February and August 2027. Several financial commitments were supported in the proposal itself, including the requested Ada amount, the stated cost basis, the staffing model, the Pro-plan pricing, and the stablecoin/return mechanism.

The review could not reach a directional YES or NO because key gates did not clear. Intake was blocked because the required treasury amount field was missing. Claims and evidence were thin because some important adoption claims, including platform availability and install counts, relied on proposer assertion rather than independent evidence. Treasury analysis was incomplete because milestone-gated disbursement and cost-benefit clarity were missing. Risk review remained unknown or incomplete because independent assurance and a dependency map were missing.

A YES case exists: the proposal does substantiate its own cost request and annual funding logic. A NO case also exists: material claims remained unsupported, and treasury spending has a higher evidence bar because it uses shared ADA and sets precedent. To unblock a directional vote, BEACN would need the missing treasury amount field, independent evidence for the key adoption claims, clearer milestone-gated disbursement and cost-benefit analysis, plus stronger independent assurance and dependency mapping.

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
- finding: Requested: 12 months of operations, maintenance, and improvements for the Eternl Cardano light wallet, including frontend, backend, infrastructure, support, administration, audits, and governance tooling.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: ₳2,350,000
- finding: Deliverables: Maintain and develop Eternl frontend across web, browser extension, Android, iOS, and beta channels, Maintain backend infrastructure including multi-region servers, Cardano nodes, DBSync/indexers, app servers, metadata aggregation, and monitoring, Provide Discord and Telegram user support, bug triage, ecosystem project support, wiki updates, and educational videos, Introduce Eternl Pro plans priced at $96/year for Personal and $360/year for Company, Convert up to $420,000 worth of Ada into stablecoins, place funds in a public company wallet, and return Ada above that amount to the treasury, Commission independent fund-use audits in February 2027 and August 2027, Publish Pro plan earnings reports and repayment or donation transaction hashes, Continue work on Eternl Core rewrite, Eternl Hub, enhanced hardware wallet support, wallet data export, and governance tooling
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 of annual costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The team says 10 people contribute to Eternl and this proposal funds 6.0 FTE at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce paid Pro plans at $96/year for personal users and $360/year for company users, and says about 5,500 paying users would fully cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl states it has about 100,000 browser extension installs and about 30,000 installs across Android and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal commits to converting up to $420,000 worth of Ada into stablecoins, holding funds in a public company wallet, and returning Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- missing: Independent evidence for: Eternl states it has about 100,000 browser extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: The proposer says 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: The proposer says that without treasury funding, Eternl may need to let developers go, scale down to essential maintenance, focus outside the Cardano ecosystem, or remove the free option.
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
- finding: Strongest NO: a material claim is unsupported — "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." — so cost or precedent may outweigh the benefit.
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
- Claims and evidence missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- Claims and evidence missing: Independent evidence for: Eternl states it has about 100,000 browser extension installs and about 30,000 installs across Android and iOS.
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
- input_hash: `e287cc3815789db24131d0129b75e6add9d999cd8b04670ad83aea763fed580e`
- snapshot_bundle_hash: `08427cf031b78bb51f2ee17b213bd948623036a46e53fa372751efe23d712a6b`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

