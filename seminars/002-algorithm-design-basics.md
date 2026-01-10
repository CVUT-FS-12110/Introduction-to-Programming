# 002 - Algorithm Design Basics

Objectives

- Translate real-world problems into step-by-step solutions.
- Write clear pseudocode and draw simple flowcharts.
- Evaluate basic algorithm correctness and simple performance intuition.

Description

Students will practice algorithmic thinking: defining problems, decomposing tasks, and expressing solutions with pseudocode and flowcharts. Emphasis is on clarity, correctness, and simple complexity reasoning (big-O intuition) for everyday programming problems. (38 words)

Outline

1. Problem specification and inputs/outputs
2. Pseudocode conventions
3. Flowchart components and mapping to code
4. Common patterns: loops, conditionals, divide-and-conquer
5. Basic complexity intuition and correctness checks

Exercises

- Short coding exercise: Implement linear search in a list and write pseudocode + a flowchart for it.
- Mini-project: Design two approaches to a small problem (e.g., finding duplicates); implement, compare correctness and performance on sample inputs.

Sample Code (Python)

```python
# linear search
def linear_search(arr, x):
    for i, v in enumerate(arr):
        if v == x:
            return i
    return -1
```

Resources

- Introduction to Algorithms (CLRS) — selected intro chapters
- Flowchart tutorial: https://www.lucidchart.com/pages/what-is-a-flowchart
