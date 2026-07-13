# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **YES**
Score: `0.2055` (raw `-0.33` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7414` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal has plausible public-benefit alignment as established wallet infrastructure, but the assessment marks claims and evidence as thin, and several high-materiality adoption, cost, and operational-dependency claims are proposer-asserted rather than independently evidenced. Given treasury stewardship and evidence quality outrank ecosystem growth, a small cautionary negative nudge is justified without overriding the deterministic gates.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Eternl: Path to Sustainability - v2. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal for 12 months of Eternl operations, maintenance, support, infrastructure, audits/oversight, and continued development while Eternl introduces paid Pro plans. It asks the treasury for 2350000 ADA. The strongest grounded claim is: Eternl requests ₳2,350,000, valued at about $420,000 using $0.1787 per Ada, to fund a 12-month operating period.

A residual watch item: this claim remains proposer-asserted rather than independently shown: Eternl states that 6.0 FTE across 10 contributors at $70,000 per FTE are required for its annual operations.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 2.35M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal for 12 months of Eternl operations, maintenance, support, infrastructure, audits/oversight, and continued development while Eternl introduces paid Pro plans.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for web, browser extension, iOS, Android, and beta channels, Backend infrastructure and operations including multi-region servers, Cardano nodes, DBSync/indexers, metadata aggregation, and monitoring, User support through Discord, Telegram, public channels, partner channels, wiki updates, and educational content, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Independent treasury fund-use audits in February 2027 and August 2027 with oversight metrics for balances, conversion rates, transaction hashes, and repayment hashes
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $420,000 using $0.1787 per Ada, to fund a 12-month operating period.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal allocates the request across frontend, backend, support, admin, and audits, with frontend receiving 55% and backend 25%.
- finding: Claim (economic, proposer_asserted, high materiality): Eternl states that 6.0 FTE across 10 contributors at $70,000 per FTE are required for its annual operations.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl says it has about 100,000 browser-extension installs and about 30,000 Android/iOS installs, and that about 5,500 Pro users would cover the $420,000 annual cost.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposer commits to converting up to $420,000 worth of Ada into stablecoins, placing it in a public company wallet, and returning any Ada above that amount to the treasury.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposer commits to semiannual repayment checks and to using surplus treasury stablecoins plus paid-plan income to repay up to the received $420,000 USD value in Ada, with possible additional donations capped at $210,000 worth of Ada.
- missing: Independent evidence for: Eternl states that 6.0 FTE across 10 contributors at $70,000 per FTE are required for its annual operations.
- missing: Independent evidence for: Eternl says it has about 100,000 browser-extension installs and about 30,000 Android/iOS installs, and that about 5,500 Pro users would cover the $420,000 annual cost.
- missing: Independent evidence for: Independent audits of treasury fund use are planned for February 2027 and August 2027 by a party unaffiliated with Tastenkunst GmbH or the Eternl team.
- missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using $0.1787 per Ada, to fund a 12-month operating period." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl states that 6.0 FTE across 10 contributors at $70,000 per FTE are required for its annual operations." — so cost or precedent may outweigh the benefit.
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
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using $0.1787 per Ada, to fund a 12-month operating period." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The proposal has plausible public-benefit alignment as established wallet infrastructure, but the assessment marks claims and evidence as thin, and several high-materiality adoption, cost, and operational-dependency claims are proposer-asserted rather than independently evidenced. Given treasury stewardship and evidence quality outrank ecosystem growth, a small cautionary negative nudge is justified without overriding the deterministic gates.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl states that 6.0 FTE across 10 contributors at $70,000 per FTE are required for its annual operations.
- Claims and evidence missing: Independent evidence for: Eternl says it has about 100,000 browser-extension installs and about 30,000 Android/iOS installs, and that about 5,500 Pro users would cover the $420,000 annual cost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `e83e61d9caace6a900c1603f5e23eff10d3708351d50c885723de5c3b3b3afc1`
- snapshot_bundle_hash: `57a4a02d7141cd3cd6f652e6ab455464dd8ad1c01572f7a0d72c5abf2195748f`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `a650e5f55d3662a45d71b3a19d5301fd64c2bbee`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2255, "NO": 0.0496, "YES": 0.7249}`

