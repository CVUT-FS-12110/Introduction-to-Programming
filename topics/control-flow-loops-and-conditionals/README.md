## **4. Loops**
Loops let you repeat code multiple times without writing it again and again.

They are useful when you need to perform a task many times or go through a collection of data.

---

### `while` Loop
A `while` loop repeats as long as its condition is **True**.

```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
```
Example output:
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```
Be careful with while loops - if the condition never becomes `False`, you’ll create an infinite loop.

**Summing Numbers with a `while` Loop:**

```python
total = 0
number = 1

while number <= 5:
    total += number
    number += 1

print("Total:", total)
```

Example output:
```
Total: 15
```

**Try it for yourself** – Simple Guessing Game:

```python
secret = 7
guess = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Guess again: "))

print("You got it!")
```

---