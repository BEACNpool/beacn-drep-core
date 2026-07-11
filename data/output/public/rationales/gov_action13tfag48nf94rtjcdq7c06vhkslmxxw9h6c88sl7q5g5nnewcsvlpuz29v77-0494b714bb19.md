# Rationale: gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpuz29v77
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.1833` (raw `-0.1833` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7658` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Withdraw ₳3,000,000 for High-yield RWA Asset for Cardano: Tokenized Real Estate. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw ₳3,000,000 for High-yield RWA Asset for Cardano: Tokenized Real Estate. It asks the treasury for 3.00M ADA. The strongest grounded claim is: This treasury withdrawal funds High-yield RWA Asset for Cardano : Tokenized Real Estate which will provide the following services: Haus is building an open-source Tokenized Home Equity Liquidity Protocol to unlock the $16 trillion in illiquid home equity si.

Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
- finding: Proposed epoch: 570
- finding: Expires after epoch: 577
- finding: Treasury request: 3.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw ₳3,000,000 for High-yield RWA Asset for Cardano: Tokenized Real Estate
- finding: Recipient: 
- finding: Stated amount: 3.00M ADA
- finding: Deliverables: This treasury withdrawal funds High-yield RWA Asset for Cardano : Tokenized Real Estate which will provide the following services: Haus is building an open-source Tokenized Home Equity Liquidity Protocol to unlock the $16 trillion in illiquid home equity si..., By leveraging blockchain technology, our platform enables homeowners to sell fractional ownership of their home equity, instantly accessing liquidity while allowing investors to gain exposure to real estate appreciation., We have already prototyped and deployed this model on a private Ethereum blockchain, securing $20 million in Total Value Locked (TVL)., With this proposal, we aim to transition HausCoin and the liquidity protocol to Cardano, leveraging its secure, scalable, and cost-effective infrastructure to power a decentralized marketplace for home equity trading.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, independently_verifiable, high materiality): This treasury withdrawal funds High-yield RWA Asset for Cardano : Tokenized Real Estate which will provide the following services: Haus is building an open-source Tokenized Home Equity Liquidity Protocol to unlock the $16 trillion in illiquid home equity si...
- finding: Claim (economic, independently_verifiable, low materiality): By leveraging blockchain technology, our platform enables homeowners to sell fractional ownership of their home equity, instantly accessing liquidity while allowing investors to gain exposure to real estate appreciation.
- finding: Claim (economic, independently_verifiable, low materiality): We have already prototyped and deployed this model on a private Ethereum blockchain, securing $20 million in Total Value Locked (TVL).
- finding: Claim (technical, independently_verifiable, low materiality): With this proposal, we aim to transition HausCoin and the liquidity protocol to Cardano, leveraging its secure, scalable, and cost-effective infrastructure to power a decentralized marketplace for home equity trading.
- finding: Claim (economic, independently_verifiable, low materiality): This proposal aims to solve the following problem: Many homeowners are asset-rich but cash-poor, lacking access to liquidity tied up in their homes.
- finding: Claim (economic, independently_verifiable, low materiality): At the same time, investors struggle to find stable, appreciating, asset-backed alternatives to traditional stablecoins or volatile crypto assets.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 3.00M ADA
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
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal funds High-yield RWA Asset for Cardano : Tokenized Real Estate which will provide the following services: Haus is building an open-source Tokenized Home Equity Liquidity Protocol to unlock the $16 trillion in illiquid home equity si..." and clears the evidence gates.
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
- Treasury analysis: Requested ADA: 3.00M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal funds High-yield RWA Asset for Cardano : Tokenized Real Estate which will provide the following services: Haus is building an open-source Tokenized Home Equity Liquidity Protocol to unlock the $16 trillion in illiquid home equity si..." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).
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
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence
- delivery controls, milestones, assurance, or remedy path

## Reproducibility
- input_hash: `0494b714bb19516f3d81e842a159717dd71bf77bc460d1e74b927bb36fc20757`
- snapshot_bundle_hash: `b71761a1624f4daa127d2f93ef7f49d66ee07235075cebd3a8666cdb780190ae`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `18`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5114, "NO": 0.4276, "YES": 0.061}`

