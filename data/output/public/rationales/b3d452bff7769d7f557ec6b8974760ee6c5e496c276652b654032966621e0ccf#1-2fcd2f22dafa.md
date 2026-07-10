# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal was missing: `treasury_amount_lovelace`. Without that core evidence, BEACN could not make a responsible directional vote.

The action requested 540,750 ada for Year 2 funding of TxPipe’s Dolos work, including 12 months of part-time maintenance, protocol compatibility work, bug fixes, documentation, community support, contribution review, and AI-friendly integration resources. The proposal claimed the total included 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee, and the review found that claim substantiated. It also found support for the description of Dolos as a lightweight open-source Cardano data node with several query interfaces, and for the general maintainer scope.

However, several important claims were not independently evidenced in the review. These included the breakdown of 420,000 ada core maintenance plus 105,000 ada contingency reserve tied to a $105,000 annual maintainer rate, and claims about TxPipe’s past Catalyst and Intersect delivery record. The treasury review was also incomplete, missing a sustainability path and cost-benefit clarity, while the risk review was missing independent assurance and a rollback or remedy path.

This abstention is a conservative, evidence-based hold, not a rejection of Dolos or TxPipe. A directional vote would require the missing treasury withdrawal baseline evidence, especially `treasury_amount_lovelace`, plus stronger independent support for the budget breakdown, delivery-history claims, sustainability plan, cost-benefit case, assurance, and remedy path.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2, including maintenance, community support, and AI-friendly documentation/integration resources.
- finding: Recipient: TxPipe via Intersect treasury management smart contracts
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months after the existing contract closes, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12-month grant period beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, composed of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect administration fee.
- finding: Claim (technical, independently_verifiable, high materiality): The on-chain treasury withdrawal reward is 540,750,000,000 lovelace to the listed 2026 Treasury Reserve Smart Contract stake address.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says the core maintenance request is 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): Dolos is described as a lightweight open-source Cardano data node in Rust that indexes ledger primitives and exposes multiple query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C socket.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes dependency updates, protocol compatibility, performance improvements, bug fixes, documentation, issue triage, contribution review, ecosystem-feedback enhancements, and AI-friendly resources.
- missing: Independent evidence for: The proposal says the core maintenance request is 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- missing: Independent evidence for: The proposal states TxPipe has received 30 Project Catalyst grants across Funds 9 through 14, with 26 delivered and 4 under development on schedule, and that prior Intersect 2025 open-source maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.66
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, composed of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal says the core maintenance request is 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, composed of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect administration fee." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: The proposal says the core maintenance request is 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- Claims and evidence missing: Independent evidence for: The proposal states TxPipe has received 30 Project Catalyst grants across Funds 9 through 14, with 26 delivered and 4 under development on schedule, and that prior Intersect 2025 open-source maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `2fcd2f22dafadb203cd4479633936ff3375f3bfb6e71db7b12a5854fe02404e4`
- snapshot_bundle_hash: `62abc90da012964f580bf1c21c464eaab856cc79f13d7be15738c0d71054c6b2`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

