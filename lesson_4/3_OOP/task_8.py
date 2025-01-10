#!/usr/bin/python3

"""
Создай класс Circle, с полем radius (указывается при инициализации)

Добавь методы:

get_radius() - возвращает радиус
get_diameter() - возвращает двойной радиус
get_perimeter() - возвращает 2*радиус*Пи (можно использовать pi=3.14 или math.pi)
"""

# Задача
"""
import math

class Circle:

    def __init__(...):
        ...

    def get_radius(self):
        ...

    def get_diameter(self):
        ...

    def get_perimeter(self):
        ...

# Не удаляйте этот код, он нужен для проверки

circle_1 = Circle(7)
print("радиус", circle_1.get_radius() )
print("диаметр", circle_1.get_diameter() )
print("периметр", round(circle_1.get_perimeter(),1))
"""

# Решение
import math


class Circle:

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def get_radius(self) -> int:
        return self.radius

    def get_diameter(self) -> int:
        return self.radius * 2

    def get_perimeter(self) -> float:
        return self.radius * 2 * 3.14


# Не удаляйте этот код, он нужен для проверки

circle_1 = Circle(7)
print("радиус", circle_1.get_radius())
print("диаметр", circle_1.get_diameter())
print("периметр", round(circle_1.get_perimeter(), 1))
