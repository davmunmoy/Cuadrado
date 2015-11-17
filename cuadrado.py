# cuadrado.py
class cuadrado:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def area(self):
		return self.x * self.y

	def perimeter(self, x, y):
		return (2 * self.x) + (2 * self.y)