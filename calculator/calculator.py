""" This is the increment function"""

from typing import List
from calc.addition import Addition
from calc.calculation import Calculation
from calc.division import Division
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication


class Calculator:
    """ This is the Calculator class"""
    # this is the calculator static property
    history: List[Calculation] = []

    @staticmethod
    def get_history():
        return Calculator.history

    @staticmethod
    def get_first_calculation():
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation():
        return Calculator.get_last_calculation_object()

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)

    @staticmethod
    def get_last_calculation_result():
        return Calculator.get_last_calculation_object().get_result()

    @staticmethod
    def get_last_calculation_object():
        return Calculator.history[-1]

    @staticmethod
    def clear_history():
        Calculator.history.clear()

    @staticmethod
    def get_history_count():
        return len(Calculator.history)

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].get_result()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation_result()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_last_calculation_result()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        division = Division.create(value_a, value_b)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_last_calculation_result()
