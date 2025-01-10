#!/usr/bin/python3

"""
Некоторые рыбы предпочитают морскую воду, некоторые — пресную.
Разделите список словарей на два, затем выведите названия вида из каждого словаря в строку.
Вот так:

Морские: Тунец, Скумбрия
Пресноводные: Красноперка, Карась
"""

# Задача
"""
fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []
"""

# Решение
fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]

sea_water = [sea["specie"] for sea in fish if sea["water"] == "sea"]
fresh_water = [fresh["specie"] for fresh in fish if fresh["water"] == "fresh"]

print(f"Морские: {', '.join(sea_water)}\n"
      f"Пресноводные: {', '.join(fresh_water)}")