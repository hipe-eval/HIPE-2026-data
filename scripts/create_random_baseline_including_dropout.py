import json
import random
import glob
import os

# Allowed prediction values
AT_VALUES = ["TRUE", "PROBABLE", "FALSE"]
ISAT_VALUES = ["TRUE", "FALSE"]

# Directory containing your JSONL files
INPUT_DIR = "."  # Change if needed
OUTPUT_SUFFIX = "-randomized_dropout.jsonl"

# Dropout rate for sample pairs
PAIR_DROPOUT_RATE = 0.2  # 20% dropout


def randomize_predictions(obj):
    """
    Takes a JSON object and replaces prediction fields in all sampled pairs.
    Also applies dropout to randomly remove sample pairs.
    """
    if "sampled_pairs" not in obj:
        return obj

    # Apply dropout: keep only 80% of pairs on average
    kept_pairs = []
    for pair in obj["sampled_pairs"]:
        if random.random() > PAIR_DROPOUT_RATE:  # otherwise it's dropped
            if "at" in pair:
                pair["at"] = random.choice(AT_VALUES)
            else:
                print("INFO: At value is missing at " + str(pair))

            if "isAt" in pair:
                pair["isAt"] = random.choice(ISAT_VALUES)
            else:
                print("INFO: isAt value is missing at " + str(pair))

            kept_pairs.append(pair)

    obj["sampled_pairs"] = kept_pairs
    return obj


def process_files():
    files = glob.glob(os.path.join(INPUT_DIR, "*.jsonl"))

    for file_path in files:
        out_path = file_path.replace(".jsonl", OUTPUT_SUFFIX)

        # Read all lines first
        all_objects = []
        with open(file_path, "r", encoding="utf-8") as infile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                all_objects.append(obj)

        # Randomly select one document to delete (if there are multiple)
        if len(all_objects) > 1:
            delete_index = random.randint(0, len(all_objects) - 1)
            print(f"Deleting document at index {delete_index} from {file_path}")
            all_objects.pop(delete_index)

        # Process and write remaining documents
        with open(out_path, "w", encoding="utf-8") as outfile:
            for obj in all_objects:
                obj = randomize_predictions(obj)
                outfile.write(json.dumps(obj, ensure_ascii=False) + "\n")

        print(f"Processed: {file_path} → {out_path}")


if __name__ == "__main__":
    process_files()
