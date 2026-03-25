import argparse
import csv
import json
from pathlib import Path
from .engine import run_once, run_all, verify_replay
from .adapters.github_adapter import publish_to_github
from .config import RESOURCES_REPO


def _read_action_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open(newline="", encoding="utf-8") as f:
        return {r.get("action_id", "") for r in csv.DictReader(f) if r.get("action_id")}


def cmd_check_new_actions() -> None:
    all_path = RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_all.csv"
    all_ids = _read_action_ids(all_path)

    runs_dir = Path(__file__).resolve().parents[3] / "data" / "output"
    seen_ids: set[str] = set()
    if runs_dir.exists():
        for d in runs_dir.iterdir():
            if not d.is_dir() or d.name == "public":
                continue
            rid = d.name.split("-")[0]
            if rid:
                seen_ids.add(rid)

    new_ids = sorted(all_ids - seen_ids)
    print(json.dumps({
        "actions_all": len(all_ids),
        "actions_seen_in_runs": len(seen_ids),
        "new_or_unprocessed_action_ids": new_ids,
        "count": len(new_ids),
    }, indent=2))


def cmd_run_once(action_id: str | None) -> None:
    result = run_once(action_id=action_id)
    print(result["run_id"])


def cmd_run_all(limit: int | None) -> None:
    result = run_all(limit=limit)
    print(json.dumps(result, indent=2))


def cmd_publish(path: str | None) -> None:
    target = path or "data/output"
    print(publish_to_github(target))


def cmd_verify_replay(run_id: str) -> None:
    print(json.dumps(verify_replay(run_id), indent=2))


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("check-new-actions")
    run = sub.add_parser("run-once")
    run.add_argument("--action-id", default=None)

    run_all_p = sub.add_parser("run-all")
    run_all_p.add_argument("--limit", type=int, default=None)

    pub = sub.add_parser("publish")
    pub.add_argument("--path", default=None)

    vr = sub.add_parser("verify-replay")
    vr.add_argument("--run-id", required=True)

    args = p.parse_args()
    if args.cmd == "check-new-actions":
        cmd_check_new_actions()
    elif args.cmd == "run-once":
        cmd_run_once(args.action_id)
    elif args.cmd == "run-all":
        cmd_run_all(args.limit)
    elif args.cmd == "publish":
        cmd_publish(args.path)
    elif args.cmd == "verify-replay":
        cmd_verify_replay(args.run_id)


if __name__ == "__main__":
    main()
