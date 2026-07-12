# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1164` (raw `-0.08` + doctrine-LLM nudge `-0.01`) | Confidence: `0.7491` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal aligns with public-benefit ecosystem growth and provides meaningful governance and custody detail, but several high-materiality adoption and delivery-history claims are asserted rather than evidenced inside the document, and the maintainer cost plus contingency warrants a small treasury-stewardship caution nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs verified Net Change Limit evidence before a directional vote can be justified. The proposal may have public-benefit value, but BEACN’s rules require higher scrutiny when shared treasury ada is being spent.

The action asks to withdraw 540,750 ada to fund Year 2 maintenance of UTxO RPC by TxPipe, submitted by Intersect on behalf of the vendor. The proposal describes a 12-month part-time maintainer, maintenance of the protobuf specification and official SDKs, community support, documentation, and AI-friendly integration resources. It states that 525,000 ada would fund maintenance and enhancement, with a 15,750 ada Intersect administration fee.

Several core claims were supported well enough for review: the pinned anchor document was available and replayable, the requested amount and basic budget structure were stated, UTxO RPC’s technical role and SDK coverage were described, and the proposal included governance and custody details using Sundae Labs treasury management smart contracts and audit tooling. However, some material claims were still thin or unsupported inside the evidence set, including independent evidence that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node, and independent evidence for TxPipe’s Catalyst delivery-history claim. The review also noted missing detail on a line-item budget, sustainability path, independent assurance, and rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the project. A directional vote would be unblocked by pinned, independently verifiable public chain evidence showing that the applicable 350M ada Net Change Limit for Epoch 613 to Epoch 713 is not breached, plus stronger replayable evidence for the material adoption and delivery-history claims.

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
- finding: Requested: Treasury withdrawal to fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor TxPipe.
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for UTxO RPC over 12 months after the existing contract closes., Maintenance of the protobuf specification, including protocol compatibility, versioning, and documentation., Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixing., Community support, including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication., AI-friendly documentation and integration resources for AI-driven development workflows.
- finding: Deadline/expiry: 12-month grant period; exact start and end dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The on-chain treasury withdrawal amount is 540,750 ADA, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python to standardize interactions with UTxO-based blockchains.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: The proposal states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.55
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: low
- finding: Technical risk: low
- finding: Treasury exposure risk: low
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface." — so cost or precedent may outweigh the benefit.
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
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.010 (display cap ±0.05) and had zero influence on the binding score: The proposal aligns with public-benefit ecosystem growth and provides meaningful governance and custody detail, but several high-materiality adoption and delivery-history claims are asserted rather than evidenced inside the document, and the maintainer cost plus contingency warrants a small treasury-stewardship caution nudge rather than a positive adjustment.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `a2ad2a8e04f58041664cd484b314fa313cf493a4ca0a5556dee88d367c172569`
- snapshot_bundle_hash: `5849f7de999ea6b1611d34a03f17153ec5f1d30131e3256169b37dd70c60f365`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5073, "NO": 0.13, "YES": 0.3628}`

