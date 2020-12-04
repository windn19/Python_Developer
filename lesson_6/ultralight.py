from math import factorial as fact  # импорт метода вычисления факториала с псевдонимом  из библиотеки


def c(n, m):
    """
    количество сочетаний m элементов из n
    """
    return fact(n) / (fact(n - m) * fact(m))


assert c(4, 2) == 6, 'все в порядке'
assert c(10, 3) == 8, 'Далеко не все в порядке'
