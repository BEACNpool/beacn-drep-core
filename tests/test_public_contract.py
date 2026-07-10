import unittest
from pathlib import Path


class PublicContractTests(unittest.TestCase):
    def test_ui_prioritizes_current_recommendation(self):
        app = (Path(__file__).resolve().parents[2] / "beacn-drep-web" / "app.assessment.js").read_text()
        self.assertIn("live.recommendation || item.decision || live.our_vote", app)
        self.assertIn("live.recommendation || record.decision || live.our_vote", app)
        self.assertNotIn("onchainVote || decision.vote", app)

    def test_ui_discloses_separate_onchain_vote_and_score_contract(self):
        app = (Path(__file__).resolve().parents[2] / "beacn-drep-web" / "app.assessment.js").read_text()
        self.assertIn("Current recommendation", app)
        self.assertIn("Recorded on-chain vote", app)
        self.assertIn("How this decision was scored", app)
        self.assertIn("model_vote_influence", app)


if __name__ == "__main__":
    unittest.main()
