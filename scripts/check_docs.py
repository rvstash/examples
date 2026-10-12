#!/usr/bin/env python3
"""Reject obsolete Ravenstash commands in public examples."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REMOVED_COMMANDS = {
    "rvs account use": "use `rvs account switch`",
}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".toml", ".json", ".xml"}


def main() -> int:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8")
        for command, guidance in REMOVED_COMMANDS.items():
            if command in content:
                errors.append(f"{path.relative_to(ROOT)}: removed command `{command}`; {guidance}")
    if errors:
        print("\n".join(errors))
        return 1
    print("Public example documentation command checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
