from typing import Tuple


class Calculation:

    # contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self, values: Tuple[float]):
        # self references the instantiated object of the class
        # these are instance properties that are being sharred with the child classes (addition, subtraction, etc...)
        self.values = list(values)

    # Class Factory Method <- bound to the class and not the instance of the class
    @classmethod
    def create(cls, values: Tuple[float]):
        return cls(values)

    def get_result(self):
        raise NotImplementedError(
            'Child classes should always be used instead of calculation bas class',
        )
