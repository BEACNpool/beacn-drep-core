# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence, especially the missing `treasury_amount_lovelace` field required for a treasury withdrawal. This is a conservative, evidence-based hold, not a rejection of Mithril or of the stated funding purpose.

The action requests 3,810,423 ada for Mithril Protocol continuous development and related Intersect administration costs, with funds sent to the 2026 Treasury Reserve Smart Contract and administered by Intersect on behalf of the vendor. The proposal says this includes 3,699,440 ada for development and 110,983 ada for administration, with milestone-based disbursement controls through TRSC/PSSC smart contracts. It also claims Mithril improves Cardano state verification and lowers onboarding friction through faster sync times and broader tooling possibilities.

Some governance and funding-process claims were well supported: the proposal anchor was pinned and replayable, the action passed the required 67% Intersect Budget Process Hydra Voting threshold, the amount did not breach the applicable Net Change Limit at submission, and the smart-contract administration structure and oversight approach were described. But important parts remained unsupported or incomplete, including independent evidence for the technical and adoption claims, a sustainability path, cost-benefit clarity, independent assurance, and a rollback or remedy path.

A directional YES or NO vote would require the missing treasury amount field to be complete and the review dossier to include stronger independent evidence for the key technical claims, clearer treasury analysis, and a fuller risk review. Until then, BEACN abstained rather than pretending the evidence base was strong enough for a responsible treasury vote.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continuous development and related Intersect administration costs.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with Intersect administering funds on behalf of the vendor.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Administrative oversight via Intersect Budget Administration fee, Milestone-based disbursement controls through TRSC/PSSC smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ADA, consisting of 3,699,440 ADA for Mithril Protocol Continuous Development and 110,983 ADA for an Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal says Mithril lowers onboarding friction through faster sync times and can unlock tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (governance, independently_verifiable, high materiality): The requested amount does not, at time of submission, alone or in aggregate, breach the applicable 350M ADA Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (governance, supported_in_proposal, high materiality): Audit and oversight costs are included in the overhead, and independent oversight will be provided through Intersect and technically capable third parties with reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: The proposal says Mithril lowers onboarding friction through faster sync times and can unlock tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs, while its Mithril work to date has been funded by IOG.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
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
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ADA, consisting of 3,699,440 ADA for Mithril Protocol Continuous Development and 110,983 ADA for an Intersect Budget Administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ADA, consisting of 3,699,440 ADA for Mithril Protocol Continuous Development and 110,983 ADA for an Intersect Budget Administration fee." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: The proposal says Mithril lowers onboarding friction through faster sync times and can unlock tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `2f3510b87a1d1a8e7b4c1728491d8c8f1034a1ae367b73004229b11c6f991ecb`
- snapshot_bundle_hash: `ced69597aba9eb4b7566d48c86ed5516e031b148df9755b9416330e406b9ebba`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

