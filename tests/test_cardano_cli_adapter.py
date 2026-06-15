import unittest

from beacn_drep.adapters.cardano_cli_adapter import (
    DREP_KEY_HASH,
    decode_gov_action_id,
    _tx_is_vote_only,
)


FEE_ADDR = "addr1vfee"
TX_IN = "ab" * 32 + "#0"


def valid_view() -> dict:
    return {
        "auxiliary scripts": None,
        "certificates": None,
        "inputs": [TX_IN],
        "mint": None,
        "outputs": [
            {
                "address": FEE_ADDR,
                "amount": {"lovelace": 9_800_000},
            }
        ],
        "redeemers": [],
        "scripts": [],
        "treasuryDonation": 0,
        "voters": {
            f"drep-keyHash-{DREP_KEY_HASH}": {
                f'{"cd" * 32}#0': {
                    "anchor": None,
                    "decision": "Abstain",
                }
            }
        },
        "withdrawals": None,
    }


class VoteOnlyTransactionTests(unittest.TestCase):
    def assert_valid(self, view: dict) -> None:
        ok, reason = _tx_is_vote_only(
            view,
            fee_addr=FEE_ADDR,
            expected_inputs={TX_IN},
        )
        self.assertTrue(ok, reason)

    def test_accepts_expected_vote_only_shape(self) -> None:
        self.assert_valid(valid_view())

    def test_rejects_external_output(self) -> None:
        view = valid_view()
        view["outputs"][0]["address"] = "addr1vattacker"
        ok, _ = _tx_is_vote_only(view, fee_addr=FEE_ADDR, expected_inputs={TX_IN})
        self.assertFalse(ok)

    def test_rejects_unexpected_input(self) -> None:
        view = valid_view()
        view["inputs"].append("ef" * 32 + "#1")
        ok, _ = _tx_is_vote_only(view, fee_addr=FEE_ADDR, expected_inputs={TX_IN})
        self.assertFalse(ok)

    def test_rejects_non_ada_change(self) -> None:
        view = valid_view()
        view["outputs"][0]["amount"]["policy.asset"] = 1
        ok, _ = _tx_is_vote_only(view, fee_addr=FEE_ADDR, expected_inputs={TX_IN})
        self.assertFalse(ok)

    def test_rejects_multiple_votes(self) -> None:
        view = valid_view()
        votes = view["voters"][f"drep-keyHash-{DREP_KEY_HASH}"]
        votes[f'{"ef" * 32}#0'] = {"anchor": None, "decision": "VoteNo"}
        ok, _ = _tx_is_vote_only(view, fee_addr=FEE_ADDR, expected_inputs={TX_IN})
        self.assertFalse(ok)


class GovernanceActionIdTests(unittest.TestCase):
    ACTION_ID = (
        "gov_action1fl6r784t2ffw7q96du2znhprw90r3xvrfugvqelgqewgxex42kdqq9tgrd5"
    )

    def test_accepts_valid_action_id(self) -> None:
        tx_id, index = decode_gov_action_id(self.ACTION_ID)
        self.assertEqual(len(tx_id), 64)
        self.assertGreaterEqual(index, 0)

    def test_rejects_invalid_checksum(self) -> None:
        replacement = "q" if self.ACTION_ID[-1] != "q" else "p"
        with self.assertRaisesRegex(ValueError, "checksum"):
            decode_gov_action_id(self.ACTION_ID[:-1] + replacement)


if __name__ == "__main__":
    unittest.main()
