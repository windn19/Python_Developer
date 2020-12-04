from divisor_master import is_prime_num, biggest_simple_divider, list_simple_divider  # импорт методов из модуля


def test_is_prime_num():  # набор методов для тестирования
    assert is_prime_num(97)


def test_is_prime_num1():
    assert is_prime_num('234')


def test_is_prime_num2():
    assert is_prime_num([234, 456])


def test_biggers():
    assert biggest_simple_divider(30) == 15


def test_biggers1():
    assert biggest_simple_divider(30) == 5


def test_list_prime():
    assert list_simple_divider(30) == [1, 2, 4]


def test_list_prime1():
    assert list_simple_divider(30) == [2, 3, 5]