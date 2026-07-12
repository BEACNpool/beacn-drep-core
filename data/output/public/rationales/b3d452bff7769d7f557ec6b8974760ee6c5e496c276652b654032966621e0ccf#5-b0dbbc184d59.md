# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.219` (raw `-0.33` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7747` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe established public infrastructure, continuity funding, explicit oversight controls, milestone-based disbursement, on-chain addresses, and independently checkable governance-process references; the adjustment remains small because core technical and adoption benefits are mostly asserted rather than evidenced inside the document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 3,810,423 ada for continued Mithril Protocol development through the Intersect budget process, with 3,699,440 ada for Mithril work and 110,983 ada for Intersect budget administration. The recipient is the 2026 Treasury Reserve Smart Contract stake address, with Intersect administering funds and Teragone identified as the vendor. The proposal describes milestone-based disbursement controls, oversight and reporting obligations, and multi-party oversight involving Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, and Eternl.

Several governance and treasury-process claims were supported well enough to review: the anchor document was pinned and replayable, the requested amount and budget split were stated, oversight controls were described, and the proposal included smart-contract addresses plus references to community and on-chain tracking. However, core benefit claims were thinner: the technical claims that Mithril solves the cost and complexity of secure Cardano state verification, and enables rapid trustless verification without the full chain, were treated as proposer assertions without independent evidence in the supplied review.

This is a conservative, evidence-based hold, not a rejection of Mithril. A directional vote would be unblocked by pinned, independently verifiable public-chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the main technical benefit claims, clearer cost-benefit and sustainability information, independent assurance, and a rollback or remedy path for execution risk.

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
- finding: Requested: Withdraw treasury funds for Mithril Protocol continued development through the Intersect budget process.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with Intersect administering funds and Teragone identified as the vendor in the rationale.
- finding: Stated amount: 3810423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect budget administration and oversight, Milestone-based disbursement controls through treasury management smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state using stake-based threshold multi-signatures.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says Mithril enables rapid trustless state verification for nodes and applications without relying on the entire chain.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal claims faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested amount does not breach the applicable 350M ada Net Change Limit covering Epoch 613 to Epoch 713 at the time of submission.
- missing: Independent evidence for: Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state using stake-based threshold multi-signatures.
- missing: Independent evidence for: The proposal says Mithril enables rapid trustless state verification for nodes and applications without relying on the entire chain.
- missing: Independent evidence for: The proposal claims faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- missing: Independent evidence for: The proposal says Teragone has not previously received direct Cardano treasury or community governance funding but has worked on Mithril for several years through IOG funding.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state using stake-based threshold multi-signatures." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe established public infrastructure, continuity funding, explicit oversight controls, milestone-based disbursement, on-chain addresses, and independently checkable governance-process references; the adjustment remains small because core technical and adoption benefits are mostly asserted rather than evidenced inside the document.
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
- Claims and evidence missing: Independent evidence for: Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state using stake-based threshold multi-signatures.
- Claims and evidence missing: Independent evidence for: The proposal says Mithril enables rapid trustless state verification for nodes and applications without relying on the entire chain.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `b0dbbc184d59850e07f6937767b2de28c018776a65fb66e7a3d8975ee03ecbe6`
- snapshot_bundle_hash: `305773a78eb8d01d89fcbae614561e801c127fc766cfff4cdbbe00fe3f458800`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5007, "NO": 0.0487, "YES": 0.4505}`

