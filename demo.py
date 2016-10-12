#!/usr/bin/env python

import sys
import random
import pygame
from boid import *
from vec2 import *

w = 800
h = 600
numboids = 50
crowd_dist = 30 
close_dist = 200

def display_boid(screen, boid, sprite, frame_num):
	#pygame.draw.line(screen, (255.0, 255.0, 255.0), \
	#	(boid.pos.x, boid.pos.y), \
	#	(boid.pos.x + boid.vel.x, boid.pos.y + boid.vel.y), 1)

	spriterect = sprite.get_rect()
	spriterect.x = boid.pos.x
	spriterect.y = boid.pos.y

	sprite.set_clip(pygame.Rect((48 * frame_num) % 384, 0, 48, 48))
	frame = sprite.subsurface(sprite.get_clip())

	screen.blit(frame, spriterect)

def main():
	boids = []
	run = True
	#screen = pygame.display.set_mode((w, h))
	screen = pygame.display.set_mode((w, h), pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE)

	background = pygame.image.load("resources/hauntedhouse.jpg").convert()
	backrect = background.get_rect()

	bird = pygame.image.load("resources/bat1.png").convert()
	bird.set_colorkey((173, 239, 255))
	frame_num = 0

	for i in range(0, numboids):
		boids.append(Boid(Vec2(random.randint(0, w), random.randint(0, h))))

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False

		screen.fill((127.0, 127.0, 127.0))
		screen.blit(background, backrect)

		move_boids(boids, close_dist, crowd_dist, w, h)
		
		for boid in boids:
			display_boid(screen, boid, bird, boids.index(boid) + frame_num)

		frame_num += 1
		
		pygame.display.flip()
		pygame.time.delay(10)

	pygame.quit()
	sys.exit(0)

if __name__ == "__main__":
	main()
