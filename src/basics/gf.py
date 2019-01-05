from polynomial import Polynomial
from alpha import Alpha
from bit import Bit


class GF:
    def __init__(self):
        self.index = 7
        self.generating_polynomial = Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(0), Bit(1)])
        self.alpha_elements = []
        self.generate_alpha_elements()

    def add_alpha_element(self, alpha):
        self.alpha_elements.append(alpha)

    def generate_alpha_elements(self):
        for i in range(self.index):
            index = i
            elements = self.index * [Bit(0)]
            elements[self.index - i - 1] = Bit(1)
            self.add_alpha_element(Alpha(index=index, elements=Polynomial(elements), gf_index=self.index))

    def __str__(self):
        return "Alpha elements: " + str(self.alpha_elements) + ", Generating polynomial: " + str(self.generating_polynomial)
