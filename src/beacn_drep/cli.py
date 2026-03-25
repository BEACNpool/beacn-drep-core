import argparse
from .engine import run_once
from .adapters.github_adapter import publish_stub


def cmd_check_new_actions() -> None:
    print("check-new-actions:stub")


def cmd_run_once(action_id: str | None) -> None:
    result = run_once(action_id=action_id)
    print(result["run_id"])


def cmd_publish(path: str | None) -> None:
    target = path or "data/output"
    print(publish_stub(target))


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("check-new-actions")
    run = sub.add_parser("run-once")
    run.add_argument("--action-id", default=None)

    pub = sub.add_parser("publish")
    pub.add_argument("--path", default=None)

    args = p.parse_args()
    if args.cmd == "check-new-actions":
        cmd_check_new_actions()
    elif args.cmd == "run-once":
        cmd_run_once(args.action_id)
    elif args.cmd == "publish":
        cmd_publish(args.path)


if __name__ == "__main__":
    main()
