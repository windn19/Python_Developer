from Light import Desk  # импортирование из модуля тестируемого класса
import pytest  # импортирование библиотеки для тестирование


class Test_Desk:
    """
    класс тестирования колоды
    """

    def setup(self):
        """
        начальные условие тестирование
        """
        self.desk = Desk()

    def test_issue_cards(self):
        """
        тестирование количества выдаваемых карт
        """
        card = self.desk.issue_cards(2)  # получение карт для добавления
        assert sum(len(x) for x in card.values()) == 2  # проверка соответствия количества карт заявленному

    def test_is_empty(self):
        """
        проверка: является ли колода пустой
        """
        assert not self.desk.is_empty


if __name__=='__main__':
    pytest.main()  # запуск модуля.
