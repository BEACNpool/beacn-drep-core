# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#8
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.08` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.74` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a defined open-source infrastructure maintenance scope, stated downstream ecosystem dependence, externally checkable usage and governance references, and detailed treasury administration controls. The adjustment remains small because several adoption and prior-delivery claims are proposer-stated and the doctrine prioritizes treasury stewardship and independently verified evidence before ecosystem growth.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal depends on a required Net Change Limit check that was not pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Pallas or TxPipe.

The action requests 540,750 ada for 12 months of Year 2 Pallas maintenance: 420,000 ada for the work, 105,000 ada as contingency, and 15,750 ada for Intersect administration. The proposal says Pallas maintains core Rust libraries for Cardano primitives and would fund part-time maintenance, dependency updates, protocol compatibility, performance work, bug fixes, documentation, community support, and AI-friendly integration resources. Those scope and budget claims were well supported by the proposal materials, and the anchor document was available, pinned, and replayable.

Several points helped the case but did not fully clear the evidence bar. The review found independently checkable signals for Pallas activity, including pull requests, stars, forks, contributors, and crates.io downloads, and it noted that the proposal passed the 2026 Intersect Budget Process Hydra Voting support threshold. It also found the treasury management structure and public audit mechanisms described in the proposal. But some material adoption and delivery-history claims remained proposer-stated or thinly evidenced, including the claim that named projects rely on Pallas and the claim about TxPipe’s prior Catalyst delivery record.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny. The intake, pinned anchor, counterargument pass, and basic treasury amount review were sufficient to review the proposal, but directional voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. A YES or NO vote would be unblocked by that public NCL verification, plus stronger independent evidence for the adoption claims, clearer cost-benefit and sustainability information, and more detail on independent assurance and rollback or remedy paths.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: ratified
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
- finding: Requested: Fund Pallas by TxPipe for Year 2 maintenance of Cardano core Rust libraries over 12 months.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe as vendor
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Pallas over 12 months, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months; grant period begins after closure of existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): Pallas is a collection of Rust crates that re-implement core Ouroboros and Cardano primitives including CBOR encoding, cryptographic operations, mini-protocol networking, ledger traversal, transaction building, and address handling.
- finding: Claim (adoption, proposer_asserted, high materiality): Projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and others rely on Pallas for low-level protocol details.
- finding: Claim (adoption, independently_verifiable, medium materiality): Pallas has over 649 pull requests, 199 stars, 91 forks, 60 contributors, and 214,446 downloads on crates.io.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer will perform code maintenance, community support, and AI-workflow compatibility improvements to keep Pallas usable, reliable, and up to date for downstream projects.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and others rely on Pallas for low-level protocol details.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 currently under development and on schedule.
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
- finding: Financial confidence: 0.63
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and others rely on Pallas for low-level protocol details." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a defined open-source infrastructure maintenance scope, stated downstream ecosystem dependence, externally checkable usage and governance references, and detailed treasury administration controls. The adjustment remains small because several adoption and prior-delivery claims are proposer-stated and the doctrine prioritizes treasury stewardship and independently verified evidence before ecosystem growth.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and others rely on Pallas for low-level protocol details.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 currently under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `1a2215850ee7cd5097721b775347367aeae8e8a8b84b005c368814a024f2df5f`
- snapshot_bundle_hash: `5164003bc8ccb18505bad318c561f93b9255b99104a64ea5cc8001399e5b15d3`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `4be57618f85e778396d883cd24aa46e529b1399c`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.505, "NO": 0.3275, "YES": 0.1675}`

