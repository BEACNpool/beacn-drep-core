# Rationale: 35b44189eb4795d5775122da52a3a115753f83fd662dd1ff205ea633fc99b34e#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal was missing: `treasury_amount_lovelace`. Even though the proposal describes a request for 4,969,231 ada, the review record’s treasury analysis could not complete the required baseline evidence check for the actual withdrawal amount field.

The action requested funding for Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, with Intersect administering the funds through the Sundae Labs TRSC/PSSC framework. The proposal claimed it would deliver a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, a smart-contract audit, launch activity, public metrics, and quarterly reporting over eight months.

Some proposal-level claims were supported in the review, including the stated 4,969,231 ada request, the Phase 2 deliverables, the revenue-share repayment commitment, milestone gating, oversight, reporting, and audit commitments. But other important claims remained only proposer-asserted or lacked independent evidence, including that Phase 1 is already live on Cardano mainnet with the stated features and investment, and that Sellout has 200,000+ registered users, 250,000+ issued tickets, and 350+ annual events. The risk review was also incomplete because independent assurance and a rollback or remedy path were missing.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would require the missing `treasury_amount_lovelace` baseline field, independent evidence for the Phase 1 and adoption claims, and clearer assurance around execution risk, including independent assurance and a rollback or remedy path.

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
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.
- finding: Recipient: Intersect as budget administrator, holding and disbursing funds through the Sundae Labs TRSC/PSSC framework for the Anvil/Sellout project.
- finding: Stated amount: 4,969,231 ada
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding inside Sellout's existing flow, Organizer dashboard and ticket lifecycle tools, Independent third-party smart-contract security audit with published remediation, Public launch campaign and three trade-show activations, Public metrics dashboard and quarterly reporting
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, over 8 months and inclusive of a 3% Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 is intended to deliver a secondary ticket marketplace, smart-contract royalty enforcement, anti-scalping rules, wallet onboarding, organizer tools, a third-party audit, and launch amplification.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says Sellout has 200,000+ registered users, has issued 250,000+ tickets, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million or more in ticket revenue on-chain, and 20,000+ new wallets.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism using 25% of fees until reimbursement, then 5% permanently, with quarterly public reporting.
- missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested.
- missing: Independent evidence for: The proposal says Sellout has 200,000+ registered users, has issued 250,000+ tickets, and currently supports 350+ events annually.
- missing: Independent evidence for: The proposer projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million or more in ticket revenue on-chain, and 20,000+ new wallets.
- missing: Independent evidence for: The proposal states Anvil/Sellout have not received ada from the Cardano Treasury within the last 24 months.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, over 8 months and inclusive of a 3% Intersect administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, over 8 months and inclusive of a 3% Intersect administration fee." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested.
- Claims and evidence missing: Independent evidence for: The proposal says Sellout has 200,000+ registered users, has issued 250,000+ tickets, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `fea7f7aaa9ff81f12d58c99463d3e2782650f5d676740493acee0b9cf833c6cd`
- snapshot_bundle_hash: `aef9d2d5299862d9b08e71b40b76d23d66505a23c3460d8f0ac38f37a845db70`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

