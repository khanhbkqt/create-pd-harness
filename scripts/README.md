# Scripts — Công cụ Hỗ Trợ Design Pipeline

> Python scripts để verify, tracking, và sync artifacts trong design pipeline.

## Yêu cầu

- Python 3.10+ (không cần dependencies ngoài — chỉ dùng standard library)

## Scripts

### `status.py` — Status Dashboard & Tracking

Scan frontmatter từ tất cả docs, hiển thị trạng thái tổng quan.

```bash
# Hiển thị dashboard trên terminal
python scripts/status.py

# Cập nhật docs/STATUS.md từ frontmatter scan
python scripts/status.py --update

# Output JSON cho automation
python scripts/status.py --json
```

**Chức năng**:
- Scan tất cả `docs/` directories, đọc YAML frontmatter
- Parse Completeness Tracker tables trong documents
- Check dependency satisfaction (artifact A cần artifact B approved trước)
- Generate `docs/STATUS.md` tự động
- Gợi ý next action dựa trên dependency graph

### `sync_check.py` — Sync & Stale Detection

Phát hiện artifacts có thể outdated sau khi upstream document thay đổi.

```bash
# Check tất cả artifacts
python scripts/sync_check.py

# Check impact khi sửa 1 file cụ thể
python scripts/sync_check.py docs/prd/auth.md

# Verbose output
python scripts/sync_check.py --verbose
```

**Chức năng**:
- So sánh file modification timestamps theo dependency graph
- Nếu upstream (ví dụ PRD) mới hơn downstream (ví dụ SRS) → flag stale
- Report downstream files cần review
- Recursive chain detection (PRD → SRS → TDD)

## Dependency Graph

```
Vision ──→ PRD ──→ Flows ──→ Mockup ──→ TDD
Brief  ──→ PRD ──→ SRS   ──────────→ TDD
                   Decisions ·····→ TDD
```

- `──→` = Recommended dependency
- `···→` = Soft dependency

## Khi nào chạy?

| Tình huống | Script |
|---|---|
| Bắt đầu session design | `python scripts/status.py` |
| Sau khi tạo/sửa document | `python scripts/status.py --update` |
| Trước Review Gate | `python scripts/sync_check.py` |
| Sửa PRD, muốn biết ảnh hưởng | `python scripts/sync_check.py docs/prd/[file].md` |
| CI/automation | `python scripts/status.py --json` |
