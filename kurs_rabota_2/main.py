from players import Player
from utils import create_instance_class, get_correct_word


def main() -> None:
    """
    Запускает основную логику программы.
    :return: (None)
    """
    player = Player(input("Введите имя игрока: "))
    print(f"Привет, {player.name.capitalize()}!")
    word = create_instance_class()
    print(f"Составьте {word.get_count_subwords()} слов из слова {word.word.upper()}\n"
          f"Слова должны быть не короче {word.get_min_len()} букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите \"stop\"\n"
          f"Поехали, ваше первое слово? ")

    while len(word.subwords) != len(player.used_word):
        player_word = input().lower()
        if len(player_word) < word.get_min_len():
            print("слишком короткое слово\n")
        elif player.check_used_word(player_word):
            print("уже использовано\n")
        elif player_word in ("stop", "стоп"):
            break
        elif word.is_correct(player_word):
            print("верно\n")
            player.add_word(player_word)
        else:
            print("неверно\n")

    print(f"Игра завершена, вы угадали {player.get_count_used_word()} {get_correct_word(player.get_count_used_word())}!")


if __name__ == '__main__':
    main()
