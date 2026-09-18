"""Calculate average rubric scores by dimension."""

from __future__ import annotations

import argparse
from pathlib import Path

from score_validation import load_scored_rows


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

    try:
        rows = load_scored_rows(args.csv_path, SCORE_COLUMNS)
    except ValueError as error:
        parser.error(str(error))

    print("Dimension averages")
    print("------------------")
    for column in SCORE_COLUMNS:
        values = [int(row[column]) for row in rows]
        average = sum(values) / len(values) if values else 0
        print(f"{column:24} {average:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
