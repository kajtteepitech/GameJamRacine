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
        self.player = pygame.image.load("assets/img/player_left.png")
        self.player = pygame.transform.scale(self.player, scale)

    def draw(self, screen):
        screen.blit(self.player, (self.x, self.y))

    def update(self, infoScreen):
        self.velX = 0
        
        if self.left_pressed and not self.right_pressed and self.x > 0:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed and self.x < infoScreen.current_w - self.player.get_width():
            self.velX = self.speed
        
        self.x += self.velX