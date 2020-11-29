from math import factorial as fact


def p(n):
    return fact(n)


def a(n, m):
    return c(n, m) * p(m)


def bernully(n, k, p):
    return c(n, k) * (p ** k) * (1 - p) ** (n - k)


def c(n, m):
    return fact(n) / (fact(n - m) * fact(m))


def a_repl(n, k):
    return n ** k


def p_repl(n, n_list):
    num = 1
    for i in n_list:
        num *= fact(i)
    return fact(n) / num


def c_repl(n, m):
    return fact(n + m - 1) / (fact(n - 1) * fact(m))
