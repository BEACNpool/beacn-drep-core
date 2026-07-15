# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): The extracted claims show a public-infrastructure proposal with checkable governance-process, NCL, smart-contract, audit, and dashboard references, which modestly improves evidence quality and treasury stewardship beyond unsupported technical benefit assertions. The nudge remains small because several high-value benefit and adoption claims are still proposer assertions rather than demonstrated outcome evidence.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Mithril or its value.

The action requests 3,810,423 ada from the treasury to fund continued Mithril Protocol development through Intersect, with milestone-based disbursement through TRSC/PSSC smart contracts. The proposal says Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid verification without relying on the full chain; that claim was supported in the proposal and was the strongest case for a YES vote. The review also found independently verifiable support for the Intersect budget-process approval, the stated TRSC/PSSC governance setup, and public auditability through dashboards and on-chain records.

Several important benefit claims were still only proposer assertions, including that full node synchronization is slow today, that light clients rely on centralized trust, and that faster sync would lower onboarding friction or unlock new tooling for exchanges, wallets, and monitoring. The treasury review also found missing or thin evidence around the line-item budget, sustainability path, independent assurance, rollback or remedy path, and execution risk.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny: shared ada is being spent and the vote creates precedent. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger evidence for the unsupported technical and adoption claims and the missing treasury and risk details.

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
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continued development through Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect budget administration and oversight, Milestone-based disbursement through TRSC/PSSC smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid verification without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): Full node synchronisation is slow today and light clients rely on centralized trust.
- finding: Claim (adoption, proposer_asserted, medium materiality): Faster sync times lower onboarding friction and unlock new tooling for exchanges, wallets, and monitoring.
- finding: Claim (technical, proposer_asserted, high materiality): Funding Mithril's continued development through Intersect MBO helps Cardano scale while preserving decentralization guarantees and reducing dependency on centralized indexers and hosted APIs.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, independently_verifiable, high materiality): The requested withdrawal does not, at the time of submission either alone or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: Full node synchronisation is slow today and light clients rely on centralized trust.
- missing: Independent evidence for: Faster sync times lower onboarding friction and unlock new tooling for exchanges, wallets, and monitoring.
- missing: Independent evidence for: Funding Mithril's continued development through Intersect MBO helps Cardano scale while preserving decentralization guarantees and reducing dependency on centralized indexers and hosted APIs.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs, while prior Mithril work was funded by IOG.
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
- finding: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid verification without relying on the entire chain." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Full node synchronisation is slow today and light clients rely on centralized trust." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid verification without relying on the entire chain." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a public-infrastructure proposal with checkable governance-process, NCL, smart-contract, audit, and dashboard references, which modestly improves evidence quality and treasury stewardship beyond unsupported technical benefit assertions. The nudge remains small because several high-value benefit and adoption claims are still proposer assertions rather than demonstrated outcome evidence.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Full node synchronisation is slow today and light clients rely on centralized trust.
- Claims and evidence missing: Independent evidence for: Faster sync times lower onboarding friction and unlock new tooling for exchanges, wallets, and monitoring.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `a124aaad6e054cbcf4d59c7462b930076354c327e06768c788e37d6ae35a483c`
- snapshot_bundle_hash: `21d37c506b85c488b8501bb60a9a6114edc5c6a8a965cef2e6f7215479920b24`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `afd630a34be9d7440e2fac020ac552cde501098f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

