# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.0` | Readiness: `0`


## Plain-language explanation (deterministic-template)
BEACN's autonomous DRep recorded ABSTAIN on "Blockfrost's transformation to not-for-profit" (TreasuryWithdrawals). This is a conservative, evidence-based hold rather than opposition. The action requests 9.83M ADA from the treasury. A key material claim lacks independent support: "Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.". Open questions before a directional vote: freshness gate failed. Reason code: STALE_DATA. (Plain-language summary generated deterministically; a model-written explanation appears here when the reasoning layer is enabled.)

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 9.83M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Transition Blockfrost into a free, community-governed public API/public good under an independent not-for-profit, including 18 months of transition and operations funding.
- finding: Recipient: not stated in document
- finding: Stated amount: 9832979
- finding: Deliverables: Not-for-profit entity established or host-organization agreement signed under a preliminary board in Q3 2026, Technical transition architecture and migration plan published for community review in Q3 2026, Public usage dashboard live in Q3 2026, Board election held via on-chain voting under public rules in Q4 2026, All public API traffic for mainnet, preview, and preprod served by the new stack in Q1 2027, Blockfrost source code, trademarks, domain names, and associated assets legally transferred to the governing entity in Q1 2027, Public sustainability consultation and proposal published in Q2-Q3 2027, Public API operated at minimum 99% monthly uptime with quarterly reports during 2027 operational milestones
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (adoption, independently_verifiable, high materiality): Blockfrost is used by 71.5% of surveyed Cardano developers in 2025, up from 39.3% in 2022, according to linked Cardano Foundation developer ecosystem survey pages.
- finding: Claim (adoption, proposer_asserted, high materiality): Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal will transfer all Blockfrost intellectual property, including source code, trademarks, domains, and associated assets, to the governing not-for-profit entity.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed not-for-profit board will have five seats, with four for open-source infrastructure development entities and one community seat, preceded by a named preliminary board.
- missing: Independent evidence for: Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: Long-term sustainability may come from paid not-for-profit commercial tiers or a vendor-backed model, with future profits or fees intended to support the public API and potentially flow back to the Cardano Treasury.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is used by 71.5% of surveyed Cardano developers in 2025, up from 39.3% in 2022, according to linked Cardano Foundation developer ecosystem survey pages." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: freshness gate failed
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Data freshness check failed: data is 91634s old, max allowed is 21600s
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is used by 71.5% of surveyed Cardano developers in 2025, up from 39.3% in 2022, according to linked Cardano Foundation developer ecosystem survey pages." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce reliable recommendation with stale data.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- All scoring suspended until fresh data is available.
- Claims and evidence missing: Independent evidence for: Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: freshness gate failed
- Synthesis status is blocked.

## Reproducibility
- input_hash: `f57b7c57dd03d201c7d9ab9eaf77a9ec6713e3aaba97ea845b95d9a5429c8f95`
- snapshot_bundle_hash: `334cd49bfc6f1ba361b37e522dec6f21ce167c4c0357f959ee4a645e95d4d22d`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `eec0908e48c56be13e86e06ac5d9440d0cac813a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `91634`
- uncertainty_band: `LOW`
- evidence_depth_score: `2`
- decision_probs: `{"ABSTAIN": 0.32, "NO": 0.34, "YES": 0.34}`

- **DATA STALE**: age exceeded threshold

