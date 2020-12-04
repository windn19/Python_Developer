def prime_def():
    """
    нахождение множества простых чисел
    """
    prime_set = set(range(1, 1001))  # множество всех чисел от 1 до 1000
    for i in range(2, 101):  # перебор всех чисел от 2 до корня из 1000
        if i in prime_set:  # если очерендное число в множестве
            prime_set -= set(range(2 * i, 1001, i))  # то в множестве само число, а остальные его множители удаляем
    return prime_set


def is_prime_num(num):
    """
    Проверка числа на простоту
    """
    global PRIME_SET  # применение глобальной переменной PRIME_SET
    if not PRIME_SET:  # если она не определена
        PRIME_SET = prime_def()  # то запустить метод по ее определению
    return num in PRIME_SET


def dividers_num(num):
    """
    Выводит множетели числа num
    """
    result = []  # объявление результирующего списка
    for i in range(1, num // 2 + 1):  # перебор всех чисел от 1 до  num // 2 + 1
        if num % i == 0:  # если число делится на i без остатка
            result.append(i)  # то добавляем i в результирующий список
    return result+[num]  # возврат результирующего списка плюс само число в форме списка


def prepare_prime_set(num):
    """
    Нахождение списка простых чисел меньше или равных num
    """
    global PRIME_SET  # применение глобальной переменной PRIME_SET
    if not PRIME_SET:  # если она не определена
        PRIME_SET = prime_def()  # то запустить метод по ее определению
    prime_list = sorted(list(PRIME_SET))  # сортировка множества простых чисел преобразованных в лист
    prime_list = [i for i in prime_list if i <= num]  # отбор только чисел, которые меньше или равны num
    return prime_list


def biggest_simple_divider(num):
    """
    нахождение самого большого простого делителя num
    """
    prime_list = prepare_prime_set(num)  # вызов метода формирования списка простых чисел меньше или равных num
    for i in reversed(prime_list):  # каждый элемент из этого списка начиная с самого большого
        if num % i == 0:  # разделить на num и если не будет остатка
            return i  # возвратить его и прекратить выполнение функции


def list_simple_divider(num):
    prime_list = prepare_prime_set(num)  # вызов метода формирования списка простых чисел меньше или равных num
    result = []  # объявление результирующего списка
    for i in reversed(prime_list):  # каждый элемент из этого списка начиная с самого большого
        while num % i == 0:  # пока элемент делится на i нацело делай
            num //= i  # элемент разделить на i и сохранить с тем же именем
            result.append(i)  # добавить элемент i в результирующий массив
        if num == 1:  # если в num равно 1
            break  # выйти из цикла
    return result


def max_divider(num):
    """
    Нахождение максимального делителя num
    """
    result = dividers_num(num)  # запуск метода поиска списка делителей
    return result[-2]   # возврат предпоследнего элемента


PRIME_SET = set()  # объявление PRIME_SET множеством