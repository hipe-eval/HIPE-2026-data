"""Evaluate HIPE-2026 submission files against gold standard folder."""

import sys
import argparse
from pathlib import Path

from typing import Optional, List

from check_jsonlschema import load_schema, validate_jsonl_file

from evaluation_utils import (
    load_jsonl_to_reshaped_dict,
    impute_missing_submission_data,
    flatten_predictions,
    calculate_metrics,
    print_metrics,
)

GOLD_FILENAMES_PREFIXES = [
    "HIPE-2026-*-impresso-sample-de",
    "HIPE-2026-*-impresso-sample-fr",
]


def validate_folder_path(path_string, folder_name):
    """Convert path string to Path object and validate it exists as directory.

    Args:
        path_string: Path provided via command line.
        folder_name: Human-readable name for the folder.

    Returns:
        Validated pathlib.Path object.

    Exits:
        Program exits with status 1 if validation fails.
    """
    path_obj = Path(path_string)

    if not path_obj.exists():
        print(f"Error: {folder_name} not found at '{path_obj}'.", file=sys.stderr)
        sys.exit(1)

    if not path_obj.is_dir():
        print(
            f"Error: Path '{path_obj}' exists but is not a directory for the {folder_name.lower()}.",
            file=sys.stderr,
        )
        sys.exit(1)

    return path_obj


def find_most_recent_gold_file(gold_dir: Path, file_pattern: str) -> Optional[Path]:
    """Find gold file by prioritizing highest versioned file.

    Args:
        gold_dir: Path to gold data directory.
        file_pattern: Filename pattern with single '*' wildcard.

    Returns:
        Path to selected gold file, or None if none found.
    """
    glob_pattern = f"{file_pattern}.jsonl"
    matching_gold_files = list(gold_dir.glob(glob_pattern))

    if not matching_gold_files:
        print("No matching gold_files found for " + str(file_pattern))
        return None

    matching_gold_files.sort(key=lambda p: p.name, reverse=True)

    if len(matching_gold_files) > 1:
        print(
            "WARNING: Multiple versioned gold files found. Performing evaluation using : "
            + str(matching_gold_files[0])
        )
    return matching_gold_files[0]


def aggregate_labels(all_labels: List[dict]) -> dict:
    """Aggregate labels across multiple files.

    Args:
        all_labels: List of label dictionaries from individual files.

    Returns:
        Aggregated labels across all files.
    """
    aggregated = {"at": {"gold": [], "pred": []}, "isAt": {"gold": [], "pred": []}}

    for labels in all_labels:
        aggregated["at"]["gold"].extend(labels["at"]["gold"])
        aggregated["at"]["pred"].extend(labels["at"]["pred"])
        aggregated["isAt"]["gold"].extend(labels["isAt"]["gold"])
        aggregated["isAt"]["pred"].extend(labels["isAt"]["pred"])

    return aggregated


def print_metrics(metrics: dict, title: str):
    """Print metrics for all targets.

    Args:
        metrics: Dictionary containing metrics for each target.
        title: Title to display above the metrics.
    """
    print(f"\n{title}:")

    for target, target_metrics in metrics.items():
        metric_strings = []
        for metric_name, metric_value in target_metrics.items():
            if metric_name in ["correct", "total"]:
                continue
            elif isinstance(metric_value, float):
                metric_strings.append(f"{metric_name}={metric_value:.4f}")

        metrics_str = ", ".join(metric_strings)

        if "correct" in target_metrics and "total" in target_metrics:
            counts_str = f" ({target_metrics['correct']}/{target_metrics['total']})"
        else:
            counts_str = ""

        print(f"  '{target}': {metrics_str}{counts_str}")
    print()


def main():
    """Execute folder level evaluation of HIPE-2026 submission files."""
    parser = argparse.ArgumentParser(
        description="Evaluate submission files made to HIPE2026"
    )
    parser.add_argument(
        "--schema_file",
        default="schemas/hipe-2026-data.schema.json",
        help="The path to the JSON schema file for validation.",
    )
    parser.add_argument(
        "--gold_data_folder",
        default="data/newspapers/v0.9",
        help="The folder path containing the gold data to evaluate against.",
    )
    parser.add_argument(
        "team_name",
        help="The unique team name for the submitting team (e.g., TEAM_A).",
    )
    parser.add_argument(
        "submission_folder",
        help="The folder path containing the submission files to evaluate",
    )

    args = parser.parse_args()

    schema_data = load_schema(args.schema_file)

    gold_dir = validate_folder_path(args.gold_data_folder, "Gold data folder")
    submission_dir = validate_folder_path(args.submission_folder, "Submission folder")
    team_name = args.team_name

    if not GOLD_FILENAMES_PREFIXES:
        print(
            "Error: The GOLD_PREFIXES list is not set within the script variables. Cannot proceed.",
            file=sys.stderr,
        )
        sys.exit(1)

    all_files_intermediates = []
    for gold_file_prefix_pattern in GOLD_FILENAMES_PREFIXES:
        gold_file_path = find_most_recent_gold_file(gold_dir, gold_file_prefix_pattern)

        submission_file_path = (
            submission_dir / f"{team_name}_{gold_file_path.stem}_run1.jsonl"
        )

        if not submission_file_path.exists():
            print(
                f" Error: Required submission file not found: {submission_file_path.name}",
                file=sys.stderr,
            )
            continue

        gold_json_schema_errors = validate_jsonl_file(gold_file_path, schema_data)
        submission_json_schema_errors = validate_jsonl_file(
            submission_file_path, schema_data
        )

        if not (gold_json_schema_errors == 0 and submission_json_schema_errors == 0):
            print(
                f"SKIPPING EVALUATION for {submission_file_path}: "
                f"JSON Schema issues detected. "
                f"Gold File Errors: {gold_json_schema_errors}, "
                f"Submission File Errors: {submission_json_schema_errors}.",
                file=sys.stderr,
            )
        else:
            gold_data = load_jsonl_to_reshaped_dict(gold_file_path)
            submission_data = load_jsonl_to_reshaped_dict(submission_file_path)
            submission_data = impute_missing_submission_data(gold_data, submission_data)
            flatten_preds_and_labels = flatten_predictions(gold_data, submission_data)
            file_metrics = calculate_metrics(flatten_preds_and_labels)

            all_files_intermediates.append(flatten_preds_and_labels)

            print_metrics(file_metrics, f"Per-file Results for {gold_file_path.name}")

    if all_files_intermediates:
        print(f"\n{'='*60}")
        print("Overall Results Across All Files")
        print(f"{'='*60}")

        flatten_overall = aggregate_labels(all_files_intermediates)
        overall_metrics = calculate_metrics(flatten_overall)

        print_metrics(overall_metrics, "Overall Metrics")


if __name__ == "__main__":
    main()
