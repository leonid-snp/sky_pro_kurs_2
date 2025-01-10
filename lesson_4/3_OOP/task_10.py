#!/usr/bin/python3

"""
У вас есть класс Room c полями

Номер номера (number) – целое число

Свободно ли (is_free) – булев тип

Допишите функцию, которая перебирает список номеров и возвращает список свободных номеров (список экземпляров класса Room).
"""
from xml.dom import NoModificationAllowedErr

# Задача
"""
class Room:

    def __init__(self, number, is_free):
        self.number = number
        self.is_free = is_free


def get_free_rooms(rooms):
    free_rooms = []
    ...
    return free_rooms


rooms = [Room(14, True), Room(15, False), Room(16, True)]
rooms_free = get_free_rooms(rooms)

# Не удаляйте этот код, он нужен для проверки

[print(r.number) for r in rooms_free]
"""


# Решение
class Room:

    def __init__(self, number: int, is_free: bool) -> None:
        self.number = number
        self.is_free = is_free


def get_free_rooms(rooms):
    free_rooms = [room for room in rooms if room.is_free is True]
    return free_rooms


rooms = [Room(14, True), Room(15, False), Room(16, True)]
rooms_free = get_free_rooms(rooms)

# Не удаляйте этот код, он нужен для проверки

[print(r.number) for r in rooms_free]
