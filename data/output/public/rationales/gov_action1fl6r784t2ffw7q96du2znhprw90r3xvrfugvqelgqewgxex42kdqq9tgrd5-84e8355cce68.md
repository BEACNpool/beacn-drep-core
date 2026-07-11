# Rationale: gov_action1fl6r784t2ffw7q96du2znhprw90r3xvrfugvqelgqewgxex42kdqq9tgrd5
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7758` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a treasury action: 7 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Cardano Global Listing Expansion - Powered by Snek. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Cardano Global Listing Expansion - Powered by Snek. It asks the treasury for 5 ADA. The strongest grounded claim is: This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms.

Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
- finding: Proposed epoch: 573
- finding: Expires after epoch: 580
- finding: Treasury request: 5 ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Cardano Global Listing Expansion - Powered by Snek
- finding: Recipient: 
- finding: Stated amount: 5 ADA
- finding: Deliverables: This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms., SNEK is the largest community token on Cardano, holding the highest market capitalization, over 42,000 wallets, and more than 2 billion ADA in all-time trading volume., Over the past two years, the Snek Foundation has already invested over $4 million, entirely self funded, to secure major exchange listings., We’ve delivered the first and second ever Tier 1 listings for any Cardano native token, with Kraken and Crypto.com setting historic precedents for the ecosystem.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms.
- finding: Claim (economic, supported_in_proposal, medium materiality): SNEK is the largest community token on Cardano, holding the highest market capitalization, over 42,000 wallets, and more than 2 billion ADA in all-time trading volume.
- finding: Claim (economic, supported_in_proposal, high materiality): Over the past two years, the Snek Foundation has already invested over $4 million, entirely self funded, to secure major exchange listings.
- finding: Claim (economic, supported_in_proposal, low materiality): We’ve delivered the first and second ever Tier 1 listings for any Cardano native token, with Kraken and Crypto.com setting historic precedents for the ecosystem.
- finding: Claim (economic, proposer_asserted, low materiality): This proposal aims to address the following challenges: - Lack of exchange presence for Cardano native tokens: Most major centralized exchanges and retail brokers still do not support Cardano Native Tokens (CNTs).
- finding: Claim (economic, supported_in_proposal, low materiality): This severely limits Cardano’s accessibility and competitiveness on a global scale.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 5 ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms." and clears the evidence gates.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of TreasuryWithdrawals.
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
- Treasury analysis: Requested ADA: 5 ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a treasury action: 7 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).
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
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence
- delivery controls, milestones, assurance, or remedy path

## Reproducibility
- input_hash: `84e8355cce68fc62df9488a8b359cbaf20b0fbac03bc51b2a50eba0425e88dce`
- snapshot_bundle_hash: `58502d850be5692bd224861c7fe41565a9a3b184757b13a3a629eb9bf8c01c25`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `15`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

