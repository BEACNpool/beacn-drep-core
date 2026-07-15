"""Guards on the vote-time truth ledger.

The invariant: what the engine believed when a vote was CAST is frozen at submission and
never rewritten by later runs. The exporter's proof_of_vote for a cast vote must come from
the frozen snapshot; the re-derived today-values live in a separate `current` block.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from beacn_drep.vote_snapshots import (  # noqa: E402
    append_snapshot, latest_snapshot, load_snapshots, record_submission,
)
from beacn_drep.exporters.export_public_artifacts import _proof_of_vote_block  # noqa: E402

AID = "ab" * 32 + "#0"


class AppendOnlyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "vote_time_snapshots.json"

    def tearDown(self):
        self.tmp.cleanup()

    def test_append_is_idempotent_on_tx_hash(self):
        entry = {"tx_hash": "t1", "vote": "YES", "frozen": True}
        self.assertTrue(append_snapshot(AID, entry, self.path))
        self.assertFalse(append_snapshot(AID, dict(entry), self.path))
        self.assertEqual(len(load_snapshots(self.path)[AID]), 1)

    def test_revision_appends_and_never_edits_the_first_entry(self):
        first = {"tx_hash": "t1", "vote": "NO", "score": -0.3, "frozen": True,
                 "submitted_at": "2026-07-01T00:00:00+00:00"}
        append_snapshot(AID, first, self.path)
        append_snapshot(AID, {"tx_hash": "t2", "vote": "YES", "score": 0.2, "frozen": True,
                              "submitted_at": "2026-07-10T00:00:00+00:00"}, self.path)
        entries = load_snapshots(self.path)[AID]
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0], first, "an existing frozen entry must never change")
        latest = latest_snapshot(load_snapshots(self.path), AID)
        self.assertEqual(latest["tx_hash"], "t2", "latest entry is the vote standing on-chain")

    def test_record_submission_freezes_the_run_rationale(self):
        run_dir = Path(self.tmp.name) / f"{AID}-abcdef123456"
        run_dir.mkdir()
        (run_dir / "rationale.json").write_text(json.dumps({
            "action_id": AID, "recommendation": "YES", "score": 0.21, "confidence": 0.74,
            "input_hash": "ih", "snapshot_bundle_hash": "sbh", "soul_commit": "sc",
            "resource_registry_commit": "rc", "rationale_anchor_hash": "rah",
        }))
        receipt = {"transaction_hash": "t3", "recommendation": "YES",
                   "submitted_at": "2026-07-15T00:00:00+00:00"}
        entry = record_submission(run_dir, receipt, self.path)
        self.assertEqual(entry["vote"], "YES")
        self.assertEqual(entry["resources_commit"], "rc")
        self.assertEqual(entry["run_id"], run_dir.name)
        self.assertTrue(entry["frozen"])
        self.assertEqual(load_snapshots(self.path)[AID][0], entry)


class ProofOfVoteBlockTests(unittest.TestCase):
    CURRENT = {"vote": "ABSTAIN", "score": 0.0, "confidence": 0.1,
               "input_hash": "new-ih", "snapshot_bundle_hash": "new-sbh"}

    def test_cast_vote_publishes_the_frozen_snapshot_not_the_rederivation(self):
        frozen = {"tx_hash": "t1", "vote": "YES", "recommendation": "YES", "score": 0.21,
                  "confidence": 0.74, "input_hash": "old-ih", "snapshot_bundle_hash": "old-sbh",
                  "rationale_anchor_hash": "aa" * 32, "frozen": True}
        block = _proof_of_vote_block(frozen, self.CURRENT, {"anchor_hash": "aa" * 32, "vote": "Yes"})
        self.assertTrue(block["frozen"])
        self.assertEqual(block["vote"], "YES")
        self.assertEqual(block["score"], 0.21)
        self.assertEqual(block["input_hash"], "old-ih",
                         "a later engine run must never overwrite vote-time hashes")
        self.assertEqual(block["onchain_vote"], "Yes")

    def test_uncast_action_falls_back_to_current_and_says_so(self):
        block = _proof_of_vote_block(None, self.CURRENT, None)
        self.assertFalse(block["frozen"])
        self.assertEqual(block["input_hash"], "new-ih")


if __name__ == "__main__":
    unittest.main()
