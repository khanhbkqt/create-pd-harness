---
name: srs-writer
description: Viết Software Requirements Specification theo IEEE 830 và SDLC. Traceability matrix bắt buộc - mỗi SRS requirement trỏ ngược về PRD.
---

# Skill: SRS Writer (IEEE 830, SDLC-Compliant)

## KÍCH HOẠT

Khi PRD đã được approve (`status: approved`). VERIFY PRD tồn tại và đã approved trước khi bắt đầu.

## PERSONA ACTIVE: `Spec_Steward` + `Tech_Advisor`

Spec_Steward đảm bảo completeness. Tech_Advisor đảm bảo feasibility kỹ thuật.

## QUY TRÌNH

### Bước 1: Phân tích PRD

ĐỌC PRD target. LIỆT KÊ tất cả REQ-IDs và phân loại:
- Functional Requirements (FR)
- Non-Functional Requirements (NFR)
- Interface Requirements (IR)
- Data Requirements (DR)

### Bước 2: Viết SRS

TẠO file `docs/srs/[feature-name].md` theo template `docs/srs/_TEMPLATE.md`.

**Cấu trúc IEEE 830:**

```markdown
# 1. Giới thiệu
## 1.1 Mục đích
## 1.2 Phạm vi
## 1.3 Định nghĩa & Viết tắt (trỏ → GLOSSARY.md)
## 1.4 Tài liệu tham chiếu

# 2. Mô tả tổng quan
## 2.1 Bối cảnh sản phẩm
## 2.2 Chức năng chính
## 2.3 Đặc điểm người dùng
## 2.4 Ràng buộc
## 2.5 Giả định & Phụ thuộc

# 3. Yêu cầu cụ thể
## 3.1 Yêu cầu chức năng
## 3.2 Yêu cầu phi chức năng
## 3.3 Yêu cầu giao diện

# 4. Mô hình dữ liệu
## 4.1 Entity Relationship
## 4.2 Data Dictionary

# 5. Đặc tả giao diện ngoài
## 5.1 API Contracts
## 5.2 UI Wireframe References

# 6. Traceability Matrix
```

### Bước 3: Traceability Matrix

TẠO bảng truy ngược:

```markdown
| SRS ID | Loại | Mô tả tóm tắt | PRD REQ-ID | Trạng thái |
|---|---|---|---|---|
| FR-001 | Functional | [Mô tả] | REQ-001 | Draft |
| NFR-001 | Non-Functional | [Mô tả] | REQ-003 | Draft |
```

VERIFY: mỗi PRD REQ-ID xuất hiện ít nhất 1 lần trong matrix. Nếu thiếu → GHI RÕ "REQ-XXX chưa được map trong SRS".

### Bước 4: Format yêu cầu cụ thể

MỖI yêu cầu functional:

```markdown
### FR-[ID]: [Tên]
- **Truy ngược**: REQ-[ID] từ PRD
- **Mô tả**: [Chi tiết kỹ thuật]
- **Input**: [Dữ liệu đầu vào, format, constraints]
- **Processing**: [Logic xử lý]
- **Output**: [Kết quả mong đợi, format]
- **Error Handling**: [Các trường hợp lỗi và xử lý]
- **Performance**: [Thời gian phản hồi, throughput yêu cầu]
```

MỖI yêu cầu non-functional:

```markdown
### NFR-[ID]: [Tên]
- **Truy ngược**: REQ-[ID] từ PRD
- **Danh mục**: Performance | Security | Availability | Scalability | Usability
- **Metric**: [Đo lường cụ thể - ví dụ: "Response time < 200ms ở p95"]
- **Phương pháp đo**: [Công cụ/cách đo]
- **Baseline hiện tại**: [Nếu có, hoặc "CHƯA CÓ DỮ LIỆU"]
```

## FRONTMATTER

```yaml
---
title: "SRS: [Tên feature]"
status: draft | review | approved
version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Spec_Steward
source_prd: docs/prd/[feature-name].md
linked_docs:
  - docs/prd/[feature-name].md
  - docs/tdd/[feature-name].md
  - docs/flows/[flow-name].md
sdlc_phase: analysis
---
```

## QUY TẮC

1. MỖI FR format: `FR-[3 chữ số]` (FR-001...)
2. MỖI NFR format: `NFR-[3 chữ số]` (NFR-001...)
3. MỖI interface requirement format: `IR-[3 chữ số]`
4. MỖI data requirement format: `DR-[3 chữ số]`
5. TRACEABILITY MATRIX bắt buộc - không có ngoại lệ
6. TRÍCH NGUYÊN VĂN PRD requirement cho mỗi truy ngược
7. GHI "CHƯA CÓ DỮ LIỆU" khi metric chưa xác định
8. CẬP NHẬT GLOSSARY khi xuất hiện thuật ngữ kỹ thuật mới

## CHUYỂN GIAO

→ SRS approved → Input cho TDD Writer
→ SRS là reference cho: Mockup Designer (UI specs), Flow Designer (behavior specs)
