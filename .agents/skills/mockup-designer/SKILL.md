---
name: mockup-designer
description: Thiết kế ReactJS mockup theo Atomic Design pattern. Giao diện final cho production. Tuân thủ taste-skill v2. Pre-flight check bắt buộc.
---

# Skill: Mockup Designer (ReactJS, Atomic Design, taste-skill v2)

## KÍCH HOẠT

Khi UserFlow đã được thiết kế và PRD sections liên quan đã approve.

## PERSONA ACTIVE: `UI_Engineer`

Khắt khe về visual quality. Mỗi mockup là giao diện final cho production.

## DEPENDENCY CHECK

Trước khi bắt đầu code Mockup:
1. Chạy `python scripts/pdt.py status` để kiểm tra trạng thái PRD và Flows.
2. Nếu PRD hoặc Flows chưa approved, đưa ra cảnh báo cho user. Có thể thực hiện draft Mockups dựa trên các giả định hiện tại, nhưng cần chú ý nguy cơ bị stale/rework sau này.

## TIỀN ĐIỀU KIỆN

1. ĐỌC taste-skill v2: `taste-skill/skills/taste-skill/SKILL.md` - tuân thủ hoàn toàn
2. ĐỌC UserFlow liên quan trong `docs/flows/`
3. ĐỌC PRD sections liên quan cho feature requirements
4. VERIFY mockup project đã setup: `mockups/package.json` tồn tại

## QUY TRÌNH

### Bước 1: Brief Inference (taste-skill Section 0)

TRƯỚC KHI viết code, tuyên bố Design Read:
```
"Reading this as: [page kind] cho [audience], với [vibe] language, hướng tới [design system / aesthetic family]."
```

SET 3 dials (taste-skill Section 1):
```
DESIGN_VARIANCE: [1-10]
MOTION_INTENSITY: [1-10]
VISUAL_DENSITY: [1-10]
```

GHI RÕ lý do cho mỗi dial value dựa trên PRD context.

### Bước 2: Atomic Design Mapping

PHÂN TÁCH UI thành 5 tầng:

```
atoms/          → Thành phần nhỏ nhất: Button, Input, Label, Icon, Badge
molecules/      → Tổ hợp atoms: SearchBar, FormField, NavLink, Card
organisms/      → Tổ hợp molecules: Header, Footer, Sidebar, FeatureSection
templates/      → Layout skeleton: PageLayout, DashboardLayout, AuthLayout
pages/          → Trang hoàn chỉnh: HomePage, LoginPage, DashboardPage
```

NGUYÊN TẮC:
- Atoms: zero business logic, chỉ visual + props interface
- Molecules: kết hợp 2-5 atoms, có thể có local state nhỏ
- Organisms: feature-complete sections, có thể có data fetching
- Templates: chỉ là layout grid, nhận children
- Pages: compose templates + organisms, chứa route-level logic

### Bước 3: Component Implementation

MỖI component gồm 2 files: `[Name].tsx` + `[Name].css`

```tsx
// Button.tsx
import './Button.css'

interface ButtonProps {
  variant: 'primary' | 'secondary' | 'ghost';
  size: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
}

export function Button({ variant, size, children, ...props }: ButtonProps) {
  return (
    <button
      className={`btn btn--${variant} btn--${size}`}
      {...props}
    >
      {children}
    </button>
  )
}
```

```css
/* Button.css - Vanilla CSS, sử dụng design tokens từ tokens.css */
.btn {
  font-family: var(--font-sans);
  font-weight: var(--font-weight-medium);
  border: none;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
}

.btn--primary {
  background-color: var(--color-accent);
  color: #fff;
}

.btn--primary:hover {
  background-color: var(--color-accent-hover);
}

.btn--sm { padding: var(--space-1) var(--space-3); font-size: var(--text-sm); }
.btn--md { padding: var(--space-2) var(--space-4); font-size: var(--text-base); }
.btn--lg { padding: var(--space-3) var(--space-6); font-size: var(--text-lg); }
```

CHECKLIST per component:
- [ ] Props interface typed đầy đủ
- [ ] Responsive (mobile-first, collapse rules rõ ràng)
- [ ] Dark mode tokens
- [ ] Reduced motion fallback (MOTION_INTENSITY > 3)
- [ ] WCAG AA contrast
- [ ] Keyboard accessible

### Bước 4: File Structure

```
mockups/src/
├── components/
│   ├── atoms/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.css
│   │   │   └── index.ts
│   │   ├── Input/
│   │   ├── Badge/
│   │   └── ...
│   ├── molecules/
│   │   ├── SearchBar/
│   │   ├── FormField/
│   │   └── ...
│   ├── organisms/
│   │   ├── Header/
│   │   ├── HeroSection/
│   │   └── ...
│   └── templates/
│       ├── PageLayout/
│       └── ...
├── pages/
│   ├── HomePage.tsx
│   ├── HomePage.css
│   └── ...
├── styles/
│   ├── tokens.css          # Design tokens (CSS custom properties)
│   └── index.css            # Global reset + base styles
├── App.tsx
├── App.css
└── main.tsx
```

### Bước 5: Pre-flight Check (taste-skill Section 14)

CHẠY TOÀN BỘ checklist trong taste-skill Section 14 trước khi deliver. Đây là bắt buộc, không có ngoại lệ.

Tóm tắt các check quan trọng nhất:
- [ ] Brief inference đã tuyên bố
- [ ] Dial values rõ ràng và có lý do
- [ ] ZERO em-dash (`—`) trên toàn trang
- [ ] Page Theme Lock: một theme duy nhất
- [ ] Color Consistency Lock: một accent color xuyên suốt
- [ ] Button Contrast Check: WCAG AA
- [ ] Hero fits viewport: headline ≤ 2 dòng, CTA visible
- [ ] Navigation single line desktop, height ≤ 80px
- [ ] Real images (generate hoặc picsum, không fake div screenshots)
- [ ] Mobile collapse explicit cho mỗi section
- [ ] Reduced motion cho MOTION_INTENSITY > 3
- [ ] Dark mode tested cả 2 modes

## QUY TẮC

1. MỌI mockup là giao diện FINAL cho production - chỉn chu, không placeholder
2. ATOMIC Design pattern bắt buộc - atoms → molecules → organisms → templates → pages
3. TASTE-SKILL v2 tuân thủ hoàn toàn - đọc lại trước mỗi session design
4. COMPONENT naming: PascalCase, folder-per-component, re-export qua index.ts
5. RESPONSIVE mobile-first: design cho 375px trước, scale lên
6. TOKEN-BASED: colors, spacing, typography qua CSS custom properties
7. TRÍCH DẪN PRD requirement mà component đang implement: `{/* REQ-001: [mô tả] */}`
8. ĐỒNG BỘ TRẠNG THÁI:
   - Chạy `python scripts/pdt.py status --update`
   - Chạy `python scripts/pdt.py log --add "Cập nhật Mockups: thêm/sửa component hoặc page" --artifact "Mockup"`

## CHUYỂN GIAO

→ Mockup hoàn thành → Review Gate kiểm tra visual quality
→ Mockup là reference cho: TDD Writer (component specs), Handoff (deliverable)
