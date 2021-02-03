from Light import Player, get_cart_index  # импорт класса и метода для проверки
import pytest  # импорт библиотеки осуществляющую проверку


class Test_Player:
    """
    класс проверки игрока
    """

    def setup(self):
        """
        начальные установки
        """
        self.player = Player(2, 'Pete')  # объявление объекта игрока
        self.player.desk = {'П': ['6'], 'К': [], 'Б': [], 'Ч': []}  # объявление колоды игрока
        self.card = '7П'  # объявление карты
        self.mycard = '8П'  # объявление второй карты

    def test_init(self):
        """
        проверка номера игрока
        """
        assert self.player.number == 2

    def test_my_cart(self):
        """
        проверка, что карта не состоит в колоде
        """
        assert not self.player.is_my_cart(self.card)

    def test_get_card_index(self):
        """
        проверка индекса карты
        """
        assert get_cart_index(self.card[:-1]) == 1

    def test_is_my_cart_big(self):
        """
        проверка, что одна карта больше другой
        """
        assert self.player.is_my_cart_big(self.mycard, self.card) == True

    def test_amound_cart(self):
        """
        проверка количества карт
        """
        assert self.player.amount_cart() == 1


if __name__ == '__main__':
    pytest.main()  # запуск модуля.
