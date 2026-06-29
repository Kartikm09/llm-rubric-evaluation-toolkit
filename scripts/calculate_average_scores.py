"""Calculate average rubric scores by dimension."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


SCORE_COLUMNS = [
    "general_quality",
    "factuality",
    "reasoning",
    "instruction_following",
    "safety",
    "tone",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate average scores by rubric dimension.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    with args.csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    print("Dimension averages")
    print("------------------")
    for column in SCORE_COLUMNS:
        values = [int(row[column]) for row in rows]
        average = sum(values) / len(values) if values else 0
        print(f"{column:24} {average:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
