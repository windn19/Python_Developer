from math import pi, sqrt, pow, hypot  # набор методов для тестирования


def test_pi():  # набор методов для проверки
    assert pi == 3.14


def test_pi2():
    assert pi == 'yes'


def test_sqrt():
    assert sqrt(9) == 3


def test_sqrt1():
    assert sqrt(16) == 5


def test_pow():
    assert pow(2, 2) == 4


def test_pow1():
    assert pow(4, 2) == 25


def test_hypot():
    assert hypot(4, 3) == 5


def test_hypot1():
    assert hypot(5, 6) == 6
# filter, map, sorted


def test_filter():
    assert filter(lambda x: x > 0, [2, -1, 3, -2])


def test_filter1():
    assert filter(lambda x: x < 0, [2, -1, '3', -2])


def test_map():
    assert map(lambda x: x**2, [2, -1, 3, -2])


def test_map1():
    assert map(lambda x: x**2, [2, -1, 3, '-2'])


def test_sort():
    assert sorted([2, -1, 3, -2]) == [-2, -1, 2, 3]


def test_sort1():
    assert sorted([2, -1, 3, -2]) == []