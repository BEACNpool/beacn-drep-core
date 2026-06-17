# BEACN DRep — Decision Methodology & Transparency Notes

BEACN is an autonomous Cardano DRep designed for **open-source transparency**: every vote
is produced from public, declared inputs, the reasoning is published in full, and the
binding decision is deterministic and replayable. This document explains exactly how a
vote is made, what is machine-derived vs. model-assisted vs. network-derived, and where the
current limitations are. Nothing here is hidden from delegators.

## The binding contract
The **directional vote, score, and gates are pure deterministic Python** (`src/beacn_drep/engine.py`).
They are the binding record and are byte-for-byte replayable (`cli verify-replay`). A language
model assists with two clearly-labelled, **non-authoritative** layers only: reading the proposal
to extract claims, and writing the plain-language explanation. The model can never set, change,
or veto a vote.

## The pipeline (per proposal)
1. **Intake / claim extraction** *(model-assisted, advisory)* — read the proposal's cached
   anchor document and extract structured intake facts + claim rows, each tagged by how the
   document supports it (`supported_in_proposal` / `independently_verifiable` / `proposer_asserted`
   / `unsupported`) and materiality. Output: `claims.json`. Never feeds a gate.
2. **Evidence check** *(deterministic)* — baseline integrity (anchor pinned, metadata, amount),
   freshness, and the decision-support evidence (`beacn-drep-resources/.../decision_support/*.csv`).
3. **Analysis** *(deterministic)* — treasury sustainability (rolling-window regime) and risk review.
4. **Score + gates** *(deterministic, authoritative)* — weighted score from
   `beacn-drep-soul/scoring_weights.json`, with hard gates (stale data → ABSTAIN; treasury
   without a completed deep-research dossier → NEEDS_MORE_INFO; etc.). Produces the vote.
5. **Rationale** *(deterministic)* — facts/inferences/uncertainty, per-proposal counterarguments
   (best YES / NO / hold case derived from the actual claims and failed gates), `assessment.json`.
6. **Human message** *(model-assisted)* — plain-English explanation of the *already-decided*
   verdict. Output: `rationale_message.md`. It explains; it cannot change the vote.

Each run also emits `input_manifest.json` with a `model_layer` attestation (model id, anchor
sha256, prompt/output hashes, and the provenance `source` of each model layer).

## Provenance of the model layer (`source`)
- `model` — produced by a live Claude API call (`ANTHROPIC_API_KEY` set, `anthropic` SDK installed).
- `precomputed` — supplied from a cache (`BEACN_DREP_LLM_CACHE`) produced by a reasoning pass and
  stored in-repo for audit (`data/output/llm_cache_active.json`, built by
  `scripts/build_active_llm_cache.py`). Used when a live key is not available; identical schema.
- `deterministic-template` — no model available; a plain templated summary from the structured record.

## Data freshness
Governance data is exported to `beacn-drep-resources` from a SQLite store
(`skills/cardano-gov/data/proposals.db`) that is refreshed ~4-hourly from Koios. (db-sync
PostgreSQL is the intended primary but is currently unused; the SQLite exporter
`python3 -m beacn_drep.exporters.export_proposals_to_resources` is the live path.) The engine
**forces ABSTAIN on any snapshot older than 6 hours** (`BEACN_MAX_STALE_SECONDS`) so it never
votes on a stale view. A genuine refresh re-runs the exporter; the freshness gate is never
bypassed by editing timestamps.

## Decision-support evidence (honesty rules)
The per-proposal evidence CSVs (financial / risk / dossier / readiness) are populated from the
actual proposals (`scripts/build_active_decision_support.py`). Rules we hold:
- `independent_assurance_present` is `yes` only when a genuine third-party audit/assurance exists
  (for the current active set: none — so all `no`).
- **No treasury action is marked dossier-complete** until BEACN has done full independent diligence.
  As a result treasury actions correctly resolve to **NEEDS_MORE_INFO**, and each names the
  specific outstanding items rather than rubber-stamping a directional vote.

## Action-type policy
Different governance action types do not mean the same thing when evidence is thin.

- **Treasury withdrawals:** strictest path. Without a completed independent dossier, BEACN returns
  `NEEDS_MORE_INFO`; missing controls, milestones, budget clarity, or sustainability evidence block
  directional votes.
- **Hard-fork initiations:** high-impact protocol changes, but the generic treasury-style risk
  checklist is not allowed to convert thin fields into automatic opposition. If the action has a
  pinned anchor, valid baseline metadata, no flags, and no explicit blocker, the engine may recommend
  `YES` while keeping missing risk detail in the uncertainty record.
- **Operator review:** high-impact hard-fork `YES` recommendations set
  `operator_review_required=true`. Shadow signing still works, but live submission requires
  `BEACN_OPERATOR_APPROVED_ACTION_ID=<action_id>` in addition to the normal live-voting switch.
- **Ratification support:** exported DRep/SPO percentages are treated as ratification-support context,
  not a clean ledger of explicit YES-vs-NO sentiment. Low YES support early in a vote is never treated
  as active opposition by itself.

## Doctrine (versioned, auditable)
Values and weights live in `beacn-drep-soul/` (README charter, `values_hierarchy.md`,
`scoring_weights.json`), are versioned, and every decision cites the exact doctrine commit and a
hash of the weights file. Weight changes require a `CHANGELOG.md` entry (change-control policy).

**v1.1.0 (2026-06-15):** `drep_margin_cap` reduced 0.45 → 0.10. At 0.45 the network DRep vote
distribution could single-handedly drive a directional vote (the non-treasury threshold is ±0.12),
which contradicted README §14 ("do not optimize for popularity, social pressure, or delegation
size") and the values hierarchy (social consensus momentum ranks last). The network distribution
may now only **inform** a vote, never **determine** it. Effect: BEACN no longer votes against a
sensible action merely because the crowd does — it abstains when its own evidence is thin.

## Known limitations & disclosures
- BEACN is an autonomous **advisory** DRep; treat published rationales as transparent reasoning,
  not financial advice. (Registration/voting is a separate, human-gated step.)
- Treasury actions hold at NEEDS_MORE_INFO pending BEACN's own deep-research dossiers; the
  rationale states exactly what is outstanding.
- Non-treasury votes still use the network distribution as a *minor* signal (cap 0.10).
- The model layer is provider-agnostic in spirit but implemented against the Anthropic SDK
  (`claude-opus-4-8`); without a key it degrades to precomputed/deterministic outputs.

## Reproduce / audit
```bash
# fresh export from the live source (never fakes freshness)
PYTHONPATH=src python3 -m beacn_drep.exporters.export_proposals_to_resources
# rebuild auditable provenance inputs
python3 scripts/build_active_llm_cache.py
python3 scripts/build_active_decision_support.py
# run + verify the deterministic record is byte-reproducible
BEACN_DREP_LLM_CACHE=$PWD/data/output/llm_cache_active.json \
  PYTHONPATH=src python3 -m beacn_drep.cli run-all --status active
PYTHONPATH=src python3 -m beacn_drep.cli verify-replay --run-id <run_id>
```
For a live model run, install `anthropic`, set `ANTHROPIC_API_KEY`, and omit `BEACN_DREP_LLM_CACHE`.
