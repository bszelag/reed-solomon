from src.encoder import Encoder
from src.decoder import Decoder
from src.basics.gf import GF
from src.basics.exceptions import CannotDetectErrorException


def run_example_program():
    e = Encoder()
    d = Decoder(coding_polynomial=e.coding_polynomial, k=e.k, t=e.r, gf_index=e.gf.index)

    message = "zaqwsxcderfvbgtyhnmjuik,ol.p;/zaqwsxedcrf"
    print('Message: ' + message)
    codeword = e.encode(message)
    print('Codeword: ' + str(codeword))
    decoded_message = d.decode(codeword, 'basic')
    print('Decoded message: ' + decoded_message[:len(message)])

    for i in range(1, 28):
        codeword.elements[i] = codeword.elements[i].multiplicative_inversion()
    print('27 errors occurred...')
    print(codeword)
    decoded_message = d.decode(codeword, 'basic')
    print('Decoded message: ' + decoded_message[:len(message)])


if __name__ == '__main__':
    run_example_program()
