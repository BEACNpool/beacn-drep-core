from typing import List, Dict


_TYPE_MAP = {
    "treasurywithdrawals": "treasury_withdrawal",
    "treasury_withdrawal": "treasury_withdrawal",
    "parameterchange": "parameter_change",
    "parameter_change": "parameter_change",
    "hardforkinitiation": "hardfork",
    "hardforkinitiaton": "hardfork",
    "hardfork": "hardfork",
    "infoaction": "info_action",
    "newconstitution": "new_constitution",
    "newcommittee": "new_committee",
    "updatecommittee": "new_committee",
    "noconfidence": "new_committee",
}


def _normalize_action_type(action_type: str) -> str:
    key = (action_type or "").lower().replace("-", "").replace(" ", "").replace("__", "_")
    key = key.replace("_", "")
    return _TYPE_MAP.get(key, (action_type or "").lower())


def select_resources(registry_rows: List[Dict[str, str]], action_type: str) -> List[Dict[str, str]]:
    normalized = _normalize_action_type(action_type)
    return [r for r in registry_rows if r["status"] == "approved" and (r["action_type"] in ("all", normalized))]
