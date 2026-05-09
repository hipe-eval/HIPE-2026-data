# HIPE-2026 Data Repository Guide

This repository contains the public data, schema, sample submissions, and
evaluation utilities for the HIPE 2026 shared task on person-place relation
extraction in multilingual historical documents.

## Repository Purpose

HIPE 2026 data is distributed as UTF-8 JSON Lines files. Each line is one
document with OCR text, document metadata, and sampled person-location pairs.
The main prediction targets are:

- `at`: whether the text provides evidence that the person was at the location
  at any time before publication. Allowed values are `TRUE`, `FALSE`,
  `PROBABLE`, or `null`.
- `isAt`: whether the text supports that the person was present at the location
  within roughly one month before publication. Allowed values are `TRUE`,
  `FALSE`, or `null`.

During evaluation, missing or `null` prediction values are treated as `FALSE`.

## Top-Level Structure

- `README.md`: public project description, release notes, data format overview,
  and example prediction/evaluation commands.
- `Makefile`: helper targets for environment setup, validation, and cleanup.
  On macOS, run these targets with `remake` instead of the system `make`.
- `requirements.txt`: Python dependencies for validation and scoring.
- `schemas/`: JSON Schema definitions for validating HIPE 2026 JSONL files.
- `data/`: training data, sandbox data, and sample submissions.
- `official_test_unlabeled/`: unlabeled official test files for submission
  preparation.
- `scripts/`: Python utilities for validation, baseline prediction generation,
  and evaluation.

## Data Layout

The current released newspaper training data is under:

```text
data/newspapers/v1.0/
```

It contains one JSONL file per language:

- `HIPE-2026-v1.0-impresso-train-de.jsonl`
- `HIPE-2026-v1.0-impresso-train-en.jsonl`
- `HIPE-2026-v1.0-impresso-train-fr.jsonl`

Sandbox data is under:

```text
data/sandbox/
```

These files contain high-quality automatic annotations for German, English, and
French train/dev splits. See `data/sandbox/README.md`.

Sample submissions are under:

```text
data/sample_submissions/
```

There are two examples:

- `random_baseline/`: complete random predictions.
- `random_baseline_including_dropout/`: random predictions with submission
  dropout behavior represented.

Unlabeled official test data is under:

```text
official_test_unlabeled/
```

This includes `impresso` test files for German, English, and French, plus a
French surprise test file.

## JSON Schema

The active schema file is:

```text
schemas/hipe-2026-data.schema.json
```

Required document-level fields include:

- `document_id`
- `source`
- `media`
- `date`
- `language`
- `text`
- `sampled_pairs`

Each sampled pair requires person and location entity identifiers, Wikidata QIDs
or `null`, mention lists, and labels for `at` and `isAt`.

## Scripts

- `scripts/check_jsonlschema.py`: validates one or more JSONL files against a
  JSON schema.
- `scripts/dummy_predict.py`: creates random `at` and `isAt` predictions for an
  input JSONL file.
- `scripts/file_scorer_evaluation.py`: validates and evaluates one prediction
  file against one gold file.
- `scripts/folder_scorer_evaluation.py`: evaluates a folder of submission files
  against matching gold files.
- `scripts/evaluation_utils.py`: shared loading, imputation, flattening, metric,
  and reporting helpers.
- `scripts/create_random_baseline_including_dropout.py`: utility for generating
  randomized baseline files with optional pair/document dropout.
- `scripts/tmp/`: scratch area for generated local predictions.

## Common Local Workflow

Create a local environment with `venv/` or `.venv/`, matching the maintainer's
usual project conventions:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Validate JSONL files directly:

```bash
python scripts/check_jsonlschema.py \
  --schemafile schemas/hipe-2026-data.schema.json \
  data/newspapers/v1.0/*.jsonl
```

Generate a random prediction file:

```bash
python scripts/dummy_predict.py \
  --input_path data/newspapers/v1.0/HIPE-2026-v1.0-impresso-train-de.jsonl \
  --output_path scripts/tmp/RANDOM_HIPE-2026-v1.0-impresso-train-de.jsonl
```

Evaluate one prediction file:

```bash
python scripts/file_scorer_evaluation.py \
  --gold_data_file data/newspapers/v1.0/HIPE-2026-v1.0-impresso-train-de.jsonl \
  --predictions_file scripts/tmp/RANDOM_HIPE-2026-v1.0-impresso-train-de.jsonl
```

If using Makefile targets, use `remake`:

```bash
remake help
remake validate
```

Note that direct script commands are the clearest source of truth for current
paths because the Makefile may lag behind the released directory/schema names.

## Agent Notes

- Preserve JSONL as UTF-8, one valid JSON object per line.
- Do not reorder or rewrite large data files unless the task explicitly requires
  it.
- Keep generated predictions in `scripts/tmp/` or another clearly temporary
  location.
- Prefer direct Python script invocations when checking schema or scoring
  behavior.
- Use `remake`, not `make`, when invoking Makefile targets on macOS.
