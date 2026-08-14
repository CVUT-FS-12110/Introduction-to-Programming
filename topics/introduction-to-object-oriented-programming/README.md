## 5. Object-Oriented Programming (OOP)

OOP helps you organize your code around objects - things that have properties (data) and behaviors (functions).
For example, a `Car` can have a color (property) and a `drive()` function (behavior).

OOP is one of the most important concepts in programming!

---

### What Is a Class and an Object?

- **Class** – a blueprint for creating objects
- **Object** – an instance of a class

Think of a class like a *recipe*, and an object like the *cake* you bake from that recipe.

---

### Defining a Simple Class

You can use `raise` to generate a custom error when certain conditions aren’t met.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving!")

# Create an object
my_car = Car("Toyota", "red")
my_car.drive()
```
`__init__()` is called automatically when a new object is created.

`self` refers to the current object.

Example output:
```
The red Toyota is driving!
```

---

### Attributes and Methods

| Term          | Meaning                     | Example                         |
| ------------- | --------------------------- | ------------------------------- |
| **Attribute** | A variable inside an object | `self.color`                    |
| **Method**    | A function inside a class   | `def drive(self):`              |
| **Object**    | An instance of a class      | `my_car = Car("Toyota", "red")` |

---

### Example: Dog Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

dog1.bark()
dog2.bark()
```

Example output:
```
Buddy says woof!
Lucy says woof!
```

---

### Adding and Modifying Attributes

You can change object properties after creation:

```python
dog1.age = 4
print(dog1.age)
```

Example output:
```
4
```

You can also add new attributes dynamically:

```python
dog1.breed = "Golden Retriever"
print(dog1.breed)
```

Example output:
```
Golden Retriever
```

---

### Inheritance

A class can inherit from another class - it means the child class can use all attributes and methods of the parent.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

cat = Cat()
cat.speak()
```
The child class (`Cat`) can override methods from the parent class (`Animal`).

Example output:
```
Meow!
```
---

### Summary - Object-Oriented Programming

| Concept         | Description                 | Example              |
| --------------- | --------------------------- | -------------------- |
| **Class**       | Blueprint for objects       | `class Car:`         |
| **Object**      | Instance of a class         | `my_car = Car()`     |
| **Attribute**   | Variable in a class         | `self.name`          |
| **Method**      | Function in a class         | `def drive(self):`   |
| **Constructor** | Initializes an object       | `__init__()`         |
| **Inheritance** | Child class inherits parent | `class Dog(Animal):` |

---