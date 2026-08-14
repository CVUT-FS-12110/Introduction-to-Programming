## **1. Introduction to Python Basics**

### `print()` – Displaying Output
Prints the specified message to the screen.
```python
print("Hello World!")
```
Always put text inside quotation marks (`" "` or `' '`) — otherwise, Python thinks it’s a variable name, not text.

Example output:
```
Hello World!
```

---

### `Variables` – Storing Information
A variable is a name used to store data so you can reuse it later.

Think of it as a labeled box where you keep a value.
```python
name = "Bob"
age = 27
print(name)
print(age)
```
Variable names cannot have spaces and must start with a letter or underscore.

Example output:
```
Bob
27
```
---

### `Data Types` – Numbers, Text and Booleans
Python can store different types of data:
- `str` – String: text, written in quotes
- `int` – Integer: whole numbers
- `float` – Float: decimal numbers
- `bool` – Boolean: `True` or `False`

```python
name = "Bob"      # string
age = 27          # integer
height = 1.75     # float
is_student = True # boolean
```

---

### `input()` – Getting User Input
You can ask the user for input using the `input()` function.

Everything entered by the user is read as text (a string).

```python
name = input("Enter your name: ")
print("Hello,", name, "!")
```
Example output:
```
Enter your name: Bob
Hello, Bob !
```

---

### Simple Arithmetic
| Operation          | Symbol | Example  | Result |
| ------------------ | ------ | -------- | ------ |
| Addition           | `+`    | `2 + 2`  | 4      |
| Subtraction        | `-`    | `4 - 1`  | 3      |
| Multiplication     | `*`    | `5 * 2`  | 10     |
| Division           | `/`    | `8 / 2`  | 4.0    |
| Floor division     | `//`   | `8 // 3` | 2      |
| Modulo (remainder) | `%`    | `7 % 3`  | 1      |
| Power              | `**`   | `2 ** 3` | 8      |

```python
a = 10
b = 3
print("Sum:", a + b)
print("Remainder:", a % b)
```
Example output:
```
Sum: 13
Remainder: 1
```

---

### Simple Assignment Operators

| Operator | Example   | Same as      | Description                            |
| -------- | --------- | ------------ | -------------------------------------- |
| `=`      | `x = 5`   | `x = 5`      | Assigns value 5 to variable `x`        |
| `+=`     | `x += 3`  | `x = x + 3`  | Adds and assigns the result            |
| `-=`     | `x -= 2`  | `x = x - 2`  | Subtracts and assigns the result       |
| `*=`     | `x *= 4`  | `x = x * 4`  | Multiplies and assigns the result      |
| `/=`     | `x /= 2`  | `x = x / 2`  | Divides and assigns the result (float) |
| `%=`     | `x %= 3`  | `x = x % 3`  | Modulus (remainder) and assign         |
| `//=`    | `x //= 2` | `x = x // 2` | Floor division and assign (integer)    |
| `**=`    | `x **= 2` | `x = x ** 2` | Exponentiation and assign              |
| `&=`     | `x &= 3`  | `x = x & 3`  | Bitwise AND and assign                 |
| `\|=`    | `x \|= 2` | `x = x \| 2` | Bitwise OR and assign                  |
| `^=`     | `x ^= 2`  | `x = x ^ 2`  | Bitwise XOR and assign                 |
| `>>=`    | `x >>= 1` | `x = x >> 1` | Bitwise right shift and assign         |
| `<<=`    | `x <<= 1` | `x = x << 1` | Bitwise left shift and assign          |

```python
count = 0
count += 1
print("Result:", count)
```
Example output:
```
Result: 1
```

---

## **2. Collections in Python**

Collections let you store multiple values in a single variable.

The four main built-in types in Python are:
| Type           | Ordered             | Changeable | Allows Duplicates     | Syntax         |
| -------------- | ------------------- | ---------- | --------------------- | -------------- |
| **List**       | ✅ Yes               | ✅ Yes      | ✅ Yes                 | `[ ]`          |
| **Tuple**      | ✅ Yes               | ❌ No       | ✅ Yes                 | `( )`          |
| **Set**        | ❌ No                | ✅ Yes      | ❌ No                  | `{ }`          |
| **Dictionary** | ✅ Yes (Python 3.7+) | ✅ Yes      | ❌ Keys must be unique | `{key: value}` |

