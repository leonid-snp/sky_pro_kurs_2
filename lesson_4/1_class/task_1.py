#!/usr/bin/python3

"""
На самом деле мы уже работали с экземплярами классов, просто не знали об этом.
Чтобы плавно приступить к написанию классов, начнем с использования готового класса.
Создайте экземпляр класса Hero
затем вызовите несколько раз методы нового героя, чтобы получилось:

Я иду налево
Я осматриваюсь
Я иду направо
Я иду направо
Я иду направо
Я осматриваюсь
Я иду направо
"""

# Задача
"""
class Hero:

  def go_right(self):
    print("Я иду направо")

  def go_left(self):
    print("Я иду налево")

  def observe(self):
    print("Я осматриваюсь")

hero = Новый герой

hero.идиналево()
hero.идинаправо()
"""


# Решение
class Hero:

    def go_right(self):
        print("Я иду направо")

    def go_left(self):
        print("Я иду налево")

    def observe(self):
        print("Я осматриваюсь")


hero = Hero()

hero.go_left()
hero.observe()
hero.go_right()
hero.go_right()
hero.go_right()
hero.observe()
hero.go_right()
