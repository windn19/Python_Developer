# Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью библиотеки pytest;
# Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью библиотеки unittest.

from Light import Desk  # импорт класса для проверки
from Light import amount_task, cart_in_desk, n_cart_in_desk  # импорт методов для проверки
import unittest  # импорт библиотеки для тестов


class Test_Light(unittest.TestCase):
    """
    класс тестов
    """
    def setUp(self) -> None:
        """
        начальные условия
        """
        self.card = Desk()  # объявление колоды
        self.card = self.card.issue_cards(3)  # передача трех карт в колоду
        self.card2 = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}  # объявление второй колоды
        self.card1 = '7П'  # объявление карты

    def test_amount_desk(self):
        """
        проверка количества карт в колоде
        """
        self.assertEqual(amount_task(self.card), 3, 'Количество карт не соответствует')

    def test_cart_desk(self):
        """
        проверка включения карты в колоду игрока
        """
        self.assertEqual(cart_in_desk(self.card2, self.card1), True, 'Нет такой колоды на руках игрока')

    def test_n_cart_desk(self):
        """
        проверка номинала карт
        """
        self.assertEqual(n_cart_in_desk(self.card2), ['7'], 'Не соответствие номинала')


if __name__ == '__main__':
    unittest.main()  # активация модуля.
