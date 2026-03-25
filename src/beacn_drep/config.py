import os
from pathlib import Path

_WS = Path(os.environ.get("BEACN_WORKSPACE", Path.home() / ".openclaw" / "workspace"))

SOUL_REPO = Path(os.environ.get("BEACN_SOUL_REPO", _WS / "beacn-drep-soul")).resolve()
RESOURCES_REPO = Path(os.environ.get("BEACN_RESOURCES_REPO", _WS / "beacn-drep-resources")).resolve()
CORE_REPO = Path(os.environ.get("BEACN_CORE_REPO", _WS / "beacn-drep-core")).resolve()
WEB_REPO = Path(os.environ.get("BEACN_WEB_REPO", _WS / "beacn-drep-web")).resolve()

OUTPUT_DIR = CORE_REPO / "data" / "output"
AUDIT_LOG = CORE_REPO / "logs" / "audit_log.jsonl"

# Freshness: max seconds since last export before engine forces ABSTAIN
MAX_STALE_SECONDS = int(os.environ.get("BEACN_MAX_STALE_SECONDS", "21600"))  # 6 hours

# PostgreSQL db-sync connection
DBSYNC_HOST = os.environ.get("BEACN_DBSYNC_HOST", "")
DBSYNC_PORT = os.environ.get("BEACN_DBSYNC_PORT", "5432")
DBSYNC_DB = os.environ.get("BEACN_DBSYNC_DB", "cexplorer")
DBSYNC_USER = os.environ.get("BEACN_DBSYNC_USER", "postgres")
DBSYNC_PASS = os.environ.get("BEACN_DBSYNC_PASS", "")

# SQLite fallback
SQLITE_DB = Path(os.environ.get(
    "BEACN_SQLITE_DB",
    _WS / "skills" / "cardano-gov" / "data" / "proposals.db"
))
