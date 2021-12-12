from calc.calculation import Calculation


class Subtraction(Calculation):
    """The subtraction class has one method to get the result of the the calculation A and B come from the calculation parent class"""

    def get_result(self):
        return sum(-1 * v for v in self.values)
