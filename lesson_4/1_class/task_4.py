#!/usr/bin/python3

"""
У нас есть класс. Создайте 3 героев:

pythomir, flaskomir, djangomir (последние два недолюбливают друг друга).

Убедитесь, что они имеют класс Hero.
Добавьте героев в список heroes.
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


pythomir = ...
flaskomir = ...
djangomir = ...

heroes = 

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)
assert len(heroes) == 3, "в списке не три героя"
assert isinstance(pythomir, Hero) , "pythomir – не экземпляр Hero"
assert isinstance(flaskomir, Hero) , "flaskomir – не экземпляр Hero"
assert isinstance(djangomir, Hero) , "djangomir – не экземпляр Hero"
print("Условия выполнены")
"""


# Решение
class Hero:

    def go_right(self):
        print("Я иду направо")

    def go_left(self):
        print("Я иду налево")

    def observe(self):
        print("Я осматриваюсь")


pythomir = Hero()
flaskomir = Hero()
djangomir = Hero()

heroes = [pythomir, flaskomir, djangomir]

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)
assert len(heroes) == 3, "в списке не три героя"
assert isinstance(pythomir, Hero), "pythomir – не экземпляр Hero"
assert isinstance(flaskomir, Hero), "flaskomir – не экземпляр Hero"
assert isinstance(djangomir, Hero), "djangomir – не экземпляр Hero"
print("Условия выполнены")
