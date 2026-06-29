"""Generate concise feedback themes from scored LLM evaluation rows."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
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
    parser = argparse.ArgumentParser(description="Generate feedback summary from evaluation CSV.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    with args.csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    weak_dimensions: Counter[str] = Counter()
    comments: list[str] = []
    for row in rows:
        scores = {column: int(row[column]) for column in SCORE_COLUMNS}
        weakest = min(scores, key=scores.get)
        if scores[weakest] <= 3:
            weak_dimensions[weakest] += 1
            comments.append(f"{row['item_id']}: {row['reviewer_comment']}")

    print("Feedback summary")
    print("----------------")
    print("Weakest recurring dimensions:")
    for dimension, count in weak_dimensions.most_common():
        print(f"- {dimension}: {count}")
    print("\nReviewer comments needing follow-up:")
    for comment in comments:
        print(f"- {comment}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
