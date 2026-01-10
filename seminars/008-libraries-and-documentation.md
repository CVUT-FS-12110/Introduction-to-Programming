# 008 - Libraries & Documentation

**Objectives**

- Use third-party libraries and manage dependencies.
- Read and write effective docstrings and inline comments.
- Use package managers to install and isolate libraries (pip, venv).

**Description**

Covers how to find, install, and use external libraries safely, plus writing clear documentation and docstrings. Students practice reading library docs, using virtual environments, and documenting functions for others.

**Outline**

1. Finding and selecting libraries
2. Package management and virtual environments
3. Reading API docs and examples
4. Writing docstrings and inline comments
5. Licensing and community resources

**Exercises**

- Short coding exercise: Install a small library (e.g., requests), and call a simple API.
- Mini-project: Create a small module, write docstrings and a README, and publish locally into a venv for demonstration.

**Resources**

- pip and venv docs
- Docstring conventions (PEP 257)

---

Example: using requests (requires installing the requests package)

```python
# example using requests
import requests

r = requests.get('https://httpbin.org/get')
print(r.status_code)
```
