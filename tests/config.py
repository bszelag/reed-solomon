from src.basics.bit import Bit

from src.basics.gf import GF
from src.basics.polynomial import Polynomial
from src.encoder import Encoder
from src.decoder import Decoder


addition_params = [{'a': Bit(0), 'b': Bit(0), 'c': Bit(0)},
                   {'a': Bit(1), 'b': Bit(0), 'c': Bit(1)},
                   {'a': Bit(0), 'b': Bit(1), 'c': Bit(1)},
                   {'a': Bit(1), 'b': Bit(1), 'c': Bit(0)}]

subtraction_params = [{'a': Bit(0), 'b': Bit(0), 'c': Bit(0)},
                      {'a': Bit(1), 'b': Bit(0), 'c': Bit(1)},
                      {'a': Bit(0), 'b': Bit(1), 'c': Bit(1)},
                      {'a': Bit(1), 'b': Bit(1), 'c': Bit(0)}]

multiply_params = [{'a': Bit(0), 'b': Bit(0), 'c': Bit(0)},
                   {'a': Bit(1), 'b': Bit(0), 'c': Bit(0)},
                   {'a': Bit(0), 'b': Bit(1), 'c': Bit(0)},
                   {'a': Bit(1), 'b': Bit(1), 'c': Bit(1)}]

divide_params = [
    {'a': Bit(0), 'b': Bit(1), 'c': Bit(0)},
    {'a': Bit(1), 'b': Bit(1), 'c': Bit(1)}]

divide_params_exceptions = [{'a': Bit(0), 'b': Bit(0)},
                            {'a': Bit(1), 'b': Bit(0)}]

add_poly = [{'a': Polynomial([Bit(0), Bit(1), Bit(0), Bit(1), Bit(1), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(1), Bit(0), Bit(1), Bit(0), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(0), Bit(0), Bit(0), Bit(1), Bit(0)])},

            {'a': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)]),
             'b': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)])},

            {'a': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)]),
             'c': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)])},

            {'a': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)]),
             'b': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)]),
             'c': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)])},

            {'a': Polynomial([Bit(1), Bit(0)]),
             'b': Polynomial([Bit(1), Bit(0), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(1), Bit(1)])}]

# add_poly_with_alphas = [
#     {'a': Polynomial([Alpha(1, 1, 3), Alpha(2, 2, 3), Alpha(3, 4, 3)]),
#      'b': Polynomial([Alpha(4, 3, 3), Alpha(5, 6, 3), Alpha(6, 7, 3)]),
#      'c': Polynomial([Alpha(2, 2, 3), Alpha(3, 4, 3), Alpha(4, 3, 3)])}
# ]

add_alpha = [{'a': GF.Alpha(2, 2, 3), 'b': GF.Alpha(5, 6, 3), 'c': GF.Alpha(3, 4, 3)},
             {'a': GF.Alpha(3, 4, 3), 'b': GF.Alpha(6, 7, 3), 'c': GF.Alpha(4, 3, 3)},
             {'a': GF.Alpha(5, 6, 3), 'b': GF.Alpha(6, 7, 3), 'c': GF.Alpha(1, 1, 3)},
             {'a': GF.Alpha(7, 5, 3), 'b': GF.Alpha(5, 6, 3), 'c': GF.Alpha(4, 3, 3)},
             {'a': GF.Alpha(7, 5, 3), 'b': GF.Alpha(4, 3, 3), 'c': GF.Alpha(5, 6, 3)}]

alphas_multiplicative_inversions = [
    {'a': GF.Alpha(2, 2, 3), 'b': GF.Alpha(5, 6, 3)},
    {'a': GF.Alpha(3, 4, 3), 'b': GF.Alpha(4, 3, 3)},
    {'a': GF.Alpha(5, 6, 3), 'b': GF.Alpha(2, 2, 3)},
    {'a': GF.Alpha(7, 5, 3), 'b': GF.Alpha(0, -1, 3)},
    {'a': GF.Alpha(4, 3, 3), 'b': GF.Alpha(3, 4, 3)},
    {'a': GF.Alpha(1, 1, 3), 'b': GF.Alpha(6, 7, 3)},
    {'a': GF.Alpha(6, 7, 3), 'b': GF.Alpha(1, 1, 3)}
]

