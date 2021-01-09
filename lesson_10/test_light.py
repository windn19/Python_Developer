# Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью библиотеки pytest;
# Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью библиотеки unittest.

from lesson_9.Light import Player
from lesson_9.Light import amount_task, cart_in_desk, get_cart_index
import pytest
import unittest


class Test_Player(unittest.TestCase):

    def setUp(self):
        self.player = Player(2)
        self.player.desk = {'П': ['6'], 'К': [], 'Б': [], 'Ч': []}
        self.card = '7П'

    def test_init(self):
        assert self.player.num == 2

    def test_my_cart(self):
        assert self.player.is_my_cart(self.card)

    def test_get_card_index(self):
        assert get_cart_index(self.card) == 1


# class Test_Light(unittest.TestCase):
#
#     def test_amount_desk(self):
#         card = Desk()
#         card = card.issue_cards(3)
#         self.assertEqual(amount_task(card), 2, 'kkas')
#
#     def test_cart_desk(self):
#         card = {'П': ['7'], 'К': [], 'Б': [], 'Ч': []}
#         card1 = '7П'
#         self.assertEqual(cart_in_desk(card, card1), True, 'Gffd')


if __name__ == '__main__':
    # unittest.main()
    pytest.main()
