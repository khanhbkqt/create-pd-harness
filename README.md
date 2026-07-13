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

## 🎨 Tích hợp Taste-Skill (UI/UX Best Practices)

Một trong những painpoints lớn nhất của AI là thiết kế giao diện (UI) rất cơ bản và rập khuôn. Repo này **tích hợp sẵn [taste-skill](https://github.com/v0-inc/taste-skill)** — một bộ kỹ năng và nguyên tắc thiết kế UI/UX nâng cao dành cho AI.

Nhờ `taste-skill`, các Mockup ReactJS được tạo ra bởi AI sẽ tự động tuân thủ:
- **Spacing & Typography chuẩn mực**: Sử dụng các hệ thống khoảng cách và font chữ hiện đại.
- **Color Palette hài hoà**: Tránh các màu cơ bản nguyên thủy, sử dụng các dải màu (scales) tinh tế.
- **Micro-interactions & Animations**: Tích hợp sẵn các hiệu ứng hover, transition mượt mà.
- **Thẩm mỹ cao cấp**: Đảm bảo giao diện trông chuyên nghiệp, "có gu" (tasteful) và sẵn sàng cho môi trường production.

## 🚀 Hướng Dẫn Sử Dụng (Quy Trình Chuẩn)

### Bước 1: Khởi Tạo Dự Án Mới

Bạn có thể khởi tạo một repo thiết kế mới dựa trên template này bằng `npx`:

```bash
# Sử dụng trực tiếp từ npm:
npx create-pd-harness my-project

# Hoặc khởi tạo từ GitHub repository:
npx github:khanhbkqt/create-pd-harness my-project
```

Sau đó di chuyển vào thư mục dự án:
```bash
cd my-project
```

### Bước 2: Bắt Đầu Định Hình (Bootstrapping)

Mở thư mục này trong IDE có hỗ trợ Agent (như **Antigravity IDE**) hoặc sử dụng CLI. Gõ lệnh sau để kích hoạt chu trình phân tích ban đầu:
```text
/project-bootstrapping
```
Agent sẽ phỏng vấn bạn bằng phương pháp Socratic để làm rõ tầm nhìn (Vision) và phạm vi MVP trước khi bắt tay vào thiết kế.

### Bước 3: Chu Trình Thiết Kế (Design Cycle)

Mỗi khi cần thiết kế một tính năng mới, bạn gọi lệnh:
```text
/feature-intake
```
Quy trình sẽ tự động diễn ra theo các bước nghiêm ngặt:
1. **Brainstorm & Viết PRD**: Xác định requirement.
2. **UserFlow**: Vẽ sơ đồ luồng (Mermaid).
3. **Mockup**: Code giao diện ReactJS + Vanilla CSS.
4. **TDD / SRS**: Viết tài liệu kỹ thuật và thiết kế hệ thống.
5. **Review Gate**: Kiểm tra chéo giữa các persona trước khi chốt.

### Bước 4: Chạy thử Mockup UI

Mockup được tổ chức theo pattern **Atomic Design** (atoms, molecules, organisms, templates, pages) và styling bằng **Vanilla CSS** (CSS Custom Properties).

Cài đặt và chạy môi trường phát triển local:
```bash
cd mockups
npm install
npm run dev
```

## 📦 Kết Quả Đầu Ra (Handoff Package)

Đầu ra của Product Design Harness không phải là một ứng dụng chạy thực tế với database, mà là **một Gói Bàn Giao (Handoff Package)**. Khi bạn chạy lệnh `/handoff-package`, toàn bộ kết quả sẽ được đóng gói lại trong thư mục `handoff/`.

Gói này bao gồm:
- **Mockup tĩnh hoàn thiện**: Code React/CSS thể hiện chính xác 100% giao diện và tương tác UI.
- **Spec Documents**: PRD (Yêu cầu sản phẩm), SRS (Đặc tả hệ thống), TDD (Thiết kế kỹ thuật).
- **Architecture Decisions**: Các quyết định kỹ thuật đã được chốt (ADRs).
- **Implementation Plan**: Kế hoạch chi tiết từng bước (Step-by-step) để đội ngũ Dev hoặc Coding Agent bắt tay vào lập trình backend/tích hợp.

> **💡 Lợi ích**: Với Handoff Package này, team Dev (hoặc Coding Agent ở repo Implementation) sẽ không cần phải đoán mò hay liên tục hỏi lại Requirement. Mọi thứ đã được chốt cứng và minh chứng rõ ràng!
> 
> **🚀 Next Step**: Từ tài liệu handoff này, bạn có thể tiếp tục sử dụng **Antigravity IDE** với lệnh `/teamwork-preview` (phân chia sub-agents) hoặc `/goal` (tự hành dài hạn) để Agent tiến hành viết code backend, tích hợp hệ thống và hoàn thành dự án ngay lập tức!

## 📂 Cấu trúc Repo

```
├── AGENTS.md                          # Entrypoint cho Agent - chứa chỉ dẫn mệnh lệnh, indexing
├── .agents/
│   ├── skills/                        # Các kỹ năng chuyên biệt của Agent (Brainstorm, PRD, Mockup...)
│   └── workflows/                     # Các workflow vận hành (Feature Intake, Design Cycle, Handoff)
├── docs/
│   ├── decisions/                     # Architecture Decision Records (ADR)
│   ├── flows/                         # UserFlow / SystemFlow (Mermaid diagrams)
│   ├── prd/                           # Product Requirements Documents (PRD)
│   ├── srs/                           # Software Requirements Specifications (SRS)
│   ├── tdd/                           # Technical Design Documents (TDD)
│   └── vision/                        # Vision & North Star Documents
├── mockups/                           # ReactJS design mockups (Atomic Design, Vanilla CSS)
├── taste-skill/                       # Bộ quy chuẩn UI/UX thẩm mỹ cao
└── handoff/                           # Thư mục chứa gói handoff cho team dev
```

## ⚙️ Nguyên Tắc Vận Hành Core

1. **Persona Bias**: AI Agent đóng vai các chuyên gia khắt khe (`Product_Strategist`, `UX_Architect`, `UI_Engineer`, `Spec_Steward`, `Tech_Advisor`, `QA_Skeptic`).
2. **Do's over Don'ts**: Chỉ dẫn dạng hành động tích cực.
3. **Citation-Enforced**: Mọi phát biểu kỹ thuật, business logic, requirement phải kèm dẫn chứng `[Nguồn: tài_liệu, section]`.
4. **Context-Awareness**: Luôn SCAN trạng thái pipeline và cập nhật `Trạng thái Pipeline` trong các tài liệu thiết kế & implementation plan.
