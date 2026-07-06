# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s5z9qdza
Recommendation: **NO**
Score: `-0.2733` (raw `-0.2533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7883` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has concrete scope, budget lines, references, on-chain addresses, and governance-process evidence, but several high-materiality value claims remain proposer-asserted, including ecosystem adoption significance and TxPipe delivery history, while the treasury ask funds ongoing maintenance at a substantial amount. Under the doctrine, treasury stewardship and evidence quality justify only a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks for a substantial treasury withdrawal, but a key claim about ecosystem adoption was not independently supported strongly enough for that level of spending.

The action requested 540,750 ada for year-two maintenance and enhancement of UTxO RPC by TxPipe, including 525,000 ada for project work and 15,750 ada for Intersect administration. The proposal described a 12-month scope covering a part-time maintainer, protobuf specification maintenance, SDK updates, bug fixes, community support, and AI-friendly documentation. It also named the treasury reserve smart contract recipient address and described Intersect administration, oversight, reporting, milestone controls, and later transfer to a project-specific smart contract.

Several core facts were well-supported: the anchor document was available and replayable, the requested amount and budget split were clear, the maintenance scope was concrete, the open-source technical basis of UTxO RPC was independently verifiable, and the proposal had governance-process evidence from the Intersect budget process. The review also recognized the strongest YES case: the proposal clearly substantiated what it was asking for and passed important evidence gates.

The NO came from the higher bar BEACN applies to treasury withdrawals. Some material value claims remained only proposer-asserted, especially that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC in a way that validates it as an ecosystem standard, and the stated TxPipe Catalyst delivery history. The review also found thin evidence overall, no clear sustainability path, limited cost-benefit clarity, unknown execution risk, no independent assurance, and no rollback or remedy path. Given those gaps, BEACN judged that the cost and treasury precedent outweighed the demonstrated benefit.

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
- finding: Requested: Fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including maintenance and enhancement over 12 months plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for project funding to be managed by Intersect and later transferred to a Project-Specific Smart Contract for the vendor.
- finding: Stated amount: 540750
- finding: Deliverables: A part-time maintainer for UTxO RPC over 12 months at an annual rate of $105,000 USD., Maintenance of the protobuf specification, including protocol compatibility, versioning, and documentation., Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixing., Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication., AI-friendly documentation and integration resources to improve compatibility with AI-driven development workflows.
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested maintenance scope is for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD, with the new grant period beginning after the existing contract closes.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification using Protocol Buffers with SDKs in Rust, Go, Node.js, .NET, Haskell, and Python to standardize interactions with UTxO-based blockchains.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 currently under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.66
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has concrete scope, budget lines, references, on-chain addresses, and governance-process evidence, but several high-materiality value claims remain proposer-asserted, including ecosystem adoption significance and TxPipe delivery history, while the treasury ask funds ongoing maintenance at a substantial amount. Under the doctrine, treasury stewardship and evidence quality justify only a small cautionary nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- Claims and evidence missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 currently under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `e5d4d4d378723ba67836adae679bdcdba465cb13beb595afa984acbd455768ab`
- snapshot_bundle_hash: `2116fa1d62c9cdbd14ebd5ae2120854affd962cbdd465a42a4b4dc1324f0c33f`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2047, "NO": 0.7491, "YES": 0.0462}`

