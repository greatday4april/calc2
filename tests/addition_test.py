from calc.addition import Addition


def test_addition_create():
    calc_obj = Addition.create((1, 2, 3))
    assert isinstance(calc_obj, Addition)


def test_addition_get_result():
    calc_obj = Addition.create((1, 2, 3))
    assert calc_obj.get_result() == 6
