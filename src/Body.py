import pygame

class Body:
    def __init__(self, x, y, scale):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.scale = scale
        self.sprites = {
            "body": [],
        }
        self.init_sprites()
        self.current_sprite = 0
        self.image = self.sprites["body"][self.current_sprite]
        self.image = pygame.transform.scale(self.image, scale)

    def init_sprites(self):
        self.sprites["body"].append(pygame.image.load("assets/img/brother/dead.png"))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))