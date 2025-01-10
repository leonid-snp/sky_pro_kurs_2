import random

from utils import open_file


class Question:

    def __init__(self, text: str, level: str, answer: str) -> None:
        """
        Инициализатор класса Question.
        :param text: (str) текст вопроса
        :param level: (str) уровень сложности
        :param answer: (str) верный ответ
        """
        self.text = text
        self.level = level
        self.answer = answer
        self.is_question = False
        self.user_answer = None
        self.point = int(self.level) * 10

    def get_points(self) -> int:
        """
        Возвращает количество баллов.
        :return: (int) количество баллов
        """
        return self.point

    def is_correct(self) -> bool:
        """
        Возвращает True если ответ верен, иначе False.
        :return: (boll) статус ответа
        """
        return self.answer == self.user_answer

    def build_question(self) -> str:
        """
        Возвращает вопрос пользователю, с отображением уровня сложности.
        :return: (str) вопрос
        """
        return f"{self.text}\nСложность {self.level}/5\n"

    def build_feedback(self) -> str:
        """
        Возвращает комментарий в зависимости от ответа пользователя.
        :return: (str) комментарий
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.point} баллов\n"
        else:
            return f"Ответ неверный. Верный ответ - {self.answer}\n"


def main() -> None:
    """
    Запускает программу.
    :return: (None)
    """
    questions = [Question(*question.values()) for question in open_file("data.json")]
    len_questions = len(questions)
    count_answer = 0
    user_point = 0
    print("Игра начинается!\n")
    while len(questions) != 0:
        question = random.choice(questions)
        question.user_answer = input(question.build_question())
        if question.is_correct():
            count_answer += 1
            user_point += question.point
        print(question.build_feedback())
        questions.remove(question)

    print(f"Вот и все!\n"
          f"Отвечено {count_answer} вопросов из {len_questions}\n"
          f"Набрано баллов: {user_point}")


if __name__ == "__main__":
    main()
