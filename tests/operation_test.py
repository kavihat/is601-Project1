# pylint: disable=too-few-public-methods
"""Testing the opertions"""
from calculator.operation import Operation, Add, Subtract, Multiply, Divide


def test_operation_is_instance():
    """Testing the Calculator instantiation"""
    operation = Add(1,2)
    assert isinstance(operation, Operation)


def test_operation_addition():
    """Testing the Addition"""
    obj_a = Add(6, 3)
    assert obj_a.get_result() == 9


def test_operation_subtraction():
    """Testing the Subtraction"""
    obj_s = Subtract(6, 3)
    assert obj_s.get_result() == 3


def test_operation_multiplication():
    """Testing the Multiplication"""
    obj_m = Multiply(6, 3)
    assert obj_m.get_result() == 18


def test_operation_division():
    """Testing the Division"""
    obj_d = Divide(6, 3)
    assert obj_d.get_result() == 2

def test_operation_division_by_zero():
    """Testing the Division"""
    obj_d = Divide(6, 0)
    assert obj_d.get_result() is None