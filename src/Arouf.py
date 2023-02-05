import pygame

class Arouf:
    def __init__(self, x, y, scale):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.scale = scale
        self.sprites = {
            "idle_right": [],
        }
        self.init_sprites()
        self.current_sprite = 0
        self.image = self.sprites["idle_right"][self.current_sprite]
        self.image = pygame.transform.scale(self.image, scale)

    def init_sprites(self):
        self.sprites["idle_right"].append(pygame.image.load("assets/img/arouf/idle_right_1.png"))
        self.sprites["idle_right"].append(pygame.image.load("assets/img/arouf/idle_right_2.png"))
        self.sprites["idle_right"].append(pygame.image.load("assets/img/arouf/idle_right_3.png"))
        self.sprites["idle_right"].append(pygame.image.load("assets/img/arouf/idle_right_4.png"))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, infoScreen):
        self.current_sprite += 0.09

        if self.current_sprite >= len(self.sprites["idle_right"]):
            self.current_sprite = 0
        self.image = self.sprites["idle_right"][int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, self.scale)
