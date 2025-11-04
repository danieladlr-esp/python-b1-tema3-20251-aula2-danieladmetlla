# arithmetic.py
import math

def power(base: float, exponent: float) -> float:
	try:
		return pow(base,exponent)
	except TypeError:
		raise TypeError("Bbase y exponent deben ser números.")

def square_root(num_1: float) -> float:
	
	try:
		return math.sqrt(num_1)
	except ValueError:
		raise ValueError("El número debe ser no negativo.")
	except TypeError:
		raise TypeError("num_1 debe ser un número.")
	
