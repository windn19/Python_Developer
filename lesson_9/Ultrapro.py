from random import choice


def amount_task(desk):
    return sum(len(desk[x]) for x in desk.keys())


def n_cart_in_desk(desk):
    result = []
    for i in desk:
        result.extend(desk[i])
    return result


def cart_in_desk(desk, cart, kosyr):
    if1 = cart[-1] in desk and cart[:-1] in desk[cart[-1]]
    if2 = cart[-1] in kosyr
    print('>> - ', if1 or if2)
    return if1 or if2


def get_cart_index(value):
    sample = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    return sample.index(value)


def is_my_cart_big(my_cart, cart, kosyr):
    print(len(kosyr[cart[-1]]) != 0)
    print(len(kosyr[my_cart[-1]]) > 0)
    if len(kosyr[cart[-1]]) == 0 and len(kosyr[my_cart[-1]]) > 0:
        res = True
    else:
        result = my_cart[-1] == cart[-1]
        res = get_cart_index(my_cart[:-1]) > get_cart_index(cart[:-1])
        res = result and res
    return res


class Player:
    """
    набор карт на руке
    ход
    """

    def __init__(self, num):
        self.number = num
        self.desk = {'П': [], 'К': [], 'Б': [], 'Ч': []}

    def is_my_cart(self, cart):
        return cart[-1] in self.desk and cart[:-1] in self.desk[cart[-1]]

    def amount_cart(self):
        return sum(len(self.desk[x]) for x in self.desk.keys())

    def __str__(self):
        s = ''
        for i in self.desk.keys():
            for j in sorted(self.desk[i]):
                s += j + i + ' '
        return f'{self.name} {self.number} : {s}'

    def is_alive(self):
        return sum(len(self.desk[x]) for x in self.desk.keys()) != 0


class Desk:

    def __init__(self):
        self.desk = {'П': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                     'К': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                     'Б': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т'],
                     'Ч': ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']}
        self.kosyr = None
        self.flag = True

    @property
    def is_empty(self):
        return sum(len(x) for x in self.desk.values()) == 0

    def issue_cards(self, n):
        result = {'П': [], 'К': [], 'Б': [], 'Ч': []}
        suit_list = [i for i in self.desk.keys() if self.desk[i]]
        if suit_list and self.flag:
            for _ in range(n):
                suit_list = [i for i in self.desk.keys() if self.desk[i]]
                if suit_list:
                    suit = choice(suit_list)
                    value = choice(self.desk[suit])
                    if value:
                        self.desk[suit].remove(value)
                    result[suit].append(value)
                else:
                    suit = [x for x in self.kosyr.keys() if self.kosyr[x]]
                    value = self.kosyr[suit][0]
                    result[suit].append(value)
                    self.flag = False
                    break
        elif self.flag and self.kosyr:
            result = self.kosyr
            self.flag = False
        return result


class Full:
    """
    кон
    """

    def __init__(self, num=1):
        self.players = [CompPlayer(0), *[HumanPlayer(_) for _ in range(1, num + 1)]]
        self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}
        self.defender = None
        self.attack = None

    def game_over(self, desk):
        return desk.is_empty and sum(x.is_alive() for x in self.players) == 1

    def first_hod(self, desk):
        for i in self.players:
            i.desk = desk.issue_cards(6)
        desk.kosyr = desk.issue_cards(1)

    def pr_kosyr(self, kosyr):
        for i in kosyr.keys():
            if kosyr[i]:
                value = kosyr[i][0]
                suit = i
        return f'Козырь: {value}{suit}'

    def pr_task(self, task):
        s = ''
        for i in task.keys():
            if task[i]:
                for j in task[i]:
                    s += ''.join([j, i, ' '])
        return s

    def run2(self):
        desk = Desk()
        self.first_hod(desk)
        n = 1
        count_players = len(self.players)
        while not self.game_over(desk):
            k = 0
            while not self.players[n % count_players].is_alive():
                n += 1
            self.attack = self.players[n % count_players]
            print('Attack', self.attack.name, self.attack.number)
            d = n + 1
            if not self.defender:
                self.defender = self.players[d % count_players]
            print('Defender', self.defender.name, self.defender.number)
            print(n, d)
            num = 0
            while num < 6:
                if amount_task(self.task):
                    print(f'На столе: {self.pr_task(self.task)}  {self.pr_kosyr(desk.kosyr)}')
                else:
                    print(self.pr_kosyr(desk.kosyr))
                print(self.attack)
                cart = self.attack.go(self.task, desk.kosyr)
                if not self.attack.is_alive():
                    break
                if cart:
                    self.task[cart[-1]].append(cart[:-1])
                    print()
                    print(f'На столе: {self.pr_task(self.task)} ход: {cart} {self.pr_kosyr(desk.kosyr)}')
                    print()
                    print(self.defender)
                    cart = self.defender.go(self.task, desk.kosyr, defend=cart)
                    if not self.defender.is_alive():
                        break
                if isinstance(cart, str):
                    self.task[cart[-1]].append(cart[:-1])
                else:
                    if cart:
                        n += 2
                        print(n)
                        self.defender = None
                        num = 6
                        self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}
                    else:
                        n += 1
                        print("*", n)
                        k += 1
                        if k >= len(self.players) - 1:
                            self.defender = None
                            self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}
                            break
            print(self.task)
            print()
            for i in self.players:
                if i.amount_cart() < 6:
                    add_cart = desk.issue_cards(6 - i.amount_cart())
                    for j in add_cart:
                        i.desk[j].extend(add_cart[j])
                print(i, i.amount_cart())


