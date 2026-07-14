# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (raw `-0.08` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a public-benefit infrastructure maintenance request with defined scope, budget, governance-process references, and custody controls, but the main extra considerations for treasury stewardship, evidence verification, and NCL compliance appear already captured by the deterministic assessment; no additional nudge is justified from the supplied record alone.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and the applicable Net Change Limit still needs to be pinned and independently verified from public chain evidence before BEACN can make a directional vote.

The action requests 540,750 ada for UTxO RPC by TxPipe, covering a second year of maintenance: protobuf specification upkeep, SDK maintenance, community support, ecosystem feedback work, public communication, and AI-friendly documentation. The proposal breaks the amount into 420,000 ada for the work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. The anchor document was available, pinned, and replayable, and the proposal includes Intersect oversight, reporting obligations, milestone-based disbursement controls, and named external Oversight Committee entities.

Several basic claims were supported in the proposal, including the funding amount, the technical maintenance scope, and the description of UTxO RPC as an open interface using Protocol Buffers and SDKs across multiple languages. However, important claims remained too thinly evidenced for a treasury vote: independent evidence was missing for adoption by Amaru, Dingo, and the Haskell Cardano node, and for the claim that the project maintains more than 10 open-source Apache 2.0 repositories. The review also flagged missing clarity on sustainability path, cost-benefit, independent assurance, and rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger replayable evidence for the material adoption and open-source maintenance claims and clearer treasury-risk answers around sustainability, cost-benefit, assurance, and remedies.

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
- finding: Requested: Fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including part-time maintenance over 12 months and Intersect administration.
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v on behalf of the vendor TxPipe
- finding: Stated amount: 540750
- finding: Deliverables: WP1 - UTxO RPC Maintenance and Enhancement, Maintenance of the protobuf specification, including compatibility, versioning, and documentation, Maintenance of official SDKs through dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months; new grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is described as an open interface specification for UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers protobuf specification maintenance, SDK maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard.
- finding: Claim (technical, proposer_asserted, medium materiality): The project is said to maintain more than 10 repositories and remain fully open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting results and audit materials.
- missing: Independent evidence for: The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard.
- missing: Independent evidence for: The project is said to maintain more than 10 repositories and remain fully open-source under Apache 2.0.
- missing: Independent evidence for: TxPipe is said to have delivered 26 of 30 prior Project Catalyst proposals, with 4 under development on schedule, and to be delivering prior Intersect-funded Pallas, Dolos, and UTxO RPC maintenance on schedule.
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
- finding: Strongest NO: a material claim is unsupported — "The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard." — so cost or precedent may outweigh the benefit.
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
- Claims and evidence missing: Independent evidence for: The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard.
- Claims and evidence missing: Independent evidence for: The project is said to maintain more than 10 repositories and remain fully open-source under Apache 2.0.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `91de2dce266b62849d161527b58189f069b72473e7d5a2f1f08aa092a176d9ec`
- snapshot_bundle_hash: `f9051d738b3fd24e65a6e6b1060391dff60ecf7310920437e8a8c2314ea91c7e`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

