from src.basics.gf import GF
from src.basics.polynomial import Polynomial
from src.basics.exceptions import CannotDetectErrorException


class Decoder:
    def __init__(self, coding_polynomial, k, t, gf_index):
        self.coding_polynomial = coding_polynomial
        self.k = k
        self.t = int((t-1)/2)
        self.gf_index = gf_index
        self.n = 2 ** self.gf_index - 1

    def get_syndrome(self, codeword):
        return codeword % self.coding_polynomial

    def check_if_code_is_valid(self, codeword):
        return self.get_syndrome(codeword) == Polynomial([GF.Alpha(-1, 0, self.gf_index)])

    def get_decoded_polynomial(self, codeword):
        for i in range(0, self.k):
            syndrome = self.get_syndrome(codeword)
            weight = syndrome.get_hamming_weight()
            # print('Code: ' + str(codeword) + ' len=' + str(len(codeword)))
            # print('Syndrome: ' + str(syndrome) + ', Weight: ' + str(weight))
            if weight <= self.t:
                newcodeword = codeword + syndrome
                if i > 0:
                    new_elements = newcodeword.elements[i:] + newcodeword.elements[0:i]
                    return Polynomial(new_elements)
                else:
                    return newcodeword

            else:
                codes = [*[codeword.elements[len(codeword)-1]], *(self.n - len(codeword.elements))*[GF.Alpha(-1, 0, self.gf_index)], *codeword.elements[0:len(codeword)-1]]
                codeword = Polynomial(codes)
        raise CannotDetectErrorException

    def decode(self, codeword):
        decoded_polynomial = self.get_decoded_polynomial(codeword)
        print(decoded_polynomial)
        result = []

        for i in range(len(codeword)):
            w = int(bin(decoded_polynomial.elements[i].value), 2)
            result.append(w)

        return ''.join([chr(x) for x in result])
