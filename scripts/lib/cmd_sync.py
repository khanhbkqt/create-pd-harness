"""
cmd_sync.py — Detect stale artifacts sau khi document thay đổi.

Dựa trên dependency graph + file timestamps.

Usage:
    python scripts/pdt.py sync                    # Check tất cả
    python scripts/pdt.py sync docs/prd/auth.md   # Impact analysis 1 file
"""

from pathlib import Path
from datetime import datetime

from .config import REPO_ROOT, ARTIFACT_DEPS
from .frontmatter import scan_all_artifacts, get_file_mtime, identify_artifact_type


# Reverse dependency map: type → list of downstream types
DOWNSTREAM_MAP = {}
for downstream, upstreams in ARTIFACT_DEPS.items():
    for upstream in upstreams:
        DOWNSTREAM_MAP.setdefault(upstream, []).append(downstream)


def find_all_stale(results: dict) -> list[dict]:
    """Find all stale artifacts bằng timestamp comparison."""
    stale = []

    for downstream_type, upstream_types in ARTIFACT_DEPS.items():
        downstream_files = results.get(downstream_type, [])

        for df in downstream_files:
            df_mtime = get_file_mtime(Path(df["abs_path"]))
            if df_mtime is None:
                continue

            for upstream_type in upstream_types:
                upstream_files = results.get(upstream_type, [])
                for uf in upstream_files:
                    uf_mtime = get_file_mtime(Path(uf["abs_path"]))
                    if uf_mtime is None:
                        continue

                    if uf_mtime > df_mtime:
                        delta = uf_mtime - df_mtime
                        stale.append({
                            "downstream": df["file"],
                            "downstream_type": downstream_type,
                            "upstream": uf["file"],
                            "upstream_type": upstream_type,
                            "upstream_modified": uf_mtime.strftime("%Y-%m-%d %H:%M"),
                            "downstream_modified": df_mtime.strftime("%Y-%m-%d %H:%M"),
                            "stale_hours": round(delta.total_seconds() / 3600, 1),
                        })

    return stale


def find_impact(filepath: Path, results: dict) -> list[dict]:
    """Find downstream impact khi sửa 1 file cụ thể."""
    artifact_type = identify_artifact_type(filepath)
    if artifact_type is None:
        return []

    impacted = []
    file_mtime = get_file_mtime(filepath)

    # Direct downstream
    for ds_type in DOWNSTREAM_MAP.get(artifact_type, []):
        for a in results.get(ds_type, []):
            impacted.append({
                "file": a["file"],
                "type": ds_type,
                "status": a["status"],
                "relation": "direct downstream",
            })

    # Indirect downstream (2nd level)
    for ds_type in DOWNSTREAM_MAP.get(artifact_type, []):
        for ds2_type in DOWNSTREAM_MAP.get(ds_type, []):
            for a in results.get(ds2_type, []):
                impacted.append({
                    "file": a["file"],
                    "type": ds2_type,
                    "status": a["status"],
                    "relation": f"indirect ({artifact_type} → {ds_type} → {ds2_type})",
                })

    return impacted


def format_sync_report(stale: list[dict]) -> str:
    """Format stale items report."""
    if not stale:
        return "✅ All artifacts are in sync.\n"

    lines = []
    lines.append("")
    lines.append("⚠  SYNC ISSUES DETECTED")
    lines.append("═" * 60)
    lines.append("")

    # Group by downstream
    by_downstream = {}
    for item in stale:
        key = item["downstream"]
        by_downstream.setdefault(key, []).append(item)

    for downstream, items in by_downstream.items():
        lines.append(f"  📄 {downstream}")
        lines.append(f"     Type: {items[0]['downstream_type']}")
        lines.append(f"     Last modified: {items[0]['downstream_modified']}")
        lines.append(f"     Stale because:")
        for item in items:
            hours = item["stale_hours"]
            time_str = f"{hours}h" if hours < 24 else f"{hours / 24:.1f}d"
            lines.append(f"       ← {item['upstream']} changed {time_str} later")
        lines.append("")

    lines.append("═" * 60)
    lines.append("  Actions:")
    lines.append("    1. Review stale artifacts against updated upstreams")
    lines.append("    2. Update content + frontmatter 'updated' date")
    lines.append("    3. Run `python scripts/pdt.py status --update`")
    lines.append("")
    return "\n".join(lines)


def format_impact_report(filepath: Path, impacted: list[dict]) -> str:
    """Format impact analysis report."""
    lines = []
    lines.append("")
    lines.append(f"  🔍 Impact Analysis: {filepath.relative_to(REPO_ROOT)}")
    lines.append("═" * 60)

    if not impacted:
        lines.append("  No downstream artifacts affected.")
    else:
        lines.append(f"  {len(impacted)} artifact(s) may need review:")
        lines.append("")
        for item in impacted:
            icon = "🔴" if item["status"] == "approved" else "🟡"
            lines.append(f"  {icon} {item['file']}")
            lines.append(f"     Status: {item['status']} | {item['relation']}")

    lines.append("")
    lines.append("═" * 60)
    lines.append("")
    return "\n".join(lines)


def cmd_sync(args: list[str]):
    """Entry point cho `pdt sync`."""
    results = scan_all_artifacts()

    file_args = [a for a in args if not a.startswith("-")]

    if file_args:
        filepath = Path(file_args[0])
        if not filepath.is_absolute():
            filepath = REPO_ROOT / filepath
        if not filepath.exists():
            print(f"❌ File not found: {filepath}")
            return

        impacted = find_impact(filepath, results)
        print(format_impact_report(filepath, impacted))
    else:
        stale = find_all_stale(results)
        print(format_sync_report(stale))
