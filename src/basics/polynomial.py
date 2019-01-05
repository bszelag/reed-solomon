import logging
from bit import Bit
from exceptions import DivideByZeroException


class Polynomial:

    def __init__(self, elements):
        self.index = len(elements)
        self.elements = elements
        self.zero = Bit(0) if isinstance(self.elements[0], Bit) else Bit(0)
        self.one = Bit(1) if isinstance(self.elements[0], Bit) else Bit(1)

    def __len__(self):
        self.index = len(self.elements)
        return self.index

    def __str__(self):
        result = ''
        for e in self.elements:
            result = result + str(e.value)
        return result

    def __eq__(self, other):
        a_index = self.get_index_of_one()
        if a_index is None:
            a_elements = [Bit(0)]
        else:
            a_elements = self.elements[a_index:]

        b_index = other.get_index_of_one()
        if b_index is None:
            b_elements = [Bit(0)]
        else:
            b_elements = other.elements[b_index:]
        if len(a_elements) != len(b_elements):
            return False
        return a_elements == b_elements

    def __ge__(self, other):
        """
        :param other:
        :return:
        """
        a_index = self.get_index_of_one()
        if a_index is None:
            a_elements = [Bit(0)]
        else:
            a_elements = self.elements[a_index:]

        b_index = other.get_index_of_one()
        if b_index is None:
            b_elements = [Bit(0)]
        else:
            b_elements = other.elements[b_index:]

        if len(a_elements) > len(b_elements):
            return True
        if len(a_elements) < len(b_elements):
            return False
        for i in range(len(a_elements)):
            if a_elements[i] < b_elements[i]:
                return False
            elif a_elements[i] > b_elements[i]:
                return True
        return True

    def get_index_of_one(self):
        for i in range(len(self.elements)):
            if self.elements[i].value == self.one.value:
                return i
        return None

    def __lt__(self, other):
        return not self.__ge__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        a_poly = self.elements
        b_poly = other.elements
        result_elements = []
        diff = abs(len(a_poly) - len(b_poly))
        if len(a_poly) > len(b_poly):
            b_poly = diff*[self.zero] + b_poly
        else:
            a_poly = diff*[self.zero] + a_poly
        for i in range(len(a_poly))[::-1]:
            result_elements.append(a_poly[i] + b_poly[i])
        result = Polynomial(result_elements[::-1])
        return result

    def __sub__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        result_elements = []
        for i in range(len(self.elements))[::-1]:
            partial_results = []
            for j in range(len(other.elements))[::-1]:
                partial_results.append(self.elements[i] * other.elements[j])
            shift_value = len(self.elements) - i - 1
            result_elements.append(Polynomial(partial_results[::-1] + shift_value*[self.zero]))
        result = result_elements[0]
        for r in result_elements[1:]:
            result = result + r
        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if other == Polynomial([self.zero]):
            raise DivideByZeroException('Cannot divide polynomial by zero!')
        result_elements = []
        reminder_elements = [Bit(0)]

        for i in range(len(self.elements)):
            reminder_elements = reminder_elements + [self.zero]
            reminder_elements[len(reminder_elements)-1] = self.elements[i]
            logging.error("reminder: " + str(Polynomial(reminder_elements)))
            logging.error("other: " + str(other))
            if Polynomial(reminder_elements) >= other:
                logging.error("result of r-d = " + str(Polynomial(reminder_elements) - other))
                reminder_elements_result_poly = Polynomial(reminder_elements) - other
                reminder_elements = reminder_elements_result_poly.elements
                result_elements.insert(i, self.one)
            else:
                result_elements.insert(i, self.zero)

        if not result_elements:
            result_elements = [Bit(0)]
        return Polynomial(result_elements), Polynomial(reminder_elements)
