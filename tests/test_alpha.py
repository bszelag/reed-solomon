import pytest
from tests.config import add_alpha, alphas_multiplicative_inversions


@pytest.mark.parametrize("params", add_alpha)
def test_addition(params):
    result = params['a'] + params['b']
    assert result == params['c']


# @pytest.mark.skip
@pytest.mark.parametrize("params", alphas_multiplicative_inversions)
def test_multiplicative_inversions(params):
    result = params['a'].multiplicative_inversion()
    print(result)
    print(params['b'])
    assert result == params['b']
