import random

import requests
from basic_word import BasicWord


def get_list_word() -> list | str:
    """
    Возвращает список с данными.
    :return: (list) словарь с данными
    """
    response = requests.get('https://api.npoint.io/eee582e173e0f5c3ba30')
    if response.status_code == 200:
        return response.json()
    return f"Что то пошло не так: {response.status_code}"


def get_random_word() -> dict:
    """
    Возвращает случайный набор данных одного слова.
    :return: (dict) данные о слове
    """
    list_data = get_list_word()
    return random.choice(list_data)


def create_instance_class():
    """
    Возвращает объект класса.
    :return: (object) объект класса
    """
    data = get_random_word()
    return BasicWord(**data)

def get_correct_word(num: int) -> str:
    """
    Возвращает корректное отображение слова: "слов"
    :param num: (int) число для склонения слова
    :return: (str) корректное отображение
    """
    if num == 1:
        return "слово"
    elif 2 <= num <= 4:
        return "слова"
    elif num in (0, *range(5, 16)):
        return "слов"
