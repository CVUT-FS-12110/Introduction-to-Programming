# 011 - State & Communication

**Objectives**

- Explain shared state vs local state and their implications.
- Pass data between program components cleanly.
- Identify simple concurrency concerns (overview).

**Description**

Covers how programs manage state and how components communicate: function params, return values, shared variables, and basic concurrency concepts. Focus is on clear data flow and avoiding common pitfalls when sharing state.

**Outline**

1. What is state? Local vs shared
2. Passing data between functions/modules
3. Immutable vs mutable state
4. Simple concurrency hazards (race conditions) - overview
5. Strategies for clear communication and data flow

**Exercises**

- Short coding exercise: Refactor code to remove a global variable by passing state explicitly.
- Mini-project: Build a small producer/consumer example using queues (single-threaded or with threading) and demonstrate safe communication.

**Resources**

- Articles on managing state in programs
- Intro to concurrency (overview)

---

Example: passing state dictionary

```python
# passing state example
def increment_counter(state):
    state['count'] += 1

s = {'count': 0}
increment_counter(s)
print(s)
```
