---
id: ADR-[NNN]
title: "[Tiêu đề quyết định]"
status: proposed
created: YYYY-MM-DD
updated: YYYY-MM-DD
deciders: "[Personas tham gia]"
linked_reqs: []
supersedes: null
superseded_by: null
---

# ADR-[NNN]: [Tiêu đề quyết định]

## Bối cảnh

_[Tình huống dẫn đến cần ra quyết định. Trích dẫn requirements liên quan.]_

> "[Trích nguyên văn requirement hoặc constraint]"
> — _[Nguồn: PRD/SRS, REQ-XXX / FR-XXX]_

## Quyết định

_[Phát biểu quyết định rõ ràng, 1-2 câu. Dạng: "Sử dụng [X] cho [mục đích] vì [lý do chính]."]_

## Các phương án đã xem xét

### Phương án A: [Tên]

_[Mô tả ngắn phương án]_

- **Ưu điểm**:
  - _[Ưu điểm 1]_ — _[Nguồn: benchmark/doc/experience]_
  - _[Ưu điểm 2]_
- **Nhược điểm**:
  - _[Nhược điểm 1]_ — _[Nguồn]_
  - _[Nhược điểm 2]_
- **Ảnh hưởng tới requirements**: REQ-XXX, FR-XXX

### Phương án B: [Tên]

_[Format tương tự phương án A]_

### Phương án C: [Tên] _(nếu có)_

_[Format tương tự]_

## Hệ quả

### Tích cực
- _[Hệ quả tốt từ quyết định]_

### Tiêu cực
- _[Hệ quả cần chấp nhận]_

### Rủi ro
| Rủi ro | Khả năng | Biện pháp giảm thiểu |
|---|---|---|
| _[Rủi ro]_ | Cao/TB/Thấp | _[Biện pháp]_ |

## Liên kết

- **PRD**: _[Link tới PRD file, REQ-IDs]_
- **SRS**: _[Link tới SRS file, FR/NFR-IDs]_
- **TDD**: _[Link tới TDD section affected]_
- **Related ADRs**: _[Links tới ADRs liên quan]_

---

_Quy ước: ADR là immutable sau khi accepted. Thay đổi quyết định = tạo ADR mới với `supersedes: ADR-[NNN]`._
