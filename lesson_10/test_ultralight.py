# Написать один тест к собственному классу из вебинара 9 с помощью библиотеки pytest;
# Написать один тест к собственному классу из вебинара 9 с помощью библиотеки unittest.

from Light import Desk  # импорт класса из модуля
from Light import amount_task, cart_in_desk  # импорт методов из модуля
import unittest  # импорт модуля тестирования


class Test_Light(unittest.TestCase):
    """
    создание класса тестирования
    """

    def test_amount_desk(self):
        """
        тест на количество карт
        """
        card = Desk()  # объявление класса колоды
        card = card.issue_cards(3)  # добавление к колоде трех карт
        self.assertEqual(amount_task(card), 3, 'Неправильное количество в колоде')
        # проверка, что количество карт в колоде равно заявленному

    def test_cart_desk(self):
        """
        тест на то, что карта в колоде
        """
        card = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}  # начальная колода
        card1 = '7П'  # карта для проверки
        self.assertEqual(cart_in_desk(card, card1), True, 'Карта не в колоде')
        # проверка, что карта находится в колоде


if __name__ == '__main__':
    unittest.main()  # запуск модуля.
