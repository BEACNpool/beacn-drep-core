# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe established open-source infrastructure with checkable public artifacts, explicit maintenance deliverables, NCL compliance, and milestone/oversight controls; the adjustment remains modest because several adoption and prior-delivery claims are proposer-asserted and treasury stewardship still requires caution on recurring maintenance spend.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Dolos or its maintenance work.

The action asks to withdraw 540,750 ada for 12 months of Dolos maintenance by TxPipe, administered through the Intersect Treasury Reserve Smart Contract stake address. The proposal says this includes 420,000 ada for maintenance, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It describes Dolos as a Rust-based lightweight Cardano data node with several query interfaces, and the maintainer scope includes protocol compatibility, bug fixes, performance work, documentation, community support, contribution review, and AI-friendly integration resources.

Several important claims were supported by the proposal or were independently verifiable: the budget structure, the technical description of Dolos, the stated repository activity, Intersect budget-process support, the stated Net Change Limit compliance, and the described smart-contract administration and oversight controls. But the review also found thin evidence in key places. The claim that Dolos serves developer and infrastructure operator needs without a full node was only proposer-asserted, as were prior-delivery claims about TxPipe’s Catalyst and Intersect-funded work. The treasury review was also missing a sustainability path and clearer cost-benefit evidence, while the risk review lacked independent assurance and a rollback or remedy path.

Because this is a treasury withdrawal, BEACN applies a higher evidence bar: shared ada is being spent and the action can set precedent. A YES vote would be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger replayable evidence for adoption value, prior delivery, sustainability, cost-benefit clarity, independent assurance, and remedy options if execution falls short.

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
- finding: Requested: Fund Dolos by TxPipe: maintaining Cardano's lightweight data node for Year 2 over 12 months, including maintenance, community support, and AI-friendly documentation/integration resources.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address for administration on behalf of TxPipe as vendor
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months, Dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources, Milestone-based disbursement controls through Intersect-managed smart contracts
- finding: Deadline/expiry: 12-month grant period beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Dolos maintenance, with a 15,750 ADA Intersect administration fee for a total withdrawal of 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): Dolos is described as a Rust-based lightweight Cardano data node that connects to the Cardano network, indexes ledger primitives, and exposes multiple query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C socket.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes code maintenance, protocol compatibility, performance work, bug fixes, documentation, community support, contribution review, and AI-friendly documentation and integration resources.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal asserts Dolos provides an open-source alternative for querying Cardano chain data without running a full node and supports developer and infrastructure operator needs.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: The proposal asserts Dolos provides an open-source alternative for querying Cardano chain data without running a full node and supports developer and infrastructure operator needs.
- missing: Independent evidence for: The proposal discloses that TxPipe has received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Dolos maintenance, with a 15,750 ADA Intersect administration fee for a total withdrawal of 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts Dolos provides an open-source alternative for querying Cardano chain data without running a full node and supports developer and infrastructure operator needs." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Dolos maintenance, with a 15,750 ADA Intersect administration fee for a total withdrawal of 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe established open-source infrastructure with checkable public artifacts, explicit maintenance deliverables, NCL compliance, and milestone/oversight controls; the adjustment remains modest because several adoption and prior-delivery claims are proposer-asserted and treasury stewardship still requires caution on recurring maintenance spend.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal asserts Dolos provides an open-source alternative for querying Cardano chain data without running a full node and supports developer and infrastructure operator needs.
- Claims and evidence missing: Independent evidence for: The proposal discloses that TxPipe has received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `6ff47fed44afd958656445a0cc6eebbe2226acf907376a2746cab5293f76c46d`
- snapshot_bundle_hash: `e2611a79ba20586bc7adedb4f18e928e5002b6d88a9720f782b8107cf3995bfd`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

