# Rationale: 35b44189eb4795d5775122da52a3a115753f83fd662dd1ff205ea633fc99b34e#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.11`; LLM lean `-0.02` recorded, not added) | Confidence: `0.75` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth and includes milestone gating, repayment terms, oversight, and concrete deliverables, but several high-materiality adoption and prior-delivery claims remain proposer-asserted within the document rather than evidenced there. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge despite the potential enterprise adoption upside.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Withdraw 4,969,231 ada for Cardano Enterprise Adoption: Ticketing Platform. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign. It asks the treasury for 4,969,231 ADA. The strongest grounded claim is: The withdrawal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursements.

A material claim remains proposer-asserted or thinly supported: Phase 1 is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.

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
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: Anvil Development Agency, Inc. / Intersect as budget administrator under the TRSC/PSSC framework
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding inside Sellout's flow, Organizer dashboard and lifecycle tools, Independent third-party security audit with remediation report, Public launch campaign and trade-show activations, Public metrics dashboard and quarterly reporting
- finding: Deadline/expiry: 8 months across five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- finding: Claim (economic, proposer_asserted, medium materiality): Sellout has invested over $130,000 of its own capital into Phase 1.
- finding: Claim (economic, supported_in_proposal, high materiality): The withdrawal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursements.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed Phase 2 deliverables include a secondary marketplace, smart-contract royalty splits, anti-scalping rules, wallet onboarding, organizer tools, an independent audit, and launch amplification.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism using 25% of fees until reimbursement and 5% thereafter.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6M+ ticket revenue on-chain, and 20,000+ new wallets.
- missing: Independent evidence for: Phase 1 is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
- missing: Independent evidence for: The proposal projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6M+ ticket revenue on-chain, and 20,000+ new wallets.
- missing: Independent evidence for: Sellout is described as having 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
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
- finding: Strongest YES: the proposal substantiates "The withdrawal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursements." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The withdrawal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursements." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal is aligned with public-benefit ecosystem growth and includes milestone gating, repayment terms, oversight, and concrete deliverables, but several high-materiality adoption and prior-delivery claims remain proposer-asserted within the document rather than evidenced there. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge despite the potential enterprise adoption upside.
- Directional NO is supported by affirmative independent evidence of waste, duplication, excessive cost, or failed delivery — not by missing information.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- Claims and evidence missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `bb2058589aee333f52eeb8d9351e28ac8e617b7862913dd58e81ab216b0f2e08`
- snapshot_bundle_hash: `00c7066773cddf93ed8f16854c69e97dbeb20f9ec8f4928713b9d155c2687742`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2263, "NO": 0.6475, "YES": 0.1263}`

