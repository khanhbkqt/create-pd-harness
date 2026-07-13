---
feature: "[Tên feature]"
created: YYYY-MM-DD
handoff_status: ready
source_docs:
  - docs/prd/[feature].md
  - docs/srs/[feature].md
  - docs/tdd/[feature].md
---

# Handoff Checklist: [Tên Feature]

## Artifact Verification

| # | Artifact | File | Status | Verified |
|---|---|---|---|---|
| 1 | Vision | docs/vision/VISION.md | _[status]_ | [ ] |
| 2 | PRD | docs/prd/[feature].md | _[status]_ | [ ] |
| 3 | SRS | docs/srs/[feature].md | _[status]_ | [ ] |
| 4 | TDD | docs/tdd/[feature].md | _[status]_ | [ ] |
| 5 | Flows | docs/flows/[flows].md | _[status]_ | [ ] |
| 6 | Decisions | docs/decisions/[adrs].md | _[status]_ | [ ] |
| 7 | Mockups | mockups/src/pages/ | _[status]_ | [ ] |
| 8 | Glossary | docs/GLOSSARY.md | _[status]_ | [ ] |

## Review Gate Results

| Check | Status | Notes |
|---|---|---|
| Completeness | _[Pass/Fail]_ | _[Notes]_ |
| Traceability | _[Pass/Fail]_ | _[Notes]_ |
| Consistency | _[Pass/Fail]_ | _[Notes]_ |
| Citation | _[Pass/Fail]_ | _[Notes]_ |
| Mockup Quality | _[Pass/Fail]_ | _[Notes]_ |

## Handoff Contents

```
handoff/[feature-name]/
├── IMPLEMENTATION_PLAN.md
├── QUICK_START.md
├── REVIEW_GATE_REPORT.md
└── ARTIFACT_INDEX.md
```

## Cho Implementation Team

1. ĐỌC `QUICK_START.md` trước (5 phút)
2. CHẠY mockups: `cd mockups && npm install && npm run dev`
3. FOLLOW `IMPLEMENTATION_PLAN.md` task-by-task
4. REFERENCE `ARTIFACT_INDEX.md` khi cần chi tiết

---

_Handoff date: YYYY-MM-DD_
