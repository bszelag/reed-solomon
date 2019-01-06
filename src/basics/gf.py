from src.basics.polynomial import Polynomial
# from src.basics.alpha import Alpha
from src.basics.bit import Bit

import logging


class GF:
    def __init__(self, generating_polynomial=Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(0), Bit(1)])):
        self.generating_polynomial = generating_polynomial
        self.index = len(self.generating_polynomial) - 1
        self.alpha_elements = []
        self.alpha_elements_by_index = {}
        self.alpha_elements_by_value = {}
        self.generate_alpha_elements()
        self.assign_alphas_to_dicts()

    def generate_alpha_elements(self):
        all_alpha_elements = (pow(2, self.index))
        self.alpha_elements.append(self.Alpha(index=0, value=0, gf_index=self.index))
        poly = Polynomial([Bit(1)])
        for i in range(1, all_alpha_elements):
            a = poly % self.generating_polynomial
            logging.error(a)
            self.alpha_elements.append(self.Alpha(index=i, value=int(a.get_string_representation(), 2), gf_index=self.index))
            poly = Polynomial(poly.elements + [Bit(0)])

    def assign_alphas_to_dicts(self):
        for a in self.alpha_elements:
            self.alpha_elements_by_index[a.index] = a.value
            self.alpha_elements_by_value[a.value] = a.index

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
            return GF.Alpha(index=None, value=result, gf_index=self.gf_index)

        def __sub__(self, other):
            return self.__add__(other)

        def set_value(self, value):
            self.value = value

        def set_index(self, index):
            self.index = index

        def __mul__(self, other):
            index = (self.index + other.index) % (2 ** self.gf_index)
            return GF.Alpha(index=index, value=GF.alpha_elements_by_index(index), gf_index=self.gf_index)

        def multiplicative_inversion(self):
            index = (2**self.gf_index - 1 - self.index)
            return GF.Alpha(index=index, value=GF.alpha_elements_by_index(index), gf_index=self.gf_index)

        def __str__(self):
            return "Index: " + str(self.index) + ", Value: " + str(self.value)
