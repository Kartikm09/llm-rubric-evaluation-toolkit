# llm-rubric-evaluation-toolkit

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![Rubric QA](https://img.shields.io/badge/LLM%20Evaluation-Rubric%20Based-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A practical toolkit for evaluating LLM outputs with clear scoring rubrics, reviewer comments, structured feedback, and simple Python summaries.

This repository is designed for AI trainer, data annotator, model evaluator, QA specialist, prompt engineer, and RLHF-adjacent portfolio work.

## Project Overview

The toolkit shows how to review AI outputs in a consistent way:

- Score responses across multiple quality dimensions.
- Compare before/after feedback.
- Log evaluator comments.
- Calculate average scores and identify weak dimensions.
- Generate concise feedback summaries for model improvement.

## Evaluation Dimensions

| Dimension | What it checks |
| --- | --- |
| General quality | Completeness, relevance, clarity, and user usefulness |
| Factuality | Evidence, uncertainty, and unsupported claims |
| Reasoning quality | Step logic, consistency, and explanation quality |
| Instruction following | Format, constraints, and task completion |
| Safety and policy | Privacy, misuse prevention, and sensitive-domain caution |
| Tone and clarity | Professional tone, readability, and user fit |

## Scoring Scale

| Score | Label | Meaning |
| --- | --- | --- |
| 5 | Excellent | Fully satisfies the rubric with clear evidence |
| 4 | Good | Minor issue, still acceptable |
| 3 | Mixed | Useful but needs revision |
| 2 | Poor | Major issue in one or more dimensions |
| 1 | Unacceptable | Unsafe, fabricated, irrelevant, or fails task |

## Example Evaluation

| Item | Prompt type | Weakness found | Feedback |
| --- | --- | --- | --- |
| EVAL-001 | Factuality | Unsupported exact statistic | Add uncertainty and request a source |
| EVAL-002 | Instruction following | Did not output JSON | Validate required format before final answer |
| EVAL-003 | Tone | Too verbose | Shorten response and lead with answer |

## Folder Structure

```text
rubrics/   Dimension-specific scoring rubrics
examples/  Prompt/response pairs, scored samples, and feedback rewrites
data/      CSV dataset, JSON schema, Excel scoring template
scripts/   Standard-library evaluation utilities
docs/      Evaluator guidelines and QA checklists
```

## How To Use The Python Scripts

```bash
python3 scripts/evaluate_responses.py data/evaluation_dataset_sample.csv
python3 scripts/calculate_average_scores.py data/evaluation_dataset_sample.csv
python3 scripts/generate_feedback_summary.py data/evaluation_dataset_sample.csv
```

The scripts use only the Python standard library.

## How This Supports RLHF / AI Training Workflows

Rubric-based evaluation creates structured evidence that can be used for:

- Ranking candidate responses
- Training evaluator consistency
- Identifying recurring model weaknesses
- Writing targeted feedback
- Auditing annotation quality
- Creating reusable QA checklists

## Recruiter-Facing Skills Demonstrated

- LLM output evaluation
- Rubric design
- AI training data review
- RLHF-style feedback
- Prompt-response analysis
- Factuality review
- Safety review
- Python automation
- Documentation and quality control

## LinkedIn Project Description

Created a practical LLM rubric evaluation toolkit for scoring AI outputs across factuality, reasoning, instruction following, safety, tone, and general response quality. The project includes reusable rubrics, scored examples, feedback templates, a sample evaluation dataset, an Excel scoring template, and Python scripts for score summaries and evaluator feedback.

## Verification

Run `make verify` (or `python3 -m unittest discover -s tests -v`). The
standard-library suite uses independent synthetic fixtures and command-line
checks, including malformed inputs. GitHub CI runs the same command on Python
3.11. These checks verify the reporting code; they do not measure a live model
or validate the truth of a human-assigned score.

Score-reporting commands reject missing, blank, noninteger, or out-of-range
scores with a clear error. The documented scale is 1–5; missing assessments
are data errors and are not converted into model failures.

See [repair scope and evidence](docs/verified-repair.md).
