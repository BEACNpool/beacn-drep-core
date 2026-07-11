# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show a public-benefit infrastructure proposal with specific budget allocation, checkable governance-process references, NCL compliance claims, smart-contract custody details, and audit/oversight references. The adjustment remains small because several core benefit and vendor-history claims are still proposer asserted rather than evidenced within the document itself.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Mithril or the requested work.

The action requested 3,810,423 ada from the treasury for Mithril Protocol continuous development and Intersect budget administration. The proposal says 3,699,440 ada would fund Mithril continuous development and 110,983 ada would cover the Intersect administration fee. It also says Intersect would administer the funds for Teragone through the Treasury Reserve Smart Contract and Project-Specific Smart Contract framework, with milestone-based controls, audit and oversight references, and an Oversight Committee role limited to verifying administrative actions through on-chain logic.

Several important points were supported well enough to review: the proposal anchor was pinned and replayable, the budget split was stated, the Intersect Budget Process Hydra Voting threshold claim was substantiated, and the smart-contract custody framework and references were checkable. But some material claims were still not independently evidenced in the supplied review, including the claim that Mithril reduces the cost and complexity of securely accessing and verifying Cardano state, and the claim that it will lower onboarding friction through faster sync times and enable tooling for exchanges, wallets, monitoring, bridges, full wallets, light wallets, and light clients.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny. The review also noted stressed treasury-flow conditions, thin claims-and-evidence status, unknown execution risk, and missing support for sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path. The evidence that would unblock a directional vote is public, independently verifiable Net Change Limit evidence for the applicable period, plus stronger replayable evidence for the main technical benefit claims and the missing treasury and risk items.

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
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect on behalf of the vendor Teragone
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit and oversight through Intersect and technically capable third parties, Milestone-based disbursement controls through TRSC and PSSC smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, proposer_asserted, high materiality): Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify Cardano state in a trustless way.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states Mithril will lower onboarding friction through faster sync times and enable tooling for exchanges, wallets, monitoring, bridges, full wallets, light wallets, and light clients.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested 3,810,423 ada is split into 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested withdrawal does not, at submission, individually or in aggregate breach the applicable 350M ada Net Change Limit for Epoch 613 to Epoch 713.
- finding: Claim (governance, proposer_asserted, medium materiality): Audit and oversight costs are included in the proposal overhead, with independent oversight provided through Intersect and technically capable third parties, reporting obligations, and milestone-based disbursement controls.
- missing: Independent evidence for: Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify Cardano state in a trustless way.
- missing: Independent evidence for: The proposal states Mithril will lower onboarding friction through faster sync times and enable tooling for exchanges, wallets, monitoring, bridges, full wallets, light wallets, and light clients.
- missing: Independent evidence for: Audit and oversight costs are included in the proposal overhead, with independent oversight provided through Intersect and technically capable third parties, reporting obligations, and milestone-based disbursement controls.
- missing: Independent evidence for: Teragone has not previously received direct funding from the Cardano treasury or community governance programs, while prior Mithril work was funded by IOG.
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
- finding: Strongest YES: the proposal substantiates "The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify Cardano state in a trustless way." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show a public-benefit infrastructure proposal with specific budget allocation, checkable governance-process references, NCL compliance claims, smart-contract custody details, and audit/oversight references. The adjustment remains small because several core benefit and vendor-history claims are still proposer asserted rather than evidenced within the document itself.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Mithril addresses the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify Cardano state in a trustless way.
- Claims and evidence missing: Independent evidence for: The proposal states Mithril will lower onboarding friction through faster sync times and enable tooling for exchanges, wallets, monitoring, bridges, full wallets, light wallets, and light clients.
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
- snapshot_bundle_hash: `e6f53c6932f837d753ef5b90b758fd419789ae6e4133b417c23b56a11234b502`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

