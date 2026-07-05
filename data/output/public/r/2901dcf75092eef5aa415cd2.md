# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.2333` (raw `-0.2533` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7783` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a clearly specified amount, budget split, on-chain recipient structure, references for Hydra voting and audits, and governance controls for disbursement, which modestly improves evidence quality and treasury stewardship relative to a thin treasury ask. The nudge remains small because core impact and prior-funding claims are partly proposer asserted and the document does not state detailed milestones or deadlines.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a treasury withdrawal request under elevated scrutiny, and the review found the evidence too thin on key impact, cost-benefit, and risk questions to justify spending 3,810,423 ada.

The action asked to withdraw 3,810,423 ada for continuous Mithril Protocol development, administered through Intersect budget management smart contracts for Teragone. The proposal split the amount into 3,699,440 ada for development and 110,983 ada for Intersect’s administration fee. It also described milestone-based disbursement controls through Treasury Reserve and Project-Specific Smart Contracts, with an Oversight Committee and public dashboard for auditability. No deadline was stated in the document.

Several parts were well supported. The proposal had a pinned, replayable anchor document. It substantiated the technical claim that Mithril uses stake-based threshold multi-signatures to certify Cardano state and enable faster state verification. The amount and budget split were clear, the Intersect budget process support threshold was documented, and the on-chain administration structure was independently verifiable. Those factors counted in favor of the proposal.

The NO came from what remained unresolved. Some important benefit claims were only proposer asserted, including the scale of the infrastructure problem and the expected adoption, utility, interoperability, sync-time, and tooling benefits. The review also found missing treasury sustainability path, missing cost-benefit clarity, unknown execution risk, missing independent assurance, and no rollback or remedy path. With treasury flow already in an unsustainable signal regime, BEACN treated the spending request conservatively and concluded that the evidence did not meet the higher bar for a treasury withdrawal.

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
- finding: Requested: Withdraw treasury funds for Mithril Protocol continuous development, with administration through Intersect budget management smart contracts.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor Teragone
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Milestone-based disbursement controls through TRSC and PSSC
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling faster state verification without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that full node synchronisation is slow and light clients rely on centralized trust, making secure and efficient access to blockchain state a pressing infrastructure challenge.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal says Mithril supports infrastructure and research excellence, adoption and utility, and community ecosystem growth by improving interoperability, sync times, and tooling opportunities.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested 3,810,423 ada is split into 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states that the requested amount does not, at submission, breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713.
- missing: Independent evidence for: The proposal states that full node synchronisation is slow and light clients rely on centralized trust, making secure and efficient access to blockchain state a pressing infrastructure challenge.
- missing: Independent evidence for: The proposal says Mithril supports infrastructure and research excellence, adoption and utility, and community ecosystem growth by improving interoperability, sync times, and tooling opportunities.
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
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling faster state verification without relying on the entire chain." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that full node synchronisation is slow and light clients rely on centralized trust, making secure and efficient access to blockchain state a pressing infrastructure challenge." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling faster state verification without relying on the entire chain." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): The extracted claims show a clearly specified amount, budget split, on-chain recipient structure, references for Hydra voting and audits, and governance controls for disbursement, which modestly improves evidence quality and treasury stewardship relative to a thin treasury ask. The nudge remains small because core impact and prior-funding claims are partly proposer asserted and the document does not state detailed milestones or deadlines.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that full node synchronisation is slow and light clients rely on centralized trust, making secure and efficient access to blockchain state a pressing infrastructure challenge.
- Claims and evidence missing: Independent evidence for: The proposal says Mithril supports infrastructure and research excellence, adoption and utility, and community ecosystem growth by improving interoperability, sync times, and tooling opportunities.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `546412e8d758f9f4c7c1d860db04348578f5f3c5bc533395f2eaa56dbe863bc9`
- snapshot_bundle_hash: `ed5dbbed1c45f2f319d0aa29c2476c237cfaac4afa2e7284d3ff45502e2573fe`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.214, "NO": 0.7379, "YES": 0.048}`

