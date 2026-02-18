import json
import sys
import random
import argparse
import os
import glob

random.seed(42)

parser = argparse.ArgumentParser(description="Create a baseline by randomly assigning 'at' and 'isAt' values in the sampled pairs.")
parser.add_argument("--input_dir", help="Path to folder of input JSONL files")
parser.add_argument("--output_dir", help="Path to folder for output JSONL files")
args = parser.parse_args()

for input_file in glob.glob(os.path.join(args.input_dir, "*.jsonl")):
    output_file = os.path.join(args.output_dir, os.path.basename(input_file).replace(".jsonl", "_random_baseline.jsonl"))

    with open(input_file, "r", encoding="utf-8") as fin, \
         open(output_file, "w", encoding="utf-8") as fout:

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
