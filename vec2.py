import math

class Vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, v):
		return Vec2(self.x + v.x, self.y + v.y)

	def __sub__(self, v):
		return Vec2(self.x - v.x, self.y - v.y)

	def __div__(self, n):
		return Vec2(self.x / n, self.y / n)

	def __mul__(self, n):
		return Vec2(self.x * n, self.y * n)

	def __eq__(self, v):
		if v.x == self.x and v.y == self.y:
			return Trune
		return False

	def len(self):
		return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
