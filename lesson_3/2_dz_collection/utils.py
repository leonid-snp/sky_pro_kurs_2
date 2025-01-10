import json


def open_file(name: str, mode: str) -> dict:
    """
    Читает файл и возвращает содержимое.
    :param name: (str) название файла
    :param mode: (str) режим чтения
    :return: (dit) словарь с данными
    """
    with open(name, mode) as file:
        return json.load(file)


def get_student_by_pk(pk: int) -> dict | str:
    """
    Получает словарь с данными студента по его pk.
    :param pk: (int) номер студента
    :return: (dict) словарь с данными
    """
    list_students = open_file("data/students.json", "r")
    for student in list_students:
        if student["pk"] == pk:
            return student
    print("У нас нет такого студента")
    return quit()


def get_profession_by_title(title: str) -> dict | str:
    """
    Получает словарь с инфо о профессии по названию.
    :param title: (str) название профессии
    :return: (dict) словарь с данными
    """
    list_professions = open_file("data/professions.json", "r")
    for profession in list_professions:
        if profession["title"] == title:
            return profession
    print("У нас нет такой специальности")
    return quit()


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Возвращает словарь с данными о совпадении.
    :param student: (dict) данные студента
    :param profession: (dict) данные профессии
    :return: (dict) данные о совпадении
    """
    data_student = student
    data_profession = profession
    lacks_skills = set(data_profession["skills"]).difference(data_student["skills"])
    data_check_fitness = {
        "has": data_student["skills"],
        "lacks": lacks_skills,
        "fit_percent": int(100 - (len(lacks_skills) / len(data_profession["skills"])) * 100)
    }
    return data_check_fitness


def main() -> None:
    """
    Запускает программу по подбору персонала.
    :return: (None)
    """
    student_pk = int(input("Введите номер студента: "))
    data_student = get_student_by_pk(student_pk)
    full_name_student = data_student["full_name"]
    print(f"Студент {full_name_student}\n"
          f"Знает {', '.join(data_student["skills"])}\n")

    profession = input(f"Выберите специальность для оценки студента {full_name_student}: ").capitalize()
    data_profession = get_profession_by_title(profession)
    data_check_fitness = check_fitness(data_student, data_profession)
    print(f"Пригодность {data_check_fitness["fit_percent"]}%\n"
          f"{full_name_student} знает {', '.join(data_check_fitness["has"])}\n"
          f"{full_name_student} не знает {', '.join(data_check_fitness['lacks'])}")


if __name__ == '__main__':
    main()
