import random
from vec2 import *

class Boid:
	pos = Vec2(0.0, 0.0)
	vel = Vec2(0.0, 0.0)

	def __init__(self, pos):
		self.pos = pos
		self.vel.x = random.randint(1, 10) / 10.0
		self.vel.y = random.randint(1, 10) / 10.0

	def distance(self, boid):
		return((boid.pos - self.pos).len())

	def move_towards(self, boids):
		if len(boids) < 1:
			return

		avg = Vec2(0.0, 0.0)
		for boid in boids:
			avg += self.pos - boid.pos
		
		avg /= len(boids)

		self.vel -= avg / 100.0

	def move_with(self, boids):
		pass

	def move_away(self, boids, dist):
		pass

	def move(self):
		self.pos += self.vel
