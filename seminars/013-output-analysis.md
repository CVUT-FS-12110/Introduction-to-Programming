# 013 - Output Analysis

**Objectives**

- Interpret program outputs and spot anomalies.
- Use simple visualization or logging to explain results.
- Write concise reports of findings.

**Description**

Focus on interpreting and presenting program results clearly. Students will practice basic logging, simple visualizations, and writing short reports that explain what the outputs mean and how they were obtained.

**Outline**

1. Types of outputs and result formats
2. Logging and basic metrics
3. Simple visualization techniques
4. Interpreting anomalies and errors
5. Writing clear summaries/reports

**Exercises**

- Short coding exercise: Produce a simple plot from sample data and save it to a file.
- Mini-project: Run a small experiment, collect outputs, visualize results, and write a one-page summary.

**Resources**

- Matplotlib beginner guide
- Articles on interpreting experimental results

---

Example: simple plot using matplotlib

Note: the example below requires matplotlib. Install with `pip install matplotlib` or skip the plotting steps if matplotlib isn't available in the environment.

```python
# plotting example (requires matplotlib)
try:
    import matplotlib.pyplot as plt
except Exception:
    print('matplotlib not available; skipping plot example')
else:
    plt.plot([1, 4, 9, 16])
    plt.title('Sample Plot')
    plt.savefig('plot.png')
    print('Saved plot.png')
```
