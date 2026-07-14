# Tournament-Based-Behavioral-Evaluation-of-LLMs
A research project proposing a tournament-based evaluation framework for Large Language Models (LLMs), where models compete by generating responses and iteratively voting to eliminate the weakest answer.

Unlike traditional benchmarks that evaluate models independently, this framework explores competitive and behavioral dynamics including:

Self-voting

Adversarial voting

Format compliance

Voting patterns

Elimination behavior

Motivation
Current LLM benchmarks focus on correctness and reasoning ability.

This project investigates an alternative question:

How do LLMs behave when competing against one another?

Features
Tournament-style elimination

Anonymous answer evaluation

Peer voting between LLMs

Behavioral metric analysis

Automated result aggregation

Visualization of tournament statistics

Models Evaluated
Mistral

Llama 2

Gemma

Phi

Qwen

using Ollama.

Methodology
All models answer the same prompt.

Responses are anonymized.

Every model votes for the weakest answer.

The most-voted response is eliminated.

Repeat until one winner remains.

Metrics
The framework measures

Tournament wins

Average elimination round

Votes cast

Votes received

Invalid votes

Self-voting behavior

Results
<img width="478" height="160" alt="Screenshot 2026-07-14 232700" src="https://github.com/user-attachments/assets/cc7bf4a5-fc51-4205-8b2b-95d1b0cac998" />
Wins per Model
<img width="419" height="313" alt="Screenshot 2026-07-14 232720" src="https://github.com/user-attachments/assets/aff53963-0689-42f8-b19b-426582f56217" />





Average Elimination Round
<img width="445" height="329" alt="Screenshot 2026-07-14 232739" src="https://github.com/user-attachments/assets/6d15cc2f-c546-4835-9520-97f16e5aa990" />



Invalid Votes
<img width="470" height="309" alt="Screenshot 2026-07-14 232759" src="https://github.com/user-attachments/assets/2e6240b9-3060-481f-bd26-df55de338e4b" />
