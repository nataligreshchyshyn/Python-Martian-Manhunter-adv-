import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-2, 3) == 1
    assert Calculator.add(-2, -3) == -5
    assert Calculator.add('2', '3') == '23'
    with pytest.raises(TypeError):
        Calculator.add(2, '3')
        Calculator.add('2', '3')
        Calculator.add('2', 3)


def test_subtract():
    assert Calculator.subtract(2, 3) == -1
    assert Calculator.subtract(-2, 3) == -5
    assert Calculator.subtract(-2, -3) == 1
    assert Calculator.subtract(2, -3) == 5
    with pytest.raises(TypeError):
        Calculator.subtract(2, '3')
        Calculator.subtract('2', '3')
        Calculator.subtract('2', 3)


def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(-2, -3) == 6
    assert Calculator.multiply('2', 3) == '222'
    assert Calculator.multiply(2, '3') == '33'
    with pytest.raises(TypeError):
        Calculator.multiply('2', '3')
        Calculator.multiply(-2, '3')
        Calculator.multiply('2', 0)


def test_divide():
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(-6, 2) == -3
    assert Calculator.divide(-6, -2) == 3
    with pytest.raises(TypeError):
        Calculator.divide(6, '2')
        Calculator.divide('6', '2')
        Calculator.divide('6', 2)
    with pytest.raises(ValueError):
        Calculator.divide(6, 0)
        Calculator.divide('6', 0)
