from src.basics.gf import GF
from src.basics.polynomial import Polynomial
from src.basics.bit import Bit


class Encoder:
    def __init__(self, generating_polynomial=Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(0), Bit(1)]), k=73, s=7):
        self.gf = GF(generating_polynomial=generating_polynomial)
        self.n = 2 ** self.gf.index - 1
        self.k = k
        # self.s = s
        self.r = self.n - self.k
        self.coding_polynomial = self.get_coding_polynomial()

    def get_coding_polynomial(self):
        result = Polynomial([GF.Alpha(1, 1, self.gf.index), GF.Alpha(1, 1, self.gf.index)])
        for i in range(2, self.r):
            result = result * Polynomial([GF.Alpha(1, 1, self.gf.index), GF.Alpha(i, self.gf.alpha_elements_by_index[i], self.gf.index)])
        return result

    def encode(self, word):
        word2encode = [ord(c) for c in word]
        word2alphas = []
        for i in range(len(word2encode)):
            w = int(bin(word2encode[i])[2:], 2)
            word2alphas.append(GF.Alpha(index=GF.alpha_elements_by_value[w], value=w, gf_index=self.gf.index))

        # print(len(word2alphas))

        word2poly = Polynomial(word2alphas + self.r*[GF.Alpha(-1, 0, self.gf.index)])
        # print(word2poly)
        # print(len(word2poly.elements))

        coding_reminder = word2poly % self.coding_polynomial
        # print(coding_reminder)
        # print(len(coding_reminder))

        code = word2poly + coding_reminder
        return code
