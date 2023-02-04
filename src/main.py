#!/usr/bin/env python3

import pygame
import sys
from src.Button import Button

class main_loop:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(3, 3)
        self.infoScreen = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoScreen.current_w, self.infoScreen.current_h), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("Arial", 30)
        self.score = 0
        #self.player = player(self)
        #self.enemies = [enemy(self)]
        self.game_over = False

        self.img = pygame.image.load("assets/img/mainmenu.png")
        self.img = pygame.transform.scale(self.img, (self.infoScreen.current_w, self.infoScreen.current_h))

        self.current_scene = "MAIN_MENU"

        self.button_start = Button(
            "Start",
            (self.infoScreen.current_w * (3/4), 250),
            font=50,
            bg="navy",
        )

        self.player_x = self.infoScreen.current_w // 2
        self.player_y = self.infoScreen.current_h // 2

        self.player = pygame.image.load("assets/img/player_left.png")
        # Scale the image keeping the aspect ratio
        self.player = pygame.transform.scale(self.player, (self.infoScreen.current_w // 10, self.infoScreen.current_h // 10 * 2.5))

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
                pressed = pygame.key.get_pressed()
                
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    sys.exit()

                if event.key == pygame.K_q:
                    self.player_x -= 1

                if event.key == pygame.K_d:
                    self.player_x += 1
            
            if self.button_start.click(event):
                self.current_scene = "GAME"

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.current_scene == "MAIN_MENU":
            self.screen.blit(self.img, (0, 0))
            self.button_start.show(self.screen)

        if self.current_scene == "GAME":
            self.screen.blit(self.player, (self.player_x, self.player_y))

        pygame.display.flip()
    def music(self):
        pygame.mixer.music.load("assets/music/mainmusic.wav")
        pygame.mixer.music.play(-1)

def main():
    pygame.init()
    pygame.display.set_caption("The Father")
    main_loop().run()

if __name__ == "__main__":
    main()