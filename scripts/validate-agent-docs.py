from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "CONTRACT.md",
    "VERSIONING.md",
    "docs/agent/PERMISSIONS.md",
    "docs/agent/RUNBOOK.md",
    "docs/agent/TESTS.md",
    "docs/agent/SECURITY.md",
    "docs/agent/DATA_SCHEMA.md",
    "docs/agent/CONFIG.md",
    "docs/agent/RELEASE.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        for path in missing:
            print(f"Missing required agent doc: {path}")
        return 1

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    if "Compartir contratos" not in agents:
        print("AGENTS.md must state the contract boundary rule.")
        return 1

    print("Agent documentation is present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
