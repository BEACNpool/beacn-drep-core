# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (raw `-0.08` + doctrine-LLM nudge `+0.0`) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a public-benefit open-source infrastructure ask with some independently checkable governance, repository, NCL, and tooling references, while several delivery-history and operational-benefit claims remain proposer-stated; the deterministic assessment already marks treasury, risk, and evidence review complete, so no additional discretionary nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and the applicable Net Change Limit still needs to be pinned and independently verified from public chain evidence before a directional vote is justified.

The action asks for 540,750 ada to fund Year 2 maintenance of Dolos by TxPipe, administered through Intersect. The proposal says this includes 525,000 ada for Dolos maintenance and enhancement plus a 15,750 ada administration fee. It describes a 12-month part-time maintainer role covering dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, community support, and AI-friendly integration resources.

Several points were supported well enough for review: the requested amount, budget breakdown, pinned anchor document, and the claim that Dolos has public GitHub activity metrics available for verification. The proposal also claims Intersect process support, treasury administration controls, milestone-based disbursement, and that the request does not breach the applicable 350M ada Net Change Limit. But some material claims remained thin or unsupported by independent evidence, including the technical claim that Dolos is a lightweight Rust data node that avoids full-node overhead, and the delivery-history claim about TxPipe’s Catalyst and prior maintenance work.

This is a conservative, evidence-based hold, not a rejection of the project. A directional vote would be unblocked by independently pinned public chain evidence for the applicable Net Change Limit, stronger independent evidence for the key technical and delivery-history claims, and clearer treasury review on sustainability, cost-benefit, independent assurance, and any rollback or remedy path.

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
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2.
- finding: Recipient: TxPipe via Intersect treasury withdrawal administration
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months after the existing contract closes, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12-month grant period; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and a 15,750 ADA Intersect budget administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation text states the underlying grant is 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- finding: Claim (technical, supported_in_proposal, high materiality): The document says Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with existing tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document reports Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, with a GitHub repository link provided for verification.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos is fully open source and welcomes broader developer community contributions.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- missing: Independent evidence for: The document states TxPipe has received 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development on schedule, and that prior Intersect maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
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
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: The document states TxPipe has received 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development on schedule, and that prior Intersect maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `a5e08a5049d50a1da3eac7300103b003dc9615ea9dbf93487dc910f3d94406f1`
- snapshot_bundle_hash: `c75d9776af86ced2c39375b69b8b46e6e7ba9ad261719543e9ca854e18d3a01b`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

