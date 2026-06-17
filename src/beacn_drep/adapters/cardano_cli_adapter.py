"""Cardano CLI signing adapter for the BEACN automated DRep.

Replaces the former `sign_vote_stub`. Turns an engine decision (a run directory
under data/output/) into a guarded, signed Conway governance vote transaction.

Security / topology (mirrors ~/.openclaw/workspace/ops/beacn-drep-wallet):
  * Signing keys stay on THIS host (opsbox): ~/.secrets/cardano/beacn-drep-cli/.
  * Chain queries + the unsigned tx build run on the `relay` over SSH (the relay
    holds the node socket). The block producer is never in the voting path.
  * Signing is offline on opsbox. Submission happens on the relay.

Shadow by default. A vote is broadcast ONLY when BOTH the caller passes
`live=True` AND the environment sets BEACN_VOTING_LIVE=1. Every gate below must
pass first; any failure (or any uncertainty) blocks the vote — fail closed.

The 8-point automation gate is defined in
~/.openclaw/workspace/infra/drep-cli-wallet.md and enforced in `_run_gates`.
"""
from __future__ import annotations

import hashlib
import json
import os
import shlex
import subprocess
import tempfile
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# --- config (env-overridable; defaults match the wallet helper) --------------
HOME = Path.home()
WALLET = Path(os.environ.get("BEACN_DREP_WALLET", HOME / ".secrets/cardano/beacn-drep-cli"))
CLI = os.environ.get("CARDANO_CLI", str(HOME / ".local/bin/cardano-cli"))
RELAY = os.environ.get("CARDANO_RELAY", "relay")
RELAY_CLI = os.environ.get("CARDANO_RELAY_CLI", "/home/cardano/.local/bin/cardano-cli")
SOCKET = os.environ.get("CARDANO_NODE_SOCKET", "/opt/cardano/cnode/sockets/node.socket")
NETWORK = ["--mainnet"]

DREP_VKEY = WALLET / "automation-drep.vkey"
DREP_SKEY = WALLET / "automation-drep.skey"
PAY_SKEY = WALLET / "payment.skey"
PAY_ADDR_FILE = WALLET / "payment.addr"
DREP_KEY_HASH = "22914b7a8de488fad11adabf38cfda3738be3f73150a3cc6b4850650"

MAX_FEE_LOVELACE = int(os.environ.get("BEACN_MAX_VOTE_FEE_LOVELACE", "1000000"))   # 1 ADA
MAX_VOTES_PER_RUN = int(os.environ.get("BEACN_MAX_VOTES_PER_RUN", "3"))
VOTABLE = {"YES": "--yes", "NO": "--no", "ABSTAIN": "--abstain"}

_BECH32_CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"


# --- bech32 decode (BIP-173) for gov_action1... -> (tx_id_hex, index) --------
def _bech32_decode(bech: str) -> tuple[str, list[int]]:
    bech = bech.strip()
    if bech.lower() != bech and bech.upper() != bech:
        raise ValueError("invalid mixed-case bech32 string")
    bech = bech.lower()
    pos = bech.rfind("1")
    if pos < 1:
        raise ValueError(f"invalid bech32 string: {bech}")
    hrp, data = bech[:pos], bech[pos + 1:]
    if len(data) < 6:
        raise ValueError(f"invalid bech32 string: {bech}")
    values = [_BECH32_CHARSET.find(c) for c in data]
    if any(v == -1 for v in values):
        raise ValueError(f"invalid bech32 string: {bech}")
    if _bech32_polymod(_bech32_hrp_expand(hrp) + values) != 1:
        raise ValueError(f"invalid bech32 checksum: {bech}")
    return hrp, values[:-6]  # drop the 6-symbol checksum


def _bech32_hrp_expand(hrp: str) -> list[int]:
    return [ord(char) >> 5 for char in hrp] + [0] + [ord(char) & 31 for char in hrp]


def _bech32_polymod(values: list[int]) -> int:
    generators = (0x3B6A57B2, 0x26508E6D, 0x1EA119FA, 0x3D4233DD, 0x2A1462B3)
    checksum = 1
    for value in values:
        top = checksum >> 25
        checksum = ((checksum & 0x1FFFFFF) << 5) ^ value
        for index, generator in enumerate(generators):
            if (top >> index) & 1:
                checksum ^= generator
    return checksum


def _convertbits(data: list[int], frm: int, to: int) -> list[int]:
    acc = bits = 0
    out: list[int] = []
    maxv = (1 << to) - 1
    for value in data:
        acc = (acc << frm) | value
        bits += frm
        while bits >= to:
            bits -= to
            out.append((acc >> bits) & maxv)
    return out


