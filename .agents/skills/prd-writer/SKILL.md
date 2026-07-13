---
name: prd-writer
description: Viết Product Requirements Document theo SDLC. Citation-enforced. Mỗi requirement truy ngược được tới Feature Brief hoặc stakeholder statement.
---

# Skill: PRD Writer (SDLC-Compliant)

## KÍCH HOẠT

Khi Feature Brief đã hoàn thành và được user approve. VERIFY Feature Brief tồn tại trước khi bắt đầu.

## PERSONA ACTIVE: `Spec_Steward`

Khắt khe về completeness và traceability. Mỗi requirement PHẢI có nguồn. Mỗi section PHẢI hoàn chỉnh trước khi chuyển sang section tiếp.

## QUY TRÌNH

### Dependency Check & Khởi đầu
1. Chạy `python scripts/pdt.py status` để kiểm tra Feature Brief và Vision.
2. Nếu Feature Brief chưa có hoặc chưa approved, thông báo cho user trước khi tiếp tục.

### Bước 1: Thu thập nguồn

SCAN các artifacts hiện có:
- Feature Brief trong `docs/features/` hoặc output từ brainstorm session
- Vision document (`docs/vision/VISION.md`)
- Glossary (`docs/GLOSSARY.md`)
- Decisions đã có (`docs/decisions/`)
- Existing PRDs (`docs/prd/`)

GHI RÕ danh sách nguồn đã đọc:
```
Nguồn đã tham chiếu:
- [x] Feature Brief: [tên file]
- [x] Vision: VISION.md
- [ ] Glossary: GLOSSARY.md (chưa có)
```

### Bước 2: Viết PRD

TẠO file `docs/prd/[feature-name].md` theo template `docs/prd/_TEMPLATE.md`.

MỖI requirement viết theo format:

```markdown
### REQ-[ID]: [Tên requirement]
- **Mức ưu tiên**: Must/Should/Could/Won't (MoSCoW)
- **Mô tả**: [Mô tả chi tiết]
- **Nguồn**: [Trích nguyên văn từ Feature Brief, section X]
- **Acceptance Criteria**:
  - [ ] AC-1: [Tiêu chí cụ thể, đo lường được]
  - [ ] AC-2: [Tiêu chí cụ thể, đo lường được]
- **Dependencies**: [Liệt kê REQ-IDs phụ thuộc]
```

### Bước 3: Traceability Check

VERIFY mỗi requirement:
- Có source reference trỏ về Feature Brief ✓
- Có acceptance criteria đo lường được ✓
- Dependencies rõ ràng ✓
- Không mâu thuẫn với requirements khác ✓

### Bước 4: Output

GHI FILE vào `docs/prd/[feature-name].md` với frontmatter:

```yaml
---
title: "PRD: [Tên feature]"
status: draft | review | approved | superseded
version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Spec_Steward
source: docs/prd/feature-brief-[name].md
linked_docs:
  - docs/vision/VISION.md
  - docs/srs/[feature-name].md
sdlc_phase: requirements
---
```

Sau khi hoàn thành, BẮT BUỘC thực hiện:
- Chạy `python scripts/pdt.py status --update` để đồng bộ tracker.
- Chạy `python scripts/pdt.py log --add "Viết/Cập nhật PRD cho [feature-name]" --artifact "PRD"`

## SDLC MAPPING

| SDLC Phase | PRD Section | Mục đích |
|---|---|---|
| Inception | Executive Summary, Problem Statement | Tại sao làm? |
| Requirements | Feature Requirements, Acceptance Criteria | Làm gì? |
| Analysis | User Personas, Scope, Dependencies | Cho ai? Giới hạn? |
| Planning | Timeline, Risks, Success Metrics | Khi nào? Rủi ro? |

## QUY TẮC

1. MỖI requirement format: `REQ-[3 chữ số]` (REQ-001, REQ-002...)
2. MỖI acceptance criteria format: `AC-[REQ ID]-[số]` (AC-001-1, AC-001-2...)
3. TRÍCH NGUYÊN VĂN từ Feature Brief cho mỗi requirement source
4. GHI "CHƯA CÓ DỮ LIỆU - cần xác nhận" khi thiếu thông tin
5. LIÊN KẾT tới Vision document cho business alignment
6. CẬP NHẬT Glossary khi xuất hiện thuật ngữ mới
7. ĐỒNG BỘ: Chạy `pdt.py status --update` và `pdt.py log` cho mọi thay đổi.

## CHUYỂN GIAO

→ Khi PRD status = `approved`, kích hoạt Design Cycle workflow.
→ PRD là input cho: SRS Writer, Flow Designer, Mockup Designer.
