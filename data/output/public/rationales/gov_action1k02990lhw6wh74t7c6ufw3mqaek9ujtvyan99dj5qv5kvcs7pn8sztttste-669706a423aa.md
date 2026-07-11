# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a specific open-source infrastructure maintenance scope, disclosed budget components, stated governance-process approval, NCL compliance, and concrete oversight mechanisms with externally checkable references. The nudge is small because several material adoption and delivery-history claims remain proposer-stated rather than verified within the document, and treasury stewardship still cautions against over-weighting ecosystem benefit alone.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the Dolos maintenance work.

The proposal requested 540,750 ada for Year 2 maintenance of Dolos by TxPipe, with funds going to the 2026 Treasury Reserve Smart Contract stake address. The request includes 525,000 ada for Dolos maintenance and enhancement, including a part-time maintainer over 12 months, dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, community support, AI-friendly integration resources, milestone-based disbursement controls, and reporting obligations. It also includes a 15,750 ada Intersect budget administration fee.

Several parts of the proposal were well-supported in the review: the pinned anchor document was available and replayable, the budget structure was disclosed, the Intersect budget-process support threshold was stated, oversight and milestone controls were described, and public tracking through a dashboard and smart-contract framework was stated. However, some material claims remained too thin or unsupported for a confident treasury withdrawal vote, including independent evidence that Dolos provides the claimed lightweight node benefits and independent evidence for TxPipe’s Catalyst delivery history. The review also flagged missing clarity on sustainability, cost-benefit, independent assurance, and rollback or remedy path.

Because this is a treasury withdrawal, BEACN applies a higher evidence bar: spending shared ada sets precedent and must be auditable by skeptical delegators. The specific evidence that would unblock a directional vote is a pinned, independently verifiable Net Change Limit check from public chain evidence, along with stronger independent support for the material technical and delivery-history claims.

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
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months, Essential maintenance including dependency updates, protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, contribution review, feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources, Milestone-based disbursement controls and reporting obligations
- finding: Deadline/expiry: 12 months; grant period begins after closure of existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The total withdrawal is 540,750 ADA, consisting of 525,000 ADA for Dolos maintenance and enhancement and 15,750 ADA for the Intersect budget administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- finding: Claim (technical, supported_in_proposal, medium materiality): Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing Cardano tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node in Rust that provides efficient chain-data access without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a specific open-source infrastructure maintenance scope, disclosed budget components, stated governance-process approval, NCL compliance, and concrete oversight mechanisms with externally checkable references. The nudge is small because several material adoption and delivery-history claims remain proposer-stated rather than verified within the document, and treasury stewardship still cautions against over-weighting ecosystem benefit alone.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- snapshot_bundle_hash: `88c6cc349cdc4931e5ed2d1eaa82e41145a48232cf09e693cc710bd4bcd856aa`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

