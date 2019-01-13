from src.basics.polynomial import Polynomial
from src.basics.bit import Bit

import logging


class GF:

    alpha_elements_by_index = {}
    alpha_elements_by_value = {}

    def __init__(self, generating_polynomial=Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(0), Bit(1)])):
        self.generating_polynomial = generating_polynomial
        self.index = len(self.generating_polynomial) - 1
        self.alpha_elements = []
        self.generate_alpha_elements()
        self.assign_alphas_to_dicts()

    def generate_alpha_elements(self):
        all_alpha_elements = pow(2, self.index) - 1
        self.alpha_elements.append(self.Alpha(index=-1, value=0, gf_index=self.index))
        poly = Polynomial([Bit(1)])
        for i in range(all_alpha_elements):
            a = poly % self.generating_polynomial
            self.alpha_elements.append(self.Alpha(index=i, value=int(a.get_string_representation(), 2), gf_index=self.index))
            poly = Polynomial(poly.elements + [Bit(0)])

    def assign_alphas_to_dicts(self):
        for a in self.alpha_elements:
            GF.alpha_elements_by_index[a.index] = a.value
            GF.alpha_elements_by_value[a.value] = a.index

    def __str__(self):
        result = ''
        for a in self.alpha_elements:
            result = result + '(' + str(a) + ')'
        result = result + ", Generating polynomial: " + str(self.generating_polynomial)
        return result

    class Alpha:
        def __init__(self, index, value, gf_index=7):
            self.index = index
            self.value = value
            self.gf_index = gf_index

        def __eq__(self, other):
            return self.value == other.value

        def __ne__(self, other):
            return not self.__eq__(other)

        def __add__(self, other):
            result = self.value ^ other.value
            return GF.Alpha(index=GF.alpha_elements_by_value[result], value=result, gf_index=self.gf_index)

        def __sub__(self, other):
            return self.__add__(other)

        def set_value(self, value):
            self.value = value

        def set_index(self, index):
            self.index = index

        def __mul__(self, other):
            index = (self.index + other.index) % (2 ** self.gf_index - 1)
            return GF.Alpha(index=index, value=GF.alpha_elements_by_index[index], gf_index=self.gf_index)

        def multiplicative_inversion(self):
            index = (-1 * self.index) % (2**self.gf_index - 1)
            return GF.Alpha(index=index, value=GF.alpha_elements_by_index[index], gf_index=self.gf_index)

        def __str__(self):
            return "Index: " + str(self.index) + ", Value: " + str(self.value)

        def __truediv__(self, other):
            index = self.index - other.index
            if index < 0:
                index = index % (2**self.gf_index - 1)
            return GF.Alpha(index=index, value=GF.alpha_elements_by_index[index], gf_index=self.gf_index)

        __div__ = __truediv__
