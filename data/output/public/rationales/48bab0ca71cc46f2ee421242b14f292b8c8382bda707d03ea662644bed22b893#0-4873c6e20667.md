# Rationale: 48bab0ca71cc46f2ee421242b14f292b8c8382bda707d03ea662644bed22b893#0
Recommendation: **ABSTAIN**
Score: `0.01` (base + flags + capped margin; LLM lean `+0.03` recorded, not added) | Confidence: `0.5925` | Readiness: `0.6`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 4 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Name the Protocol Version 12 hard fork “von Bergen“. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Name the Protocol Version 12 hard fork “von Bergen“. The strongest grounded claim is: This info action proposes naming the Protocol Version 12 hard fork “von Bergen” as a salute and recognition to Fabian von Bergen, also known as Zyroxa.

Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 644
- finding: Expires after epoch: 651
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Name the Protocol Version 12 hard fork “von Bergen“
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: This info action proposes naming the Protocol Version 12 hard fork “von Bergen” as a salute and recognition to Fabian von Bergen, also known as Zyroxa., Fabian has been a Cardano community member since the ITN, an always critical, honest and sound voice in Cardano's past who introduced and guided many through the Cardano ecosystem, a well known person on the Cardano Forum, also SPO of the Tempus Stake Pool..., Many of us remember Fabian as a humble and modest, yet hard working person., Kind and smart and always honest and authentic to his perspectives and opinions, a person who said what he thought and stood his ground.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): This info action proposes naming the Protocol Version 12 hard fork “von Bergen” as a salute and recognition to Fabian von Bergen, also known as Zyroxa.
- finding: Claim (adoption, supported_in_proposal, medium materiality): Fabian has been a Cardano community member since the ITN, an always critical, honest and sound voice in Cardano's past who introduced and guided many through the Cardano ecosystem, a well known person on the Cardano Forum, also SPO of the Tempus Stake Pool...
- finding: Claim (other, proposer_asserted, low materiality): Many of us remember Fabian as a humble and modest, yet hard working person.
- finding: Claim (other, supported_in_proposal, low materiality): Kind and smart and always honest and authentic to his perspectives and opinions, a person who said what he thought and stood his ground.
- finding: Claim (other, proposer_asserted, low materiality): Fabian passed away in January 2026.
- finding: Claim (adoption, supported_in_proposal, high materiality): Naming the hard fork “von Bergen” would preserve Fabian’s name in Cardano’s history and recognize his lasting contribution to the community.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

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
- finding: Strongest YES: the proposal substantiates "This info action proposes naming the Protocol Version 12 hard fork “von Bergen” as a salute and recognition to Fabian von Bergen, also known as Zyroxa." and clears the evidence gates.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of InfoAction.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Flag score present (3), reducing confidence.
- Intake: Action type: InfoAction
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This info action proposes naming the Protocol Version 12 hard fork “von Bergen” as a salute and recognition to Fabian von Bergen, also known as Zyroxa." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was +0.030 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a info action: 4 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `4873c6e20667c6aa0f50094b9b565004ed468e427fa195649964fde39f151050`
- snapshot_bundle_hash: `50c7d51b47ea5f030b06d946ea89663abcb3231d9e416afdfd17b70737b457ce`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `863e0cdf62372fc7df18a82f5f52ef17ffb55832`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4681, "NO": 0.2559, "YES": 0.2759}`

