# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims describe maintenance of established open-source developer infrastructure, provide checkable references for governance process and oversight, and include concrete operational controls; the nudge remains small because the document still relies on proposer assertions for some delivery history and adoption claims.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Dolos or TxPipe.

The action asks to withdraw 540,750 ada for year-two Dolos maintenance through the 2026 Treasury Reserve Smart Contract stake address, administered via Intersect. The proposal breaks that into 420,000 ada for the work, 105,000 ada contingency, and a 15,750 ada Intersect administration fee. The stated work covers 12 months of part-time maintenance, protocol compatibility, dependency updates, performance improvements, bug fixing, documentation, community support, external contribution review, ecosystem-feedback enhancements, public communication, and AI-friendly integration resources.

Several parts were well supported in the proposal: the requested amount and fee structure, the maintenance scope, the listed query interfaces, the Intersect administration model, and references for Hydra voting, voting documentation, audited results, smart contract materials, and audit reports. The proposal also states that it cleared the 67% Intersect Budget Process Hydra Voting support threshold and that the withdrawal did not breach the 350M Net Change Limit at submission. But some claims remained unsupported or thin for BEACN’s standard, including independent evidence that Dolos is a lightweight Rust Cardano data node providing resource-efficient chain access, and independent evidence for TxPipe’s Catalyst delivery history.

The review gates allowed the proposal to be reviewed because the anchor document was pinned and replayable, and the strongest YES case was acknowledged. However, treasury actions require elevated scrutiny because they spend shared ada and set precedent. The review still found stressed treasury-flow context, thin evidence status, unknown execution risk, missing sustainability path, missing cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the Net Change Limit, plus stronger independent evidence for the key technical and delivery-history claims.

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
- finding: Requested: Withdraw treasury funds to support Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for TxPipe Dolos via Intersect administration
- finding: Stated amount: 540,750
- finding: Deliverables: 12 months of part-time Dolos maintenance and enhancement, Dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12-month grant period beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient chain data access without the overhead of traditional full nodes.
- finding: Claim (technical, supported_in_proposal, medium materiality): Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli and Ogmios.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The requested maintenance scope includes codebase maintenance, protocol compatibility, performance improvements, bug fixing, documentation, community support, and AI-friendly integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient chain data access without the overhead of traditional full nodes.
- missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient chain data access without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims describe maintenance of established open-source developer infrastructure, provide checkable references for governance process and oversight, and include concrete operational controls; the nudge remains small because the document still relies on proposer assertions for some delivery history and adoption claims.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient chain data access without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `f07a39efd2124b589b972bf14299c77d9894a0193cb62665ad8d2238bbebf8eb`
- snapshot_bundle_hash: `235345018cd35e3623385b670dba13b50e3f24b1732ea9f42bbd250acf057b87`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `7`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

