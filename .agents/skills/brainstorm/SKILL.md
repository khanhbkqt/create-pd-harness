---
name: brainstorm
description: Phân tích yêu cầu tính năng mới bằng Socratic method. Challenge assumptions từ nhiều góc nhìn chuyên gia. Output Feature Brief có cấu trúc.
---

# Skill: Brainstorm & Challenge Assumptions

## KÍCH HOẠT

Khi user đưa ra yêu cầu tính năng mới, ý tưởng, hoặc vấn đề cần giải quyết.

## QUY TRÌNH

### Bước 1: Tiếp nhận & Phân loại

PARSE yêu cầu của user thành:
- **Vấn đề gốc**: User đang cố giải quyết điều gì?
- **Giải pháp đề xuất**: User đang gợi ý hướng nào (nếu có)?
- **Ngữ cảnh ngầm**: Những giả định user đang mặc nhiên chấp nhận?

### Bước 2: Socratic Challenge (3-5 câu hỏi)

ĐẶT nhiều câu hỏi thách thức, mỗi câu từ một góc nhìn persona cho đến khi clear các vấn đề:

**Product_Strategist** hỏi:
- "Nhóm user nào hưởng lợi trực tiếp? Quy mô nhóm đó bao nhiêu?"
- "Feature này tạo revenue trực tiếp, giữ chân user, hay giảm chi phí vận hành?"
- "Nếu bỏ feature này, user sẽ chuyển sang giải pháp thay thế nào?"

**UX_Architect** hỏi:
- "User hiện tại đang hoàn thành task này bằng cách nào? Bao nhiêu bước?"
- "Cognitive load tăng thêm bao nhiêu? User cần học thêm concept mới nào?"
- "Edge case nào phổ biến nhất trong hành trình này?"

**Tech_Advisor** hỏi:
- "Giải pháp này scale tới 10x load hiện tại được chưa?"
- "Dependency mới nào được đưa vào? Rủi ro kỹ thuật của từng dependency?"
- "Latency budget cho feature này bao nhiêu ms?"

### Bước 3: Tổng hợp Multi-Persona

SAU KHI user trả lời (hoặc sau khi phân tích đủ context), tổng hợp từ 3 góc nhìn:

```markdown
## Phân tích đa chiều

### Góc nhìn Business (Product_Strategist)
[Phân tích ROI, market fit, priority]
[Nguồn: user_statement, section X]

### Góc nhìn UX (UX_Architect)
[Phân tích user journey, cognitive load, accessibility]
[Nguồn: user_statement, section Y]

### Góc nhìn Kỹ thuật (Tech_Advisor)
[Phân tích feasibility, constraints, risks]
[Nguồn: user_statement, section Z]
```

### Bước 4: Output Feature Brief

TẠO Feature Brief theo format:

```markdown
---
title: [Tên feature]
status: draft
created: [YYYY-MM-DD]
author: brainstorm-session
priority: [P0/P1/P2/P3]
linked_docs: []
---

# Feature Brief: [Tên feature]

## Vấn đề
[Mô tả vấn đề gốc. Citation-enforced: trích nguyên văn từ user request.]

## Đối tượng
[User personas bị ảnh hưởng. Quy mô.]

## Giải pháp đề xuất
[Mô tả giải pháp ở mức high-level.]

## Giá trị mang lại
[Business value cụ thể. Metrics đo lường.]

## Phạm vi
### Bao gồm
- [Item 1]
### Loại trừ
- [Item 1]

## Rủi ro & Giả định
| # | Nội dung | Loại | Mức độ | Biện pháp |
|---|---|---|---|---|
| 1 | [Nội dung] | Rủi ro/Giả định | Cao/TB/Thấp | [Biện pháp] |

## Câu hỏi mở
- [ ] [Câu hỏi chưa được trả lời]

## Bước tiếp theo
→ Chuyển sang PRD Writer khi tất cả câu hỏi mở được giải quyết.
```

## QUY TẮC

1. TRÍCH NGUYÊN VĂN lời user vào dấu ngoặc kép làm dẫn chứng
2. GHI RÕ "CHƯA CÓ DỮ LIỆU" khi thiếu thông tin, kèm câu hỏi cụ thể để thu thập
3. PHÂN TÍCH từ ít nhất 3 góc nhìn persona trước khi kết luận
4. MỖI kết luận kèm `[Nguồn: ...]`
