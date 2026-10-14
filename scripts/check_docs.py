#!/usr/bin/env python3
"""Reject obsolete Ravenstash commands and mixed CLI pins in public examples."""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REMOVED_COMMANDS = {
    "rvs account use": "use `rvs account switch`",
}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".toml", ".json", ".xml"}
CLI_PINS = (
    re.compile(r"RVS_INSTALL_VERSION=(\S+)"),
    re.compile(r"rvstash/setup-ravenstash@\S+.*\n\s*with:\n(?:\s+#.*\n)*\s*version:\s*\"?([^\"\s]+)"),
)


def main() -> int:
    errors: list[str] = []
    pins: dict[str, set[str]] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8")
        for command, guidance in REMOVED_COMMANDS.items():
            if command in content:
                errors.append(f"{path.relative_to(ROOT)}: removed command `{command}`; {guidance}")
        for pattern in CLI_PINS:
            for match in pattern.finditer(content):
                pins.setdefault(match.group(1), set()).add(str(path.relative_to(ROOT)))
    if len(pins) != 1:
        found = "; ".join(f"{version} in {', '.join(sorted(paths))}" for version, paths in sorted(pins.items()))
        errors.append(f"examples must pin exactly one rvs version, found: {found or 'none'}")
    if errors:
        print("\n".join(errors))
        return 1
    print("Public example documentation command checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