def decode_gov_action_id(action_id: str) -> tuple[str, int]:
    """gov_action1... -> (tx_id hex, governance action index)."""
    hrp, data5 = _bech32_decode(action_id)
    if hrp != "gov_action":
        raise ValueError(f"not a gov_action id (hrp={hrp})")
    raw = bytes(_convertbits(data5, 5, 8))
    # 32-byte tx hash followed by a 1-byte action index (CIP-129).
    if len(raw) != 33:
        raise ValueError(f"decoded gov action id has invalid length: {len(raw)} bytes")
    return raw[:32].hex(), raw[32]


# --- shell helpers -----------------------------------------------------------
def _run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, timeout=120, **kw)


def _opsbox(args: list[str]) -> str:
    p = _run([CLI, *args])
    if p.returncode != 0:
        raise RuntimeError(f"cardano-cli {args[:3]}… failed: {p.stderr.strip()}")
    return p.stdout


def _transaction_hash(tx_file: Path) -> str:
    raw = _opsbox([
        "conway", "transaction", "txid", "--tx-file", str(tx_file),
    ]).strip()
    try:
        decoded = json.loads(raw)
        tx_hash = decoded.get("txhash", "") if isinstance(decoded, dict) else str(decoded)
    except json.JSONDecodeError:
        tx_hash = raw
    if len(tx_hash) != 64 or any(char not in "0123456789abcdef" for char in tx_hash.lower()):
        raise RuntimeError(f"unexpected transaction hash output: {raw}")
    return tx_hash.lower()


def _relay_query(args: list[str]) -> str:
    remote = f"{shlex.quote(RELAY_CLI)} {' '.join(shlex.quote(a) for a in args)} --socket-path {shlex.quote(SOCKET)}"
    p = _run(["ssh", RELAY, remote])
    if p.returncode != 0:
        raise RuntimeError(f"relay query {args[:3]}… failed: {p.stderr.strip()}")
    return p.stdout


def _relay_cleanup(path: str) -> None:
    _run(["ssh", RELAY, f"rm -rf -- {shlex.quote(path)}"])


# --- report model ------------------------------------------------------------
@dataclass
class GateResult:
    blocked: bool = False
    reasons: list[str] = field(default_factory=list)
    checks: dict = field(default_factory=dict)

    def fail(self, name: str, why: str) -> None:
        self.blocked = True
        self.checks[name] = False
        self.reasons.append(f"{name}: {why}")

    def ok(self, name: str) -> None:
        self.checks.setdefault(name, True)


# --- gates -------------------------------------------------------------------
def _verify_replay(run_id: str | None) -> bool:
    """Fail closed: only return True on an explicit success signal from the engine."""
    if not run_id:
        return False
    try:
        from ..engine import verify_replay  # lazy; avoids import cost/cycles
        res = verify_replay(run_id)
    except Exception:
        return False
    if isinstance(res, dict):
        if res.get("match") is True or res.get("ok") is True or res.get("verified") is True:
            return True
        if res.get("mismatch") or res.get("mismatches"):
            return False
        return res.get("status") in ("ok", "match", "verified")
    return False


def _fetch_and_hash(url: str) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            return hashlib.blake2b(r.read(2_000_000), digest_size=32).hexdigest()
    except Exception:
        return None


def _run_gates(decision: dict, run_dir: Path) -> GateResult:
    g = GateResult()
    rec = (decision.get("recommendation") or "").upper()

    # 1. Governance data current + manifest verifies.
    fresh = decision.get("freshness") or {}
    if fresh.get("is_stale", True):
        g.fail("freshness", f"data stale ({fresh.get('reason', 'is_stale')})")
    else:
        g.ok("freshness")
    if not (run_dir / "input_manifest.json").exists():
        g.fail("manifest", "input_manifest.json missing")
    else:
        g.ok("manifest")

    # 2. Recommendation is directional; NEEDS_MORE_INFO must never vote.
    if rec not in VOTABLE:
        g.fail("recommendation", f"{rec or 'EMPTY'} is not votable")
    else:
        g.ok("recommendation")

    # 3. Replay verification.
    run_id = decision.get("run_id") or run_dir.name
    if _verify_replay(run_id):
        g.ok("replay")
    else:
        g.fail("replay", f"replay verification did not pass for {run_id}")

    # 4. Public rationale reachable + hash matches.
    url = decision.get("rationale_anchor_url") or os.environ.get("BEACN_RATIONALE_URL")
    want = decision.get("rationale_anchor_hash")
    if not url or not want:
        g.fail("rationale_anchor", "no published rationale url/hash recorded")
    elif _fetch_and_hash(url) != want:
        g.fail("rationale_anchor", "published rationale unreachable or hash mismatch")
    else:
        g.ok("rationale_anchor")

    # 8a. Per-run vote cap (fee cap checked after build).
    if int(os.environ.get("BEACN_VOTES_THIS_RUN", "0")) >= MAX_VOTES_PER_RUN:
        g.fail("per_run_cap", "per-run vote cap reached")
    else:
        g.ok("per_run_cap")
    return g


