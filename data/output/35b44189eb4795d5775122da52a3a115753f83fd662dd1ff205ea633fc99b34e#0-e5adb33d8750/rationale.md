# Rationale: 35b44189eb4795d5775122da52a3a115753f83fd662dd1ff205ea633fc99b34e#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.11` (raw `-0.11` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7775` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth and includes milestone gating, audit commitments, budget detail, and a repayment structure, but several of the most material adoption and execution claims remain proposer-asserted within the extracted record, including Phase 1 live status, Sellout user volume, Yellowstone deployment economics, and projected usage. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment for plausible growth upside.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project.

The action requests 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, with Intersect acting as budget administrator under the Sundae Labs TRSC/PSSC framework. The proposal describes an 8-month, five-milestone plan covering a secondary ticket marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, a third-party smart-contract audit, public launch activity, a metrics dashboard, quarterly reports, and a final governance report.

Several parts of the proposal were well-supported in the submitted record: the anchor document was pinned and replayable, the budget included line items and a 3% Intersect administration fee, funds would be milestone-gated, and the proposal commits to repay 1,093,231 ada to the Treasury through a revenue-share mechanism. However, some of the most material claims remained proposer-asserted rather than independently verified in the extracted review, including that Phase 1 is already live on Cardano mainnet, Sellout’s user and ticketing volume, the Yellowstone Club deployment economics, and the projected adoption targets.

The review gates showed enough structure to review the action, and the strongest positive case was acknowledged: the repayment commitment and milestone framework are real supporting factors. But treasury votes require a higher bar because they spend shared ada and set precedent. To unblock a YES or NO vote, BEACN would need the Net Change Limit pinned and independently verified from public chain evidence, plus stronger independent evidence for the live Phase 1 mainnet claims and clearer assurance around execution risk, rollback, and remedies.

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
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.
- finding: Recipient: Intersect as budget administrator by prior agreement, holding and disbursing funds through the Sundae Labs TRSC/PSSC framework; project delivered by Anvil Development Agency and Sellout.
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, and reselling tickets with on-chain settlement, Smart-contract-level royalty enforcement for artists and venues, Configurable anti-scalping controls including price ceilings, transfer limits, identity-binding, and time-based restrictions, Custodial wallet onboarding inside Sellout's existing user flow with self-custody export described for testnet milestone, Organizer dashboard and tools for resale parameters, lifecycle data, royalty distributions, and ticket verification, Independent third-party smart-contract audit with report and remediation published, Public launch campaign including Big Storm marketing and three trade-show activations, Public metrics dashboard, quarterly reports, and final governance report
- finding: Deadline/expiry: 8 months across five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- finding: Claim (economic, proposer_asserted, medium materiality): Sellout has invested over $130,000 of its own capital into Phase 1.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal projects 12-month launch targets of 200+ on-chain events, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move $6M+ through Cardano in year one, with 2025 historical revenue of $5.88M.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal commits to repay $1,093,231 to the Cardano Treasury via a revenue-share mechanism, initially sending 25% of all fees until full reimbursement and 5% permanently afterward.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The proposal projects 12-month launch targets of 200+ on-chain events, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
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
- finding: Strongest YES: the proposal substantiates "The proposal commits to repay $1,093,231 to the Cardano Treasury via a revenue-share mechanism, initially sending 25% of all fees until full reimbursement and 5% permanently afterward." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal commits to repay $1,093,231 to the Cardano Treasury via a revenue-share mechanism, initially sending 25% of all fees until full reimbursement and 5% permanently afterward." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal is aligned with public-benefit ecosystem growth and includes milestone gating, audit commitments, budget detail, and a repayment structure, but several of the most material adoption and execution claims remain proposer-asserted within the extracted record, including Phase 1 live status, Sellout user volume, Yellowstone deployment economics, and projected usage. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment for plausible growth upside.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- Claims and evidence missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `e5adb33d8750d996405d4b0a66a24348f2e4500a02fa7d3852c13b9935893fc8`
- snapshot_bundle_hash: `e24cecc185bc7002b3c0a6f66bd5f72e9df6c40906aaa4aa9da00adecd556cb3`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5144, "NO": 0.3528, "YES": 0.1328}`

