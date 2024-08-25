#!/usr/bin/python3

"""
Создайте функцию check_pin(pin).

Функция должна возвращать True, если pin — это строка из 4 цифр, иначе — False.

Например:
1234 — True
123 — False
a000 — False
0000 — True
"""

# Задача
"""
1234 — True
123 — False
a000 — False
0000 — True
"""


# Решение
def check_pin(pin: str) -> bool:
    if pin.isdigit() and len(pin) == 4:
        return True
    return False


# Код вашей функции должен быть выше
try:
    assert check_pin("1234") == True
    assert check_pin("123") == False
    assert check_pin("a000") == False
    assert check_pin("0000") == True
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")
