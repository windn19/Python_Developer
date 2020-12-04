from math import factorial as fact  # импорт метода фактора из библиотеке main


def c(n, m):
    """
    Количество сочетаний m элементов из n
    """
    return fact(n) / (fact(n - m) * fact(m))


assert c(4, 2) == 6, 'Все в порядке'
assert c(10, 3) == 8, 'Не все в порядке'
