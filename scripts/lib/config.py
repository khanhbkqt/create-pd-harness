"""
config.py — Shared configuration: paths, dependency graph, constants.
"""

from pathlib import Path

# --- Paths ---
REPO_ROOT = Path(__file__).parent.parent.parent
DOCS_DIR = REPO_ROOT / "docs"
MOCKUPS_DIR = REPO_ROOT / "mockups" / "src"
SCRIPTS_DIR = REPO_ROOT / "scripts"
LOG_FILE = DOCS_DIR / ".activity_log.jsonl"

# --- Artifact Dependency Graph ---
# Key = artifact type, Value = list of recommended upstream dependencies
ARTIFACT_DEPS = {
    "Vision":        [],
    "Feature Brief": [],
    "PRD":           ["Vision", "Feature Brief"],
    "Flows":         ["PRD"],
    "SRS":           ["PRD"],
    "Mockup":        ["Flows", "PRD"],
    "TDD":           ["SRS", "Decisions"],
    "Decisions":     [],
}

# --- Priority Weights ---
# Higher weight = more important to complete first
PRIORITY_WEIGHTS = {
    "Vision":        10,   # Foundation — needed for everything
    "Feature Brief": 9,    # Business context
    "PRD":           8,    # Requirements baseline
    "Flows":         6,    # UX clarity
    "SRS":           7,    # Technical requirements
    "Mockup":        5,    # Visual reference
    "TDD":           4,    # Technical design (needs SRS + Mockup)
    "Decisions":     3,    # Can be done anytime
}

# --- Scan Paths ---
# Where to find files for each artifact type
ARTIFACT_SCAN = {
    "Vision":        {"dirs": [DOCS_DIR / "vision"],     "glob": "*.md"},
    "Feature Brief": {"dirs": [DOCS_DIR / "features"],   "glob": "*.md"},
    "PRD":           {"dirs": [DOCS_DIR / "prd"],        "glob": "*.md"},
    "Flows":         {"dirs": [DOCS_DIR / "flows"],      "glob": "*.md"},
    "SRS":           {"dirs": [DOCS_DIR / "srs"],        "glob": "*.md"},
    "TDD":           {"dirs": [DOCS_DIR / "tdd"],        "glob": "*.md"},
    "Decisions":     {"dirs": [DOCS_DIR / "decisions"],  "glob": "*.md"},
    "Mockup":        {"dirs": [MOCKUPS_DIR / "pages"],   "glob": "*.tsx"},
}

# --- Status Lifecycle ---
VALID_STATUSES = ["draft", "review", "approved", "superseded"]

# --- Completeness: required sections per doc type ---
REQUIRED_SECTIONS = {
    "Vision": [
        "Tầm nhìn sản phẩm", "North Star Metric", "Đối tượng mục tiêu",
        "Vấn đề cốt lõi", "Giải pháp đề xuất", "Nguyên tắc thiết kế sản phẩm",
        "Phạm vi MVP", "Thị trường & Đối thủ", "Rủi ro chiến lược"
    ],
    "Feature Brief": [
        "Vấn đề", "Đối tượng", "Giải pháp đề xuất",
        "Giá trị mang lại", "Phạm vi", "Rủi ro & Giả định", "Câu hỏi mở"
    ],
    "PRD": [
        "Tóm tắt", "Vấn đề cần giải quyết", "User Personas",
        "Phạm vi", "Yêu cầu chức năng", "Metrics thành công",
        "Ràng buộc & Giả định", "Dependencies", "Timeline",
        "Rủi ro & Biện pháp", "Lịch sử phê duyệt"
    ],
    "SRS": [
        "Giới thiệu", "Mô tả tổng quan", "Yêu cầu cụ thể",
        "Mô hình dữ liệu", "Đặc tả giao diện ngoài", "Traceability Matrix"
    ],
    "TDD": [
        "Tổng quan kiến trúc", "Component Design", "Data Model",
        "API Design", "Security", "Performance",
        "Trade-off Analysis", "Monitoring & Observability", "Deployment"
    ],
}

# --- Help Text ---
HELP_TEXT = """
╔══════════════════════════════════════════════════════════╗
║  pdt — Product Design Tool                              ║
║  CLI cho design pipeline: track, sync, verify, search   ║
╚══════════════════════════════════════════════════════════╝

USAGE:
    python scripts/pdt.py <command> [options]

COMMANDS:
    status      Dashboard overview, cập nhật STATUS.md
    sync        Detect stale artifacts sau thay đổi
    log         Xem/ghi activity log
    priority    Gợi ý việc cần làm tiếp theo
    verify      Pre-review-gate checks
    search      Tìm kiếm requirement/pattern xuyên docs

EXAMPLES:
    python scripts/pdt.py status              # Dashboard
    python scripts/pdt.py status --update     # Cập nhật STATUS.md
    python scripts/pdt.py sync                # Check sync toàn bộ
    python scripts/pdt.py sync docs/prd/x.md  # Impact analysis
    python scripts/pdt.py log                 # Xem log
    python scripts/pdt.py log --add "Viết PRD xong section 5"
    python scripts/pdt.py priority            # Next actions
    python scripts/pdt.py verify              # Run all checks
    python scripts/pdt.py verify --check traceability
    python scripts/pdt.py search REQ-001      # Trace requirement
    python scripts/pdt.py search --pattern "authentication"

FLAGS:
    --help, -h     Hiển thị help
    --json         JSON output (status, verify, search)
    --verbose, -v  Chi tiết hơn
"""
