# 007 - File Handling: Reading from and Writing to Files

**Objectives**

- Open, read, and write files safely.
- Use context managers for resource management.
- Handle common file errors and encoding issues.

**Description**

Students learn practical file I/O: reading and writing text/binary files, using context managers, and handling encoding and errors safely. Includes patterns for logging data and simple file-based persistence.

**Outline**

1. Opening files and modes
2. Reading vs writing, text and binary
3. Context managers (with statement)
4. Encoding and newline handling
5. Error handling and file paths

**Exercises**

- Short coding exercise: Read a CSV-like file and print its rows.
- Mini-project: Implement a small logger that appends timestamped messages to a file and rotates when the file gets large.

**Resources**

- Python docs: File I/O (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- Articles on handling CSV and JSON files

---

Example: simple write/read

```python
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```
