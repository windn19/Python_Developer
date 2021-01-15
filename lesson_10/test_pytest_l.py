from Light import Player  # импорт класса для тестирования
from Light import get_cart_index  # импорт метода для тестирования
import pytest  # импорт библиотеки для тестирования


class Test_Player:
    """
    класс тестирования
    """

    def setup(self):
        """
        начальные условия
        """
        self.player = Player(2, 'Pete')  # активация класса игрока
        self.player.desk = {'П': ['6'], 'К': [], 'Б': [], 'Ч': []}  # приравнивание ему колоды
        self.card = '7П'  # значение карты

    def test_init(self):
        """
        проверка инициация
        """
        assert self.player.number == 2

    def test_my_cart(self):
        """
        проверка, что карта находится в руке игрока
        """
        assert not self.player.is_my_cart(self.card)

    def test_get_card_index(self):
        """
        проверка, что индекс карты равен одному.
        """
        assert get_cart_index(self.card[:-1]) == 1


if __name__ == '__main__':
    pytest.main()  # запуск модуля.
