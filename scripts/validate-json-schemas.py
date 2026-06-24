from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_DIRS = ["schemas", "examples"]


def main() -> int:
    failures: list[str] = []
    for directory in JSON_DIRS:
        for path in sorted((ROOT / directory).rglob("*.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                failures.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
                continue

            if path.parts[-2] != "examples" and "schemas" in path.parts:
                for key in ["$schema", "$id", "title"]:
                    if key not in data:
                        failures.append(f"{path.relative_to(ROOT)}: missing {key}")

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print("JSON schemas and examples parsed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
