import json


def open_file(file: str) -> list[dict]:
    """
    Читает файл json и возвращает словарь.
    :param file: (str) название файла
    :return: (list[dict]) список словарей с данными
    """
    with open(file, "r") as file:
        return json.load(file)

