from calc.calculation import Calculation


class Multiplication(Calculation):
    """The multiplication class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):
        # you need to use self to reference the data contained in the instance of the object.  This is encapsulation
        return self.value_a * self.value_b
