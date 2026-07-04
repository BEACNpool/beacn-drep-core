# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.5233` (raw `-0.4833` + doctrine-LLM nudge `-0.04`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims describe a large treasury exposure with conversion to USDM, custody and smart contract risk, modeled but non-guaranteed yield, and several important adoption and audit claims that are not backed by attached references. The deterministic assessment already marks treasury, feasibility, risk, alternatives, and failure-mode analysis as incomplete, so only a small additional caution nudge is justified for evidence quality and downside protection.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal would put 9,000,000 ADA into a complex liquidity deployment while key diligence gates remained incomplete or thin, especially around budget analysis, feasibility, risk mitigation, alternatives, and failure modes.

The proposal asked to deploy Cardano treasury assets into Strike Finance V2 liquidity infrastructure for 12 months, selling ADA for USDM liquidity. It described this as a productive deployment rather than grant funding, with an independent multisig council administering the assets, monthly transparency reports, third-party assurance checkpoints, a month-6 yield return, and a month-12 return of remaining treasury-owned assets plus yield, minus any realized wind-down losses.

Several basic claims were supported in the proposal: the 9,000,000 ADA request, the ADA-to-USDM deployment model, the proposed multisig custody structure, the listed risks, the review and wind-down triggers, and V2 usage metrics through 2026-06-15. But important claims were only proposer assertions or lacked independent evidence, including the modeled 10% annual USD-denominated return, broader Strike adoption and revenue figures, the claim that Strike handled more than 50% of Cardano trading activity over six months, and the expected official audit, since no completed audit report was included.

Because this is a treasury withdrawal, BEACN applied a higher evidence bar. The review found an available pinned anchor document and a plausible strongest YES case, but still recorded seven open blockers: missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. With treasury diligence incomplete, risk review thin, no milestone-gated disbursement or line-item budget shown, and unsupported material claims about expected returns and adoption, the evidence did not justify approving this use of shared treasury ADA.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 9.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: 12-month productive deployment of Cardano treasury assets into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM stablecoin liquidity.
- finding: Recipient: independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta, administering a Strike Finance liquidity deployment
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned liquidity into Strike Finance V2 USDM liquidity infrastructure, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of remaining treasury-owned deployed assets plus remaining realized yield at month 12, minus any realized losses in a wind-down scenario, Provide monthly public transparency reports covering deployment status, utilization, volume, P&L, yield, drawdown, stablecoin exposure, risks, and deviations, Provide third-party assurance reports at deployment confirmation, month-6 distribution, and month-12 return
- finding: Deadline/expiry: 12 months from deployment; month-6 yield distribution; wind-down reconciliation within 30 days if triggered
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to create approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer models a 10% USD-denominated annual return, equal to about 135,000 USD or 900,000 ADA-equivalent in annual yield, but states returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, more than 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states Strike accounted for more than 50% of Cardano trading activity over the past six months.
- finding: Claim (adoption, supported_in_proposal, medium materiality): The document provides V2 launch-to-2026-06-15 metrics including 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 users, and 30,105 USD total V2 revenue.
- missing: Independent evidence for: The proposer models a 10% USD-denominated annual return, equal to about 135,000 USD or 900,000 ADA-equivalent in annual yield, but states returns are not guaranteed.
- missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, more than 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposer states Strike accounted for more than 50% of Cardano trading activity over the past six months.
- missing: Independent evidence for: The proposal states Strike V2 has undergone unofficial reviews and that an official audit by Christian Schmitz is expected by July 1, 2026, but no completed audit report is included in the document.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 9.00M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposer models a 10% USD-denominated annual return, equal to about 135,000 USD or 900,000 ADA-equivalent in annual yield, but states returns are not guaranteed." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9.00M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.040 (clamped to ±0.05): The claims describe a large treasury exposure with conversion to USDM, custody and smart contract risk, modeled but non-guaranteed yield, and several important adoption and audit claims that are not backed by attached references. The deterministic assessment already marks treasury, feasibility, risk, alternatives, and failure-mode analysis as incomplete, so only a small additional caution nudge is justified for evidence quality and downside protection.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer models a 10% USD-denominated annual return, equal to about 135,000 USD or 900,000 ADA-equivalent in annual yield, but states returns are not guaranteed.
- Claims and evidence missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, more than 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `7e125de27e860c7bf378c8bb0e4af613e2f3902c0d5500c2151bbf70e21be5f0`
- snapshot_bundle_hash: `61cda46b3a0de992abe10257d2b9fcee635f1bba82e93e61bc108972df5f5680`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1218`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

