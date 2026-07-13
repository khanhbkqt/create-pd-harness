---
name: project-bootstrapping
description: Khởi tạo định hướng dự án thông qua Strategic Socratic Challenge và hoàn thiện Product Vision.
---

# Skill: Project Bootstrapping

## MỤC ĐÍCH
Xử lý các ý tưởng ở mức độ dự án/sản phẩm lớn, xác định đúng Product-Market Fit và thiết lập tài liệu `VISION.md` trước khi đi vào phân rã tính năng chi tiết.

## QUY TRÌNH THỰC THI

### Bước 1: Parse ý tưởng dự án
Khi user cung cấp thông tin, agent cần phân tách rạch ròi:
- Vấn đề cốt lõi muốn giải quyết.
- Đối tượng khách hàng mục tiêu.
- Giải pháp hoặc công nghệ định hướng.

### Bước 2: Strategic Socratic Challenge
Kích hoạt 3 persona chính để chất vấn user:

**Product_Strategist**:
- Mô hình kinh doanh của dự án này là gì (B2B, B2C, SaaS)?
- North Star Metric là gì (Ví dụ: Số user kích hoạt, Doanh thu/khách hàng)?
- Đối thủ cạnh tranh trực tiếp lớn nhất là ai? Tại sao họ chưa giải quyết tốt vấn đề này?

**UX_Architect**:
- 3 Nguyên tắc thiết kế cốt lõi (Design Principles) của dự án này là gì?
- Hành trình người dùng vĩ mô (Macro User Journey) từ lúc biết đến sản phẩm đến khi sử dụng thành công mất bao lâu?

**Tech_Advisor**:
- Mức độ chịu tải (Scalability) và bảo mật (Security) yêu cầu ở mức nào ngay từ Phase 1?
- Có những External Integrations (API bên thứ 3) nào mang tính sống còn?

### Bước 3: Biên soạn `VISION.md`
Dựa trên câu trả lời, sử dụng file `docs/vision/VISION.md` (nếu chưa có thì tạo mới theo template chuẩn của framework) để điền vào 9 mục lớn:
1. Tầm nhìn sản phẩm
2. North Star Metric
3. Đối tượng mục tiêu
4. Vấn đề cốt lõi
5. Giải pháp đề xuất (High-level)
6. Nguyên tắc thiết kế sản phẩm
7. Phạm vi MVP
8. Thị trường & Đối thủ
9. Rủi ro chiến lược

### Bước 4: Roadmap Deconstruction
Sau khi VISION.md được duyệt, bóc tách "Phạm vi MVP" thành danh sách các Features. Hướng dẫn user chọn một Feature ưu tiên cao nhất để bắt đầu `Feature Intake`.
