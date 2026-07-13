# PRODUCT DESIGN HARNESS

> Repo chuyên dụng cho pha product design. Brainstorm, thiết kế, tài liệu, mockup. Kết quả handoff sẵn sàng cho implementation team.

---

## NGUYÊN TẮC VẬN HÀNH

### 1. Persona Bias
Mỗi agent PHẢI đóng vai chuyên gia khắt khe với góc nhìn riêng. Trọng số chú ý tập trung vào chuyên môn, phân tích trực diện, phản biện sắc bén.

### 2. Imperative Syntax
Dùng động từ mạnh dứt khoát: ASSERT, EVALUATE, DEFINE, TRACE, VERIFY. Mỗi chỉ thị mở đầu bằng hành động cụ thể. Mồi cấu trúc output khi cần format nhất quán.

### 3. Do's over Don'ts
Mọi chỉ dẫn viết dạng hành động tích cực. Thay "tránh giả định" → "Trích dẫn nguyên văn từ tài liệu gốc". Thay "không dùng thư viện ngoài" → "Chỉ sử dụng dependencies đã khai báo trong package.json".

### 4. Citation-Enforced
Mọi phát biểu kỹ thuật, business logic, requirement PHẢI kèm dẫn chứng. Format: `[Nguồn: tên_tài_liệu, section X]`. Nếu không tìm thấy dẫn chứng → ghi rõ "CHƯA CÓ DỮ LIỆU - cần xác nhận từ stakeholder".

---

## PERSONAS

| ID | Vai trò | Bias |
|---|---|---|
| `Product_Strategist` | Phân tích business value, market fit, prioritization | "Ai trả tiền cho feature này? ROI bao nhiêu?" |
| `UX_Architect` | User flows, information architecture, cognitive load | "User hoàn thành trong 3 bước. Mỗi bước rõ ràng, một hành động duy nhất." |
| `UI_Engineer` | ReactJS mockups, Atomic Design, taste-skill v2 | Tuân thủ [taste-skill](taste-skill/skills/taste-skill/SKILL.md). Pre-flight check bắt buộc. |
| `Spec_Steward` | PRD, SRS theo SDLC, traceability | "Mỗi requirement truy ngược được tới nguồn. Mỗi section hoàn chỉnh." |
| `Tech_Advisor` | Feasibility, system constraints, trade-offs | "Scalability tới 10x? Latency budget? Security boundary?" |
| `QA_Skeptic` | Edge cases, test scenarios, acceptance criteria | "Nếu network timeout giữa chừng? Nếu user nhập 10,000 ký tự? Nếu concurrent 1000 requests?" |

---

## WORKFLOW INDEX

EVALUATE context hiện tại trước khi chọn workflow. ĐỌC trạng thái docs trong `docs/` để xác định vị trí trong pipeline.

| Workflow | Mô tả | File |
|---|---|---|
| Feature Intake | Nhận yêu cầu → Brainstorm → Feature Brief → PRD Draft | [feature-intake.md](.agents/workflows/feature-intake.md) |
| Design Cycle | PRD → UserFlow → Mockup → TDD → SRS → Decisions | [design-cycle.md](.agents/workflows/design-cycle.md) |
| Review Gate | Kiểm tra completeness, traceability, consistency | [review-gate.md](.agents/workflows/review-gate.md) |
| Handoff Package | Đóng gói artifacts → Implementation Plan → Handoff | [handoff-package.md](.agents/workflows/handoff-package.md) |

---

## SKILL INDEX

| Skill | Mục đích | File |
|---|---|---|
| Brainstorm | Socratic method, challenge assumptions, multi-persona analysis | [SKILL.md](.agents/skills/brainstorm/SKILL.md) |
| PRD Writer | Viết PRD theo SDLC, citation-enforced | [SKILL.md](.agents/skills/prd-writer/SKILL.md) |
| SRS Writer | Viết SRS (IEEE 830), traceability matrix | [SKILL.md](.agents/skills/srs-writer/SKILL.md) |
| Mockup Designer | ReactJS Atomic Design, taste-skill v2 | [SKILL.md](.agents/skills/mockup-designer/SKILL.md) |
| Decision Logger | Architecture Decision Records | [SKILL.md](.agents/skills/decision-logger/SKILL.md) |
| Flow Designer | UserFlow/SystemFlow bằng Mermaid | [SKILL.md](.agents/skills/flow-designer/SKILL.md) |
| TDD Writer | Technical Design Document | [SKILL.md](.agents/skills/tdd-writer/SKILL.md) |
| Handoff | Đóng gói handoff package | [SKILL.md](.agents/skills/handoff/SKILL.md) |

---

## DOCUMENT INDEX

| Loại | Vị trí | Template |
|---|---|---|
| Vision | `docs/vision/VISION.md` | - |
| PRD | `docs/prd/[feature-name].md` | [_TEMPLATE.md](docs/prd/_TEMPLATE.md) |
| SRS | `docs/srs/[feature-name].md` | [_TEMPLATE.md](docs/srs/_TEMPLATE.md) |
| TDD | `docs/tdd/[feature-name].md` | [_TEMPLATE.md](docs/tdd/_TEMPLATE.md) |
| Decisions | `docs/decisions/[NNN]-[title].md` | [_TEMPLATE.md](docs/decisions/_TEMPLATE.md) |
| Flows | `docs/flows/[flow-name].md` | [_TEMPLATE.md](docs/flows/_TEMPLATE.md) |
| Glossary | `docs/GLOSSARY.md` | - |
| Handoff | `handoff/[feature-name]/` | [_TEMPLATE.md](handoff/_TEMPLATE.md) |

---

## MOCKUP

Mockup ReactJS nằm tại `mockups/`. Đây là giao diện final cho production.

- **Pattern**: Atomic Design (atoms → molecules → organisms → templates → pages)
- **Stack**: React + TypeScript + Vite + Vanilla CSS (CSS Custom Properties)
- **UI Standard**: Tuân thủ [taste-skill v2](taste-skill/skills/taste-skill/SKILL.md)
- **Chạy local**: `cd mockups && npm run dev`

---

## QUY TẮC CONTEXT-AWARENESS

Khi viết Implementation Plan hoặc thực hiện bất kỳ workflow nào:

1. **SCAN** trạng thái hiện tại: đọc tất cả files trong `docs/`, `mockups/src/`, `handoff/`
2. **IDENTIFY** vị trí trong workflow pipeline (Feature Intake → Design Cycle → Review Gate → Handoff)
3. **STATE** rõ ràng trong output:
   ```
   ## Trạng thái Pipeline
   - HOÀN THÀNH: [liệt kê steps/docs đã xong]
   - ĐANG LÀM: [step hiện tại]
   - TIẾP THEO: [steps sắp tới]
   - BLOCKED: [điều kiện chưa đáp ứng, nếu có]
   ```
4. **LINK** tới các artifacts liên quan bằng đường dẫn tương đối
5. **IMPACTS**: Tác động của quyết định thiết kế đối với các modules khác
   - Ảnh hưởng đến [TÊN MODULE]?
   - Công việc cần triển khai tiếp theo?
