# 006 - Introduction to Objects (OOP Basics)

**Objectives**

- Understand the concepts of classes and objects.
- Define simple classes with attributes and methods.
- Explain encapsulation and basic inheritance.

**Description**

An introductory seminar to Object-Oriented Programming concepts: classes, instances, methods, and simple inheritance. Students will model real-world entities as classes, interact with objects, and see how encapsulation improves code organization.

**Outline**

1. Objects vs classes
2. Attributes and methods
3. Constructors and instance state
4. Encapsulation and access patterns
5. Simple inheritance and composition

**Exercises**

- Short coding exercise: Implement a Point class with x,y coordinates and a distance method.
- Mini-project: Model a small domain (e.g., library books and members) with classes and basic interactions.

**Resources**

- Official Python tutorial: Classes (https://docs.python.org/3/tutorial/classes.html)
- OOP primer articles (various)

---

Example: Point class

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

# demo
if __name__ == '__main__':
    p = Point(3, 4)
    print(p.distance_to_origin())  # 5.0
```
