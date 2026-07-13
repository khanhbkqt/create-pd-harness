---
name: decision-logger
description: Ghi Architecture Decision Records (ADR). Mỗi quyết định thiết kế quan trọng được lưu trữ với context, alternatives, consequences. Citation-enforced.
---

# Skill: Decision Logger (ADR)

## KÍCH HOẠT

Khi xuất hiện quyết định thiết kế quan trọng trong bất kỳ phase nào. Trigger conditions:
- Chọn giữa 2+ giải pháp kỹ thuật
- Trade-off rõ ràng (ví dụ: performance vs. simplicity)
- Thay đổi giả định ban đầu
- Phản bác requirement từ PRD với lý do kỹ thuật

## PERSONA ACTIVE: `Tech_Advisor` + `Spec_Steward`

Tech_Advisor phân tích trade-offs. Spec_Steward đảm bảo documentation quality.

## QUY TRÌNH

### Bước 1: Xác định quyết định

PHÁT BIỂU quyết định dưới dạng câu hỏi:
- "Sử dụng [X] hay [Y] cho [mục đích]?"
- "Tách [component] thành microservice hay giữ monolith?"

### Bước 2: Viết ADR

TẠO file `docs/decisions/[NNN]-[title-kebab-case].md` theo template.

NNN = số thứ tự 3 chữ số, tăng dần (001, 002, 003...).

SCAN `docs/decisions/` để xác định số tiếp theo.

### Bước 3: Phân tích Alternatives

MỖI alternative phải có:
- Mô tả giải pháp
- Ưu điểm (với dẫn chứng)
- Nhược điểm (với dẫn chứng)
- Ảnh hưởng tới các requirements cụ thể (trỏ REQ-IDs)

CITATION: trích nguồn cho mỗi claim kỹ thuật. Nếu claim dựa trên kinh nghiệm chung → ghi "Best practice, industry standard". Nếu claim dựa trên benchmark cụ thể → trích nguồn benchmark.

## FORMAT ADR

```markdown
---
id: ADR-[NNN]
title: [Tiêu đề quyết định]
status: proposed | accepted | deprecated | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
deciders: [Personas tham gia]
linked_reqs: [REQ-IDs liên quan]
supersedes: [ADR-ID nếu có]
superseded_by: [ADR-ID nếu có]
---

# ADR-[NNN]: [Tiêu đề]

## Bối cảnh
[Tình huống dẫn đến quyết định. Trích dẫn requirements liên quan.]
[Nguồn: PRD docs/prd/[file], REQ-XXX]

## Quyết định
[Phát biểu quyết định rõ ràng, 1-2 câu.]

## Các phương án đã xem xét

### Phương án A: [Tên]
- **Ưu điểm**: [Liệt kê, kèm nguồn]
- **Nhược điểm**: [Liệt kê, kèm nguồn]
- **Ảnh hưởng**: [REQ-IDs bị tác động]

### Phương án B: [Tên]
- **Ưu điểm**: [Liệt kê, kèm nguồn]
- **Nhược điểm**: [Liệt kê, kèm nguồn]
- **Ảnh hưởng**: [REQ-IDs bị tác động]

## Hệ quả

### Tích cực
- [Hệ quả tốt]

### Tiêu cực
- [Hệ quả cần chấp nhận]

### Rủi ro
- [Rủi ro và biện pháp giảm thiểu]

## Liên kết
- PRD: [link]
- SRS: [link]
- Related ADRs: [links]
```

## QUY TẮC

1. MỖI ADR là immutable sau khi accepted - chỉ supersede bằng ADR mới
2. MINIMUM 2 alternatives cho mỗi quyết định
3. CITATION bắt buộc cho mỗi claim kỹ thuật
4. LINKED_REQS bắt buộc - quyết định nào cũng liên quan tới requirement
5. STATUS transitions: proposed → accepted | deprecated; accepted → superseded
6. CẬP NHẬT AGENTS.md index khi có ADR mới
7. ĐỒNG BỘ TRẠNG THÁI:
   - Chạy `python scripts/pdt.py status --update`
   - Chạy `python scripts/pdt.py log --add "Tạo quyết định thiết kế ADR-[NNN]" --artifact "Decisions"`

## CHUYỂN GIAO

→ ADR accepted → Ảnh hưởng tới TDD Writer (architecture decisions)
→ ADR là reference cho: SRS (constraints), Handoff (design rationale)
