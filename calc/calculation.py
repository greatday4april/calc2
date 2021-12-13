from re import M
from typing import Tuple
from datetime import datetime


class Calculation:

    # contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self, values: Tuple[float]):
        # self references the instantiated object of the class
        # these are instance properties that are being sharred with the child classes (addition, subtraction, etc...)
        self.values = list(values)
        self.time = datetime.now()

    # Class Factory Method <- bound to the class and not the instance of the class
    @classmethod
    def create(cls, values: Tuple[float]):
        return cls(values)

    def to_str(self):
        data = self.to_dict()
        return "{};{};{};{}".format(
            data["operated_values"],
            data["operation"],
            data["result"],
            data["operation_time"],
        )

    def to_dict(self):
        return {
            "operated_values": ",".join([str(v) for v in self.values]),
            "operation": type(self).__name__,
            "result": self.get_result(),
            "operation_time": self.time.isoformat(),
        }

    def get_result(self):
        raise NotImplementedError(
            "Child classes should always be used instead of calculation base class",
        )
