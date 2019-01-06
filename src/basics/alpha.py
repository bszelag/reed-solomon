from src.basics.exceptions import AlphasFromDifferentField


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
        return Alpha(index=None, value=result, gf_index=self.gf_index)

    def __sub__(self, other):
        return self.__add__(other)

    def set_value(self, value):
        self.value = value

    def set_index(self, index):
        self.index = index

    def __mul__(self, other):
        index = (self.index + other.index) % (2 ** self.gf_index)
        return Alpha(index=index, value=None, gf_index=self.gf_index)

    def multiplicative_inversion(self):
        index = (2**self.gf_index - 1 - self.index)
        return Alpha(index=index, value=None, gf_index=self.gf_index)

    def __str__(self):
        return "Index: " + str(self.index) + ", Value: " + str(self.value)
