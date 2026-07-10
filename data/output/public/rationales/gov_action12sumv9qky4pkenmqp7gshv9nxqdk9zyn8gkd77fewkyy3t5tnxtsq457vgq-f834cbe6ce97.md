# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7758` | Readiness: `0.75`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure value and some checkable adoption evidence, but the assessment labels evidence as thin and several high-materiality claims remain proposer-asserted, including current traffic, transaction-share dependence, Icebreaker scale, and future treasury-returning sustainability. Given the very large treasury request and unresolved legal/governance formation details, a small cautionary nudge is justified beyond the mechanical score.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Blockfrost's transformation to not-for-profit. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API for Cardano, including operations during the transition. It asks the treasury for 9,832,979 ADA. The strongest grounded claim is: Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node.

A material claim remains proposer-asserted or thinly supported: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month. Reason code: VERIFIED_NCL_REQUIRED.

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
- finding: Requested: Fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API for Cardano, including operations during the transition.
- finding: Recipient: Input Output / Blockfrost transition under legal contract with Cardano Development Holdings administered by Intersect
- finding: Stated amount: 9,832,979 ADA
- finding: Deliverables: Not-for-profit entity legally established or host-organization agreement signed under a preliminary board in Q3 2026, Technical transition architecture and migration plan published for community review in Q3 2026, Public usage dashboard live in Q3 2026, Board election held via on-chain voting under public rules in Q4 2026, Newly elected board formally assumes its mandate from the preliminary board in Q4 2026, All public API traffic for mainnet, preview, and preprod served by the new stack in Q1 2027, Blockfrost source code, trademarks, domain names, and associated assets legally transferred to the governing entity in Q1 2027, Public sustainability consultation and proposal published in Q2-Q3 2027, Public API operated at minimum 99% monthly uptime with quarterly technical and budget reports during 2027
- finding: Deadline/expiry: 18 months of operations including transition; milestones run from Q3 2026 through 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost developer-survey usage grew from 39.3% in 2022 to 71.5% in 2025, citing Cardano Foundation survey links for each year.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal commits to transferring all Blockfrost intellectual property, including source code, trademarks, domain names, and associated assets, to the governing not-for-profit entity.
- missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: The proposal states that long-term sustainability may come from paid not-for-profit commercial tiers or vendor membership fees, with future profits returned to the Cardano Treasury.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9832979
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.67
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
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
- finding: Flag count: 2
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9832979
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show plausible public-benefit infrastructure value and some checkable adoption evidence, but the assessment labels evidence as thin and several high-materiality claims remain proposer-asserted, including current traffic, transaction-share dependence, Icebreaker scale, and future treasury-returning sustainability. Given the very large treasury request and unresolved legal/governance formation details, a small cautionary nudge is justified beyond the mechanical score.
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
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `f834cbe6ce97b268c9f453eec13ab619c9b5ecb97075763fda9b0e46b17be46e`
- snapshot_bundle_hash: `26c30af4972565165b2813c784f2e032946f9d85e1a8af70532f75d09c69bca2`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

