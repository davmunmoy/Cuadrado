# cuadrado.py
class cuadrado:
	def __init__(self, x, y):
		"""Funcion init de la clase cuadrado"""
		self.x = x
		self.y = y

	def area(self):
		"""Esta funcion calcula el area de un cuadrado"""
		return self.x * self.y

	def perimeter(self, x, y):
		"""Esta funcion calcula el perimetro de un cuadrado"""
		return (2 * self.x) + (2 * self.y)