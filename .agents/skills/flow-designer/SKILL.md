---
name: flow-designer
description: Thiết kế UserFlow và SystemFlow bằng Mermaid diagrams. Mỗi flow có happy path + error paths. Truy ngược về PRD requirements.
---

# Skill: Flow Designer (UserFlow / SystemFlow)

## KÍCH HOẠT

Khi PRD đã approve và cần visualize hành trình user hoặc tương tác hệ thống.

## PERSONA ACTIVE: `UX_Architect` + `QA_Skeptic`

UX_Architect thiết kế happy path tối ưu. QA_Skeptic thách thức mọi edge case.

## QUY TRÌNH

### Bước 1: Xác định loại flow

| Loại | Mục đích | Notation |
|---|---|---|
| UserFlow | Hành trình user qua các screen/action | Mermaid flowchart |
| SystemFlow | Tương tác giữa services/components | Mermaid sequence diagram |
| StateFlow | Trạng thái của entity qua lifecycle | Mermaid state diagram |

### Bước 2: Thiết kế Happy Path

TỪ PRD requirements, XÂY DỰNG luồng chính:
- Mỗi node = 1 hành động hoặc 1 screen
- Mỗi edge = 1 transition rõ ràng
- Maximum 10 nodes cho happy path (nếu vượt → tách thành sub-flows)

### Bước 3: Thêm Error Paths (QA_Skeptic)

MỖI flow PHẢI có minimum 2 error paths:

QA_Skeptic challenge:
- "Nếu network timeout tại bước N?"
- "Nếu validation fail tại bước N?"
- "Nếu user quay lại bước trước?"
- "Nếu session hết hạn giữa chừng?"
- "Nếu concurrent request xảy ra?"

### Bước 4: Viết Mermaid Diagram

**UserFlow example:**
```mermaid
flowchart TD
    A["User mở trang Login"] --> B{"Đã có tài khoản?"}
    B -->|Có| C["Nhập email + password"]
    B -->|Chưa| D["Chuyển trang Register"]
    C --> E{"Validation OK?"}
    E -->|OK| F["Gọi API /auth/login"]
    E -->|Fail| G["Hiển thị lỗi validation"]
    G --> C
    F --> H{"Response status?"}
    H -->|200| I["Redirect tới Dashboard"]
    H -->|401| J["Hiển thị 'Sai thông tin đăng nhập'"]
    H -->|500| K["Hiển thị 'Lỗi hệ thống, thử lại sau'"]
    J --> C
    K --> C
```

**SystemFlow example:**
```mermaid
sequenceDiagram
    participant U as User
    participant FE as Frontend
    participant API as API Gateway
    participant Auth as Auth Service
    participant DB as Database

    U->>FE: Submit login form
    FE->>FE: Validate input (client-side)
    FE->>API: POST /auth/login
    API->>Auth: Verify credentials
    Auth->>DB: Query user record
    DB-->>Auth: User data
    Auth-->>API: JWT token
    API-->>FE: 200 + token
    FE->>FE: Store token, redirect
```

### Bước 5: Document Flow

TẠO file `docs/flows/[flow-name].md`:

```markdown
---
title: "[Tên flow]"
type: userflow | systemflow | stateflow
status: draft | review | approved
created: YYYY-MM-DD
linked_reqs: [REQ-IDs]
linked_screens: [Mockup page names]
---

# [Tên Flow]

## Mô tả
[1-2 câu mô tả mục đích flow]
[Nguồn: PRD REQ-XXX, "trích nguyên văn requirement"]

## Actors
- [Actor 1]: [Vai trò]
- [Actor 2]: [Vai trò]

## Preconditions
- [Điều kiện tiên quyết 1]
- [Điều kiện tiên quyết 2]

## Happy Path
[Mermaid diagram]

## Error Paths
### Error Path 1: [Tên]
[Mermaid diagram hoặc mô tả]

### Error Path 2: [Tên]
[Mermaid diagram hoặc mô tả]

## Postconditions
- [Kết quả khi hoàn thành]

## Liên kết
- PRD: [REQ-IDs]
- Mockup screens: [Pages]
- SRS: [FR-IDs]
```

## QUY TẮC

1. MỖI flow minimum: 1 happy path + 2 error paths
2. MAXIMUM 10 nodes trên happy path - tách sub-flow nếu vượt
3. MỖI node có label rõ ràng, dạng hành động ("User nhấn nút X", "System gọi API Y")
4. TRÍCH DẪN PRD requirement cho mỗi flow
5. LIÊN KẾT tới mockup screens tương ứng
6. MERMAID syntax valid - test render trước khi commit
7. QA_Skeptic PHẢI review và thêm edge cases

## CHUYỂN GIAO

→ Flows approved → Input cho Mockup Designer (screen mapping)
→ Flows là reference cho: SRS (behavior specs), TDD (interaction sequences)
