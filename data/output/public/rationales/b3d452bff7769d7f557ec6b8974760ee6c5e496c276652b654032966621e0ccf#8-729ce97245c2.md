# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#8
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1559` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.759` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a public-benefit infrastructure maintenance request with concrete scope, named downstream users, checkable adoption/process references, and described oversight and disbursement controls. The nudge is small because several important adoption and delivery-history claims remain proposer-asserted within the document, and treasury stewardship remains prior to ecosystem growth.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 540,750 ada to a Treasury Reserve Smart Contract stake address for Year 2 maintenance and enhancement of Pallas by TxPipe, administered by Intersect. The proposal says this includes 420,000 ada for the work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It describes a 12-month part-time maintainer scope covering dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, community support, AI-friendly integration resources, and milestone-based disbursement controls.

Several parts were well-supported inside the proposal: the requested amount and budget breakdown, the technical description of Pallas, the maintenance scope, the Intersect oversight and reporting structure, and the use of treasury-management smart contracts with specified control arrangements. The review also found the proposal anchor pinned and replayable, and treated the stated Intersect Budget Process support and Net Change Limit claim as independently verifiable claims. But important claims remained thin or unsupported by independent evidence in the review, including the claim that Pallas is shared infrastructure for named downstream projects and the claim about TxPipe’s Catalyst delivery history.

This is a conservative, evidence-based hold, not a rejection of the work. Treasury withdrawals consume shared ada and require a higher bar. A directional vote would be unblocked by public chain evidence pinning and independently verifying the applicable Net Change Limit, along with stronger independent evidence for the major adoption and delivery-history claims, plus clearer sustainability, cost-benefit, independent assurance, and rollback or remedy information.

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
- finding: Requested: Treasury withdrawal to fund Pallas by TxPipe maintenance and enhancement for Year 2, including Intersect administration fee.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for work by TxPipe administered by Intersect
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Pallas over 12 months, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12 months; new grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): Pallas is a collection of Rust crates re-implementing core Ouroboros and Cardano primitives including CBOR encoding, cryptographic operations, mini-protocol networking, multi-era ledger traversal, transaction building, and address handling.
- finding: Claim (adoption, proposer_asserted, high materiality): Pallas serves as shared infrastructure for projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Pallas has over 649 pull requests, 199 stars, 91 forks, 60 contributors, and 214,446 crates.io downloads, with links to GitHub and crates.io.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers essential maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission.
- missing: Independent evidence for: Pallas serves as shared infrastructure for projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest NO: a material claim is unsupported — "Pallas serves as shared infrastructure for projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a public-benefit infrastructure maintenance request with concrete scope, named downstream users, checkable adoption/process references, and described oversight and disbursement controls. The nudge is small because several important adoption and delivery-history claims remain proposer-asserted within the document, and treasury stewardship remains prior to ecosystem growth.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Pallas serves as shared infrastructure for projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- Claims and evidence missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `729ce97245c2f4104b6a0ed949dfc33cd316f7de26efcaf644ecaabcbc38511a`
- snapshot_bundle_hash: `18bf1656ae33576165e044dd2cf2ff1d8d36d64e114ff95b33fa3c3399914566`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5098, "NO": 0.0892, "YES": 0.401}`

