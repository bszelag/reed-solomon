from exceptions import AlphasFromDifferentField


class Alpha:
    def __init__(self, index, elements, gf_index):
        """
        Alpha is an element of GF
        :param index: element's index
        :param value:  element's value
        :param elements: elements in Polynomial
        :param gf_index: number of elements in GF
        """
        self.index = index
        self.elements = elements
        self.gf_index = gf_index
        self.value = self.get_value()

    def __eq__(self, other):
        return (self.index == other.index) and (self.gf_index == other.gf_index) and (self.value == other.value) and (self.elements == other.elements)

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_value(self):
        elements_value = 0
        weight = self.gf_index - 1
        for e in self.elements.elements:
            elements_value = elements_value + (e.value * (2 ^ weight))
            weight = weight - 1
        return elements_value

    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise AlphasFromDifferentField
        elements = self.elements + other.elements
        return Alpha(index=None, elements=elements, gf_index=self.gf_index)

    def __sub__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        index = (self.index * other.index) % self.gf_index
        return Alpha(index=index, elements=None, gf_index=self.gf_index)

    def multiplicative_inversion(self):
        index = (self.gf_index - self.index)
        return Alpha(index=index, elements=None, gf_index=self.gf_index)

    def __str__(self):
        return "Index: " + str(self.index) + ", Value: " + str(self.value) + ", Elements: " + self.elements
