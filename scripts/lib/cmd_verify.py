"""
cmd_verify.py — Pre-review-gate verification checks.

Chạy các checks tương tự Review Gate nhưng nhẹ hơn, bất kỳ lúc nào.

Usage:
    python scripts/pdt.py verify                     # Run all checks
    python scripts/pdt.py verify --check completeness
    python scripts/pdt.py verify --check traceability
    python scripts/pdt.py verify --check citation
    python scripts/pdt.py verify --json
"""

import re
import json
from pathlib import Path

from .config import ARTIFACT_DEPS, REQUIRED_SECTIONS, REPO_ROOT, DOCS_DIR
from .frontmatter import scan_all_artifacts


def check_completeness(results: dict) -> dict:
    """Check 1: Artifact completeness."""
    issues = []
    passed = 0
    total = 0

    for artifact_type in ARTIFACT_DEPS:
        total += 1
        artifacts = results.get(artifact_type, [])
        if not artifacts:
            issues.append({
                "severity": "HARD",
                "artifact": artifact_type,
                "issue": "Not started — no files found",
            })
        else:
            has_content = False
            for a in artifacts:
                if a["completeness_total"] > 0:
                    has_content = True
                    if a["completeness_done"] < a["completeness_total"]:
                        pct = int(a["completeness_done"] / a["completeness_total"] * 100)
                        issues.append({
                            "severity": "SOFT" if pct >= 50 else "HARD",
                            "artifact": f"{artifact_type} ({a['file']})",
                            "issue": f"Incomplete: {a['completeness']} sections ({pct}%)",
                        })
                    else:
                        passed += 1
                elif a["status"] in ("draft", "review", "approved"):
                    passed += 1

            if not has_content and artifacts:
                # Has files but no completeness tracker
                passed += 1  # Assume OK if file exists

    return {
        "name": "Completeness",
        "passed": len(issues) == 0,
        "total": total,
        "ok": passed,
        "issues": issues,
    }


def check_traceability(results: dict) -> dict:
    """Check 2: Traceability — scan REQ-IDs in PRD, check they appear in SRS."""
    issues = []

    # Collect REQ-IDs from PRD files
    req_ids = set()
    prd_files = results.get("PRD", [])
    for prd in prd_files:
        try:
            content = Path(prd["abs_path"]).read_text(encoding="utf-8")
            found = re.findall(r"REQ-\d{3}", content)
            req_ids.update(found)
        except (OSError, UnicodeDecodeError):
            pass

    if not req_ids:
        return {
            "name": "Traceability",
            "passed": True,
            "issues": [{"severity": "INFO", "artifact": "PRD", "issue": "No REQ-IDs found (PRD may not exist yet)"}],
        }

    # Check REQ-IDs appear in SRS
    srs_content = ""
    srs_files = results.get("SRS", [])
    for srs in srs_files:
        try:
            srs_content += Path(srs["abs_path"]).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            pass

    # Check REQ-IDs appear in TDD
    tdd_content = ""
    tdd_files = results.get("TDD", [])
    for tdd in tdd_files:
        try:
            tdd_content += Path(tdd["abs_path"]).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            pass

    for req_id in sorted(req_ids):
        in_srs = req_id in srs_content if srs_content else False
        in_tdd = req_id in tdd_content if tdd_content else False

        if not in_srs and srs_files:
            issues.append({
                "severity": "HARD",
                "artifact": "SRS",
                "issue": f"{req_id} not found in SRS",
            })
        if not in_tdd and tdd_files:
            issues.append({
                "severity": "SOFT",
                "artifact": "TDD",
                "issue": f"{req_id} not traced to TDD",
            })

    return {
        "name": "Traceability",
        "passed": not any(i["severity"] == "HARD" for i in issues),
        "total_reqs": len(req_ids),
        "issues": issues,
    }


