#!/usr/bin/env python3

import pygame

def street(screen):
	img = pygame.image.load("assets/scene2.jpg")
	img = pygame.transform.scale(img,(1920,1080))
	screen.blit(img, (0, 0))
	pygame.display.flip()
