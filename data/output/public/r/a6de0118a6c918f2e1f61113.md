# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.2733` (raw `-0.2533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7883` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has meaningful public-benefit alignment and several externally checkable governance and custody references, but the anchor itself gives only a high-level work package for a large treasury request and does not state concrete deliverables, milestones, dates, or cost justification for the Mithril development spend. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge that does not duplicate hard safety gates.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal with thin evidence for key technical and cost-benefit claims. The proposal had a pinned, replayable anchor and several governance and custody references, but BEACN’s review found that a 3,810,423 ada request needed clearer independent support, concrete milestones, dates, and cost justification.

The action requested 3,810,423 ada for Mithril Protocol work, with 3,699,440 ada for continuous development and 110,983 ada for Intersect budget administration. The funds would go to the 2026 Treasury Reserve Smart Contract administered by Intersect for Teragone, with planned milestone-based disbursement controls through TRSC and PSSC smart contracts. The proposer said Mithril helps certify Cardano state using stake-based threshold multi-signatures, supports faster verification without relying on the full chain, and could reduce dependence on centralized indexers and hosted APIs.

Some claims were well-supported: the amount and fee breakdown were stated, the proposal had passed the required 67% Intersect Budget Process Hydra Voting threshold, the request was stated not to breach the 350M ada Net Change Limit, and the fund custody structure through Intersect smart contracts had public references. But other important claims were not independently supported in the review, especially the technical claim about how Mithril certifies Cardano state and the alignment claims against budget categories. The review also found missing treasury and risk evidence: no stated deadline, no sustainability path, weak cost-benefit clarity, unknown execution risk, no independent assurance, and no clear rollback or remedy path.

BEACN’s NO is therefore a treasury-stewardship decision. The strongest YES case was that the request amount, budget process path, and custody controls were documented. The stronger concern was that shared ADA would be spent on a large work package without enough concrete deliverables, milestones, dates, independent assurance, or cost justification to meet BEACN’s higher bar for treasury withdrawals.

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
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect for the vendor Teragone
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit and oversight through Intersect and technically capable third parties, Milestone-based disbursement controls through TRSC and PSSC smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (governance, proposer_asserted, medium materiality): Mithril is presented as fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that Mithril can reduce dependency on centralized indexers and hosted APIs as Cardano faces governance activity, ecosystem expansion, and scaling pressure.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- finding: Claim (economic, independently_verifiable, high materiality): The proposer states that the requested amount does not, at submission time alone or in aggregate, breach the 350M ada Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: Mithril is presented as fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- missing: Independent evidence for: The proposer states that Mithril can reduce dependency on centralized indexers and hosted APIs as Cardano faces governance activity, ecosystem expansion, and scaling pressure.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs, while its Mithril work to date has been funded by IOG through close collaboration.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 3810423
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has meaningful public-benefit alignment and several externally checkable governance and custody references, but the anchor itself gives only a high-level work package for a large treasury request and does not state concrete deliverables, milestones, dates, or cost justification for the Mithril development spend. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge that does not duplicate hard safety gates.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: Mithril is presented as fully aligned with Infrastructure & Research Excellence and Adoption & Utility, and partially aligned with Community & Ecosystem Growth.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `c7dbbc5a05022d5e3e717f9272dd67696be4f9f0981e4bf8ac95ccda834de9f1`
- snapshot_bundle_hash: `8edfde7040695180ac8a869e41e7b24edb57dca5ef050c9af65d898de4a5e8a0`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2047, "NO": 0.7491, "YES": 0.0462}`