def check_citation(results: dict) -> dict:
    """Check 3: Citation — scan for unresolved data gaps."""
    issues = []
    total_claims = 0
    uncited = 0

    doc_types = ["PRD", "SRS", "TDD"]
    for doc_type in doc_types:
        for a in results.get(doc_type, []):
            try:
                content = Path(a["abs_path"]).read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            # Count "CHƯA CÓ DỮ LIỆU" occurrences
            gaps = re.findall(r"CHƯA CÓ DỮ LIỆU", content)
            if gaps:
                issues.append({
                    "severity": "SOFT",
                    "artifact": a["file"],
                    "issue": f"{len(gaps)} unresolved data gap(s) — 'CHƯA CÓ DỮ LIỆU'",
                })
                uncited += len(gaps)

            # Count [Nguồn: ...] citations
            citations = re.findall(r"\[Nguồn:", content)
            total_claims += len(citations)

    rate = (total_claims / (total_claims + uncited) * 100) if (total_claims + uncited) > 0 else 100

    return {
        "name": "Citation",
        "passed": uncited == 0,
        "citation_rate": round(rate, 1),
        "total_citations": total_claims,
        "unresolved_gaps": uncited,
        "issues": issues,
    }


def check_consistency(results: dict) -> dict:
    """Check 4: Cross-document consistency."""
    issues = []

    # Check: Flows reference screens that exist in Mockup
    flow_screens = set()
    for flow in results.get("Flows", []):
        fm = flow.get("frontmatter", {})
        linked = fm.get("linked_screens", [])
        if isinstance(linked, list):
            flow_screens.update(linked)

    mockup_pages = set()
    for mockup in results.get("Mockup", []):
        mockup_pages.add(mockup["title"])

    for screen in flow_screens:
        if screen and screen not in mockup_pages:
            issues.append({
                "severity": "SOFT",
                "artifact": "Flows → Mockup",
                "issue": f"Flow references screen '{screen}' but no mockup page found",
            })

    return {
        "name": "Consistency",
        "passed": not any(i["severity"] == "HARD" for i in issues),
        "issues": issues,
    }


ALL_CHECKS = {
    "completeness": check_completeness,
    "traceability": check_traceability,
    "citation": check_citation,
    "consistency": check_consistency,
}


def format_verify_report(check_results: list[dict]) -> str:
    """Format verification report."""
    lines = []
    lines.append("")
    lines.append("╔══════════════════════════════════════════════════════════╗")
    lines.append("║  🔍 VERIFICATION REPORT                                 ║")
    lines.append("╚══════════════════════════════════════════════════════════╝")
    lines.append("")

    hard_fails = 0
    soft_warns = 0

    for check in check_results:
        icon = "✅" if check["passed"] else "❌"
        lines.append(f"  {icon} {check['name']}")

        if check.get("citation_rate") is not None:
            lines.append(f"     Citation rate: {check['citation_rate']}%")

        if check.get("total_reqs") is not None:
            lines.append(f"     REQ-IDs tracked: {check['total_reqs']}")

        for issue in check.get("issues", []):
            if issue["severity"] == "HARD":
                hard_fails += 1
                lines.append(f"     🔴 HARD: [{issue['artifact']}] {issue['issue']}")
            elif issue["severity"] == "SOFT":
                soft_warns += 1
                lines.append(f"     🟡 SOFT: [{issue['artifact']}] {issue['issue']}")
            elif issue["severity"] == "INFO":
                lines.append(f"     ℹ  INFO: [{issue['artifact']}] {issue['issue']}")

        lines.append("")

    lines.append("  ─── Summary ───")
    if hard_fails == 0 and soft_warns == 0:
        lines.append("  ✅ All checks passed! Ready for Review Gate.")
    elif hard_fails == 0:
        lines.append(f"  🟡 Passed with {soft_warns} warning(s). Handoff possible with accepted risks.")
    else:
        lines.append(f"  🔴 {hard_fails} hard fail(s), {soft_warns} warning(s). Fix hard fails before handoff.")
    lines.append("")

    return "\n".join(lines)


def cmd_verify(args: list[str]):
    """Entry point cho `pdt verify`."""
    results = scan_all_artifacts()

    # Filter to specific check?
    specific_check = None
    for i, arg in enumerate(args):
        if arg == "--check" and i + 1 < len(args):
            specific_check = args[i + 1].lower()

    if specific_check:
        if specific_check not in ALL_CHECKS:
            print(f"❌ Unknown check: {specific_check}")
            print(f"   Available: {', '.join(ALL_CHECKS.keys())}")
            return
        check_results = [ALL_CHECKS[specific_check](results)]
    else:
        check_results = [check_fn(results) for check_fn in ALL_CHECKS.values()]

    if "--json" in args:
        print(json.dumps(check_results, indent=2, ensure_ascii=False))
    else:
        print(format_verify_report(check_results))
