## **1. Functions**

Functions are **blocks of reusable code** that perform a specific task.

They help make your programs easier to read, test, and maintain.

---

### Defining and Calling a Function

You define a function using a keyword `def`, followed by the function name and parentheses `()`.

```python
def greet():
    print("Hello, Python learner!")
```
To run the function, call it by name:

```python
greet()
```

Example output:
```
Hello, Python learner!
```
---

### Functions with Parameters

Functions can take **parameters** - values you pass in when calling the function.

```python
def greet_user(name):
    print("Hello,", name + "!")

greet_user("Bob")
```
Here, `"Bob"` is an argument passed into the function parameter `name`.

Example output:
```
Hello, Bob!
```
---

### Functions That Return a Value

Functions can **return a result** instead of printing directly.

```python
def add(a):
    return a + 1

result = add(3)
print("Sum:", result)
```
The `return` statement sends a value back to the place where the function was called.

Example output:
```
Sum: 4
```
---

### Default Parameters

You can set a **default value** for a parameter - used when no argument is provided.

```python
def greet(name="friend"):
    print("Hello,", name + "!")

greet()
greet("John")
```
Example output:
```
Hello, friend!
Hello, John!
```
---

### Multiple Parameters

Functions can take multiple inputs - separate them with commas.

```python
def multiply(x, y):
    return x * y

print(multiply(4, 5))
```
Example output:
```
20
```
---

### Local and Global Variables

Variables created **inside a function** exist only there - they’re *local*.

```python
x = 10

def show_number():
    x = 5
    print("Inside function:", x)

show_number()
print("Outside function:", x)
```
Example output:
```
Inside function: 5
Outside function: 10
```
---

### Summary - Functions in Python

| Concept           | Description                 | Example                       |
| ----------------- | --------------------------- | ----------------------------- |
| Define a function | Create reusable code block  | `def greet():`                |
| Call a function   | Run the code inside it      | `greet()`                     |
| Parameter         | Value passed into function  | `def add(a):`                 |
| Return value      | Send result back            | `return a + 1`                |
| Default value     | Optional parameter value    | `def greet(name="friend"):`   |
| Local variable    | Exists only inside function | `x` inside `def` block        |
| Global variable   | Accessible everywhere       | Declared outside any function |

---