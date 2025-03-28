#!/usr/bin/python3

"""
Опишите класс Box, у которого будут свойства:

size weight contains и метод observe(), который возвращает:

Это похоже на ящик размером 30x30 и весом 35кг

Наследуйте от него класс Container.

Он будет отличаться наличием метода open(), который возвращает то, что лежит в ящике, например:

В ящике размером 40x40 и весом 1кг оказалось 4 кг апельсинов

Создайте экземпляр box_1 с размерами 30x30, весом 1 и содержимым "15 золотых монет".

Создайте экземпляр container_1 с размерами 50x30, весом 2 и содержимым "7 золотых монет".
"""

# Задача
"""
class ...
  pass

class ...()
  pass

box_1 = 

container_1 = 

# Код проверки, не удаляйте его

try: Box
except:print("Класс Box не задан")
try: Container
except:print("Класс Container не задан")
try: Container.open
except:print("Метод open у Container не задан или с ошибкой")
try: Container.observe
except:print("Метод observe у Container не наследуется или с ошибкой")
try: box_1
except:print("Экземпляр box_1 не существует")
try: container_1
except:print("Экземпляр container_1 не существует")

print(container_1.observe())
print(container_1.open())
"""


# Решение
class Box:

    def __init__(self, size: str, weight: int, contains: str) -> None:
        self.size = size
        self.weight = weight
        self.contains = contains

    def observe(self) -> str:
        return f"Это похоже на ящик размером {self.size} и весом {self.weight}кг"


class Container(Box):

    def open(self) -> str:
        return f"В ящике размером {self.size} и весом {self.weight}кг оказалось {self.contains}"


box_1 = Box("30x30", 1, "15 золотых монет")

container_1 = Container("50x30", 2, "7 золотых монет")

# Код проверки, не удаляйте его

try:
    Box
except:
    print("Класс Box не задан")
try:
    Container
except:
    print("Класс Container не задан")
try:
    Container.open
except:
    print("Метод open у Container не задан или с ошибкой")
try:
    Container.observe
except:
    print("Метод observe у Container не наследуется или с ошибкой")
try:
    box_1
except:
    print("Экземпляр box_1 не существует")
try:
    container_1
except:
    print("Экземпляр container_1 не существует")

print(container_1.observe())
print(container_1.open())
