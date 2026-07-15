# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `0.027` (raw `-0.08` + doctrine-LLM nudge `+0.01`) | Confidence: `0.7268` | Readiness: `0.65`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe maintenance of established open-source infrastructure, include concrete scope, governance-process references, smart-contract controls, and on-chain/auditable addresses, while some adoption and delivery-history claims remain proposer-asserted and the treasury spend is substantial enough to keep the adjustment minimal.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 540,750 ada for “Oura by TxPipe” over 12 months, submitted by Intersect on behalf of the vendor. The proposal describes funding for a part-time maintainer, dependency and protocol-compatibility work, performance improvements, bug fixes, documentation, community support, AI-friendly integration resources, and reporting with milestone-based controls. The strongest supported case for voting yes is that the proposal gives a concrete funding structure: 420,000 ada plus a 105,000 ada contingency reserve, with a 15,750 ada Intersect administration fee, for a maintainer budgeted at $105,000 USD per year.

Several important claims were well-supported or independently checkable: the anchor document was available and replayable, Oura’s technical role was clearly described, the repository metrics were tied to a public GitHub source, the Intersect Budget Process support threshold was referenced with audit materials, and the treasury smart contract framework included specific addresses, roles, thresholds, audit references, and a tracking dashboard. But other claims remained unsupported by independent evidence, including prior Catalyst funding for Oura and TxPipe’s stated Catalyst delivery history. The review also found thin evidence overall, a missing line-item budget, missing independent assurance, an unknown execution-risk profile, and no clear rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the project. A directional vote would be unblocked by independently pinned public-chain evidence that the withdrawal complies with the applicable Net Change Limit, plus stronger independent support for the missing Catalyst-history claims, clearer line-item budgeting, milestone-gated disbursement evidence, independent assurance, and a rollback or remedy path.

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
- finding: Requested: Withdraw treasury funds for Oura by TxPipe: Maintaining Cardano's Event Pipeline, submitted by Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with project funding later transferred to a Project-Specific Smart Contract for the vendor.
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Oura over 12 months, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources, Milestone-based disbursement controls and reporting obligations
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is described as a Rust-native Cardano event pipeline tool supporting multiple data sources and sinks for indexing, monitoring, analytics, and real-time event processing.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal says Oura has 654 commits, 288 stars, 79 forks, and 58 contributors, and identifies the GitHub repository where those figures can be checked.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer states that Oura has previously been funded through Project Catalyst Funds 9 and 13 for feature development.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes dependency updates, protocol compatibility, performance work, bug fixing, documentation, issue triage, contribution review, public communication, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting, documentation, final audited results, and audit materials.
- missing: Independent evidence for: The proposer states that Oura has previously been funded through Project Catalyst Funds 9 and 13 for feature development.
- missing: Independent evidence for: TxPipe is claimed to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.43
- missing: line-item budget
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that Oura has previously been funded through Project Catalyst Funds 9 and 13 for feature development." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.010 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe maintenance of established open-source infrastructure, include concrete scope, governance-process references, smart-contract controls, and on-chain/auditable addresses, while some adoption and delivery-history claims remain proposer-asserted and the treasury spend is substantial enough to keep the adjustment minimal.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposer states that Oura has previously been funded through Project Catalyst Funds 9 and 13 for feature development.
- Claims and evidence missing: Independent evidence for: TxPipe is claimed to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `e4c962630a3b1ee9016bbd5cfde89098e7690770360c3cd31dac3a39e09b4569`
- snapshot_bundle_hash: `cb5ccaf650ecb39eb3bc5b2a7be12dfe3037f5d0274e0252649267d6afce1475`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5017, "NO": 0.2222, "YES": 0.2762}`

