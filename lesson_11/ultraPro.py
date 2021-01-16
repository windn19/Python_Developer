# Выполнить задание уровня pro
# В своем проекте использовать любые подходящие магические методы для того
# чтобы сделать код более читаемым и удобным для переиспользования;
# Покрыть новый код тестами;

from random import choice  # импортирование библиотеки random метода выбора из списков


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
        result = CurrDesk()  # объявление словаря с результатом
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
                        self.desk = self.desk - (value + suit)
                    result = result + (value + suit)  # добавление карты в итоговый словарь
                else:  # иначе
                    # получение масти козыря
                    suit = [x for x in self.kosyr.keys() if self.kosyr[x]]
                    value = self.kosyr[suit][0]  # получение значения козыря
                    result = result + (value + suit)  # добавление карты в итоговый словарь
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
        if not isinstance(other, str):
            for i in self.desk.keys():
                if len(other.desk[i]):
                    self.desk[i].extend(other.desk[i])
        else:
            self.desk[other[-1]].append(other[:-1])
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


def amount_task(desk):
    """
    нахождение количества карт в колоде
    """
    # сумма длин каждого значения словаря колоды, перебираемые по ключам
    return sum(len(desk[x]) for x in desk.keys())


def n_cart_in_desk(desk):
    """
    нахождение списка всех значений карт
    desk - колода для определения значения
    return: список всех значений колоды
    """
    result = []  # объявление результирующего списка
    for i in desk:  # для каждого значения ключа колоды
        result.extend(desk[i])  # вставка значений списка масти в результирующий список
    return result


def cart_in_desk(desk, cart, kosyr):
    """
    определение находится ли карта в колоде
    desk - колода
    cart - карта
    kosyr - козырь
    return - возврат истина или ложь
    """
    # условие, что карта находится в колоде и значение тоже находится в этой колоде
    if1 = cart in desk
    if2 = cart[-1] in kosyr  # условие, что масть карты соответствует козырю
    return if1 or if2


def get_cart_index(value):
    """
    нахождение индекса значения карты
    value - значение проверяемой карты
    return - вывод индекса значения по списку образцу
    """
    sample = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']  # образец полного списка значений карт
    return sample.index(value)


def is_my_cart_big(my_cart, cart, kosyr):
    """
    проверка больше ли значение cart значение my_cart
    my_cart - карта, которую сравнивают
    cart - карту, с которой сравнивают
    kosyr - козырная масть
    return: истина или ложь
    """
    # если масть сравниваемой карты не козырная, а масть карты, которую сравнивают, козырная
    if len(kosyr[cart[-1]]) == 0 and len(kosyr[my_cart[-1]]) > 0:
        res = True  # результат истина
    else:  # иначе
        result = my_cart[-1] == cart[-1]  # если масть карт совпадают
        # и индекс карты больше, чем у основной карты
        res = get_cart_index(my_cart[:-1]) > get_cart_index(cart[:-1])
        res = result and res  # если оба условия выполняются
    return res


class Player:
    """
    Основной класс игрока
    """

    def __init__(self, num):
        """
        инициация класса
        """
        self.number = num  # присвоение номера конкретному игроку
        self.desk = CurrDesk()  # объявление значений карт на руках

    def is_my_cart(self, cart):
        """
        проверка нахождения карты на руке
        cart - карта, которую нужно проверить
        """
        # если масть карты находится на руках и значение карты находится в списке этой масти
        return cart[-1] in self.desk and cart[:-1] in self.desk[cart[-1]]

    def amount_cart(self):
        """
        возврат количество карт на руке
        """
        return sum(len(self.desk[x]) for x in self.desk.keys())

    def __str__(self):
        """
        способ вывода значений класса
        """
        s = ''  # объявление результирующей строки
        for i in self.desk.keys():  # перебираем все ключи для колоды
            for j in sorted(self.desk[i]):  # и для каждого значения из списков в мастях
                s += j + i + ' '  # добавить в результирующую строку
        return f'{self.name} {self.number} : {s}'  # возврат строки из имени игрока, его номера и карт

    def is_alive(self):
        """
        проверка, что у игрока есть еще карты
        """
        return sum(len(self.desk[x]) for x in self.desk.keys()) != 0


