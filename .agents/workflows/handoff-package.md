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

```
## Trạng thái Pipeline
- HOÀN THÀNH: Feature Intake ✓, Design Cycle ✓, Review Gate ✓
- ĐANG LÀM: Handoff Packaging
- TIẾP THEO: Delivery cho Implementation Team
- BLOCKED: [Nếu có]
```

## CHI TIẾT

### Step 1: Artifact Verification

**Skill**: [handoff/SKILL.md](../skills/handoff/SKILL.md) - Bước 1+2

VERIFY và GHI checklist:
- Tất cả artifacts approved ✓
- Cross-references consistent ✓
- Glossary up to date ✓

### Step 2: Implementation Plan

**Skill**: [handoff/SKILL.md](../skills/handoff/SKILL.md) - Bước 3

TẠO Implementation Plan với:
- Task breakdown (phased)
- Dependency graph (Mermaid)
- Acceptance criteria per task (traced to SRS)
- Design decisions summary (from ADRs)
- Mockup reference mapping

**CONTEXT AWARENESS trong Implementation Plan**:
```markdown
## Trạng thái dự án tại thời điểm handoff
- Vision: [tóm tắt 1 dòng]
- Scope: [tóm tắt PRD scope]
- Architecture: [tóm tắt TDD architecture]
- Constraints: [liệt kê từ SRS NFRs]
- Key Decisions: [liệt kê ADR-IDs với 1 dòng mỗi cái]
- Mockup Status: [X pages built, runnable via npm run dev]
```

### Step 3: Quick Start Guide

**Skill**: [handoff/SKILL.md](../skills/handoff/SKILL.md) - Bước 5

TẠO Quick Start cho implementation team:
- Đọc gì trước (priority order)
- Cách chạy mockups
- Bắt đầu code từ đâu
- Hỏi gì ở đâu

### Step 4: Bundle & Deliver

TẠO thư mục `handoff/[feature-name]/` với:
```
handoff/[feature-name]/
├── IMPLEMENTATION_PLAN.md
├── QUICK_START.md
├── REVIEW_GATE_REPORT.md     # Copy of review gate output
└── ARTIFACT_INDEX.md          # Links tới tất cả source docs
```

ARTIFACT_INDEX.md format:
```markdown
# Artifact Index: [Feature Name]

## Documents
| Type | Path | Status | Version |
|---|---|---|---|
| Vision | docs/vision/VISION.md | approved | 1.0 |
| PRD | docs/prd/[feature].md | approved | 1.2 |
| SRS | docs/srs/[feature].md | approved | 1.0 |
| TDD | docs/tdd/[feature].md | approved | 1.0 |

## Flows
| Flow | Path | Type |
|---|---|---|
| [Name] | docs/flows/[flow].md | userflow |

## Decisions
| ADR | Path | Status |
|---|---|---|
| ADR-001 | docs/decisions/001-[title].md | accepted |

## Mockups
| Page | Path | PRD Refs |
|---|---|---|
| HomePage | mockups/src/pages/HomePage.tsx | REQ-001, REQ-002 |

## Run Mockups
\`\`\`bash
cd mockups && npm install && npm run dev
\`\`\`
```

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
4. ARTIFACT_INDEX.md - Index toàn bộ docs

### Cho Implementation Team:
1. Đọc QUICK_START.md trước
2. Chạy mockups: cd mockups && npm run dev
3. Follow IMPLEMENTATION_PLAN.md task-by-task
4. Reference ARTIFACT_INDEX.md khi cần chi tiết

### Trạng thái Pipeline: HOÀN THÀNH
```

## QUY TẮC

1. HANDOFF chỉ sau Review Gate PASSED
2. IMPLEMENTATION PLAN chứa đầy đủ context cho team mới
3. QUICK START cho phép onboarding trong 30 phút
4. ARTIFACT INDEX là single source of truth cho tất cả docs
5. BUNDLE là self-contained - team chỉ cần đọc thư mục handoff
