# The 8 Signing Gates

Public specification of the fail-closed gate stack enforced by the signing
adapter, `src/beacn_drep/adapters/cardano_cli_adapter.py`
(`prepare_vote(run_dir, live=False)`). Every on-chain vote this DRep casts
passes through this one function; there is no other signing path. Anyone can
audit the safety property directly against the code — this document quotes
the enforced conditions from it.

**The safety property:** a vote is broadcast only if the governance data is
fresh and manifest-verified, the recommendation is votable, the decision
replays deterministically, the published rationale is independently fetched
and hash-verified at vote time, the action is still live and not
same-direction re-voted, the built transaction does nothing but vote, and the
fee and per-run volume sit under fixed caps. Any failure — or any
*uncertainty* — blocks the vote. Blocked is the default state; every gate
must affirmatively pass.

Shadow by default: even with all gates green, submission additionally
requires **both** the caller passing `live=True` **and** the environment
setting `BEACN_VOTING_LIVE=1`. Otherwise the adapter stops at
`shadow_signed` — built and signed, never broadcast.

## Gate order in the code

`_run_gates` checks gates 1–4 and the per-run half of gate 8 before anything
is built. Then: strict action-id decode → gate 7 (live gov-state) → the
unsigned tx is built on the relay → fee cap (gate 8) and gates 5–6 are
checked against the *built transaction body* → sign → live check → submit.

## Gate 1 — Governance data current + manifest verifies

From `_run_gates`:

```python
fresh = decision.get("freshness") or {}
if fresh.get("is_stale", True):
    g.fail("freshness", f"data stale ({fresh.get('reason', 'is_stale')})")
...
if not (run_dir / "input_manifest.json").exists():
    g.fail("manifest", "input_manifest.json missing")
```

Note the fail-closed default: a rationale with *no* freshness block at all is
treated as stale (`fresh.get("is_stale", True)`). The run directory must
carry its `input_manifest.json` (the hash manifest of every admitted input).

## Gate 2 — Recommendation is directional; NEEDS_MORE_INFO never votes

```python
VOTABLE = {"YES": "--yes", "NO": "--no", "ABSTAIN": "--abstain"}
...
if rec not in VOTABLE:
    g.fail("recommendation", f"{rec or 'EMPTY'} is not votable")
```

Only `YES`, `NO`, `ABSTAIN` can reach the chain. `NEEDS_MORE_INFO`, an empty
recommendation, or any other verdict string is blocked here.

## Gate 3 — Replay verification

```python
def _verify_replay(run_id: str | None) -> bool:
    """Fail closed: only return True on an explicit success signal from the engine."""
```

The engine's `verify_replay(run_id)` re-derives the decision from the
manifested inputs. The gate passes only on an explicit success signal
(`match`/`ok`/`verified` `is True`, or `status` in `("ok", "match",
"verified")`); a missing run id, an exception, a mismatch report, or any
ambiguous result returns `False` and blocks.

## Gate 4 — Public rationale reachable + hash matches

```python
url = decision.get("rationale_anchor_url") or os.environ.get("BEACN_RATIONALE_URL")
want = decision.get("rationale_anchor_hash")
if not url or not want:
    g.fail("rationale_anchor", "no published rationale url/hash recorded")
elif _fetch_and_hash(url) != want:
    g.fail("rationale_anchor", "published rationale unreachable or hash mismatch")
```

At vote time the adapter independently fetches the published rationale over
HTTPS (20s timeout, first 2,000,000 bytes) and computes
`hashlib.blake2b(..., digest_size=32)`; the digest must equal the recorded
anchor hash exactly. Any fetch failure hashes to `None` and blocks. This is
what makes "the public can read why, byte-for-byte, before the vote exists"
an enforced property rather than a policy: an unpublished, moved, or edited
rationale physically cannot vote. The same URL + hash are attached to the
vote itself as its on-chain anchor (`--anchor-url` / `--anchor-data-hash`).

## Gate 5 — Only known fee-wallet inputs and fee-wallet change

Enforced by `_tx_is_vote_only` against the *built* transaction body
(`cardano-cli debug transaction view` of `tx.raw`), not against intent:

```python
if set(view.get("inputs") or []) != expected_inputs:
    return False, "transaction inputs differ from the queried fee-wallet UTxOs"

outputs = view.get("outputs") or []
if len(outputs) != 1:
    return False, f"expected one fee-wallet change output, found {len(outputs)}"
...
if output.get("address") != fee_addr:
    return False, "transaction output does not return to the fee wallet"
amount = output.get("amount") or {}
if set(amount) != {"lovelace"} or int(amount.get("lovelace", 0)) <= 0:
    return False, "fee-wallet change contains unexpected assets or no lovelace"
```

Inputs must be exactly the queried spendable UTxOs of the fee wallet, and
those are pre-filtered to **pure-lovelace UTxOs only** (`_spendable_utxos`):

```python
if set(value) == {"lovelace"} and int(value.get("lovelace") or 0) > 0:
```

An asset-bearing UTxO (a LEDGER_SCROLLS token is parked at the fee address)
is never selected, never spent. There must be exactly one output, returning
lovelace-only change to the fee wallet.

## Gate 6 — Nothing but the vote

The same body inspection rejects any transaction field beyond fee inputs,
change, and this DRep's single vote:

