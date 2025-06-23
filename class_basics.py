class Dog:
    # class attribute
    _count = 0

    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        Dog._count += 1
        
    def bark(self) -> None:
        print(f"{self.name} says woof!")

    def birthday(self) -> None:
        self.age += 1

    @classmethod
    def how_many(cls) -> int:
        return cls._count

    @staticmethod
    def attack():  # Utility; no access to cls or self
        return "Attack initiated!"

    @staticmethod
    def are_dog_cool():
        return "Dogs are cool!"

    def __str__(self) -> str:
        return f"{self.name} is ({self.age} yrs)"
    


