"""
cmd_search.py — Tìm kiếm requirements, patterns xuyên suốt tất cả docs.

Usage:
    python scripts/pdt.py search REQ-001          # Trace 1 requirement
    python scripts/pdt.py search --pattern "auth"  # Tìm pattern
    python scripts/pdt.py search --type FR         # List tất cả FR-IDs
    python scripts/pdt.py search --type REQ        # List tất cả REQ-IDs
    python scripts/pdt.py search --type ADR        # List tất cả ADR-IDs
"""

import re
from pathlib import Path

from .config import REPO_ROOT, DOCS_DIR, ARTIFACT_DEPS, ARTIFACT_SCAN


def search_in_files(pattern: str, case_insensitive: bool = True) -> list[dict]:
    """Search pattern trong tất cả docs files."""
    results = []
    flags = re.IGNORECASE if case_insensitive else 0

    for artifact_type, scan_config in ARTIFACT_SCAN.items():
        for scan_dir in scan_config["dirs"]:
            if not scan_dir.exists():
                continue
            for f in sorted(scan_dir.glob(scan_config["glob"])):
                if f.name.startswith("_"):
                    continue
                try:
                    content = f.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    continue

                for i, line in enumerate(content.split("\n"), 1):
                    if re.search(pattern, line, flags):
                        results.append({
                            "file": str(f.relative_to(REPO_ROOT)),
                            "type": artifact_type,
                            "line": i,
                            "content": line.strip()[:120],
                        })

    return results


def trace_requirement(req_id: str) -> dict:
    """Trace 1 requirement ID xuyên suốt tất cả documents.

    Returns mapping: artifact_type → [locations found]
    """
    trace = {}
    for artifact_type, scan_config in ARTIFACT_SCAN.items():
        locations = []
        for scan_dir in scan_config["dirs"]:
            if not scan_dir.exists():
                continue
            for f in sorted(scan_dir.glob(scan_config["glob"])):
                if f.name.startswith("_"):
                    continue
                try:
                    content = f.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    continue

                for i, line in enumerate(content.split("\n"), 1):
                    if req_id in line:
                        locations.append({
                            "file": str(f.relative_to(REPO_ROOT)),
                            "line": i,
                            "content": line.strip()[:120],
                        })

        trace[artifact_type] = locations

    return trace


def list_ids_by_type(id_type: str) -> list[dict]:
    """List tất cả IDs theo type (REQ, FR, NFR, ADR, etc.)."""
    pattern = rf"{id_type}-\d{{3}}"
    found = {}

    for artifact_type, scan_config in ARTIFACT_SCAN.items():
        for scan_dir in scan_config["dirs"]:
            if not scan_dir.exists():
                continue
            for f in sorted(scan_dir.glob(scan_config["glob"])):
                if f.name.startswith("_"):
                    continue
                try:
                    content = f.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    continue

                ids = re.findall(pattern, content)
                for id_val in ids:
                    if id_val not in found:
                        found[id_val] = {"id": id_val, "found_in": []}
                    found[id_val]["found_in"].append({
                        "file": str(f.relative_to(REPO_ROOT)),
                        "type": artifact_type,
                    })

    return sorted(found.values(), key=lambda x: x["id"])


def format_trace_report(req_id: str, trace: dict) -> str:
    """Format trace report cho 1 requirement."""
    lines = []
    lines.append("")
    lines.append(f"  🔗 Tracing: {req_id}")
    lines.append("  " + "═" * 56)

    found_anywhere = False
    for artifact_type in ARTIFACT_DEPS:
        locations = trace.get(artifact_type, [])
        if locations:
            found_anywhere = True
            icon = "✅"
        else:
            icon = "⬜"

        lines.append(f"  {icon} {artifact_type}")
        for loc in locations:
            lines.append(f"     {loc['file']}:{loc['line']}")
            lines.append(f"       {loc['content']}")

    if not found_anywhere:
        lines.append(f"  ❌ {req_id} not found in any document.")

    lines.append("")
    return "\n".join(lines)


def format_search_results(pattern: str, results: list[dict]) -> str:
    """Format search results."""
    lines = []
    lines.append("")
    lines.append(f"  🔍 Search: \"{pattern}\"")
    lines.append(f"  Found: {len(results)} match(es)")
    lines.append("  " + "─" * 56)

    # Group by file
    by_file = {}
    for r in results:
        by_file.setdefault(r["file"], []).append(r)

    for file, matches in by_file.items():
        lines.append(f"\n  📄 {file} ({matches[0]['type']})")
        for m in matches:
            lines.append(f"    L{m['line']:>4}: {m['content']}")

    lines.append("")
    return "\n".join(lines)


def format_id_list(id_type: str, ids: list[dict]) -> str:
    """Format ID listing."""
    lines = []
    lines.append("")
    lines.append(f"  📋 All {id_type}-xxx IDs")
    lines.append("  " + "─" * 56)

    if not ids:
        lines.append(f"  No {id_type} IDs found.")
    else:
        for id_info in ids:
            files = ", ".join(set(f["type"] for f in id_info["found_in"]))
            lines.append(f"  {id_info['id']:<12} found in: {files}")

    lines.append(f"\n  Total: {len(ids)} unique IDs")
    lines.append("")
    return "\n".join(lines)


def cmd_search(args: list[str]):
    """Entry point cho `pdt search`."""

    # Parse args
    pattern = None
    id_type = None
    positional = []

    i = 0
    while i < len(args):
        if args[i] == "--pattern" and i + 1 < len(args):
            pattern = args[i + 1]
            i += 2
        elif args[i] == "--type" and i + 1 < len(args):
            id_type = args[i + 1].upper()
            i += 2
        elif not args[i].startswith("-"):
            positional.append(args[i])
            i += 1
        else:
            i += 1

    if id_type:
        ids = list_ids_by_type(id_type)
        print(format_id_list(id_type, ids))
    elif positional:
        # Trace a specific ID
        req_id = positional[0]
        trace = trace_requirement(req_id)
        print(format_trace_report(req_id, trace))
    elif pattern:
        results = search_in_files(pattern)
        print(format_search_results(pattern, results))
    else:
        print("  Usage:")
        print("    pdt.py search REQ-001           # Trace requirement")
        print("    pdt.py search --pattern \"auth\"   # Search pattern")
        print("    pdt.py search --type REQ         # List all REQ-IDs")
        print("    pdt.py search --type FR          # List all FR-IDs")
