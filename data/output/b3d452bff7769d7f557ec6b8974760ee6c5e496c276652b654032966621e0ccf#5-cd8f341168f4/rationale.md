# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (binding treasury composite; advisory raw signal `-0.53`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): A small positive nudge is justified because the proposal provides a concrete budget breakdown, on-chain recipient details, external references for Hydra voting and audits, and described milestone/oversight controls, while several core technical-benefit claims remain proposer assertions rather than evidence in the anchor itself.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs independently verified Net Change Limit evidence before a directional vote. This is a conservative, evidence-based hold: the proposal may be reviewable and several governance and budget details are present, but BEACN will not approve or oppose a treasury withdrawal until the applicable limit is pinned and independently verified from public chain evidence.

The action requests 3,810,423 ada for Mithril Protocol continuous development through Intersect, with 3,699,440 ada for development and 110,983 ada for Intersect budget administration. The recipient is the 2026 Treasury Reserve Smart Contract stake address, with Intersect administering the withdrawal and later transferring funds to a project-specific smart contract. The proposal says Mithril helps certify Cardano state using stake-based threshold multi-signatures, addresses slow full-node synchronization and centralized light-client trust, and aligns with Cardano budget priorities.

BEACN found some claims well-supported: the anchor document was pinned and replayable, the budget total was stated, the proposal cleared the required 67% Intersect Budget Process Hydra Voting support threshold, and the described treasury administration includes smart-contract controls, role thresholds, oversight, dashboard tracking, and on-chain records. But several important claims remained thin or unsupported by independent evidence in the review, including the core technical-benefit claims about Mithril’s trustless certification model and the problem statement around node sync and light-client trust.

The review gates therefore did not clear enough evidence for a directional treasury vote. Treasury actions receive elevated scrutiny because they spend shared ada and set precedent. To unblock a YES or NO vote, BEACN would need the applicable Net Change Limit pinned and independently verified from public chain evidence, plus stronger independent support for the core technical claims, clearer line-item budget and sustainability path, independent assurance, and a rollback or remedy path.

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
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with administration by Intersect and later transfer to a project-specific smart contract.
- finding: Stated amount: 3810423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect budget administration and oversight for the withdrawal
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that full node synchronization is slow and light clients rely on centralized trust today.
- finding: Claim (governance, supported_in_proposal, medium materiality): The proposal states that Mithril is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The requested withdrawal does not, at time of submission, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget allocates 3,699,440 ada to Mithril Protocol Continuous Development and 110,983 ada to an Intersect Budget Administration fee, totaling 3,810,423 ada.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust today.
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
- finding: Strongest YES: the proposal substantiates "The proposal states that Mithril is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal states that Mithril is fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the proposal provides a concrete budget breakdown, on-chain recipient details, external references for Hydra voting and audits, and described milestone/oversight controls, while several core technical-benefit claims remain proposer assertions rather than evidence in the anchor itself.
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
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust today.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `cd8f341168f40818a0d79d96d4885345a7d1c910048345077a3b56edbda205a1`
- snapshot_bundle_hash: `eda78549f1216c09a31f5c79b8e80169a32d8c0b6a768a33d01d0c86feed3174`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `199e0465f8eabf20be3ce768498dd41ae56148a9`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

