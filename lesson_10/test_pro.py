# Выполнить задание уровня light, но тестов не менее 5-ти;
# постараться добиться 100 % покрытия тестами (желательно приложить скрин с процентами покрытия).

from Light import Desk
from Light import amount_task, cart_in_desk, n_cart_in_desk
import unittest


class Test_Desk(unittest.TestCase):

    def setUp(self):
        self.card = Desk()
        self.mdesk = Desk()
        self.card = self.card.issue_cards(3)
        self.card2 = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}
        self.card1 = '7П'
        self.card_new = {'П': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],  # начальная колода
                         'К': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                         'Б': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                         'Ч': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']}

    def test_amount_desk(self):
        self.assertEqual(amount_task(self.card), 3, 'kkas')

    def test_cart_desk(self):
        self.assertEqual(cart_in_desk(self.card2, self.card1), True, 'Gffd')

    def test_n_cart_desk(self):
        self.assertEqual(n_cart_in_desk(self.card2), ['7'], 'doned')

    def test_init(self):
        self.assertEqual(self.mdesk.desk, self.card_new, 'beeee')

    def test_is_empty(self):
        self.mdesk.desk = {'П': [], 'К': [], 'Б': [], 'Ч': []}
        self.assertEqual(self.mdesk.is_empty, True, 'Jamayka')


if __name__ == '__main__':
    unittest.main()
    # pytest.main()

