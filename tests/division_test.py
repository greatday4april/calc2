from calc.division import Division


def test_division_create():
    calc_obj = Division.create((1, 2))
    assert isinstance(calc_obj, Division)


def test_division_get_result():
    calc_obj = Division.create((4, 2))
    assert calc_obj.get_result() == 0.125
    calc_obj = Division.create((5, 4))
    assert calc_obj.get_result() == 0.05
