#!/usr/bin/env python3
import pygame
from pygame import mixer
import time
import sys
import random

class main_loop:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.infoScreen = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoScreen.current_w, self.infoScreen.current_h), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("Arial", 30)
        self.score = 0
        #self.player = player(self)
        #self.enemies = [enemy(self)]
        self.game_over = False

        self.img = pygame.image.load("src/mainmenu.png")
    def run(self):
        self.music()
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    sys.exit()
    def update(self):
        pass
    def draw(self):
        self.screen.blit(self.img, (0, 0))
        pygame.display.flip()
    def music(self):
        pygame.mixer.music.load("src/mainmusic.wav")
        pygame.mixer.music.play(-1)

def main():
    pygame.init()
    pygame.display.set_caption("Jam")
    main_loop().run()

if __name__ == "__main__":
    main()