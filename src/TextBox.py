import pygame

class TextBox:
    def __init__(self, text, color, x, y, font, size):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.font = font
        self.size = size

    def show(self, screen):
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.text, True, self.color)
        # Add black background behind text with a padding of 40 pixels on width and 20 on height
        pygame.draw.rect(screen, (45, 52, 54), ((self.x - text.get_width() // 2) - 40, (self.y - text.get_height() // 2) - 20, text.get_width() + 80, text.get_height() + 40))
        screen.blit(text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2))