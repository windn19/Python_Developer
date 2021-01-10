# Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью библиотеки pytest;
# Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью библиотеки unittest.

from Light import Desk
from Light import amount_task, cart_in_desk, n_cart_in_desk
import unittest


class Test_Light(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Desk()
        self.card = self.card.issue_cards(3)
        self.card2 = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}
        self.card1 = '7П'

    def test_amount_desk(self):
        self.assertEqual(amount_task(self.card), 3, 'kkas')

    def test_cart_desk(self):
        self.assertEqual(cart_in_desk(self.card2, self.card1), True, 'Gffd')

    def test_n_cart_desk(self):
        self.assertEqual(n_cart_in_desk(self.card2), ['7'], 'doned')


if __name__ == '__main__':
    unittest.main()
