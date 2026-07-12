"""Canonical governance-action identity — one action, one id, everywhere.

A Cardano governance action reaches this system under TWO spellings, depending on which
upstream source produced the row:

    CIP-129 : "<tx_id_hex>#<index>"      e.g. fbb8d1a4…a7#0
    legacy  : "gov_action1…"  (bech32)   e.g. gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps…

bech32 merely ENCODES (tx_id, index). The two are provably the same action.

Treating them as different actions was not cosmetic — it corrupted decisions:

  * the engine scored EACH spelling separately, so one action got two verdicts;
  * evidence packets (decision_support/*.csv) are keyed by ONE spelling, so the other
    spelling saw no evidence at all and fell to NEEDS_MORE_INFO;
  * on 2026-07-12 this produced, in the same run and the same minute, YES (score +0.2055)
    under tx#idx and NEEDS_MORE_INFO (score -0.16) under bech32, for the same proposal
    ("Eternl: Path to Sustainability - v2");
  * the vote runner resolves on-chain gov-state (which is bech32) against run dirs, so it
    would have read the evidence-less verdict and voted on it.

Canonical form is CIP-129 `<tx_id_hex>#<index>` — it is what the ledger and the vote path
actually use, and it is derivable from bech32 (never the reverse without the ledger).
"""
from __future__ import annotations


def canonical_action_id(action_id: str) -> str:
    """Return the CIP-129 `<tx_id>#<index>` form of a governance action id.

    Non-bech32 input is returned unchanged. If a bech32 id cannot be decoded we return it
    as-is rather than guessing — a wrong canonicalisation would merge two distinct actions,
    which is far worse than failing to merge two spellings of one.
    """
    aid = (action_id or "").strip()
    if not aid.startswith("gov_action"):
        return aid
    try:
        from .adapters.cardano_cli_adapter import decode_gov_action_id
        tx_id, index = decode_gov_action_id(aid)
        return f"{tx_id}#{index}"
    except Exception:
        return aid


def same_action(a: str, b: str) -> bool:
    """True when two ids denote the same governance action, whatever their spelling."""
    return canonical_action_id(a) == canonical_action_id(b)
