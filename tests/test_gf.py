import pytest
from src.basics.exceptions import DivideByZeroException, AlphasFromDifferentField
from tests.config import alphas


@pytest.mark.parametrize("params", alphas)
def test_generate_first_n_alphas(params):
    a = params['a'].alpha_elements
    assert a == params['b']
