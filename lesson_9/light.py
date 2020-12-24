from random import randint, choice


def amount_task(desk):
    return sum(len(desk[x]) for x in desk.keys())


def n_cart_in_desk(desk):
    result = []
    for i in desk:
        result.extend(desk[i])
    return result


def cart_in_desk(desk, cart):
    return cart[-1] in desk and cart[:-1] in desk[cart[-1]]


def get_cart_index(value):
    sample = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    return sample.index(value)


class Player:
    """
    набор карт на руке
    ход
    """

    def __init__(self, num):
        self.name = input('ВВедите имя: ')
        self.number = num
        self.human = True
        self.desk = {'П': [], 'К': [], 'Б': [], 'Ч': []}

    def is_my_cart(self, cart):
        return cart[-1] in self.desk and cart[:-1] in self.desk[cart[-1]]

    def is_my_cart_big(self, my_cart, cart):
        result = my_cart[-1] == cart[-1]
        res = get_cart_index(my_cart[:-1]) > get_cart_index(cart[:-1])
        return result and res

    def amount_cart(self):
        return sum(len(self.desk[x]) for x in self.desk.keys())

    def go(self, value_task, defend=None):
        if defend:
            cart = input('Ход def или взять (в): ')
            while 2 < len(cart) > 3 or not (cart_in_desk(self.desk, cart) and self.is_my_cart_big(cart, defend)):
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
                while 2 < len(cart) > 3 or not (cart_in_desk(self.desk, cart)):
                    cart = input('Ход ')
                self.desk[cart[-1]].remove(cart[:-1])
            else:
                cart = input('Ход или бито(б): ')
                print(value_task.values())
                while 2 < len(cart) > 3\
                        or not (cart_in_desk(self.desk, cart))\
                        or not (cart[:-1] in n_cart_in_desk(value_task)):
                    if cart.rstrip() == 'б':
                        cart = False
                        break
                    cart = input('Ход или бито(б): ')
                if cart:
                    self.desk[cart[-1]].remove(cart[:-1])
        return cart

    def __str__(self):
        s = ''
        for i in self.desk.keys():
            for j in sorted(self.desk[i]):
                s += j+i+' '
        return f'{self.name} {self.number} : {s}'

    def is_alive(self):
        return sum(len(self.desk[x]) for x in self.desk.keys()) != 0


class Desk:

    def __init__(self):
        self.desk = {'П': ['6', '7', '8'], #'9', '10', 'В', 'Д', 'К', 'Т'],
                     'К': ['6', '7', '8'], #'9', '10', 'В', 'Д', 'К', 'Т'],
                     'Б': ['6', '7', '8'], #'9', '10', 'В', 'Д', 'К', 'Т'],
                     'Ч': ['6', '7', '8']} # '9', '10', 'В', 'Д', 'К', 'Т']}

    @property
    def is_empty(self):
        return sum(len(x) for x in self.desk.values()) == 0

    def issue_cards(self, n):
        result = {'П': [], 'К': [], 'Б': [], 'Ч': []}
        suit_list = [i for i in self.desk.keys() if self.desk[i]]
        print(suit_list)
        if suit_list:
            for _ in range(n):
                suit_list = [i for i in self.desk.keys() if self.desk[i]]
                suit = choice(suit_list)
                value = choice(self.desk[suit])
                if value:
                    self.desk[suit].remove(value)
                result[suit].append(value)
        return result


class Full:
    """
    кон
    """

    def __init__(self, num):
        self.players = [Player(_) for _ in range(num)]
        self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}
        self.defender = None
        self.attack = None

    def game_over(self, desk):
        return desk.is_empty and sum(x.is_alive() for x in self.players) == 1

    def run2(self):
        desk = Desk()
        for i in self.players:
            i.desk = desk.issue_cards(6)
        for i in self.players:
            print(i, i.amount_cart())
        n = 0
        while not self.game_over(desk):
            if not self.defender:
                self.attack = self.players[n % 2]
                self.defender = self.players[(n+1) % 2]
            num = 0
            while num < 6:
                print(self.attack)
                cart = self.attack.go(self.task)
                if not self.attack.is_alive():
                    break
                if cart:
                    self.task[cart[-1]].append(cart[:-1])
                    print()
                    print(self.task)
                    print()
                    print(self.defender)
                    cart = self.defender.go(self.task, defend=cart)
                    if not self.defender.is_alive():
                        break
                if isinstance(cart, str):
                    self.task[cart[-1]].append(cart[:-1])
                else:
                    if not cart:
                        n = 1 if n == 0 else 0
                        self.defender = None
                    num = 6
                    self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}
            print(self.task)
            print()
            for i in self.players:
                if i.amount_cart() < 6:
                    add_cart = desk.issue_cards(6 - i.amount_cart())
                    for j in add_cart:
                        i.desk[j].extend(add_cart[j])
                print(i, i.amount_cart())



    def run(self):
        desk = Desk()
        for i in self.players:
            i.desk = desk.issue_cards(6)
        # for i in self.players:
        #     print(i, i.amount_cart())
        n = 0
        while not self.game_over(desk):
            if not self.defender:
                self.attack = [i for i in self.players if i.number != (n+1) % len(self.players)]
                self.defender = self.players[(n+1) % len(self.players)]
            num = 0
            while num < 6:
                for attack in self.attack:
                    while True:
                        print(attack)
                        cart = attack.go(self.task)
                        if cart:
                            self.task[cart[-1]].append(cart[:-1])
                            print(self.task)
                            print()
                            print(self.defender)
                            cart = self.defender.go(self.task, defend=cart)
                        if isinstance(cart, str):
                            self.task[cart[-1]].append(cart[:-1])
                        else:
                            break
                        num += 1
                num = 6
            else:
                self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}
            print(self.task)
            print()
            # else:
            #         self.task = {'П': [], 'К': [], 'Б': [], 'Ч': []}
            #         break
            for i in self.players:
                print(i, i.amount_cart())
                if i.amount_cart() < 6:
                    add_cart = desk.issue_cards(6-i.amount_cart())
                    for j in add_cart:
                        i.desk[j].extend(add_cart[j])
                print(i, i.amount_cart())


first = Full(2)
first.run2()
