#!/usr/bin/env python3

import sys
import json
import argparse
from pathlib import Path
from jsonschema import validate, ValidationError


def load_schema(schema_path):
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_data = json.load(f)
    return schema_data


def validate_jsonl_file(file_path, schema_data):
    errors = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if not line.strip():
                continue  # skip empty lines
            try:
                data = json.loads(line)
                validate(instance=data, schema=schema_data)
            except ValidationError as e:
                print(f"[ERROR] {file_path} (line {i}): {e.message}")
                errors += 1
            except json.JSONDecodeError as e:
                print(f"[ERROR] {file_path} (line {i}): Invalid JSON - {e}")
                errors += 1
            except Exception as e:
                print(f"[ERROR] {file_path} (line {i}): {e}")
                errors += 1
    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate one or more JSONL files against a JSON Schema."
    )
    parser.add_argument(
        "--schemafile", "-s", required=True, help="Path to JSON schema file."
    )
    parser.add_argument(
        "jsonl_files", nargs="+", help="One or more .jsonl files to validate."
    )

    args = parser.parse_args()
    schema_data = load_schema(args.schemafile)

    total_errors = 0
    for file in args.jsonl_files:
        path = Path(file)
        if not path.is_file():
            print(f"[ERROR] File not found: {file}")
            total_errors += 1
            continue

        print(f"Validating {file}...")
        errors = validate_jsonl_file(file, schema_data)
        if errors == 0:
            print(f"[OK] {file} passed validation.")
        else:
            print(f"[FAIL] {file} had {errors} error(s).")
        total_errors += errors

    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
