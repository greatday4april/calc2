from calc.calculation import Calculation


class Division(Calculation):
    """The division class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):
        output = 1.0
        for value in self.values:
            output /= value
        return output
