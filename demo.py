#!/usr/bin/env python

import sys
import random
import pygame
from boid import *
from vec2 import *

w = 800
h = 600
numboids = 10

boids = []

def render_boid(screen, boid):
	pass

def tick():
	pass	

def main():
	run = True
	screen = pygame.display.set_mode((w, h))

	for i in range(0, numboids):
		boids.append(Boid(Vec2(random.randint(0, w), random.randint(0, h))))

	while run:
		tick()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False

		screen.fill((0.0, 0.0, 0.0))

		for boid in boids:
			render_boid(screen, boid)

		pygame.display.flip()
		pygame.time.delay(10)

	pygame.quit()
	sys.exit(0)

if __name__ == "__main__":
	main()
