from divisor_master import dividers_num, max_divider


def test_div_list():
    assert dividers_num(30) == []


def test_max_div():
    assert max_divider(30) == 15