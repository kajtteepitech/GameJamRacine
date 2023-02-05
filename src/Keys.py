import pygame

class Key:
    def __init__(self, x, y, scale):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.scale = scale
        self.sprites = {
            "key": [],
        }
        self.init_sprites()
        self.image = self.sprites["key"][self.current_sprite]
        self.image = pygame.transform.scale(self.image, scale)

    def init_sprites(self):
        self.sprites["key"].append(pygame.image.load("assets/img/key.png"))
        self.sprites["idle_left"].append(pygame.image.load("assets/img/key_selected.png"))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))