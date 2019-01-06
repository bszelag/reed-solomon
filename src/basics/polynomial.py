import logging
from src.basics.bit import Bit


class Polynomial:

    def __init__(self, elements):
        self.index = len(elements)
        self.elements = elements
        self.zero = Bit(0) if isinstance(self.elements[0], Bit) else type(self.elements[0])(-1, 0)
        self.one = Bit(1) if isinstance(self.elements[0], Bit) else type(self.elements[0])(0, 1)
        a_index = self.get_index_of_non_zero_element()
        if a_index is None:
            a_elements = [self.zero]
        else:
            a_elements = self.elements[a_index:]
        self.elements = a_elements

    def __len__(self):
        self.index = len(self.elements)
        return self.index

    def __str__(self):
        result = ''
        for e in self.elements:
            result = result + str(e.value)
        return result

    def __eq__(self, other):
        return self.elements == other.elements

    def __ge__(self, other):
        if len(self.elements) > len(other.elements):
            return True
        if len(self.elements) < len(other.elements):
            return False
        for i in range(len(self.elements)):
            if self.elements[i] < other.elements[i]:
                return False
            elif self.elements[i] > other.elements[i]:
                return True
        return True

    def get_index_of_non_zero_element(self):
        for i in range(len(self.elements)):
            if self.elements[i].value > 0:
                return i
        return None

    def __lt__(self, other):
        return not self.__ge__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        a_poly = self.elements
        b_poly = other.elements
        logging.error('a=' + str(Polynomial(a_poly)) + '+ b=' + str(Polynomial(b_poly)))
        result_elements = []
        diff = abs(len(a_poly) - len(b_poly))
        if len(a_poly) > len(b_poly):
            b_poly = diff*[self.zero] + b_poly
        elif len(a_poly) < len(b_poly):
            a_poly = diff*[self.zero] + a_poly

        for i in range(len(a_poly)):
            result = a_poly[i] + b_poly[i]
            logging.error(str(a_poly[i]) + ' + ' + str(b_poly[i]) + ' = ' + str(result))
            result_elements.append(result)
        result = Polynomial(result_elements)
        return result

    def __radd__(self, other):
        return self.__add__(other)

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

    def __divmod__(self, other):
        q = Polynomial([self.zero])
        r = Polynomial(self.elements)
        while r != Polynomial([self.zero]) and len(r) >= len(other):
            t = r.elements[0] / other.elements[0]
            t = Polynomial([t]+[self.zero]*(len(r) - len(other)))
            q = q + t
            r = r - (t * other)
            logging.error(r)
            logging.error(q)
        return q, r

    def __mod__(self, other):
        _, reminder = self.__divmod__(other)
        return reminder

    def __truediv__(self, other):
        result, _ = self.__divmod__(other)
        return result

    __div__ = __truediv__

    def get_string_representation(self):
        result = ''
        for e in self.elements:
            result = result + str(e.value)
        return result

#
# if __name__ == '__main__':
#     # a = Polynomial([Bit(1), Bit(1), Bit(1), Bit(0), Bit(1)])
#     # b = Polynomial([Bit(1), Bit(1)])
#     # print(a/b)
#     # a = Polynomial([Alpha(1, 1, 3), Alpha(2, 2, 3), Alpha(3, 4, 3)])
#     # b = Polynomial([Alpha(4, 3, 3), Alpha(5, 6, 3), Alpha(6, 7, 3)])
#     # print(a+b)
