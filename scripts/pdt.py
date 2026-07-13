#!/usr/bin/env python3
"""
pdt — Product Design Tool

CLI thống nhất cho toàn bộ design pipeline: tracking, sync, priority, logs, verify, search.

Usage:
    python scripts/pdt.py status              # Dashboard overview
    python scripts/pdt.py status --update     # Cập nhật docs/STATUS.md
    python scripts/pdt.py status --json       # JSON output

    python scripts/pdt.py sync                # Full sync check
    python scripts/pdt.py sync docs/prd/x.md  # Impact analysis cho 1 file

    python scripts/pdt.py log                 # Xem activity log
    python scripts/pdt.py log --add "msg"     # Ghi log entry mới

    python scripts/pdt.py priority            # Việc gì nên làm tiếp?

    python scripts/pdt.py verify              # Pre-review-gate checks
    python scripts/pdt.py verify --check traceability

    python scripts/pdt.py search REQ-001      # Trace requirement xuyên docs
    python scripts/pdt.py search --pattern "authentication"
"""

import sys
import os

# Add scripts dir to path
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS_DIR)

from lib.config import HELP_TEXT
from lib.cmd_status import cmd_status
from lib.cmd_sync import cmd_sync
from lib.cmd_log import cmd_log
from lib.cmd_priority import cmd_priority
from lib.cmd_verify import cmd_verify
from lib.cmd_search import cmd_search


COMMANDS = {
    "status":   cmd_status,
    "sync":     cmd_sync,
    "log":      cmd_log,
    "priority": cmd_priority,
    "verify":   cmd_verify,
    "search":   cmd_search,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print(HELP_TEXT)
        sys.exit(0)

    command = sys.argv[1]
    if command not in COMMANDS:
        print(f"❌ Unknown command: {command}")
        print(f"   Available: {', '.join(COMMANDS.keys())}")
        print(f"   Run `python scripts/pdt.py --help` for usage.")
        sys.exit(1)

    args = sys.argv[2:]
    COMMANDS[command](args)


if __name__ == "__main__":
    main()
