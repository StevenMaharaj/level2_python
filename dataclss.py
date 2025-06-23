from dataclasses import dataclass

# @dataclass
# class Employee:
#     name: str
#     emp_id: int
#     department: str
#     salary: float

# emp1 = Employee("John Doe", 1001, "Engineering", 75000.0)

# # Accessing fields
# print(f"Employee Name: {emp1.name}")
# print(f"Employee ID: {emp1.emp_id}")
# print(f"Department: {emp1.department}")
# print(f"Salary: ${emp1.salary:.2f}")

# @dataclass
# class Book:
#     title: str
#     author: str
#     pages: int = 0
#     price: float = 0.0

# # Example usage
# book1 = Book("1984", "George Orwell", 328, 9.99)
# print(f"Book Title: {book1.title}")

# @dataclass(frozen=True)
# class Point:
#     x: float
#     y: float

# # Example usage
# point1 = Point(3.0, 4.0)

# Can't modify a frozen dataclass
# point1.x = 5.0  # This will raise a FrozenInstanceError



@dataclass
class MyClass:
    attribute1: str
    attribute2: int

    def __post_init__(self):
        # Perform additional initialization here
        self.attribute3 = self.attribute1 + str(self.attribute2)