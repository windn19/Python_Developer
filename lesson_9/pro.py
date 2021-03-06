from random import choice  # импортирование библиотеки random метода выбора из списков


def amount_task(desk):
    """
    нахождение количества карт в колоде
    desk -  колода, которую перебираем
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
    if1 = cart[-1] in desk and cart[:-1] in desk[cart[-1]]
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
        self.name = input('ВВедите имя: ')   # ввод имени игрока
        self.number = num  # присвоение номера конкретному игроку
        self.desk = {'П': [], 'К': [], 'Б': [], 'Ч': []}  # объявление значений карт на руках

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
            while 2 < len(cart) > 3 or not (cart_in_desk(self.desk, cart, kosyr) and is_my_cart_big(cart, defend, kosyr)):
                if cart.rstrip() == 'в':   # если ввели "в"
                    # все карты добавляются в колоду игрока
                    for i in self.desk.keys():
                        if value_task[i]:
                            self.desk[i].extend(value_task[i])
                    cart = 1
                    break # прерывание цикла
                cart = input('Ход def или взять (в): ')
            if cart != 1:  # если карты не взяты, то они убираются из колоды игрока
                self.desk[cart[-1]].remove(cart[:-1])
        else:  # иначе
            if not amount_task(value_task):  # если количество карт в колоде кона не равно нулю
                cart = input('Ход ')  # ввод карты хода
                # проверка корректности ввода
                while 2 < len(cart) > 3 or not (cart_in_desk(self.desk, cart, kosyr)):
                    cart = input('Ход ')
                # удаление карты из колоды игрока
                self.desk[cart[-1]].remove(cart[:-1])
            else: # иначе
                cart = input('Ход или бито(б): ')  # ввод карты и действия
                # проверка корректности ввода
                while 2 < len(cart) > 3\
                        or not (cart_in_desk(self.desk, cart, kosyr))\
                        or not (cart[:-1] in n_cart_in_desk(value_task)):
                    if cart.rstrip() == 'б':  # если ввели бито
                        cart = False
                        break  # прерывание цикла.
                    cart = input('Ход или бито(б): ')
                if cart:  # если значение карты не равно лжи
                    self.desk[cart[-1]].remove(cart[:-1])  # удаляем ее из колоды игрока
        return cart

    def __str__(self):
        """
        способ вывода значений класса
        """
        s = ''  # объявление результирующей строки
        for i in self.desk.keys():  # перебираем все ключи для колоды
            for j in sorted(self.desk[i]):  # и для каждого значения из списков в мастях
                s += j+i+' '   # добавить в результирующую строку
        return f'{self.name} {self.number} : {s}'  # возврат строки из имени игрока, его номера и карт

    def is_alive(self):
        """
        проверка, что у игрока есть еще карты
        """
        return sum(len(self.desk[x]) for x in self.desk.keys()) != 0


class Desk:
    """
    Класс колоды
    """
    def __init__(self):
        """
        инициализация класса
        """
        self.desk = {'П': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],  # начальная колода
                     'К': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                     'Б': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                     'Ч': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']}
        self.kosyr = None   # объявление козыря
        self.flag = True   # и признака, что запас карт закончен

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
        if suit_list and self.flag: # если этот список не пустой, и флаг признака окончание колоды не поднят
            for _ in range(n):  # повторяя действия для каждой нужно карты
                # формирование списка мастей, в которых остались карты
                suit_list = [i for i in self.desk.keys() if self.desk[i]]
                if suit_list:  # если список не пустой
                    suit = choice(suit_list)  # выбираем случайную масть
                    value = choice(self.desk[suit])   # выбираем случайную карту из оставшихся в этой колоде карт
                    if value:
                        # удаление выбранной карты из колоды
                        self.desk[suit].remove(value)
                    result[suit].append(value)  # добавление карты в итоговый словарь
                else:  # иначе
                    # получение масти козыря
                    suit = [x for x in self.kosyr.keys() if self.kosyr[x]]
                    value = self.kosyr[suit][0]  # получение значения козыря
                    result[suit].append(value)  # добавление карты в итоговый словарь
                    self.flag = False   # поднятие флага окончания колоды
                    break   # прерывание цикла
        elif self.flag and self.kosyr:  # иначе если флаг не поднят и есть значение козыря
            result = self.kosyr  # приравнивание итогового словаря к словарю козыря
            self.flag = False  # поднятие флага окончания колоды
        return result


class Full:
    """
    класс игры
    """

    def __init__(self, num):
        """
        инициация класса
        num - количество игроков
        """
        # объявление игроков: по умолчанию 0 - компьютер, а остальные люди
        self.players = [Player(_) for _ in range(num)]
        self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}  # объявление кона
        self.defender = None   # объявление переменной для защищающегося
        self.attack = None  # объявление списка нападающих

    def game_over(self, desk):
        """
        признак окончания игры
        desk - активная колода
        """
        # если колода пуста и сумма всех активных игроков меньше или равна 1
        return desk.is_empty and sum(x.is_alive() for x in self.players) == 1

    def first_hod(self, desk):
        """
        первый ход для играков
        desk - активная колода
        """
        for i in self.players:   # для каждого игрока
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

    def pr_task(self, task):
        """
        вывод карт на руках играка
        task - колода, которую нужно вывести
        return: строка с названиями карт, которые есть в наличии
        """
        s = ''  # объявление результирующей переменной
        for i in task.keys():  # для каждого из ключей колоды
            if task[i]:  # если значение по этому ключу не пустое
                for j in task[i]:  # для каждого из значений списка по ключу
                    s += ''.join([j, i, ' '])  # добавление к итоговой строке новых значений масти и карты
        return s

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
            num = 0  # номер розыгрыша
            while num <= 6:  # пока номер меньше или равно 6
                if amount_task(self.task):  # если количество карт в колоде не равно нулю
                    # выводим колоду кона и козырь
                    print(f'На столе: {self.pr_task(self.task)}  {self.pr_kosyr(desk.kosyr)}')
                else:
                    # выводим только козырь
                    print(self.pr_kosyr(desk.kosyr))
                print(self.attack)  # карты атакующего
                cart = self.attack.go(self.task, desk.kosyr)  # ход атакующего
                if not self.attack.is_alive():  # если атакующий не активен
                    break  # прерывание списка
                if cart:  # если карта - не пустое значение
                    self.task[cart[-1]].append(cart[:-1])  # добавляем ее в колоду кона
                    print()
                    print(f'На столе: {self.pr_task(self.task)} ход: {cart} {self.pr_kosyr(desk.kosyr)}')
                    print()
                    print(self.defender)  # выводим карты защищающегося
                    cart = self.defender.go(self.task, desk.kosyr, defend=cart)  # ход защищающегося
                    if not self.defender.is_alive():  # если он не активен
                        break  # прерывание цикла
                if isinstance(cart, str):  # если тип карты строка
                    self.task[cart[-1]].append(cart[:-1])  # добавляем ее в колоду кона
                else:  # иначе
                    if cart:  # если cart == true
                        n += 2  # добавление к n 2
                        self.defender = None  # обнуление защитника
                        num = 6  # выход из цикла
                        self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}  # обнуление колоды кона
                    else:  # иначе
                        n += 1  # добавление к n 1
                        k += 1  # добавление 1 к игрокам, что сказали бито
                        # если k больше чем количество игроков минус защищающийся
                        if k >= len(self.players) - 1:
                            self.defender = None  # обнуление защитника
                            self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}  # обнуление колоды кона
                            break  # прерывание цикла
            print()
            for i in self.players:  # после окончание круга игры для каждого игрока
                if i.amount_cart() < 6:  # если его количество карт меньше 6
                    # добавление нужного количества карт в колоду игрока
                    add_cart = desk.issue_cards(6 - i.amount_cart())
                    for j in add_cart:
                        i.desk[j].extend(add_cart[j])


first = Full(2)
first.run2()
