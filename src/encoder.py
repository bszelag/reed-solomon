from src.basics.gf import GF
from src.basics.polynomial import Polynomial
from src.basics.bit import Bit
from src.basics.alpha import Alpha


class Encoder:
    def __init__(self, generating_polynomial=Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(0), Bit(1)]), k=73, s=7):
        self.gf = GF(generating_polynomial=generating_polynomial)
        self.n = 2 ** self.gf.index - 1
        self.k = k
        self.s = s
        self.r = self.n - self.k
        self.d = self.r + 1
        self.coding_polynomial = self.get_coding_polynomial()

    def get_coding_polynomial(self):
        result = Polynomial([Alpha(1, 1, self.gf.index), Alpha(1, 1, self.gf.index)])
        for i in range(2, self.r):
            result = result * Polynomial([Alpha(1, 1, self.gf.index),
                                          Alpha(i, self.gf.alpha_elements_by_index[i], self.gf.index)])
            print('Partial result coding: ' + str(result))
        print(result)
        return result

    def encode(self, word):
        pass