class HumanPlayer(Player):

    def __init__(self, num):
        super().__init__(num)
        self.name = input(f'ВВедите имя {num + 1} игрока: ')

    def go(self, value_task, kosyr, defend=None):
        if defend:
            cart = input('Ход def или взять (в): ')
            while 2 < len(cart) > 3 or not (
                    cart_in_desk(self.desk, cart, kosyr) and is_my_cart_big(cart, defend, kosyr)):
                if cart.rstrip() == 'в':
                    for i in self.desk.keys():
                        if value_task[i]:
                            self.desk[i].extend(value_task[i])
                    cart = 1
                    break
                cart = input('Ход def или взять (в): ')
            if cart != 1:
                self.desk[cart[-1]].remove(cart[:-1])
        else:
            if not amount_task(value_task):
                cart = input('Ход ')
                while 2 < len(cart) > 3 or not (cart_in_desk(self.desk, cart, kosyr)):
                    cart = input('Ход ')
                self.desk[cart[-1]].remove(cart[:-1])
            else:
                cart = input('Ход или бито(б): ')
                print(value_task.values())
                while 2 < len(cart) > 3 \
                        or not (cart_in_desk(self.desk, cart, kosyr)) \
                        or not (cart[:-1] in n_cart_in_desk(value_task)):
                    if cart.rstrip() == 'б':
                        print('Hello')
                        cart = False
                        break
                    cart = input('Ход или бито(б): ')
                if cart:
                    self.desk[cart[-1]].remove(cart[:-1])
        return cart


class CompPlayer(Player):

    def __init__(self, num):
        super(CompPlayer, self).__init__(num)
        self.name = 'Comp'

    def go(self, value_task, kosyr, defend=None):
        if defend:
            cart = self.go_deferend(kosyr, value_task, defend)
            if cart != 1:
                self.desk[cart[-1]].remove(cart[:-1])
            else:
                print('ВЗЯЛ')
        else:
            cart = self.go_attack(kosyr, value_task)
            print(cart)
            if cart:
                self.desk[cart[-1]].remove(cart[:-1])
            else:
                print('БИТО')
        return cart

    def go_attack(self, kosyr, task):
        for i in kosyr.keys():
            if kosyr[i]:
                suit_kosyr = i
        suits = [i for i in self.desk.keys() if i != suit_kosyr and len(self.desk[i])]
        print(amount_task(task))
        if not amount_task(task):
            r_suit = choice(suits) if suits else suit_kosyr
            r_value = self.desk[r_suit][0]
        else:
            desk = set(n_cart_in_desk(task))
            suits.append(suit_kosyr)
            r_suit = False
            r_value = False
            for i in suits:
                for j in self.desk[i]:
                    if j in desk:
                        r_suit = i
                        r_value = j
            else:
                print(r_suit, r_value)
                r_suit = 0 if not r_value else r_suit
            print(r_suit, r_value)
        return f'{r_value}{r_suit}' if r_suit else r_suit

    def go_deferend(self, kosyr, task, cart):
        for i in kosyr.keys():
            if kosyr[i]:
                suit_kosyr = i
        suits = [i for i in self.desk.keys() if i != suit_kosyr and len(self.desk[i])]
        suits.append(suit_kosyr)
        r_suit = False
        r_value = False
        for i in suits:
            for j in self.desk[i]:
                if is_my_cart_big(f'{j}{i}', cart, kosyr):
                    r_suit = i
                    r_value = j
        else:
            print(r_suit, r_value)
            r_suit = 1 if not r_value else r_suit
        print(r_suit, r_value)
        return f'{r_value}{r_suit}' if r_value else r_suit


first = Full()
first.run2()
