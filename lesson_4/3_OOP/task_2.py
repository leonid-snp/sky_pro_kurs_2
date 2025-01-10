#!/usr/bin/python3

"""
Создай класс Student (студент) с полями

Имя (name) - строка
Курс (course) - целое число
Создай два экземпляра

Алиса, 3
Маргарита, 2
"""

# Задача
"""
class ...:

    def __init__(...):

student_1 = ...
student_2 = ...


# Не удаляйте этот код, он нужен для проверки

print(student_1.name, student_1.course)
print(student_2.name, student_2.course)
"""


# Решение
class Student:

    def __init__(self, name: str, course: int) -> None:
        self.name = name
        self.course = course


student_1 = Student("Алиса", 3)
student_2 = Student("Маргарита", 2)

# Не удаляйте этот код, он нужен для проверки

print(student_1.name, student_1.course)
print(student_2.name, student_2.course)
