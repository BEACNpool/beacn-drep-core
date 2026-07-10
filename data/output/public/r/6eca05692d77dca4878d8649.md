# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a public-benefit developer infrastructure project with meaningful governance and custody details, but the deterministic assessment already marked claims, treasury analysis, risk review, and synthesis as complete; the remaining evidence-quality issues, including several proposer-asserted delivery and prior-performance claims, do not justify an additional positive or negative nudge beyond the engine's scoring.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a Treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requested 540,750 ada to fund Year 2 maintenance of Dolos by TxPipe, submitted by Intersect on behalf of TxPipe to the 2026 Treasury Reserve Smart Contract stake address. The proposal says this includes 525,000 ada for Dolos maintenance and enhancement plus a 15,750 ada Intersect administration fee. It describes a 12-month part-time maintainer role covering dependency updates, protocol compatibility, performance work, bug fixes, documentation, community support, and AI-friendly integration resources, beginning after the current contract closes, though exact dates were not stated.

Several core facts were supported well enough for review: the anchor document was pinned and replayable, the requested amount and budget split were substantiated, Dolos was technically described as a Rust-based lightweight Cardano data node with multiple query interfaces, and the proposal’s passage through the 2026 Intersect Budget Process was independently verifiable. The proposal also described oversight, reporting, milestone-based disbursement controls, smart contract addresses, authorization thresholds, committee roles, and audit references.

The hold is conservative and evidence-based. BEACN did not reject the proposal’s purpose, but the review found thin claims evidence, unknown execution risk, missing sustainability and cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path. It also lacked independent evidence for some material claims, including Dolos’s role as an open-source alternative to running a full node and TxPipe’s delivery record across Catalyst and prior Intersect funding. A directional vote would be unblocked by pinned, independently verifiable Net Change Limit evidence from public chain data, plus stronger public evidence for those unsupported claims and clearer treasury-risk mitigations.

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
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe.
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months after the existing contract closes., Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation., Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public developer communication., AI-friendly documentation and integration resources for AI-driven development workflows.
- finding: Deadline/expiry: 12-month grant period beginning after closure of the existing contract; exact dates not stated in document.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ada total, consisting of 525,000 ada for Dolos maintenance and enhancement and a 15,750 ada Intersect budget administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The maintainer funding is described as 420,000 ADA plus a 105,000 ADA contingency reserve for 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): Dolos is a lightweight Cardano data node built in Rust that connects directly to the Cardano network, indexes ledger primitives, and exposes multiple query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, with the GitHub repository provided as a reference.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is presented as an open-source alternative for querying Cardano chain data without running a full node, intended to remain reliable and performant as developer adoption grows.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved framework.
- missing: Independent evidence for: Dolos is presented as an open-source alternative for querying Cardano chain data without running a full node, intended to remain reliable and performant as developer adoption grows.
- missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, plus prior Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ada total, consisting of 525,000 ada for Dolos maintenance and enhancement and a 15,750 ada Intersect budget administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is presented as an open-source alternative for querying Cardano chain data without running a full node, intended to remain reliable and performant as developer adoption grows." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ada total, consisting of 525,000 ada for Dolos maintenance and enhancement and a 15,750 ada Intersect budget administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Dolos is presented as an open-source alternative for querying Cardano chain data without running a full node, intended to remain reliable and performant as developer adoption grows.
- Claims and evidence missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, plus prior Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `669706a423aa13b99df39c7de461593e9749783b36c1b1805dce75bae79ef2d4`
- snapshot_bundle_hash: `49165b75c5ae39df652c1076106275d254d5f2a7ddffa8c960d722150204f53b`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

