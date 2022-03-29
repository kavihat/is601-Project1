# pylint: disable=too-few-public-methods
"""Testing the opertions"""
from calculator.operation import Operation, Add, Subtract, Multiply, Divide


def test_operation_is_instance():
    """Testing the Calculator instantiation"""
    operation = Add(1,2)
    assert isinstance(operation, Operation)


def test_operation_addition():
    """Testing the Addition"""
    a = Add(6, 3)
    assert a.get_result() == 9


def test_operation_subtraction():
    """Testing the Subtraction"""
    s = Subtract(6, 3)
    assert s.get_result() == 3


def test_operation_multiplication():
    """Testing the Multiplication"""
    m = Multiply(6, 3)
    assert m.get_result() == 18


def test_operation_division():
    """Testing the Division"""
    d = Divide(6, 3)
    assert d.get_result() == 2
