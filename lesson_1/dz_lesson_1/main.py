import random


def open_file(file_name: str, mode='r', text='') -> list | None:
    """
    Принимает название файла, режим (default=r)
    текст (default='')
    Если режим (r) то возвращает список
    Если режим (a) то записывает в файл текст
    :param file_name: (str) название файла
    :param mode: (str) режим
    :param text: (str) текст для записи
    :return: (list | None) список или нечего
    """
    with open(file_name, mode) as file:
        if mode == 'r':
            return file.read().strip().split()
        else:
            file.write(text)


def shuffles_letters(word: str) -> str:
    """
    Принимает на вход строку, перемешивает буквы в строке
    и возвращает перемешанную строку.
    :param word: (str) строка
    :return: (str) перемешанная строка
    """
    list_letters = list(word)
    random.shuffle(list_letters)
    return ''.join(list_letters)


def write_history(name: str, points: int) -> None:
    """
    Принимает на вход имя пользователя и очки которые заработал,
    записывает данные в файл.
    :param name: (str) имя пользователя
    :param points: (int) заработанные очки
    :return: None
    """
    open_file('history.txt', 'a', f'{name} {points}\n')


def display_statistics(file_name: str) -> str:
    """
    Принимает название файла,
    после чего считает количество сыгранных игр
    и максимальный результат.
    :param file_name: (str) имя файла
    :return: (str) статистика
    """
    file = open_file(file_name)
    number_games = len(file) // 2
    max_ball = 0
    for word in file:
        if word.isdigit():
            if int(word) > max_ball:
                max_ball = int(word)

    return (f'Всего игр сыграно: {number_games}\n'
            f'Максимальный рекорд: {max_ball}')


def main() -> None:
    """
    Запускает основную логику, спрашивает имя пользователя,
    и запускает игру в угадай слово,
    в конце записывает результат в файл
    :return: None
    """
    user_name = input('Введите ваше имя\n'
                      'Ввод: ')
    ball = 0
    file = open_file('words.txt')
    for word in file:
        answer = input(f'Угадайте слово: {shuffles_letters(word)}\n'
                       f'Ввод: ').lower()
        if answer == word:
            ball += 10
            print('Верно! Вы получаете 10 очков.')
        else:
            print(f'Неверно! Верный ответ {word}.')

    write_history(user_name, ball)


if __name__ == '__main__':
    main()
    print(display_statistics('history.txt'))
