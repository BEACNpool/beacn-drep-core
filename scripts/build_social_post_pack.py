#!/usr/bin/env python3
"""Build a human-review social post pack for a BEACN DRep governance action."""
from __future__ import annotations

import argparse
import csv
import json
import shutil
import textwrap
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
RESOURCES = WORKSPACE / "beacn-drep-resources"
WEB = WORKSPACE / "beacn-drep-web"
DESKTOP = Path.home() / "Desktop"
SCREENSHOT_DIR = ROOT / "data/output/screenshots"

ACTIVE_CSV = RESOURCES / "data/input/governance/governance_actions_active.csv"
ALL_CSV = RESOURCES / "data/input/governance/governance_actions_all.csv"
STATUS_JSON = WEB / "status.json"
PUBLIC_ACTIONS = ROOT / "data/output/public/actions"
PUBLIC_BASE = "https://beacnpool.github.io/beacn-drep-web"

FONT_REGULAR = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
FONT_BOLD = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
FONT_MONO = Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")

PALETTE = {
    "YES": {"accent": (40, 190, 125), "soft": (18, 78, 55), "label": "YES"},
    "NO": {"accent": (235, 82, 92), "soft": (92, 28, 37), "label": "NO"},
    "ABSTAIN": {"accent": (148, 163, 184), "soft": (48, 58, 75), "label": "ABSTAIN"},
    "NEEDS_MORE_INFO": {"accent": (245, 178, 64), "soft": (96, 63, 18), "label": "NEEDS MORE INFO"},
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def active_rows() -> list[dict]:
    with ACTIVE_CSV.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def all_rows() -> list[dict]:
    with ALL_CSV.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def choose_action(action_id: str | None) -> dict:
    rows = active_rows()
    if action_id:
        match = next((row for row in [*rows, *all_rows()] if row["action_id"] == action_id), None)
        if not match:
            raise SystemExit(f"action_id not found in governance snapshot: {action_id}")
        return match
    return max(rows, key=lambda row: (row.get("first_seen") or "", int(row.get("proposed_epoch") or 0)))


def status_by_cip129(open_only: bool = False) -> dict[str, dict]:
    status = load_json(STATUS_JSON)
    return {
        row["cip129_action_id"]: row
        for row in status.get("actions", [])
        if row.get("cip129_action_id")
        and (not open_only or str(row.get("status", "")).lower() == "open")
    }


def open_actions() -> list[dict]:
    open_status = status_by_cip129(open_only=True)
    rows_by_id = {row["action_id"]: row for row in all_rows()}
    rows_by_id.update({row["action_id"]: row for row in active_rows()})
    open_ids = set(open_status)
    synthetic = []
    for action_id in sorted(open_ids - set(rows_by_id)):
        status = open_status[action_id]
        synthetic.append({
            "action_id": action_id,
            "metadata_title": status.get("title", ""),
            "action_type": status.get("type", ""),
            "proposed_epoch": status.get("proposed_in_epoch") or 0,
            "expiration_epoch": status.get("expires_after_epoch") or 0,
            "first_seen": "",
        })
    return sorted(
        [rows_by_id[action_id] for action_id in open_ids if action_id in rows_by_id] + synthetic,
        key=lambda row: (int(row.get("proposed_epoch") or 0), row.get("first_seen") or "", row.get("action_id") or ""),
        reverse=True,
    )


def verdict_key(value: object) -> str:
    text = str(value or "").upper().replace("VOTE", "").replace(" ", "_")
    if "NEEDS" in text:
        return "NEEDS_MORE_INFO"
    if "ABSTAIN" in text:
        return "ABSTAIN"
    if "YES" in text:
        return "YES"
    if "NO" in text:
        return "NO"
    return "NEEDS_MORE_INFO"


def short_id(action_id: str) -> str:
    return f"{action_id[:18]}...{action_id[-8:]}"


def first_reason(summary: str) -> str:
    text = summary.strip()
    if text.startswith("Vote:") and "." in text:
        text = text.split(".", 1)[1].strip()
    text = text.split("Why:", 1)[0].strip() or text.split("Why:", 1)[-1].strip()
    text = text.split("Additional context:", 1)[0].strip()
    if "." in text:
        text = text.split(".", 1)[0].strip() + "."
    return text or "The deterministic rationale names the governing evidence and risk checks."


def hours(seconds: object) -> str:
    try:
        return f"{float(seconds) / 3600:.1f}h"
    except (TypeError, ValueError):
        return "unknown"


def quality(detail: dict, status_row: dict) -> list[dict]:
    evidence = detail.get("proposal_evidence") or {}
    freshness = detail.get("freshness") or {}
    proof = detail.get("proof_of_vote") or {}
    decision = detail.get("decision") or {}
    evidence_status = str(evidence.get("fetch_status") or "")
    evidence_ok = bool(evidence.get("available")) and evidence_status.startswith("ok")
    on_chain_vote = decision.get("submitted") or bool(status_row.get("our_vote"))
    on_chain_detail = (
        decision.get("transaction_hash")
        or status_row.get("transaction_hash")
        or status_row.get("our_vote")
        or status_row.get("action_id")
        or ""
    )

    return [
        {
            "label": "Evidence",
            "value": "Anchor fetched" if evidence_ok else "Incomplete",
            "detail": f"{evidence.get('content_bytes') or '0'} bytes admitted",
        },
        {
            "label": "Freshness",
            "value": "Fresh" if not freshness.get("is_stale") else "Stale",
            "detail": f"snapshot age {hours(freshness.get('snapshot_age_seconds'))}",
        },
        {
            "label": "Replay",
            "value": "Hash-bound" if proof.get("input_hash") and proof.get("snapshot_bundle_hash") else "Missing hash",
            "detail": (proof.get("input_hash") or "")[:12] or "no input hash",
        },
        {
            "label": "On-chain",
            "value": "Submitted" if on_chain_vote else "Pending",
            "detail": str(on_chain_detail)[:12],
        },
    ]


def build_pack(action_row: dict) -> dict:
    action_id = action_row["action_id"]
    detail = load_json(PUBLIC_ACTIONS / f"{action_id}.json")
    status_row = status_by_cip129().get(action_id, {})
    decision = detail.get("decision") or {}
    proof = detail.get("proof_of_vote") or {}
    rationale = detail.get("rationale") or {}
    verdict = verdict_key(decision.get("vote") or proof.get("vote") or status_row.get("recommendation"))
    title = detail.get("title") or action_row.get("metadata_title") or "Governance action"
    reason = first_reason(rationale.get("summary") or "")
    receipt_url = proof.get("rationale_anchor_url") or f"{PUBLIC_BASE}/#/action/{action_id}"
    action_url = f"{PUBLIC_BASE}/#/action/{action_id}"

    post_text = (
        f"BEACN DRep verdict: {PALETTE[verdict]['label']}\n\n"
        f"{title}\n\n"
        f"{reason}\n\n"
        f"Receipts: {action_url}"
    )
    alt_text = (
        f"BEACN DRep governance card for {title}. Verdict: {PALETTE[verdict]['label']}. "
        f"Primary reason: {reason}"
    )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "action_id": action_id,
        "title": title,
        "type": detail.get("type") or action_row.get("action_type"),
        "verdict": verdict,
        "verdict_label": PALETTE[verdict]["label"],
        "reason": reason,
        "confidence": proof.get("confidence"),
        "score": proof.get("score"),
        "proposed_epoch": int(action_row.get("proposed_epoch") or status_row.get("proposed_in_epoch") or 0),
        "expires_epoch": int(action_row.get("expiration_epoch") or status_row.get("expires_after_epoch") or 0),
        "receipt_url": receipt_url,
        "action_url": action_url,
        "quality": quality(detail, status_row),
        "post_text": post_text,
        "alt_text": alt_text,
        "image_prompt": {
            "use_case": "productivity-visual",
            "asset_type": "mobile social post image, 4:5 portrait",
            "brand": "BEACN DRep",
            "watermark": "BEACN DRep",
            "verbatim_text": {
                "verdict": PALETTE[verdict]["label"],
                "title": title,
                "reason": reason,
                "action_id": short_id(action_id),
            },
            "constraints": [
                "Use only supplied structured facts.",
                "Do not invent claims, vote status, amounts, or citations.",
                "Keep text readable on a phone.",
            ],
        },
    }


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def wrap(draw: ImageDraw.ImageDraw, text: str, font_obj: ImageFont.ImageFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textbbox((0, 0), trial, font=font_obj)[2] <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            if draw.textbbox((0, 0), word, font=font_obj)[2] <= width:
                line = word
            else:
                chunks = textwrap.wrap(word, width=18)
                lines.extend(chunks[:-1])
                line = chunks[-1]
    if line:
        lines.append(line)
    return lines


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font_obj: ImageFont.ImageFont,
                 fill: tuple[int, int, int], max_width: int, line_gap: int = 8, max_lines: int | None = None) -> int:
    x, y = xy
    lines = wrap(draw, text, font_obj, max_width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(".") + "..."
    line_height = draw.textbbox((0, 0), "Ag", font=font_obj)[3] + line_gap
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += line_height
    return y


def render_image(pack: dict, out: Path) -> None:
    w, h = 1600, 2000
    image = Image.new("RGB", (w, h), (8, 13, 24))
    draw = ImageDraw.Draw(image)
    verdict = pack["verdict"]
    accent = PALETTE[verdict]["accent"]
    soft = PALETTE[verdict]["soft"]

    for y in range(h):
        blend = y / h
        color = (
            int(8 + soft[0] * 0.28 * blend),
            int(13 + soft[1] * 0.24 * blend),
            int(24 + soft[2] * 0.18 * blend),
        )
        draw.line([(0, y), (w, y)], fill=color)

    draw.rounded_rectangle((78, 78, w - 78, h - 78), radius=44, fill=(13, 22, 37), outline=(50, 65, 88), width=3)
    draw.rounded_rectangle((112, 112, 505, 190), radius=34, fill=(20, 31, 51), outline=(70, 88, 116), width=2)
    draw.ellipse((140, 132, 178, 170), fill=accent)
    draw.text((198, 130), "BEACN DRep", font=font(FONT_BOLD, 40), fill=(245, 248, 252))
    draw.text((198, 170), "verifiable governance", font=font(FONT_REGULAR, 24), fill=(160, 176, 198))

    draw.rounded_rectangle((112, 250, 590, 390), radius=42, fill=accent)
    draw.text((152, 278), "VERDICT", font=font(FONT_BOLD, 28), fill=(8, 13, 24))
    draw.text((152, 310), pack["verdict_label"], font=font(FONT_BOLD, 62), fill=(8, 13, 24))

    y = 465
    draw.text((112, y), pack["type"], font=font(FONT_BOLD, 34), fill=accent)
    y += 62
    y = draw_wrapped(draw, (112, y), pack["title"], font(FONT_BOLD, 70), (248, 250, 252), 1370, line_gap=16, max_lines=4)
    y += 42
    draw.text((112, y), "Primary rationale", font=font(FONT_BOLD, 34), fill=(203, 213, 225))
    y += 52
    y = draw_wrapped(draw, (112, y), pack["reason"], font(FONT_REGULAR, 42), (226, 232, 240), 1370, line_gap=14, max_lines=5)

    y = max(y + 54, 1160)
    draw.text((112, y), "Quality gates", font=font(FONT_BOLD, 36), fill=(248, 250, 252))
    y += 58
    card_w = 660
    card_h = 178
    gap = 36
    for i, item in enumerate(pack["quality"]):
        x = 112 + (i % 2) * (card_w + gap)
        cy = y + (i // 2) * (card_h + gap)
        draw.rounded_rectangle((x, cy, x + card_w, cy + card_h), radius=28, fill=(20, 31, 51), outline=(51, 65, 85), width=2)
        draw.text((x + 34, cy + 28), item["label"], font=font(FONT_BOLD, 28), fill=(148, 163, 184))
        draw.text((x + 34, cy + 70), item["value"], font=font(FONT_BOLD, 40), fill=(248, 250, 252))
        draw.text((x + 34, cy + 124), item["detail"], font=font(FONT_MONO, 24), fill=(180, 190, 205))

    footer_y = h - 270
    draw.line((112, footer_y, w - 112, footer_y), fill=(51, 65, 85), width=2)
    draw.text((112, footer_y + 44), f"Action: {short_id(pack['action_id'])}", font=font(FONT_MONO, 27), fill=(190, 205, 224))
    draw.text((112, footer_y + 88), f"Epoch {pack['proposed_epoch']} -> expires {pack['expires_epoch']}", font=font(FONT_REGULAR, 30), fill=(190, 205, 224))
    if pack.get("confidence") is not None:
        draw.text((112, footer_y + 132), f"Confidence {pack['confidence']:.0%} | score {pack.get('score')}", font=font(FONT_REGULAR, 30), fill=(190, 205, 224))
    draw.text((w - 445, h - 150), "BEACN DRep", font=font(FONT_BOLD, 48), fill=(55, 70, 92))
    draw.text((w - 375, h - 100), "public rationale first", font=font(FONT_REGULAR, 24), fill=(55, 70, 92))
    image.save(out, "PNG")


def image_name(pack: dict) -> str:
    return f"{pack['action_id']}-beacn-drep-post.png"


def write_pack(pack: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    image_path = out_dir / image_name(pack)
    (out_dir / "manifest.json").write_text(json.dumps(pack, indent=2) + "\n", encoding="utf-8")
    (out_dir / "post.txt").write_text(pack["post_text"] + "\n", encoding="utf-8")
    (out_dir / "alt_text.txt").write_text(pack["alt_text"] + "\n", encoding="utf-8")
    (out_dir / "image_prompt.json").write_text(json.dumps(pack["image_prompt"], indent=2) + "\n", encoding="utf-8")
    legacy = out_dir / "beacn-drep-post.png"
    if legacy.exists() and legacy != image_path:
        legacy.unlink()
    render_image(pack, image_path)


def default_pack_dir(pack: dict, out_root: Path) -> Path:
    return out_root / pack["action_id"]


def copy_to_desktop(source_dir: Path, pack: dict) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_id = pack["action_id"].replace("gov_action", "ga")[:22]
    dest = DESKTOP / f"BEACN-DRep-post-pack-{stamp}-{safe_id}"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(source_dir, dest)
    return dest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action-id", help="CIP-129 governance action id; defaults to newest first_seen active action")
    parser.add_argument("--all-open", action="store_true", help="Build a post pack for every open action in status.json")
    parser.add_argument("--out-root", type=Path, default=SCREENSHOT_DIR, help="Root directory for repo post packs")
    parser.add_argument("--out-dir", type=Path, help="Exact output directory for a single action")
    parser.add_argument("--desktop-copy", action="store_true", help="Copy generated single-action pack to a timestamped Desktop folder")
    args = parser.parse_args()

    if args.all_open and args.action_id:
        raise SystemExit("--all-open and --action-id are mutually exclusive")
    if args.all_open and args.out_dir:
        raise SystemExit("--out-dir is only valid for a single action; use --out-root with --all-open")

    actions = open_actions() if args.all_open else [choose_action(args.action_id)]
    results = []
    for action in actions:
        pack = build_pack(action)
        out_dir = args.out_dir or default_pack_dir(pack, args.out_root)
        write_pack(pack, out_dir)
        result = {
            "action_id": pack["action_id"],
            "title": pack["title"],
            "verdict": pack["verdict_label"],
            "image": str(out_dir / image_name(pack)),
            "post_text": str(out_dir / "post.txt"),
            "manifest": str(out_dir / "manifest.json"),
        }
        if args.desktop_copy:
            result["desktop_copy"] = str(copy_to_desktop(out_dir, pack))
        results.append(result)
    print(json.dumps({"count": len(results), "items": results}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
