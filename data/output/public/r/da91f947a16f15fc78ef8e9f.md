# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (raw `-0.33` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): The extracted claims show a protocol-infrastructure proposal with checkable governance-process, NCL, smart-contract, dashboard, repository, and audit references, plus explicit oversight and milestone-control mechanics. The positive nudge is small because the cost justification and delivery timeline are thin in the anchor text despite strong infrastructure relevance.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 3,810,423 ada for continued Mithril Protocol development, administered through Intersect and paid through treasury smart-contract tooling. The proposal says Mithril helps solve slow full-node synchronization and reduces reliance on centralized trust for light clients through stake-based threshold multi-signatures. Those core technical claims were supported in the proposal, and the anchor document was available, pinned, and replayable.

The review also found several positive signals: the proposal listed the recipient stake address, described Intersect budget administration and milestone-based disbursement controls, gave a total budget split of 3,699,440 ada for Mithril development and 110,983 ada for administration, and referenced governance-process, smart-contract, dashboard, repository, and audit materials. But some important claims remained unsupported or thin, including the broader decentralization claim, budget line-item detail, sustainability path, independent assurance, and rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of Mithril. BEACN would need the Net Change Limit independently verified from public chain evidence before making a directional treasury vote, with stronger supporting evidence on the missing budget, assurance, sustainability, and remedy details improving confidence.

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
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continuous development through Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with Intersect administering funds and later transferring project funding to a Project-Specific Smart Contract.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration and oversight, Milestone-based disbursement controls through TRSC/PSSC tooling
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril is presented as solving slow full-node synchronization and centralized trust reliance for light clients by using stake-based threshold multi-signatures to certify Cardano state.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states that Mithril enables rapid, trustless verification of Cardano state for nodes and applications without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that continued Mithril funding supports decentralization by reducing dependency on centralized indexers and hosted APIs during increased governance activity, ecosystem expansion, and scaling pressure.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal claims full alignment with Infrastructure & Research Excellence and Adoption & Utility, and partial alignment with Community & Ecosystem Growth.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and links to voting and audited-results references.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states the requested withdrawal does not breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 at the time of submission and links to the referenced governance action.
- missing: Independent evidence for: The proposal states that continued Mithril funding supports decentralization by reducing dependency on centralized indexers and hosted APIs during increased governance activity, ecosystem expansion, and scaling pressure.
- missing: Independent evidence for: The proposal claims full alignment with Infrastructure & Research Excellence and Adoption & Utility, and partial alignment with Community & Ecosystem Growth.
- missing: Independent evidence for: The proposal states Teragone has not previously received direct Cardano treasury or community governance funding, while IOG has funded its Mithril work to date.
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
- finding: Strongest YES: the proposal substantiates "Mithril is presented as solving slow full-node synchronization and centralized trust reliance for light clients by using stake-based threshold multi-signatures to certify Cardano state." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that continued Mithril funding supports decentralization by reducing dependency on centralized indexers and hosted APIs during increased governance activity, ecosystem expansion, and scaling pressure." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril is presented as solving slow full-node synchronization and centralized trust reliance for light clients by using stake-based threshold multi-signatures to certify Cardano state." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a protocol-infrastructure proposal with checkable governance-process, NCL, smart-contract, dashboard, repository, and audit references, plus explicit oversight and milestone-control mechanics. The positive nudge is small because the cost justification and delivery timeline are thin in the anchor text despite strong infrastructure relevance.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 30% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: The proposal states that continued Mithril funding supports decentralization by reducing dependency on centralized indexers and hosted APIs during increased governance activity, ecosystem expansion, and scaling pressure.
- Claims and evidence missing: Independent evidence for: The proposal claims full alignment with Infrastructure & Research Excellence and Adoption & Utility, and partial alignment with Community & Ecosystem Growth.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `b8c9e538c4ab1857ebcc7e036dab9a9be87b9b0ecf8a6139bd4e0d16c16f1f14`
- snapshot_bundle_hash: `eaf9a619353cfae3fc1ce609cb1cabf3639880d1644ac431901aa4d49459112b`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `6`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