class Full:
    """
    класс игры
    """

    def __init__(self, num=1):
        """
        инициация класса
        num - количество игроков
        """
        # объявление игроков: по умолчанию 0 - компьютер, а остальные люди
        self.players = [CompPlayer(0), *[HumanPlayer(_) for _ in range(1, num + 1)]]
        self.task = CurrDesk()  # объявление кона
        self.defender = None  # объявление переменной для защищающегося
        self.attack = None  # объявление списка нападающих

    def game_over(self, desk):
        """
        признак окончания игры
        """
        # если колода пуста и сумма всех активных игроков меньше или равна 1
        return desk.is_empty and sum(x.is_alive() for x in self.players) <= 1

    def first_hod(self, desk):
        """
        первый ход для играков
        desk - активная колода
        """
        for i in self.players:  # для каждого игрока
            i.desk = desk.issue_cards(6)  # добавление в колоду игрока 6 начальных карт
        desk.kosyr = desk.issue_cards(1)  # объявление козыря

    def pr_kosyr(self, kosyr):
        """
        вывод козыря
        return - вывод строки со значение козыря и его масти
        """
        for i in kosyr.keys():  # для каждого ключа словаря козырь
            if kosyr[i]:  # если значение ключа не пустое
                value = kosyr[i][0]  # запомним значение
                suit = i  # запомним масть
                break  # прерывание цикла
        return f'Козырь: {value}{suit}'

    # def pr_task(self, task):
    #     """
    #     вывод карт на руках играка
    #     task - колода, которую нужно вывести
    #     return: строка с названиями карт, которые есть в наличии
    #     """
    #     s = ''  # объявление результирующей переменной
    #     for i in task.keys():  # для каждого из ключей колоды
    #         if task[i]:  # если значение по этому ключу не пустое
    #             for j in task[i]:  # для каждого из значений списка по ключу
    #                 s += ''.join([j, i, ' '])  # добавление к итоговой строке новых значений масти и карты
    #     return s

    def run2(self):
        """
        запуск игры
        """
        desk = Desk()  # инициализация колоды
        self.first_hod(desk)  # запуск метода первого хода с активной колодой
        n = 1  # первый атакующий игрок
        count_players = len(self.players)  # запоминание количества игроков
        while not self.game_over(desk):  # пока не получен признак конца игры
            k = 0  # номер первого игрока
            while not self.players[n % count_players].is_alive():  # пока не получен активный игрок
                n += 1  # добавление номера атакующего игрока
            self.attack = self.players[n % count_players]  # запись атакующего игрока
            print('Атакует: ', self.attack.name, self.attack.number)
            d = n + 1  # получение номера защищающегося игрока
            if not self.defender:  # если защищающийся не пределен
                self.defender = self.players[d % count_players]  # определяем его
            print('Защитник: ', self.defender.name, self.defender.number)
            num = 0  #  номер розыгрыша
            while num <= 6:  # пока номер меньше или равно 6
                if len(self.task):  # если количество карт в колоде не равно нулю
                    # выводим колоду кона и козырь
                    print(f'На столе: {self.task}  {self.pr_kosyr(desk.kosyr)}')
                else:
                    # выводим только козырь
                    print(self.pr_kosyr(desk.kosyr))
                print(self.attack)  # карты атакующего
                cart = self.attack.go(self.task, desk.kosyr) # ход атакующего
                if not self.attack.is_alive():  # если атакующий не активен
                    break  # прерывание списка
                if cart:  # если карта - не пустое значение
                    self.task = self.task + cart  # добавляем ее в колоду кона
                    print()
                    print(f'На столе: {self.task} ход: {cart} {self.pr_kosyr(desk.kosyr)}')
                    print()
                    print(self.defender)  # выводим карты защищающегося
                    cart = self.defender.go(self.task, desk.kosyr, defend=cart)  # ход защищающегося
                    if not self.defender.is_alive():  # если он не активен
                        break  # прерывание цикла
                if isinstance(cart, str):  # если тип карты строка
                    self.task = self.task + cart  # добавляем ее в колоду кона
                else:  # иначе
                    if cart:  # если cart == true
                        n += 2  # добавление к n 2
                        self.defender = None  # обнуление защитника
                        num = 6  # выход из цикла
                        self.task = CurrDesk()  # обнуление колоды кона
                    else:  # иначе
                        n += 1  # добавление к n 1
                        k += 1  # добавление 1 к игрокам, что сказали бито
                        # если k больше чем количество игроков минус защищающийся
                        if k >= len(self.players) - 1:
                            self.defender = None  # обнуление защитника
                            self.task = CurrDesk  # обнуление колоды кона
                            break  # прерывание цикла
            print()
            for i in self.players: # после окончание круга игры для каждого игрока
                if i.amount_cart() < 6:  # если его количество карт меньше 6
                    # добавление нужного количества карт в колоду игрока
                    add_cart = desk.issue_cards(6 - i.amount_cart())
                    i.desk = i.desk + add_cart


