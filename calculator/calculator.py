"""importing operations for Calculator"""
from calculator.operation import Add, Subtract, Multiply, Divide


class Calculator:
    """importing operations for Calculator"""
    @staticmethod
    def add(value1, value2):
        """Testing the add"""
        obj_a = Add(value1, value2)
        return obj_a.get_result()

    @staticmethod
    def subtract(value1, value2):
        """performing subtract"""
        obj_a = Subtract(value1, value2)
        return obj_a.get_result()

    @staticmethod
    def multiply(value1, value2):
        """performing multiplication"""
        obj_a = Multiply(value1, value2)
        return obj_a.get_result()

    @staticmethod
    def divide(value1, value2):
        """performing division"""
        obj_a = Divide(value1, value2)
        output = obj_a.get_result()
        if not output:
            print("Cannot divide by 0")
        return output
