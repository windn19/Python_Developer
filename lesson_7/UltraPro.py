import pickle
from os.path import exists

def menu(num):
    """
    Функция вывода меню
    :param num: сумма наличных денег
    :return: ответ пользователя
    """
    print(f'Доступная сумма: {num} руб.', end='\n\n')  # вывод наличных денег с добавлением пустой строки
    print('1. Пополнить счет')
    print('2. Совершить покупку')
    print('3. История покупок')
    print('4. Выход')
    ans = input('Введите номер пункта: ')  # ввод пункт меню пользователем
    return ans


def add(num, hist):
    """
    Добавление суммы покупки и ее наименования покупки
    :param num: количество наличных денег
    :param hist: список покупок
    :return: измененное количество наличных денег и список покупок
    """
    sale = input('Введите сумму покупки: ')  # ввод суммы покупки
    while not sale.replace('.', '', 1).isdigit():  # пока ввод пользователя с убиранием точек не цифры
        sale = input('Введите сумму покупки: ')  # снова ввести суммы
    sale = float(sale)  # перевод суммы в дробный тип данных
    if sale > num:  # если сумма покупки больше, чем сумма наличных денег
        print('Сумма покупки больше наличных денег')
    else:  # иначе
        name = input('Введите название покупки: ') # ввод название покупки
        hist.append((name, sale))  # добавление названия и суммы покупки в архив истории
        num -= sale  # вычитание суммы покупки из наличных денег
    save_sum((num, history))
    return num, hist


def save_sum(data):
    with open('exp.pickle', mode='wb') as f:
        pickle.dump(data, f)


# with open('exp.pickle', mode='wb') as f:
#     pickle.dump((car_data, num), f)
if exists('exp.pickle'):
    with open('exp.pickle', mode='rb') as f:
        num, history = pickle.load(f)
else:
    num = 0
    history = [] # объявление глобальных переменных

while True:  # вечный цикл
    ans = menu(num)  # получение ответа пользователя
    while ans not in ['1', '2', '3', '4']:  # пока ответ не в списке
        ans = menu(num)  # получение ответа пользователя
    if ans == '1':  # если выбран ответ 1
        amount = input('Введите сумму: ')  # ввод добавляемой суммы наличных денег
        while not amount.replace('.', '', 1).isdigit():   # пока ввод пользователя с убиранием точек не цифры
            amount = input('Введите сумму: ')  # повторить ввод суммы
        num += float(amount)  # добавить сумму к общей сумме наличных денег
        save_sum((num, history))
    elif ans == '2':  # если ответ 2
       num, history = add(num, history)  # запустить функцию добавления продуктов
    elif ans == '3':  # если ответ 3
        for name, sale in history:  # перебрать все элементы списка истории
            print(f'Было куплено {name} за {sale} руб.')  # и вывести его
    else:  # иначе
        break  # выйти из основного цикла
    print()
