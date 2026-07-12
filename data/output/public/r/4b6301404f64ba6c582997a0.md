# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.219` (raw `-0.33` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7747` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has meaningful public-benefit and infrastructure alignment, and several governance and contract-administration claims are externally checkable, but the deterministic assessment says treasury analysis remains incomplete and many core benefit and continuity claims are asserted rather than evidenced in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify only a small cautionary nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a high-impact treasury withdrawal and the deep research dossier was not complete enough to support a directional vote.

The action requested 3,810,423 ada for Mithril Protocol continuous development and Intersect budget administration, sent to the 2026 Treasury Reserve Smart Contract stake address administered by Intersect. The proposal described deliverables including Mithril development, treasury management smart contracts, milestone-based disbursement controls, reporting obligations, and an Intersect administration fee. It claimed Mithril helps Cardano by enabling faster, trustless state verification, reducing slow full-node sync and reliance on centralized services, and improving infrastructure for wallets, exchanges, monitoring, and other tools.

Some governance and budget claims were reviewable: the proposal said it met the required 67% Intersect Budget Process Hydra Voting threshold, stayed within the applicable 350M Net Change Limit, identified treasury management contract addresses and oversight structures, and gave a budget split of 3,699,440 ada for Mithril development plus 110,983 ada for administration. But several material claims still lacked independent supporting evidence in the review, including the core technical claim about Mithril’s stake-based threshold multi-signatures and the claim that it solves slow full-node synchronisation and centralized-trust reliance. The treasury review was also incomplete on sustainability and cost-benefit clarity, and the risk review was incomplete on independent assurance and rollback or remedy paths.

This is a conservative, evidence-based hold. A directional vote would require a completed deep research dossier with replayable public evidence for the major technical claims, a clearer treasury analysis covering sustainability and cost-benefit, and a risk review that addresses independent assurance plus what happens if delivery, controls, or outcomes fall short.

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
- finding: Snapshot freshness source: governance_actions_all.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw treasury funds for Mithril Protocol continuous development and Intersect budget administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect for the vendor/project.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Use of TRSC and PSSC treasury management smart contracts, Milestone-based disbursement controls and reporting obligations
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says Mithril addresses slow full-node synchronisation and centralized-trust reliance by light clients.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal asserts that without fast, verifiable, trustless infrastructure, Cardano risks growing dependency on centralized indexers and hosted APIs.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states the requested amount does not breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713 at the time of submission.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: The proposal says Mithril addresses slow full-node synchronisation and centralized-trust reliance by light clients.
- missing: Independent evidence for: The proposal states that faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- missing: Independent evidence for: The proposal asserts that without fast, verifiable, trustless infrastructure, Cardano risks growing dependency on centralized indexers and hosted APIs.
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
- finding: Strongest YES: the proposal substantiates "The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase." and clears the evidence gates.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal has meaningful public-benefit and infrastructure alignment, and several governance and contract-administration claims are externally checkable, but the deterministic assessment says treasury analysis remains incomplete and many core benefit and continuity claims are asserted rather than evidenced in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify only a small cautionary nudge.
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
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: The proposal says Mithril addresses slow full-node synchronisation and centralized-trust reliance by light clients.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `3a0284ffd49b558ac788d3f46a2a1309878d8039d2138b52e63fd5f784f166f5`
- snapshot_bundle_hash: `b34e403459c8e1c968350bdf96df089ade904417c153937199d4f5b178bf27b4`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `82a02efa3be4dedf61fea1548ca03635163347a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `21`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5007, "NO": 0.0487, "YES": 0.4505}`

