---
title: "PRD: [Tên feature]"
status: draft
version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Spec_Steward
source: "[Link tới Feature Brief]"
linked_docs: []
sdlc_phase: requirements
---

# PRD: [Tên Feature]

## Completeness Tracker
<!-- Agent cập nhật tự động khi viết/sửa sections -->
| Section | Status | Notes |
|---|---|---|
| 1. Tóm tắt | ⬜ todo | |
| 2. Vấn đề cần giải quyết | ⬜ todo | |
| 3. User Personas & Nhu cầu | ⬜ todo | |
| 4. Phạm vi | ⬜ todo | |
| 5. Yêu cầu chức năng (MoSCoW) | ⬜ todo | |
| 6. Metrics thành công | ⬜ todo | |
| 7. Ràng buộc & Giả định | ⬜ todo | |
| 8. Dependencies | ⬜ todo | |
| 9. Timeline & Milestones | ⬜ todo | |
| 10. Rủi ro & Biện pháp | ⬜ todo | |
| 11. Lịch sử phê duyệt | ⬜ todo | |

---

## 1. Tóm tắt

_[2-3 câu mô tả feature, business value, và impact dự kiến.]_

## 2. Vấn đề cần giải quyết

_[Mô tả vấn đề chi tiết. TRÍCH NGUYÊN VĂN từ Feature Brief hoặc user statement.]_

> "[Trích dẫn nguyên văn từ user/stakeholder]"
> — _[Nguồn: Feature Brief, section X]_

### Tình trạng hiện tại
_[User đang giải quyết vấn đề này như thế nào?]_

### Hệ quả nếu không giải quyết
_[Ảnh hưởng business/user nếu feature này không được xây dựng.]_

## 3. User Personas & Nhu cầu

### Persona 1: [Tên]
- **Mô tả**: _[Demographics, vai trò]_
- **Nhu cầu**: _[Cần gì từ feature này]_
- **Pain point**: _[Đau ở đâu hiện tại]_
- **Nguồn**: _[Từ user research / interview / assumption]_

### Persona 2: [Tên]
_[Tương tự trên]_

## 4. Phạm vi

### 4.1 Bao gồm (In Scope)
- _[Capability 1]_
- _[Capability 2]_

### 4.2 Loại trừ (Out of Scope)
- _[Capability để phase sau]_
- _[Lý do loại trừ]_

## 5. Yêu cầu chức năng (MoSCoW)

### Must Have

#### REQ-001: [Tên requirement]
- **Mức ưu tiên**: Must
- **Mô tả**: _[Chi tiết]_
- **Nguồn**: _"[Trích nguyên văn từ Feature Brief]"_ — _[Nguồn: Feature Brief, section X]_
- **Acceptance Criteria**:
  - [ ] AC-001-1: _[Tiêu chí đo lường được]_
  - [ ] AC-001-2: _[Tiêu chí đo lường được]_
- **Dependencies**: Không

#### REQ-002: [Tên requirement]
_[Format tương tự REQ-001]_

### Should Have

#### REQ-003: [Tên requirement]
_[Format tương tự]_

### Could Have

#### REQ-004: [Tên requirement]
_[Format tương tự]_

### Won't Have (this release)

#### REQ-005: [Tên requirement]
- **Lý do delay**: _[Giải thích]_

## 6. Metrics thành công

| Metric | Mô tả | Target | Cách đo | Timeline |
|---|---|---|---|---|
| _[Metric 1]_ | _[Mô tả]_ | _[Target]_ | _[Tool/method]_ | _[Khi nào đo]_ |
| _[Metric 2]_ | _[Mô tả]_ | _[Target]_ | _[Tool/method]_ | _[Khi nào đo]_ |

## 7. Ràng buộc & Giả định

### Ràng buộc
| # | Ràng buộc | Loại | Ảnh hưởng |
|---|---|---|---|
| 1 | _[Ràng buộc]_ | Kỹ thuật/Business/Pháp lý | _[Ảnh hưởng]_ |

### Giả định
| # | Giả định | Cách verify | Rủi ro nếu sai |
|---|---|---|---|
| 1 | _[Giả định]_ | _[Cách kiểm chứng]_ | _[Hệ quả]_ |

## 8. Dependencies

| Dependency | Loại | Owner | Status | Impact nếu delay |
|---|---|---|---|---|
| _[Dependency]_ | Internal/External | _[Team/Person]_ | _[Status]_ | _[Impact]_ |

## 9. Timeline & Milestones

| Milestone | Mô tả | Target Date | Status |
|---|---|---|---|
| Design Complete | Tất cả docs approved | _[Date]_ | Chưa bắt đầu |
| Implementation Start | Handoff cho dev team | _[Date]_ | Chưa bắt đầu |
| Alpha Release | Internal testing | _[Date]_ | Chưa bắt đầu |
| Beta Release | Limited user testing | _[Date]_ | Chưa bắt đầu |
| GA | General availability | _[Date]_ | Chưa bắt đầu |

## 10. Rủi ro & Biện pháp

| # | Rủi ro | Khả năng | Tác động | Biện pháp | Owner |
|---|---|---|---|---|---|
| 1 | _[Rủi ro]_ | Cao/TB/Thấp | Cao/TB/Thấp | _[Biện pháp]_ | _[Ai]_ |

## 11. Lịch sử phê duyệt

| Ngày | Người | Hành động | Ghi chú |
|---|---|---|---|
| _[Date]_ | _[Tên]_ | Created | Bản draft đầu tiên |

---

_Quy ước: Mỗi REQ-ID là duy nhất trong toàn bộ dự án. Format: REQ-[3 chữ số]. Acceptance Criteria format: AC-[REQ-ID]-[số]._
