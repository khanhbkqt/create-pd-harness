# Product Design Harness Template

> Repo template chuyên dụng cho pha Product Design. Brainstorm, thiết kế, làm tài liệu, mockup. Kết quả handoff sẵn sàng cho implementation team.

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
