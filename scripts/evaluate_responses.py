"""Evaluate rubric-scored LLM response rows from a CSV file."""

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


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def row_average(row: dict[str, str]) -> float:
    scores = [int(row[column]) for column in SCORE_COLUMNS]
    return round(sum(scores) / len(scores), 2)


def weakest_dimension(row: dict[str, str]) -> str:
    scores = {column: int(row[column]) for column in SCORE_COLUMNS}
    return min(scores, key=scores.get)


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate rubric-scored LLM responses.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    rows = load_rows(args.csv_path)
    print("item_id,average_score,weakest_dimension,needs_follow_up")
    for row in rows:
        average = row_average(row)
        weakest = weakest_dimension(row)
        needs_follow_up = average < 4 or int(row[weakest]) <= 2
        print(f"{row['item_id']},{average},{weakest},{str(needs_follow_up).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
