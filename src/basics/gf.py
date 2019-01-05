from src.basics.polynomial import Polynomial
from src.basics.alpha import Alpha
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
        all_alpha_elements = (pow(2, self.index)) - 1
        logging.error(all_alpha_elements)
        poly = Polynomial([Bit(1)])
        for i in range(all_alpha_elements):
            a = poly % self.generating_polynomial
            logging.error(a)
            self.alpha_elements.append(Alpha(index=i, value=int(a.get_string_representation(), 2), gf_index=self.index))
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
