#!/usr/bin/python3

"""
Создай класс Bottle (бутылка) c полями

Цвет (color) - строка
Содержимое в мл (contains) - число с плавающей точкой
При инициализации класса, поле contains устанавливается = 0

Создай два экземпляра класса

Красная
Синяя

Добавь классу Bottle метод get_content
который вернет актуальное количество жидкости внутри в виде числа с плавающей точкой.

Добавь классу Bottle метод fill(volume)
который увеличит contains на указанный объем.
"""

# Задача
"""
class Bottle:
  def __init__(self, color):
    ...

  def get_content(self):
    ...

  def fill(self, volume):
     ...


bottle_1 = ...
bottle_2 = ...


# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())
"""


# Решение
class Bottle:
    def __init__(self, color: str) -> None:
        self.color = color
        self.contains = 0

    def get_content(self):
        return float(self.contains)

    def fill(self, volume):
        self.contains += volume


bottle_1 = Bottle("Красная")
bottle_2 = Bottle("Синяя")

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())
