#!/usr/bin/env python

import sys
import random
import pygame
from boid import *
from vec2 import *

w = 800
h = 600
numboids = 25 
crowd_dist = 20
close_dist = 200

def display_boid(screen, boid):
	pygame.draw.line(screen, (255.0, 255.0, 255.0), \
		(boid.pos.x, boid.pos.y), \
		(boid.pos.x + boid.vel.x, boid.pos.y + boid.vel.y), 1)

def main():
	boids = []
	run = True
	screen = pygame.display.set_mode((w, h))
	#screen = pygame.display.set_mode((w, h), pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE)

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

		move_boids(boids, close_dist, crowd_dist, w, h)
		
		for boid in boids:
			display_boid(screen, boid)

		pygame.display.flip()
		pygame.time.delay(10)

	pygame.quit()
	sys.exit(0)

if __name__ == "__main__":
	main()
