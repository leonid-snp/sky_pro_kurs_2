#!/usr/bin/python3

"""
Создайте функцию is_palindrome(word).

Функция должна возвращать True, если слово палиндром, иначе — False.

Чтобы проверить, является ли строка палиндромом, проверьте,
что инвертированная строка (reversed_str = str[::-1]) равна оригинальной строке.

Например:
level — True
sagas — True
hero — False
drama — False
"""

# Задача
"""
level — True
sagas — True
hero — False
drama — False
"""


# Решение
def is_palindrome(word: str) -> bool:
    if word == word[::-1]:
        return True
    return False


# Код вашей функции должен быть выше
try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")
