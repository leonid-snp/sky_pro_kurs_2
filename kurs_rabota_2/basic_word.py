class BasicWord:
    """
    Класс для работы со словами.
    """

    def __init__(self, word: str, subwords: list) -> None:
        """
        Инициализатор класса.
        :param word: (str) слово
        :param subwords: (list) список подслово
        """
        self.word = word
        self.subwords = subwords

    def __repr__(self) -> str:
        """
        Возвращает данные отладки для разработчиков.
        :return: (str) данные отладки
        """
        return f"Класс: {self.__class__.__name__}, Атрибуты: {self.word}, [{', '.join(self.subwords)}]"

    def is_correct(self, word: str) -> bool:
        """
        Возвращает True если слово есть в списке подслово.
        :param word: (str) слово
        :return: (bool) булево значение
        """
        return word in self.subwords

    def get_count_subwords(self) -> int:
        """
        Возвращает количество подслово.
        :return: (int) количество подслово
        """
        return len(self.subwords)

    def get_min_len(self) -> int:
        """
        Возвращает длину самого короткого слова.
        :return: (int) длину слова
        """
        return len(min(self.subwords, key=len))
