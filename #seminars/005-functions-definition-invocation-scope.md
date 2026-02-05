# 005 - Functions: Definition, Invocation, and Scope

Objectives

- Define and call functions with parameters and return values.
- Explain local vs global scope and variable lifetime.
- Use simple modularization to structure programs.

Description

Covers function definition, parameter passing, return values, and scope. Students learn how to break problems into reusable functions, avoid common scoping bugs, and apply simple modular design principles to keep code readable. (36 words)

Outline

1. Defining functions and calling them
2. Parameters, defaults, and return values
3. Variable scope: local vs global
4. Modular design and code reuse
5. Simple debugging of function behavior

Exercises

- Short coding exercise: Write a function that returns the factorial of a non-negative integer and test it.
- Mini-project: Refactor a small script into functions (input parsing, processing, output) and demonstrate improved clarity.

Sample Code (Python)

```python
# factorial.py
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
```

Resources

- Python docs: Defining Functions (https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- Articles on modularization and design
