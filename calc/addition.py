from calc.calculation import Calculation


class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):
        return sum(v for v in self.values)
