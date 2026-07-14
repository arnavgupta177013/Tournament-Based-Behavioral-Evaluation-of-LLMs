import json
import matplotlib.pyplot as plt
from collections import defaultdict

# =========================
# CONFIG
# =========================
RESULTS_FILE = r"C:\Users\Arnav\results.jsonl"

# =========================
# LOAD RESULTS
# =========================
results = []
with open(RESULTS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        results.append(json.loads(line))

print(f"Loaded {len(results)} runs")

# =========================
# AGGREGATE STATS
# =========================
wins = defaultdict(int)
elim_rounds = defaultdict(list)
votes_cast = defaultdict(int)
votes_received = defaultdict(int)
invalid_votes = defaultdict(int)

for run in results:
    wins[run["winner"]] += 1

    eliminated = {}
    for r in run["rounds"]:
        eliminated[r["eliminated"]] = r["round"]
        for voter, target in r["votes"].items():
            votes_cast[voter] += 1
            votes_received[target] += 1

    for m in run["answers"].keys():
        if m in eliminated:
            elim_rounds[m].append(eliminated[m])
        else:
            elim_rounds[m].append(len(run["rounds"]) + 1)

    for m, c in run["invalid_votes"].items():
        invalid_votes[m] += c

models = sorted(wins.keys())
avg_elim = {m: sum(elim_rounds[m]) / len(elim_rounds[m]) for m in models}

# =========================
# PLOT 1: WINS PER MODEL
# =========================
plt.figure()
plt.bar(models, [wins[m] for m in models])
plt.title("Wins per Model")
plt.ylabel("Number of Wins")
plt.xlabel("Model")
plt.tight_layout()
plt.show()

# =========================
# PLOT 2: AVG ELIMINATION ROUND
# =========================
plt.figure()
plt.bar(models, [avg_elim[m] for m in models])
plt.title("Average Elimination Round")
plt.ylabel("Round")
plt.xlabel("Model")
plt.tight_layout()
plt.show()

# =========================
# PLOT 3: INVALID VOTES
# =========================
plt.figure()
plt.bar(models, [invalid_votes[m] for m in models])
plt.title("Invalid Votes per Model")
plt.ylabel("Count")
plt.xlabel("Model")
plt.tight_layout()
plt.show()

# =========================
# PLOT 4: VOTES CAST vs RECEIVED
# =========================
plt.figure()
x = range(len(models))
plt.bar(x, [votes_cast[m] for m in models], width=0.4, label="Votes Cast")
plt.bar([i + 0.4 for i in x], [votes_received[m] for m in models],
        width=0.4, label="Votes Received")

plt.xticks([i + 0.2 for i in x], models)
plt.title("Votes Cast vs Votes Received")
plt.ylabel("Count")
plt.xlabel("Model")
plt.legend()
plt.tight_layout()
plt.show()
