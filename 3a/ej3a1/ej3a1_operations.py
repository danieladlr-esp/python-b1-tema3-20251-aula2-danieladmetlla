# archivo ej3a1_operations.py


def add(num_1: float, num_2: float) -> float:
    try:
        return num_1 + num_2
    except TypeError:
        raise TypeError("Error: Both parameters must be numbers.")


def subtract(num_1: float, num_2: float) -> float:
    try:
        return num_1 - num_2
    except TypeError:
        raise TypeError("Error: Both parameters must be numbers.")


def multiply(num_1: float, num_2: float) -> float:
    try:
        return num_1 * num_2
    except TypeError:
        raise TypeError("Error: Both parameters must be numbers.")


def divide(num_1: float, num_2: float) -> float:
    try:
        return num_1 / num_2
    except TypeError:
        raise TypeError("Error: Both parameters must be numbers.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
