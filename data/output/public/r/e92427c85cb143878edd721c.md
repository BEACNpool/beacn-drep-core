# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal was missing: the review could not confirm `treasury_amount_lovelace`, even though the proposal text requests 9,832,979 ADA. For a treasury action, that missing baseline evidence blocks a responsible directional vote.

The proposal asks for 18 months of funding to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with milestones covering legal setup, technical migration, public dashboards, board election, asset transfer, operations, and quarterly reporting. It claims Blockfrost is important Cardano infrastructure, citing survey growth from 39.3% usage in 2022 to 71.5% in 2025, and it provides a budget split across staffing, operations and infrastructure, and legal/accounting costs. The review found some claims supported in the proposal, including what Blockfrost does, the commitment to transfer assets into community stewardship, and the requested budget structure.

However, several important claims remained unsupported by independent evidence, including last month’s usage figures, the claim that most Cardano epochs see more than 50% of transactions submitted through Blockfrost, and the public-good financing claim around free-tier traffic. The treasury review also lacked a sustainability path and clear cost-benefit analysis, while the risk review lacked independent assurance and a dependency map. Execution risk was assessed as medium.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by the missing treasury withdrawal amount in lovelace, independent evidence for the major usage and transaction-share claims, clearer sustainability and cost-benefit evidence, and stronger assurance around execution dependencies and governance risk.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent not-for-profit, including 18 months of transition and operations funding.
- finding: Recipient: Input Output / Blockfrost transition under Intersect/CDH administration; exact treasury withdrawal recipient is not stated in document.
- finding: Stated amount: 9,832,979 ADA
- finding: Deliverables: Not-for-profit entity established or host-organization agreement signed under preliminary board in Q3 2026, Technical transition architecture and migration plan published for community review in Q3 2026, Public usage dashboard live in Q3 2026, Board election held via on-chain voting under published rules in Q4 2026, Newly elected board formally assumes mandate by Q4 2026 / no later than end of Q1 2027, All public API traffic for mainnet, preview, and preprod served by the new stack in Q1 2027, Blockfrost source code, trademarks, domain names, and associated assets legally transferred to the governing entity in Q1 2027, Sustainability consultation and proposal published in Q2-Q3 2027, Public API operated at minimum 99% monthly uptime SLA during 2027 operational milestones, Quarterly reports published covering technical metrics and budget summary
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states Blockfrost usage in the Cardano Foundation developer ecosystem survey grew from 39.3% in 2022 to 71.5% in 2025, with links to the cited survey pages.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 rps, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance this public-good operation.
- missing: Independent evidence for: The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 rps, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance this public-good operation.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- missing: sustainability path
- missing: cost-benefit clarity
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 rps, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 rps, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `ae4f57c7dfe309d3da9cb5ca56ece188810cf8f10657bfbe745e31300cc448aa`
- snapshot_bundle_hash: `1550aa2300d51911acc9548f28cd6da0a21bc9f78b14d5e9c21c6b5cbc470e56`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

