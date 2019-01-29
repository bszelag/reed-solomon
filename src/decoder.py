from src.basics.gf import GF
from src.basics.polynomial import Polynomial
from src.basics.exceptions import CannotDetectErrorException

import logging


class Decoder:

    def __init__(self, coding_polynomial, k, t, gf_index):
        self.coding_polynomial = coding_polynomial
        self.k = k
        self.t = int((t-1)/2)
        self.gf_index = gf_index
        self.n = 2 ** self.gf_index - 1
        self.decoders = {'basic': self.get_decoded_polynomial, 'advanced': self.advanced_decoder}

    def get_syndrome(self, codeword):
        return codeword % self.coding_polynomial

    def code_is_valid(self, codeword):
        return self.get_syndrome(codeword) == Polynomial([GF.Alpha(-1, 0, self.gf_index)])

    def get_decoded_polynomial(self, codeword):
        if self.code_is_valid(codeword):
            return codeword
        else:
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

    def _get_error_locator(self, syndrome):
        sigma, omega = 0, 0
        return sigma, omega

    def _find_errors_chien_search(self, sigma):
        x, j = 0, 0
        return x, j

    def _find_error_magnitude_forney(self, omega, x):
        y = 0
        return y

    def advanced_decoder(self, codeword):
        # TODO - ALGORITHM
        # Calculate syndrome
        # Find error locator polynomial L(x) and number of errors with Berlekamp's algorithm
        # Find roots of L(x) with Chien search
        # Using Forney's algorithm find symbol error values (using syndrome and L(x) roots)
        # Fix message
        if self.code_is_valid(codeword):
            return codeword[:-(self.n - self.k)]
        else:
            syndrome = self.get_syndrome(codeword)
            sigma, omega = self._get_error_locator(syndrome)
            x, j = self._find_errors_chien_search(sigma)
            if x is None or j is None:
                raise CannotDetectErrorException
            y = self._find_error_magnitude_forney(omega, x)

            errors = Polynomial([GF.Alpha(-1, 0, self.gf_index)])

            message_output = codeword - errors
            if not self.code_is_valid(message_output):
                raise CannotDetectErrorException
            return message_output

    def decode(self, codeword, algorithm):
        full_decoded_polynomial = self.decoders[algorithm](codeword)
        decoded_polynomial = Polynomial(full_decoded_polynomial.elements[:-(self.n-self.k)])
        binary_result = ''
        result = []

        for i in range(len(decoded_polynomial)):
            w = format(decoded_polynomial.elements[i].value, '07b')
            binary_result = binary_result + w

        last_bits = len(binary_result) % 8
        binary_result = binary_result[:-last_bits]

        for i in range(0, len(binary_result), 8):
            w = int(binary_result[i:i+8], 2)
            result.append(w)

        logging.info(result)

        return ''.join([chr(x) for x in result])
