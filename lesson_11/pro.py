# Выполнить задание уровня light
# Реализовать собственный класс с использованием магических методов (не менее 10-ти).
# Можно использовать собственный класс из вебинара 10.

from random import choice


class Desk:
    """
    Класс колоды
    """

    def __init__(self):
        """
        инициализация класса
        """
        self.sample = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
        self.desk = {x: self.sample for x in ['П', "К", "Б", "Ч"]}
        self.kosyr = None  # объявление козыря
        self.flag = True  # и признака, что запас карт закончен


    @property
    def is_empty(self):
        """
        свойство, что колода пуста
        """
        return sum(len(x) for x in self.desk.values()) == 0

    def issue_cards(self, n):
        """
        раздача карт
        n  - количество необходимых карт
        return - словарь с выданными картами
        """
        result = {'П': [], 'К': [], 'Б': [], 'Ч': []}  # объявление словаря с результатом
        # формирование списка мастей, в которых остались карты
        suit_list = [i for i in self.desk.keys() if self.desk[i]]
        if suit_list and self.flag:  # если этот список не пустой, и флаг признака окончание колоды не поднят
            for _ in range(n):  # повторяя действия для каждой нужно карты
                # формирование списка мастей, в которых остались карты
                suit_list = [i for i in self.desk.keys() if self.desk[i]]
                if suit_list:  # если список не пустой
                    suit = choice(suit_list)  # выбираем случайную масть
                    # выбираем случайную карту из оставшихся в этой колоде карт
                    value = choice(self.desk[suit])
                    if value:
                        # удаление выбранной карты из колоды
                        self.desk[suit].remove(value)
                    result[suit].append(value)  # добавление карты в итоговый словарь
                else:  # иначе
                    # получение масти козыря
                    suit = [x for x in self.kosyr.keys() if self.kosyr[x]]
                    value = self.kosyr[suit][0]  # получение значения козыря
                    result[suit].append(value)  # добавление карты в итоговый словарь
                    self.flag = False  # поднятие флага окончания колоды
                    break  # прерывание цикла
        elif self.flag and self.kosyr:  # иначе если флаг не поднят и есть значение козыря
            result = self.kosyr  # приравнивание итогового словаря к словарю козыря
            self.flag = False  # поднятие флага окончания колоды
        return result

    def __len__(self):
        return sum(len(x) for x in self.desk.values())

    def __str__(self):
        s = ''  # объявление результирующей переменной
        for i in self.desk.keys():  # для каждого из ключей колоды
            if self.desk[i]:  # если значение по этому ключу не пустое
                for j in self.desk[i]:  # для каждого из значений списка по ключу
                    s += ''.join([j, i, ' '])  # добавление к итоговой строке новых значений масти и карты
        return s

    def __add__(self, other):
        for i in self.desk.keys():
            if len(other.desk[i]):
                self.desk[i].extend(other.desk[i])
        return self

    def __sub__(self, other):
        if isinstance(other, str):
            self.desk[other[-1]].remove(other[:-1])
        return self

    def __contains__(self, item):
        return item[:-1] in self.desk[item[-1]]



class CurrDesk(Desk):
    def __init__(self):
        super().__init__()
        self.desk = {'П': [], 'К': [], 'Б': [], 'Ч': []}

    def set_desk(self, task):
        self.desk = task

    def add_cart(self, cart):
        self.desk[cart[-1]].append(cart[:-1])


desk1 = CurrDesk()
desk = Desk()
desk2 = CurrDesk()
desk2.set_desk(desk.issue_cards(3))
print(desk2)
print(desk1)
print(len(desk1))
desk1 = desk1 + desk2
print(desk1)
print(len(desk1))
desk1.add_cart('10П')
print(desk1, len(desk1))
desk = desk - '10П'
print(len(desk))
print('9П' in desk1)