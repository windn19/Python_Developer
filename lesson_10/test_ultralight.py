# Написать один тест к собственному классу из вебинара 9 с помощью библиотеки pytest;
# Написать один тест к собственному классу из вебинара 9 с помощью библиотеки unittest.

from Light import Desk
from Light import amount_task, cart_in_desk
import unittest


class Test_Light(unittest.TestCase):

    def test_amount_desk(self):
        card = Desk()
        card = card.issue_cards(3)
        self.assertEqual(amount_task(card), 3, 'kkas')

    def test_cart_desk(self):
        card = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}
        card1 = '7П'
        self.assertEqual(cart_in_desk(card, card1), True, 'Gffd')


if __name__ == '__main__':
    unittest.main()
