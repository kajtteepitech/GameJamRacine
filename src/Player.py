import pygame

class Player:
    def __init__(self, x, y, scale):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.left_pressed = False
        self.right_pressed = False
        self.speed = 6
        self.scale = scale
        self.last_direction = "right"
        self.is_fighting = False

        self.sprites = {
            "left": [],
            "right": [],
            "idle_left": [],
            "idle_right": [],
            "fight_left": [],
            "fight_right": []
        }
        self.init_sprites()
        self.current_sprite = 0
        self.image = self.sprites["idle_right"][self.current_sprite]
        self.image = pygame.transform.scale(self.image, scale)

    def init_sprites(self):
        self.sprites["left"].append(pygame.image.load("assets/img/player/run_left_1.png"))
        self.sprites["left"].append(pygame.image.load("assets/img/player/run_left_2.png"))
        self.sprites["left"].append(pygame.image.load("assets/img/player/run_left_3.png"))
        self.sprites["left"].append(pygame.image.load("assets/img/player/run_left_4.png"))
        self.sprites["right"].append(pygame.image.load("assets/img/player/run_right_1.png"))
        self.sprites["right"].append(pygame.image.load("assets/img/player/run_right_2.png"))
        self.sprites["right"].append(pygame.image.load("assets/img/player/run_right_3.png"))
        self.sprites["right"].append(pygame.image.load("assets/img/player/run_right_4.png"))
        self.sprites["idle_left"].append(pygame.image.load("assets/img/player/idle_left_1.png"))
        self.sprites["idle_left"].append(pygame.image.load("assets/img/player/idle_left_2.png"))
        self.sprites["idle_left"].append(pygame.image.load("assets/img/player/idle_left_3.png"))
        self.sprites["idle_left"].append(pygame.image.load("assets/img/player/idle_left_4.png"))
        self.sprites["idle_right"].append(pygame.image.load("assets/img/player/idle_right_1.png"))
        self.sprites["idle_right"].append(pygame.image.load("assets/img/player/idle_right_2.png"))
        self.sprites["idle_right"].append(pygame.image.load("assets/img/player/idle_right_3.png"))
        self.sprites["idle_right"].append(pygame.image.load("assets/img/player/idle_right_4.png"))
        self.sprites["fight_left"].append(pygame.image.load("assets/img/player/fight_left_1.png"))
        self.sprites["fight_left"].append(pygame.image.load("assets/img/player/fight_left_2.png"))
        self.sprites["fight_left"].append(pygame.image.load("assets/img/player/fight_left_3.png"))
        self.sprites["fight_left"].append(pygame.image.load("assets/img/player/fight_left_4.png"))
        self.sprites["fight_right"].append(pygame.image.load("assets/img/player/fight_right_1.png"))
        self.sprites["fight_right"].append(pygame.image.load("assets/img/player/fight_right_2.png"))
        self.sprites["fight_right"].append(pygame.image.load("assets/img/player/fight_right_3.png"))
        self.sprites["fight_right"].append(pygame.image.load("assets/img/player/fight_right_4.png"))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, infoScreen):
        self.velX = 0
        
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        
        self.x += self.velX

        if self.left_pressed:
            self.current_sprite += 0.09

            if self.current_sprite >= len(self.sprites["left"]):
                self.current_sprite = 0

            self.image = self.sprites["left"][int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, self.scale)
            self.last_direction = "left"

        if self.right_pressed:
            self.current_sprite += 0.09

            if self.current_sprite >= len(self.sprites["right"]):
                self.current_sprite = 0

            self.image = self.sprites["right"][int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, self.scale)
            self.last_direction = "right"

        if not self.right_pressed and not self.left_pressed:
            if self.last_direction == "right":
                self.current_sprite += 0.09

                if self.current_sprite >= len(self.sprites["idle_right"]):
                    self.current_sprite = 0

                self.image = self.sprites["idle_right"][int(self.current_sprite)]
                self.image = pygame.transform.scale(self.image, self.scale)
            else:
                self.current_sprite += 0.09

                if self.current_sprite >= len(self.sprites["idle_left"]):
                    self.current_sprite = 0

                self.image = self.sprites["idle_left"][int(self.current_sprite)]
                self.image = pygame.transform.scale(self.image, self.scale)
        
        if self.is_fighting:
            if self.last_direction == "right":
                self.current_sprite += 0.09

                if self.current_sprite >= len(self.sprites["fight_right"]):
                    self.current_sprite = 0

                self.image = self.sprites["fight_right"][int(self.current_sprite)]
                self.image = pygame.transform.scale(self.image, self.scale)
            else:
                self.current_sprite += 0.09

                if self.current_sprite >= len(self.sprites["fight_left"]):
                    self.current_sprite = 0

                self.image = self.sprites["fight_left"][int(self.current_sprite)]
                self.image = pygame.transform.scale(self.image, self.scale)
