# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (raw `-0.08` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure maintenance and several independently checkable governance and oversight references, but key adoption and delivery-history assertions remain largely proposer-asserted within the document and the ask includes AI-related documentation work without cost granularity beyond the work package total. The deterministic assessment already marked the review ready, so no additional nudge is justified beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs independently pinned Net Change Limit evidence before BEACN can cast a directional vote. This is a conservative, evidence-based hold, not a rejection of the work.

The proposal asks for 540,750 ada to fund Year 2 maintenance and enhancement of UTxO RPC by TxPipe, with Intersect administration and milestone-based disbursement controls. The budget breakdown was supported in the proposal: 420,000 ada for the work, 105,000 ada contingency, and 15,750 ada for Intersect administration. The review also found support for the basic technical scope: UTxO RPC is described as an open Protocol Buffers interface with SDKs across several languages, and the maintainer scope covers specification maintenance, SDK updates, community support, and AI-friendly documentation.

Several governance facts were independently verifiable: the proposal passed the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase, and Intersect’s use of treasury management smart contracts with auditability was verified. But key benefit claims were still unsupported by independent public evidence, especially the claim that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node, and the claim that the project maintains more than 10 Apache 2.0 repositories across the specification, SDKs, documentation, and integrations.

The vote would be unblocked by public, replayable evidence that pins and independently verifies the applicable Net Change Limit from chain evidence, plus stronger independent evidence for the major adoption and repository claims. BEACN also noted missing clarity on sustainability, cost-benefit, independent assurance, and rollback or remedy paths. For a treasury action consuming shared ada, BEACN requires that evidence before moving from a hold to a YES or NO.

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
- finding: Requested: Fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including maintenance and enhancement plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v for onward administration by Intersect and project-specific contracts
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for UTxO RPC over 12 months, Maintenance of the protobuf specification including compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixing, Community support including issue triage, contribution review, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Intersect oversight, reporting obligations, and milestone-based disbursement controls
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification for UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, proposer_asserted, medium materiality): The project maintains more than 10 repositories covering the core specification, SDKs, documentation, and provider integrations under Apache 2.0.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers specification maintenance, SDK maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: The project maintains more than 10 repositories covering the core specification, SDKs, documentation, and provider integrations under Apache 2.0.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- missing: Independent evidence for: Independent oversight will be provided through Intersect and technically capable third parties with reporting obligations and milestone-based disbursement controls.
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
- finding: Strongest NO: a material claim is unsupported — "UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface." — so cost or precedent may outweigh the benefit.
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
- Claims and evidence missing: Independent evidence for: UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence missing: Independent evidence for: The project maintains more than 10 repositories covering the core specification, SDKs, documentation, and provider integrations under Apache 2.0.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `55eb90bd31c616ea19b14e5738b03117d99c9f178a518d7dfe46a198636c30e6`
- snapshot_bundle_hash: `020ffa60cd7496d775e09285803852f86e4e73974ef8a5419a38e56af132a0e2`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `a650e5f55d3662a45d71b3a19d5301fd64c2bbee`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

