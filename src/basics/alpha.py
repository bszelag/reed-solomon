from src.basics.exceptions import AlphasFromDifferentField


class Alpha:
    def __init__(self, index, value, gf_index=7):
        self.index = index
        self.value = value
        self.gf_index = gf_index

    def __eq__(self, other):
        return (self.index == other.index) and (self.value == other.value)

    def __ne__(self, other):
        return not self.__eq__(other)

    # def get_value(self):
    #     elements_value = ''
    #     for e in self.elements.elements:
    #         elements_value = elements_value + str(e.value)
    #     return int(elements_value, 2)

    def __add__(self, other):
        elements = self.value + other.value
        return Alpha(index=None, value=elements, gf_index=self.gf_index)

    def __sub__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        index = (self.index * other.index) % self.gf_index
        return Alpha(index=index,value=None, gf_index=self.gf_index)

    def multiplicative_inversion(self):
        index = (2**self.gf_index - 1 - self.index)
        return Alpha(index=index, value=None, gf_index=self.gf_index)

    def __str__(self):
        return "Index: " + str(self.index) + ", Value: " + str(self.value)
