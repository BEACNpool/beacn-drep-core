# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (raw `-0.66` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has strong claimed public-benefit alignment and some concrete governance and delivery mechanisms, but several highly material adoption and dependency claims are proposer-asserted rather than evidenced in the anchor, while the deterministic assessment already marks claims and evidence as thin and overall status incomplete. A small cautionary nudge is justified for treasury stewardship and evidence quality, without overriding the engine's gates.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the required Net Change Limit has not yet been pinned and independently verified from public chain evidence. That blocks a directional vote, even though the proposal has a replayable anchor document and includes some concrete governance and delivery commitments.

The action asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, funding 18 months of transition and operations. The proposal says Blockfrost is a hosted REST interface for Cardano developers, and that claim was supported. It also commits to transferring source code, trademarks, domains, and associated assets to the governing entity, with milestones, quarterly reporting, Intersect delivery assurance, third-party assurer review, and a written off-chain legal contract.

Several important claims were not independently evidenced in the review. These include the reported 781k monthly unique visitors, 1.84 billion API requests, nearly 700 requests per second, over 7 TB of API data, and the claim that more than 50% of Cardano transactions in most epochs are submitted through Blockfrost. The review also found thin claims-and-evidence status, medium execution risk, missing sustainability path, missing cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the public-good goal. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger independent evidence for the major adoption and dependency claims and clearer treasury-risk support around sustainability, cost-benefit, assurance, and remedies.

## Review Tree
- overall_status: `incomplete`

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent not-for-profit and fund 18 months of transition and operations.
- finding: Recipient: Input Output / Intersect-administered project-specific treasury process; final withdrawal recipient not stated in document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Establish a not-for-profit entity or host-organization agreement under a preliminary board in Q3 2026., Publish technical transition architecture and migration plan for community review in Q3 2026., Launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under public rules in Q4 2026., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027., Transfer Blockfrost source code, trademarks, domains, and associated assets to the governing entity in Q1 2027., Open a public sustainability consultation and publish a proposal for community feedback in Q2-Q3 2027., Operate the public API at minimum 99% monthly uptime with quarterly technical and budget reports during 2027.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Blockfrost developer adoption grew from 39.3% in 2022 to 71.5% in 2025 according to Cardano Foundation developer ecosystem survey links.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operators.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says 90% of Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing public-good operations.
- missing: Independent evidence for: The proposal states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operators.
- missing: Independent evidence for: The proposal says 90% of Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing public-good operations.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9832979
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data." — so cost or precedent may outweigh the benefit.
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
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9832979
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal has strong claimed public-benefit alignment and some concrete governance and delivery mechanisms, but several highly material adoption and dependency claims are proposer-asserted rather than evidenced in the anchor, while the deterministic assessment already marks claims and evidence as thin and overall status incomplete. A small cautionary nudge is justified for treasury stewardship and evidence quality, without overriding the engine's gates.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
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
- Claims and evidence missing: Independent evidence for: The proposal states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `cf44dd6d69581f43a713eb38dd1e0f6d5dadadc4c6a9449daa51fec7a0f33f2a`
- snapshot_bundle_hash: `1a93cd8477a405ec08d2448c50f016fa4488e2842cefc192ba92d9dd81e805d6`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

