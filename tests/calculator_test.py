"""Testing the Calculator"""
import pprint

import pytest

from calculator.calculator import Calculator

# this is how you define a function that will run each time you pass it to a test, it is called a fixture


@pytest.fixture
def clear_history():
    Calculator.clear_history()


def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.get_history_count() == 4
    assert Calculator.get_last_calculation_result() == 6
    pprint.pprint(Calculator.history)


def test_clear_history(clear_history):
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.get_history_count() == 4
    Calculator.clear_history()
    assert Calculator.get_history_count() == 0


def test_count_history(clear_history):
    assert Calculator.get_history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_history_count() == 2


def test_get_last_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_last_calculation_result() == 5


def test_get_first_calculation(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    first_calculation = Calculator.get_first_calculation()
    assert first_calculation.get_result()


def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2
