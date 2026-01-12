"""Runnable examples showing variables and simple OOP patterns.

Run:
    python examples/variables_and_oop.py

Change values and re-run to experiment.
"""

from typing import List

# -----------------------
# Variables examples
# -----------------------

# simple variables and types
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = False

# mutable vs immutable
nums = [1, 2, 3]  # list is mutable
text = "hello"    # str is immutable

def show_variables():
    print("-- Variables --")
    print(f"name={name!r} (type={type(name).__name__})")
    print(f"age={age} (type={type(age).__name__})")
    print(f"nums before: {nums}")
    nums.append(4)
    print(f"nums after append: {nums}")
    print()


# -----------------------
# OOP examples
# -----------------------

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old." 

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age})"


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, courses: List[str] = None):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses or []  # avoid mutable default

    def introduce(self) -> str:
        base = super().introduce()
        return f"{base} My student ID is {self.student_id}."

    @property
    def course_count(self) -> int:
        return len(self.courses)

    def enroll(self, course: str):
        if course not in self.courses:
            self.courses.append(course)


def show_oop_examples():
    print("-- OOP examples --")
    p = Person("Bob", 40)
    print(p.introduce())
    s = Student("Charlie", 22, "S1001")
    print(s.introduce())
    s.enroll("Math")
    s.enroll("English")
    print(f"{s.name} courses: {s.courses} (count={s.course_count})")
    print(f"repr(student): {s!r}")
    print()


def demonstrate_when_to_use_oop():
    print("-- When to use OOP --")
    print("Functions are great for small utilities.")
    print("Use classes when you have objects with state and behavior, e.g., Student.")
    print()


if __name__ == "__main__":
    show_variables()
    show_oop_examples()
    demonstrate_when_to_use_oop()
