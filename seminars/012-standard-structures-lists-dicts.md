# 012 - Standard Structures: Lists, Dictionaries/Maps

**Objectives**

- Use lists and dictionaries for collection storage.
- Choose appropriate data structures for lookup vs ordered data.
- Perform common operations: iteration, comprehension, mutation.

**Description**

Students learn core compound structures: arrays/lists and maps/dictionaries. The seminar covers creation, common operations, iteration patterns, and simple performance tradeoffs to guide selection.

**Outline**

1. Lists: creation, indexing, slicing
2. Dictionaries: keys, values, lookups
3. Iteration and comprehensions
4. When to use which structure
5. Brief complexity notes

**Exercises**

- Short coding exercise: Count word frequencies in a text using a dictionary.
- Mini-project: Implement a small in-memory index for quick lookups on a dataset.

**Resources**

- Python data structures docs
- Articles on algorithmic complexity basics

---

Example: count words with a dictionary

```python
text = 'a b a c a b'
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
print(counts)
```
