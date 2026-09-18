"""Generate concise feedback themes from scored LLM evaluation rows."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from score_validation import load_scored_rows, validated_scores


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

    try:
        rows = load_scored_rows(args.csv_path, SCORE_COLUMNS)
    except ValueError as error:
        parser.error(str(error))

    weak_dimensions: Counter[str] = Counter()
    comments: list[str] = []
    for row in rows:
        scores = validated_scores(row, SCORE_COLUMNS)
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
