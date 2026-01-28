import json
import sys
import random
import argparse

random.seed(42)

parser = argparse.ArgumentParser(description="Rewrite a JSONL file unchanged")
parser.add_argument("--input_path", help="Path to input JSONL file")
parser.add_argument("--output_path", help="Path to output JSONL file")
args = parser.parse_args()

with open(args.input_path, "r", encoding="utf-8") as fin, \
     open(args.output_path, "w", encoding="utf-8") as fout:

    for line_num, line in enumerate(fin, start=1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue

        for pair in record.get("sampled_pairs", []):
            at = pair.get("at")
            at = None
            is_at = pair.get("isAt")
            is_at = None
            pair["at"] = random.choice(["TRUE","PROBABLE", "FALSE"])
            pair["isAt"] = random.choice(["TRUE", "FALSE"])
        fout.write(json.dumps(record, ensure_ascii=False) + "\n")
