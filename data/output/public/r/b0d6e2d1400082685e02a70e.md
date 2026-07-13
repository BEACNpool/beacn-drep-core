# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (raw `-0.33` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): The extracted claims show a public-benefit infrastructure proposal with verifiable governance-process references, NCL compliance claims, smart contract addresses, audit references, and milestone-control mechanisms. The nudge is small because several core benefit and prior-funding claims remain proposer-asserted and the amount is material, so treasury stewardship and evidence quality still warrant caution.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Mithril.

The proposal requests 3,810,423 ada from the treasury for Mithril Protocol continuous development and Intersect budget administration, paid to the 2026 Treasury Reserve Smart Contract stake address. It claims Mithril improves Cardano infrastructure by using stake-based threshold multi-signatures to certify Cardano state, enabling faster state verification without relying on the full chain. That technical claim was supported in the proposal, and the proposal also provided a replayable anchor, budget totals, TRSC/PSSC treasury-management controls, audit and oversight arrangements, and milestone-based disbursement controls.

Several other claims were not strong enough on their own for a treasury withdrawal decision. The need claim that full node synchronization is slow and light clients rely on centralized trust was still missing independent evidence. The alignment claims with Intersect priorities were proposer-asserted. The review also found thin evidence overall, missing line-item budget detail, no stated sustainability path, unknown execution risk, missing independent assurance, and no clear rollback or remedy path.

The review gates did show meaningful positives: the proposal passed the Intersect Budget Process Hydra Voting support threshold, the pinned anchor was available and replayable, and the strongest YES case cleared evidence gates around Mithril’s core technical value. But treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. A directional vote would be unblocked by pinned, independently verifiable public-chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the unsupported need and risk controls.

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
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit and oversight through Intersect and technically capable third-party oversight, Milestone-based disbursement controls through TRSC/PSSC treasury management smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling faster state verification without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): Full node synchronisation is currently slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- finding: Claim (governance, proposer_asserted, medium materiality): Continued Mithril development is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- finding: Claim (adoption, proposer_asserted, high materiality): Funding Mithril through Intersect MBO is presented as preserving Cardano decentralization by reducing dependency on centralized indexers and hosted APIs during governance and scaling growth.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The requested 3,810,423 ada does not, at submission, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: Full node synchronisation is currently slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- missing: Independent evidence for: Continued Mithril development is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- missing: Independent evidence for: Funding Mithril through Intersect MBO is presented as preserving Cardano decentralization by reducing dependency on centralized indexers and hosted APIs during governance and scaling growth.
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
- finding: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling faster state verification without relying on the entire chain." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Full node synchronisation is currently slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling faster state verification without relying on the entire chain." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a public-benefit infrastructure proposal with verifiable governance-process references, NCL compliance claims, smart contract addresses, audit references, and milestone-control mechanisms. The nudge is small because several core benefit and prior-funding claims remain proposer-asserted and the amount is material, so treasury stewardship and evidence quality still warrant caution.
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
- Claims and evidence missing: Independent evidence for: Full node synchronisation is currently slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- Claims and evidence missing: Independent evidence for: Continued Mithril development is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `65edfd870a6f493c20f80841316f85f54c0674e6c4c9a482380d2ee573bb0f17`
- snapshot_bundle_hash: `8e220228d68ccf2f4b162bc06e07c6f14ca0f32776de81fcaa9cef435027f900`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `a650e5f55d3662a45d71b3a19d5301fd64c2bbee`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

