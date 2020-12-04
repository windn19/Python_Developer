from divisor_master import dividers_num, max_divider  # импорт методов из модуля


def test_div_list():  # набор тесто для этих методов
    assert dividers_num(30) == []


def test_max_div():
    assert max_divider(30) == 15
