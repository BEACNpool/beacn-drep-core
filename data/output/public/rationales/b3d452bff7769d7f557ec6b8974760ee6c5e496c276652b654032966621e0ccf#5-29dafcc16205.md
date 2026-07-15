# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show alignment with protocol infrastructure, decentralization, milestone controls, on-chain smart-contract custody, budget-process references, and public audit paths; the nudge remains small because several adoption, prior-work, and centralization-risk claims are still proposer asserted rather than independently verified in the supplied document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests 3,810,423 ada for Mithril Protocol continuous development and Intersect budget administration: 3,699,440 ada for development work and 110,983 ada for the administration fee. The funds would go to the 2026 Treasury Reserve Smart Contract stake address, administered by Intersect for Teragone through TRSC and PSSC, with milestone-based disbursement controls. The proposal says Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling faster state verification without relying on the full chain; that core technical claim was well supported in the proposal and cleared the evidence gates.

Several governance and treasury signals were also positive: the proposal anchor was pinned and replayable, the proposal passed the 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase, the requested amount was reported as not breaching the 350M Net Change Limit at submission, and public audit paths such as treasury.sundae.fi were provided. But some important claims remained proposer-asserted rather than independently verified, including the claim that full node synchronization is slow and light clients rely on centralized trust today, that Teragone has not previously received direct Cardano treasury or community governance funding, and that Mithril will enable broader community-built tooling.

This is a conservative, evidence-based hold, not a rejection of Mithril. The review found a strong YES case around protocol infrastructure, milestone controls, smart-contract custody, and public auditability, but treasury votes require a higher bar because they spend shared ada and set precedent. A directional vote would be unblocked by pinned, independently verifiable public-chain evidence for the applicable Net Change Limit, plus stronger support for the missing budget, sustainability, independent assurance, and rollback or remedy details.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 3.81M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continuous development and Intersect budget administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect for the vendor Teragone via TRSC and PSSC.
- finding: Stated amount: 3810423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Milestone-based disbursement controls through Intersect treasury management smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid state verification without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that full node synchronization is slow and light clients rely on centralized trust today.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested 3,810,423 ada consists of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for an Intersect Budget Administration fee.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The requested amount does not at submission, alone or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (governance, supported_in_proposal, high materiality): Independent oversight will be provided through Intersect and technically capable third parties, with reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust today.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs.
- missing: Independent evidence for: Teragone has worked on Mithril for several years through collaboration with IOG, which has funded the project to date.
- missing: Independent evidence for: Mithril enables community-built tools such as bridges, light wallets, full wallets, light clients, and monitoring tools to emerge around Cardano.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 3810423
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.45
- missing: line-item budget
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
- finding: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid state verification without relying on the entire chain." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that full node synchronization is slow and light clients rely on centralized trust today." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 3810423
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid state verification without relying on the entire chain." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show alignment with protocol infrastructure, decentralization, milestone controls, on-chain smart-contract custody, budget-process references, and public audit paths; the nudge remains small because several adoption, prior-work, and centralization-risk claims are still proposer asserted rather than independently verified in the supplied document.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust today.
- Claims and evidence missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `29dafcc16205671507e946463ea5d0e27513df985d699830b00b53e85d1e41f9`
- snapshot_bundle_hash: `28f42ad59b0c1044d4e0c3a237aa214a8d676c020407ba1cb6d2f442373492a9`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `880436a840989202a38cccce66fd8f1cbf15004d`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

