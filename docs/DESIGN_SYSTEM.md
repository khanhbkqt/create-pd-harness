# Design System (Single Source of Truth)

> Tài liệu này định nghĩa các Design Tokens cốt lõi cho toàn bộ UI mockups. Bất kỳ UI_Engineer nào khi tạo component đều BẮT BUỘC phải dùng các token (CSS Variables) được định nghĩa tại đây, KHÔNG sử dụng màu/kích thước hard-code.

## 1. Colors

| Token | Giá trị HSL / HEX | Mục đích |
|---|---|---|
| `--color-primary` | `hsl(var(--hue), 80%, 50%)` | Màu chủ đạo cho nút CTA, link |
| `--color-background` | `hsl(0, 0%, 100%)` | Màu nền chính (White/Light mode) |
| `--color-surface` | `hsl(0, 0%, 98%)` | Màu nền cho card, panel |
| `--color-text-main` | `hsl(0, 0%, 10%)` | Màu chữ chính |
| `--color-text-muted` | `hsl(0, 0%, 40%)` | Màu chữ phụ, caption |
| `--color-border` | `hsl(0, 0%, 90%)` | Đường viền (borders, dividers) |
| `--color-error` | `hsl(0, 80%, 50%)` | Trạng thái lỗi, cảnh báo |

## 2. Typography

Sử dụng Google Fonts hiện đại (Inter, Roboto, hoặc Outfit).

| Token | Thuộc tính | Giá trị |
|---|---|---|
| `--font-family-main` | `font-family` | `'Inter', sans-serif` |
| `--font-size-sm` | `font-size` | `0.875rem` (14px) |
| `--font-size-base` | `font-size` | `1rem` (16px) |
| `--font-size-lg` | `font-size` | `1.125rem` (18px) |
| `--font-size-xl` | `font-size` | `1.5rem` (24px) |
| `--font-weight-regular` | `font-weight` | `400` |
| `--font-weight-medium` | `font-weight` | `500` |
| `--font-weight-bold` | `font-weight` | `700` |

## 3. Spacing & Layout

Tuân thủ hệ thống spacing base-4 hoặc base-8.

| Token | Giá trị | Ví dụ |
|---|---|---|
| `--spacing-xs` | `0.25rem` (4px) | Khoảng cách siêu nhỏ |
| `--spacing-sm` | `0.5rem` (8px) | Giữa icon và text |
| `--spacing-md` | `1rem` (16px) | Padding mặc định của component |
| `--spacing-lg` | `1.5rem` (24px) | Padding của Card |
| `--spacing-xl` | `2rem` (32px) | Giữa các section |

## 4. Shadows & Radii

| Token | Giá trị | Mục đích |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Buttons, Cards nhẹ |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` | Dropdown, Modal |
| `--radius-sm` | `4px` | Input, Checkbox |
| `--radius-md` | `8px` | Button, Card |
| `--radius-full` | `9999px` | Avatar, Pill badge |

---
_Cập nhật bởi UI_Engineer_