def _gate_action_live(tx_id: str, index: int) -> tuple[bool, str]:
    """Gate 7: action still active and this DRep has not already voted on it."""
    try:
        gs = json.loads(_relay_query(["conway", "query", "gov-state", "--mainnet"]))
    except Exception as e:  # noqa: BLE001
        return False, f"gov-state query failed: {e}"
    for p in gs.get("proposals", []):
        aid = p.get("actionId", {})
        if aid.get("txId") == tx_id and int(aid.get("govActionIx", -1)) == index:
            if (p.get("dRepVotes") or {}).get(f"keyHash-{DREP_KEY_HASH}") is not None:
                return False, "this DRep has already voted on the action"
            return True, "active and unvoted"
    return False, "action not present in active gov-state (expired/ratified)"


def _tx_is_vote_only(
    view: dict,
    *,
    fee_addr: str,
    expected_inputs: set[str],
) -> tuple[bool, str]:
    """Gates 5 & 6: only fee inputs, fee-wallet change, and vote procedures."""
    forbidden = ["certificate", "minting", "mint", "script", "withdrawal",
                 "treasury donation", "redeemer"]
    for k, v in view.items():
        kl = k.lower()
        if any(f in kl for f in forbidden) and v not in (None, {}, [], 0, "0"):
            return False, f"transaction carries unexpected '{k}'"

    if set(view.get("inputs") or []) != expected_inputs:
        return False, "transaction inputs differ from the queried fee-wallet UTxOs"

    outputs = view.get("outputs") or []
    if len(outputs) != 1:
        return False, f"expected one fee-wallet change output, found {len(outputs)}"
    output = outputs[0]
    if output.get("address") != fee_addr:
        return False, "transaction output does not return to the fee wallet"
    amount = output.get("amount") or {}
    if set(amount) != {"lovelace"} or int(amount.get("lovelace", 0)) <= 0:
        return False, "fee-wallet change contains unexpected assets or no lovelace"

    voters = view.get("voters") or {}
    expected_voter = f"drep-keyHash-{DREP_KEY_HASH}"
    if set(voters) != {expected_voter}:
        return False, "transaction does not contain exactly this DRep's vote"
    votes = voters[expected_voter]
    if not isinstance(votes, dict) or len(votes) != 1:
        return False, "transaction must contain exactly one governance vote"

    return True, "vote-only"


