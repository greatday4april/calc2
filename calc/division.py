from calc.calculation import Calculation


class Division(Calculation):
    """The division class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):
        return self.value_a / self.value_b
