# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The anchor provides meaningful governance process evidence, custody controls, and externally checkable references, but for a large treasury withdrawal the concrete milestone schedule, acceptance criteria, and cost justification are thin in the supplied claims. Under BEACN's hierarchy, treasury stewardship and evidence reproducibility justify a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Mithril or its value.

The action requests 3,810,423 ada from the treasury for continued Mithril Protocol development through Intersect, with funds first going to the 2026 Treasury Reserve Smart Contract stake address and later moving to a project-specific smart contract when contract and readiness conditions are met. The proposal says 3,699,440 ada would fund Mithril continuous development and 110,983 ada would cover Intersect budget administration and oversight. It also claims Mithril helps users securely access and verify Cardano state through stake-based threshold multi-signatures, enabling faster trustless verification without needing the whole chain.

Several parts were well-supported: the anchor document was available, pinned, and replayable; the technical case for Mithril cleared the evidence gates; the proposal showed Intersect budget-process support; and custody controls, oversight, reporting, milestone-based disbursement controls, named smart contract structures, and public tracking were described. But some claims remained unsupported or thin, including independent evidence for the claimed onboarding and tooling benefits, independent evidence about prior Teragone funding, cost-benefit clarity, sustainability path, independent assurance, and a rollback or remedy path. Execution risk was also unknown.

For BEACN to move from NEEDS_MORE_INFO to a directional YES or NO, the missing blocker is specific: the applicable 350M Net Change Limit must be pinned and independently verified from public chain evidence. Stronger independent evidence for the adoption claims, clearer cost-benefit justification, and fuller risk controls would also improve confidence, but the verified Net Change Limit is the gating item for this treasury withdrawal.

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
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with later transfer to a project-specific smart contract for the vendor when contract and readiness conditions are met.
- finding: Stated amount: 3810423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration and oversight
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state through stake-based threshold multi-signatures.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states Mithril enables rapid trustless verification of Cardano state without relying on the entire chain.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal claims faster sync times lower onboarding friction and support tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal claims the requested withdrawal does not breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 at the time of submission.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget allocates 3,699,440 ada to Mithril Protocol Continuous Development and 110,983 ada to the Intersect Budget Administration fee.
- missing: Independent evidence for: The proposal claims faster sync times lower onboarding friction and support tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- missing: Independent evidence for: The proposal states Teragone has not previously received direct funding from Cardano treasury or community governance programs, while prior Mithril work was funded by IOG.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 3810423
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.52
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
- finding: Strongest YES: the proposal substantiates "Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state through stake-based threshold multi-signatures." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal claims faster sync times lower onboarding friction and support tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 3810423
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state through stake-based threshold multi-signatures." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The anchor provides meaningful governance process evidence, custody controls, and externally checkable references, but for a large treasury withdrawal the concrete milestone schedule, acceptance criteria, and cost justification are thin in the supplied claims. Under BEACN's hierarchy, treasury stewardship and evidence reproducibility justify a small cautionary nudge rather than a positive adjustment.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal claims faster sync times lower onboarding friction and support tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- Claims and evidence missing: Independent evidence for: The proposal states Teragone has not previously received direct funding from Cardano treasury or community governance programs, while prior Mithril work was funded by IOG.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `45016175fd4db381f1fc62ea19259c8740ea72dd9286c4e9693159d8057f9f09`
- snapshot_bundle_hash: `92448cc6bb3067b6bc82101140d0bcc3d725045a2e66689f4f317134d0c32db1`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

