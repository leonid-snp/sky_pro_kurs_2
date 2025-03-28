#!/usr/bin/python3

"""
Напишите метод инициализации, который принимает два аргумента: name, motto — и записывает их в свойства класса.
"""

# Задача
"""
class Hero:
  def __init__(self, ..., ...):
    self.name = ...


pythomir = Hero("Питомир", "Кусь за Русь")
flaskomir = Hero("Фласкомир", "Это нужно отметить")
djangomir = Hero("Джангомир", "Работает – и ладно!")

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

if not hasattr(pythomir, "name"): print("Имя не задано")
if not hasattr(pythomir, "motto"): print("Девиз не задан")
print("Условия выполнены")
"""


# Решение
class Hero:
    def __init__(self, name: str, motto: str) -> None:
        self.name = name
        self.motto = motto


pythomir = Hero("Питомир", "Кусь за Русь")
flaskomir = Hero("Фласкомир", "Это нужно отметить")
djangomir = Hero("Джангомир", "Работает – и ладно!")

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

if not hasattr(pythomir, "name"): print("Имя не задано")
if not hasattr(pythomir, "motto"): print("Девиз не задан")
print("Условия выполнены")
