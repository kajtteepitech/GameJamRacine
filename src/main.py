#!/usr/bin/env python3

import pygame
import pygame.freetype
import sys
from src.Button import Button
from src.Player import Player
from src.Brother import Brother
from src.Keys import Key
from src.TextBox import TextBox
from src.Body import Body
from src.Arouf import Arouf

class main_loop:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.infoScreen = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoScreen.current_w, self.infoScreen.current_h), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("Arial", 30)
        self.GAME_FONT = pygame.freetype.Font("assets/fonts/default.ttf", 30)
        self.score = 0
        self.game_over = False
        self.can_get_key = False
        self.found_body = False

        self.bg_img = pygame.image.load("assets/img/mainmenu.png")
        self.bg_img = pygame.transform.scale(self.bg_img, (self.infoScreen.current_w, self.infoScreen.current_h))

        self.pause_img = pygame.image.load("assets/img/pausemenu.jpg")
        self.pause_img = pygame.transform.scale(self.pause_img, (self.infoScreen.current_w, self.infoScreen.current_h))

        self.scene1 = pygame.image.load("assets/img/scene1.png")
        self.scene1 = pygame.transform.scale(self.scene1, (self.infoScreen.current_w, self.infoScreen.current_h))

        self.scene2 = pygame.image.load("assets/img/scene2.jpg")
        self.scene2 = pygame.transform.scale(self.scene2, (self.infoScreen.current_w, self.infoScreen.current_h))

        self.scene3 = pygame.image.load("assets/img/scene3.jpg")
        self.scene3 = pygame.transform.scale(self.scene3, (self.infoScreen.current_w, self.infoScreen.current_h))

        self.lvl10 = pygame.image.load("assets/img/Lvl10.jpg")

        self.lvl42 = pygame.image.load("assets/img/Lvl42.jpg")

        self.lvl50 = pygame.image.load("assets/img/Lvl50.jpg")

        self.current_scene = "MAIN_MENU"
        self.current_level = 0

        self.button_start = Button(
            "Start",
            (self.infoScreen.current_w * (3/4), 250),
            font=50,
            bg="navy",
        )
        self.button_quit = Button(
            "Quit",
            (self.infoScreen.current_w * (3/4), 350),
            font=50,
            bg="navy",
        )

        self.key = Key(self.infoScreen.current_w // 6, self.infoScreen.current_h - 150, (self.infoScreen.current_w // 25, self.infoScreen.current_h // 25))
        self.player = Player(self.infoScreen.current_w // 3, self.infoScreen.current_h - 380, (self.infoScreen.current_w // 7, self.infoScreen.current_h // 7 * 2.5))
        self.brother = Brother(self.infoScreen.current_w - 300, self.infoScreen.current_h - 380, (self.infoScreen.current_w // 7, self.infoScreen.current_h // 7 * 2.5))
        self.body = Body(self.infoScreen.current_w // 2, self.infoScreen.current_h - 300, (self.infoScreen.current_w // 7, self.infoScreen.current_h // 7 * 2.5))
        self.arouf = Arouf(self.infoScreen.current_w // 10, self.infoScreen.current_h - 380, (self.infoScreen.current_w // 7, self.infoScreen.current_h // 7 * 2.5))

        self.previous_scene = ""
        self.previous_music = ""

        self.brother_text = TextBox("What's up Tony! Are you ready to go seeing the Don? Go get my car keys real quick!", (255, 255, 255), self.infoScreen.current_w // 2, 75, "assets/fonts/default.ttf", 20)
        self.welcome_text = TextBox("Meet up with your brother Alfredo in the street", (255, 255, 255), self.infoScreen.current_w // 2, 75, "assets/fonts/default.ttf", 20)
        self.get_key_text = TextBox("Find and get the keys then join Alfredo.", (255, 255, 255), self.infoScreen.current_w // 2, 75, "assets/fonts/default.ttf", 20)
        self.brother_death_text = TextBox("Jesus Christ! My brother just died... He tells me to go see the Don. I need to find him.", (255, 255, 255), self.infoScreen.current_w // 2, 75, "assets/fonts/default.ttf", 20)
        self.arouf_text = TextBox("Wolla moi j'ai tue ton frr, je suis le plus beau de tous les rebeux! T'as pas une coca bien frais chacal?", (255, 255, 255), self.infoScreen.current_w // 2, 75, "assets/fonts/default.ttf", 20)

    def run(self):
        self.menumusic()
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            self.gameplayevents()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if self.player.x <= self.key.x + 150 and self.player.x >= self.key.x - 150 and not self.key.picked_up:
                    if event.key == pygame.K_e:
                        self.key.picked_up = True
                        self.current_level = 1

                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    if self.current_scene == "PAUSE_MENU":
                        self.current_scene = self.previous_scene
                        if self.current_scene != "MAIN_MENU" and pygame.key.get_pressed()[pygame.K_q]:
                            self.player.left_pressed = True
                        if self.current_scene != "MAIN_MENU" and pygame.key.get_pressed()[pygame.K_d]:
                            self.player.right_pressed = True
                        if self.previous_music == "GAME":
                            self.roommusic()
                        if self.previous_music == "MAIN_MENU":
                            self.menumusic()
                        if self.previous_music == "STREET":
                            self.streetmusic()
                        if self.previous_music == "FOREST":
                            self.forestmusic()
                    elif self.current_scene == "MAIN_MENU":
                        self.previous_scene = self.current_scene
                        self.previous_music = self.current_scene
                        self.current_scene = "PAUSE_MENU"
                        self.pausemusic()
                    elif self.current_scene != "MAIN_MENU":
                        self.player.left_pressed = False
                        self.player.right_pressed = False
                        self.previous_scene = self.current_scene
                        self.previous_music = self.current_scene
                        self.current_scene = "PAUSE_MENU"
                        self.pausemusic()
                    elif self.current_scene == "STREET":
                        self.previous_scene = self.current_scene
                        self.previous_music = self.current_scene
                        self.current_scene = "PAUSE_MENU"
                        self.pausemusic()
                    elif self.current_scene == "FOREST":
                        self.previous_scene = self.current_scene
                        self.previous_music = self.current_scene
                        self.current_scene = "PAUSE_MENU"
                        self.pausemusic()

                if self.current_scene != "MAIN_MENU" or self.current_scene != "PAUSE_MENU":
                    if event.key == pygame.K_q:
                        self.player.left_pressed = True
                    if event.key == pygame.K_d:
                        self.player.right_pressed = True
                    if event.key == pygame.K_r:
                        self.player.is_fighting = True
                        if self.arouf.x <= self.player.x + 150 and self.arouf.x >= self.player.x - 150:
                            self.arouf.health -= 25

            if event.type == pygame.KEYUP:
                if self.current_scene != "MAIN_MENU" or self.current_scene != "PAUSE_MENU":
                    if event.key == pygame.K_q:
                        self.player.left_pressed = False
                    if event.key == pygame.K_d:
                        self.player.right_pressed = False
                    if event.key == pygame.K_r:
                        self.player.is_fighting = False

            if (self.current_level == 0 and self.player.x >= self.infoScreen.current_w - 700 and self.current_scene == "STREET"):
                # self.player.right_pressed = False
                self.can_get_key = True
                if self.player.x >= self.infoScreen.current_w - 400:
                    self.player.right_pressed = False

            if (self.current_level == 0 and self.player.x >= 1470 and self.current_scene == "STREET"):
                self.player.right_pressed = False
            if (self.current_level == 1 and self.player.x <= 350 and self.current_scene == "STREET" and self.found_body and self.arouf.health > 0):
                self.player.left_pressed = False

            if self.button_start.click(event):
                self.current_scene = "GAME"
                self.roommusic()
            if self.button_quit.click(event):
                self.running = False
                sys.exit()

            if (self.current_level == 2 and self.current_scene == "FOREST" and self.found_body == False):
                self.found_body = True
            if (self.current_level == 1 and self.current_scene == "STREET"):
                self.current_scene = "LVL10"
                self.lvlupmusic()
            if (self.current_scene == "LVL10" and event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                self.current_scene = "STREET"
                self.streetmusic()
                self.current_level = 2
            if (self.current_scene == "LVL42" and event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                self.current_scene = "STREET"
                self.streetmusic()
                self.current_level = 3
            if (self.current_level == 2 and self.current_scene == "STREET" and self.found_body == True):
                self.current_scene = "LVL42"
                self.lvlupmusic()
            if (self.current_level == 4 and self.current_scene == "STREET"):
                self.current_scene = "LVL50"
                self.lvlupmusic()
            if (self.current_scene == "LVL50" and event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                self.current_scene = "STREET"
                self.streetmusic()
                self.current_level = 5


    def update(self):
        self.player.update(self.infoScreen)
        self.brother.update(self.infoScreen)
        self.arouf.update(self.infoScreen)

        if (self.player.x > self.infoScreen.current_w - 130 and self.current_scene == "GAME"):
            self.current_scene = "STREET"
            self.streetmusic()
            self.player.x = 50
        if (self.player.x < 0 and self.current_scene == "STREET"):
            self.current_scene = "GAME"
            self.roommusic()
            self.player.x = self.infoScreen.current_w - 200
        if (self.player.x > self.infoScreen.current_w - 130 and self.current_scene == "STREET"):
            self.current_scene = "FOREST"
            self.forestmusic()
            self.player.x = 50
        if (self.player.x < 0 and self.current_scene == "FOREST"):
            self.current_scene = "STREET"
            self.streetmusic()
            self.player.x = self.infoScreen.current_w - 200

    def gameplayevents(self):
        if (self.player.x > self.infoScreen.current_w - 200 and self.current_scene == "STREET"):
            text_surface, rect = self.GAME_FONT.render("Hello World!", (255, 255, 255))
            self.screen.blit(text_surface, (40, 250))

    def draw(self):
        self.screen.fill((255, 255, 255))

        if (self.current_level == 0 and self.current_scene == "GAME" and self.can_get_key == True):
            self.key.draw(self.screen, self.player)

        if self.current_scene == "MAIN_MENU":
            self.screen.blit(self.bg_img, (0, 0))
            self.button_start.show(self.screen)
            self.button_quit.show(self.screen)

        if self.current_scene == "GAME":
            self.screen.blit(self.scene1, (0, 0))
            self.player.draw(self.screen)
            if self.can_get_key:
                self.get_key_text.show(self.screen)
                self.key.draw(self.screen, self.player)
            elif self.current_level == 0:
                self.welcome_text.show(self.screen)
			
        if self.current_scene == "STREET":
            self.screen.blit(self.scene2, (0, 0))
            self.player.draw(self.screen)
            if self.current_level == 3 and self.found_body:
                if self.arouf.health > 0:
                    self.arouf.draw(self.screen)
                    self.arouf_text.show(self.screen)
                if self.arouf.health <= 0:
                    self.current_level = 4
            if self.current_level == 0:
                self.brother.draw(self.screen)
                if self.player.x > self.infoScreen.current_w - 700:
                    self.brother_text.show(self.screen)

        if self.current_scene == "FOREST":
            self.screen.blit(self.scene3, (0, 0))
            self.player.draw(self.screen)
            if self.current_level == 2 and self.found_body:
                self.body.draw(self.screen)
                self.brother_death_text.show(self.screen)

        if self.current_scene == "LVL10":
            self.screen.blit(self.lvl10, (0, 0))
        if self.current_scene == "LVL42":
            self.screen.blit(self.lvl42, (0, 0))
        if self.current_scene == "LVL50":
            self.screen.blit(self.lvl50, (0, 0))

        elif self.current_scene == "PAUSE_MENU":
            self.screen.blit(self.pause_img, (0, 0))
            self.button_quit.show(self.screen)

        pygame.display.flip()

    def lvlupmusic(self):
        pygame.mixer.music.load("assets/music/donachived.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
    def forestmusic(self):
        pygame.mixer.music.load("assets/music/forest.mp3")
        pygame.mixer.music.play(-1)
    def streetmusic(self):
        pygame.mixer.music.load("assets/music/street.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(5)
    def roommusic(self):
        pygame.mixer.music.load("assets/music/room.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
    def pausemusic(self):
        pygame.mixer.music.load("assets/music/pausemusic.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
    def menumusic(self):
        pygame.mixer.music.load("assets/music/mainmusic.wav")
        pygame.mixer.music.play(-1)

def main():
    pygame.init()
    pygame.display.set_caption("The Father")
    main_loop().run()

if __name__ == "__main__":
    main()