sub_poly = [{'a': Polynomial([Bit(0), Bit(1), Bit(0), Bit(1), Bit(1), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(1), Bit(0), Bit(1), Bit(0), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(0), Bit(0), Bit(0), Bit(1), Bit(0)])},

            {'a': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)]),
             'b': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)])},

            {'a': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(1), Bit(1)]),
             'c': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)])},

            {'a': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)]),
             'b': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)]),
             'c': Polynomial([Bit(0), Bit(0), Bit(0), Bit(0), Bit(0), Bit(0)])}]

mul_poly = [{'a': Polynomial([Bit(1)]),
             'b': Polynomial([Bit(1), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(1)])},

            {'a': Polynomial([Bit(1), Bit(1), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(0)]),
             'c': Polynomial([Bit(1), Bit(1), Bit(1), Bit(0)])},

            {'a': Polynomial([Bit(1), Bit(1), Bit(0), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(0), Bit(1), Bit(1), Bit(1)])}]

div_poly = [{'a': Polynomial([Bit(1), Bit(1), Bit(0), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(0), Bit(0)]),
             'd': Polynomial([Bit(1)])},

            {'a': Polynomial([Bit(1), Bit(1), Bit(0), Bit(0), Bit(1)]),
             'b': Polynomial([Bit(1), Bit(0), Bit(1)]),
             'c': Polynomial([Bit(1), Bit(1), Bit(1)]),
             'd': Polynomial([Bit(1), Bit(0)])}]

ge_poly = [{'a': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1)]),
            'b': Polynomial([Bit(1), Bit(1), Bit(1), Bit(0)])},
           {'a': Polynomial([Bit(1), Bit(1), Bit(1), Bit(0)]),
            'b': Polynomial([Bit(1), Bit(1), Bit(0), Bit(1)])},
           {'a': Polynomial([Bit(1), Bit(1), Bit(1), Bit(1), Bit(0), Bit(1)]),
            'b': Polynomial([Bit(1), Bit(1)])},
           {'a': Polynomial([Bit(1)]), 'b': Polynomial([Bit(0), Bit(0), Bit(1)])}]

alphas = [{
    'a': GF(generating_polynomial=Polynomial([Bit(1), Bit(0), Bit(1), Bit(1)])),
    'b': [GF.Alpha(-1, 0, 3),
          GF.Alpha(0, 1, 3),
          GF.Alpha(1, 2, 3),
          GF.Alpha(2, 4, 3),
          GF.Alpha(3, 3, 3),
          GF.Alpha(4, 6, 3),
          GF.Alpha(5, 7, 7),
          GF.Alpha(6, 5, 3)]
}]

test_messages = ["This is message for RS encoder.",
                 "lets find out why this is not working, ok"]
encoder = Encoder()
decoder = Decoder(coding_polynomial=encoder.coding_polynomial, k=encoder.k, t=encoder.r, gf_index=encoder.gf.index)

proper_codewords = [{'message': test_messages[0], 'codeword': encoder.encode(test_messages[0])},
                    {'message': test_messages[1], 'codeword': encoder.encode(test_messages[1])}]

codeword_able_to_fix = proper_codewords[0]['codeword']
for i in range(0, 26):
    codeword_able_to_fix.elements[i] = codeword_able_to_fix.elements[i].multiplicative_inversion()
codeword_with_error = [{'message': test_messages[0], 'codeword': codeword_able_to_fix}]

codeword_with_more_errors_than_could_be_fixed = proper_codewords[1]['codeword']
for i in range(0, 40):
    codeword_with_more_errors_than_could_be_fixed.elements[i] = codeword_with_more_errors_than_could_be_fixed.elements[i].multiplicative_inversion()
codeword_without_fix = [{'message': test_messages[1], 'codeword': codeword_with_more_errors_than_could_be_fixed}]
