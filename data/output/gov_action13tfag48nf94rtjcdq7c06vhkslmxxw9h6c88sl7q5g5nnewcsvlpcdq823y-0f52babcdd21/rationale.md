# Rationale: gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpcdq823y
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.1833` (raw `-0.1833` + doctrine-LLM nudge `+0.02`) | Confidence: `0.8658` | Readiness: `0.85`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a treasury action: 7 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Withdraw ₳3,126,000 for Ecosystem Exchange Listing and Market Making service. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw ₳3,126,000 for Ecosystem Exchange Listing and Market Making service. It asks the treasury for 3.13M ADA. The strongest grounded claim is: This treasury withdrawal funds Ecosystem Exchange Listing and Market Making service pool which will provide MMAAS (Market Making as a Service): Proposal Overview This proposal aims to address two core issues within the Cardano ecosystem: - Problem 1: No Car.

Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 570
- finding: Expires after epoch: 577
- finding: Treasury request: 3.13M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw ₳3,126,000 for Ecosystem Exchange Listing and Market Making service...
- finding: Recipient: 
- finding: Stated amount: 3.13M ADA
- finding: Deliverables: This treasury withdrawal funds Ecosystem Exchange Listing and Market Making service pool which will provide MMAAS (Market Making as a Service): Proposal Overview This proposal aims to address two core issues within the Cardano ecosystem: - Problem 1: No Car..., Problem 2: No Cardano Native Token (CNT) is listed on top-tier exchanges such as Binance, Bybit, Okex, Kraken and Coinbase., Objective We, at Flowdesk, are committed to solving these problems., Our goal is to act as a trustworthy partner in assisting Cardano Web 3.0 projects by providing essential services such as Market Making as-a-Service (MMAAS) and helping with exchange listings.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, independently_verifiable, high materiality): This treasury withdrawal funds Ecosystem Exchange Listing and Market Making service pool which will provide MMAAS (Market Making as a Service): Proposal Overview This proposal aims to address two core issues within the Cardano ecosystem: - Problem 1: No Car...
- finding: Claim (economic, independently_verifiable, low materiality): Problem 2: No Cardano Native Token (CNT) is listed on top-tier exchanges such as Binance, Bybit, Okex, Kraken and Coinbase.
- finding: Claim (economic, independently_verifiable, low materiality): Objective We, at Flowdesk, are committed to solving these problems.
- finding: Claim (economic, independently_verifiable, low materiality): Our goal is to act as a trustworthy partner in assisting Cardano Web 3.0 projects by providing essential services such as Market Making as-a-Service (MMAAS) and helping with exchange listings.
- finding: Claim (economic, independently_verifiable, low materiality): This proposal aims to solve the following problem: - Problem 1: No Cardano project currently has a top-tier market maker, with the exception of Snek and Iagon.
- finding: Claim (economic, independently_verifiable, low materiality): Flowdesk are committed to solving these problems.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 3.13M ADA
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
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal funds Ecosystem Exchange Listing and Market Making service pool which will provide MMAAS (Market Making as a Service): Proposal Overview This proposal aims to address two core issues within the Cardano ecosystem: - Problem 1: No Car..." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 3.13M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal funds Ecosystem Exchange Listing and Market Making service pool which will provide MMAAS (Market Making as a Service): Proposal Overview This proposal aims to address two core issues within the Cardano ecosystem: - Problem 1: No Car..." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): Doctrine-aware offline lean for a treasury action: 7 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `0f52babcdd21193ae16edff463a0e054dcfc721de7bd160fa2552482b0ca255f`
- snapshot_bundle_hash: `cfc51ec8061bf71ff5de81fafabab11a8338e44cb86e3e9486ad4ceec597f92f`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `19`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5356, "NO": 0.4144, "YES": 0.0499}`

