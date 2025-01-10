#!/usr/bin/python3

"""
Создай класс Number c полем value (указывается при инициализации)

Добавь методы:

.get() возвращает текущее value
.add(<значение>) добавляет указанное число к value
.subtract(<значение>)вычитает указанное число из value
"""

# Задача
"""
class Number:

    def __init__(self, value):
        ...

    def ...(self):
        ...

    def ...:
        ...

    def ...:
        ...
# Пример использования, не влияет ни на что, можно удалить.

x = Number(7)
x.add(3)
x.subtract(10)
x.get()

# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())
"""


# Решение
class Number:

    def __init__(self, value: int) -> None:
        self.value = value

    def get(self) -> int:
        return self.value

    def add(self, value: int) -> None:
        self.value += value

    def subtract(self, value: int) -> None:
        self.value -= value

# Пример использования, не влияет ни на что, можно удалить.

x = Number(7)
x.add(3)
x.subtract(10)
x.get()

# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())
