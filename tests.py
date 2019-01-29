from src.encoder import Encoder
from src.decoder import Decoder
from src.basics.gf import GF
from src.basics.exceptions import CannotDetectErrorException

k = [4, 12, 20, 26, 27]
tests_types = ['multiple', 'burst']


def run_tests():
    e = Encoder()
    d = Decoder(coding_polynomial=e.coding_polynomial, k=e.k, t=e.r, gf_index=e.gf.index)

    message = "zaqwsxcderfvbgtyhnmjuik,ol.p;/zaqwsxedcrfvtgbyhnujmzaqwsxcderf"
    codeword = e.encode(message)
    decoded_message = d.decode(codeword, 'basic')

    for i in range(2, 28):
        codeword.elements[i] = codeword.elements[i].multiplicative_inversion()
    print('27 errors occurred...')
    print(codeword)
    decoded_message = d.decode(codeword, 'basic')
    print('Decoded message: ' + decoded_message[:len(message)])


if __name__ == '__main__':
    for t in tests_types:
        for i in k:
            run_tests(k, t)
