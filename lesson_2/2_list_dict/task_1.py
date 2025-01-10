#!/usr/bin/python3

"""
Перенесите в подсписок vaccinated только сотрудников, которые прошли вакцинацию, а остальных отправьте в not_vaccinated.
Затем распечатайте оба списка в таком формате:

Вакцинированные:
Киселёв Всеволод Эдуардович
...
Остальные:
Довлатова Эмилия Ефимовна
"""

# Задача
"""
employees = [

 {"fio": "Киселёв Всеволод Эдуардович", "vaccinated": True},
 {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
 {"fio": "Аверин Мартын Егорович", "vaccinated": True},
 {"fio": "Князева Августа Егоровна", "vaccinated": False}, 
 {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
 {"fio": "Куприна Марина Викторовна", "vaccinated": False},
 {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},   
]

vaccinated = []
not_vaccinated = []
"""

# Решение
employees = [

    {"fio": "Киселёв Всеволод Эдуардович", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = [employ for employ in employees if employ["vaccinated"] is True]
not_vaccinated = [employ for employ in employees if employ["vaccinated"] is False]

print("Вакцинированные:")
[print(fio["fio"]) for fio in vaccinated]
print("Остальные:")
[print(fio["fio"]) for fio in not_vaccinated]
