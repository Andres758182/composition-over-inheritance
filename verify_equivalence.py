"""Run both designs and check that their observable behavior is identical."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def payroll_lines(version: str) -> list[str]:
    """Run <version>/main.py and return its output without the title line."""
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=ROOT / version,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.splitlines()[1:]


def main() -> None:
    inheritance = payroll_lines("inheritance")
    composition = payroll_lines("composition")
    if inheritance != composition:
        print("MISMATCH between inheritance and composition output:")
        for left, right in zip(inheritance, composition):
            marker = "  " if left == right else "!!"
            print(f"{marker} {left}\n{marker} {right}")
        sys.exit(1)
    print(f"OK - both designs print the same {len(inheritance)} payroll lines.")


if __name__ == "__main__":
    main()
