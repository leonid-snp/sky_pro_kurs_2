#!/usr/bin/python3

"""
Теперь мы предоставим вам структуру данных с высокой вложенностью. Это данные экскурсоводов.
Выведите экскурсоводов, у которых количество туров больше или равно 5.

Формат вывода:
Андрей Васечкин | туров: 5
Георги Беридзе | туров: 5
"""

# Задача
"""
...
"""

# Решение
from task_2_1 import guides


def get_info(_list: list[dict]) -> str:
    five_tours = []
    for item in _list:
        if item['fields']['tours_count'] >= 5:
            five_tours.append(f"{item['fields']['full_name']} | туров: {item['fields']['tours_count']}")

    return '\n'.join(five_tours)


print(get_info(guides))
