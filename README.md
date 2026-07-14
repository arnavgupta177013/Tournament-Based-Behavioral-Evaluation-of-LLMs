# Tournament-Based-Behavioral-Evaluation-of-LLMs
# 🏆 Tournament-Based Behavioral Evaluation of Large Language Models

A research project proposing a **tournament-based evaluation framework** for Large Language Models (LLMs), where models compete by generating responses and iteratively vote to eliminate the weakest answer.

Unlike traditional benchmarks that evaluate models independently, this framework explores **competitive and behavioral dynamics**, including:

- Self-voting behavior
- Adversarial voting
- Format compliance
- Voting patterns
- Elimination behavior

---

# 🎯 Motivation

Current LLM benchmarks primarily evaluate models based on correctness and reasoning ability.

This project investigates an alternative research question:

> **How do Large Language Models behave when competing against one another?**

The proposed tournament framework aims to reveal behavioral characteristics that are not observable through traditional benchmark-based evaluation.

---

# ✨ Features

- Tournament-style elimination framework
- Anonymous answer evaluation
- Peer voting between LLMs
- Behavioral metric analysis
- Automated result aggregation
- Tournament statistics visualization

---

# 🤖 Models Evaluated

The framework evaluates the following open-source models using **Ollama**:

- Mistral
- Llama 2
- Gemma
- Phi
- Qwen

---

# ⚙️ Methodology

For each prompt:

1. All models generate responses to the same prompt.
2. Responses are anonymized.
3. Every model votes for the weakest response.
4. The response receiving the most votes is eliminated.
5. The process repeats until one model remains as the winner.

---

# 📊 Metrics

The framework measures:

- Tournament Wins
- Average Elimination Round
- Votes Cast
- Votes Received
- Invalid Votes
- Self-Voting Behavior

---

# 📈 Results


<img width="478" height="160" alt="Screenshot 2026-07-14 232700" src="https://github.com/user-attachments/assets/cc7bf4a5-fc51-4205-8b2b-95d1b0cac998" />


The following metrics are visualized and analyzed:

- 🏆 Wins per Model
<img width="419" height="313" alt="Screenshot 2026-07-14 232720" src="https://github.com/user-attachments/assets/aff53963-0689-42f8-b19b-426582f56217" />


- 📉 Average Elimination Round
<img width="445" height="329" alt="Screenshot 2026-07-14 232739" src="https://github.com/user-attachments/assets/6d15cc2f-c546-4835-9520-97f16e5aa990" />


- ⚠️ Invalid Vote Count
<img width="470" height="309" alt="Screenshot 2026-07-14 232759" src="https://github.com/user-attachments/assets/2e6240b9-3060-481f-bd26-df55de338e4b" />


- 📊 Votes Cast vs. Votes Received

<img width="458" height="314" alt="Screenshot 2026-07-14 233030" src="https://github.com/user-attachments/assets/a64e04bc-1d97-4d31-baa8-ed6e8e58fc7c" />


---

# 🛠️ Tech Stack

- Python
- Ollama
- Pandas
- NumPy
- Matplotlib

---

# 📄 Research Paper

The complete research paper is available in the `paper/` directory.

---

# 🚀 Future Work

- Multi-agent debate framework
- LangGraph-based implementation
- Evaluation with larger LLMs
- Embedding-based explanation clustering
- Human vs. LLM evaluation comparison

---

# 👨‍💻 Author

**Arnav Gupta**

- LinkedIn: https://www.linkedin.com/in/arnavgupta1470
- GitHub: https://github.com/arnavgupta177013
