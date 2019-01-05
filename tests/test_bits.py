import pytest
from src.basics.exceptions import DivideByZeroException
from tests.config import addition_params, subtraction_params, multiply_params, divide_params, \
    divide_params_exceptions


@pytest.mark.parametrize("params", addition_params)
def test_addition(params):
    assert params['a'] + params['b'] == params['c']


@pytest.mark.parametrize("params", subtraction_params)
def test_subtraction(params):
    assert params['a'] - params['b'] == params['c']


@pytest.mark.parametrize("params", multiply_params)
def test_multiplication(params):
    assert params['a'] * params['b'] == params['c']


@pytest.mark.parametrize("params", divide_params)
def test_divide(params):
    assert params['a'] / params['b'] == params['c']


@pytest.mark.parametrize("params", divide_params_exceptions)
def test_divide_by_zero(params):
    with pytest.raises(DivideByZeroException):
        params['a'] / params['b']