# --- main entry --------------------------------------------------------------
def prepare_vote(run_dir: str | Path, *, live: bool = False) -> dict:
    """Gate, build, and sign a vote for one engine run. Submit only if live + env."""
    run_dir = Path(run_dir)
    decision = json.loads((run_dir / "rationale.json").read_text())
    rec = (decision.get("recommendation") or "").upper()
    action_id = decision["action_id"]
    report = {"action_id": action_id, "recommendation": rec, "live_requested": live,
              "submitted": False, "signed_tx": None}

    gates = _run_gates(decision, run_dir)
    report["gates"] = gates.checks
    if gates.blocked:
        report.update(status="blocked", reasons=gates.reasons)
        return report

    try:
        tx_id, index = decode_gov_action_id(action_id)
    except Exception as e:  # noqa: BLE001
        report.update(status="blocked", reasons=[f"action id decode failed: {e}"])
        return report
    report.update(tx_id=tx_id, index=index)

    live_ok, why = _gate_action_live(tx_id, index)
    report["gates"]["action_live"] = live_ok
    if not live_ok:
        report.update(status="blocked", reasons=[f"action_live: {why}"])
        return report

    fee_addr = PAY_ADDR_FILE.read_text().strip()
    work = Path(tempfile.mkdtemp(prefix="beacn-vote-"))
    vote_file = work / "vote.action"
    anchor = []
    if decision.get("rationale_anchor_url") and decision.get("rationale_anchor_hash"):
        anchor = ["--anchor-url", decision["rationale_anchor_url"],
                  "--anchor-data-hash", decision["rationale_anchor_hash"]]

    # Vote certificate — offline, only the DRep vkey is needed.
    _opsbox(["conway", "governance", "vote", "create", VOTABLE[rec],
             "--governance-action-tx-id", tx_id,
             "--governance-action-index", str(index),
             "--drep-verification-key-file", str(DREP_VKEY), *anchor,
             "--out-file", str(vote_file)])

    # Build the unsigned tx on the relay (needs the socket; no signing keys leave opsbox).
    try:
        utxo = json.loads(_relay_query(["conway", "query", "utxo", "--mainnet",
                                        "--address", fee_addr, "--output-json"]))
    except Exception as e:  # noqa: BLE001
        report.update(status="error", reasons=[f"utxo query failed: {e}"])
        return report
    if not utxo:
        report.update(status="blocked", reasons=["fee wallet has no UTxO"])
        return report
    tx_ins: list[str] = []
    for u in utxo:
        tx_ins += ["--tx-in", u]

    rcli = shlex.quote(RELAY_CLI)
    sock = shlex.quote(SOCKET)
    rwork = f"/tmp/beacn-vote-{os.getpid()}"
    try:
        subprocess.run(["ssh", RELAY, f"mkdir -m 700 {rwork}"], check=True, timeout=60)
        subprocess.run(["scp", "-q", str(vote_file), f"{RELAY}:{rwork}/vote.action"],
                       check=True, timeout=60)
        build = (f"{rcli} conway transaction build --mainnet --socket-path {sock} "
                 + " ".join(shlex.quote(x) for x in tx_ins)
                 + f" --change-address {shlex.quote(fee_addr)} "
                 f"--vote-file {rwork}/vote.action --witness-override 2 "
                 f"--out-file {rwork}/tx.raw")
        b = _run(["ssh", RELAY, build])
        if b.returncode != 0:
            report.update(status="error", reasons=[f"tx build failed: {b.stderr.strip()}"])
            return report
        subprocess.run(["scp", "-q", f"{RELAY}:{rwork}/tx.raw", str(work / "tx.raw")],
                       check=True, timeout=60)
    finally:
        _relay_cleanup(rwork)

    # Gates 5 & 6: inspect the built body before signing.
    view = json.loads(_opsbox(["debug", "transaction", "view",
                               "--tx-body-file", str(work / "tx.raw"),
                               "--output-json"]))
    raw_fee = view.get("fee", 0)
    fee = int(str(raw_fee).split()[0]) if raw_fee else 0
    report["fee_lovelace"] = fee
    if fee > MAX_FEE_LOVELACE:
        report.update(status="blocked", reasons=[f"fee {fee} exceeds cap {MAX_FEE_LOVELACE}"])
        return report
    vote_only, why = _tx_is_vote_only(
        view,
        fee_addr=fee_addr,
        expected_inputs=set(utxo),
    )
    report["gates"]["vote_only_tx"] = vote_only
    if not vote_only:
        report.update(status="blocked", reasons=[f"tx contents: {why}"])
        return report

    # Sign offline on opsbox with both keys.
    signed = work / "tx.signed"
    _opsbox(["conway", "transaction", "sign", "--mainnet",
             "--tx-body-file", str(work / "tx.raw"),
             "--signing-key-file", str(PAY_SKEY),
             "--signing-key-file", str(DREP_SKEY),
             "--out-file", str(signed)])
    report["signed_tx"] = str(signed)
    report["transaction_hash"] = _transaction_hash(signed)

    # Submit only with explicit live intent AND environment opt-in.
    env_live = os.environ.get("BEACN_VOTING_LIVE") == "1"
    if not (live and env_live):
        report.update(status="shadow_signed",
                      note="SHADOW: signed but not submitted (need live=True and BEACN_VOTING_LIVE=1)")
        (run_dir / "shadow_report.json").write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
        return report

    if decision.get("operator_review_required"):
        approval = os.environ.get("BEACN_OPERATOR_APPROVED_ACTION_ID", "")
        if approval not in (action_id, "1"):
            report.update(
                status="blocked",
                reasons=[
                    "operator_review_required: set BEACN_OPERATOR_APPROVED_ACTION_ID "
                    "to this action_id after reviewing the rationale"
                ],
            )
            return report

    try:
        subprocess.run(["ssh", RELAY, f"mkdir -m 700 {rwork}"], check=True, timeout=60)
        subprocess.run(["scp", "-q", str(signed), f"{RELAY}:{rwork}/tx.signed"],
                       check=True, timeout=60)
        s = _run(["ssh", RELAY, f"{rcli} conway transaction submit --mainnet "
                  f"--socket-path {sock} --tx-file {rwork}/tx.signed"])
        if s.returncode != 0:
            report.update(status="error", reasons=[f"submit failed: {s.stderr.strip()}"])
            return report
    finally:
        _relay_cleanup(rwork)
    report.update(
        status="submitted",
        submitted=True,
        submitted_at=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    )
    (run_dir / "vote_receipt.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    return report


# --- deprecated shim ---------------------------------------------------------
def sign_vote_stub(action_id: str, vote: str) -> dict:
    """Deprecated. Kept so old imports don't break; routes nothing on-chain."""
    return {"action_id": action_id, "vote": vote, "signed": False,
            "mode": "stub", "note": "use prepare_vote(run_dir); this stub is retained for compatibility"}
