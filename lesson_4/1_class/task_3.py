#!/usr/bin/python3

"""
В качественных играх на каждом новом уровне герои открывают в себе новые способности.
А кто реализует их? Программисты, конечно!

Добавьте классу Hero методы:

go_up - выводит "Я иду наверх"
go_down - выводит "Я иду вниз"
rest - выводит "Я отдыхаю"

Напишите код, который реализует патрулирование:

Я иду наверх
Я иду наверх
Я осматриваюсь
Я иду вниз
Я иду вниз
Я отдыхаю
"""

# Задача
"""
class Hero:

  def go_right(self):
    print("Я иду направо")

  def go_left():
    print("Я иду налево")

  def observe():
    print("Я осматриваюсь")

  ...

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

    def go_up(self):
        print("Я иду наверх")

    def go_down(self):
        print("Я иду вниз")

    def relax(self):
        print("Я отдыхаю")


hero = Hero()

hero.go_up()
hero.go_up()
hero.observe()
hero.go_down()
hero.go_down()
hero.relax()
