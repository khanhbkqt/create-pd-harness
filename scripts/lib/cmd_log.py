"""
cmd_log.py — Activity logging cho design pipeline.

Ghi và đọc activity log (JSONL format) để track ai làm gì, khi nào.

Usage:
    python scripts/pdt.py log                              # Xem 20 entries gần nhất
    python scripts/pdt.py log --all                        # Xem toàn bộ
    python scripts/pdt.py log --add "Viết PRD section 5"   # Ghi log entry
    python scripts/pdt.py log --add "msg" --artifact PRD   # Ghi + tag artifact
    python scripts/pdt.py log --filter PRD                 # Filter theo artifact
"""

import json
from datetime import datetime
from pathlib import Path
try:
    import fcntl
except ImportError:
    fcntl = None

from .config import LOG_FILE


def read_log(limit: int | None = None, filter_artifact: str | None = None) -> list[dict]:
    """Đọc activity log từ JSONL file."""
    if not LOG_FILE.exists():
        return []

    entries = []
    for line in LOG_FILE.read_text(encoding="utf-8").strip().split("\n"):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            if filter_artifact and entry.get("artifact", "").lower() != filter_artifact.lower():
                continue
            entries.append(entry)
        except json.JSONDecodeError:
            continue

    if limit is not None:
        entries = entries[-limit:]

    return entries


def write_log_entry(message: str, artifact: str = "", action: str = "manual"):
    """Ghi 1 entry vào activity log."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "action": action,
        "artifact": artifact,
        "message": message,
    }

    # Append to JSONL
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        if fcntl:
            fcntl.flock(f, fcntl.LOCK_EX)
        try:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            f.flush()
        finally:
            if fcntl:
                fcntl.flock(f, fcntl.LOCK_UN)

    return entry


def format_log_display(entries: list[dict]) -> str:
    """Format log entries cho terminal display."""
    if not entries:
        return "  📋 No activity log entries yet.\n  Use `pdt.py log --add \"message\"` to start logging.\n"

    lines = []
    lines.append("")
    lines.append("  📋 ACTIVITY LOG")
    lines.append("  " + "─" * 56)

    current_date = ""
    for entry in entries:
        date = entry.get("date", "unknown")[:10]
        time = entry.get("date", "")[11:] or ""

        # Date header
        if date != current_date:
            current_date = date
            lines.append(f"\n  📅 {date}")

        artifact = entry.get("artifact", "")
        artifact_tag = f" [{artifact}]" if artifact else ""
        action_icon = {
            "created": "🆕",
            "updated": "📝",
            "approved": "✅",
            "reviewed": "🔍",
            "manual": "📌",
        }.get(entry.get("action", ""), "•")

        lines.append(f"    {time} {action_icon}{artifact_tag} {entry.get('message', '')}")

    lines.append("")
    lines.append("  " + "─" * 56)
    lines.append(f"  Total: {len(entries)} entries")
    lines.append("")
    return "\n".join(lines)


def cmd_log(args: list[str]):
    """Entry point cho `pdt log`."""

    # Parse args
    add_msg = None
    artifact = ""
    filter_val = None
    show_all = "--all" in args

    i = 0
    while i < len(args):
        if args[i] == "--add" and i + 1 < len(args):
            add_msg = args[i + 1]
            i += 2
        elif args[i] == "--artifact" and i + 1 < len(args):
            artifact = args[i + 1]
            i += 2
        elif args[i] == "--filter" and i + 1 < len(args):
            filter_val = args[i + 1]
            i += 2
        elif args[i] == "--action" and i + 1 < len(args):
            action = args[i + 1]
            i += 2
        else:
            i += 1

    if add_msg:
        action = "manual"
        # Auto-detect action from message keywords
        msg_lower = add_msg.lower()
        if any(w in msg_lower for w in ["tạo", "created", "new", "viết"]):
            action = "created"
        elif any(w in msg_lower for w in ["sửa", "updated", "edit", "cập nhật"]):
            action = "updated"
        elif any(w in msg_lower for w in ["approve", "approved", "duyệt"]):
            action = "approved"
        elif any(w in msg_lower for w in ["review", "kiểm tra"]):
            action = "reviewed"

        entry = write_log_entry(add_msg, artifact=artifact, action=action)
        print(f"  ✅ Logged: {entry['date']} | {entry['message']}")
        return

    # Display log
    limit = None if show_all else 20
    entries = read_log(limit=limit, filter_artifact=filter_val)
    print(format_log_display(entries))
