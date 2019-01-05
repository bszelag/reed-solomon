import pytest
from src.basics.exceptions import DivideByZeroException, AlphasFromDifferentField
from tests.config import basic_alphas


@pytest.mark.parametrize("params", basic_alphas)
def test_generate_first_n_alphas(params):
    alphas = params['a'].alpha_elements
    assert alphas == params['b']
