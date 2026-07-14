import json
from collections import defaultdict

RESULTS_FILE = "results.jsonl"

# -------------------------
# Load results
# -------------------------
results = []
with open(RESULTS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        results.append(json.loads(line))

print(f"Loaded {len(results)} runs")

# -------------------------
# Data containers
# -------------------------
wins = defaultdict(int)
elimination_rounds = defaultdict(list)
votes_cast = defaultdict(int)
votes_received = defaultdict(int)
self_votes = defaultdict(int)
invalid_votes = defaultdict(int)

# -------------------------
# Parse each run
# -------------------------
for run in results:
    winner = run["winner"]
    wins[winner] += 1

    # Track elimination rounds
    eliminated = {}
    for r in run["rounds"]:
        eliminated[r["eliminated"]] = r["round"]

        # Votes
        for voter, target in r["votes"].items():
            votes_cast[voter] += 1
            votes_received[target] += 1

    # Any model not eliminated is the winner
    for model in run["answers"].keys():
        if model in eliminated:
            elimination_rounds[model].append(eliminated[model])
        else:
            elimination_rounds[model].append(len(run["rounds"]) + 1)

    # Self / invalid votes
    for model, count in run["self_votes"].items():
        self_votes[model] += count

    for model, count in run["invalid_votes"].items():
        invalid_votes[model] += count

# -------------------------
# Print summary
# -------------------------
models = sorted(wins.keys())

print("\n==============================")
print("📊 SUMMARY STATISTICS")
print("==============================")

for m in models:
    avg_round = sum(elimination_rounds[m]) / len(elimination_rounds[m])
    print(f"\nModel: {m}")
    print(f"  Wins: {wins[m]}")
    print(f"  Avg elimination round: {avg_round:.2f}")
    print(f"  Votes cast: {votes_cast[m]}")
    print(f"  Votes received: {votes_received[m]}")
    print(f"  Self-votes: {self_votes[m]}")
    print(f"  Invalid votes: {invalid_votes[m]}")

# -------------------------
# Integrity checks
# -------------------------
print("\n==============================")
print("🔍 INTEGRITY CHECKS")
print("==============================")

for i, run in enumerate(results, 1):
    if not run.get("winner"):
        print(f"❌ Run {i}: No winner")
    if len(run["rounds"]) < 1:
        print(f"❌ Run {i}: No rounds recorded")

print("✅ Integrity checks completed")
