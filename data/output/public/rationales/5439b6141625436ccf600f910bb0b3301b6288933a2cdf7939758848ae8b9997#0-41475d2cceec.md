# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline treasury field was missing: `treasury_amount_lovelace` was not available for a TreasuryWithdrawals action. Even though the anchor document states a request of 9,832,979 ADA, the deterministic review could not responsibly issue a directional vote while the machine-readable treasury amount was missing.

The proposal requested 18 months of funding to transition Blockfrost into a free, community-governed public API/public good under an independent not-for-profit structure. It described funding of 9,832,979 ADA, or 1,868,266 USD at 0.19 USD per ADA, for transition and operations. It also proposed deliverables including legal setup or a host-organization agreement, a technical transition plan, a public usage dashboard, board election rules and voting, service for mainnet, preview, and preprod traffic, transfer of source code, trademarks, domains, and related assets, public consultation on sustainability, 99% monthly uptime, and quarterly technical and budget reports.

Some claims were supported in the proposal, including the stated ADA request, the staffing and operations budget split, the proposed five-seat governance model, and the use of delivery assurance and budget-management structures. The review also found an independently verifiable adoption claim from Cardano Foundation survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025. But several important claims remained only proposer-asserted or thinly evidenced, including the future free community-governed API model, the transfer of Blockfrost intellectual property, recent usage figures, and the claim that Blockfrost submits more than 50% of transactions in most epochs.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the idea. The intake and synthesis gates were blocked by the missing `treasury_amount_lovelace` field, claims-and-evidence was thin, treasury analysis lacked sustainability path and cost-benefit clarity, and risk review lacked independent assurance and a dependency map. A directional vote would be unblocked by the missing treasury amount field, independent evidence for the governance and IP-transfer claims, clearer sustainability and cost-benefit evidence, and stronger assurance and dependency documentation.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public API/public good under an independent not-for-profit, with 18 months of transition and operations funding.
- finding: Recipient: Input Output / Blockfrost transition administered through Intersect and CDH contract structures, with the eventual governing not-for-profit entity not yet determined.
- finding: Stated amount: 9,832,979 ADA stated in the anchor document; treasury_amount_lovelace is missing in the deterministic assessment.
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under the preliminary board., Publish technical transition architecture and migration plan for community review., Launch a public usage dashboard., Hold a board election via on-chain voting under publicly published rules., Serve all public API traffic for mainnet, preview, and preprod from the new stack., Legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity., Open public consultation on long-term sustainability and publish a proposal for community feedback., Operate the public API at minimum 99% monthly uptime and publish quarterly technical and budget reports.
- finding: Deadline/expiry: 18 months of operations including transition period, with milestones from Q3 2026 through 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,832,979 ADA, described as 1,868,266 USD at 0.19 USD per ADA, for 18 months of Blockfrost transition and operations.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says Blockfrost will become a free, community-governed public API covering Cardano mainnet, preview, and preprod networks.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says all Blockfrost intellectual property, including source code, trademarks, domains, and associated assets, will be transferred to the governing not-for-profit entity.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal cites Cardano Foundation developer ecosystem survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal says Blockfrost will become a free, community-governed public API covering Cardano mainnet, preview, and preprod networks.
- missing: Independent evidence for: The proposal says all Blockfrost intellectual property, including source code, trademarks, domains, and associated assets, will be transferred to the governing not-for-profit entity.
- missing: Independent evidence for: The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,832,979 ADA, described as 1,868,266 USD at 0.19 USD per ADA, for 18 months of Blockfrost transition and operations." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal says Blockfrost will become a free, community-governed public API covering Cardano mainnet, preview, and preprod networks." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,832,979 ADA, described as 1,868,266 USD at 0.19 USD per ADA, for 18 months of Blockfrost transition and operations." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposal says Blockfrost will become a free, community-governed public API covering Cardano mainnet, preview, and preprod networks.
- Claims and evidence missing: Independent evidence for: The proposal says all Blockfrost intellectual property, including source code, trademarks, domains, and associated assets, will be transferred to the governing not-for-profit entity.
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
- input_hash: `41475d2cceeceb2d4965fa680318b6a2398701ce23d213268753ed0de57354bb`
- snapshot_bundle_hash: `b48f265269840c2e401840172e047e402ccacb91757cf62b6495c152d67a2c0e`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

