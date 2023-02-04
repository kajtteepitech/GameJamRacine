#!/usr/bin/env python3

import pygame

def forest(screen):
	img = pygame.image.load("assets/scene3.jpg")
	img = pygame.transform.scale(img,(1920,1080))
	screen.blit(img, (0, 0))
	pygame.display.flip()
