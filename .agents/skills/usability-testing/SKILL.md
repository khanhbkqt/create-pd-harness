---
name: usability-testing
description: Thiết lập kịch bản và thực thi kiểm thử trải nghiệm người dùng trên Mockup.
---

# Skill: Usability Testing

## MỤC ĐÍCH
Phát hiện các rào cản UX (UX friction), cognitive overload, và logic hổng trước khi chốt Mockup để viết SRS và TDD.

## QUY TRÌNH THỰC THI

### 1. Xác định Task List
Lập danh sách các tác vụ (tasks) mà user phải hoàn thành dựa trên UserFlow.
*Ví dụ*: "Tạo một tài khoản mới và hoàn thành onboarding", "Tìm kiếm một sản phẩm và thêm vào giỏ".

### 2. Chuẩn bị Kịch bản (Test Scenario)
Cho mỗi task, chuẩn bị:
- **Scenario context**: "Hãy tưởng tượng bạn đang cần..."
- **Expected path**: Đường đi dự kiến trên Mockup (Click A -> Nhập B -> Click C).
- **Success Criteria**: Điều kiện ghi nhận task thành công.

### 3. Thực thi (Simulated or Real)
- **Simulated Test (Agent đóng vai User)**: `QA_Skeptic` hoặc `UX_Architect` duyệt qua Mockup components/pages để tự đánh giá:
  - Có dễ nhận biết CTA không?
  - Báo lỗi (Validation) có rõ ràng không?
  - Có trạng thái loading không?
- **Real Test (User cung cấp feedback)**: Cung cấp kịch bản để user tự thao tác trên Mockup và phản hồi lại những đoạn họ thấy cấn/bối rối.

### 4. Báo cáo UX Issue
Tổng hợp lỗi theo format:

| Issue | Mức độ nghiêm trọng (High/Medium/Low) | Khuyến nghị sửa đổi |
|---|---|---|
| Nút "Xóa" dễ ấn nhầm | High | Thêm confirmation modal, đổi màu đỏ |
| Chữ hơi nhỏ trên mobile | Medium | Tăng base font size hoặc điều chỉnh rem |

### 5. Transition
- Nếu có lỗi High/Medium: Yêu cầu `UI_Engineer` sửa lại Mockup.
- Nếu không có lỗi lớn: Đánh dấu Pass Usability Test.
