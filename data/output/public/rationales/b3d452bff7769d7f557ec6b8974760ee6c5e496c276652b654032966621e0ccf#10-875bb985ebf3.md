# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (raw `-0.08` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a public-benefit infrastructure maintenance proposal with stated deliverables, budget structure, governance-process references, and independently checkable oversight mechanisms. The main positive factors, including open-source infrastructure value and counterfactual maintenance continuity, are already captured by the assessment, while several important adoption and prior-delivery claims remain proposer-asserted within the supplied text, so no additional spending-positive nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The action asks to withdraw 540,750 ada for Year 2 of UTxO RPC maintenance by TxPipe: 420,000 ada for a 12-month part-time maintainer, 105,000 ada as contingency, and 15,750 ada for Intersect administration. The stated work includes maintaining the protobuf specification, official SDKs, community support, AI-friendly documentation, and milestone-based disbursement through Intersect oversight.

Several claims were supported: the budget breakdown, the maintainer scope, the open interface and SDK scope, the pinned and replayable proposal anchor, Intersect administration through smart contracts, and that the withdrawal did not breach the stated 350M Net Change Limit at submission. But important claims were still not independently evidenced, including adoption by Amaru, Dingo, and the Haskell Cardano node, and TxPipe’s Catalyst delivery record. The review also found thin evidence overall, unknown execution risk, no sustainability path, limited cost-benefit clarity, no independent assurance, and no rollback or remedy path.

The evidence that would unblock a directional vote is a pinned, independently verifiable Net Change Limit from public chain evidence, plus replayable public support for the material adoption and delivery-history claims, and clearer treasury-risk evidence around sustainability, cost-benefit, assurance, and remedies. Until then, BEACN holds rather than overclaim certainty on a treasury withdrawal.

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
- finding: Requested: Treasury withdrawal to fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including maintenance and enhancement plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540,750
- finding: Deliverables: 12 months of part-time UTxO RPC maintenance after the current contract closes, Maintenance of the protobuf specification, including compatibility, versioning, and documentation, Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixes, Community support including issue triage, review of external contributions, feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested funding would pay for a part-time UTxO RPC maintainer for 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification using Protocol Buffers with SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface, validating it as an ecosystem standard.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, language SDKs, documentation, and provider integrations, and is open source under Apache 2.0.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes protobuf specification maintenance, SDK dependency updates and bug fixes, community support, and AI-friendly documentation and integration resources.
- missing: Independent evidence for: UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface, validating it as an ecosystem standard.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest NO: a material claim is unsupported — "UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface, validating it as an ecosystem standard." — so cost or precedent may outweigh the benefit.
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
- Claims and evidence missing: Independent evidence for: UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface, validating it as an ecosystem standard.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `875bb985ebf3b602be28d0433f1547f6d9eb8efff8d467e5b6ab67481ff5d13e`
- snapshot_bundle_hash: `d65242b0e8386c615c3686d573b9e5b4bff67de60b6b7f7180dacab1c97d0bf8`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

