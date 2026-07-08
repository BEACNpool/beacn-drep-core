# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.2733` (raw `-0.2533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7883` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has stronger-than-thin governance and custody evidence through checkable voting, NCL, smart-contract, audit, and dashboard references, but the core economic justification and deliverable specifics remain limited relative to a 3.81M ada treasury withdrawal. A small cautionary nudge is warranted because treasury stewardship and evidence quality are only partly satisfied by process controls, not by detailed scope, milestones, or cost basis in the supplied claims.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks for a large treasury withdrawal, but the supplied evidence did not sufficiently support the core technical and economic case for spending 3,810,423 ada.

The action requested 3,810,423 ada for Mithril Protocol continuous development through Intersect, with 3,699,440 ada for development and 110,983 ada for Intersect’s administration fee. The proposal included milestone-based disbursement controls through treasury smart contracts, oversight arrangements, reporting obligations, and a public dashboard. It also cleared some important process checks: the anchor document was available, the request did not breach the applicable Net Change Limit, and it had passed the 2026 Intersect Budget Process Hydra Voting threshold.

However, the review found the evidence base too thin for a treasury withdrawal of this size. The strongest technical claims, including that Mithril enables trustless certification of Cardano state using stake-based threshold multi-signatures and addresses slow full-node synchronization and light-client trust reliance, were treated as proposer assertions without independent evidence in the supplied review. The review also found missing cost-benefit clarity, no stated sustainability path, unknown execution risk, no independent assurance, and no clear rollback or remedy path.

This was not a rejection of Mithril’s potential value. It was a treasury-stewardship decision: process controls and governance support helped the proposal, but they did not fully answer whether the requested amount was justified by independently supported deliverables, costs, risks, and remedies.

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
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Milestone-based disbursement controls through TRSC and PSSC
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol continuous development and 110,983 ada for the Intersect budget administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril addresses slow full-node synchronization and centralized-trust reliance by light clients.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): At submission, the requested amount does not on its own or in aggregate breach the applicable 350M ada Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (governance, supported_in_proposal, high materiality): Audit, administrative oversight, reporting obligations, and milestone-based disbursement controls are included through Intersect overhead and third-party oversight.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: Mithril addresses slow full-node synchronization and centralized-trust reliance by light clients.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs but has worked on Mithril for several years through IOG-funded collaboration.
- missing: Independent evidence for: The Oversight Committee consists of Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, and Eternl, and its role is to verify key administrative actions using on-chain logic without discretion over governance decisions.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol continuous development and 110,983 ada for the Intersect budget administration fee." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol continuous development and 110,983 ada for the Intersect budget administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has stronger-than-thin governance and custody evidence through checkable voting, NCL, smart-contract, audit, and dashboard references, but the core economic justification and deliverable specifics remain limited relative to a 3.81M ada treasury withdrawal. A small cautionary nudge is warranted because treasury stewardship and evidence quality are only partly satisfied by process controls, not by detailed scope, milestones, or cost basis in the supplied claims.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: Mithril addresses slow full-node synchronization and centralized-trust reliance by light clients.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `45016175fd4db381f1fc62ea19259c8740ea72dd9286c4e9693159d8057f9f09`
- snapshot_bundle_hash: `5f3f6e2f4908cfbddd3d902d7a3e47c70d5cc26f41551993e6dd845996c57284`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2047, "NO": 0.7491, "YES": 0.0462}`

