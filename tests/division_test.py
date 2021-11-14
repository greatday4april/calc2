from calc.division import Division


def test_division_create():
    calc_obj = Division.create(1, 2)
    assert isinstance(calc_obj, Division)


def test_division_get_result():
    calc_obj = Division.create(9, 2)
    assert calc_obj.get_result() == 4.5
    calc_obj = Division.create(9, 3)
    assert calc_obj.get_result() == 3
