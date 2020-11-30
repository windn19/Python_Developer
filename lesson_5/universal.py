from math import factorial as fact  # импорт функции факториала из math


def p(n):
    """
    расчет перестановок
    """
    return fact(n)


def a(n, m):
    """
    расчет количество размещений m элементов из n
    """
    return c(n, m) * p(m)


def bernully(n, k, p):
    """
    Формула Бернулли для выпадения k элементов из n с вероятностью p
    """
    return c(n, k) * (p ** k) * (1 - p) ** (n - k)


def c(n, m):
    """
    Количество  сочетаний m элементов из n
    """
    return fact(n) / (fact(n - m) * fact(m))


def a_repl(n, k):
    """
    количество размещений с повторением k элементов из n
    """
    return n ** k


def p_repl(n, n_list):
    """
    количество размещений с повторением
    n - общее число элементов
    n_list - количество повторений элементов
    """
    num = 1  # объявление переменной
    for i in n_list:  # для каждого элемента делай
        num *= fact(i)  # перемножение количества перестановок
    return fact(n) / num


def c_repl(n, m):
    """
    количество сочетаний с повторением m элементов из n
    """
    return fact(n + m - 1) / (fact(n - 1) * fact(m))
