# Rationale: gov_action18a9sytyez02jl8ee4ryz5xu7heg587m5tu6nr7fkd3ex30umnnjqq27e7ey
Recommendation: **NO**
Score: `-0.5333` (raw `-0.5033` + doctrine-LLM nudge `-0.03`) | Confidence: `1.0` | Readiness: `0.6`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit ecosystem growth through established events and some checkable references, but the ask is large, includes discretionary and forward-looking items such as a 2027 deposit, depends on asserted sponsorship value and VIP-sale returns, and the deterministic assessment identifies missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under the doctrine, weak or incomplete evidence for a treasury withdrawal should receive a cautious negative nudge rather than spending momentum.

## Plain-language explanation (precomputed)
BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is procedural rather than a verdict on the proposal's merits. BEACN's on-chain governance data snapshot is currently about eight hours old, which is beyond the six-hour freshness limit its policy requires before it will cast a directional vote. When data is this stale BEACN holds rather than risk voting on an out-of-date picture of the proposal, the treasury, and the wider vote distribution. The request is 2.75 million ADA to make Cardano the title sponsor of Rare Evo 2026 and the associated Dev Gov Day in Las Vegas, with a pledge to return 20% of VIP ticket sales to the treasury. Event sponsorship is inherently harder to evaluate than infrastructure: the central claims about reach, governance participation and developer engagement are marketing projections that are asserted rather than measured, and the value Cardano receives depends on outcomes that are difficult to verify after the fact. The 20% VIP rebate is a sensible alignment mechanism but its dollar value is uncertain. For a spend of this size BEACN would want concrete, independently verifiable success metrics and a milestone or rebate structure before committing treasury funds, alongside its standard deep-research dossier. With the data snapshot stale, the correct action today is to hold rather than vote directionally.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 633
- finding: Expires after epoch: 640
- finding: Treasury request: 2.75M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to make Cardano the title sponsor of Rare Evo 2026 main stage and global livestream and to support Rare Dev Gov Day 2026.
- finding: Recipient: Rare Network
- finding: Stated amount: 2750000
- finding: Deliverables: Cardano title sponsorship for Rare Evo 2026 main stage and livestream, Cardano title sponsorship for Cardano Dev Gov Day 2026, free General Admission access for the Cardano community, complimentary booth space for selected Cardano ecosystem projects, travel and lodging support for 20 Cardano ecosystem contributors or volunteers, five Cardano-focused main stage panel opportunities, Cardano workshops and governance sessions, livestream ads and global livestream participation, tier-1 media coverage using 2-3 selected vendors, return of 20% of all VIP ticket sales to the Cardano Treasury
- finding: Deadline/expiry: Rare Dev Gov Day on July 28, 2026 and Rare Evo 2026 on July 28-31, 2026 in Las Vegas
- finding: Claim (economic, supported_in_proposal, high materiality): Rare Network requests ₳2,750,000, described as $660,000 at a $0.24 ADA valuation, to fund two Cardano sponsorship packages for Rare Evo 2026 and Cardano Dev Gov Day 2026.
- finding: Claim (economic, supported_in_proposal, high materiality): The cost breakdown allocates ₳1,166,666.67 to Cardano Dev Gov Day 2026 sponsorship, ₳833,333.33 to Rare Evo 2026 title sponsorship, and ₳750,000 to Intersect, audit, fees, tax withholdings, and a Dev Gov Day 2027 venue deposit.
- finding: Claim (economic, proposer_asserted, high materiality): Rare Network says it will return 20% of all VIP ticket sales to the Cardano Treasury, with the current retail value of a VIP ticket stated as $900.
- finding: Claim (adoption, proposer_asserted, high materiality): Rare Evo 2026 will occur regardless of treasury funding, but the proposal says treasury funding would expand Cardano presence, accessibility, participation, and strategic industry outreach through existing event infrastructure.
- finding: Claim (adoption, supported_in_proposal, high materiality): The proposal states Rare Evo 2025 had 2,500 attendees, 80 exhibitor booths, 85 speakers, 100+ ecosystem partners, 20K+ livestream views, 4M social impressions, 40+ Cardano projects represented, and 50+ enterprise participants.
- finding: Claim (adoption, supported_in_proposal, medium materiality): The proposal states Cardano Dev Gov Day 2025 was free and publicly accessible, welcomed approximately 500 attendees, and included a Charles Hoskinson keynote, governance discussions, technical education, workshops, and community activities.
- missing: Independent evidence for: Rare Network says it will return 20% of all VIP ticket sales to the Cardano Treasury, with the current retail value of a VIP ticket stated as $900.
- missing: Independent evidence for: Rare Evo 2026 will occur regardless of treasury funding, but the proposal says treasury funding would expand Cardano presence, accessibility, participation, and strategic industry outreach through existing event infrastructure.
- missing: Independent evidence for: Rare Network claims it has been active in the Cardano ecosystem since 2020 and has produced more than 60 blockchain industry side events and activations across conferences including ETHDenver, TOKEN2049, Consensus, Duke Blockchain Conference, Paris Blockchain Week, and Cardano Summit.
- missing: Independent evidence for: The sponsorship allocation may change if a different sponsor purchases the mainstage or livestream package before passage, in which case Cardano would receive a sponsorship of equal impact or dollar value such as Enterprise & Policy Social, Registration, Closeout Party, or College Row.
- missing: budget analysis
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 2750000
- finding: Budget granularity: unknown
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: not confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unknown (stale snapshot)
- finding: Financial confidence: 0.35
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: low
- finding: Technical risk: low
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: not confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Rare Network requests ₳2,750,000, described as $660,000 at a $0.24 ADA valuation, to fund two Cardano sponsorship packages for Rare Evo 2026 and Cardano Dev Gov Day 2026." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Rare Network says it will return 20% of all VIP ticket sales to the Cardano Treasury, with the current retail value of a VIP ticket stated as $900." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing budget analysis
- missing: missing feasibility assessment
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
- Treasury analysis: Requested ADA: 2750000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Rare Network requests ₳2,750,000, described as $660,000 at a $0.24 ADA valuation, to fund two Cardano sponsorship packages for Rare Evo 2026 and Cardano Dev Gov Day 2026." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show plausible public-benefit ecosystem growth through established events and some checkable references, but the ask is large, includes discretionary and forward-looking items such as a 2027 deposit, depends on asserted sponsorship value and VIP-sale returns, and the deterministic assessment identifies missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under the doctrine, weak or incomplete evidence for a treasury withdrawal should receive a cautious negative nudge rather than spending momentum.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Rare Network says it will return 20% of all VIP ticket sales to the Cardano Treasury, with the current retail value of a VIP ticket stated as $900.
- Claims and evidence missing: Independent evidence for: Rare Evo 2026 will occur regardless of treasury funding, but the proposal says treasury funding would expand Cardano presence, accessibility, participation, and strategic industry outreach through existing event infrastructure.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `d09d76c7bd08d8d2b6687b1d3d45211608de508a368353742f812b49c05b898d`
- snapshot_bundle_hash: `a99919dd3f5956b1b1e8b8f3c8499c1aca024a4bd8709c3e626890640059e359`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `660`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1518, "NO": 0.8093, "YES": 0.0389}`

