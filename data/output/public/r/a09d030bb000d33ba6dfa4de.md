# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7808` | Readiness: `0.9`
> Reasoning layer (precomputed): A small cautionary negative nudge is warranted because the proposal asks for a large treasury withdrawal while core value claims around existing mainnet status, Sellout adoption, Yellowstone contracted deployment, and team track record are mostly proposer-asserted, and the repayment mechanism leaves material terms to later M1 contracting. The document does include milestones, oversight, audit, and reporting protections, so the nudge should remain modest rather than maximal.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, with Intersect as budget administrator through the Sundae Labs TRSC/PSSC framework. The requested work includes a secondary ticket marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent smart-contract audit, a launch campaign, public metrics, and quarterly reporting over five milestones in eight months.

Several proposal details were clear and supported in the document: the amount requested, the 8-month schedule, the 3% Intersect administration fee, the list of Phase 2 deliverables, the proposed revenue-share repayment mechanism, and the oversight protections such as milestone-gated disbursement, contingency return, reporting, audit, and TRSC/PSSC oversight. However, several important value claims were still mostly proposer-asserted rather than independently evidenced, including that Phase 1 is already live on Cardano mainnet, Sellout’s user and ticketing scale, the Yellowstone Club anchor deployment, and Anvil’s delivery track record. The revenue-share base and cadence were also not finalized in the document and were deferred to later M1 contracting.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by public chain evidence independently verifying the applicable Net Change Limit, plus replayable independent evidence for the key claims around Phase 1 mainnet status, Sellout adoption, the anchor deployment, and delivery assurance, including the missing independent assurance and dependency map.

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
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: Intersect as budget administrator for disbursement through the Sundae Labs TRSC/PSSC framework, with Anvil Development Agency and Sellout as delivery parties.
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, and reselling tickets with on-chain settlement, Smart-contract-level royalty enforcement for configured artist and venue shares, Per-event anti-scalping controls including price ceilings, transfer limits, identity-binding compatibility, and time restrictions, Custodial wallet onboarding inside Sellout's existing user flow with self-custody export, Organizer dashboard and tools for resale parameters, ticket lifecycle data, royalty distributions, and verification, Independent third-party smart-contract security audit with remediation report, Public launch campaign including Big Storm campaign and three trade-show activations, Public metrics dashboard and quarterly reporting
- finding: Deadline/expiry: Five milestones over 8 months
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded entirely by Sellout with over $130,000 invested.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months and includes a 3% Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 will deliver a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and a professional launch campaign.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 series is presented as a contracted anchor deployment projected to move more than $6 million through Cardano in Year 1, based on $5.88 million historical 2025 activity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism using 25% of fees until reimbursement, then a permanent 5% fee afterward.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded entirely by Sellout with over $130,000 invested.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The Yellowstone Club 2026 series is presented as a contracted anchor deployment projected to move more than $6 million through Cardano in Year 1, based on $5.88 million historical 2025 activity.
- missing: Independent evidence for: Anvil claims a track record of 250+ Cardano projects delivered, 456,000+ assets minted, 50,000,000+ ADA staked through Anvil infrastructure, and 267,000+ on-chain transactions.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 4969231
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
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
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months and includes a 3% Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded entirely by Sellout with over $130,000 invested." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 4969231
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months and includes a 3% Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: A small cautionary negative nudge is warranted because the proposal asks for a large treasury withdrawal while core value claims around existing mainnet status, Sellout adoption, Yellowstone contracted deployment, and team track record are mostly proposer-asserted, and the repayment mechanism leaves material terms to later M1 contracting. The document does include milestones, oversight, audit, and reporting protections, so the nudge should remain modest rather than maximal.
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
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded entirely by Sellout with over $130,000 invested.
- Claims and evidence missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `6b0c013556ee0118b6f09090423749cc3bbc725dbafffb72a07335fcbe2412ad`
- snapshot_bundle_hash: `0d358d8e07d5e8f9b677cd3c338c4efdd48cea92c73537d78788b9538ce2b155`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

