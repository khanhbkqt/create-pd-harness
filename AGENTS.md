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

### 5. Sub-Agent Orchestration
Nếu environment làm việc có hỗ trợ tính năng sub-agents, BẮT BUỘC ưu tiên sử dụng mô hình orchestrator: phân rã công việc lớn và điều phối các sub-agents đóng vai các Persona khác nhau để xử lý các tác vụ một cách độc lập và song song.

### 6. Human-In-The-Loop (HITL)
Tại các điểm nút quan trọng (Gate Reviews, Handoff, Transition giữa các phase), Agent KHÔNG ĐƯỢC tự ý vượt qua (Proceed) mà BẮT BUỘC phải dừng lại, báo cáo kết quả và đợi Explicit Approval từ người dùng/stakeholder.

---

## QUY TẮC CONTEXT-AWARENESS & TRACKING

Trước khi thực hiện bất kỳ workflow hoặc task nào:

1. **CHECK STATUS**: Chạy `python scripts/pdt.py status` để kiểm tra trạng thái hiện tại của toàn bộ artifacts.
2. **CHECK PRIORITIES**: Chạy `python scripts/pdt.py priority` để xem các công việc tiếp theo có độ ưu tiên cao nhất.
3. **CHECK SYNC**: Chạy `python scripts/pdt.py sync` để đảm bảo không có sync issues/stale dependencies nào đang tồn tại. Nếu có, kích hoạt [Sync Check](.agents/workflows/sync-check.md) workflow.
4. **STATE** rõ ràng trạng thái dự án trong output:
   ```markdown
   ### Trạng thái Artifacts (Từ STATUS.md)
   | Artifact | Status | Completeness | Dependencies |
   |---|---|---|---|
   | [Tên] | [Status] | [Done/Total] | [Met/Unmet] |
   ```
5. **LOG ACTION**: Sau khi hoàn thành tạo/sửa bất kỳ artifact nào, chạy `python scripts/pdt.py log --add "[Message]" --artifact [Tên]` để ghi lại hoạt động.
6. **UPDATE STATUS HUB**: Chạy `python scripts/pdt.py status --update` để đồng bộ trạng thái vào `docs/STATUS.md`.

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
| `Data_Analyst` | Phân tích dữ liệu, tracking events, telemetry | "Chúng ta đo lường thành công của feature này bằng events gì trên Mixpanel?" |

---

## WORKFLOW INDEX

EVALUATE context hiện tại trước khi chọn workflow. ĐỌC trạng thái docs trong `docs/` để xác định vị trí trong pipeline.

| Workflow | Mô tả | File |
|---|---|---|
| Project Bootstrapping | Nhận ý tưởng lớn → Socratic Challenge → Product Vision → Feature Roadmap | [project-bootstrapping.md](.agents/workflows/project-bootstrapping.md) |
| Feature Intake | Nhận yêu cầu → Brainstorm → Feature Brief → PRD Draft | [feature-intake.md](.agents/workflows/feature-intake.md) |
| Design Cycle | PRD → Flow → Wireframe → Mockup → Usability Test → TDD/SRS → Gate | [design-cycle.md](.agents/workflows/design-cycle.md) |
| Review Gate | Kiểm tra completeness, traceability, consistency | [review-gate.md](.agents/workflows/review-gate.md) |
| Sync Check | Đồng bộ và cập nhật khi có artifact thay đổi | [sync-check.md](.agents/workflows/sync-check.md) |
| Handoff Package | Đóng gói artifacts → Implementation Plan → Handoff | [handoff-package.md](.agents/workflows/handoff-package.md) |

---

## SKILL INDEX

| Skill | Mục đích | File |
|---|---|---|
| Project Bootstrapping | Phân tích và hoàn thiện tầm nhìn dự án (VISION) | [SKILL.md](.agents/skills/project-bootstrapping/SKILL.md) |
| Competitor Analysis | Phân tích, benchmarking đối thủ cạnh tranh | [SKILL.md](.agents/skills/competitor-analysis/SKILL.md) |
| Brainstorm | Socratic method, challenge assumptions, multi-persona analysis | [SKILL.md](.agents/skills/brainstorm/SKILL.md) |
| PRD Writer | Viết PRD theo SDLC, citation-enforced | [SKILL.md](.agents/skills/prd-writer/SKILL.md) |
| SRS Writer | Viết SRS (IEEE 830), traceability matrix | [SKILL.md](.agents/skills/srs-writer/SKILL.md) |
| Visual Wireframing | Phác thảo Lo-fi wireframe chốt bố cục | [SKILL.md](.agents/skills/visual-wireframing/SKILL.md) |
| Mockup Designer | ReactJS Atomic Design, taste-skill v2 | [SKILL.md](.agents/skills/mockup-designer/SKILL.md) |
| Usability Testing | Chạy thử nghiệm trải nghiệm UX trên Mockup | [SKILL.md](.agents/skills/usability-testing/SKILL.md) |
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
| Design System | `docs/DESIGN_SYSTEM.md` | [_TEMPLATE.md](docs/DESIGN_SYSTEM.md) |
| Handoff | `handoff/[feature-name]/` | [_TEMPLATE.md](handoff/_TEMPLATE.md) |

---

## MOCKUP

Mockup ReactJS nằm tại `mockups/`. Đây là giao diện final cho production.

- **Design Tokens**: Toàn bộ quy chuẩn về màu sắc, font, spacing, shadow PHẢI được định nghĩa tại `docs/DESIGN_SYSTEM.md` làm Single Source of Truth, và import vào file CSS gốc.
- **Pattern**: Atomic Design (atoms → molecules → organisms → templates → pages)
- **Stack**: React + TypeScript + Vite + Vanilla CSS (CSS Custom Properties)
- **UI Standard**: Tuân thủ [taste-skill v2](taste-skill/skills/taste-skill/SKILL.md)
- **Chạy local**: `cd mockups && npm run dev`
