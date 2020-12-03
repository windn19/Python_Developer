from math import factorial as fact


def c(n, m):
    return fact(n) / (fact(n - m) * fact(m))


assert c(4, 2) == 6, 'Ok'
assert c(10, 3) == 8, 'fre'
