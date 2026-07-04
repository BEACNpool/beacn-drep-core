# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal describes a potentially important public-good transition with concrete milestones, governance concepts, and budget categories, but several high-materiality usage and dependency claims are asserted without embedded verification, and the sustainability path remains conditional on future board decisions rather than a committed revenue model. Given the large treasury ask and the assessment that claims and evidence are thin, a small cautionary negative nudge is justified beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and several material claims behind the request were not backed by independent, replayable evidence.

The proposal asked for 9,832,979 ADA to transition Blockfrost into a free, community-governed not-for-profit public API for Cardano and fund 18 months of transition and operations. It described concrete deliverables: creating or hosting the not-for-profit entity, publishing migration plans, holding a board election, transferring Blockfrost IP, serving mainnet and testnet API traffic from the new stack, maintaining a 99% monthly uptime SLA during 2027, and publishing technical and budget reports. The proposer also claimed strong adoption, including developer-survey growth from 39.3% in 2022 to 71.5% in 2025, high recent API traffic, and that Blockfrost submits more than 50% of transactions in most epochs.

The review found some claims well-supported in the proposal: Blockfrost’s role as a hosted Cardano API, the planned IP transfer, the five-seat not-for-profit governance model, the 18-month budget size, and the main budget categories. The survey-based adoption claim was treated as independently verifiable. But other high-materiality claims remained unsupported by independent evidence, especially the claimed 781k unique visitors, 1.84 billion API requests, nearly 700 requests per second, over 7 TB of API data last month, and the claim that more than 50% of transactions in most epochs are submitted through Blockfrost.

Because this was a treasury action, BEACN applied elevated scrutiny. The proposal had a pinned, replayable anchor and presented a credible public-good case, but the evidence review was thin for key usage and dependency claims. The treasury review also lacked milestone-gated disbursement and a committed sustainability path, while the risk review lacked independent assurance and a clear rollback or remedy path. On balance, the benefits were not evidenced strongly enough to justify the cost and precedent, so BEACN voted NO.

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
- finding: Requested: Transition Blockfrost into a free, community-governed not-for-profit public API for Cardano and fund 18 months of transition and operations.
- finding: Recipient: Input Output / Blockfrost transition under community-governed not-for-profit structure, with treasury administration involving Intersect and CDH as described
- finding: Stated amount: 9,832,979
- finding: Deliverables: Not-for-profit entity established or host-organization agreement signed, technical transition architecture and migration plan published, and public usage dashboard live in Q3 2026, Board election held via on-chain voting under published rules and newly elected board assumes mandate in Q4 2026, Public API traffic for mainnet, preview, and preprod served by the new stack, Blockfrost IP legally transferred, and service performance maintained in Q1 2027, Public sustainability consultation, proposal publication, feedback process, and chosen direction documented in Q2-Q3 2027, Public API sustained at minimum 99% monthly uptime SLA during 2027 with quarterly technical and budget reports
- finding: Deadline/expiry: 18-month funding period, with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost developer-survey usage grew from 39.3% in 2022 to 71.5% in 2025, citing Cardano Foundation survey links for each year.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operators.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal commits to transferring Blockfrost source code, trademarks, domain names, and associated assets to the governing not-for-profit entity as part of the transition.
- missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operators.
- missing: Independent evidence for: The proposal says future sustainability may come from paid not-for-profit commercial tiers or a vendor-backed model, with profits or fees supporting the public API and potentially reducing future treasury reliance.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9832979
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal describes a potentially important public-good transition with concrete milestones, governance concepts, and budget categories, but several high-materiality usage and dependency claims are asserted without embedded verification, and the sustainability path remains conditional on future board decisions rather than a committed revenue model. Given the large treasury ask and the assessment that claims and evidence are thin, a small cautionary negative nudge is justified beyond the mechanical score.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `3f577c95989a12bc5038562de5e457585de8ebd9b93c67f24cfe3f4c201c7e02`
- snapshot_bundle_hash: `33d14fa19b2f13e0df80eb28a1695eea80e70f3e394dbbbf58a3a368b35f7ca3`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.181, "NO": 0.778, "YES": 0.0409}`

