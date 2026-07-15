# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (raw `-0.53` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): The claims show strong strategic fit with infrastructure and public-benefit growth plus checkable governance, NCL, and treasury-management references, but the document gives only a high-level continuous-development work package and does not state concrete milestones or deadlines; the deterministic ready assessment appears to have already captured the evidence and treasury controls, so no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 3,810,423 ada for Mithril Protocol continuous development and Intersect budget administration, paid to the Intersect Treasury Reserve Smart Contract. The proposal says 3,699,440 ada would fund Mithril continuous development and 110,983 ada would cover the administration fee. It also describes audit, oversight, reporting obligations, milestone-based disbursement controls, and administration through Sundae Labs treasury management smart contracts.

Several important parts were well-supported. The review found the proposal anchor pinned and replayable, and accepted the technical case that Mithril uses stake-based threshold multi-signatures to certify Cardano state so nodes and applications can verify state rapidly without relying on the full chain. It also independently verified that the proposal passed the required 67% support threshold during Intersect’s 2026 Budget Process Hydra Voting phase, and that Intersect’s treasury administration structure includes specified addresses, multisignature thresholds, oversight, and a public dashboard.

The hold is conservative and evidence-based. The review still found thin claim evidence, no pinned independent verification of the relevant Net Change Limit, missing independent support for claims about interoperability and adoption benefits, and gaps around line-item budget detail, sustainability path, independent assurance, and rollback or remedy path. Those are the specific items that would unblock a clearer YES or NO vote.

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
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit, oversight, reporting obligations, and milestone-based disbursement controls
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states Mithril is fully aligned with Infrastructure & Research Excellence because state proofs strengthen cross-chain interoperability.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states Mithril is fully aligned with Adoption & Utility because faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that without fast, verifiable, and trustless infrastructure, Cardano risks growing dependency on centralized indexers and hosted APIs.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The requested amount is stated not to breach the 350M Net Change Limit at the time of submission, either alone or in aggregate, for Epoch 613 to Epoch 713.
- missing: Independent evidence for: The proposal states Mithril is fully aligned with Infrastructure & Research Excellence because state proofs strengthen cross-chain interoperability.
- missing: Independent evidence for: The proposal states Mithril is fully aligned with Adoption & Utility because faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- missing: Independent evidence for: The proposal states that without fast, verifiable, and trustless infrastructure, Cardano risks growing dependency on centralized indexers and hosted APIs.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs, but has contributed to Mithril for several years through IOG-funded collaboration.
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
- finding: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states Mithril is fully aligned with Infrastructure & Research Excellence because state proofs strengthen cross-chain interoperability." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." and clears the evidence gates.
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
- Proposal requests over 50% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: The proposal states Mithril is fully aligned with Infrastructure & Research Excellence because state proofs strengthen cross-chain interoperability.
- Claims and evidence missing: Independent evidence for: The proposal states Mithril is fully aligned with Adoption & Utility because faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `889e3fbd6af9fde1a1c3daf0039ad916f9fa37d4487a8ac4f79d5fc3d74b28a2`
- snapshot_bundle_hash: `d4e75aca6c4c47e15fc946533953599d57c1a13cdbc1e2d92652aff25ae56692`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

