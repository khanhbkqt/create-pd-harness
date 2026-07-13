"""
cmd_priority.py — Gợi ý công việc tiếp theo dựa trên dependency graph + trạng thái hiện tại.

Usage:
    python scripts/pdt.py priority            # Recommended next actions
    python scripts/pdt.py priority --verbose  # Với reasoning chi tiết
"""

from .config import ARTIFACT_DEPS, PRIORITY_WEIGHTS
from .frontmatter import scan_all_artifacts


def compute_priorities(results: dict) -> list[dict]:
    """Tính toán priority cho từng artifact type chưa hoàn thành.

    Logic:
    1. Skip artifact types đã approved
    2. Score = base_weight × dependency_readiness × urgency_multiplier
    3. Dependency readiness: tất cả deps approved = 1.0, draft = 0.7, missing = 0.3
    4. Urgency: downstream nhiều → urgency cao (nhiều thứ đang chờ)
    """
    priorities = []

    # Count downstream waiters cho mỗi type
    downstream_count = {}
    for atype, deps in ARTIFACT_DEPS.items():
        for dep in deps:
            downstream_count[dep] = downstream_count.get(dep, 0) + 1

    for artifact_type in ARTIFACT_DEPS:
        artifacts = results.get(artifact_type, [])

        # Skip if already approved
        if artifacts and all(a["status"] == "approved" for a in artifacts):
            continue

        # Base weight
        base_weight = PRIORITY_WEIGHTS.get(artifact_type, 1)

        # Dependency readiness
        deps = ARTIFACT_DEPS[artifact_type]
        dep_readiness = 1.0
        dep_detail = []
        for dep in deps:
            dep_artifacts = results.get(dep, [])
            if not dep_artifacts:
                dep_readiness *= 0.3
                dep_detail.append(f"{dep}: ❌ not started")
            elif any(a["status"] == "approved" for a in dep_artifacts):
                dep_readiness *= 1.0
                dep_detail.append(f"{dep}: ✅ approved")
            elif any(a["status"] in ("draft", "review") for a in dep_artifacts):
                dep_readiness *= 0.7
                dep_detail.append(f"{dep}: 📝 draft")
            else:
                dep_readiness *= 0.3
                dep_detail.append(f"{dep}: ❌ unknown")

        # Urgency: how many things are waiting for this
        waiters = downstream_count.get(artifact_type, 0)
        urgency = 1.0 + (waiters * 0.2)

        # Final score
        score = base_weight * dep_readiness * urgency

        # Status description
        if not artifacts:
            current_status = "not started"
            action = "Tạo mới"
        else:
            statuses = set(a["status"] for a in artifacts)
            current_status = ", ".join(statuses)
            if "draft" in statuses:
                # Check completeness
                done = sum(a["completeness_done"] for a in artifacts)
                total = sum(a["completeness_total"] for a in artifacts)
                if total > 0:
                    action = f"Hoàn thiện ({done}/{total} sections)"
                else:
                    action = "Hoàn thiện draft"
            elif "review" in statuses:
                action = "Chờ approve"
            else:
                action = "Xem lại"

        priorities.append({
            "type": artifact_type,
            "score": round(score, 1),
            "status": current_status,
            "action": action,
            "dep_readiness": dep_readiness,
            "dep_detail": dep_detail,
            "waiters": waiters,
            "reasoning": [],
        })

    # Sort by score descending
    priorities.sort(key=lambda x: x["score"], reverse=True)

    # Add reasoning
    for p in priorities:
        reasons = []
        if p["dep_readiness"] >= 0.9:
            reasons.append("Dependencies sẵn sàng")
        elif p["dep_readiness"] < 0.5:
            reasons.append("⚠ Dependencies chưa đủ — output có thể cần rework")
        if p["waiters"] > 0:
            reasons.append(f"{p['waiters']} artifact(s) đang chờ output này")
        p["reasoning"] = reasons

    return priorities


def format_priority_report(priorities: list[dict], verbose: bool = False) -> str:
    """Format priority list cho terminal."""
    if not priorities:
        return "✅ All artifacts approved! Ready for Review Gate.\n"

    lines = []
    lines.append("")
    lines.append("╔══════════════════════════════════════════════════════════╗")
    lines.append("║  🎯 PRIORITY — Next Actions                             ║")
    lines.append("╚══════════════════════════════════════════════════════════╝")
    lines.append("")

    for i, p in enumerate(priorities):
        rank = i + 1
        score_bar = "●" * min(int(p["score"]), 15)

        if rank == 1:
            marker = "👉"
        elif rank <= 3:
            marker = f" {rank}."
        else:
            marker = f" {rank}."

        lines.append(f"  {marker} {p['type']:<16} {p['action']}")
        lines.append(f"      Score: {p['score']:<6} {score_bar}")
        lines.append(f"      Status: {p['status']}")

        if p["reasoning"]:
            for r in p["reasoning"]:
                lines.append(f"      → {r}")

        if verbose and p["dep_detail"]:
            lines.append(f"      Dependencies:")
            for d in p["dep_detail"]:
                lines.append(f"        {d}")

        lines.append("")

    lines.append("  ─── Recommendation ───")
    top = priorities[0]
    lines.append(f"  Start with: {top['type']} — {top['action']}")
    if top["dep_readiness"] < 0.7:
        lines.append(f"  ⚠ Note: dependencies chưa hoàn chỉnh, output có thể cần revision")
    lines.append("")

    return "\n".join(lines)


def cmd_priority(args: list[str]):
    """Entry point cho `pdt priority`."""
    verbose = "--verbose" in args or "-v" in args
    results = scan_all_artifacts()
    priorities = compute_priorities(results)
    print(format_priority_report(priorities, verbose=verbose))
