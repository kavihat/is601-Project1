"""Testing the Calculator"""
from calculator.calculator import Calculator


def test_calculator_add():
    """Testing the addition"""
    assert Calculator.add(1, 1) == 2


def test_calculator_subtract():
    """Testing the subtraction"""
    assert Calculator.subtract(1, 1) == 0


def test_calculator_multiply():
    """Testing the multiply"""
    assert Calculator.multiply(1, 1) == 1


def test_calculator_divide():
    """Testing the divide"""
    assert Calculator.divide(1, 1) == 1


def test_calculator_divide_by_zero():
    """Testing exception case"""
    assert Calculator.divide(1,0) == None