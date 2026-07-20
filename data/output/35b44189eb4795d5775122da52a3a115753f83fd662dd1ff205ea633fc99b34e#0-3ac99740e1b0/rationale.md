# Rationale: 35b44189eb4795d5775122da52a3a115753f83fd662dd1ff205ea633fc99b34e#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.56`; LLM lean `-0.02` recorded, not added) | Confidence: `0.75` | Readiness: `0.9`
> Reasoning layer (precomputed): The claims show plausible public-benefit growth and some governance protections, but several high-materiality adoption and revenue projections are proposer-asserted while the request is large and includes substantial marketing and labor spend. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending nudge.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Withdraw 4,969,231 ada for Cardano Enterprise Adoption: Ticketing Platform. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency. It asks the treasury for 4,969,231 ADA. The strongest grounded claim is: The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months.

A material claim remains proposer-asserted or thinly supported: Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 4.97M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency.
- finding: Recipient: Anvil Development Agency, Inc. / Intersect as budget administrator
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding for Sellout users, Organizer tools and dashboards, Independent third-party security audit, Public launch campaign and trade-show activations, Public metrics dashboard and governance reporting
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 will deliver a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and launch marketing.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move over $6 million through Cardano in Year 1.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposer commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism using 25% of all fees until full reimbursement and 5% thereafter.
- missing: Independent evidence for: Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move over $6 million through Cardano in Year 1.
- missing: Independent evidence for: The proposal projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million+ ticket revenue on-chain, and 20,000+ new wallets.
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000." — so cost or precedent may outweigh the benefit.
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
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show plausible public-benefit growth and some governance protections, but several high-materiality adoption and revenue projections are proposer-asserted while the request is large and includes substantial marketing and labor spend. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending nudge.
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
- Claims and evidence missing: Independent evidence for: Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000.
- Claims and evidence missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `3ac99740e1b001698e5eb857ec52653402358158de83dae7957b95c5a06ac54e`
- snapshot_bundle_hash: `c595d7ee25f57258c123e4eae0eedc6703b32964b5110b77fa3f0525e616e4b2`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `4be57618f85e778396d883cd24aa46e529b1399c`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2263, "NO": 0.6475, "YES": 0.1263}`

