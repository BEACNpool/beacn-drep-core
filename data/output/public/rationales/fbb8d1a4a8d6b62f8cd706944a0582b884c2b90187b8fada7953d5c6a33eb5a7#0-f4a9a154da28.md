# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **YES**
Score: `0.2055` (binding treasury composite; advisory raw signal `-0.33`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7414` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims describe a plausible public-benefit infrastructure case and include some stewardship mechanisms, but the deterministic assessment labels claims and evidence as thin, while key adoption and revenue assumptions are mostly proposer-asserted. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending lean.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Eternl: Path to Sustainability - v2. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements while introducing a Pro plan intended to replace treasury support over time. It asks the treasury for 2350000 ADA. The strongest grounded claim is: Eternl requests ₳2,350,000, valued at about $0.1787 per ADA, to fund a 12-month delivery period from August 2026 to July 2027.

A residual watch item: this claim remains proposer-asserted rather than independently shown: The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements while introducing a Pro plan intended to replace treasury support over time.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend and backend maintenance and development for Eternl across web, browser extension, Android, and iOS, Backend infrastructure operations including nodes, chain indexers, application servers, metadata aggregation, and monitoring, User support through Discord, Telegram, public channels, project support, wiki updates, and educational videos, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Independent audits of treasury fund use and oversight metrics in February 2027 and August 2027, Conversion of up to $420,000 worth of ADA into stablecoins, public wallet monitoring, and return of ADA above that amount to the treasury, Semiannual assessment of repayment or donation obligations based on remaining treasury stablecoins and Pro plan income
- finding: Deadline/expiry: 12-month period, August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per ADA, to fund a 12-month delivery period from August 2026 to July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states Eternl's annual operating cost is about $420,000, funding 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce Pro plans priced at $96 per year for personal users and $360 per year for company users, with about 5,500 paying users needed to cover the stated annual cost.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says up to $420,000 worth of ADA will be converted into stablecoins and deposited into a public company wallet, with ADA above that amount returned to the treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal commits to independent audits by an unaffiliated party in February 2027 and August 2027 covering receipt, custody, conversion, spending, balances, Pro plan income relevant to repayment, and treasury refunds or repayments.
- missing: Independent evidence for: The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- missing: Independent evidence for: The proposal says up to $420,000 worth of ADA will be converted into stablecoins and deposited into a public company wallet, with ADA above that amount returned to the treasury.
- missing: Independent evidence for: The proposer claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per ADA, to fund a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per ADA, to fund a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims describe a plausible public-benefit infrastructure case and include some stewardship mechanisms, but the deterministic assessment labels claims and evidence as thin, while key adoption and revenue assumptions are mostly proposer-asserted. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending lean.
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
- Claims and evidence missing: Independent evidence for: The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- Claims and evidence missing: Independent evidence for: The proposal says up to $420,000 worth of ADA will be converted into stablecoins and deposited into a public company wallet, with ADA above that amount returned to the treasury.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `f4a9a154da28c21db13610910dd04f9e49eb9acdabccfa6625bde76f49a7c25a`
- snapshot_bundle_hash: `7ee18081f706171d701b3c332c6d41de989db325d03e89570b064ee35dc078f7`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2255, "NO": 0.0496, "YES": 0.7249}`

