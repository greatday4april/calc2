""" This is the increment function"""

from pathlib import Path
from typing import List
from calc.addition import Addition
from calc.calculation import Calculation
from calc.division import Division
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from datetime import datetime


class Calculator:
    """This is the Calculator class"""

    # this is the calculator static property
    HISTORY_FILE_PATH = Path("history.csv").absolute()
    history: List[Calculation] = []

    @staticmethod
    def load_history():
        Calculator.history = []
        lines = open(Calculator.HISTORY_FILE_PATH, "r").readlines()
        lines = [line.strip() for line in lines if len(line.strip()) != 0]
        for line in lines:
            values_str, operation, result, time = line.split(";")
            values = [float(v) for v in values_str.split(",")]
            if operation == "Addition":
                calc = Addition.create(values)
            elif operation == "Subtraction":
                calc = Subtraction.create(values)
            elif operation == "Multiplication":
                calc = Multiplication.create(values)
            elif operation == "Division":
                calc = Division.create(values)
            else:
                raise Exception("unsupported operation type: {}".format(operation))

            calc.result = result
            calc.time = datetime.fromisoformat(time)
            Calculator.history.append(calc)

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
    def add_calculation_to_history(calculation: Calculation):
        Calculator.history.append(calculation)
        with open(Calculator.HISTORY_FILE_PATH, "a") as f:
            f.write(calculation.to_str() + "\n")

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
        with open(Calculator.HISTORY_FILE_PATH, "w") as f:
            f.truncate()
        return len(Calculator.history)

    @staticmethod
    def add_number(values):
        """adds number to result"""
        addition = Addition.create(values)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation_result()

    @staticmethod
    def subtract_number(values):
        """subtract number from result"""
        subtraction = Subtraction.create(values)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation_result()

    @staticmethod
    def multiply_numbers(values):
        """multiply two numbers and store the result"""
        multiplication = Multiplication.create(values)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_last_calculation_result()

    @staticmethod
    def divide_numbers(values):
        """divide two numbers and store the result"""
        division = Division.create(values)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_last_calculation_result()
