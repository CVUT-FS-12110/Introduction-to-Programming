# 010 - Testing Fundamentals

**Objectives**

- Understand the purpose of testing and common test types.
- Write simple unit tests and run them.
- Use assertions and basic test runners.

**Description**

Introduces testing principles: unit vs integration tests, writing assertions, and using a simple test runner (unittest or pytest). Students learn to write reproducible tests and interpret failures to improve code quality.

**Outline**

1. Why test? Types of tests
2. Writing unit tests and assertions
3. Using a test runner (unittest/pytest)
4. Test organization and simple mocks
5. Interpreting failures and debugging

**Exercises**

- Short coding exercise: Write unit tests for the factorial function and run them.
- Mini-project: Add tests for a small module and integrate running tests as a project command.

**Resources**

- pytest documentation
- Testing best practices articles

---

Example: simple pytest test

```python
# test_factorial.py (example)
from factorial import factorial

def test_factorial():
    assert factorial(5) == 120

# Run with: pytest -q
```
