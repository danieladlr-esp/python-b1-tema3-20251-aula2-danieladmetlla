# geometry.py
import math


def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    try:
        return pow(side_length, 2)
    except TypeError:
        raise TypeError("side_length debe ser un número.")
    
def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    try:
        return base_length * height
    except TypeError:
        raise TypeError("base_length y height deben ser números.")
    except ValueError:
        raise ValueError("base_length y height deben ser valores positivos.")

def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    try:
        return (base_length * height) / 2
    except TypeError:
        raise TypeError("base_length y height deben ser números.")
    
def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    try:
        return math.pi * pow(radius, 2)
    except TypeError:
        raise TypeError("radius debe ser un número.")
    except ValueError:
        raise ValueError("radius debe ser un valor positivo.")
