"""Utility functions for HIPE-2026 evaluation tasks."""

import json
import sys
import copy
from pathlib import Path
from sklearn.metrics import accuracy_score, recall_score


def load_jsonl_to_reshaped_dict(file_path: Path) -> dict:
    """Load JSONL file and reshape sampled_pairs into dictionary.

    Creates a dictionary indexed by document_id. Reshapes sampled_pairs
    from array to dictionary indexed by concatenated pers_entity_id
    and loc_entity_id.

    Args:
        file_path: Path to the JSONL file.

    Returns:
        Dictionary of documents indexed by document_id.
    """
    documents = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                doc = json.loads(line)
                doc_id = doc.get("document_id")

                if doc_id is None:
                    print(
                        f"Warning: Line {line_num} in {file_path.name} missing 'document_id'. Skipping.",
                        file=sys.stderr,
                    )
                    continue

                if doc_id in documents:
                    print(
                        f"Warning: Duplicate document_id '{doc_id}' found in {file_path.name}. "
                        f"Overwriting previous entry.",
                        file=sys.stderr,
                    )

                if "sampled_pairs" in doc and isinstance(doc["sampled_pairs"], list):
                    reshaped_pairs = {}
                    for pair in doc["sampled_pairs"]:
                        pers_id = pair.get("pers_entity_id", "")
                        loc_id = pair.get("loc_entity_id", "")
                        pair_key = f"{pers_id}{loc_id}"

                        if pair_key in reshaped_pairs:
                            print(
                                f"Warning: Duplicate pair key '{pair_key}' in document '{doc_id}' "
                                f"from {file_path.name}. Overwriting.",
                                file=sys.stderr,
                            )

                        reshaped_pairs[pair_key] = pair

                    doc["sampled_pairs"] = reshaped_pairs

                documents[doc_id] = doc

            except json.JSONDecodeError as e:
                print(
                    f"Error: Failed to parse JSON on line {line_num} in {file_path.name}: {e}",
                    file=sys.stderr,
                )
                continue

    return documents


def impute_missing_submission_data(gold_data: dict, submission_data: dict) -> dict:
    """Ensure submission contains all gold documents and pairs.

    Missing entries are populated with at and isAt set to "FALSE".

    Args:
        gold_data: Dictionary of gold standard documents.
        submission_data: Dictionary of submission documents.

    Returns:
        Updated submission_data with imputed missing entries.
    """
    missing_docs_count = 0
    missing_pairs_count = 0

    for doc_id, gold_doc in gold_data.items():
        if doc_id not in submission_data:
            print(
                f"Info: Document '{doc_id}' missing from submission. Adding with default predictions.",
                file=sys.stderr,
            )

            missing_docs_count += 1

            submission_doc = copy.deepcopy(gold_doc)

            if "sampled_pairs" in submission_doc and isinstance(
                submission_doc["sampled_pairs"], dict
            ):
                for pair_key, pair_data in submission_doc["sampled_pairs"].items():
                    pair_data["at"] = "FALSE"
                    pair_data["isAt"] = "FALSE"

            submission_data[doc_id] = submission_doc

        else:
            gold_pairs = gold_doc.get("sampled_pairs", {})
            submission_pairs = submission_data[doc_id].get("sampled_pairs", {})

            if not isinstance(submission_pairs, dict):
                submission_data[doc_id]["sampled_pairs"] = {}
                submission_pairs = submission_data[doc_id]["sampled_pairs"]

            for pair_key, gold_pair in gold_pairs.items():
                if pair_key not in submission_pairs:
                    print(
                        f"Info: Pair '{pair_key}' missing in document '{doc_id}'. Adding with default predictions.",
                        file=sys.stderr,
                    )

                    missing_pairs_count += 1

                    submission_pair = copy.deepcopy(gold_pair)
                    submission_pair["at"] = "FALSE"
                    submission_pair["isAt"] = "FALSE"

                    submission_pairs[pair_key] = submission_pair

    if missing_docs_count > 0 or missing_pairs_count > 0:
        print(
            f"\nSummary: Imputed {missing_docs_count} missing document(s) and "
            f"{missing_pairs_count} missing sampled_pair(s) with default FALSE predictions.\n",
            file=sys.stderr,
        )

    return submission_data


def flatten_predictions(gold_data: dict, submission_data: dict) -> dict:
    """Collect gold and predicted labels for evaluation.

    Args:
        gold_data: Dictionary of gold standard documents.
        submission_data: Dictionary of submission documents.

    Returns:
        Dictionary with gold and predicted labels for 'at' and 'isAt'.
    """
    labels = {"at": {"gold": [], "pred": []}, "isAt": {"gold": [], "pred": []}}

    for doc_id, gold_doc in gold_data.items():
        gold_pairs = gold_doc.get("sampled_pairs", {})
        submission_pairs = submission_data[doc_id].get("sampled_pairs", {})

        for pair_key, gold_pair in gold_pairs.items():
            submission_pair = submission_pairs[pair_key]

            labels["at"]["gold"].append(gold_pair.get("at"))
            labels["at"]["pred"].append(submission_pair.get("at"))

            labels["isAt"]["gold"].append(gold_pair.get("isAt"))
            labels["isAt"]["pred"].append(submission_pair.get("isAt"))

    return labels


def calculate_metrics(labels: dict) -> dict:
    """Calculate accuracy and macro recall for predictions.

    Args:
        labels: Dictionary with gold and predicted labels.

    Returns:
        Dictionary of metrics for each target.
    """
    metrics = {}

    for target in ["at", "isAt"]:
        gold = labels[target]["gold"]
        pred = labels[target]["pred"]

        accuracy = accuracy_score(gold, pred)
        total = len(gold)
        correct = int(accuracy * total)
        macro_recall = recall_score(gold, pred, average="macro")

        metrics[target] = {
            "accuracy": accuracy,
            "macro_recall": macro_recall,
            "correct": correct,
            "total": total,
        }

    return metrics


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
