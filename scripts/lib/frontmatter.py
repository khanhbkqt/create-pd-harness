"""
frontmatter.py — Parse YAML frontmatter và completeness trackers từ markdown files.
"""

import re
from pathlib import Path
from datetime import datetime

from .config import REPO_ROOT, ARTIFACT_SCAN


def parse_frontmatter(filepath: Path) -> dict | None:
    """Parse YAML frontmatter từ markdown file.

    Returns dict với các fields từ frontmatter, hoặc None nếu không parse được.
    """
    try:
        content = filepath.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    fm = {}
    for line in match.group(1).split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            # Parse simple YAML lists
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                value = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()] if inner else []
            fm[key] = value

    return fm


def parse_completeness_tracker(filepath: Path) -> tuple[int, int, list[dict]]:
    """Parse Completeness Tracker table từ document.

    Returns (done_count, total_count, sections_detail).
    sections_detail = [{"name": str, "status": str, "notes": str}, ...]
    """
    try:
        content = filepath.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0, 0, []

    in_tracker = False
    done = 0
    total = 0
    sections = []

    for line in content.split("\n"):
        if "Completeness Tracker" in line:
            in_tracker = True
            continue
        if in_tracker and line.startswith("|") and "---" not in line and "Section" not in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 2:
                total += 1
                name = cols[0]
                status_raw = cols[1]
                notes = cols[2] if len(cols) > 2 else ""

                if "✅" in status_raw:
                    status = "done"
                    done += 1
                elif "📝" in status_raw:
                    status = "partial"
                    done += 0.5
                else:
                    status = "todo"

                sections.append({"name": name, "status": status, "notes": notes})

        if in_tracker and total > 0 and not line.startswith("|") and line.strip() == "---":
            break

    return int(done), total, sections


def get_file_mtime(filepath: Path) -> datetime | None:
    """Get file modification time."""
    try:
        return datetime.fromtimestamp(filepath.stat().st_mtime)
    except OSError:
        return None


def scan_all_artifacts() -> dict:
    """Scan tất cả artifact directories, trả về structured data.

    Returns dict: {artifact_type: [artifact_info, ...]}
    """
    results = {}

    for artifact_type, scan_config in ARTIFACT_SCAN.items():
        artifacts = []

        for scan_dir in scan_config["dirs"]:
            if not scan_dir.exists():
                continue

            glob_pattern = scan_config["glob"]
            for f in sorted(scan_dir.glob(glob_pattern)):
                if f.name.startswith("_"):
                    continue

                mtime = get_file_mtime(f)

                if glob_pattern == "*.tsx":
                    # Mockup pages — no frontmatter
                    artifacts.append({
                        "file": str(f.relative_to(REPO_ROOT)),
                        "abs_path": str(f),
                        "status": "draft",
                        "title": f.stem,
                        "updated": mtime.strftime("%Y-%m-%d") if mtime else "—",
                        "completeness": "—",
                        "completeness_done": 0,
                        "completeness_total": 0,
                        "sections": [],
                        "frontmatter": {},
                    })
                else:
                    fm = parse_frontmatter(f)
                    if fm is None:
                        continue
                    done, total, sections = parse_completeness_tracker(f)

                    artifacts.append({
                        "file": str(f.relative_to(REPO_ROOT)),
                        "abs_path": str(f),
                        "status": fm.get("status", "unknown"),
                        "title": fm.get("title", f.stem),
                        "updated": fm.get("updated", mtime.strftime("%Y-%m-%d") if mtime else "—"),
                        "version": fm.get("version", "—"),
                        "completeness": f"{done}/{total}" if total > 0 else "—",
                        "completeness_done": done,
                        "completeness_total": total,
                        "sections": sections,
                        "frontmatter": fm,
                    })

        results[artifact_type] = artifacts

    return results


def identify_artifact_type(filepath: Path) -> str | None:
    """Identify artifact type từ file path."""
    filepath_str = str(filepath)
    for artifact_type, scan_config in ARTIFACT_SCAN.items():
        for scan_dir in scan_config["dirs"]:
            if str(scan_dir) in filepath_str:
                return artifact_type
    return None
