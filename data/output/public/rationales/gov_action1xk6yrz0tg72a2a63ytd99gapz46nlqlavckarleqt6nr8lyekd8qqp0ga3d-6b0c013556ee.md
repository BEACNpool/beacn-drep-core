# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7808` | Readiness: `0.9`
> Reasoning layer (precomputed): The claims show meaningful public-benefit growth potential and some treasury-protection mechanisms, but the highest-impact adoption, repayment, Phase 1, and commercial anchor claims are mostly proposer-asserted rather than evidenced in the document. Under BEACN doctrine, treasury stewardship and evidence quality outweigh plausible ecosystem growth, so the bounded nudge should be cautious rather than supportive.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal asks for 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, with Intersect as budget administrator and milestone-based disbursement through the Sundae Labs TRSC/PSSC framework. It proposes an 8-month delivery plan covering an on-chain secondary marketplace, resale royalty enforcement, anti-scalping controls, custodial onboarding with self-custody export, organizer tools, an independent smart-contract audit, launch activity, metrics, and governance reporting.

Several claims were clear and supported in the proposal, including the requested amount, the approximate dollar value at $0.22 per ADA, the 3% Intersect administration fee, the 8-month milestone structure, and the stated revenue-share repayment mechanism. But some of the highest-impact claims were still mostly proposer-asserted rather than independently evidenced in the supplied review, including that Phase 1 is already live on Cardano mainnet, the scale of Sellout’s existing platform, the Yellowstone Club anchor deployment, and the projected 12-month adoption outcomes.

The review gates show why BEACN held instead of voting yes or no. The action had a pinned, replayable anchor document, the counterargument pass was completed, and execution risk was rated medium. But treasury withdrawals require elevated scrutiny, the claims-and-evidence status was thin, independent assurance and a dependency map were missing from the risk review, and the Net Change Limit verification remained required. A directional vote would be unblocked by public, replayable evidence verifying the applicable Net Change Limit and stronger independent evidence for the material live-platform, adoption, and commercial-anchor claims.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 4.97M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency.
- finding: Recipient: Intersect as budget administrator, with funds held and disbursed through the Sundae Labs TRSC/PSSC framework; delivery by Anvil Development Agency and Sellout.
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, reselling, and settling ticket transactions on-chain, Smart-contract royalty enforcement for resale royalty splits, Per-event anti-scalping controls including price ceilings, transfer limits, identity-binding, and time-based restrictions, Custodial wallet onboarding inside Sellout's existing user flow with self-custody export referenced in milestones, Organizer tools for resale configuration, ticket lifecycle data, royalty distributions, and ticket verification, Independent third-party smart-contract security audit with published remediation, Public launch campaign, trade-show activations, educational materials, metrics dashboard, and governance reporting
- finding: Deadline/expiry: 8 months across five milestone-gated milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested withdrawal is 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over an 8-month milestone-gated delivery period.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism in which 25% of all fees are paid until full reimbursement and 5% thereafter, with quarterly public reporting.
- finding: Claim (adoption, proposer_asserted, high materiality): Phase 2 targets 12-month outcomes of 200+ on-chain events, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move more than $6,000,000 through Cardano in Year 1, based on $5.88 million of 2025 historical activity.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout is described as an existing ticketing platform with 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: Phase 2 targets 12-month outcomes of 200+ on-chain events, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move more than $6,000,000 through Cardano in Year 1, based on $5.88 million of 2025 historical activity.
- missing: Independent evidence for: Sellout is described as an existing ticketing platform with 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 4969231
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The requested withdrawal is 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over an 8-month milestone-gated delivery period." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 4969231
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The requested withdrawal is 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over an 8-month milestone-gated delivery period." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show meaningful public-benefit growth potential and some treasury-protection mechanisms, but the highest-impact adoption, repayment, Phase 1, and commercial anchor claims are mostly proposer-asserted rather than evidenced in the document. Under BEACN doctrine, treasury stewardship and evidence quality outweigh plausible ecosystem growth, so the bounded nudge should be cautious rather than supportive.
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
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- Claims and evidence missing: Independent evidence for: Phase 2 targets 12-month outcomes of 200+ on-chain events, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `6b0c013556ee0118b6f09090423749cc3bbc725dbafffb72a07335fcbe2412ad`
- snapshot_bundle_hash: `8b2bb91660030bb23ce0f619a44c37a18fb6b02e55cbd38480846e5fc2eb33df`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

