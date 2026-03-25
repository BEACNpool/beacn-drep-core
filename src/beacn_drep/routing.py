from typing import List, Dict


def select_resources(registry_rows: List[Dict[str, str]], action_type: str) -> List[Dict[str, str]]:
    return [r for r in registry_rows if r["status"] == "approved" and (r["action_type"] in ("all", action_type))]
