#!/usr/bin/env python3

import pygame

def appartement(screen):
	img = pygame.image.load("assets/scene1.png")
	img = pygame.transform.scale(img,(1920,1080))
	screen.blit(img, (0, 0))
	pygame.display.flip()
