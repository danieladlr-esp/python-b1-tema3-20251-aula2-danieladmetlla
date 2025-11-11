# geometry.py


def square_area(side_length: float) -> float:
    return side_length * side_length


def rectangle_area(base_length: float, height: float) -> float:
    return base_length * height


def triangle_area(base_length: float, height: float) -> float:
    return 0.5 * base_length * height


def circle_area(radius: float) -> float:
    return round(3.1416 * (radius * radius), 2)
