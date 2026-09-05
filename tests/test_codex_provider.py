"""Provider replacement must retain offline and independent-verifier gates."""
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verify_dossiers as verifier
from beacn_drep import llm


def test_live_engine_calls_remain_explicitly_opt_in():
    with patch.dict(os.environ, {}, clear=True):
        assert llm._client() is None
    with patch.dict(os.environ, {"BEACN_DREP_LIVE_LLM": "1", "BEACN_DREP_DISABLE_LLM": "1"}, clear=True):
        assert llm._client() is None


def test_verifier_has_its_own_model_setting():
    payload = {"fact_verdicts": [], "material_discrepancies": [], "summary": "fixture"}
    with patch.dict(os.environ, {"BEACN_CODEX_MODEL": "gpt-5.5"}, clear=True), \
         patch.object(verifier, "codex_text", return_value=json.dumps(payload)) as call:
        assert verifier.call_codex("fixture") == payload
        assert call.call_args.kwargs["model"] == "gpt-5.6-sol"


def test_same_model_drafter_cannot_self_approve():
    with TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True), \
         patch.object(verifier, "DOSSIER_DIR", Path(tmp)), \
         patch.object(verifier, "codex_text") as model:
        (Path(tmp) / "fixture.md").write_text("# Fixture")
        (Path(tmp) / "fixture.receipt.json").write_text(json.dumps({
            "backend": "codex", "model": "gpt-5.6-sol"}))
        row = {s + "_complete": "yes" for s in verifier.SECTIONS}
        outcome, record = verifier.verify_one({"action_id": "fixture"}, row, "codex", True)
        assert outcome == "gate_failed"
        assert record["gates"]["different_model_from_drafter"] is False
        model.assert_not_called()
