# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (raw `-0.08` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal presents a clear infrastructure-maintenance scope, public-benefit rationale, budget breakdown, governance-process references, and on-chain administration details; however, several important delivery and adoption claims remain proposer assertions in the anchor text, and the deterministic assessment has already marked claims, treasury analysis, and risk review complete, so no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 540,750 ada for Year 2 maintenance of UTxO RPC by TxPipe, submitted by Intersect on behalf of the vendor. The proposal says this includes 420,000 ada for the work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. The funded work would cover a part-time maintainer for 12 months, protobuf specification compatibility and documentation, official SDK maintenance, community support, and AI-friendly integration resources.

Several core facts were supported well enough for review: the pinned anchor document was available and replayable, the requested amount was clear, the work scope was stated, the open-source technical footprint was independently verifiable, the Intersect Budget Process support threshold was met, and the submission-time Net Change Limit impact was reported as not breaching the 350M ada limit for Epoch 613 to Epoch 713. But important claims were still thin or unsupported by independent evidence, including adoption by Amaru, Dingo, and the Haskell Cardano node, and TxPipe’s stated Catalyst and 2025 Intersect delivery history.

This is a conservative, evidence-based hold, not a rejection of the project. A directional vote would be unblocked by pinned, public verification of the applicable Net Change Limit from chain evidence, plus stronger independent evidence for the adoption and delivery-history claims, clearer cost-benefit and sustainability analysis, and better assurance around execution risk, remedies, or rollback if delivery falls short.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 540.8k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor TxPipe
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for UTxO RPC over 12 months after the existing contract closes, Maintenance of the protobuf specification including protocol compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12-month grant period; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification for standardizing interactions with UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations under the Apache 2.0 open-source license.
- finding: Claim (technical, supported_in_proposal, high materiality): The funded work would maintain protobuf compatibility and documentation, official SDKs, community support, and AI-friendly integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- missing: Independent evidence for: TxPipe received Intersect 2025 open-source maintenance funding for Pallas, Dolos, and UTxO RPC, all stated to be delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `08ee647d6424d602eef93c94487ed6568269ee6752d8bf07f59b45f323d8296f`
- snapshot_bundle_hash: `347793a2aa60b840d833dd6ccecf95df7f9c8fd4450a4b190529de6ce2d53141`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `7`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

