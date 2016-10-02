import random
from vec2 import *

class Boid:
	pos = Vec2(0.0, 0.0)
	vel = Vec2(0.0, 0.0)
	maxvel = 10.0

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
		if len(boids) < 1:
			return
		
		avg = Vec2(0.0, 0.0)
		for boid in boids:
			avg += boid.vel

		avg /= len(boids)
		
		self.vel += avg / 40.0

	def move_away(self, boids, mindist):
		numclose = 0
		dist = Vec2(0.0, 0.0)

		if len(boids) < 1:
			return
		
		for boid in boids:
			if self.distance(boid) < mindist:
				numclose += 1
				diff = self.pos - boid.pos

				if diff.x > 0.0:
					diff.x = mindist - diff.x	
				else:
					diff.x = -mindist - diff.x

				if diff.y > 0.0:
					diff.y = mindist - diff.y
				else:
					diff.y = -mindist - diff.y

				dist += diff
			
		if numclose == 0:
			return

		self.vel += (dist / 5.0)

	def move(self):
		if self.vel.len() > self.maxvel:
			self.vel = (self.vel.normalise() * self.maxvel)

		self.pos += self.vel 

def move_boids(boids, close_dist, crowd_dist, w, h):
	for boid in boids:
		close = []
		for other in boids:
			if boid == other:
				continue
			if boid.distance(other) < close_dist:
				close.append(other)

		boid.move_towards(close)
		boid.move_with(close)
		boid.move_away(close, crowd_dist)

		boid.move()
		stay_within_screen(boid, w, h)
	
def stay_within_screen(boid, w, h):
	border = 25
	if boid.pos.x < border and boid.vel.x < 0.0:
		boid.vel.x = abs(boid.vel.x * random.random())	
	if boid.pos.x > w - border and boid.vel.x > 0.0:
		boid.vel.x = -abs(boid.vel.x * random.random())	
	if boid.pos.y < border and boid.vel.y < 0.0:
		boid.vel.y = abs(boid.vel.y * random.random())
	if boid.pos.y > h - border and boid.vel.y > 0.0:
		boid.vel.y = -abs(boid.vel.y * random.random())