---

### **Lists**
A list stores multiple items in a specific order and can be changed.

```python
fruits = ["apple", "banana", "cherry"]
```
**Accessing elements:**
```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # first item
print(fruits[2])   # third item
print(fruits[-1])  # last item
```

Note: Comments starts with a `#`, and Python will ignore them.

Example output:
```
apple
cherry
cherry
```
**Modifying a list:**
```python
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")  # add
fruits[1] = "kiwi"       # change
fruits.remove("apple")   # remove
print(fruits)
```
Example output:
```
['kiwi', 'cherry', 'orange']
```
**Common List functions:**
| Function      | Description        | Example          | Result    |
| ------------- | ------------------ | ---------------- | --------- |
| `len(list)`   | Number of items    | `len(fruits)`    | 3         |
| `sum(list)`   | Sum of all numbers | `sum([2, 4, 6])` | 12        |
| `max(list)`   | Largest value      | `max([3, 7, 1])` | 7         |
| `min(list)`   | Smallest value     | `min([3, 7, 1])` | 1         |
| `list.sort()` | Sorts in order     | `[3,1,2].sort()` | `[1,2,3]` |

---

### **Tuples**

A tuple is like a list, but it cannot be changed (it’s immutable).

```python
colors = ("red", "green", "blue")
print(colors[0])
```
If you try to modify it:
```python
colors[0] = "yellow"
```
You’ll get an error, because tuples can’t be changed.

Use tuples when your data shouldn’t change (like days of the week).

---

### **Sets**

A set is an unordered collection of unique items.
```python
numbers = {1, 2, 3, 3, 4}
print(numbers)
```
Example output:
```
{1, 2, 3, 4}
```
Notice: duplicates are removed automatically.

You can also perform set operations:
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))        # combine sets
print(a.intersection(b)) # common elements
```
Example output:
```
{1, 2, 3, 4, 5}
{3}
```

---

### **Dictionaries**

A dictionary stores data in key–value pairs.

```python
person = {"name": "Bob", "age": 27, "city": "Prague"}
print(person["name"])  # access value by key
```
Example output:
```
Bob
```

**Add or modify values:**

```python
person["age"] = 26
person["job"] = "Engineer"
print(person)
```
Example output:
```
{'name': 'Bob', 'age': 26, 'city': 'Prague', 'job': 'Engineer'}
```

---

## **3. Conditional Statements (if/elif/else)**

Conditional statements let your program make decisions - they control what happens based on certain conditions.

---

### `if` Statement
The `if` statement runs a block of code only if the condition is true.
```python
x = 10
if x > 5:
    print("x is greater than 5")
```
Indentation (spaces before the line) is very important in Python.
Use 4 spaces (or press Tab once) to indent code inside an if block.

Example output:
```
x is greater than 5
```

---

### `if ... else` Statement
The `else` block runs if the condition is not true.
```python
number = 0
if number > 0:
    print("Positive number")
else:
    print("Negative number or zero")
```

Example output:
```
Negative number or zero
```

---

### `if ... elif ... else` Statement
When you have multiple conditions, use elif (“else if”).
```python
temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")
```

Example output:
```
It's warm outside.
```

---

### Comparison and Logical Operators

| Operator | Meaning                  | Example  | Result |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `5 == 5` | `True` |
| `!=`     | Not equal to             | `5 != 3` | `True` |
| `>`      | Greater than             | `8 > 6`  | `True` |
| `<`      | Less than                | `3 < 5`  | `True` |
| `>=`     | Greater than or equal to | `6 >= 6` | `True` |
| `<=`     | Less than or equal to    | `4 <= 5` | `True` |

**Logical operators** let you combine conditions:
- `and` – both conditions must be True
- `or` – at least one condition must be True
- `not` – reverses the condition

```python
age = 18
if age >= 18 and age < 65:
    print("You are an adult.")
```

Example output:
```
You are an adult.
```

---