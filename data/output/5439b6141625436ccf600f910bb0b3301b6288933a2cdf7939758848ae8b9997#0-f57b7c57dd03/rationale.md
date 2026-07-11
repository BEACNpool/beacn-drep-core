# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.21` (raw `-0.21` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7725` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show strong public-benefit alignment for established infrastructure, but several highest-materiality adoption and sustainability claims are proposer-asserted rather than independently verified in the document, while the deterministic assessment already marks claims and evidence as thin and overall status incomplete. A small cautionary negative nudge is justified for treasury stewardship and evidence quality, without overriding the engine's hard-gate treatment of incomplete diligence.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The action requests 9,832,979 ADA to transition Blockfrost into a free, community-governed public API/public good under an independent not-for-profit, with 18 months of transition and operations funding. The proposal describes milestones from Q3 2026 through 2027, including forming or hosting the not-for-profit, publishing a migration plan, launching a public usage dashboard, holding an on-chain board election, moving public API traffic to the new stack, transferring Blockfrost assets, and publishing a sustainability proposal.

Several important claims were supported in the proposal: the planned transfer of source code, trademarks, domains, and associated assets; the proposed five-seat board structure; the requested amount and budget split; and the commitment to return unspent post-transition infrastructure funds. One major adoption claim was independently supported: Blockfrost’s surveyed developer usage rose to 71.5% in 2025 from 39.3% in 2022, according to linked Cardano Foundation survey pages. But other high-materiality claims remained proposer-asserted, including last month’s traffic figures and the claim that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs.

The review found the anchor document available and replayable, and the strongest YES case cleared the evidence gates. But treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. The review also found thin claims-and-evidence status, medium execution risk, missing sustainability and cost-benefit clarity, missing independent assurance, and no dependency map. A directional vote would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus independent evidence for the major usage and transaction-share claims and clearer treasury sustainability and risk documentation.

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
- finding: Strongest YES: the proposal substantiates "Blockfrost is used by 71.5% of surveyed Cardano developers in 2025, up from 39.3% in 2022, according to linked Cardano Foundation developer ecosystem survey pages." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is used by 71.5% of surveyed Cardano developers in 2025, up from 39.3% in 2022, according to linked Cardano Foundation developer ecosystem survey pages." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show strong public-benefit alignment for established infrastructure, but several highest-materiality adoption and sustainability claims are proposer-asserted rather than independently verified in the document, while the deterministic assessment already marks claims and evidence as thin and overall status incomplete. A small cautionary negative nudge is justified for treasury stewardship and evidence quality, without overriding the engine's hard-gate treatment of incomplete diligence.
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
- Claims and evidence missing: Independent evidence for: Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `f57b7c57dd03d201c7d9ab9eaf77a9ec6713e3aaba97ea845b95d9a5429c8f95`
- snapshot_bundle_hash: `0cd07c4d27332914087f54babf199c4d2aeda8508885c9c9833ea13019b27711`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.446, "YES": 0.0492}`

