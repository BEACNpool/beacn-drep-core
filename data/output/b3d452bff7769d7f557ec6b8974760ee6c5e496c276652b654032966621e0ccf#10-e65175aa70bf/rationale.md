# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe public-benefit developer infrastructure, concrete maintenance deliverables, checkable governance references, NCL compliance, and detailed fund-control mechanisms; the nudge remains small because key adoption and delivery-history claims are largely proposer asserted and the doctrine prioritizes treasury stewardship and evidence quality over ecosystem-growth upside.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a Treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 540,750 ada for year-two maintenance of UTxO RPC by TxPipe: 420,000 ada for maintenance work, 105,000 ada as contingency, and 15,750 ada for Intersect administration. The proposed work covers 12 months of part-time maintainer coverage after the current contract closes, protobuf specification maintenance, SDK updates, community support, and AI-friendly documentation and integration resources.

Several parts of the proposal were well supported in the review. The pinned anchor document was available and replayable, the requested amount and budget structure were substantiated, the work package was concrete, and the proposal described oversight, reporting, milestone-based disbursement controls, treasury smart contract administration, and public dashboard plans. The review also found independently verifiable governance context, including Intersect Budget Process support and the proposal’s statement that the withdrawal would not breach the 350M ada Net Change Limit for Epoch 613 to Epoch 713 at submission.

The hold is conservative and evidence-based. BEACN did not reject the merits of maintaining open developer infrastructure, but the evidence record was still thin for a Treasury action: adoption by Amaru, Dingo, and the Haskell Cardano node was not independently evidenced, TxPipe’s delivery-history claims were not independently evidenced, execution risk remained unknown, and the review lacked a sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger replayable evidence for the material adoption and delivery-history claims.

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
- finding: Requested: Fund UTxO RPC by TxPipe for year-two maintenance of Cardano's integration standard, including maintainer work, SDK/spec maintenance, community support, and AI-friendly documentation resources.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address for subsequent project-specific administration on behalf of TxPipe
- finding: Stated amount: 540,750
- finding: Deliverables: 12 months of part-time maintainer coverage for UTxO RPC after the existing contract closes, Maintenance of the protobuf specification including protocol compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months; start after closure of existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for UTxO RPC maintenance, with a 15,750 ADA Intersect administration fee for a total withdrawal of 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification using Protocol Buffers with SDKs in Rust, Go, Node.js, .NET, Haskell, and Python to standardize interactions with UTxO-based blockchains.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open source under Apache 2.0.
- finding: Claim (technical, supported_in_proposal, high materiality): The work package covers protobuf specification maintenance, SDK maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission.
- missing: Independent evidence for: The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: TxPipe is stated to have received 30 Project Catalyst grants from Funds 9 through 14, with 26 delivered and 4 under development and on schedule, plus prior Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for UTxO RPC maintenance, with a 15,750 ADA Intersect administration fee for a total withdrawal of 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for UTxO RPC maintenance, with a 15,750 ADA Intersect administration fee for a total withdrawal of 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe public-benefit developer infrastructure, concrete maintenance deliverables, checkable governance references, NCL compliance, and detailed fund-control mechanisms; the nudge remains small because key adoption and delivery-history claims are largely proposer asserted and the doctrine prioritizes treasury stewardship and evidence quality over ecosystem-growth upside.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence missing: Independent evidence for: TxPipe is stated to have received 30 Project Catalyst grants from Funds 9 through 14, with 26 delivered and 4 under development and on schedule, plus prior Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `e65175aa70bfe7b4b6c630cf68a1781601edf46dce3145263b6b3756b6595767`
- snapshot_bundle_hash: `3f83685b90ac0aa581a0a397b22ae8bd886c5ef3bd289cfd2329fe9b259eae6b`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4d394ccfc21657ebcbf2e1dbb3e210682b5ea383`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

