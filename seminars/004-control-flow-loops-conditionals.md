# 004 - Control Flow: Loops and Conditionals

Objectives

- Use conditional statements to branch program logic.
- Implement loops (for, while) and control statements (break/continue).
- Choose the correct control flow for a given algorithm.

Description

Focuses on decision-making and repetition in programs. Students will practice writing clear conditionals and loop constructs, learn common loop patterns, and debug typical logical errors like off-by-one faults. (33 words)

Outline

1. if/elif/else and boolean logic
2. for loops and iteration patterns
3. while loops and loop invariants
4. Loop control: break, continue, else
5. Common pitfalls and debugging strategies

Exercises

- Short coding exercise: Write a program that prints the first N Fibonacci numbers using a loop.
- Mini-project: Implement a simple menu-driven CLI that uses loops and conditionals to manage user choices.

Sample Code (Python)

```python
# fibonacci.py
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
```

Resources

- Python docs: Control Flow (https://docs.python.org/3/tutorial/controlflow.html)
- Articles on common loop mistakes
