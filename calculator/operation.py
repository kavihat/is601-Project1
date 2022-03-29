# pylint: disable=too-few-public-methods
# pylint: disable=unnecessary-pass
"""importing the abstract class"""
from abc import ABC, abstractmethod


class Operation(ABC):
    """class operation for specifying operations"""

    @abstractmethod
    def get_result(self):
        """Creating an interface which cannot be modified but extended as needed"""
        pass    # pragma: no cover


class Add(Operation):
    """performing the addition"""

    def __init__(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2

    def get_result(self):
        return self.__value1 + self.__value2


class Subtract(Operation):
    """performing the subtraction"""

    def __init__(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2

    def get_result(self):
        return self.__value1 - self.__value2


class Multiply(Operation):
    """performing the multiplication"""

    def __init__(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2

    def get_result(self):
        return self.__value1 * self.__value2


class Divide(Operation):
    """performing the division"""

    def __init__(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2

    def get_result(self):
        if self.__value2 == 0:
            return None
        return self.__value1 // self.__value2
