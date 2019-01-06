import pytest
from tests.config import add_alpha


@pytest.mark.skip
@pytest.mark.parametrize("params", add_alpha)
def test_addition(params):
    result = params['a'] + params['b']
    print(result)
    assert result == params['c']
