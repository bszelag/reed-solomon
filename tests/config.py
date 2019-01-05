from src.basics.bit import Bit

from src.basics.gf import GF
from src.basics.alpha import Alpha
from src.basics.polynomial import Polynomial

# from src.encoder import Encoder
# from src.decoder import Decoder


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
    'b': [Alpha(0, 1, 3),
          Alpha(1, 2, 3),
          Alpha(2, 4, 3),
          Alpha(3, 3, 3),
          Alpha(4, 6, 3),
          Alpha(5, 7, 7),
          Alpha(6, 5, 3)]
}]