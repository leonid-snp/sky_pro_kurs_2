#!/usr/bin/python3

"""
Выше мы уже видели структуру данных с высокой вложенностью.
Напишите код, который считает количество отзывов и среднюю оценку.

Формат вывода:
Всего отзывов: 9
Средняя оценка: 4.3
"""

# Задача
"""
...
"""

# Решение
from task_1_1 import reviews


def get_info(_list: list[dict]) -> str:
    avg_stars = 0
    count_sms = len(_list)
    for item in _list:
        avg_stars += item['fields']['stars']
    return (f"Всего отзывов: {count_sms}\n"
            f"Средняя оценка: {avg_stars / count_sms}")

print(get_info(reviews))
