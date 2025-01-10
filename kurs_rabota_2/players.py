class Player:
    """
    Класс для работы с игроком.
    """

    def __init__(self, name: str) -> None:
        """
        Инициализатор класса.
        :param name: (str) имя игрока
        """
        self.name = name
        self.used_word = []

    def __repr__(self) -> str:
        """
        Возвращает данные отладки для разработчиков.
        :return: (str) данные отладки
        """
        return f"Класс: {self.__class__.__name__}, Атрибуты: {self.name}, [{', '.join(self.used_word)}]"

    def get_count_used_word(self) -> int:
        """
        Возвращает количество использованных слов.
        :return: (int) количество слов
        """
        return len(self.used_word)

    def add_word(self, word: str) -> None:
        """
        Добавляет слово в использованные слова.
        :param word: (str) использованное слово
        :return: (None)
        """
        self.used_word.append(word)

    def check_used_word(self, word: str) -> bool:
        """
        Возвращает True если слово уже есть в списке использованных слов.
        :param word: (str) слово
        :return: (bool) булево значение
        """
        return word in self.used_word
