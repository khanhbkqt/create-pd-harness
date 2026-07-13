---
name: visual-wireframing
description: Phác thảo cấu trúc giao diện (Lo-fi Wireframe) để chốt bố cục trước khi code Mockup.
---

# Skill: Low-Fidelity Wireframing

## MỤC ĐÍCH
Đảm bảo sự thống nhất về cấu trúc layout, hierarchy, và các luồng tương tác chính trước khi `UI_Engineer` bắt tay vào viết code ReactJS (Atomic Design). Giảm thiểu change cost do sửa đổi layout.

## QUY TRÌNH THỰC THI

### 1. Phân tích Flow
Dựa trên `docs/flows/[feature].md`, xác định các màn hình (screens) cần thiết kế.
Mỗi màn hình cần trả lời:
- **Core Action**: Hành động chính user cần làm ở đây là gì?
- **Information Hierarchy**: Thông tin nào quan trọng nhất cần hiện to/trung tâm?
- **Navigation**: Làm sao user biết họ đang ở đâu và đi tiếp thế nào?

### 2. Khởi tạo Wireframe
Agent có thể tạo wireframe bằng 2 cách:

**Cách 1: ASCII Wireframe (Inline)**
Sử dụng markdown code block để phác thảo bố cục:

```text
+-------------------------------------------------+
| [Logo]       [Search Bar]         [Avatar/Menu] |
+-------------------------------------------------+
|  +---------+   +-----------------------------+  |
|  | Menu 1  |   |  TITLE (H1)                 |  |
|  | Menu 2  |   |                             |  |
|  | Menu 3  |   |  [Primary CTA Button]       |  |
|  +---------+   +-----------------------------+  |
+-------------------------------------------------+
```

**Cách 2: AI-Generated Image Mock (Nếu có tool)**
Sử dụng tool `generate_image` với prompt thiết kế lo-fi/hi-fi UI mockup (lưu vào artifacts) để trực quan hóa ý tưởng.

### 3. Review Gate cho Layout
`UX_Architect` đánh giá:
- Cognitive load có phù hợp không?
- Contrast và Hierarchy có dẫn dắt đúng luồng thao tác không?
- Trạng thái trống (Empty State), Lỗi (Error State) sẽ nằm ở đâu?

Chốt bố cục với user trước khi chuyển sang bước Mockup Design.
