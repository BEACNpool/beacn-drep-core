from __future__ import annotations

import subprocess
from pathlib import Path

from ..config import CORE_REPO


def _run(cmd: list[str], cwd: Path) -> str:
    return subprocess.check_output(cmd, cwd=str(cwd), text=True).strip()


def publish_to_github(path: str, message: str | None = None) -> str:
    """Commit + push changes under `path` to the current branch.

    Returns a concise status string for CLI output.
    """
    repo = CORE_REPO
    rel = path or "data/output"

    _run(["git", "add", rel], repo)
    status = _run(["git", "status", "--porcelain"], repo)
    if not status:
        return f"no_changes:{rel}"

    branch = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"], repo)
    msg = message or f"publish artifacts: {rel}"
    _run(["git", "commit", "-m", msg], repo)
    _run(["git", "push", "origin", branch], repo)
    head = _run(["git", "rev-parse", "--short", "HEAD"], repo)
    return f"published:{branch}:{head}"
