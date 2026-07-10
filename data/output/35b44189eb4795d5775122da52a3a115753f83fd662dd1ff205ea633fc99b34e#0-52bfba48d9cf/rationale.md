# Rationale: 35b44189eb4795d5775122da52a3a115753f83fd662dd1ff205ea633fc99b34e#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline treasury evidence: the required `treasury_amount_lovelace` field was missing for a treasury withdrawal. For a request to withdraw shared ADA, BEACN requires the basic amount and source fields to be complete and replayable before making a directional YES or NO vote.

The proposal asked for 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform over eight months, including a secondary resale marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, launch activity, and public reporting. The proposer stated that Phase 1 is already live on Cardano mainnet, that Sellout has substantial existing users and ticket volume, and that Yellowstone Club 2026 is an anchor deployment projected to move more than $6 million through Cardano in Year 1. The review found some proposal-level claims supported, including the requested amount, the planned Phase 2 deliverables, the repayment commitment, and the proposed treasury protections.

However, several important claims were not backed by independent evidence in the review. In particular, BEACN lacked independent evidence that Phase 1 is already live with the claimed Cardano functionality, and lacked independent evidence for the claimed Sellout user, ticket, and event numbers. The risk review also remained incomplete because independent assurance and a rollback or remedy path were missing. The claims-and-evidence section was therefore thin, and the synthesis was blocked.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the project’s goals. A directional vote would be unblocked by the missing treasury amount field being present and reviewable, plus independent public evidence for the live Phase 1 Cardano deployment, the Sellout adoption figures, and clearer assurance and remedy evidence for execution risk.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund Phase 2 of a Cardano-native ticketing platform: secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: Intersect as budget administrator through the Sundae Labs TRSC/PSSC framework, for Anvil Development Agency and Sellout.io project delivery.
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary ticket resale marketplace settling transactions on-chain, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding for Sellout users, Organizer dashboard/tools, Independent third-party security audit with remediation/reporting, Public launch campaign and trade-show activations, Public metrics dashboard and quarterly reporting
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000.
- finding: Claim (economic, supported_in_proposal, high materiality): The withdrawal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee over 8 months.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 will deliver a secondary marketplace, smart-contract royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and a professional launch campaign.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is contracted as an anchor deployment and is projected to move more than $6 million through Cardano in Year 1.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism using 25% of fees until reimbursement, then 5% permanently.
- missing: Independent evidence for: Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is contracted as an anchor deployment and is projected to move more than $6 million through Cardano in Year 1.
- missing: Independent evidence for: Anvil claims a record of 250+ Cardano projects delivered, 456,000+ assets minted, 50,000,000+ ADA staked through its infrastructure, and 267,000+ on-chain transactions.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.82
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The withdrawal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee over 8 months." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The withdrawal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee over 8 months." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000.
- Claims and evidence missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `52bfba48d9cfdcf53df74fbde7a002e9277f32ee4af7727d7524a806c9d4f3e6`
- snapshot_bundle_hash: `a8b3325cf0526007d08ccfd9bd5f1f36f184e80d34dc26a9074171900da520df`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

