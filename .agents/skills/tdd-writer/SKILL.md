---
name: tdd-writer
description: Viết Technical Design Document. Architecture overview, component design, data model, API design, security, performance. Trade-off analysis bắt buộc.
---

# Skill: TDD Writer (Technical Design Document)

## KÍCH HOẠT

Khi SRS đã approve và Decision Records liên quan đã ghi. VERIFY cả 2 tồn tại.

## PERSONA ACTIVE: `Tech_Advisor` + `Spec_Steward`

Tech_Advisor dẫn dắt technical decisions. Spec_Steward đảm bảo documentation completeness.

## QUY TRÌNH

### Bước 1: Thu thập Input

SCAN và GHI NHẬN:
- SRS: `docs/srs/[feature-name].md` → FR-IDs, NFR-IDs
- ADRs: `docs/decisions/` → Quyết định kiến trúc đã accepted
- Flows: `docs/flows/` → System interactions
- Mockups: `mockups/src/` → Component structure (nếu có)
- Existing TDDs: `docs/tdd/` → Tránh contradiction

### Bước 2: Viết TDD

TẠO file `docs/tdd/[feature-name].md`:

```markdown
---
title: "TDD: [Tên feature]"
status: draft | review | approved
version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Tech_Advisor
source_srs: docs/srs/[feature-name].md
linked_docs:
  - docs/srs/[feature-name].md
  - docs/decisions/[relevant-adrs].md
  - docs/flows/[relevant-flows].md
sdlc_phase: design
---

# Technical Design: [Tên feature]

## 1. Tổng quan kiến trúc

### 1.1 Context Diagram
[Mermaid C4 context diagram]

### 1.2 Tương tác với hệ thống hiện có
[Mô tả integration points]
[Nguồn: SRS Section 2.1, "trích nguyên văn"]

## 2. Component Design

### 2.1 Component Diagram
[Mermaid component diagram]

### 2.2 Chi tiết từng Component

#### Component: [Tên]
- **Trách nhiệm**: [Single responsibility]
- **Interface**: [Public API]
- **Dependencies**: [Components phụ thuộc]
- **Data Flow**: [Input → Processing → Output]
- **SRS Reference**: FR-[IDs]

## 3. Data Model

### 3.1 Entity Relationship Diagram
[Mermaid ER diagram]

### 3.2 Data Dictionary
| Entity | Field | Type | Constraints | Mô tả |
|---|---|---|---|---|
| [Entity] | [Field] | [Type] | [NOT NULL, UNIQUE...] | [Mô tả] |

### 3.3 Migration Strategy
[Cách migrate từ schema hiện tại, nếu có]

## 4. API Design

### 4.1 Endpoints
| Method | Path | Mô tả | Request | Response | SRS Ref |
|---|---|---|---|---|---|
| POST | /api/[resource] | [Mô tả] | [Schema] | [Schema] | FR-[ID] |

### 4.2 Error Codes
| Code | Mô tả | Client Action |
|---|---|---|
| 400 | [Bad Request detail] | [Hiển thị validation error] |
| 401 | [Unauthorized detail] | [Redirect login] |

## 5. Security

### 5.1 Authentication & Authorization
[Strategy, reference ADR nếu có]

### 5.2 Data Protection
[Encryption at rest, in transit]

### 5.3 Input Validation
[Validation rules per endpoint]

## 6. Performance

### 6.1 Performance Budget
| Metric | Target | Baseline | SRS Ref |
|---|---|---|---|
| Response Time (p95) | < 200ms | [Hiện tại] | NFR-[ID] |
| Throughput | [X] req/s | [Hiện tại] | NFR-[ID] |

### 6.2 Caching Strategy
[Cache layers, TTL, invalidation]

### 6.3 Scalability Plan
[Horizontal/vertical, bottleneck analysis]

## 7. Trade-off Analysis

### Trade-off 1: [Tên]
| Tiêu chí | Option A | Option B |
|---|---|---|
| Performance | [Rating + evidence] | [Rating + evidence] |
| Complexity | [Rating + evidence] | [Rating + evidence] |
| Maintainability | [Rating + evidence] | [Rating + evidence] |

**Quyết định**: [Option chọn] - [Lý do, reference ADR-NNN]

## 8. Monitoring & Observability

### 8.1 Metrics
[Key metrics cần track]

### 8.2 Logging
[Log levels, structured logging format]

### 8.3 Alerting
[Alert conditions, thresholds]

## 9. Deployment

### 9.1 Deployment Strategy
[Blue-green / canary / rolling]

### 9.2 Rollback Plan
[Steps rollback khi có lỗi]

### 9.3 Feature Flags
[Flags cần thiết, default state]
```

### Bước 3: Trade-off Analysis (bắt buộc)

MỖI design decision PHẢI có trade-off analysis:
- Minimum 2 options
- Scoring theo ít nhất 3 tiêu chí
- Evidence cho mỗi score (benchmark, reference, ADR)
- Kết luận rõ ràng với lý do

### Bước 4: Cross-reference Check

VERIFY:
- Mỗi component trỏ về FR-IDs trong SRS ✓
- Mỗi trade-off trỏ về ADR-IDs ✓
- Data model match với SRS Section 4 ✓
- API design match với SRS Section 5 ✓
- Performance targets match NFR-IDs ✓

## QUY TẮC

1. TRADE-OFF ANALYSIS bắt buộc cho mỗi design decision
2. MERMAID diagrams cho architecture, components, data model
3. CITATION: trỏ về SRS FRs/NFRs và ADRs cho mỗi section
4. PERFORMANCE BUDGET dựa trên NFR metrics cụ thể
5. SECURITY section bắt buộc - không bỏ qua
6. GHI "CHƯA CÓ DỮ LIỆU" khi baseline metrics chưa có

## CHUYỂN GIAO

→ TDD approved → Input cho Handoff Package
→ TDD là reference cho: Implementation team (primary technical guide)
