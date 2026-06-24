from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YAML_DIRS = ["openapi", "errors", ".github/workflows"]


def main() -> int:
    failures: list[str] = []
    for directory in YAML_DIRS:
        for path in sorted((ROOT / directory).rglob("*.yml")):
            content = path.read_text(encoding="utf-8")
            rel = path.relative_to(ROOT)
            if "\t" in content:
                failures.append(f"{rel}: tabs are not allowed in YAML")
            stripped = content.strip()
            if not stripped:
                failures.append(f"{rel}: empty YAML file")
            if path.name.endswith(".openapi.yml") and not stripped.startswith("openapi: 3.1.0"):
                failures.append(f"{rel}: OpenAPI files must start with 'openapi: 3.1.0'")
            if path.parent.name == "errors":
                if "domain:" not in content or "errors:" not in content:
                    failures.append(f"{rel}: error catalogs must contain domain and errors")

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print("YAML structure checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
