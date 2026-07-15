# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (binding treasury composite; advisory raw signal `-0.53`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show alignment with public-benefit infrastructure, independently verifiable governance-process references, NCL compliance, and detailed custody/oversight mechanisms. The adjustment remains small because several key benefit and prior-funding assertions are proposer-asserted rather than evidenced inside the document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Mithril or of the requested work.

The action requests 3,810,423 ada from the treasury for Mithril Protocol continuous development and Intersect budget administration. The proposal says Mithril improves fast, trustless verification of Cardano state, supports interoperability, and can reduce onboarding friction for exchanges, wallets, monitoring tools, nodes, and applications. It also states that 3,699,440 ada would go to Mithril development and 110,983 ada to Intersect administration, with funds managed through the 2026 Treasury Reserve Smart Contract stake address using the TRSC/PSSC framework.

Several governance and custody claims were well supported: the proposal anchor was pinned and replayable, the action passed the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase, the submitted withdrawal did not by itself or in aggregate breach the stated 350M ada Net Change Limit for Epoch 613 to Epoch 713, and the treasury management framework includes listed contract addresses, oversight entities, multisignature thresholds, and a public dashboard. But several important claims remained thin or unsupported by independent evidence, including the core technical claim about Mithril’s stake-based threshold multi-signatures, the claimed alignment with Infrastructure & Research Excellence, execution risk, independent assurance, rollback or remedy paths, a full line-item budget, and a sustainability path.

Because this is a treasury withdrawal, BEACN applies a higher evidence bar: shared ADA is being spent and precedent is being set. A YES vote could be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the missing technical, budget, sustainability, assurance, and remedy details. Until then, NEEDS_MORE_INFO avoids overstating certainty while keeping the proposal open for a better-evidenced directional vote.

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
- finding: Requested: Withdraw treasury funds for Mithril Protocol continuous development and Intersect budget administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, managed by Intersect using TRSC/PSSC framework
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, milestone-based disbursement controls through TRSC/PSSC
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says Mithril is fully aligned with Infrastructure & Research Excellence because state proofs strengthen cross-chain interoperability.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The requested withdrawal does not, at time of submission alone or in aggregate, breach the 350M ada Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (governance, supported_in_proposal, high materiality): Audit and oversight costs are included in the proposal overhead, with Intersect and technically capable third parties providing reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: The proposal says Mithril is fully aligned with Infrastructure & Research Excellence because state proofs strengthen cross-chain interoperability.
- missing: Independent evidence for: The proposal says faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
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
- finding: Strongest YES: the proposal substantiates "The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show alignment with public-benefit infrastructure, independently verifiable governance-process references, NCL compliance, and detailed custody/oversight mechanisms. The adjustment remains small because several key benefit and prior-funding assertions are proposer-asserted rather than evidenced inside the document.
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
- Claims and evidence missing: Independent evidence for: The proposal says Mithril is fully aligned with Infrastructure & Research Excellence because state proofs strengthen cross-chain interoperability.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `2625df61353c2adb9664ca9728a50976eaaa53535bd9f6108a52dd360184b6a2`
- snapshot_bundle_hash: `856a46adb5cd6044ef3027cfe5daffb0a7ddf739646c1799d0e4aa4e2e67d30d`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

