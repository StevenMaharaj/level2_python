---
theme: uncover
class: invert
footer: 'Coder Trader | 23/06/25'
style: |
  body {
    background-color: #2E3440; /* Dark pastel background */
    color:rgb(65, 68, 71); /* Light pastel text */
  }
  h1, h2, h3 {
    font-size: 25px; /* Adjust as needed */
    color: #88C0D0; /* Soft pastel cyan for headers */
  }
  p {
    font-size: 15px; /* Adjust as needed */
    color:rgb(205, 209, 218); /* Light pastel text */
  }
  a {
    color: #A3BE8C; /* Pastel green for links */
  }
  code.language-python {
    font-size: 15px; /* Adjust as needed */
    background-color: #3B4252; /* Slightly darker for code blocks */
    color: #D08770; /* Muted pastel orange for code text */
  }
  ul, ol {
    font-size: 15px; /* Adjust as needed */
    color: rgb(205,209,218); /* Light pastel text */
  }
---

# Dataclasses

You get all the good stuff from classes with extra functionality and short cuts.

Docs: https://docs.python.org/3/library/dataclasses.html

---
# Example Dataclass

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    emp_id: int
    department: str
    salary: float

emp1 = Employee("John Doe", 1001, "Engineering", 75000.0)

# Accessing fields
print(f"Employee Name: {emp1.name}")
print(f"Employee ID: {emp1.emp_id}")
print(f"Department: {emp1.department}")
print(f"Salary: ${emp1.salary:.2f}")
```

 - `@dataclass decorator` marks the class Employee as a dataclass.

 - Each variable `(name, emp_id, department, salary)` represents a field in the dataclass.

---
# Default Values and Type Hinting

Dataclasses support default values and type hinting:

```python
@dataclass
class Book:
    title: str
    author: str
    pages: int = 0
    price: float = 0.0
```
---
# Frozen Dataclasses
You can create immutable dataclasses by adding the frozen=True parameter:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float
```
In a frozen `dataclass` (`Point`), once an instance is created, its fields cannot be modified, ensuring immutability.

---
# Using slots in Dataclasses

```python
from dataclasses import dataclass

@dataclass
class Player:
    __slots__ = ['name', 'score']
    name: str
    score: int
```
or
```python
@dataclass(slots=True)
class Player:
    name: str
    score: int

```

- You can use `__slots__` with dataclasses to optimize memory usage and restrict attribute creation. This can be useful when defining dataclasses with a large number of instances.
---
# Post Init
- The `__post_init__` method is a special method that allows you to perform additional initialization tasks after the object has been initialized with data. This method is particularly useful when you want to customize the initialization process or perform operations that depend on the initial state of the object.

- The `__post_init__` method is automatically called by Python's dataclasses module after the object has been initialized with data from the constructor (`__init__` method).

- It provides a convenient hook to execute code that needs to run after the object's attributes have been set.
---
# Post Init Example

To define a __post_init__ method, you simply add it to your dataclass with the appropriate logic you want to execute after initialization:

```python
from dataclasses import dataclass

@dataclass
class MyClass:
    attribute1: str
    attribute2: int

    def __post_init__(self):
        # Perform additional initialization here
        self.attribute3 = self.attribute1 + str(self.attribute2)
```
`attribute3` is calculated based on attribute1 and attribute2 after they have been initialized.

Use it for
- Derived Attributes: Calculate attributes that depend on the values of other attributes.

- Validation: Perform validation checks on the initialized attributes.

- Complex Initialization: Initialize complex data structures or connections based on the object's state.
