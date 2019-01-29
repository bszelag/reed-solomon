from src.basics.exceptions import DivideByZeroException


class Bit:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __add__(self, other):
        result = Bit(self.value ^ other.value)
        return result

    def __sub__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        result = Bit(self.value & other.value)
        return result

    def __truediv__(self, other):
        if other.value == 0:
            raise DivideByZeroException(message='Cannot divide by zero')
        result = Bit(self.value)
        return result

    __div__ = __truediv__
