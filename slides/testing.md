---
theme: uncover
class: invert
footer: 'Coder Trader | 28/07/25'
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
marp: true
---
# Testing

---

## 🧪 What is pytest?
pytest is a powerful Python testing tool used to write simple and scalable test cases.

## Installation
With pip
```
pip install pytest pytest-cov
```
with uv
```
uv add pytest pytest-cov
```
---
# Create code to test
We will create a calculator app in `calculator.py`
```python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```
---
## Set up tests
We will set up the testing folder `tests` and put the calculator test here `tests/test_calculator.py`
```python
from app.calculator import add, divide

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(1, 0)
```
you can run all the tests by running the command `pytest` or you can drill down to the specific test `pytest tests/test_calculator.py::test_add`

---
# Fixtures
A fixture in pytest is a reusable piece of setup code that provides data, resources, or configuration for tests. It helps you avoid repeating setup logic and makes your tests cleaner and more modular.

- `@pytest.fixture` marks a function as a fixture.

- It can be automatically injected into tests that request it by name.
