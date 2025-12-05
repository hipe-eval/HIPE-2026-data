"""Evaluate a single HIPE-2026 prediction file against gold data."""

import sys
import argparse
from pathlib import Path
from check_jsonlschema import load_schema, validate_jsonl_file
from evaluation_utils import (
    load_jsonl_to_reshaped_dict,
    impute_missing_submission_data,
    flatten_predictions,
    calculate_metrics,
    print_metrics,
)


def validate_file_path(path_string, file_description):
    """Validate that a file path exists and is a file.

    Args:
        path_string: Path provided via command line.
        file_description: Human-readable description of the file.

    Returns:
        Validated pathlib.Path object.

    Exits:
        Program exits with status 1 if validation fails.
    """
    path_obj = Path(path_string)

    if not path_obj.exists():
        print(f"Error: {file_description} not found at '{path_obj}'.", file=sys.stderr)
        sys.exit(1)

    if not path_obj.is_file():
        print(
            f"Error: Path '{path_obj}' exists but is not a file for {file_description.lower()}.",
            file=sys.stderr,
        )
        sys.exit(1)

    return path_obj


def main():
    """Execute evaluation of a single prediction file."""
    parser = argparse.ArgumentParser(
        description="Evaluate a single submission file against gold data"
    )
    parser.add_argument(
        "--schema_file",
        default="schemas/hipe-2026-data.schema.json",
        help="The path to the JSON schema file for validation.",
    )
    parser.add_argument(
        "--gold_data_file",
        required=True,
        help="The gold data JSONL file to evaluate against.",
    )
    parser.add_argument(
        "--predictions_file",
        required=True,
        help="The predictions JSONL file to evaluate.",
    )

    args = parser.parse_args()

    schema_data = load_schema(args.schema_file)
    gold_file_path = validate_file_path(args.gold_data_file, "Gold data file")
    predictions_file_path = validate_file_path(
        args.predictions_file, "Predictions file"
    )

    # Validate schema
    gold_json_schema_errors = validate_jsonl_file(gold_file_path, schema_data)
    predictions_json_schema_errors = validate_jsonl_file(
        predictions_file_path, schema_data
    )

    if not (gold_json_schema_errors == 0 and predictions_json_schema_errors == 0):
        print(
            f"Error: JSON Schema validation failed. "
            f"Gold File Errors: {gold_json_schema_errors}, "
            f"Predictions File Errors: {predictions_json_schema_errors}.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Load data
    gold_data = load_jsonl_to_reshaped_dict(gold_file_path)
    submission_data = load_jsonl_to_reshaped_dict(predictions_file_path)

    # Impute missing data
    submission_data = impute_missing_submission_data(gold_data, submission_data)

    # Collect labels and calculate metrics
    flatten_preds_and_labels = flatten_predictions(gold_data, submission_data)
    metrics = calculate_metrics(flatten_preds_and_labels)

    # Print results
    print_metrics(metrics, f"Evaluation Results for {predictions_file_path.name}")


if __name__ == "__main__":
    main()
