from Light import Player
from Light import get_cart_index
import pytest


class Test_Player:

    def setup(self):
        self.player = Player(2, 'Pete')
        self.player.desk = {'П': ['6'], 'К': [], 'Б': [], 'Ч': []}
        self.card = '7П'

    def test_init(self):
        assert self.player.number == 2

    def test_my_cart(self):
        assert not self.player.is_my_cart(self.card)

    def test_get_card_index(self):
        assert get_cart_index(self.card[:-1]) == 1


if __name__ == '__main__':
    pytest.main()
