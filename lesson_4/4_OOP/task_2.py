#!/usr/bin/python3

"""
Унаследуйте от класса Enemy класс Dragon.

Добавьте дочернему классу методы:

bite (выводит "я кусаюсь"),
burn (выводит "я дышу огнем").
"""

# Задача
"""
class Enemy():

  def __init__(self, name, health):

    self.is_alive = True;
    self.name = name
    self.health = health


...

dragon = Dragon("Инхеритий Проворный", 300)

# Не удаляйте код ниже, это проверка!

dragon.bite()
dragon.burn()
"""


# Решение
class Enemy:

  def __init__(self, name: str, health: int) -> None:

    self.is_alive = True
    self.name = name
    self.health = health


class Dragon(Enemy):

    def bite(self) -> None:
        print("я кусаюсь")

    def burn(self) -> None:
        print("я дышу огнем")

dragon = Dragon("Инхеритий Проворный", 300)

# Не удаляйте код ниже, это проверка!

dragon.bite()
dragon.burn()
