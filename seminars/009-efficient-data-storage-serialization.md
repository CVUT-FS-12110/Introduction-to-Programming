# 009 - Efficient Data Storage: Serialization

**Objectives**

- Explain serialization formats (JSON, CSV, binary).
- Serialize and deserialize simple data structures.
- Choose formats based on use-case tradeoffs.

**Description**

An overview of serializing data for storage and interchange: JSON, CSV, and simple binary formats. Students learn to persist structured data, load it back, and reason about tradeoffs like readability vs size.

**Outline**

1. Formats: JSON, CSV, binary (pickle) basics
2. Encoding and data types mapping
3. Reading/writing serialized data
4. Performance and security considerations
5. When to use which format

**Exercises**

- Short coding exercise: Save a list of dictionaries to JSON and load it back.
- Mini-project: Implement a small data export/import tool that converts between CSV and JSON for a dataset.

**Resources**

- JSON spec and tutorials
- Python json and csv module docs

---

Example: JSON dump/load

```python
import json

data = [{'name':'Alice','age':30},{'name':'Bob','age':25}]
# write using json.dumps to produce a string and avoid static typing warnings
with open('data.json','w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2))

with open('data.json','r', encoding='utf-8') as f:
    loaded = json.load(f)
print(loaded)
```
