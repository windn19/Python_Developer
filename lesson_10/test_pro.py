# Выполнить задание уровня light, но тестов не менее 5-ти;
# постараться добиться 100 % покрытия тестами (желательно приложить скрин с процентами покрытия).

from Light import Desk  # импорт класса для тестирования
from Light import amount_task, cart_in_desk, n_cart_in_desk  # импорт методов для тестирования
import unittest  # импорт библиотеки тестирования


class Test_Desk(unittest.TestCase):
    """
    класс тестов
    """
    def setUp(self):
        """
        начальные условия для тестирования
        """
        self.card = Desk()  # объявление переменной колоды для тестирования
        self.mdesk = Desk()
        self.card = self.card.issue_cards(3)  # передача в колоду трех случайных карт
        self.card2 = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}  # определение колоды образца
        self.card1 = '7П'  # определение входящей карты
        self.card_new = {'П': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],  # полная колода
                         'К': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                         'Б': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                         'Ч': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']}

    def test_amount_desk(self):
        """
        тест на правильность пополнения колоды
        """
        self.assertEqual(amount_task(self.card), 3, 'Количество в колоде не равно нужному')

    def test_cart_desk(self):
        """
        проверка наличия карты в колоды
        """
        self.assertEqual(cart_in_desk(self.card2, self.card1), True, 'Карта не в колоде, а должна быть там')

    def test_n_cart_desk(self):
        """
        проверка номиналов карт в колооде
        """
        self.assertEqual(n_cart_in_desk(self.card2), ['7'], 'Список номиналов карт не правильный')

    def test_init(self):
        """
        соответствие новой колоды и той, что должно быть
        """
        self.assertEqual(self.mdesk.desk, self.card_new, 'Не соответствует одна колода другой')

    def test_is_empty(self):
        """
        проверка пустоты колоды
        """
        self.mdesk.desk = {'П': [], 'К': [], 'Б': [], 'Ч': []}  # объявление пустой колоды
        self.assertEqual(self.mdesk.is_empty, True, 'Колода не пустая')


if __name__ == '__main__':
    unittest.main()  # запуск модуля тестов

