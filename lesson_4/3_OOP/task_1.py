#!/usr/bin/python3

"""
Создай класс Bottle (бутылка) c полями

Цвет (color) - строка
Объем (volume) - число с плавающей точкой
Создай три экземпляра

Красная 0.7
Белая 0.3
Черная 1.0
"""

# Задача
"""
class Bottle:

	def __init__(self, c.., v..):
		...
		...

bottle_1 = Bottle("Красная", 0.7)
bottle_2 = ...
bottle_3 = ...

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.volume)
print(bottle_2.color, bottle_2.volume)
print(bottle_3.color, bottle_3.volume)
"""


# Решение
class Bottle:

    def __init__(self, color: str, volume: float) -> None:
        self.color = color
        self.volume = volume


bottle_1 = Bottle("Красная", 0.7)
bottle_2 = Bottle("Белая", 0.3)
bottle_3 = Bottle("Черная", 1.0)

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.volume)
print(bottle_2.color, bottle_2.volume)
print(bottle_3.color, bottle_3.volume)
