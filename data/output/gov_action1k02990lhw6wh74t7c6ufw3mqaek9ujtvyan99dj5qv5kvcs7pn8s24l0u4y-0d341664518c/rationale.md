# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.2533` (raw `-0.2533` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7833` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show meaningful public-benefit infrastructure alignment and several checkable governance and oversight references, but the core technical impact, cost reasonableness, milestone substance, and vendor execution details are mostly asserted in the anchor rather than demonstrated. The deterministic engine already accounts for treasury caution and evidence completeness, so no additional bounded adjustment is warranted.

## Plain-language explanation (precomputed)
BEACN voted NO because a central technical claim behind the funding request was not independently supported by replayable public evidence, and treasury withdrawals require a higher evidence bar because they spend shared ada and set precedent.

The action requested 3,810,423 ada from the treasury for Mithril Protocol continuous development and Intersect budget administration. The proposal broke this into 3,699,440 ada for Mithril development and 110,983 ada for administration, with funds administered through Intersect using Treasury Reserve and Project-Specific smart contracts, oversight, reporting obligations, and milestone-based disbursement controls. The pinned anchor document was available, the requested amount was clear, and the proposal included evidence that it passed the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.

Several governance and budget-administration claims were well supported, including the Intersect process, smart contract administration structure, oversight model, dashboard visibility, and the claim that the request did not breach the applicable 350M ada Net Change Limit at submission. However, the review found the evidence base thin for key technical and adoption claims. In particular, the claim that Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid verification without relying on the full chain, was treated as unsupported by independent evidence in the review. The related claim that slow full-node sync and centralized light-client trust create a pressing infrastructure challenge was also not independently supported.

The main gates passed were basic intake, anchor availability, and several governance and treasury-administration checks. The main failures were missing independent evidence for material technical claims, missing sustainability path and cost-benefit clarity in the treasury analysis, and missing independent assurance plus a rollback or remedy path in the risk review. Given the elevated scrutiny for treasury withdrawals, those gaps outweighed the strongest YES case that the amount and administrative controls were clearly documented.

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
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor Teragone.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit and oversight through Intersect and technically capable third parties, Milestone-based disbursement controls through TRSC and PSSC smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposer states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that funding Mithril's continued development through Intersect ensures Cardano can scale while preserving decentralization guarantees.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and links to voting documentation, final audited results, and an audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states that the requested amount does not, at submission, alone or in aggregate, breach the applicable 350M ada Net Change Limit for Epoch 613 to Epoch 713.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: The proposer states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- missing: Independent evidence for: The proposer states that funding Mithril's continued development through Intersect ensures Cardano can scale while preserving decentralization guarantees.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs, while prior Mithril work was funded by IOG.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: The proposer states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `0d341664518c985716dc18cd79a8736cab97d5eb09584d61565b83798c9745a4`
- snapshot_bundle_hash: `bd6b9098832405e6d3519656509fe89873b1acd80166c17b7355aa75268833bd`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2093, "NO": 0.7436, "YES": 0.0471}`

