# Product Design Harness Template

> Bộ công cụ và khuôn mẫu chuyên dụng cho pha Product Design kết hợp với AI Agents. Đi từ Ý tưởng -> Brainstorm -> Tài liệu (PRD/SRS) -> Mockup -> Handoff Package sẵn sàng cho đội ngũ (hoặc Agent) lập trình.

## 🤔 Tại sao cần Product Design Harness?

### ⚠️ Lời nguyền của "Vibecoding" (Code theo cảm hứng)
Khi làm việc với các AI Coding Agents, chúng ta thường có xu hướng đưa ra yêu cầu chung chung: *"Hãy code cho tôi app X"*. Cách tiếp cận **Vibecoding** này giúp thấy kết quả rất nhanh lúc đầu, nhưng nhanh chóng bộc lộ các "painpoints" (nỗi đau) chí mạng khi dự án lớn lên:
- **Lạc trôi Requirement**: Yêu cầu thay đổi liên tục, AI bị nhiễu context do nhớ nhớ quên quên, dẫn đến code chồng chéo, chắp vá (spaghetti code).
- **UI/UX thiếu nhất quán**: Giao diện phụ thuộc vào "cảm hứng" của AI tại từng thời điểm prompt. Không có Design System chuẩn mực, giao diện trông "phổ thông", chắp vá và thiếu chuyên nghiệp.
- **Nợ Kỹ thuật (Technical Debt) khổng lồ**: Bỏ qua bước phân tích kiến trúc, dẫn tới khi scale lên hoặc thêm tính năng phức tạp thì codebase gãy vỡ, đập đi xây lại.
- **Hallucination**: AI tự "bịa" ra business logic hoặc các tính năng không cần thiết mà không dựa trên bất kỳ nguồn tham chiếu nào.

### 💡 Giải pháp: Nhanh mà Chính xác
Để tận dụng tối đa sức mạnh của AI mà không rơi vào mớ hỗn độn, chúng ta cần tách bạch rõ ràng **Pha Thiết kế (Product Design)** và **Pha Lập trình (Implementation)**. 

**Product Design Harness** cung cấp một môi trường (với các prompts, skills và workflow cấu hình sẵn) để ép AI làm việc có kỷ luật:
1. **Tư duy Đa góc nhìn (Multi-Persona)**: Thay vì một "AI thợ gõ" chung chung, Agent trong repo này sẽ lần lượt đóng vai *Product Strategist* (thách thức ý tưởng), *UX Architect* (thiết kế luồng), *UI Engineer* (làm mockup), và *Spec Steward* (viết PRD/SRS).
2. **Citation-Enforced (Dẫn chứng bắt buộc)**: Mọi tính năng, luồng đi, hay dòng code mockup đều phải có truy xuất ngược (traceability) về một tài liệu gốc (PRD, Flow). Khắc phục triệt để tình trạng AI tự biên tự diễn.
3. **Đóng gói Handoff**: Output cuối cùng của repo này không phải là backend/database chắp vá, mà là **một bản thiết kế hoàn chỉnh nhất** (bao gồm Tài liệu Requirement, Mermaid Diagrams, và ReactJS Mockup tĩnh đã chạy thực tế). 

Gói handoff này sẽ đóng vai trò là "Kinh thánh" (Single Source of Truth) để giao cho Implementation team (hoặc một Coding Agent khác) code ra sản phẩm cuối cùng một cách **nhanh chóng, tự tin và chính xác tuyệt đối**.

## Khởi Tạo Dự Án Mới

Bạn có thể dễ dàng khởi tạo một repo thiết kế mới dựa trên template này bằng lệnh `npx`:

```bash
# Nếu publish trên npm:
npx create-pd-harness my-project

# Hoặc khởi tạo trực tiếp từ GitHub repository:
npx github:khanhbkqt/create-pd-harness my-project
```

Sau đó di chuyển vào thư mục dự án:
```bash
cd my-project
```

Tiếp theo, mở thư mục này trong **Antigravity IDE** (hoặc CLI) và gõ lệnh sau để bắt đầu định hình dự án với Agent:
```
/project-bootstrapping
```

## Cấu trúc Repo

```
├── AGENTS.md                          # Entrypoint cho Agent - chứa chỉ dẫn mệnh lệnh, indexing
├── .agents/
│   ├── skills/                        # Các kỹ năng chuyên biệt của Agent (Brainstorm, PRD, SRS, Mockup, TDD...)
│   └── workflows/                     # Các workflow vận hành (Feature Intake, Design Cycle, Review Gate, Handoff)
├── docs/
│   ├── decisions/                     # Architecture Decision Records (ADR)
│   ├── flows/                         # UserFlow / SystemFlow (Mermaid diagrams)
│   ├── prd/                           # Product Requirements Documents (PRD)
│   ├── srs/                           # Software Requirements Specifications (SRS)
│   ├── tdd/                           # Technical Design Documents (TDD)
│   ├── vision/                        # Vision & North Star Documents
│   └── GLOSSARY.md                    # Thuật ngữ dự án
├── mockups/                           # ReactJS design mockups (Atomic Design, Vanilla CSS)
└── handoff/                           # Gói handoff output cho team dev
```

## Cách Sử Dụng Cho Developer & Designer

### 1. Xem Quy Trình Làm Việc & Agent Setup
- Đọc [AGENTS.md](file:///Users/khanhnguyen/Projects/experimentals/repo-design/AGENTS.md) ở root để hiểu persona, workflow và các kỹ năng của AI Agents.
- Các template tài liệu nằm sẵn trong `docs/*/` dưới dạng các file `_TEMPLATE.md`.

### 2. Chạy Mockup UI (ReactJS + TypeScript + Vite)
Mockup được tổ chức theo pattern **Atomic Design** (atoms, molecules, organisms, templates, pages) và styling bằng **Vanilla CSS** (CSS Custom Properties).

Cài đặt và chạy môi trường phát triển local:
```bash
cd mockups
npm install
npm run dev
```

## Nguyên Tắc Vận Hành Core

1. **Persona Bias**: AI Agent đóng vai các chuyên gia khắt khe (`Product_Strategist`, `UX_Architect`, `UI_Engineer`, `Spec_Steward`, `Tech_Advisor`, `QA_Skeptic`).
2. **Do's over Don'ts**: Chỉ dẫn dạng hành động tích cực.
3. **Citation-Enforced**: Mọi phát biểu kỹ thuật, business logic, requirement phải kèm dẫn chứng `[Nguồn: tài_liệu, section]`.
4. **Context-Awareness**: Luôn SCAN trạng thái pipeline và cập nhật `Trạng thái Pipeline` trong các tài liệu thiết kế & implementation plan.
