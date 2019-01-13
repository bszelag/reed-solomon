import pytest
from src.basics.exceptions import DivideByZeroException
from tests.config import add_poly, sub_poly, mul_poly, div_poly, ge_poly


@pytest.mark.parametrize("params", add_poly)
def test_addition(params):
    result = params['a'] + params['b']
    assert result == params['c']

#
# @pytest.mark.parametrize("params", add_poly_with_alphas)
# def test_addition(params):
#     result = params['a'] + params['b']
#     print(result)
#     for i in range(len(result.elements)):
#         print(str(i) + ': ' + str(result.elements[i]))
#         assert result.elements[i].value == params['c'].elements[i].value


@pytest.mark.parametrize("params", sub_poly)
def test_subtraction(params):
    result = params['a'] - params['b']
    assert result == params['c']


@pytest.mark.parametrize("params", mul_poly)
def test_multiplication(params):
    result = params['a'] * params['b']
    print(result)
    print(params['c'])
    assert result == params['c']


@pytest.mark.parametrize("params", div_poly)
def test_div(params):
    result = params['a'].__div__(params['b'])
    reminder = params['a'].__mod__(params['b'])
    assert result == params['c']
    assert reminder == params['d']


@pytest.mark.parametrize("params", ge_poly)
def test_ge(params):
    result = params['a'] >= params['b']
    assert result
