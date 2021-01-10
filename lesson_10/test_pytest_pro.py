from Light import Player, get_cart_index
import pytest


class Test_Player:

    def setup(self):
        self.player = Player(2, 'Pete')
        self.player.desk = {'П': ['6'], 'К': [], 'Б': [], 'Ч': []}
        self.card = '7П'
        self.mycard = '8П'

    def test_init(self):
        assert self.player.number == 2

    def test_my_cart(self):
        assert not self.player.is_my_cart(self.card)

    def test_get_card_index(self):
        assert get_cart_index(self.card[:-1]) == 1

    def test_is_my_cart_big(self):
        assert self.player.is_my_cart_big(self.mycard, self.card) == True

    def test_amound_cart(self):
        assert self.player.amount_cart() == 1


if __name__ == '__main__':
    pytest.main()
