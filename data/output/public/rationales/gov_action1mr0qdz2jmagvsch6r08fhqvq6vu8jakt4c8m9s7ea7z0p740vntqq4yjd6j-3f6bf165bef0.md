# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims describe established open-source wallet infrastructure, concrete maintenance deliverables, independently verifiable release/version metrics, and milestone-based Intersect oversight. The nudge remains small because several important adoption and track-record claims are proposer asserted and the request is a substantial treasury spend.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal requires independent Net Change Limit verification before a directional vote. The proposal says the withdrawal does not breach the applicable 350 million ADA Net Change Limit for Epoch 613 to Epoch 713, but BEACN’s review requires that limit to be pinned and independently verified from public chain evidence before supporting or opposing a treasury action.

The proposal asks for 1,785,333 ADA for Se7en Labs, Inc. to maintain and improve Daedalus over a 52-week contract period, administered through Intersect and project-specific treasury smart contract arrangements. The requested budget is clearly broken down: 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for a financial audit, and 52,000 ADA for Intersect administration. The work includes protocol maintenance, hard fork readiness, support for Keystone and Flex hardware wallets, a CIP-30 dApp connector, Japanese localisation, user support, security and dependency maintenance, signed releases, and an architecture assessment due by Q3 2027.

Several parts of the proposal were well-supported enough to review: the anchor document was pinned and replayable, the budget was specific, release timing and version-currency metrics were described as publicly verifiable, and Intersect was described as administrator and independent milestone verifier with monthly disbursements against verified work. But important claims remained unsupported by independent evidence, including that Daedalus is Cardano’s only full-node desktop wallet, that it avoids third-party APIs or trusted backends, and that it has about 4,000 monthly active users with a higher true count. The review also found thin evidence overall, medium execution risk, missing sustainability and cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the key wallet, adoption, assurance, sustainability, cost-benefit, and remedy claims.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 1.79M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. via Intersect administration and project-specific treasury smart contract arrangements
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, hard fork readiness, and releases at least 2 weeks before each mainnet hard fork, Ecosystem expansion including Keystone and Flex hardware wallet support, CIP-30 dApp connector, and Japanese localisation, User support across GitHub, community forums, direct channels, and Japanese-language support, Security and dependency maintenance for Electron, Node.js, wallet dependencies, Nix build infrastructure, and signed releases, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: Contract year covering 52 weeks; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be higher.
- finding: Claim (adoption, proposer_asserted, high materiality): Se7en Labs has operated under an IOG contract for Daedalus maintenance since January 2026, closing August 31, 2026, and shipped Daedalus 8.0 and 11.0 during that period.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,785,333 ADA, including 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): The work will maintain Daedalus compatibility with upcoming Cardano protocol changes, including hard forks, Leios, Peras, and Nested Transactions, with compatible stable releases at least two weeks before mainnet activation.
- finding: Claim (technical, supported_in_proposal, medium materiality): The proposal commits to implementing Keystone and Flex hardware wallet support and a CIP-30 dApp connector in stable Daedalus releases during the contract period.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be higher.
- missing: Independent evidence for: Se7en Labs has operated under an IOG contract for Daedalus maintenance since January 2026, closing August 31, 2026, and shipped Daedalus 8.0 and 11.0 during that period.
- missing: Independent evidence for: Se7en Labs states it has not received ADA from the Cardano Treasury within the last 24 months.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,785,333 ADA, including 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1785333
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,785,333 ADA, including 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims describe established open-source wallet infrastructure, concrete maintenance deliverables, independently verifiable release/version metrics, and milestone-based Intersect oversight. The nudge remains small because several important adoption and track-record claims are proposer asserted and the request is a substantial treasury spend.
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
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `3f6bf165bef09c0437ec8ba119e6b340c47839e11f08c1f31bc1322d93a74bcf`
- snapshot_bundle_hash: `f4589d1eec27bd078212e352e12cd91251f3578381c8340d4c2459561dbf7993`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

