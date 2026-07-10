# Rationale: gov_action1fdatlfcdnzzcw5x9pnt9r42v992nqw65zze57s8tyk0jll78eyusqccn9gc
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7758` | Readiness: `0.75`
> Reasoning layer (precomputed): The claims show meaningful alignment with public-benefit ecosystem growth and some checkable track record references, but the request is large and several central assertions about KPI effectiveness, live on-chain measurement, and official ecosystem adoption remain proposer-asserted within the supplied material. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than rewarding plausible but incompletely verified ecosystem growth claims.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Cardano Builder DAO. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to continue and expand the Cardano Builder DAO as a smart contract-governed, KPI-driven funding mechanism for Cardano builders. It asks the treasury for 20000000 ADA. The strongest grounded claim is: The proposal says funded projects are required to track monthly active users, TVL, and on-chain transactions.

A material claim remains proposer-asserted or thinly supported: The Cardano Builder DAO is presented as an ecosystem-wide, purpose-built, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs. Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 20.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to continue and expand the Cardano Builder DAO as a smart contract-governed, KPI-driven funding mechanism for Cardano builders.
- finding: Recipient: Cardano Builder DAO, with funds first received and overseen by an independent council composed of dRep DAO members before milestone-based disbursement.
- finding: Stated amount: 20000000
- finding: Deliverables: Allocate capital to builders expected to improve Cardano 2030 KPIs such as monthly active users, monthly on-chain transactions, and TVL., Require funded projects to track monthly active users, TVL, and on-chain transactions., Continue development of KPI tracking from self-reported dashboards toward live on-chain Cardano data., Run DAO governance processes including review, debate, temperature checks, final voting, and transparent fund distribution., Use an independent multisig and administrator validation before Cardano Builder DAO receives funds after milestone completion.
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, proposer_asserted, high materiality): The Cardano Builder DAO is presented as an ecosystem-wide, purpose-built, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says funded projects are required to track monthly active users, TVL, and on-chain transactions.
- finding: Claim (technical, proposer_asserted, high materiality): The DAO says it built Version 1 and Version 2 of a KPI dashboard, moving from self-reported KPI tracking toward tracking tied directly to live on-chain Cardano data.
- finding: Claim (adoption, independently_verifiable, high materiality): The Cardano Builder DAO says it has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- finding: Claim (governance, independently_verifiable, high materiality): Round 1 is described as having 38 voting members, 27 requesting members, 20 funded companies, an 83% governance participation rate, and 5,541,335 ADA distributed through a transparent smart contract-governed process.
- finding: Claim (governance, independently_verifiable, high materiality): Round 2 is described as adding 18 new members, funding 14 companies, and achieving an 88% member participation rate after review, debate, temperature checks, and final voting.
- missing: Independent evidence for: The Cardano Builder DAO is presented as an ecosystem-wide, purpose-built, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs.
- missing: Independent evidence for: The DAO says it built Version 1 and Version 2 of a KPI dashboard, moving from self-reported KPI tracking toward tracking tied directly to live on-chain Cardano data.
- missing: Independent evidence for: The proposal says official Cardano developer documentation describes the CB DAO as a smart contract-governed mechanism with more than 50 established Cardano projects participating in funding decisions and KPI tracking tied to on-chain activity, users, and TVL.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 20000000
- finding: Budget granularity: unknown
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.48
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal says funded projects are required to track monthly active users, TVL, and on-chain transactions." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The Cardano Builder DAO is presented as an ecosystem-wide, purpose-built, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 20000000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal says funded projects are required to track monthly active users, TVL, and on-chain transactions." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The claims show meaningful alignment with public-benefit ecosystem growth and some checkable track record references, but the request is large and several central assertions about KPI effectiveness, live on-chain measurement, and official ecosystem adoption remain proposer-asserted within the supplied material. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than rewarding plausible but incompletely verified ecosystem growth claims.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The Cardano Builder DAO is presented as an ecosystem-wide, purpose-built, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs.
- Claims and evidence missing: Independent evidence for: The DAO says it built Version 1 and Version 2 of a KPI dashboard, moving from self-reported KPI tracking toward tracking tied directly to live on-chain Cardano data.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `b22ea5de12b32ab50dc3a4850dfa63d02d6a0d278497e4d9507b3ab5bee09a5c`
- snapshot_bundle_hash: `5109272491d87ec5e888164dc210cffc2575be2f21f5ceeb1fedbc8b81dd403a`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

