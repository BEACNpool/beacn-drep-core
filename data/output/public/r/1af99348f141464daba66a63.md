# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NO**
Score: `-0.2733` (raw `-0.2533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7883` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has meaningful public-benefit alignment and several checkable governance and oversight references, but the anchor leaves key treasury-stewardship details thin for a 540,750 ADA withdrawal, especially concrete milestone dates, measurable acceptance criteria, and independent backing for past-delivery claims. Under the doctrine's caution around treasury spending and evidence quality, this warrants only a small negative nudge rather than overriding the deterministic assessment.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal, and the review found the evidence too thin on key treasury-stewardship points for 540,750 ada.

The proposal asked to fund Year 2 maintenance of Dolos by TxPipe, with 420,000 ada for work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It described 12 months of part-time maintainer coverage, protocol compatibility work, performance improvements, bug fixing, documentation, community support, AI-friendly integration resources, and milestone-based disbursement through Intersect-administered smart contracts.

Several governance and payment facts were supported or checkable: the amount breakdown was clear, the anchor document was available and replayable, Intersect oversight and reporting were described, budget-process support and treasury-limit claims were presented with references, and on-chain tracking addresses were provided. But important technical and delivery claims were not independently backed in the review, including the claim that Dolos provides lightweight chain-data access without full-node overhead and the claim about its five query interfaces. The review also found missing treasury details: no specific milestone dates, thin cost-benefit clarity, no sustainability path, no independent assurance, and no rollback or remedy path.

Because treasury withdrawals consume shared ada and set precedent, BEACN applies a higher evidence bar. The strongest YES case was that the proposal had a clear funding request and passed several evidence gates, but the unsupported material claims and missing treasury-risk details outweighed that case.

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
- finding: Requested: Treasury withdrawal to fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2.
- finding: Recipient: Intersect 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v for administration on behalf of TxPipe/vendor.
- finding: Stated amount: 540,750
- finding: Deliverables: 12 months of part-time maintainer coverage for Dolos after the existing contract closes, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls through Intersect-administered smart contracts
- finding: Deadline/expiry: 12 months; specific milestone dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- finding: Claim (technical, proposer_asserted, medium materiality): Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, and provides a GitHub project link where those metrics can be checked.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes codebase maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to the voting process and audited results.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- missing: Independent evidence for: Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing tooling.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
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
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has meaningful public-benefit alignment and several checkable governance and oversight references, but the anchor leaves key treasury-stewardship details thin for a 540,750 ADA withdrawal, especially concrete milestone dates, measurable acceptance criteria, and independent backing for past-delivery claims. Under the doctrine's caution around treasury spending and evidence quality, this warrants only a small negative nudge rather than overriding the deterministic assessment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing tooling.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `3992a3c2935d5fe8ad3f0e4543eaecd5d95f833e55be83b027a7edc325931e14`
- snapshot_bundle_hash: `e7e7817e67910e463abc7c002c49a5f23f07c14a2a1a8087eb2441cc9d5f8c92`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2047, "NO": 0.7491, "YES": 0.0462}`

