import json
from collections import defaultdict

RESULTS_FILE = r"C:\Users\Arnav\results.jsonl"

CATEGORIES = {
    "factual_error": [
        "incorrect", "wrong", "false", "error", "inaccurate"
    ],
    "clarity": [
        "unclear", "confusing", "hard to follow", "not clear"
    ],
    "missing_detail": [
        "lacks detail", "incomplete", "superficial", "too brief", "missing"
    ],
    "moral_disagreement": [
        "ethical", "moral", "values", "should", "ought"
    ],
    "format_protocol": [
        "format", "instruction", "did not follow", "protocol"
    ],
    "vagueness": [
        "vague", "generic", "unspecific", "too general"
    ]
}

counts = defaultdict(lambda: defaultdict(int))

with open(RESULTS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        run = json.loads(line)
        for r in run["rounds"]:
            for model, text in r["explanations"].items():
                t = text.lower()
                for category, keywords in CATEGORIES.items():
                    if any(k in t for k in keywords):
                        counts[model][category] += 1

print("\n==============================")
print("📌 EXPLANATION CRITIQUE TYPES")
print("==============================")

for model, cats in counts.items():
    print(f"\nModel: {model}")
    for cat, c in cats.items():
        print(f"  {cat}: {c}")