class HumanPlayer(Player):
    """
    Класс игрока Человека
    """

    def __init__(self, num):
        """
        Инициализация класса
        num - номер игрока
        """
        super().__init__(num)  # вызов инициализации вышестоящего класса
        self.name = input(f'ВВедите имя {num + 1} игрока: ')  # ввод имени игрока

    def go(self, value_task, kosyr, defend=None):
        """
        ход игрока
        value_task - колода кона
        kosyr - козырь игры
        defend - если есть, то карта, которую нужно покрыть
        return - значение на выход: карта или признак операции
        """
        if defend:  # если нужно покрыть карту
            cart = input('Ход def или взять (в): ')  # ввод карты или действий
            # проверка ввода
            while 2 < len(cart) > 3 or not (
                    cart_in_desk(self.desk, cart, kosyr) and is_my_cart_big(cart, defend, kosyr)):
                if cart.rstrip() == 'в':  # если ввели "в"
                    # все карты добавляются в колоду игрока
                    self.desk = self.desk + value_task
                    cart = 1
                    break  # прерывание цикла
                cart = input('Ход def или взять (в): ')
            if cart != 1:  # если карты не взяты, то они добавляются к колоде игрока
                self.desk = self.desk - cart
        else:  # иначе
            if not len(value_task):  # если количество карт в колоде кона не равно нулю
                cart = input('Ход ')  # ввод карты хода
                # проверка корректности ввода
                while 2 < len(cart) > 3 or not (cart_in_desk(self.desk, cart, kosyr)):
                    cart = input('Ход ')
                # удаление карты из колоды игрока
                self.desk = self.desk - cart
            else:  # иначе
                cart = input('Ход или бито(б): ')  # ввод карты и действия
                # проверка корректности ввода
                while 2 < len(cart) > 3 \
                        or not (cart_in_desk(self.desk, cart, kosyr)) \
                        or not (cart[:-1] in n_cart_in_desk(value_task)):
                    if cart.rstrip() == 'б':  # если ввели бито
                        cart = False
                        break  # прерывание цикла.
                    cart = input('Ход или бито(б): ')
                if cart:  # если значение карты не равно лжи
                    self.desk = self.desk - cart
                    # удаляем ее из колоды игрока
        return cart


class CompPlayer(Player):
    """
    класс игрока Компьютера
    """

    def __init__(self, num):
        """
        инициализация класса
        num - номер игрока
        """
        super(CompPlayer, self).__init__(num)  # вызов инициализации вышестоящего класса
        self.name = 'Comp'  # присвоение стандартного имени

    def go(self, value_task, kosyr, defend=None):
        """
        ход игрока
        value_task - колода кона
        kosyr - козырь игры
        defend - если есть, то карта, которую нужно покрыть
        return - значение на выход: карта или признак операции
        """
        if defend:  # если защита
            cart = self.go_deferend(kosyr, value_task, defend)  # вызов метода ход в защите
            if cart != 1:  # если значение карты не равно 1
                self.desk = self.desk - cart
                # удаляем ее из колоды игрока
            else:  # иначе
                print('ВЗЯЛ')
        else:  # иначе, если атакуем
            cart = self.go_attack(kosyr, value_task)  # вызов метода ход в атаке
            if cart:  # если значение карты не равно 0
                self.desk = self.desk - cart
                # удаляем ее из колоды игрока
            else:
                print('БИТО')
        return cart

    def go_attack(self, kosyr, task):
        """
        ход атакующего
        kosyr - словарь с козырем
        task - словарь с текущей колодой
        return - значение карты или действие
        """
        # получение значение масти козыря
        for i in kosyr.keys():
            if kosyr[i]:
                suit_kosyr = i
        # список мастей у колоды, в который еще остались карты и не равных козырю
        suits = [i for i in self.desk.keys() if i != suit_kosyr and len(self.desk[i])]
        if not len(task):   # если количество карт в колоде кона не равно нулю
            # результирующая масть либо случайный выбор из списка мастей, если он существует,
            # иначе масть козыря
            r_suit = choice(suits) if suits else suit_kosyr
            r_value = self.desk[r_suit][0]  # значение козыря первое значение в списке рез. масти
        else:  # иначе
            desk = set(n_cart_in_desk(task))  # все значения их колоды объединяем одно множество
            suits.append(suit_kosyr)  # к списку мастей добавляем масть козыря
            r_suit = False  # объявление начальных результирующих значений
            r_value = False
            # нахождение карт содержащихся в колоде игрока и в колоде кона
            for i in suits:
                for j in self.desk[i]:
                    if j in desk:
                        r_suit = i
                        r_value = j
            else:  # в конце цикла
                # если значение не было найдено вывод 0, иначе найденного значения
                r_suit = 0 if not r_value else r_suit
        return f'{r_value}{r_suit}' if r_suit else r_suit

    def go_deferend(self, kosyr, task, cart):
        """
        ход в защите
        kosyr - словарь козыря
        task - неиспользуется, оставлена для совместимости
        cart - карта, которую нужно покрыть
        return - значение карты или действие
        """
        # получение значение масти козыря
        for i in kosyr.keys():
            if kosyr[i]:
                suit_kosyr = i
        # список мастей у колоды, в который еще остались карты и не равных козырю
        suits = [i for i in self.desk.keys() if i != suit_kosyr and len(self.desk[i])]
        suits.append(suit_kosyr)   # к списку мастей добавляем масть козыря
        r_suit = False  # объявление начальных результирующих значений
        r_value = False
        # сравнение своих карт с получаемой и нахождение большей
        for i in suits:
            for j in self.desk[i]:
                if is_my_cart_big(f'{j}{i}', cart, kosyr):
                    r_suit = i
                    r_value = j
        else:
            # если после цикла не получено значение приравнивание 1
            r_suit = 1 if not r_value else r_suit
        return f'{r_value}{r_suit}' if r_value else r_suit


first = Full()  # активация объекта игры
first.run2()  # запуск игры
