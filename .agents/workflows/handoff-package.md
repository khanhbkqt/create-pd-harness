---
description: Review Gate Pass → Bundle Artifacts → Generate Implementation Plan → Handoff
---

# Workflow: Handoff Package

> Review Gate Pass → Bundle Artifacts → Generate Implementation Plan → Handoff

## PIPELINE

```mermaid
flowchart LR
    A["Review Gate\nPASSED ✓"] --> B["1. Artifact\nVerification"]
    B --> C["2. Implementation\nPlan"]
    C --> D["3. Quick Start\nGuide"]
    D --> E["4. Bundle\n& Deliver"]
    E --> F["HANDOFF\nCOMPLETE"]
```

## TIỀN ĐIỀU KIỆN

VERIFY Review Gate đã passed. Nếu chưa → BLOCK và trỏ tới [review-gate.md](review-gate.md).

## CONTEXT AWARENESS

TRƯỚC KHI bắt đầu Handoff, chạy `python scripts/pdt.py status` để kiểm tra độ sẵn sàng của toàn bộ dự án.

## CHI TIẾT

### Step 1: Artifact Verification

**Skill**: [handoff/SKILL.md](../skills/handoff/SKILL.md) - Bước 1+2

VERIFY và GHI checklist:
- Tất cả artifacts approved hoặc draft-accepted (có note ghi rõ trong STATUS.md) ✓
- Cross-references consistent (chạy `python scripts/pdt.py sync` trả về sạch lỗi) ✓
- Glossary up to date ✓

---

### Step 2: Implementation Plan

**Skill**: [handoff/SKILL.md](../skills/handoff/SKILL.md) - Bước 3

TẠO Implementation Plan với:
- Task breakdown (phased)
- Dependency graph (Mermaid)
- Acceptance criteria per task (traced to SRS)
- Design decisions summary (from ADRs)
- Mockup reference mapping

---

### Step 3: Quick Start Guide

**Skill**: [handoff/SKILL.md](../skills/handoff/SKILL.md) - Bước 5

TẠO Quick Start cho implementation team.

---

### Step 4: Bundle & Deliver

TẠO thư mục `handoff/[feature-name]/` với:
```
handoff/[feature-name]/
├── IMPLEMENTATION_PLAN.md
├── QUICK_START.md
├── REVIEW_GATE_REPORT.md     # Copy of review gate output
├── STATUS.md                 # Copy of docs/STATUS.md tại thời điểm handoff
└── ARTIFACT_INDEX.md          # Links tới tất cả source docs
```

Trước khi tạo package:
1. Chạy `python scripts/pdt.py status --update` lần cuối.
2. Sao chép `docs/STATUS.md` vào `handoff/[feature-name]/STATUS.md`.
3. Ghi log hoạt động handoff:
   - `python scripts/pdt.py log --add "Handoff package completed cho [feature-name]" --artifact "Handoff"`

---

## OUTPUT CUỐI CÙNG

```
## HANDOFF COMPLETE ✓

Feature: [Tên]
Package: handoff/[feature-name]/
Ngày: YYYY-MM-DD

### Nội dung package:
1. IMPLEMENTATION_PLAN.md - [X tasks, Y phases]
2. QUICK_START.md - Hướng dẫn onboarding
3. REVIEW_GATE_REPORT.md - Kết quả review
4. STATUS.md - Bản chụp trạng thái artifacts
5. ARTIFACT_INDEX.md - Index toàn bộ docs

### Cho Implementation Team:
1. Đọc QUICK_START.md trước
2. Chạy mockups: cd mockups && npm run dev
3. Follow IMPLEMENTATION_PLAN.md task-by-task
4. Reference ARTIFACT_INDEX.md khi cần chi tiết

### Trạng thái Pipeline: HOÀN THÀNH
```

## QUY TẮC

1. **Gate Pass**: Chỉ tiến hành handoff khi Review Gate đạt status `PASSED` hoặc `PASSED WITH WARNINGS` (user đồng ý).
2. **STATUS COPY**: Bắt buộc đính kèm copy của `docs/STATUS.md` trong handoff package.
3. **LOGGING**: Log action đầy đủ trước khi kết thúc phase.