```python
forbidden = ["certificate", "minting", "mint", "script", "withdrawal",
             "treasury donation", "redeemer"]
for k, v in view.items():
    kl = k.lower()
    if any(f in kl for f in forbidden) and v not in (None, {}, [], 0, "0"):
        return False, f"transaction carries unexpected '{k}'"
```

And the vote itself is pinned to identity, target, and direction:

```python
expected_voter = f"drep-keyHash-{DREP_KEY_HASH}"
if set(voters) != {expected_voter}:
    return False, "transaction does not contain exactly this DRep's vote"
...
if not isinstance(votes, dict) or len(votes) != 1:
    return False, "transaction must contain exactly one governance vote"
```

plus, with `expected_action`/`expected_decision` always supplied by
`prepare_vote`: the one vote must target exactly `"<tx_id>#<index>"` of the
decided action and carry exactly the decided direction
(`VoteYes`/`VoteNo`/`Abstain`). A build that voted on the wrong action or
flipped direction is blocked *after* build, *before* signing.

## Gate 7 — Action still active; no same-direction re-vote

`_gate_action_live` queries live `gov-state` on the relay:

```python
if existing_rec == rec:
    return False, f"this DRep has already voted {existing_rec} on the action"
if existing_rec is not None:
    return True, f"active with agentic vote revision from {existing_rec} to {rec}"
return True, "active and unvoted"
```

and if the action is absent from the active proposal set:

```python
return False, "action not present in active gov-state (expired/ratified)"
```

Expired or already-ratified actions cannot be voted. A vote that already
exists on-chain with the same direction is never re-cast; a *changed*
recommendation is allowed through as an explicit revision (the reason string
records the transition).

## Gate 8 — Fee cap and per-run vote cap

```python
MAX_FEE_LOVELACE = int(os.environ.get("BEACN_MAX_VOTE_FEE_LOVELACE", "1000000"))   # 1 ADA
MAX_VOTES_PER_RUN = int(os.environ.get("BEACN_MAX_VOTES_PER_RUN", "3"))
...
if int(os.environ.get("BEACN_VOTES_THIS_RUN", "0")) >= MAX_VOTES_PER_RUN:
    g.fail("per_run_cap", "per-run vote cap reached")
...
if fee > MAX_FEE_LOVELACE:
    report.update(status="blocked", reasons=[f"fee {fee} exceeds cap {MAX_FEE_LOVELACE}"])
```

The fee is read from the built body and capped at 1 ADA by default. The vote
runner (`scripts/run_live_votes.py`) sets `BEACN_VOTES_THIS_RUN` to the count
of votes already submitted in the run, so at most 3 votes (default) can be
cast per daily run regardless of how many actions are approved.

## Supporting strictness (not numbered gates, same fail-closed posture)

- **Action-id parsing never guesses.** `decode_gov_action_id` accepts the two
  real spellings of one identity — CIP-129 `<tx_hex>#<index>` and bech32
  `gov_action1…` — with strict validation (64-hex tx hash, integer index,
  bech32 checksum, exactly 33 decoded bytes); anything malformed raises
  instead of resolving to some other action.
- **UTxO wait vs. empty wallet.** Consecutive votes race the chain: the
  previous vote's change may still be in the mempool. The adapter waits up to
  `BEACN_UTXO_WAIT_SECONDS` (default 240) for a spendable UTxO before
  declaring the wallet genuinely unfunded — bounded, so a truly empty wallet
  still fails loudly.
- **Key topology.** Signing keys never leave the orchestrator host; the relay
  only builds the unsigned body and submits the signed one. The block
  producer is never in the voting path.
- **Audit trail.** Every submission writes `vote_receipt.json` into the run
  directory and appends the vote-time truth (score/confidence/hashes as cast)
  to the append-only snapshot ledger republished in the public artifacts.

## Environment knobs

| Variable | Default | Effect |
|---|---|---|
| `BEACN_VOTING_LIVE` | unset | Must be `1` (with caller `live=True`) for any broadcast; otherwise shadow. |
| `BEACN_MAX_VOTE_FEE_LOVELACE` | `1000000` (1 ADA) | Gate 8 fee cap on the built transaction. |
| `BEACN_MAX_VOTES_PER_RUN` | `3` | Gate 8 per-run submission cap. |
| `BEACN_VOTES_THIS_RUN` | `0` | Set by the runner to votes already cast this run; compared against the cap. |
| `BEACN_UTXO_WAIT_SECONDS` | `240` | Bound on waiting for in-flight change to confirm. |
| `BEACN_RATIONALE_URL` | unset | Fallback anchor URL if the decision recorded none (the hash must still match). |
| `BEACN_DREP_WALLET`, `CARDANO_CLI`, `CARDANO_RELAY`, `CARDANO_RELAY_CLI`, `CARDANO_NODE_SOCKET` | host paths | Deployment topology; change none of the gate semantics. |

Above the adapter, the daily runner adds `BEACN_AUTO_DIRECTIONS` (default
`YES,NO,ABSTAIN`) to narrow which directions may auto-submit, and
`BEACN_AUTOVOTE_DISABLED=1` as the kill switch — see
`docs/BREAK_GLASS_VOTE_RUNBOOK.md`. Honest caveat: the two caps are
env-overridable, so an attacker who controls the process environment could
*loosen* them — but no environment variable exists that disables a gate,
skips the anchor hash verification or replay check, relaxes the vote-only
body inspection, or makes `NEEDS_MORE_INFO` votable. Those properties are
unconditional in the code.
