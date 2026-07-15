# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): The extracted claims show a large treasury request for established infrastructure with concrete budget line items, on-chain recipient details, governance-process references, NCL compliance claims, smart contract custody details, audits, and a public dashboard. The document still relies on proposer assertions for some core benefit claims and does not state deadlines, so the nudge should remain small and evidence-quality bounded.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 3,810,423 ada for Mithril Protocol continuous development, administered through the Intersect budget process and smart contract controls. The proposal says this includes 3,699,440 ada for Mithril development and 110,983 ada for Intersect’s administration fee, with funds first directed to the 2026 Treasury Reserve Smart Contract stake address and later managed through TRSC and PSSC smart contracts. It also claims Mithril addresses slow full-node synchronization and centralized light-client trust assumptions, using stake-based threshold multi-signatures to certify Cardano state.

Several parts were well-supported in the proposal: the requested amount, the budget split, the recipient flow, the Intersect process references, milestone-based disbursement controls, oversight, audits, smart contract administration, and public dashboard references. But some core benefit claims remained only proposer-asserted, including the technical claims about Mithril’s trustless state certification and the infrastructure problem it solves. The review also found missing or thin evidence around line-item budget detail, sustainability path, independent assurance, rollback or remedy path, and execution risk.

This is a conservative, evidence-based hold, not a rejection of Mithril. To unblock a YES or NO vote, BEACN would need the applicable Net Change Limit pinned and independently verified from public chain evidence, plus stronger replayable evidence for the unsupported technical benefit claims and the missing treasury-risk details.

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
- finding: Requested: Withdraw treasury funds for Mithril Protocol continuous development through Intersect budget process administration and smart contract management.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor Teragone
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Milestone-based disbursement controls through TRSC and PSSC smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril is described as using stake-based threshold multi-signatures to certify Cardano state trustlessly, enabling faster state verification without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that full node synchronization is slow and light clients currently rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal claims Mithril is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to Hydra voting records, documentation, final audited results, and an audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposer states the requested withdrawal does not, at submission, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713 and links to the related governance action.
- missing: Independent evidence for: Mithril is described as using stake-based threshold multi-signatures to certify Cardano state trustlessly, enabling faster state verification without relying on the entire chain.
- missing: Independent evidence for: The proposer states that full node synchronization is slow and light clients currently rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- missing: Independent evidence for: The proposal claims Mithril is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- missing: Independent evidence for: The proposal states Teragone has not previously received direct Cardano treasury or community governance funding, but has worked on Mithril for several years through IOG-funded collaboration.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril is described as using stake-based threshold multi-signatures to certify Cardano state trustlessly, enabling faster state verification without relying on the entire chain." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a large treasury request for established infrastructure with concrete budget line items, on-chain recipient details, governance-process references, NCL compliance claims, smart contract custody details, audits, and a public dashboard. The document still relies on proposer assertions for some core benefit claims and does not state deadlines, so the nudge should remain small and evidence-quality bounded.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Mithril is described as using stake-based threshold multi-signatures to certify Cardano state trustlessly, enabling faster state verification without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: The proposer states that full node synchronization is slow and light clients currently rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `3bfaeef564f7962db3b50a7a74032122570a61515205b9ef405e5899dba6cbb5`
- snapshot_bundle_hash: `15567f7bb3b018f4d4690d3d3237064cf025168f6d322772166734c1e1cebd79`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

