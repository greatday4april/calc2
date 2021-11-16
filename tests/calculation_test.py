import pytest
from calc.calculation import Calculation


def test_calculation_create():
    calc_obj = Calculation.create((1, 2, 3))
    assert isinstance(calc_obj, Calculation)


def test_calculation_get_result():
    calc_obj = Calculation.create((1, 2, 3))
    with pytest.raises(NotImplementedError):
        calc_obj.get_result()
