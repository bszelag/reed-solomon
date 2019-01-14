from src.basics.bit import Bit

from src.basics.gf import GF
from src.basics.polynomial import Polynomial

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

add_poly_with_alphas = [
    {'a': Polynomial([GF.Alpha(1, 2, 3), GF.Alpha(2, 4, 3), GF.Alpha(3, 3, 3)]),
     'b': Polynomial([GF.Alpha(4, 6, 3), GF.Alpha(5, 7, 3), GF.Alpha(6, 5, 3)]),
     'c': Polynomial([GF.Alpha(2, 4, 3), GF.Alpha(3, 3, 3), GF.Alpha(4, 6, 3)])}
]

add_alpha = [{'a': GF.Alpha(1, 2, 3), 'b': GF.Alpha(0, 1, 3), 'c': GF.Alpha(3, 3, 3)},
             {'a': GF.Alpha(2, 4, 3), 'b': GF.Alpha(5, 7, 3), 'c': GF.Alpha(3, 3, 3)},
             {'a': GF.Alpha(4, 6, 3), 'b': GF.Alpha(6, 5, 3), 'c': GF.Alpha(3, 3, 3)},
             {'a': GF.Alpha(6, 5, 3), 'b': GF.Alpha(4, 6, 3), 'c': GF.Alpha(3, 3, 3)},
             {'a': GF.Alpha(3, 3, 3), 'b': GF.Alpha(6, 5, 3), 'c': GF.Alpha(4, 6, 3)}]

alphas_multiplicative_inversions = [
    {'a': GF.Alpha(1, 2, 3), 'b': GF.Alpha(6, 5, 3)},
    {'a': GF.Alpha(2, 4, 3), 'b': GF.Alpha(5, 7, 3)},
    {'a': GF.Alpha(4, 6, 3), 'b': GF.Alpha(3, 3, 3)},
    {'a': GF.Alpha(6, 5, 3), 'b': GF.Alpha(1, 2, 3)},
    {'a': GF.Alpha(3, 3, 3), 'b': GF.Alpha(4, 6, 3)},
    {'a': GF.Alpha(0, 1, 3), 'b': GF.Alpha(0, 1, 3)},
    {'a': GF.Alpha(5, 7, 3), 'b': GF.Alpha(2, 4, 3)}
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

test_messages = ["This is a message for RS encoder",
                 "This is a message for RS encoderThis is a message for RS encoder",
                 "This is a message for RS encoderThis is a message for RS encoderThis is a"]
