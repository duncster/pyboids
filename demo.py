#!/usr/bin/env python

import sys
import random
import pygame
from boid import *
from vec2 import *

w = 800
h = 600
numboids = 50
crowd_dist = 20
close_dist = 200

def stay_within_screen(boid):
	border = 25
	if boid.pos.x < border and boid.vel.x < 0.0:
		boid.vel.x = -boid.vel.x * random.random()	
	if boid.pos.x > w - border and boid.vel.x > 0.0:
		boid.vel.x = -boid.vel.x * random.random()	
	if boid.pos.y < border and boid.vel.y < 0.0:
		boid.vel.y = -boid.vel.y * random.random()
	if boid.pos.y > h - border and boid.vel.y > 0.0:
		boid.vel.y = -boid.vel.y * random.random()

def display_boid(screen, boid):
	pygame.draw.line(screen, (255.0, 255.0, 255.0), \
		(boid.pos.x, boid.pos.y), \
		(boid.pos.x + boid.vel.x, boid.pos.y + boid.vel.y), 1)

def move_boids(boids):
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
		stay_within_screen(boid)
	

def main():
	boids = []
	run = True
	screen = pygame.display.set_mode((w, h))

	for i in range(0, numboids):
		boids.append(Boid(Vec2(random.randint(0, w), random.randint(0, h))))

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False

		screen.fill((0.0, 0.0, 0.0))

		move_boids(boids)
		
		for boid in boids:
			display_boid(screen, boid)

		pygame.display.flip()
		pygame.time.delay(10)

	pygame.quit()
	sys.exit(0)

if __name__ == "__main__":
	main()
