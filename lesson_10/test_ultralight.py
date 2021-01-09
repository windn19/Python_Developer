# Написать один тест к собственному классу из вебинара 9 с помощью библиотеки pytest;
# Написать один тест к собственному классу из вебинара 9 с помощью библиотеки unittest.

from lesson_9.Light import Desk
from lesson_9.Light import amount_task, cart_in_desk
import pytest
import unittest


class Test_Desk:

    def setup(self):
        self.desk = Desk()

    def test_issue_cards(self):
        card = self.desk.issue_cards(2)
        assert sum(len(x) for x in card.values()) == 2

    def test_is_empty(self):
        assert not self.desk.is_empty


class Test_Light(unittest.TestCase):

    def test_amount_desk(self):
        card = Desk()
        card = card.issue_cards(3)
        self.assertEqual(amount_task(card), 2, 'kkas')

    def test_cart_desk(self):
        card = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}
        card1 = '7П'
        self.assertEqual(cart_in_desk(card, card1), True, 'Gffd')


if __name__ == '__main__':
    # unittest.main()
    pytest.main()
