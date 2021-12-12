from calc.multiplication import Multiplication


def test_multiplication_create():
    calc_obj = Multiplication.create((1, 2))
    assert isinstance(calc_obj, Multiplication)


def test_multiplication_get_result():
    calc_obj = Multiplication.create((3, 4))
    assert calc_obj.get_result() == 12
