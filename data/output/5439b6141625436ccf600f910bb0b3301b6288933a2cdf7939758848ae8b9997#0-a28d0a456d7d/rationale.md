# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (raw `-0.66` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure value and concrete governance deliverables, but several high-materiality adoption and cost-justification claims are proposer-asserted while the deterministic assessment already marks evidence as thin and incomplete; under BEACN's hierarchy this warrants only a small cautionary nudge against spending rather than a larger adjustment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Blockfrost’s public-good value.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with 18 months of transition and operations funding. It includes concrete deliverables: forming or hosting the not-for-profit entity, publishing a technical transition plan, launching a public usage dashboard, holding an on-chain board election, migrating public API traffic to the new stack, transferring source code and related assets, meeting a 99% monthly uptime SLA, and publishing quarterly technical and budget reports.

Several claims were supported well enough for review, including Blockfrost’s role as hosted Cardano infrastructure, the commitment to transfer source code and assets, the requested budget split, return of unspent post-transition infrastructure funds, and use of Intersect delivery assurance. But several high-materiality claims remained proposer-asserted or thinly evidenced, including recent traffic numbers, the claim that more than 50% of transactions are submitted through Blockfrost in most epochs, the 90% free-tier traffic claim, and the participation of more than 100 Icebreakers. The review also found missing clarity on sustainability, cost-benefit justification, independent assurance, and rollback or remedy paths.

The pinned proposal anchor was available and replayable, the counterargument review was completed, and the strongest case for YES was recognized: Blockfrost appears to provide important developer infrastructure. But treasury withdrawals consume shared ADA and require elevated scrutiny. To unblock a directional vote, BEACN would need the Net Change Limit pinned and independently verified from public chain evidence, plus stronger public evidence for the major adoption and cost-justification claims.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent not-for-profit, including 18 months of transition and operations funding.
- finding: Recipient: Input Output / Blockfrost transition administered through Intersect and CDH contractual arrangements
- finding: Stated amount: 9,832,979
- finding: Deliverables: Not-for-profit entity established or host-organization agreement signed under a preliminary board in Q3 2026, Technical transition architecture and migration plan published for community review, Public usage dashboard launched, Board election held via on-chain voting by Q4 2026 and elected board seated, Public API traffic for mainnet, preview, and preprod served by the new stack by Q1 2027, Blockfrost source code, trademarks, domain names, and associated assets legally transferred to the governing entity, Public API operated at minimum 99% monthly uptime SLA with quarterly technical and budget reports, Sustainability consultation and proposal published in Q2-Q3 2027
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node infrastructure.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Cardano Foundation developer ecosystem surveys show Blockfrost hosted-platform usage rose from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in the previous month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that more than 50% of all transactions are submitted through Blockfrost in most Cardano epochs.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model challenging for financing the public-good operation.
- missing: Independent evidence for: The proposal states that in the previous month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposal states that more than 50% of all transactions are submitted through Blockfrost in most Cardano epochs.
- missing: Independent evidence for: The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- missing: Independent evidence for: The proposal states that 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model challenging for financing the public-good operation.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node infrastructure." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that in the previous month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node infrastructure." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The claims show plausible public-benefit infrastructure value and concrete governance deliverables, but several high-materiality adoption and cost-justification claims are proposer-asserted while the deterministic assessment already marks evidence as thin and incomplete; under BEACN's hierarchy this warrants only a small cautionary nudge against spending rather than a larger adjustment.
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
- Claims and evidence missing: Independent evidence for: The proposal states that in the previous month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence missing: Independent evidence for: The proposal states that more than 50% of all transactions are submitted through Blockfrost in most Cardano epochs.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `a28d0a456d7d6141a13cee255463e5057afc52dd94fc7731c59a15643f916ed9`
- snapshot_bundle_hash: `0032a0d30955d16d771e2ad1d6267a523f01008eb6fac6adea964658c227e572`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

